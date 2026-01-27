import os
import shared
import mcell as m

from parameters import *
from subsystem import *
from geometry import *
MODEL_PATH = os.path.dirname(os.path.abspath(__file__))

class Namespace:
    pass

vesicles = Namespace()

# Bind all global sensor_*_site_* objects to vesicles.*
global_copy = list(globals().items())
for name, obj in global_copy:
    if "_site_" in name and (name.startswith("sensor_") or name.startswith("sensor_Y_")):
        setattr(vesicles, name, obj)


# Bind all global sensor_*_sites_all objects to vesicles.*
for name, obj in global_copy:
    if name.endswith("_sites_all") and (name.startswith("sensor_") or name.startswith("sensor_Y_")):
        setattr(vesicles, name, obj)

# Automatically group all sensors into dictionaries
##############################  RL
SENSOR_PRESENT = {
    0:1,  1:1,  2:1,  3:1,  4:1,  5:1,  6:1,  7:1,  8:1,  9:1,
    10:1, 11:1, 12:1, 13:1, 14:1, 15:1, 16:1, 17:1,

    18:0, 19:0, 20:0, 21:0, 22:0, 23:0,

    24:1, 25:0, 26:1, 27:0, 28:0, 29:1, 30:0, 31:1, 32:0, 33:0,
    34:1, 35:0, 36:1, 37:0, 38:1, 39:0, 40:1, 41:0, 42:0, 43:1,
    44:0, 45:1, 46:0, 47:0, 48:1, 49:0, 50:1, 51:0
}

SENSOR_Y_PRESENT = {
    0:0, 1:0, 2:0, 3:0, 4:0, 5:0,
    6:1, 7:1, 8:1, 9:1,
    10:0, 11:0, 12:0, 13:0, 14:0, 15:0,
    16:1, 17:1, 18:1, 19:1, 20:1, 21:1, 22:1, 23:1,
    24:1, 25:1, 26:1, 27:1,
    28:0, 29:0,
    30:1, 31:1,
    32:0, 33:0, 34:0, 35:0
}

# Surface Classes

endcaps_Material.surface_class = absorb_all_calcium_ions
sensors = {}
sensors_Y = {}

for name, obj in list(globals().items()):

    # Normal syt1 sensors: sensor_AZ_VES_site_ID
    if name.startswith("sensor_") and "_site_" in name and not name.startswith("sensor_Y_"):
        parts = name.split("_")
        if len(parts) == 5 and parts[3] == "site":
            az = int(parts[1])
            ves = int(parts[2])
            sensors.setdefault((az, ves), []).append(name)

    # Y sensors: sensor_Y_AZ_VES_site_ID
    elif name.startswith("sensor_Y_") and "_site_" in name:
        parts = name.split("_")
        if len(parts) == 6 and parts[4] == "site":
            az = int(parts[2])
            ves = int(parts[3])
            sensors_Y.setdefault((az, ves), []).append(name)


for (az, ves), site_list in sensors.items():
    for name in site_list:
        sensor_obj = globals()[name]
        initial_list_name = f"{name}_initial_surface_releases"

        site_id = int(name.split("_")[-1])  
        number_to_release = SENSOR_PRESENT[site_id]

        globals()[initial_list_name] = [
            m.InitialSurfaceRelease(
                complex = unbound_sensor.inst(orientation=m.Orientation.UP),
                number_to_release = number_to_release
            )
        ]

        sensor_obj.initial_surface_releases = globals()[initial_list_name]
        setattr(vesicles, name, sensor_obj)

for (az, ves), site_list in sensors_Y.items():
    for name in site_list:
        sensor_obj = globals()[name]
        initial_list_name = f"{name}_initial_surface_releases"

        site_id = int(name.split("_")[-1])
        number_to_release = SENSOR_Y_PRESENT[site_id]

        globals()[initial_list_name] = [
            m.InitialSurfaceRelease(
                complex = unbound_sensor_Y.inst(orientation=m.Orientation.UP),
                number_to_release = number_to_release
            )
        ]

        sensor_obj.initial_surface_releases = globals()[initial_list_name]
        setattr(vesicles, name, sensor_obj)

# ---- compartments assignment ----

buffer_release1 = m.ReleaseSite(
    name = 'buffer_release1',
    complex = unbound_fixed_buffer.inst(),
    region = buffer_box,
    concentration = 1.0e-04  # 100 µM
)

# ================================
# CALCIUM CHANNEL INSTANTIATION
# ================================
########################### RL
# (AZ index, channel index) → (x, y)
CHANNEL_COORDS = {
    (1,1): (-0.561,  0.292),
    (1,2): (-0.599,  0.292),
    (1,3): (-0.561,  0.260),
    (1,4): (-0.599,  0.260),

    (2,1): ( 0.019,  0.292),
    (2,2): (-0.019,  0.292),
    (2,3): ( 0.019,  0.260),
    (2,4): (-0.019,  0.260),

    (3,1): ( 0.599,  0.292),
    (3,2): ( 0.561,  0.292),
    (3,3): ( 0.599,  0.260),
    (3,4): ( 0.561,  0.260),

    (4,1): (-0.561, -0.260),
    (4,2): (-0.599, -0.260),
    (4,3): (-0.561, -0.292),
    (4,4): (-0.599, -0.292),

    (5,1): ( 0.019, -0.260),
    (5,2): (-0.019, -0.260),
    (5,3): ( 0.019, -0.292),
    (5,4): (-0.019, -0.292),

    (6,1): ( 0.599, -0.260),
    (6,2): ( 0.561, -0.260),
    (6,3): ( 0.599, -0.292),
    (6,4): ( 0.561, -0.292),
}

Z_COORD = 0.00075


molecule_list_channel_release_site = []

for az in range(1, 7):       # Active zones 1…6
    for ch in range(1, 5):   # Channels 1…4
        cname = f"closed_channel_{az}_1_{ch}"
        channel_obj = globals()[cname]   # get the geometry object by name

        x, y = CHANNEL_COORDS[(az, ch)]
        loc = [x, y, Z_COORD]

        molecule_list_channel_release_site.append(
            m.MoleculeReleaseInfo(
                complex = channel_obj.inst(orientation=m.Orientation.DOWN),
                location = loc
            )
        )


channel_release_site = m.ReleaseSite(
    name = 'channel_release_site',
    molecule_list = molecule_list_channel_release_site,
    site_diameter = 1.0e-02
)

# ==========================================
# SK CHANNEL OFFSETS (per AZ, per channel)
# ==========================================

SK_OFFSETS = {
    (1,1): (0.020,  0.0015),  (1,2): (-0.020,  0.0015),  (1,3): (0.020, -0.0015),  (1,4): (-0.020, -0.0015),
    (2,1): (0.020,  0.0015),  (2,2): (-0.020,  0.0015),  (2,3): (0.020, -0.0015),  (2,4): (-0.020, -0.0015),
    (3,1): (0.020,  0.0015),  (3,2): (-0.020,  0.0015),  (3,3): (0.020, -0.0015),  (3,4): (-0.020, -0.0015),
    (4,1): (0.020,  0.0015),  (4,2): (-0.020,  0.0015),  (4,3): (0.020, -0.0015),  (4,4): (-0.020, -0.0015),
    (5,1): (0.020,  0.0015),  (5,2): (-0.020,  0.0015),  (5,3): (0.020, -0.0015),  (5,4): (-0.020, -0.0015),
    (6,1): (0.020,  0.0015),  (6,2): (-0.020,  0.0015),  (6,3): (0.020, -0.0015),  (6,4): (-0.020, -0.0015),
}

# ==========================================
# SK CHANNEL INSTANTIATION
# ==========================================

molecule_list_sk_release_site = []

for az in range(1, 7):       # Active zones 1..6
    for ch in range(1, 5):   # Channels 1..4

        sk_name = f"closed_SK_{az}_1_{ch}"
        sk_obj  = globals()[sk_name]

        # Base Ca-channel coordinate
        base_x, base_y = CHANNEL_COORDS[(az, ch)]

        # Apply SK-specific offset
        dx, dy = SK_OFFSETS[(az, ch)]
        x = base_x + dx
        y = base_y + dy

        # Final coordinate
        loc = [x, y, Z_COORD]

        molecule_list_sk_release_site.append(
            m.MoleculeReleaseInfo(
                complex = sk_obj.inst(orientation=m.Orientation.DOWN),
                location = loc
            )
        )

sk_channel_release_site = m.ReleaseSite(
    name = 'sk_channel_release_site',
    molecule_list = molecule_list_sk_release_site,
    site_diameter = 1.0e-2
)


# ---- create instantiation object and add components ----

instantiation = m.Instantiation()
instantiation.add_geometry_object(endcaps)
instantiation.add_geometry_object(main_membrane)
instantiation.add_geometry_object(sensor_1_1)
instantiation.add_geometry_object(sensor_1_2)
instantiation.add_geometry_object(sensor_2_1)
instantiation.add_geometry_object(sensor_2_2)
instantiation.add_geometry_object(sensor_3_1)
instantiation.add_geometry_object(sensor_3_2)
instantiation.add_geometry_object(sensor_4_1)
instantiation.add_geometry_object(sensor_4_2)
instantiation.add_geometry_object(sensor_5_1)
instantiation.add_geometry_object(sensor_5_2)
instantiation.add_geometry_object(sensor_6_1)
instantiation.add_geometry_object(sensor_6_2)
instantiation.add_geometry_object(vesicle_1_1)
instantiation.add_geometry_object(vesicle_1_2)
instantiation.add_geometry_object(vesicle_2_1)
instantiation.add_geometry_object(vesicle_2_2)
instantiation.add_geometry_object(vesicle_3_1)
instantiation.add_geometry_object(vesicle_3_2)
instantiation.add_geometry_object(vesicle_4_1)
instantiation.add_geometry_object(vesicle_4_2)
instantiation.add_geometry_object(vesicle_5_1)
instantiation.add_geometry_object(vesicle_5_2)
instantiation.add_geometry_object(vesicle_6_1)
instantiation.add_geometry_object(vesicle_6_2)
instantiation.add_geometry_object(sensor_Y_1_1)
instantiation.add_geometry_object(sensor_Y_1_2)
instantiation.add_geometry_object(sensor_Y_2_1)
instantiation.add_geometry_object(sensor_Y_2_2)
instantiation.add_geometry_object(sensor_Y_3_1)
instantiation.add_geometry_object(sensor_Y_3_2)
instantiation.add_geometry_object(sensor_Y_4_1)
instantiation.add_geometry_object(sensor_Y_4_2)
instantiation.add_geometry_object(sensor_Y_5_1)
instantiation.add_geometry_object(sensor_Y_5_2)
instantiation.add_geometry_object(sensor_Y_6_1)
instantiation.add_geometry_object(sensor_Y_6_2)
instantiation.add_geometry_object(buffer_box)
instantiation.add_release_site(buffer_release1)
instantiation.add_release_site(channel_release_site)
instantiation.add_release_site(sk_channel_release_site)

