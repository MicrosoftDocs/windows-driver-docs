---
title: Summary of changes to port an intermediate driver to NDIS 6.20
description: Summary of Changes Required to Port an Intermediate Driver to NDIS 6.20
ms.assetid: 1ed2b2f6-f337-4aaa-9ce8-90adf7d05722
keywords:
- NDIS 6.20 WDK , porting intermediate drivers
- porting intermediate drivers to NDIS 6.20 WDK
- intermediate drivers WDK
- intermediate drivers WDK , porting to NDIS 6.20
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Summary of Changes Required to Port an Intermediate Driver to NDIS 6.20





This topic summarizes the changes that are required to port an NDIS 6.*x* intermediate driver to NDIS 6.20.

To update an intermediate driver to support the NDIS 6.20 environment, you must modify the NDIS 6.*x* intermediate driver as follows:

<a href="" id="build-environment-------"></a>**Build Environment**   
-   Replace the preprocessor definition NDIS60\_MINIPORT\_DRIVER or NDIS61\_MINIPORT\_DRIVER with NDIS620\_MINIPORT\_DRIVER.

-   Replace the preprocessor definition NDIS61 or NDIS60 with NDIS620.

<a href="" id="general-porting-requirements-------"></a>**General Porting Requirements**   
-   Except where noted otherwise, protocol driver and miniport driver changes also apply to intermediate drivers. For more information about porting these drivers, see the protocol driver porting summary at [Summary of Changes Required to Port a Protocol Driver to NDIS 6.20](summary-of-changes-required-to-port-a-protocol-driver-to-ndis-6-20.md) and the miniport driver porting summary at [Summary of Changes Required to Port a Miniport Driver to NDIS 6.20](summary-of-changes-required-to-port-a-miniport-driver-to-ndis-6-20.md).

-   NDIS 5.x filter intermediate drivers will not be supported in Microsoft Windows versions after Windows 7. You should use the NDIS filter drivers interface for all filter drivers. For more information about NDIS filter drivers, see [Summary of Changes Required to Port a Filter Driver to NDIS 6.20](summary-of-changes-required-to-port-a-filter-driver-to-ndis-6-20.md).

 

 





