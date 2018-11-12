---
title: Direct3D Shader Codes
description: Direct3D Shader Codes
ms.assetid: 30d14bbe-10fe-46fc-99b3-ab2f989abb29
ms.date: 01/05/2018
ms.localizationpriority: medium
---

# Direct3D Shader Codes


Pixel shader code follows the D3DHAL\_DP2CREATEPIXELSHADER structure in the command stream. For DirectX 8.1 and earlier, vertex shader code follows the D3DHAL\_DP2CREATEVERTEXSHADER structure. For DirectX 9.0 and later, vertex shader code follows the D3DHAL\_DP2CREATEVERTEXSHADERFUNC structure. The runtime creates either a pixel or vertex shader when it calls a driver's D3dDrawPrimitives2 function. To create a pixel shader, the runtime calls D3dDrawPrimitives2 with the D3DDP2OP\_CREATEPIXELSHADER operation code. To create a vertex shader in DirectX 8.1 and earlier, the runtime calls D3dDrawPrimitives2 with the D3DDP2OP\_CREATEVERTEXSHADER operation code. To create a vertex shader in DirectX 9.0 and later, the runtime calls D3dDrawPrimitives2 with the D3DDP2OP\_CREATEVERTEXSHADERFUNC operation code.

This section describes the format of an individual shader code and the tokens that comprise each shader code.

[Shader Code Format](shader-code-format.md)

[Shader Code Tokens](shader-code-tokens.md)

[Shader Operation Codes](https://msdn.microsoft.com/library/windows/hardware/ff569706)

[Shader Register Types](https://msdn.microsoft.com/library/windows/hardware/ff569707)

[Shader Relative Addressing](shader-relative-addressing.md)

 

 





