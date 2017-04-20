---
title: XPSDrv Driver Recommendations
author: windows-driver-content
description: XPSDrv Driver Recommendations
ms.assetid: 6700afd2-8526-4464-92b8-a9c1a37f8402
keywords:
- Version 3 XPS drivers WDK XPSDrv , recommendations
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# XPSDrv Driver Recommendations


In addition to the [XPSDrv Driver Requirements](xpsdrv-driver-requirements.md), you should consider the following best practices:

-   **Use modular GPD or PPD files.** For Unidrv-based or PScript5-based configuration modules, the print driver should provide a separate GPD or PPD file for each filter. Then, a single "parent" print driver GPD or PPD file should reference all of the per-filter GPD or PPD files. Organizing the GPD and PPD files in a modular fashion by filter helps maintain the modularity and reuse of filters in the filter pipeline.

-   **Map to public Print Schema keywords.** Whenever possible, you should map all print driver settings and print driver capabilitiesto their equivalent keywords in the public Print Schema. Mapping print driver settings to public Print Schema keywords makes it easier for applications to adopt new features. This mapping also provides better synchronization of printer settings between print drivers and applications and system.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20XPSDrv%20Driver%20Recommendations%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


