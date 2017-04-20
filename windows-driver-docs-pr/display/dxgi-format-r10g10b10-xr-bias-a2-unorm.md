---
title: DXGI\_FORMAT\_R10G10B10\_XR\_BIAS\_A2\_UNORM
description: DXGI\_FORMAT\_R10G10B10\_XR\_BIAS\_A2\_UNORM
ms.assetid: 2aef590f-2328-4175-ab60-c72b1fd83db7
keywords:
- Direct3D version 10.1 WDK Windows 7 display , DXGI_FORMAT_R10G10B10_XR_BIAS_A2_UNORM
- extended format WDK Windows 7 display , DXGI_FORMAT_R10G10B10_XR_BIAS_A2_UNORM
- DXGI_FORMAT_R10G10B10_XR_BIAS_A2_UNORM WDK Windows 7 display
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# DXGI\_FORMAT\_R10G10B10\_XR\_BIAS\_A2\_UNORM


This section applies only to Windows 7 and later operating systems.

The DXGI\_FORMAT\_R10G10B10\_XR\_BIAS\_A2\_UNORM format requires the application to be aware of the biased nature of data that is related to the format. As can be seen from the conversion rules in the following sections, a shader must be aware of XR\_BIAS and must perform its own bias and scale on any data that is read from or written to the DXGI\_FORMAT\_R10G10B10\_XR\_BIAS\_A2\_UNORM format.

Scan-out hardware must be able to apply the bias and scale.

The DXGI\_FORMAT\_R10G10B10\_XR\_BIAS\_A2\_UNORM format has only the display scan-out, CPU lockable, and "cast within bit layout" resource attributes. Therefore, to render to a resource, the application typically creates a render target view of format DXGI\_FORMAT\_R10G10B10A2\_\*.

For full functionality, the display miniport driver must support XR\_BIAS as a display format. The new D3DDDIFMT\_A2B10G10R10\_XR\_BIAS value was added to the [**D3DDDIFORMAT**](https://msdn.microsoft.com/library/windows/hardware/ff544312) enumeration for XR\_BIAS support.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20DXGI_FORMAT_R10G10B10_XR_BIAS_A2_UNORM%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




