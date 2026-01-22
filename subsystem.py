# WARNING: This is an automatically generated file and will be overwritten
#          by CellBlender on the next model export.

import os
import shared
import mcell as m
import parameters

from parameters import *

# ---- subsystem ----

MODEL_PATH = os.path.dirname(os.path.abspath(__file__))


# ============================
# CALCIUM SPECIES
# ============================

CALCIUM_DIFFUSION = 6.0e-06

for az in range(1,7):
    for ch in range(1,5):
        for ap in range(1,5):  # or dynamic
            name = f"ca_{az}_1_{ch}_{ap}"
            globals()[name] = m.Species(name=name, diffusion_constant_3d=CALCIUM_DIFFUSION)


# =========================================================
# SURFACE PROPERTIES FOR ALL CALCIUM SPECIES
# (transparent + absorptive)
# =========================================================
transparent_properties = []
absorptive_properties = []

uid = 1  
for az in range(1, 7):
    for ch in range(1, 5):
        for ap in range(1, 5):
            ca = globals()[f"ca_{az}_1_{ch}_{ap}"]
            sp_t = m.SurfaceProperty(
                type = m.SurfacePropertyType.TRANSPARENT,
                affected_complex_pattern = ca.inst()
            )
            property_name_t = f"surface_class_transparent_ca_{az}_1_{ch}_{ap}_{uid}"
            globals()[property_name_t] = sp_t
            transparent_properties.append(sp_t)
            # -----------------------------
            # ABSORPTIVE surface property
            # -----------------------------
            sp_a = m.SurfaceProperty(
                type = m.SurfacePropertyType.ABSORPTIVE,
                affected_complex_pattern = ca.inst()
            )
            property_name_a = f"surface_class_absorptive_ca_{az}_1_{ch}_{ap}_{uid}"
            globals()[property_name_a] = sp_a
            absorptive_properties.append(sp_a)
            uid += 1


# ==========================================
# Combine into SurfaceClasses 
# ==========================================

transparent_to_all_diffusing_molecules = m.SurfaceClass(
    name = 'transparent_to_all_diffusing_molecules',
    properties = transparent_properties
)

absorb_all_calcium_ions = m.SurfaceClass(
    name = 'absorb_all_calcium_ions',
    properties = absorptive_properties
)

# ============================
# Unbound Sensors (syt1 and syt7)
# ============================
unbound_sensor = m.Species(
    name = 'unbound_sensor',
    diffusion_constant_2d = 0
)

unbound_sensor_Y = m.Species(
    name = 'unbound_sensor_Y',
    diffusion_constant_2d = 0
)
# ============================
# Unbound fixed buffers
# ============================
unbound_fixed_buffer = m.Species(
    name = 'unbound_fixed_buffer',
    diffusion_constant_3d = 0
)


# ============================================================
# SURFACE CLASSES FOR ALL CALCIUM SPECIES
# ============================================================

transparent_props = []
absorptive_props = []

for az in range(1, 7):
    for ch in range(1, 5):
        for ap in range(1, 5):

            ca = globals()[f"ca_{az}_1_{ch}_{ap}"]

            # --- Transparent property ---
            transparent_props.append(
                m.SurfaceProperty(
                    type = m.SurfacePropertyType.TRANSPARENT,
                    affected_complex_pattern = ca.inst(orientation=m.Orientation.DOWN)
                )
            )

            # --- Absorptive property ---
            absorptive_props.append(
                m.SurfaceProperty(
                    type = m.SurfacePropertyType.ABSORPTIVE,
                    affected_complex_pattern = ca.inst(orientation=m.Orientation.DOWN)
                )
            )

# Create the SurfaceClass objects
transparent_to_all_diffusing_molecules = m.SurfaceClass(
    name = "transparent_to_all_diffusing_molecules",
    properties = transparent_props
)

absorb_all_calcium_ions = m.SurfaceClass(
    name = "absorb_all_calcium_ions",
    properties = absorptive_props
)


#============================
###   Reactions ==============
# ============================
# ============================


# ============================
# CHANNEL STATES (2D, immobile)
# ============================
for az in range(1, 7):          # Active zones 1..6
    for ch in range(1, 5):      # Channels 1..4
        # ---- Closed ----
        name = f"closed_channel_{az}_1_{ch}"
        globals()[name] = m.Species(
            name=name,
            diffusion_constant_2d=0
        )
        # ---- Closed2 ----
        name = f"closed2_channel_{az}_1_{ch}"
        globals()[name] = m.Species(
            name=name,
            diffusion_constant_2d=0
        )
        # ---- Closed3 ----
        name = f"closed3_channel_{az}_1_{ch}"
        globals()[name] = m.Species(
            name=name,
            diffusion_constant_2d=0
        )
        # ---- Open1 ----
        name = f"open1_channel_{az}_1_{ch}"
        globals()[name] = m.Species(
            name=name,
            diffusion_constant_2d=0
        )
        # ---- Open2 ----
        name = f"open2_channel_{az}_1_{ch}"
        globals()[name] = m.Species(
            name=name,
            diffusion_constant_2d=0
        )

# ============================
# Potassium channel (SK) States 
# ============================

for az in range(1,7):
    for ch in range(1,5):

        globals()[f"closed_SK_{az}_1_{ch}"] = m.Species(
            name=f"closed_SK_{az}_1_{ch}",
            diffusion_constant_2d=0,
        )
        globals()[f"closed2_SK_{az}_1_{ch}"] = m.Species(
            name=f"closed2_SK_{az}_1_{ch}",
            diffusion_constant_2d=0,
        )
        globals()[f"closed3_SK_{az}_1_{ch}"] = m.Species(
            name=f"closed3_SK_{az}_1_{ch}",
            diffusion_constant_2d=0,
        )
        globals()[f"closed4_SK_{az}_1_{ch}"] = m.Species(
            name=f"closed4_SK_{az}_1_{ch}",
            diffusion_constant_2d=0,
        )
        globals()[f"open1_SK_{az}_1_{ch}"] = m.Species(
            name=f"open1_SK_{az}_1_{ch}",
            diffusion_constant_2d=0,
        )
        globals()[f"open2_SK_{az}_1_{ch}"] = m.Species(
            name=f"open2_SK_{az}_1_{ch}",
            diffusion_constant_2d=0,
        )

# ==========================================
# BOUND SENSORS (Syt1 and Syt7)
# ==========================================

for az in range(1,7):
    for ch in range(1,5):
        for ap in range(1,5):
            # -------- Syt1-bound sensor --------
            bs_name = f"bound_sensor_{az}_1_{ch}_{ap}"
            globals()[bs_name] = m.Species(
                name = bs_name,
                diffusion_constant_2d = 0
            )
            # -------- Syt7-bound sensor_Y --------
            bY_name = f"bound_sensor_Y_{az}_1_{ch}_{ap}"
            globals()[bY_name] = m.Species(
                name = bY_name,
                diffusion_constant_2d = 0
            )
# ==========================================
# BOUND FIXED BUFFERS
# ==========================================

for az in range(1,7):
    for ch in range(1,5):
        for ap in range(1,5):
            bf_name = f"bound_fixed_buffer_{az}_1_{ch}_{ap}"
            globals()[bf_name] = m.Species(
                name = bf_name,
                diffusion_constant_3d = 0
            )

# ===============================
# GATING TRANSITION REACTIONS
# ===============================

gating_reactions = []
release_reactions = []

for az in range(1, 7):          # 1..6 active zones
    for ch in range(1, 5):      # 1..4 channels

        closed  = globals()[f"closed_channel_{az}_1_{ch}"]
        closed2 = globals()[f"closed2_channel_{az}_1_{ch}"]
        closed3 = globals()[f"closed3_channel_{az}_1_{ch}"]
        open1   = globals()[f"open1_channel_{az}_1_{ch}"]
        open2   = globals()[f"open2_channel_{az}_1_{ch}"]

        # ============================================
        # GATING TRANSITIONS
        # ============================================

        gating_reactions.append(m.ReactionRule(
            name = f"closed_to_closed2_{az}_{ch}",
            reactants = [closed.inst(orientation=m.Orientation.DOWN)],
            products  = [closed2.inst(orientation=m.Orientation.DOWN)],
            variable_rate = parameters.ac1c2
        ))

        gating_reactions.append(m.ReactionRule(
            name = f"closed2_to_closed_{az}_{ch}",
            reactants = [closed2.inst(orientation=m.Orientation.DOWN)],
            products  = [closed.inst(orientation=m.Orientation.DOWN)],
            variable_rate = parameters.bc2c1
        ))

        gating_reactions.append(m.ReactionRule(
            name = f"closed2_to_closed3_{az}_{ch}",
            reactants = [closed2.inst(orientation=m.Orientation.DOWN)],
            products  = [closed3.inst(orientation=m.Orientation.DOWN)],
            variable_rate = parameters.ac2c3
        ))

        gating_reactions.append(m.ReactionRule(
            name = f"closed3_to_closed2_{az}_{ch}",
            reactants = [closed3.inst(orientation=m.Orientation.DOWN)],
            products  = [closed2.inst(orientation=m.Orientation.DOWN)],
            variable_rate = parameters.bc3c2
        ))

        gating_reactions.append(m.ReactionRule(
            name = f"closed3_to_open1_{az}_{ch}",
            reactants = [closed3.inst(orientation=m.Orientation.DOWN)],
            products  = [open1.inst(orientation=m.Orientation.DOWN)],
            variable_rate = parameters.ac3o1
        ))

        gating_reactions.append(m.ReactionRule(
            name = f"open1_to_closed3_{az}_{ch}",
            reactants = [open1.inst(orientation=m.Orientation.DOWN)],
            products  = [closed3.inst(orientation=m.Orientation.DOWN)],
            variable_rate = parameters.bo1c3
        ))

        # ============================================
        # CONSTANT OPEN-STATE TRANSITIONS
        # ============================================

        gating_reactions.append(m.ReactionRule(
            name = f"o1_to_o2_{az}_{ch}",
            reactants = [open1.inst(orientation=m.Orientation.DOWN)],
            products  = [open2.inst(orientation=m.Orientation.DOWN)],
            fwd_rate  = 2.5
        ))

        gating_reactions.append(m.ReactionRule(
            name = f"o2_to_o1_{az}_{ch}",
            reactants = [open2.inst(orientation=m.Orientation.DOWN)],
            products  = [open1.inst(orientation=m.Orientation.DOWN)],
            fwd_rate  = 200.0
        ))

        # ============================================
        # CALCIUM RELEASE (AP1..AP4)
        # ============================================

        CA_RATE = {
            1: parameters.k3_control_short_1,
            2: parameters.k3_control_short_2,
            3: parameters.k3_control_short_3,
            4: parameters.k3_control_short_4
        }

        for ap in range(1, 5):
            ca = globals()[f"ca_{az}_1_{ch}_{ap}"]

            release_reactions.append(m.ReactionRule(
                name = f"release_ca_o1_{az}_{ch}_{ap}",
                reactants = [open1.inst(orientation=m.Orientation.DOWN)],
                products  = [open1.inst(orientation=m.Orientation.DOWN),
                             ca.inst(orientation=m.Orientation.DOWN)],
                variable_rate = CA_RATE[ap]
            ))

            release_reactions.append(m.ReactionRule(
                name = f"release_ca_o2_{az}_{ch}_{ap}",
                reactants = [open2.inst(orientation=m.Orientation.DOWN)],
                products  = [open2.inst(orientation=m.Orientation.DOWN),
                             ca.inst(orientation=m.Orientation.DOWN)],
                variable_rate = CA_RATE[ap]
            ))

# ============================================================
# SK CHANNEL GATING REACTIONS (Ca-activated potassium channels)
# forward transitions between closed states are calcium dependent
# and are expressed as absolute rate constants in units of 
# (s^-1 per uM^-1)
# k for mcell = k / 1e-6 = k × 1e6
#          = 200 × 1e6
#          = 2.0 × 10^8  (M^-1 s^-1)
# ============================================================
SK_RATES = {
    "c1_to_c2": 200.0 * 1e6,   # 2.0e8
    "c2_to_c1": 80.0,          # s^-1 
    "c2_to_c3": 160.0 * 1e6,   # 1.6e8
    "c3_to_c2": 80.0,          # s^-1
    "c3_to_o1": 160.0,         # 1.6e2
    "o1_to_c3": 1000.0,        # s^-1
    "c3_to_c4": 80.0 * 1e6,    # 8.0e7
    "c4_to_c3": 200.0,         # s^-1
    "c4_to_o2": 1200.0,        # s^-1
    "o2_to_c4": 100.0          # s^-1
}
sk_reactions = []

for az in range(1,7):
    for ch in range(1,5):

        c1 = globals()[f"closed_SK_{az}_1_{ch}"]
        c2 = globals()[f"closed2_SK_{az}_1_{ch}"]
        c3 = globals()[f"closed3_SK_{az}_1_{ch}"]
        c4 = globals()[f"closed4_SK_{az}_1_{ch}"]
        o1 = globals()[f"open1_SK_{az}_1_{ch}"]
        o2 = globals()[f"open2_SK_{az}_1_{ch}"]

        # ---- Calcium binding: all APs contribute ----
        for ap in range(1,5):
            ca = globals()[f"ca_{az}_1_{ch}_{ap}"]

            # c1 + ca -> c2
            sk_reactions.append(m.ReactionRule(
                name=f"SK_c1_to_c2_{az}_{ch}_{ap}",
                reactants=[
                    c1.inst(orientation=m.Orientation.DOWN),
                    ca.inst(orientation=m.Orientation.DOWN)
                ],
                products=[
                    c2.inst(orientation=m.Orientation.DOWN)
                ],
                fwd_rate=SK_RATES["c1_to_c2"]
            ))

            # c2 -> c1 + ca
            sk_reactions.append(m.ReactionRule(
                name=f"SK_c2_to_c1_{az}_{ch}_{ap}",
                reactants=[
                    c2.inst(orientation=m.Orientation.DOWN)
                ],
                products=[
                    c1.inst(orientation=m.Orientation.DOWN),
                    ca.inst(orientation=m.Orientation.DOWN)
                ],
                fwd_rate=SK_RATES["c2_to_c1"]
            ))

            # c2 + ca -> c3
            sk_reactions.append(m.ReactionRule(
                name=f"SK_c2_to_c3_{az}_{ch}_{ap}",
                reactants=[
                    c2.inst(orientation=m.Orientation.DOWN),
                    ca.inst(orientation=m.Orientation.DOWN)
                ],
                products=[
                    c3.inst(orientation=m.Orientation.DOWN)
                ],
                fwd_rate=SK_RATES["c2_to_c3"]
            ))

            # c3 -> c2 + ca
            sk_reactions.append(m.ReactionRule(
                name=f"SK_c3_to_c2_{az}_{ch}_{ap}",
                reactants=[
                    c3.inst(orientation=m.Orientation.DOWN)
                ],
                products=[
                    c2.inst(orientation=m.Orientation.DOWN),
                    ca.inst(orientation=m.Orientation.DOWN)
                ],
                fwd_rate=SK_RATES["c3_to_c2"]
            ))

            # c3 + ca -> c4
            sk_reactions.append(m.ReactionRule(
                name=f"SK_c3_to_c4_{az}_{ch}_{ap}",
                reactants=[
                    c3.inst(orientation=m.Orientation.DOWN),
                    ca.inst(orientation=m.Orientation.DOWN)
                ],
                products=[
                    c4.inst(orientation=m.Orientation.DOWN)
                ],
                fwd_rate=SK_RATES["c3_to_c4"]
            ))

            # c4 -> c3 + ca
            sk_reactions.append(m.ReactionRule(
                name=f"SK_c4_to_c3_{az}_{ch}_{ap}",
                reactants=[
                    c4.inst(orientation=m.Orientation.DOWN)
                ],
                products=[
                    c3.inst(orientation=m.Orientation.DOWN),
                    ca.inst(orientation=m.Orientation.DOWN)
                ],
                fwd_rate=SK_RATES["c4_to_c3"]
            ))

        # ---- Pure gating transitions (NO calcium involved) ----

        # c3 -> o1
        sk_reactions.append(m.ReactionRule(
            name=f"SK_c3_to_o1_{az}_{ch}",
            reactants=[c3.inst(orientation=m.Orientation.DOWN)],
            products=[o1.inst(orientation=m.Orientation.DOWN)],
            fwd_rate=SK_RATES["c3_to_o1"]
        ))

        # o1 -> c3
        sk_reactions.append(m.ReactionRule(
            name=f"SK_o1_to_c3_{az}_{ch}",
            reactants=[o1.inst(orientation=m.Orientation.DOWN)],
            products=[c3.inst(orientation=m.Orientation.DOWN)],
            fwd_rate=SK_RATES["o1_to_c3"]
        ))

        # c4 -> o2
        sk_reactions.append(m.ReactionRule(
            name=f"SK_c4_to_o2_{az}_{ch}",
            reactants=[c4.inst(orientation=m.Orientation.DOWN)],
            products=[o2.inst(orientation=m.Orientation.DOWN)],
            fwd_rate=SK_RATES["c4_to_o2"]
        ))

        # o2 -> c4
        sk_reactions.append(m.ReactionRule(
            name=f"SK_o2_to_c4_{az}_{ch}",
            reactants=[o2.inst(orientation=m.Orientation.DOWN)],
            products=[c4.inst(orientation=m.Orientation.DOWN)],
            fwd_rate=SK_RATES["o2_to_c4"]
        ))

# ---------------------------------------------------------
# FIXED BUFFER REACTIONS  (unbound_fixed_buffer ↔ bound_fixed_buffer)
# ---------------------------------------------------------

FIXBUF_ON  = 1e8     # Ca + unbound_fixed_buffer → bound_fixed_buffer
FIXBUF_OFF = 1e4     # bound_fixed_buffer → Ca + unbound_fixed_buffer

fixed_buffer_reactions = []

for az in range(1, 7):
    for ch in range(1, 5):
        for ap in range(1, 5):

            ca  = globals()[f"ca_{az}_1_{ch}_{ap}"]
            bfb = globals()[f"bound_fixed_buffer_{az}_1_{ch}_{ap}"]

            # ON reaction
            fixed_buffer_reactions.append(
                m.ReactionRule(
                    name = f"fixedbuf_on_{az}_{ch}_{ap}",
                    reactants = [
                        ca.inst(),
                        unbound_fixed_buffer.inst()
                    ],
                    products = [bfb.inst()],
                    fwd_rate = FIXBUF_ON
                )
            )

            # OFF reaction
            fixed_buffer_reactions.append(
                m.ReactionRule(
                    name = f"fixedbuf_off_{az}_{ch}_{ap}",
                    reactants = [bfb.inst()],
                    products = [
                        ca.inst(),
                        unbound_fixed_buffer.inst()
                    ],
                    fwd_rate = FIXBUF_OFF
                )
            )

# ---------------------------------------------------------
# SYT1 + SYT7 SENSOR REACTION RULES (MODULAR)
# ---------------------------------------------------------

syt1_reactions = []
syt7_reactions = []

# Reaction rates
SYT1_ON  = 2.2e7    # Ca + unbound_sensor   → bound_sensor
SYT1_OFF = 910      # bound_sensor          → Ca + unbound_sensor

SYT7_ON  = 1e7      # Ca + unbound_sensor_Y → bound_sensor_Y
SYT7_OFF = 15       # bound_sensor_Y        → Ca + unbound_sensor_Y

for az in range(1, 7):        # Active zones
    for ch in range(1, 5):    # Channels per zone
        for ap in range(1, 5):  # AP1..AP4 calcium species

            ca  = globals()[f"ca_{az}_1_{ch}_{ap}"]
            bs1 = globals()[f"bound_sensor_{az}_1_{ch}_{ap}"]
            bs7 = globals()[f"bound_sensor_Y_{az}_1_{ch}_{ap}"]

            # ==========================
            # SYT1 ON
            # ==========================
            syt1_reactions.append(
                m.ReactionRule(
                    name = f"syt1_on_{az}_{ch}_{ap}",
                    reactants = [
                        ca.inst(orientation=m.Orientation.DOWN),
                        unbound_sensor.inst(orientation=m.Orientation.DOWN)
                    ],
                    products = [bs1.inst(orientation=m.Orientation.DOWN)],
                    fwd_rate = SYT1_ON
                )
            )

            # ==========================
            # SYT1 OFF
            # ==========================
            syt1_reactions.append(
                m.ReactionRule(
                    name = f"syt1_off_{az}_{ch}_{ap}",
                    reactants = [
                        bs1.inst(orientation=m.Orientation.DOWN)
                    ],
                    products = [
                        ca.inst(orientation=m.Orientation.DOWN),
                        unbound_sensor.inst(orientation=m.Orientation.DOWN)
                    ],
                    fwd_rate = SYT1_OFF
                )
            )

            # ==========================
            # SYT7 ON
            # ==========================
            syt7_reactions.append(
                m.ReactionRule(
                    name = f"syt7_on_{az}_{ch}_{ap}",
                    reactants = [
                        ca.inst(orientation=m.Orientation.DOWN),
                        unbound_sensor_Y.inst(orientation=m.Orientation.DOWN)
                    ],
                    products = [bs7.inst(orientation=m.Orientation.DOWN)],
                    fwd_rate = SYT7_ON
                )
            )

            # ==========================
            # SYT7 OFF
            # ==========================
            syt7_reactions.append(
                m.ReactionRule(
                    name = f"syt7_off_{az}_{ch}_{ap}",
                    reactants = [
                        bs7.inst(orientation=m.Orientation.DOWN)
                    ],
                    products = [
                        ca.inst(orientation=m.Orientation.DOWN),
                        unbound_sensor_Y.inst(orientation=m.Orientation.DOWN)
                    ],
                    fwd_rate = SYT7_OFF
                )
            )

#######################   RL

# ---- create subsystem object and add components ----


subsystem = m.Subsystem()

# Add all calcium species
for az in range(1, 7):
    for ch in range(1, 5):
        for ap in range(1, 5):
            subsystem.add_species(globals()[f"ca_{az}_1_{ch}_{ap}"])

subsystem.add_species(unbound_fixed_buffer)
subsystem.add_species(unbound_sensor)
subsystem.add_species(unbound_sensor_Y)
# Add all channel-state species
for az in range(1, 7):
    for ch in range(1, 5):

        subsystem.add_species(globals()[f"closed_channel_{az}_1_{ch}"])
        subsystem.add_species(globals()[f"closed2_channel_{az}_1_{ch}"])
        subsystem.add_species(globals()[f"closed3_channel_{az}_1_{ch}"])
        subsystem.add_species(globals()[f"open1_channel_{az}_1_{ch}"])
        subsystem.add_species(globals()[f"open2_channel_{az}_1_{ch}"])

# Add all SK channel-state species
for az in range(1, 7):
    for ch in range(1, 5):

        subsystem.add_species(globals()[f"closed_SK_{az}_1_{ch}"])
        subsystem.add_species(globals()[f"closed2_SK_{az}_1_{ch}"])
        subsystem.add_species(globals()[f"closed3_SK_{az}_1_{ch}"])
        subsystem.add_species(globals()[f"closed4_SK_{az}_1_{ch}"])
        subsystem.add_species(globals()[f"open1_SK_{az}_1_{ch}"])
        subsystem.add_species(globals()[f"open2_SK_{az}_1_{ch}"])

#################################################################################
#   surface_class
#
#################################################################################

subsystem.add_surface_class(transparent_to_all_diffusing_molecules)
subsystem.add_surface_class(absorb_all_calcium_ions)


# Add all bound fixed buffers
for az in range(1, 7):
    for ch in range(1, 5):
        for ap in range(1, 5):
            subsystem.add_species(globals()[f"bound_fixed_buffer_{az}_1_{ch}_{ap}"])

# Bound sensors
for az in range(1,7):
    for ch in range(1,5):
        for ap in range(1,5):
            subsystem.add_species(globals()[f"bound_sensor_{az}_1_{ch}_{ap}"])
            subsystem.add_species(globals()[f"bound_sensor_Y_{az}_1_{ch}_{ap}"])

# Add new structured reaction rules
for rr in gating_reactions:
    subsystem.add_reaction_rule(rr)

for rr in release_reactions:
    subsystem.add_reaction_rule(rr)

for rr in fixed_buffer_reactions:
    subsystem.add_reaction_rule(rr)

for rr in syt1_reactions:
    subsystem.add_reaction_rule(rr)

for rr in syt7_reactions:
    subsystem.add_reaction_rule(rr)

for rr in sk_reactions:
    subsystem.add_reaction_rule(rr)


