---
title: Summary of changes to port protocol or filter drivers to NDIS 6.3
description: To update an NDIS 6.x protocol or filter driver to support NDIS 6.30, you must modify it as outlined in the following sections.
ms.assetid: 1C6CB2E1-C129-4F3B-AF7D-357580BEE7F8
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Summary of Changes Required to Port a Protocol or Filter Driver to NDIS 6.30


To update an NDIS 6.x protocol or filter driver to support NDIS 6.30, you must modify it as outlined in the following sections.

-   [Build Environment](#build-environment)
-   [General Porting Requirements for Protocol Drivers](#general-porting-requirements-for-protocol-drivers)
-   [General Porting Requirements for Filter Drivers](#general-porting-requirements-for-filter-drivers)

## Build Environment


-   Replace the preprocessor definition NDIS60 or NDIS61 or NDIS620, if present, with NDIS630.
-   Update the major and minor NDIS version number in the NDIS\_*Xxx*\_DRIVER\_CHARACTERISTICS structure as described in [Implementing an NDIS 6.30 Driver](implementing-an-ndis-6-30-driver.md).

## General Porting Requirements for Protocol Drivers


A protocol driver should always complete **NetEventSetPower** without waiting for packets. For more information, see:

-   [Power Management Enhancements in NDIS 6.30](power-management-enhancements-in-ndis-6-30.md)
-   [Handling PnP Events and Power Management Events in a Protocol Driver](handling-pnp-events-and-power-management-events-in-a-protocol-driver.md)

For more information about NDIS 6.30 features, see [Introduction to NDIS 6.30](introduction-to-ndis-6-30.md).

## General Porting Requirements for Filter Drivers


A filter driver should always complete **NetEventSetPower** without waiting for packets. For more information, see:

-   [Power Management Enhancements in NDIS 6.30](power-management-enhancements-in-ndis-6-30.md)
-   [**NDIS\_MINIPORT\_ADAPTER\_REGISTRATION\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff565934)
-   [**NET\_PNP\_EVENT**](https://msdn.microsoft.com/library/windows/hardware/ff568751)
-   [OID\_PNP\_SET\_POWER](https://msdn.microsoft.com/library/windows/hardware/ff569780)

For more information about NDIS 6.30 features, see [Introduction to NDIS 6.30](introduction-to-ndis-6-30.md).

 

 





