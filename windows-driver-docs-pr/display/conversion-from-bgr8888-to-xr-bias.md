---
title: Conversion from BGR8888 to XR_BIAS
description: Conversion from BGR8888 to XR_BIAS
ms.assetid: 53145cfe-d344-4242-b124-ddb507d876ad
keywords:
- Direct3D version 10.1 WDK Windows 7 display , converting BGR8888 to XR_BIAS
- extended format WDK Windows 7 display , converting BGR8888 to XR_BIAS
- converting BGR8888 to XR_BIAS WDK Windows 7 display
- BGR8888 WDK Windows 7 display
- BGR8888 WDK Windows 7 display , conversion to XR_BIAS
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Conversion from BGR8888 to XR\_BIAS


This section applies only to Windows 7 and later operating systems.

The conversion from BGR8888-type formats (for example, DXGI\_FORMAT\_B8G8R8A8\_UNORM) to XR\_BIAS is lossless.

The scale factor of 510 is explicitly chosen to provide a cleanly invertible conversion between a BGR8888-type format and XR\_BIAS without causing the nonlinear jump near 0.5 that would be implied by a scale factor of 511.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Conversion%20from%20BGR8888%20to%20XR_BIAS%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




