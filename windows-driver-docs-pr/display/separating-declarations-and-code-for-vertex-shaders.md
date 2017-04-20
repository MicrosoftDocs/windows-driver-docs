---
title: Separating Declarations and Code for Vertex Shaders
description: Separating Declarations and Code for Vertex Shaders
ms.assetid: 6da26a8f-553b-4995-9dda-66a7fd6d478b
keywords:
- vertex shader declarations WDK DirectX 9.0 , separating declarations and code
- shader declarations WDK DirectX 9.0 , separating declarations and code
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Separating Declarations and Code for Vertex Shaders


## <span id="ddk_separating_declarations_and_code_for_vertex_shaders_gg"></span><span id="DDK_SEPARATING_DECLARATIONS_AND_CODE_FOR_VERTEX_SHADERS_GG"></span>


In DirectX 9.0, declarations and code for a vertex shader are no longer bound together when the vertex shader is created. A DirectX 9.0 version driver for a device that supports vertex shaders must handle separate creations and management of declaration and code objects. However, this DirectX 9.0 driver must still be able to manage a vertex shader object, which combines both declarations and code, because the DirectX 8.0 runtime might request to create such a vertex shader object. For more information, see [Vertex Shaders](vertex-shaders.md).

The DirectX 9.0 runtime assigns handles from separate handle pools to both declaration and code objects. The DirectX 9.0 driver must store these handles in separate arrays. Like the vertex shader handle space in DirectX 8.0, DirectX 9.0 shares the vertex shader declaration handle space with flexible vertex format (FVF) codes. Setting bit zero of the handle indicates a vertex shader declaration, otherwise a FVF code. For more information, see the reference rasterizer (*refrast.cpp* sample code).

The DirectX 9.0 driver receives a vertex shader declaration when it processes the D3DDP2OP\_CREATEVERTEXSHADERDECL operation code in its [**D3dDrawPrimitives2**](https://msdn.microsoft.com/library/windows/hardware/ff544704) function. A [**D3DHAL\_DP2CREATEVERTEXSHADERDECL**](https://msdn.microsoft.com/library/windows/hardware/ff545480) structure and an array of D3DVERTEXELEMENT9 structures that define the vertex elements that make up the shader declaration follow the operation code in the [command stream](command-stream.md). If the DirectX 9.0 driver is implemented to process vertex elements of the shader declaration, it must support all the possible uses of the vertex data. That is, it must support all the D3DDECLUSAGE types along with multiple meanings (usage-index values) for those types. For more information about D3DVERTEXELEMENT9 and D3DDECLUSAGE, see the latest DirectX SDK documentation.

The DirectX 9.0 driver receives vertex shader code when it processes the D3DDP2OP\_CREATEVERTEXSHADERFUNC operation code. A [**D3DHAL\_DP2CREATEVERTEXSHADERFUNC**](https://msdn.microsoft.com/library/windows/hardware/ff545490) structure and the vertex shader code follow the operation code in the command stream. For more information about the format of individual shader code and the tokens that comprise each shader code, see [Direct3D Driver Shader Codes](https://msdn.microsoft.com/library/windows/hardware/ff552855).

The DirectX 9.0 driver processes the D3DDP2OP\_SETVERTEXSHADERDECL and D3DDP2OP\_SETVERTEXSHADERFUNC operation codes to make particular vertex shader declaration and code current in the vertex shader assembler. The driver processes the D3DDP2OP\_DELETEVERTEXSHADERDECL and D3DDP2OP\_DELETEVERTEXSHADERFUNC operation codes to remove these vertex shader declaration and code from the vertex shader assembler. For each of these operations codes, a [**D3DHAL\_DP2VERTEXSHADER**](https://msdn.microsoft.com/library/windows/hardware/ff545925) structure follows in the command stream. This structure contains just one member that identifies the handle to the declaration or code to set or delete.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Separating%20Declarations%20and%20Code%20for%20Vertex%20Shaders%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




