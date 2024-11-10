#version 440

layout (local_size_x = 16, local_size_y = 16) in;

layout(binding=0, rgba32f) uniform image2D dstTex;

uniform vec3  color1;
uniform vec3  color2;


void main()
{
    ivec2 texelPos = ivec2(gl_GlobalInvocationID.xy);
    ivec2 size = imageSize(dstTex);
    vec2 uv = vec2((texelPos.x*1.0 + 0.5) / size.x, (texelPos.y*1.0 + 0.5) / size.y);

    vec4 final_color = vec4(mix(color1, color2, uv.xxx), 1.0);
    imageStore(dstTex, texelPos, final_color);
}