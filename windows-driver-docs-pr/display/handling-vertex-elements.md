---
title: Handling Vertex Elements
description: Handling Vertex Elements
ms.assetid: b931b674-f8c4-4852-a66a-97d545059287
keywords: ["vertex shader declarations WDK DirectX 9.0 , handling vertex elements", "shader declarations WDK DirectX 9.0 , handling vertex elements", "vertex elements WDK DirectX 9.0", "vertex elements WDK DirectX 9.0 , vertex shader declarations"]
---

# Handling Vertex Elements


## <span id="ddk_handling_vertex_elements_gg"></span><span id="DDK_HANDLING_VERTEX_ELEMENTS_GG"></span>


The number of vertex elements in a shader declaration that a DirectX 9.0 version driver can handle depends on whether the driver's device supports fixed-function or programmable vertex processing. For more information about vertex elements in a shader declaration, see [Separating Declarations and Code for Vertex Shaders](separating-declarations-and-code-for-vertex-shaders.md).

If the device supports fixed-function vertex processing, the driver must handle up to 17 vertex elements (FVF codes).

If the device supports programmable vertex processing, the driver must handle up to 64 vertex elements and skip over those elements that it does not use. Because each channel (4 maximum) of an input register (16 maximum) for a device that supports vertex shader 3\_0 and later can be declared separately, up to 64 (16 \* 4) vertex elements are possible. This maximum number of 64 does not include the end element, which is formed from the D3DDECL\_END macro.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Handling%20Vertex%20Elements%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




