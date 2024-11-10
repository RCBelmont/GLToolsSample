"""
FILE_NAME: hello_world.py
AUTHOR: RCB
CREATED: 2024/11/10-14:39
DESC: 
"""
import os.path
import sys

sys.path.append('../../GLToolGore')
import GLToolGore.Core as Core
import GLToolGore.Core.Utils.image_utils as iu
import GLToolGore.Core.Utils.texture_utils as tu
import GLToolGore.Core.Utils.comput_shader_utils as csu

if __name__ == '__main__':
    # Create Context
    context = Core.create_contex_standalone()
    com_shader = csu.cs_util_create_compute_shader(context, os.path.dirname(__file__) + '\\hello_world.glsl')
    target_texture = tu.tex_util_create_texture_with_color(context, 256, 256, (0, 0, 0, 1))
    if "color1" in com_shader:
        com_shader['color1'] = (1, 0, 0)
    if "color2" in com_shader:
        com_shader['color2'] = (0, 1, 0)

    target_texture.bind_to_image(0, read=True, write=True)

    com_shader.run(int(target_texture.width / 16), int(target_texture.height / 16), 1)
    img = tu.tex_util_texture_to_img(target_texture)
    iu.img_util_show_img([img])
