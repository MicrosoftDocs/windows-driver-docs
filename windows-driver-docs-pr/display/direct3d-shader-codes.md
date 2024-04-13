---
title: Direct3D Shader Codes
description: Direct3D Shader Codes
ms.date: 01/05/2018
---

# Direct3D Shader Codes


Pixel shader code follows the D3DHAL\_DP2CREATEPIXELSHADER structure in the command stream. For DirectX 8.1 and earlier, vertex shader code follows the D3DHAL\_DP2CREATEVERTEXSHADER structure. For DirectX 9.0 and later, vertex shader code follows the D3DHAL\_DP2CREATEVERTEXSHADERFUNC structure. The runtime creates either a pixel or vertex shader when it calls a driver's D3dDrawPrimitives2 function. To create a pixel shader, the runtime calls D3dDrawPrimitives2 with the D3DDP2OP\_CREATEPIXELSHADER operation code. To create a vertex shader in DirectX 8.1 and earlier, the runtime calls D3dDrawPrimitives2 with the D3DDP2OP\_CREATEVERTEXSHADER operation code. To create a vertex shader in DirectX 9.0 and later, the runtime calls D3dDrawPrimitives2 with the D3DDP2OP\_CREATEVERTEXSHADERFUNC operation code.

This section describes the format of an individual shader code and the tokens that comprise each shader code.

[Shader Code Format](shader-code-format.md)

[Shader Code Tokens](shader-code-tokens.md)

[Shader Operation Codes](/windows-hardware/drivers/ddi/d3d9types/ne-d3d9types-_d3dshader_instruction_opcode_type)

[Shader Register Types](/windows-hardware/drivers/ddi/d3d9types/ne-d3d9types-_d3dshader_param_register_type)

[Shader Relative Addressing](shader-relative-addressing.md)

 

