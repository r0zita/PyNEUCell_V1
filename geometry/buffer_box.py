import mcell as m

# ---- buffer_box ----
buffer_box_vertex_list = [
    [1.04345417022705, 0.825657695531845, -0.0088684558868411], 
    [1.04345417022705, -0.825657576322556, -0.0088684558868411], 
    [-1.04345440864563, -0.825657457113266, -0.0088684558868411], 
    [-1.04345393180847, 0.825658053159714, -0.0088684558868411], 
    [1.04345464706421, 0.825657337903976, 1.02456057071686], 
    [1.04345345497131, -0.825658053159714, 1.02456057071686], 
    [-1.04345464706421, -0.825657278299332, 1.02456057071686], 
    [-1.04345417022705, 0.82565775513649, 1.02456057071686]
] # buffer_box_vertex_list

buffer_box_wall_list = [
    [4, 0, 3], 
    [4, 3, 7], 
    [2, 6, 7], 
    [2, 7, 3], 
    [1, 5, 2], 
    [5, 6, 2], 
    [0, 4, 1], 
    [4, 5, 1], 
    [4, 7, 5], 
    [7, 6, 5], 
    [0, 1, 2], 
    [0, 2, 3]
] # buffer_box_wall_list

buffer_box_whole_mesh_wall_indices = [
    0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11
] #buffer_box_whole_mesh_wall_indices

buffer_box_whole_mesh = m.SurfaceRegion(
    name = 'whole_mesh',
    wall_indices = buffer_box_whole_mesh_wall_indices
)

buffer_box = m.GeometryObject(
    name = 'buffer_box',
    vertex_list = buffer_box_vertex_list,
    wall_list = buffer_box_wall_list,
    surface_regions = [buffer_box_whole_mesh]
)
# ^^^^ buffer_box ^^^^


