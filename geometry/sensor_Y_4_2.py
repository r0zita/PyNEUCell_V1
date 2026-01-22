import mcell as m

# ---- sensor_Y_4_2 ----
sensor_Y_4_2_vertex_list = [
    [-0.558732999414206, -0.302, 0.0218569998070598], 
    [-0.601265000104904, -0.302, 0.0218569998070598], 
    [-0.572273999843746, -0.281775000363588, 0.0224999998137355], 
    [-0.572273999843746, -0.322225999876857, 0.0224999998137355], 
    [-0.587726000156254, -0.281775000363588, 0.0224999998137355], 
    [-0.587726000156254, -0.322225999876857, 0.0224999998137355], 
    [-0.559775000363588, -0.289499999813735, 0.0272750000841916], 
    [-0.600224999636412, -0.289499999813735, 0.0272750000841916], 
    [-0.559775000363588, -0.314500000186265, 0.0272750000841916], 
    [-0.600224999636412, -0.314500000186265, 0.0272750000841916], 
    [-0.576309000067413, -0.284956999912858, 0.0170859991014004], 
    [-0.583690999932587, -0.319043000087142, 0.0170859991014004], 
    [-0.558395000100136, -0.296028999935836, 0.0239280004426837], 
    [-0.601604999899864, -0.296028999935836, 0.0239280004426837], 
    [-0.558395000100136, -0.307971000064164, 0.0239280004426837], 
    [-0.601604999899864, -0.307971000064164, 0.0239280004426837], 
    [-0.5620859991014, -0.305690999932587, 0.017956999912858], 
    [-0.5620859991014, -0.298310000075027, 0.017956999912858], 
    [-0.597913000658154, -0.298310000075027, 0.017956999912858], 
    [-0.597913000658154, -0.305690999932587, 0.017956999912858], 
    [-0.562793999835849, -0.291366999827325, 0.0203050000965595], 
    [-0.569366999827325, -0.28730500009656, 0.017677698135376], 
    [-0.565306000337005, -0.284795000076294, 0.0243669998273253], 
    [-0.569366999827325, -0.316694999903441, 0.0177950000762939], 
    [-0.562793999835849, -0.312633000172675, 0.0203050000965595], 
    [-0.565306000337005, -0.319204999923706, 0.0243669998273253], 
    [-0.58, -0.280733999654651, 0.0218569998070598], 
    [-0.58, -0.323266000345349, 0.0218569998070598], 
    [-0.59469499990344, -0.284795000076294, 0.0243669998273253], 
    [-0.590633000172675, -0.28730500009656, 0.0177950000762939], 
    [-0.597203999683261, -0.291366999827325, 0.0203050000965595], 
    [-0.59469499990344, -0.319204999923706, 0.0243669998273253], 
    [-0.597203999683261, -0.312633000172675, 0.0203050000965595], 
    [-0.590633000172675, -0.316694999903441, 0.0177950000762939], 
    [-0.576309000067413, -0.319043000087142, 0.0170859991014004], 
    [-0.583690999932587, -0.284956999912858, 0.0170859991014004]
] # sensor_Y_4_2_vertex_list

sensor_Y_4_2_wall_list = [
    [10, 2, 21], 
    [20, 6, 12], 
    [0, 17, 12], 
    [8, 24, 14], 
    [0, 14, 16], 
    [3, 34, 23], 
    [4, 26, 35], 
    [2, 10, 26], 
    [34, 3, 27], 
    [11, 27, 5], 
    [29, 4, 35], 
    [13, 7, 30], 
    [1, 13, 18], 
    [15, 32, 9], 
    [1, 19, 15], 
    [11, 5, 33], 
    [17, 0, 16], 
    [1, 18, 19], 
    [21, 2, 22], 
    [6, 20, 22], 
    [25, 24, 8], 
    [25, 3, 23], 
    [28, 4, 29], 
    [28, 30, 7], 
    [31, 9, 32], 
    [31, 33, 5], 
    [20, 12, 17], 
    [24, 16, 14], 
    [35, 26, 10], 
    [34, 27, 11], 
    [13, 30, 18], 
    [32, 15, 19], 
    [21, 22, 20], 
    [25, 23, 24], 
    [28, 29, 30], 
    [31, 32, 33]
] # sensor_Y_4_2_wall_list

sensor_Y_4_2_sites_all_wall_indices = [
    0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 
    16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 
    32, 33, 34, 35
] #sensor_Y_4_2_sites_all_wall_indices

sensor_Y_4_2_sites_all = m.SurfaceRegion(
    name = 'sites_all',
    wall_indices = sensor_Y_4_2_sites_all_wall_indices
)

sensor_Y_4_2_site_0_wall_indices = [
    0
] #sensor_Y_4_2_site_0_wall_indices

sensor_Y_4_2_site_0 = m.SurfaceRegion(
    name = 'site_0',
    wall_indices = sensor_Y_4_2_site_0_wall_indices
)

sensor_Y_4_2_site_1_wall_indices = [
    1
] #sensor_Y_4_2_site_1_wall_indices

sensor_Y_4_2_site_1 = m.SurfaceRegion(
    name = 'site_1',
    wall_indices = sensor_Y_4_2_site_1_wall_indices
)

sensor_Y_4_2_site_2_wall_indices = [
    2
] #sensor_Y_4_2_site_2_wall_indices

sensor_Y_4_2_site_2 = m.SurfaceRegion(
    name = 'site_2',
    wall_indices = sensor_Y_4_2_site_2_wall_indices
)

sensor_Y_4_2_site_3_wall_indices = [
    3
] #sensor_Y_4_2_site_3_wall_indices

sensor_Y_4_2_site_3 = m.SurfaceRegion(
    name = 'site_3',
    wall_indices = sensor_Y_4_2_site_3_wall_indices
)

sensor_Y_4_2_site_4_wall_indices = [
    4
] #sensor_Y_4_2_site_4_wall_indices

sensor_Y_4_2_site_4 = m.SurfaceRegion(
    name = 'site_4',
    wall_indices = sensor_Y_4_2_site_4_wall_indices
)

sensor_Y_4_2_site_5_wall_indices = [
    5
] #sensor_Y_4_2_site_5_wall_indices

sensor_Y_4_2_site_5 = m.SurfaceRegion(
    name = 'site_5',
    wall_indices = sensor_Y_4_2_site_5_wall_indices
)

sensor_Y_4_2_site_6_wall_indices = [
    6
] #sensor_Y_4_2_site_6_wall_indices

sensor_Y_4_2_site_6 = m.SurfaceRegion(
    name = 'site_6',
    wall_indices = sensor_Y_4_2_site_6_wall_indices
)

sensor_Y_4_2_site_7_wall_indices = [
    7
] #sensor_Y_4_2_site_7_wall_indices

sensor_Y_4_2_site_7 = m.SurfaceRegion(
    name = 'site_7',
    wall_indices = sensor_Y_4_2_site_7_wall_indices
)

sensor_Y_4_2_site_8_wall_indices = [
    8
] #sensor_Y_4_2_site_8_wall_indices

sensor_Y_4_2_site_8 = m.SurfaceRegion(
    name = 'site_8',
    wall_indices = sensor_Y_4_2_site_8_wall_indices
)

sensor_Y_4_2_site_9_wall_indices = [
    9
] #sensor_Y_4_2_site_9_wall_indices

sensor_Y_4_2_site_9 = m.SurfaceRegion(
    name = 'site_9',
    wall_indices = sensor_Y_4_2_site_9_wall_indices
)

sensor_Y_4_2_site_10_wall_indices = [
    10
] #sensor_Y_4_2_site_10_wall_indices

sensor_Y_4_2_site_10 = m.SurfaceRegion(
    name = 'site_10',
    wall_indices = sensor_Y_4_2_site_10_wall_indices
)

sensor_Y_4_2_site_11_wall_indices = [
    11
] #sensor_Y_4_2_site_11_wall_indices

sensor_Y_4_2_site_11 = m.SurfaceRegion(
    name = 'site_11',
    wall_indices = sensor_Y_4_2_site_11_wall_indices
)

sensor_Y_4_2_site_12_wall_indices = [
    12
] #sensor_Y_4_2_site_12_wall_indices

sensor_Y_4_2_site_12 = m.SurfaceRegion(
    name = 'site_12',
    wall_indices = sensor_Y_4_2_site_12_wall_indices
)

sensor_Y_4_2_site_13_wall_indices = [
    13
] #sensor_Y_4_2_site_13_wall_indices

sensor_Y_4_2_site_13 = m.SurfaceRegion(
    name = 'site_13',
    wall_indices = sensor_Y_4_2_site_13_wall_indices
)

sensor_Y_4_2_site_14_wall_indices = [
    14
] #sensor_Y_4_2_site_14_wall_indices

sensor_Y_4_2_site_14 = m.SurfaceRegion(
    name = 'site_14',
    wall_indices = sensor_Y_4_2_site_14_wall_indices
)

sensor_Y_4_2_site_15_wall_indices = [
    15
] #sensor_Y_4_2_site_15_wall_indices

sensor_Y_4_2_site_15 = m.SurfaceRegion(
    name = 'site_15',
    wall_indices = sensor_Y_4_2_site_15_wall_indices
)

sensor_Y_4_2_site_16_wall_indices = [
    16
] #sensor_Y_4_2_site_16_wall_indices

sensor_Y_4_2_site_16 = m.SurfaceRegion(
    name = 'site_16',
    wall_indices = sensor_Y_4_2_site_16_wall_indices
)

sensor_Y_4_2_site_17_wall_indices = [
    17
] #sensor_Y_4_2_site_17_wall_indices

sensor_Y_4_2_site_17 = m.SurfaceRegion(
    name = 'site_17',
    wall_indices = sensor_Y_4_2_site_17_wall_indices
)

sensor_Y_4_2_site_18_wall_indices = [
    18
] #sensor_Y_4_2_site_18_wall_indices

sensor_Y_4_2_site_18 = m.SurfaceRegion(
    name = 'site_18',
    wall_indices = sensor_Y_4_2_site_18_wall_indices
)

sensor_Y_4_2_site_19_wall_indices = [
    19
] #sensor_Y_4_2_site_19_wall_indices

sensor_Y_4_2_site_19 = m.SurfaceRegion(
    name = 'site_19',
    wall_indices = sensor_Y_4_2_site_19_wall_indices
)

sensor_Y_4_2_site_20_wall_indices = [
    20
] #sensor_Y_4_2_site_20_wall_indices

sensor_Y_4_2_site_20 = m.SurfaceRegion(
    name = 'site_20',
    wall_indices = sensor_Y_4_2_site_20_wall_indices
)

sensor_Y_4_2_site_21_wall_indices = [
    21
] #sensor_Y_4_2_site_21_wall_indices

sensor_Y_4_2_site_21 = m.SurfaceRegion(
    name = 'site_21',
    wall_indices = sensor_Y_4_2_site_21_wall_indices
)

sensor_Y_4_2_site_22_wall_indices = [
    22
] #sensor_Y_4_2_site_22_wall_indices

sensor_Y_4_2_site_22 = m.SurfaceRegion(
    name = 'site_22',
    wall_indices = sensor_Y_4_2_site_22_wall_indices
)

sensor_Y_4_2_site_23_wall_indices = [
    23
] #sensor_Y_4_2_site_23_wall_indices

sensor_Y_4_2_site_23 = m.SurfaceRegion(
    name = 'site_23',
    wall_indices = sensor_Y_4_2_site_23_wall_indices
)

sensor_Y_4_2_site_24_wall_indices = [
    24
] #sensor_Y_4_2_site_24_wall_indices

sensor_Y_4_2_site_24 = m.SurfaceRegion(
    name = 'site_24',
    wall_indices = sensor_Y_4_2_site_24_wall_indices
)

sensor_Y_4_2_site_25_wall_indices = [
    25
] #sensor_Y_4_2_site_25_wall_indices

sensor_Y_4_2_site_25 = m.SurfaceRegion(
    name = 'site_25',
    wall_indices = sensor_Y_4_2_site_25_wall_indices
)

sensor_Y_4_2_site_26_wall_indices = [
    26
] #sensor_Y_4_2_site_26_wall_indices

sensor_Y_4_2_site_26 = m.SurfaceRegion(
    name = 'site_26',
    wall_indices = sensor_Y_4_2_site_26_wall_indices
)

sensor_Y_4_2_site_27_wall_indices = [
    27
] #sensor_Y_4_2_site_27_wall_indices

sensor_Y_4_2_site_27 = m.SurfaceRegion(
    name = 'site_27',
    wall_indices = sensor_Y_4_2_site_27_wall_indices
)

sensor_Y_4_2_site_28_wall_indices = [
    28
] #sensor_Y_4_2_site_28_wall_indices

sensor_Y_4_2_site_28 = m.SurfaceRegion(
    name = 'site_28',
    wall_indices = sensor_Y_4_2_site_28_wall_indices
)

sensor_Y_4_2_site_29_wall_indices = [
    29
] #sensor_Y_4_2_site_29_wall_indices

sensor_Y_4_2_site_29 = m.SurfaceRegion(
    name = 'site_29',
    wall_indices = sensor_Y_4_2_site_29_wall_indices
)

sensor_Y_4_2_site_30_wall_indices = [
    30
] #sensor_Y_4_2_site_30_wall_indices

sensor_Y_4_2_site_30 = m.SurfaceRegion(
    name = 'site_30',
    wall_indices = sensor_Y_4_2_site_30_wall_indices
)

sensor_Y_4_2_site_31_wall_indices = [
    31
] #sensor_Y_4_2_site_31_wall_indices

sensor_Y_4_2_site_31 = m.SurfaceRegion(
    name = 'site_31',
    wall_indices = sensor_Y_4_2_site_31_wall_indices
)

sensor_Y_4_2_site_32_wall_indices = [
    32
] #sensor_Y_4_2_site_32_wall_indices

sensor_Y_4_2_site_32 = m.SurfaceRegion(
    name = 'site_32',
    wall_indices = sensor_Y_4_2_site_32_wall_indices
)

sensor_Y_4_2_site_33_wall_indices = [
    33
] #sensor_Y_4_2_site_33_wall_indices

sensor_Y_4_2_site_33 = m.SurfaceRegion(
    name = 'site_33',
    wall_indices = sensor_Y_4_2_site_33_wall_indices
)

sensor_Y_4_2_site_34_wall_indices = [
    34
] #sensor_Y_4_2_site_34_wall_indices

sensor_Y_4_2_site_34 = m.SurfaceRegion(
    name = 'site_34',
    wall_indices = sensor_Y_4_2_site_34_wall_indices
)

sensor_Y_4_2_site_35_wall_indices = [
    35
] #sensor_Y_4_2_site_35_wall_indices

sensor_Y_4_2_site_35 = m.SurfaceRegion(
    name = 'site_35',
    wall_indices = sensor_Y_4_2_site_35_wall_indices
)

sensor_Y_4_2 = m.GeometryObject(
    name = 'sensor_Y_4_2',
    vertex_list = sensor_Y_4_2_vertex_list,
    wall_list = sensor_Y_4_2_wall_list,
    surface_regions = [sensor_Y_4_2_sites_all, sensor_Y_4_2_site_0, sensor_Y_4_2_site_1, sensor_Y_4_2_site_2, sensor_Y_4_2_site_3, sensor_Y_4_2_site_4, sensor_Y_4_2_site_5, sensor_Y_4_2_site_6, sensor_Y_4_2_site_7, sensor_Y_4_2_site_8, sensor_Y_4_2_site_9, sensor_Y_4_2_site_10, sensor_Y_4_2_site_11, sensor_Y_4_2_site_12, sensor_Y_4_2_site_13, sensor_Y_4_2_site_14, sensor_Y_4_2_site_15, sensor_Y_4_2_site_16, sensor_Y_4_2_site_17, sensor_Y_4_2_site_18, sensor_Y_4_2_site_19, sensor_Y_4_2_site_20, sensor_Y_4_2_site_21, sensor_Y_4_2_site_22, sensor_Y_4_2_site_23, sensor_Y_4_2_site_24, sensor_Y_4_2_site_25, sensor_Y_4_2_site_26, sensor_Y_4_2_site_27, sensor_Y_4_2_site_28, sensor_Y_4_2_site_29, sensor_Y_4_2_site_30, sensor_Y_4_2_site_31, sensor_Y_4_2_site_32, sensor_Y_4_2_site_33, sensor_Y_4_2_site_34, sensor_Y_4_2_site_35]
)
# ^^^^ sensor_Y_4_2 ^^^^


