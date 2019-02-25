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
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Conversion from BGR8888 to XR\_BIAS


This section applies only to Windows 7 and later operating systems.

The conversion from BGR8888-type formats (for example, DXGI\_FORMAT\_B8G8R8A8\_UNORM) to XR\_BIAS is lossless.

The scale factor of 510 is explicitly chosen to provide a cleanly invertible conversion between a BGR8888-type format and XR\_BIAS without causing the nonlinear jump near 0.5 that would be implied by a scale factor of 511.

 

 





