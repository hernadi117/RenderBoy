# Visual inspection
![](https://i.imgur.com/FhiP1CU.png)


The renderer seem to give a somewhat realistic result at first glance, but there are several effects that substantially remove the photo-realistic feeling of the render.
To begin with, the shadows are very sharp, and pitch black. This is primarily due to a point light source being used, and the shadow mask being calculated a lit pixel only when it hits the exact point of the light source. A real life light source is not a point source, and therefore the light is spread more naturally, and the light sourcemay be partially obscured which would give a more natural soft shadow, especially where the shadow begins. Realistically reflections from the surroundings would light up parts of the shadowed region too.

Furthermore we notice that edges of different colors are naively handled, and shows severe aliasing, especially in the checkerboard pattern. 
A first approach to fix this can be by introducing anti-aliasing algorithms, for example by sampling the color values at edges and taking an average
value to smoothen the transitions; this would make the edges less sharp and jagged.

![](https://i.imgur.com/RNzHJyN.png)

In this second render we see that the sphere at the front exhibits some camera distortion, it looks a bit elongated and seems to be some kind of artifact, but I am not sure why. It could be an aspect ratio issue, or some optic phenomena I am not aware of. This could be because the current pinhole camera model perspective exaggerates perspective.

![](https://i.imgur.com/paoQgQw.png)
In this render we can see the noticeable curve in the reflections of the surroundings at the edge of the sphere, which is very realistic, and we can see the reflections of the light onto the ground behind the camera, which is a nice detail. This render has much higher diffusion coefficient which makes the light source's color more apparent, which I believe is realistic too, as the light energy scatters more diffusely.

It must be noted that the parameters of the material chosen for different renders are not by a scientific method, or chosen by the author from intimate material knowledge, but purely from trial and error and chosen to make the images subjectively pretty.


## Conclusion

To conclude, it seems that the major problem with the renderer is that it creates too sharp edges, and too exaggerated optic phenomenas: the shadows are too sharp and strong, the light reflections are very sharp and direct and the material does not diffuse the light rays very realistically. The first fix would be to support light-sources that are not point-light and introduce anti-aliasing. Then some substantial shader work, with texture maps that accurately capture material properties, especially diffuse shading properties, would benefit the ray tracer substantially.
