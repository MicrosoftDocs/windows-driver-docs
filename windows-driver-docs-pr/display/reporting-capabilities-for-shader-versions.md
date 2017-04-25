---
title: Reporting Capabilities for Shader Versions
description: Reporting Capabilities for Shader Versions
ms.assetid: a82ac539-1386-417a-a64f-0a7ddc6d28d9
keywords:
- shaders WDK DirectX 9.0
- vertex shaders WDK DirectX 9.0
- pixel shaders WDK DirectX 9.0
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Reporting Capabilities for Shader Versions


## <span id="ddk_reporting_capabilities_for_shader_versions_gg"></span><span id="DDK_REPORTING_CAPABILITIES_FOR_SHADER_VERSIONS_GG"></span>


The DirectX 9.0 version driver for a display device that supports pixel or vertex shader version 2.0 or 3.0 and later must indicate that it supports a minimum set of capabilities in order to bind the device to the shader version. The driver must set members of the D3DCAPS9 structure to indicate support of the capabilities. The driver returns a D3DCAPS9 structure in response to a **GetDriverInfo2** query similarly to how it returns a D3DCAPS8 structure as described in [Reporting DirectX 8.0 Style Direct3D Capabilities](reporting-directx-8-0-style-direct3d-capabilities.md). Support of this query is described in [Supporting GetDriverInfo2](supporting-getdriverinfo2.md). These capabilities are discussed in the following topics:

[Reporting Capabilities for Shader 2 Support](reporting-capabilities-for-shader-2-support.md)

[Reporting Capabilities for Shader 3 Support](reporting-capabilities-for-shader-3-support.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Reporting%20Capabilities%20for%20Shader%20Versions%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




