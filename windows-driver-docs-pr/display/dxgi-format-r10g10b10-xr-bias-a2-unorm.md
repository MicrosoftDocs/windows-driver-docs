---
title: DXGI_FORMAT_R10G10B10_XR_BIAS_A2_UNORM
description: DXGI_FORMAT_R10G10B10_XR_BIAS_A2_UNORM
ms.assetid: 2aef590f-2328-4175-ab60-c72b1fd83db7
keywords:
- Direct3D version 10.1 WDK Windows 7 display , DXGI_FORMAT_R10G10B10_XR_BIAS_A2_UNORM
- extended format WDK Windows 7 display , DXGI_FORMAT_R10G10B10_XR_BIAS_A2_UNORM
- DXGI_FORMAT_R10G10B10_XR_BIAS_A2_UNORM WDK Windows 7 display
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# DXGI\_FORMAT\_R10G10B10\_XR\_BIAS\_A2\_UNORM


This section applies only to Windows 7 and later operating systems.

The DXGI\_FORMAT\_R10G10B10\_XR\_BIAS\_A2\_UNORM format requires the application to be aware of the biased nature of data that is related to the format. As can be seen from the conversion rules in the following sections, a shader must be aware of XR\_BIAS and must perform its own bias and scale on any data that is read from or written to the DXGI\_FORMAT\_R10G10B10\_XR\_BIAS\_A2\_UNORM format.

Scan-out hardware must be able to apply the bias and scale.

The DXGI\_FORMAT\_R10G10B10\_XR\_BIAS\_A2\_UNORM format has only the display scan-out, CPU lockable, and "cast within bit layout" resource attributes. Therefore, to render to a resource, the application typically creates a render target view of format DXGI\_FORMAT\_R10G10B10A2\_\*.

For full functionality, the display miniport driver must support XR\_BIAS as a display format. The new D3DDDIFMT\_A2B10G10R10\_XR\_BIAS value was added to the [**D3DDDIFORMAT**](https://msdn.microsoft.com/library/windows/hardware/ff544312) enumeration for XR\_BIAS support.

 

 





