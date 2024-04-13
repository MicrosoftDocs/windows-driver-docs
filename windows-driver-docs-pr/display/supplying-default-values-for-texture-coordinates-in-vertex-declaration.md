---
title: Default Texture Coordinates in Vertex Declarations
description: A display driver whose display device supports a programmable pixel shader must supply default values for any texture coordinates that are missing in a vertex declaration.
keywords:
- vertex declarations WDK DirectX 9.0
- texture coordinates WDK DirectX 9.0
ms.date: 12/06/2018
---

# Default Texture Coordinates in Vertex Declarations


**This topic applies to DirectX 8.0 and later.**

A display driver whose display device supports a programmable pixel shader must supply default values for any texture coordinates that are missing in a vertex declaration. Texture coordinates that are supplied to pixel shaders must have four components (u,v,w,q). If the u, v, or w component is missing, the hardware or driver must supply a default value of 0 to that component. If the q component is missing, the hardware or driver must supply a default value of 1 to that component. Therefore, if all components are missing, (0,0,0,1) is the default value. For example, if a 2D texture coordinate is sent to a pixel shader that uses 3D texture coordinates, then the hardware or driver supplies default values of 0 and 1 to the 3rd and 4th components respectively.

The exception for [source parameter tokens](./source-parameter-token.md) is with the following instruction:

`
// D3DSIO_DEF c#,f0,f1,f2,f2
`

For this instruction, the source parameter tokens (f\#) are taken as 32-bit floats.

 
