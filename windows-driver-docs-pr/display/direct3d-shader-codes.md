---
title: Direct3D Shader Codes
description: Direct3D Shader Codes
ms.assetid: 30d14bbe-10fe-46fc-99b3-ab2f989abb29
ms.author: windowsdriverdev
ms.date: 01/05/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Direct3D Shader Codes


Pixel shader code follows the D3DHAL\_DP2CREATEPIXELSHADER structure in the command stream. For DirectX 8.1 and earlier, vertex shader code follows the D3DHAL\_DP2CREATEVERTEXSHADER structure. For DirectX 9.0 and later, vertex shader code follows the D3DHAL\_DP2CREATEVERTEXSHADERFUNC structure. The runtime creates either a pixel or vertex shader when it calls a driver's D3dDrawPrimitives2 function. To create a pixel shader, the runtime calls D3dDrawPrimitives2 with the D3DDP2OP\_CREATEPIXELSHADER operation code. To create a vertex shader in DirectX 8.1 and earlier, the runtime calls D3dDrawPrimitives2 with the D3DDP2OP\_CREATEVERTEXSHADER operation code. To create a vertex shader in DirectX 9.0 and later, the runtime calls D3dDrawPrimitives2 with the D3DDP2OP\_CREATEVERTEXSHADERFUNC operation code.

This section describes the format of an individual shader code and the tokens that comprise each shader code.

[Shader Code Format](shader-code-format.md)

[Shader Code Tokens](shader-code-tokens.md)

[Shader Operation Codes](https://msdn.microsoft.com/library/windows/hardware/ff569706)

[Shader Register Types](https://msdn.microsoft.com/library/windows/hardware/ff569707)

[Shader Relative Addressing](shader-relative-addressing.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Direct3D%20Shader%20Codes%20%20RELEASE:%20%281/4/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




