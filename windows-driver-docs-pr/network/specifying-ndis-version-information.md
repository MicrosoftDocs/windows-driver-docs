---
title: Specifying NDIS Version Information
description: Specifying NDIS Version Information
ms.assetid: 9d007046-01c5-4bf8-adda-b88b596945d6
keywords:
- NDIS version information WDK
- versioning WDK networking
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Specifying NDIS Version Information





This section provides an overview of the support that NDIS and NDIS drivers provide for NDIS version information.

Many NDIS structures include structure version information in a **Header** member. NDIS or NDIS drivers set the version information in such structures. NDIS drivers should check the version information in structures before they access the structure members.

Also, NDIS drivers specify the NDIS version that they support during driver initialization.

This section includes the following topics:

-   [Overview of NDIS Support for Header Versions](overview-of-ndis-support-for-header-versions.md)
-   [Version Information Requirements for NDIS Drivers](version-information-requirements-for-ndis-drivers.md)
-   [Version Information Requirements for NDIS](version-information-requirements-for-ndis.md)
-   [Obtaining the NDIS Version](obtaining-the-ndis-version.md)
-   [NDIS Object Version Issues for WMI](ndis-object-version-issues-for-wmi.md)

## Related topics


[Overview of NDIS versions](overview-of-ndis-versions.md)

 

 






