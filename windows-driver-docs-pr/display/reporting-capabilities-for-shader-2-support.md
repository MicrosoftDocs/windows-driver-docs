---
title: Reporting Capabilities for Shader 2 Support
description: Reporting Capabilities for Shader 2 Support
ms.assetid: 27397e32-cdc0-47b5-b9b5-a4b22ed971f3
keywords:
- shaders WDK DirectX 9.0 , shader 2.0 support
- vertex shaders WDK DirectX 9.0 , shader 2.0 support
- pixel shaders WDK DirectX 9.0 , shader 2.0 support
ms.date: 04/20/2017
ms.localizationpriority: medium
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

 

 





