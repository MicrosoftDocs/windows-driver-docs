---
title: Computing the Size of Point Sprites
description: Computing the Size of Point Sprites
ms.assetid: f92ea8c6-f330-4625-873f-70c773c86334
keywords:
- DirectX 8.0 release notes WDK Windows 2000 display , point sprites
- point sprites WDK DirectX 8.0
- size WDK point sprites
- point size WDK DirectX 8.0
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Computing the Size of Point Sprites


## <span id="ddk_computing_the_size_of_point_sprites_gg"></span><span id="DDK_COMPUTING_THE_SIZE_OF_POINT_SPRITES_GG"></span>


Point sprites are rendered by using the existing D3DPT\_POINT primitive type. The size of point sprites can be controlled either through the new render state D3DRS\_POINTSIZE or by the new FVF component D3DFVF\_PSIZE.

For vertices without the D3DFVF\_PSIZE vertex component, the current value of the D3DRS\_POINTSIZE render state should be used. Otherwise, the value specified in the vertex data should be used. In either case, the value is a floating-point number that is the size (width and height) of the rendered quad in rendering target pixels. The default value of the point size render state (1.0) is sent to the driver during initialization.

Two render states control clamping of the computed point sprite size, D3DRS\_POINTSIZE\_MIN and D3DRS\_POINTSIZE\_MAX. The computed size of the point should be clamped to be no smaller than the size given by D3DRS\_POINTSIZE\_MIN and no larger than the size given by D3DRS\_POINTSIZE\_MAX. It is the driver's responsibility to ensure that the point sprite size is clamped to the minimum and maximum sizes specified by the render states.

For drivers that support hardware vertex processing, the size of point sprites may also be scaled based on the distance from the point to the eye (in eye space). Scaling of the point sprites is enabled by the new render state D3DRS\_POINTSCALEENABLE. If the value of this render state is **TRUE** then the points are scaled according to the following parameters, the Sₛ formula, and maximum/minimum determination. Note that in this case the application-specified point size is expressed in camera space units. This scaling is performed by drivers that support transform and lighting only.

<span id="Si"></span><span id="si"></span><span id="SI"></span>S<sub>i</sub>  
Input point size (either per-vertex or D3DRS\_POINTSIZE)

<span id="A_B_C"></span><span id="a_b_c"></span>A,B,C  
Point scale factors D3DRS\_POINTSCALEA/B/C

<span id="Vh"></span><span id="vh"></span><span id="VH"></span>Vₕ  
Height of viewport (**dwHeight** field in D3D\_VIEWPORT)

<span id="Pe____Xe__Ye__Ze_"></span><span id="pe____xe__ye__ze_"></span><span id="PE____XE__YE__ZE_"></span>Pₑ = (Xₑ, Yₑ, Zₑ)  
Eye space position of point

<span id="De___sqrt__Xe2___Ye2___Ze2_"></span><span id="de___sqrt__xe2___ye2___ze2_"></span><span id="DE___SQRT__XE2___YE2___ZE2_"></span>De = sqrt (Xₑ² + Yₑ² + Zₑ²)  
Distance from eye to position (eye at origin)

<span id="Ss___Vh___Si___sqrt_1__A___B_De___C__De2___"></span><span id="ss___vh___si___sqrt_1__a___b_de___c__de2___"></span><span id="SS___VH___SI___SQRT_1__A___B_DE___C__DE2___"></span>Sₛ = Vₕ \* S<sub>i</sub> \* sqrt(1/(A + B\*Dₑ + C\*(Dₑ²)))  
Screen space point size

<span id="Smax"></span><span id="smax"></span><span id="SMAX"></span>Smax  
**MaxPointSize** (member of D3DCAPS8) device capability

<span id="Smin"></span><span id="smin"></span><span id="SMIN"></span>Smin  
D3DRS\_POINTSIZE\_MIN

<span id="Final_screen-space_point_size_S__"></span><span id="final_screen-space_point_size_s__"></span><span id="FINAL_SCREEN-SPACE_POINT_SIZE_S__"></span>Final screen-space point size S =  
Smax if Sₛ &gt; Smax

Smin if Sₛ &lt; Smin

Sₛ otherwise

Note that for the application to be drawing single pixel vertices, rather than point sprites, it must have the following render states set:

```cpp
SetRenderState (D3DRS_POINTSCALEENABLE, FALSE)
// All textures must be turned off.
SetTexture (0, NULL); 
SetTextureStageState(1, D3DTSS_COLOROP,  D3DTOP_DISABLE);
// The point size render state must be set to any value between 0.0-1.0
SetRenderState(D3DRS_POINTSIZE, 1.0);
// D3DRS_POINTSIZE_MIN and D3DRS_POINTSIZE_MAX
// must be set appropriately to allow
// D3DRS_POINTSIZE to be set to a value between 0.0-1.0
```

 

 





