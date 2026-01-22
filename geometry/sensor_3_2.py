import mcell as m

# ---- sensor_3_2 ----
sensor_3_2_vertex_list = [
    [0.58, 0.242619, 0.011414], 
    [0.586571, 0.245938, 0.011524], 
    [0.585971, 0.238928, 0.013695], 
    [0.573428, 0.254061, 0.011524], 
    [0.573428, 0.245938, 0.011524], 
    [0.566857, 0.25, 0.014034], 
    [0.586571, 0.254061, 0.011524], 
    [0.593143, 0.25, 0.014034], 
    [0.58, 0.236857, 0.014034], 
    [0.574028, 0.238928, 0.013695], 
    [0.58, 0.263143, 0.014034], 
    [0.585971, 0.261072, 0.013695], 
    [0.58, 0.257381, 0.011414], 
    [0.574028, 0.261072, 0.013695], 
    [0.5925, 0.257725, 0.015075], 
    [0.5925, 0.242275, 0.015075], 
    [0.5675, 0.242275, 0.015075], 
    [0.5675, 0.257725, 0.015075], 
    [0.58, 0.25, 0.0103], 
    [0.58369, 0.267043, 0.017386], 
    [0.590633, 0.264695, 0.018095], 
    [0.597205, 0.260633, 0.020605], 
    [0.597914, 0.253691, 0.018257], 
    [0.597914, 0.246309, 0.018257], 
    [0.597205, 0.239367, 0.020605], 
    [0.590633, 0.235305, 0.018095], 
    [0.58369, 0.232957, 0.017386], 
    [0.576309, 0.232957, 0.017386], 
    [0.569367, 0.235305, 0.018095], 
    [0.562795, 0.239367, 0.020605], 
    [0.562086, 0.246309, 0.018257], 
    [0.562086, 0.253691, 0.018257], 
    [0.562795, 0.260633, 0.020605], 
    [0.569367, 0.264695, 0.018095], 
    [0.576309, 0.267043, 0.017386]
] # sensor_3_2_vertex_list

sensor_3_2_wall_list = [
    [0, 1, 2], 
    [3, 4, 5], 
    [1, 6, 7], 
    [8, 9, 0], 
    [10, 11, 12], 
    [0, 9, 4], 
    [8, 0, 2], 
    [2, 1, 15], 
    [15, 1, 7], 
    [7, 6, 14], 
    [6, 11, 14], 
    [12, 11, 6], 
    [12, 13, 10], 
    [3, 13, 12], 
    [3, 17, 13], 
    [5, 17, 3], 
    [16, 5, 4], 
    [16, 4, 9], 
    [1, 0, 18], 
    [1, 18, 6], 
    [18, 12, 6], 
    [18, 3, 12], 
    [18, 4, 3], 
    [18, 0, 4], 
    [19, 11, 10], 
    [19, 20, 11], 
    [20, 14, 11], 
    [20, 21, 14], 
    [21, 22, 14], 
    [22, 7, 14], 
    [22, 23, 7], 
    [23, 15, 7], 
    [23, 24, 15], 
    [24, 25, 15], 
    [25, 2, 15], 
    [25, 26, 2], 
    [26, 8, 2], 
    [26, 27, 8], 
    [27, 9, 8], 
    [27, 28, 9], 
    [28, 16, 9], 
    [28, 29, 16], 
    [29, 30, 16], 
    [30, 5, 16], 
    [30, 31, 5], 
    [31, 17, 5], 
    [31, 32, 17], 
    [32, 33, 17], 
    [33, 13, 17], 
    [33, 34, 13], 
    [34, 10, 13], 
    [34, 19, 10]
] # sensor_3_2_wall_list

sensor_3_2_sites_all_wall_indices = [
    0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 
    16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 
    32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 
    48, 49, 50, 51
] #sensor_3_2_sites_all_wall_indices

sensor_3_2_sites_all = m.SurfaceRegion(
    name = 'sites_all',
    wall_indices = sensor_3_2_sites_all_wall_indices
)

sensor_3_2_site_0_wall_indices = [
    0
] #sensor_3_2_site_0_wall_indices

sensor_3_2_site_0 = m.SurfaceRegion(
    name = 'site_0',
    wall_indices = sensor_3_2_site_0_wall_indices
)

sensor_3_2_site_1_wall_indices = [
    1
] #sensor_3_2_site_1_wall_indices

sensor_3_2_site_1 = m.SurfaceRegion(
    name = 'site_1',
    wall_indices = sensor_3_2_site_1_wall_indices
)

sensor_3_2_site_2_wall_indices = [
    2
] #sensor_3_2_site_2_wall_indices

sensor_3_2_site_2 = m.SurfaceRegion(
    name = 'site_2',
    wall_indices = sensor_3_2_site_2_wall_indices
)

sensor_3_2_site_3_wall_indices = [
    3
] #sensor_3_2_site_3_wall_indices

sensor_3_2_site_3 = m.SurfaceRegion(
    name = 'site_3',
    wall_indices = sensor_3_2_site_3_wall_indices
)

sensor_3_2_site_4_wall_indices = [
    4
] #sensor_3_2_site_4_wall_indices

sensor_3_2_site_4 = m.SurfaceRegion(
    name = 'site_4',
    wall_indices = sensor_3_2_site_4_wall_indices
)

sensor_3_2_site_5_wall_indices = [
    5
] #sensor_3_2_site_5_wall_indices

sensor_3_2_site_5 = m.SurfaceRegion(
    name = 'site_5',
    wall_indices = sensor_3_2_site_5_wall_indices
)

sensor_3_2_site_6_wall_indices = [
    6
] #sensor_3_2_site_6_wall_indices

sensor_3_2_site_6 = m.SurfaceRegion(
    name = 'site_6',
    wall_indices = sensor_3_2_site_6_wall_indices
)

sensor_3_2_site_7_wall_indices = [
    7
] #sensor_3_2_site_7_wall_indices

sensor_3_2_site_7 = m.SurfaceRegion(
    name = 'site_7',
    wall_indices = sensor_3_2_site_7_wall_indices
)

sensor_3_2_site_8_wall_indices = [
    8
] #sensor_3_2_site_8_wall_indices

sensor_3_2_site_8 = m.SurfaceRegion(
    name = 'site_8',
    wall_indices = sensor_3_2_site_8_wall_indices
)

sensor_3_2_site_9_wall_indices = [
    9
] #sensor_3_2_site_9_wall_indices

sensor_3_2_site_9 = m.SurfaceRegion(
    name = 'site_9',
    wall_indices = sensor_3_2_site_9_wall_indices
)

sensor_3_2_site_10_wall_indices = [
    10
] #sensor_3_2_site_10_wall_indices

sensor_3_2_site_10 = m.SurfaceRegion(
    name = 'site_10',
    wall_indices = sensor_3_2_site_10_wall_indices
)

sensor_3_2_site_11_wall_indices = [
    11
] #sensor_3_2_site_11_wall_indices

sensor_3_2_site_11 = m.SurfaceRegion(
    name = 'site_11',
    wall_indices = sensor_3_2_site_11_wall_indices
)

sensor_3_2_site_12_wall_indices = [
    12
] #sensor_3_2_site_12_wall_indices

sensor_3_2_site_12 = m.SurfaceRegion(
    name = 'site_12',
    wall_indices = sensor_3_2_site_12_wall_indices
)

sensor_3_2_site_13_wall_indices = [
    13
] #sensor_3_2_site_13_wall_indices

sensor_3_2_site_13 = m.SurfaceRegion(
    name = 'site_13',
    wall_indices = sensor_3_2_site_13_wall_indices
)

sensor_3_2_site_14_wall_indices = [
    14
] #sensor_3_2_site_14_wall_indices

sensor_3_2_site_14 = m.SurfaceRegion(
    name = 'site_14',
    wall_indices = sensor_3_2_site_14_wall_indices
)

sensor_3_2_site_15_wall_indices = [
    15
] #sensor_3_2_site_15_wall_indices

sensor_3_2_site_15 = m.SurfaceRegion(
    name = 'site_15',
    wall_indices = sensor_3_2_site_15_wall_indices
)

sensor_3_2_site_16_wall_indices = [
    16
] #sensor_3_2_site_16_wall_indices

sensor_3_2_site_16 = m.SurfaceRegion(
    name = 'site_16',
    wall_indices = sensor_3_2_site_16_wall_indices
)

sensor_3_2_site_17_wall_indices = [
    17
] #sensor_3_2_site_17_wall_indices

sensor_3_2_site_17 = m.SurfaceRegion(
    name = 'site_17',
    wall_indices = sensor_3_2_site_17_wall_indices
)

sensor_3_2_site_18_wall_indices = [
    18
] #sensor_3_2_site_18_wall_indices

sensor_3_2_site_18 = m.SurfaceRegion(
    name = 'site_18',
    wall_indices = sensor_3_2_site_18_wall_indices
)

sensor_3_2_site_19_wall_indices = [
    19
] #sensor_3_2_site_19_wall_indices

sensor_3_2_site_19 = m.SurfaceRegion(
    name = 'site_19',
    wall_indices = sensor_3_2_site_19_wall_indices
)

sensor_3_2_site_20_wall_indices = [
    20
] #sensor_3_2_site_20_wall_indices

sensor_3_2_site_20 = m.SurfaceRegion(
    name = 'site_20',
    wall_indices = sensor_3_2_site_20_wall_indices
)

sensor_3_2_site_21_wall_indices = [
    21
] #sensor_3_2_site_21_wall_indices

sensor_3_2_site_21 = m.SurfaceRegion(
    name = 'site_21',
    wall_indices = sensor_3_2_site_21_wall_indices
)

sensor_3_2_site_22_wall_indices = [
    22
] #sensor_3_2_site_22_wall_indices

sensor_3_2_site_22 = m.SurfaceRegion(
    name = 'site_22',
    wall_indices = sensor_3_2_site_22_wall_indices
)

sensor_3_2_site_23_wall_indices = [
    23
] #sensor_3_2_site_23_wall_indices

sensor_3_2_site_23 = m.SurfaceRegion(
    name = 'site_23',
    wall_indices = sensor_3_2_site_23_wall_indices
)

sensor_3_2_site_24_wall_indices = [
    24
] #sensor_3_2_site_24_wall_indices

sensor_3_2_site_24 = m.SurfaceRegion(
    name = 'site_24',
    wall_indices = sensor_3_2_site_24_wall_indices
)

sensor_3_2_site_25_wall_indices = [
    25
] #sensor_3_2_site_25_wall_indices

sensor_3_2_site_25 = m.SurfaceRegion(
    name = 'site_25',
    wall_indices = sensor_3_2_site_25_wall_indices
)

sensor_3_2_site_26_wall_indices = [
    26
] #sensor_3_2_site_26_wall_indices

sensor_3_2_site_26 = m.SurfaceRegion(
    name = 'site_26',
    wall_indices = sensor_3_2_site_26_wall_indices
)

sensor_3_2_site_27_wall_indices = [
    27
] #sensor_3_2_site_27_wall_indices

sensor_3_2_site_27 = m.SurfaceRegion(
    name = 'site_27',
    wall_indices = sensor_3_2_site_27_wall_indices
)

sensor_3_2_site_28_wall_indices = [
    28
] #sensor_3_2_site_28_wall_indices

sensor_3_2_site_28 = m.SurfaceRegion(
    name = 'site_28',
    wall_indices = sensor_3_2_site_28_wall_indices
)

sensor_3_2_site_29_wall_indices = [
    29
] #sensor_3_2_site_29_wall_indices

sensor_3_2_site_29 = m.SurfaceRegion(
    name = 'site_29',
    wall_indices = sensor_3_2_site_29_wall_indices
)

sensor_3_2_site_30_wall_indices = [
    30
] #sensor_3_2_site_30_wall_indices

sensor_3_2_site_30 = m.SurfaceRegion(
    name = 'site_30',
    wall_indices = sensor_3_2_site_30_wall_indices
)

sensor_3_2_site_31_wall_indices = [
    31
] #sensor_3_2_site_31_wall_indices

sensor_3_2_site_31 = m.SurfaceRegion(
    name = 'site_31',
    wall_indices = sensor_3_2_site_31_wall_indices
)

sensor_3_2_site_32_wall_indices = [
    32
] #sensor_3_2_site_32_wall_indices

sensor_3_2_site_32 = m.SurfaceRegion(
    name = 'site_32',
    wall_indices = sensor_3_2_site_32_wall_indices
)

sensor_3_2_site_33_wall_indices = [
    33
] #sensor_3_2_site_33_wall_indices

sensor_3_2_site_33 = m.SurfaceRegion(
    name = 'site_33',
    wall_indices = sensor_3_2_site_33_wall_indices
)

sensor_3_2_site_34_wall_indices = [
    34
] #sensor_3_2_site_34_wall_indices

sensor_3_2_site_34 = m.SurfaceRegion(
    name = 'site_34',
    wall_indices = sensor_3_2_site_34_wall_indices
)

sensor_3_2_site_35_wall_indices = [
    35
] #sensor_3_2_site_35_wall_indices

sensor_3_2_site_35 = m.SurfaceRegion(
    name = 'site_35',
    wall_indices = sensor_3_2_site_35_wall_indices
)

sensor_3_2_site_36_wall_indices = [
    36
] #sensor_3_2_site_36_wall_indices

sensor_3_2_site_36 = m.SurfaceRegion(
    name = 'site_36',
    wall_indices = sensor_3_2_site_36_wall_indices
)

sensor_3_2_site_37_wall_indices = [
    37
] #sensor_3_2_site_37_wall_indices

sensor_3_2_site_37 = m.SurfaceRegion(
    name = 'site_37',
    wall_indices = sensor_3_2_site_37_wall_indices
)

sensor_3_2_site_38_wall_indices = [
    38
] #sensor_3_2_site_38_wall_indices

sensor_3_2_site_38 = m.SurfaceRegion(
    name = 'site_38',
    wall_indices = sensor_3_2_site_38_wall_indices
)

sensor_3_2_site_39_wall_indices = [
    39
] #sensor_3_2_site_39_wall_indices

sensor_3_2_site_39 = m.SurfaceRegion(
    name = 'site_39',
    wall_indices = sensor_3_2_site_39_wall_indices
)

sensor_3_2_site_40_wall_indices = [
    40
] #sensor_3_2_site_40_wall_indices

sensor_3_2_site_40 = m.SurfaceRegion(
    name = 'site_40',
    wall_indices = sensor_3_2_site_40_wall_indices
)

sensor_3_2_site_41_wall_indices = [
    41
] #sensor_3_2_site_41_wall_indices

sensor_3_2_site_41 = m.SurfaceRegion(
    name = 'site_41',
    wall_indices = sensor_3_2_site_41_wall_indices
)

sensor_3_2_site_42_wall_indices = [
    42
] #sensor_3_2_site_42_wall_indices

sensor_3_2_site_42 = m.SurfaceRegion(
    name = 'site_42',
    wall_indices = sensor_3_2_site_42_wall_indices
)

sensor_3_2_site_43_wall_indices = [
    43
] #sensor_3_2_site_43_wall_indices

sensor_3_2_site_43 = m.SurfaceRegion(
    name = 'site_43',
    wall_indices = sensor_3_2_site_43_wall_indices
)

sensor_3_2_site_44_wall_indices = [
    44
] #sensor_3_2_site_44_wall_indices

sensor_3_2_site_44 = m.SurfaceRegion(
    name = 'site_44',
    wall_indices = sensor_3_2_site_44_wall_indices
)

sensor_3_2_site_45_wall_indices = [
    45
] #sensor_3_2_site_45_wall_indices

sensor_3_2_site_45 = m.SurfaceRegion(
    name = 'site_45',
    wall_indices = sensor_3_2_site_45_wall_indices
)

sensor_3_2_site_46_wall_indices = [
    46
] #sensor_3_2_site_46_wall_indices

sensor_3_2_site_46 = m.SurfaceRegion(
    name = 'site_46',
    wall_indices = sensor_3_2_site_46_wall_indices
)

sensor_3_2_site_47_wall_indices = [
    47
] #sensor_3_2_site_47_wall_indices

sensor_3_2_site_47 = m.SurfaceRegion(
    name = 'site_47',
    wall_indices = sensor_3_2_site_47_wall_indices
)

sensor_3_2_site_48_wall_indices = [
    48
] #sensor_3_2_site_48_wall_indices

sensor_3_2_site_48 = m.SurfaceRegion(
    name = 'site_48',
    wall_indices = sensor_3_2_site_48_wall_indices
)

sensor_3_2_site_49_wall_indices = [
    49
] #sensor_3_2_site_49_wall_indices

sensor_3_2_site_49 = m.SurfaceRegion(
    name = 'site_49',
    wall_indices = sensor_3_2_site_49_wall_indices
)

sensor_3_2_site_50_wall_indices = [
    50
] #sensor_3_2_site_50_wall_indices

sensor_3_2_site_50 = m.SurfaceRegion(
    name = 'site_50',
    wall_indices = sensor_3_2_site_50_wall_indices
)

sensor_3_2_site_51_wall_indices = [
    51
] #sensor_3_2_site_51_wall_indices

sensor_3_2_site_51 = m.SurfaceRegion(
    name = 'site_51',
    wall_indices = sensor_3_2_site_51_wall_indices
)

sensor_3_2 = m.GeometryObject(
    name = 'sensor_3_2',
    vertex_list = sensor_3_2_vertex_list,
    wall_list = sensor_3_2_wall_list,
    surface_regions = [sensor_3_2_sites_all, sensor_3_2_site_0, sensor_3_2_site_1, sensor_3_2_site_2, sensor_3_2_site_3, sensor_3_2_site_4, sensor_3_2_site_5, sensor_3_2_site_6, sensor_3_2_site_7, sensor_3_2_site_8, sensor_3_2_site_9, sensor_3_2_site_10, sensor_3_2_site_11, sensor_3_2_site_12, sensor_3_2_site_13, sensor_3_2_site_14, sensor_3_2_site_15, sensor_3_2_site_16, sensor_3_2_site_17, sensor_3_2_site_18, sensor_3_2_site_19, sensor_3_2_site_20, sensor_3_2_site_21, sensor_3_2_site_22, sensor_3_2_site_23, sensor_3_2_site_24, sensor_3_2_site_25, sensor_3_2_site_26, sensor_3_2_site_27, sensor_3_2_site_28, sensor_3_2_site_29, sensor_3_2_site_30, sensor_3_2_site_31, sensor_3_2_site_32, sensor_3_2_site_33, sensor_3_2_site_34, sensor_3_2_site_35, sensor_3_2_site_36, sensor_3_2_site_37, sensor_3_2_site_38, sensor_3_2_site_39, sensor_3_2_site_40, sensor_3_2_site_41, sensor_3_2_site_42, sensor_3_2_site_43, sensor_3_2_site_44, sensor_3_2_site_45, sensor_3_2_site_46, sensor_3_2_site_47, sensor_3_2_site_48, sensor_3_2_site_49, sensor_3_2_site_50, sensor_3_2_site_51]
)
# ^^^^ sensor_3_2 ^^^^


