---
title: Internal Compatibility Layer
description: Internal Compatibility Layer
ms.assetid: 6cfb3842-751e-4f4c-9fac-daba70245b81
ms.date: 04/20/2017
ms.localizationpriority: medium
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

 

 




