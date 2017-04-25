---
title: Supplying Default Values for Texture Coordinates in Vertex Declarations
description: Supplying Default Values for Texture Coordinates in Vertex Declarations
ms.assetid: 5e346e7e-7460-41d9-aee1-dcc72fc642c1
keywords:
- vertex declarations WDK DirectX 9.0
- texture coordinates WDK DirectX 9.0
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Supplying Default Values for Texture Coordinates in Vertex Declarations


## <span id="ddk_supplying_default_values_for_texture_coordinates_in_vertex_declara"></span><span id="DDK_SUPPLYING_DEFAULT_VALUES_FOR_TEXTURE_COORDINATES_IN_VERTEX_DECLARA"></span>


**This topic applies to DirectX 8.0 and later.**

A display driver whose display device supports a programmable pixel shader must supply default values for any texture coordinates that are missing in a vertex declaration. Texture coordinates that are supplied to pixel shaders must have four components (u,v,w,q). If the u, v, or w component is missing, the hardware or driver must supply a default value of 0 to that component. If the q component is missing, the hardware or driver must supply a default value of 1 to that component. Therefore, if all components are missing, (0,0,0,1) is the default value. For example, if a 2D texture coordinate is sent to a pixel shader that uses 3D texture coordinates, then the hardware or driver supplies default values of 0 and 1 to the 3rd and 4th components respectively.

The exception for [source parameter tokens](https://msdn.microsoft.com/library/windows/hardware/ff569716) is with the following instruction:

```
// D3DSIO_DEF c#,f0,f1,f2,f2
```

For this instruction, the source parameter tokens (f\#) are taken as 32-bit floats.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Supplying%20Default%20Values%20for%20Texture%20Coordinates%20in%20Vertex%20Declarations%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




