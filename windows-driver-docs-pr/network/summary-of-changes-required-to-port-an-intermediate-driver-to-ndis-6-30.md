---
title: Summary of changes to port an intermediate driver to NDIS 6.30
description: To update an NDIS 6.x intermediate (IM) driver to support NDIS 6.30, you must modify it as outlined in the following sections.
ms.assetid: 02FAC8B2-16B1-49C2-8B3A-29535A698CEA
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Summary of Changes Required to Port an Intermediate Driver to NDIS 6.30


To update an NDIS 6.x intermediate (IM) driver to support NDIS 6.30, you must modify it as outlined in the following sections.

## Build Environment


-   Replace the preprocessor definition NDIS60 or NDIS61 or NDIS620, if present, with NDIS630.
-   Update the major and minor NDIS version number in the NDIS\_*Xxx*\_DRIVER\_CHARACTERISTICS structure as described in [Implementing an NDIS 6.30 Driver](implementing-an-ndis-6-30-driver.md).

## General Porting Requirements


-   Except where noted otherwise, protocol driver and miniport driver changes also apply to intermediate drivers. For more information about porting these drivers, see the [Summary of Changes Required to Port a Protocol or Filter Driver to NDIS 6.30](summary-of-changes-required-to-port-a-protocol-or-filter-driver-to-ndis-6-30.md) and [Summary of Changes Required to Port a Miniport Driver to NDIS 6.30](summary-of-changes-required-to-port-a-miniport-driver-to-ndis-6-30.md).

 

 





