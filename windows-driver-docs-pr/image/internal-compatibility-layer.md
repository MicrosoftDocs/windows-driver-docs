---
title: Internal Compatibility Layer
author: windows-driver-content
description: Internal Compatibility Layer
ms.assetid: 6cfb3842-751e-4f4c-9fac-daba70245b81
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Internal Compatibility Layer


You must consider two aspects of compatibility when you develop drivers to run on Windows Vista:

-   When applications that are intended for Windows XP or earlier operating systems communicate with Windows Vista drivers

-   When Windows Vista applications communicate with Windows XP drivers (that is, *legacy drivers*)

You do not need to consider other situations, such as when a Windows Vista application communicates with a Windows Vista driver or when a Windows XP application communicates with a Windows XP driver, because these situations do not require any compatibility components.

WIA provides an internal compatibility layer that performs all necessary conversions. Therefore, Windows XP applications that run on Windows Vista will be able to communicate with Windows Vista drivers, and Windows Vista applications will be able to communicate with Windows XP drivers that run on Windows Vista.

There are several limitations of the compatibility layer:

-   Only legacy drivers are translated for Windows Vista WIA applications.

-   Only Windows Vista scanner drivers that implement flatbed and feeder as their base items (WIA\_CATEGORY\_FLATBED and WIA\_CATEGORY\_FEEDER) are translated for legacy WIA applications.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Internal%20Compatibility%20Layer%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


