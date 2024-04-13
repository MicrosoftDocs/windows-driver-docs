---
title: Processing Shader Codes
description: Processing Shader Codes
keywords:
- user-mode display drivers WDK Windows Vista , shader codes
- shader codes WDK display
- pixel shader codes WDK display
- vertex shader codes WDK display
- vertex declarations WDK display
- tokens WDK display
- end tokens WDK display
- declarations WDK display
ms.date: 04/20/2017
---

# Processing Shader Codes


The user-mode display driver uses vertex declarations, and the tokens within each individual pixel and vertex shader code, to program shader assemblers.

The user-mode display driver receives vertex and pixel shader code when the Microsoft Direct3D runtime calls the driver's [**CreateVertexShaderFunc**](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_createvertexshaderfunc) and [**CreatePixelShader**](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_createpixelshader) functions, respectively. The user-mode display driver receives vertex declarations when the runtime calls the driver's [**CreateVertexShaderDecl**](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_createvertexshaderdecl) function. The vertex declarations consist of arrays of [**D3DDDIVERTEXELEMENT**](/windows-hardware/drivers/ddi/d3dumddi/ns-d3dumddi-_d3dddivertexelement) structures. The user-mode display driver converts shader code and vertex shader declarations into a hardware-specific format and associates the shader code and declarations with shader and declaration handles. The runtime uses the created handles in calls to the [**SetVertexShaderDecl**](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_setvertexshaderdecl), [**SetVertexShaderFunc**](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_setvertexshaderfunc), and [**SetPixelShader**](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_setpixelshader) functions to set the vertex shader declaration and the vertex and pixel shaders so that all subsequent drawing operations use them.

For more information about the format of an individual shader code and the tokens that comprise each shader code, see [Direct3D Shader Codes](./direct3d-shader-codes.md).

**Note**   When an application creates vertex shaders, pixel shaders, and vertex declarations, the shader code and declaration for each ends with an [end token](./end-token.md). When the Direct3D runtime, in turn, passes vertex and pixel shader creation requests to the user-mode display driver, the vertex and pixel shader code that accompanies the requests ends with end tokens. However, when the runtime passes vertex declaration creation requests, the vertex declarations that accompany the requests do not end with end tokens.

 

 

