import numpy as np
from loader import parse_obj, save_obj
from cut import re_index, cut_obj

path_last_full = './path/20230702185753.obj'

path_bot = './path/20230510153006_cut.obj'
path_mid = './path/20240102231959.obj'
path_top = './path/20231016151002_cut.obj'

obj_bot = parse_obj(path_bot)
obj_mid = parse_obj(path_mid)
obj_top = parse_obj(path_top)

# 400
bot_min = np.min(obj_bot['vertices'], axis=0)
# 2396
bot_max = np.max(obj_bot['vertices'], axis=0)

# 3504
mid_min = np.min(obj_mid['vertices'], axis=0)
# 4295
mid_max = np.max(obj_mid['vertices'], axis=0)

# 4295
top_min = np.min(obj_top['vertices'], axis=0)
# 5403
top_max = np.max(obj_top['vertices'], axis=0)

print(bot_min)
print(bot_max)

print(mid_min)
print(mid_max)

print(top_min)
print(top_max)

# obj_last_full = parse_obj(path_last_full)
# cut_obj(obj_last_full, splitAxis=2, splitOffset=bot_max[2], survive='right', align=True)
# re_index(obj_last_full)
# cut_obj(obj_last_full, splitAxis=2, splitOffset=top_min[2], survive='left', align=True)
# re_index(obj_last_full)
# obj_last_full['vertices'] -= np.array([256 * 12, 256 * 7, 256 * 9])
# save_obj('./path/20230702185753_cut_translate.obj', obj_last_full)

# obj_mid['vertices'] -= np.array([256 * 12, 256 * 7, 256 * 9])
# save_obj('./path/20240102231959_translate.obj', obj_mid)

# cut_obj(obj_bot, splitAxis=2, splitOffset=bot_max[2]-100, survive='right', align=True)
# re_index(obj_bot)
# save_obj('./path/20230510153006_cut.obj', obj_bot)

# cut_obj(obj_top, splitAxis=2, splitOffset=top_min[2]+100, survive='left', align=True)
# re_index(obj_top)
# save_obj('./path/20231016151002_cut.obj', obj_top)



