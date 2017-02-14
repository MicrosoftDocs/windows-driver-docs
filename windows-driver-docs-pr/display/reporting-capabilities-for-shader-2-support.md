---
title: Reporting Capabilities for Shader 2 Support
description: Reporting Capabilities for Shader 2 Support
ms.assetid: 27397e32-cdc0-47b5-b9b5-a4b22ed971f3
keywords: ["shaders WDK DirectX 9.0 , shader 2.0 support", "vertex shaders WDK DirectX 9.0 , shader 2.0 support", "pixel shaders WDK DirectX 9.0 , shader 2.0 support"]
---

# Reporting Capabilities for Shader 2 Support


## <span id="ddk_reporting_capabilities_for_shader_2_support_gg"></span><span id="DDK_REPORTING_CAPABILITIES_FOR_SHADER_2_SUPPORT_GG"></span>


The DirectX 9.0 version driver for a display device that supports pixel or vertex shader version 2.0 and later must indicate that it supports the following capabilities:

If a device supports vertex shader 2.0 and later, its driver must set the members of the D3DCAPS9 structure to the following values:

-   Set the **MaxStreams** member to be at least 8 to indicate that the device can handle 8 or more concurrent data streams.

-   Set the D3DDTCAPS\_UBYTE4 bit in the **DeclTypes** member to 1 to indicate support of the UBYTE4 vertex element type. For more information, see [Reporting Support of UBYTE4 Vertex Element](reporting-support-of-ubyte4-vertex-element.md).

If a device supports pixel shader 2.0 and later, its driver must configure the following bits in the **TextureCaps** member to indicate whether the driver supports 2-D texture mapping as nonpowers-of-2 conditionally or unconditionally. For more information, see the description of these bits in the [**D3DPRIMCAPS**](https://msdn.microsoft.com/library/windows/hardware/ff549034) reference page.

-   Set the D3DPTEXTURECAPS\_POW2 and D3DPTEXTURECAPS\_NONPOW2CONDITIONAL bits to 1 to indicate conditional support.

-   Set the D3DPTEXTURECAPS\_POW2 and D3DPTEXTURECAPS\_NONPOW2CONDITIONAL bits to 0 (that is, do not set these bits) to indicate unconditional support.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Reporting%20Capabilities%20for%20Shader%202%20Support%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




