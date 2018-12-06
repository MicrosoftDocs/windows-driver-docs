---
title: Reporting Capabilities for Shader Versions
description: Reporting Capabilities for Shader Versions
ms.assetid: a82ac539-1386-417a-a64f-0a7ddc6d28d9
keywords:
- shaders WDK DirectX 9.0
- vertex shaders WDK DirectX 9.0
- pixel shaders WDK DirectX 9.0
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Reporting Capabilities for Shader Versions


## <span id="ddk_reporting_capabilities_for_shader_versions_gg"></span><span id="DDK_REPORTING_CAPABILITIES_FOR_SHADER_VERSIONS_GG"></span>


The DirectX 9.0 version driver for a display device that supports pixel or vertex shader version 2.0 or 3.0 and later must indicate that it supports a minimum set of capabilities in order to bind the device to the shader version. The driver must set members of the D3DCAPS9 structure to indicate support of the capabilities. The driver returns a D3DCAPS9 structure in response to a **GetDriverInfo2** query similarly to how it returns a D3DCAPS8 structure as described in [Reporting DirectX 8.0 Style Direct3D Capabilities](reporting-directx-8-0-style-direct3d-capabilities.md). Support of this query is described in [Supporting GetDriverInfo2](supporting-getdriverinfo2.md). These capabilities are discussed in the following topics:

[Reporting Capabilities for Shader 2 Support](reporting-capabilities-for-shader-2-support.md)

[Reporting Capabilities for Shader 3 Support](reporting-capabilities-for-shader-3-support.md)

 

 





