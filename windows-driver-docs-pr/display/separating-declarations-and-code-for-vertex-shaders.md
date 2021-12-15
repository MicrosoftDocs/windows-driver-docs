---
title: Separating Declarations and Code for Vertex Shaders
description: Separating Declarations and Code for Vertex Shaders
keywords:
- vertex shader declarations WDK DirectX 9.0 , separating declarations and code
- shader declarations WDK DirectX 9.0 , separating declarations and code
ms.date: 04/20/2017
---

# Separating Declarations and Code for Vertex Shaders

In DirectX 9.0, declarations and code for a vertex shader are no longer bound together when the vertex shader is created. A DirectX 9.0 version driver for a device that supports vertex shaders must handle separate creations and management of declaration and code objects. However, this DirectX 9.0 driver must still be able to manage a vertex shader object, which combines both declarations and code, because the DirectX 8.0 runtime might request to create such a vertex shader object. For more information, see [Vertex Shaders](vertex-shaders.md).

The DirectX 9.0 runtime assigns handles from separate handle pools to both declaration and code objects. The DirectX 9.0 driver must store these handles in separate arrays. Like the vertex shader handle space in DirectX 8.0, DirectX 9.0 shares the vertex shader declaration handle space with flexible vertex format (FVF) codes. Setting bit zero of the handle indicates a vertex shader declaration, otherwise a FVF code. For more information, see the reference rasterizer (*refrast.cpp* sample code).

The DirectX 9.0 driver receives a vertex shader declaration when it processes the D3DDP2OP_CREATEVERTEXSHADERDECL operation code in its [**D3dDrawPrimitives2**](/windows-hardware/drivers/ddi/d3dhal/nc-d3dhal-lpd3dhal_drawprimitives2cb) function. A [**D3DHAL_DP2CREATEVERTEXSHADERDECL**](/windows-hardware/drivers/ddi/d3dhal/ns-d3dhal-_d3dhal_dp2createvertexshaderdecl) structure and an array of D3DVERTEXELEMENT9 structures that define the vertex elements that make up the shader declaration follow the operation code in the [command stream](command-stream.md). If the DirectX 9.0 driver is implemented to process vertex elements of the shader declaration, it must support all the possible uses of the vertex data. That is, it must support all the D3DDECLUSAGE types along with multiple meanings (usage-index values) for those types. For more information about D3DVERTEXELEMENT9 and D3DDECLUSAGE, see the latest DirectX SDK documentation.

The DirectX 9.0 driver receives vertex shader code when it processes the D3DDP2OP_CREATEVERTEXSHADERFUNC operation code. A [**D3DHAL_DP2CREATEVERTEXSHADERFUNC**](/windows-hardware/drivers/ddi/d3dhal/ns-d3dhal-_d3dhal_dp2createvertexshaderfunc) structure and the vertex shader code follow the operation code in the command stream. For more information about the format of individual shader code and the tokens that comprise each shader code, see [Direct3D Driver Shader Codes](direct3d-shader-codes.md).

The DirectX 9.0 driver processes the D3DDP2OP_SETVERTEXSHADERDECL and D3DDP2OP_SETVERTEXSHADERFUNC operation codes to make particular vertex shader declaration and code current in the vertex shader assembler. The driver processes the D3DDP2OP_DELETEVERTEXSHADERDECL and D3DDP2OP_DELETEVERTEXSHADERFUNC operation codes to remove these vertex shader declaration and code from the vertex shader assembler. For each of these operations codes, a [**D3DHAL_DP2VERTEXSHADER**](/windows-hardware/drivers/ddi/d3dhal/ns-d3dhal-_d3dhal_dp2vertexshader) structure follows in the command stream. This structure contains just one member that identifies the handle to the declaration or code to set or delete.
