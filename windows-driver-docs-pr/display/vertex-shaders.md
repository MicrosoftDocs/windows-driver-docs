---
title: Vertex Shaders
description: Vertex Shaders
ms.assetid: dfc421f7-b2fe-4023-a47b-cfd59fe5bdb4
keywords:
- vertex shaders WDK DirectX 8.0
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Vertex Shaders


## <span id="ddk_vertex_shaders_gg"></span><span id="DDK_VERTEX_SHADERS_GG"></span>


All drivers that support the DirectX 8.0 DDI must support the new DP2 token D3DDP2OP\_SETVERTEXSHADER even if programmable vertex shaders are not supported in hardware. This is because D3DDP2OP\_SETVERTEXSHADER is the mechanism by which the FVF code of incoming vertex data is communicated to the driver when using fixed function as well as programmable vertex processing.

D3DDP2OP\_SETVERTEXSHADER can be used to notify the driver of either the handle of the current programmable vertex shader to use or the FVF code of the vertex data for fixed function vertex processing. The handle space for vertex shaders is managed by the runtime and includes valid FVF codes. Thus, a vertex shader handle can refer either to a programmable vertex shader handle previously created by means of the D3DDP2OP\_CREATEVERTEXSHADER DP2 token, or to the FVF code of a vertex format to be processed by fixed function vertex processing.

The driver for hardware that does not support programmable vertex processing should process D3DDP2OP\_SETVERTEXSHADER to determine the FVF code (and hence the processing to be performed) on the vertex data bound to stream zero. This is particularly important when processing user memory (UM) primitives. In this case, the only way of determining the FVF code of the supplied vertex data is through the D3DDP2OP\_SETVERTEXSHADER token. If the least significant bit of the handle is set (1), then the handle is vertex shader handler. If the least significant bit is clear (0), then the handle is a legacy FVF code.

If the FVF code of a vertex buffer conflicts with that specified by D3DDP2OP\_SETVERTEXSHADER the driver should ignore the FVF code of the vertex buffer and continue.

The DirectX runtime guarantees that only FVF codes are passed as vertex shader handles to a driver that does not support programmable vertex processing. However, such a driver should have debug code to verify that the FVF code that is passed is supported.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Vertex%20Shaders%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




