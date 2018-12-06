---
title: Allocating Backfill for the Data Buffer
description: Allocating Backfill for the Data Buffer
ms.assetid: 2588986d-8d51-4f34-a3b9-d0df406afcba
keywords:
- header-data split WDK , backfill allocation
- backfill space allocations WDK header-data split
- pre-allocated backfill storage WDK header-data split
- data backfill space WDK header-data split
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Allocating Backfill for the Data Buffer





NDIS specifies the amount of data backfill space that the miniport driver should allocate in the **BackfillSize** member of the [**NDIS\_HD\_SPLIT\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff565694) structure. For more information about setting header-data split attributes, see [Initializing a Header-Data Split Provider](initializing-a-header-data-split-provider.md).

When a NIC splits the header and data in a received Ethernet frame, the miniport driver must pre-allocate backfill storage of at least the number of bytes that **BackfillSize** specifies before the starting address of data portion of the frame. The backfill storage must not cross a page boundary.

The driver stack can use the pre-allocated backfill storage to copy the header portion of the frame and create a virtually contiguous frame for network drivers that cannot handle split Ethernet frames.

 

 





