import numpy as np
from loader import parse_obj, save_obj

# x, y, z
shift = [256 * 9, 256 * 9, 256 * 41]

# u, v
uvs = [0.57, 0.47]
uve = [0.68, 0.55]

def re_index(data):
    if (data['faces'].shape[0] == 0): return

    data['faces'] -= 1
    selected_vertices = np.unique(data['faces'][:,:,0])

    # only leave the vertices used to form the faces
    data['vertices'] = data['vertices'][selected_vertices]
    data['normals']  = data['normals'][selected_vertices]
    data['uvs']      = data['uvs'][selected_vertices]
    data['colors']   = data['colors'][selected_vertices]

    # update face index
    vertex_mapping = { old_index: new_index for new_index, old_index in enumerate(selected_vertices) }
    data['faces'] = np.vectorize(lambda x: vertex_mapping.get(x, x))(data['faces'])
    data['faces'] += 1

data = parse_obj('path/20230827161847.obj')

print(data['vertices'].shape)
print(data['uvs'].shape)
print(data['faces'].shape)

triUVs = data['uvs'][data['faces'][:,:,0] - 1]
print(triUVs.shape)

tri_lower_bool = triUVs[:, :, 0] < uvs[0]
tri_lower_num = np.sum(tri_lower_bool, axis=1)

data['faces'] = data['faces'][tri_lower_num < 2]
re_index(data)

triUVs = data['uvs'][data['faces'][:,:,0] - 1]
print(triUVs.shape)

tri_lower_bool = triUVs[:, :, 1] < uvs[1]
tri_lower_num = np.sum(tri_lower_bool, axis=1)

data['faces'] = data['faces'][tri_lower_num < 2]
re_index(data)

triUVs = data['uvs'][data['faces'][:,:,0] - 1]
print(triUVs.shape)

tri_lower_bool = triUVs[:, :, 0] < uve[0]
tri_lower_num = np.sum(tri_lower_bool, axis=1)

data['faces'] = data['faces'][tri_lower_num >= 2]
re_index(data)

triUVs = data['uvs'][data['faces'][:,:,0] - 1]
print(triUVs.shape)

tri_lower_bool = triUVs[:, :, 1] < uve[1]
tri_lower_num = np.sum(tri_lower_bool, axis=1)

data['faces'] = data['faces'][tri_lower_num >= 2]
re_index(data)

print(np.min(data['vertices'], axis=0))
print(np.max(data['vertices'], axis=0))

data['vertices'] -= np.array(shift)

save_obj('./path/pi.obj', data, mtl='20230827161847')




