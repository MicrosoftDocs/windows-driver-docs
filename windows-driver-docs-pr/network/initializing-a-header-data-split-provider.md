---
title: Initializing a Header-Data Split Provider
description: Initializing a Header-Data Split Provider
ms.assetid: 19a01906-6a05-4f57-a22a-911138095c84
keywords:
- header-data split WDK , initializing provider
- initializing header-data split providers
- header-data split providers WDK
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Initializing a Header-Data Split Provider





To support header-data split, a miniport driver must register as an NDIS 6.1 or later driver. The sources file for the miniport driver must specify DNDIS61\_MINIPORT=1 instead of DNDIS60\_MINIPORT=1. The miniport driver must also specify NDIS 6.1 or a later version in the [**NDIS\_MINIPORT\_DRIVER\_CHARACTERISTICS**](https://msdn.microsoft.com/library/windows/hardware/ff565958) structure.

To register its header-data split attributes, an NDIS 6.1 miniport driver calls the [**NdisMSetMiniportAttributes**](https://msdn.microsoft.com/library/windows/hardware/ff563672) function from its [*MiniportInitializeEx*](https://msdn.microsoft.com/library/windows/hardware/ff559389) function and passes **NdisMSetMiniportAttributes** an initialized [**NDIS\_MINIPORT\_ADAPTER\_HARDWARE\_ASSIST\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff565924) structure.

The NDIS\_MINIPORT\_ADAPTER\_HARDWARE\_ASSIST\_ATTRIBUTES structure contains the following information:

-   The **HDSplitAttributes** member of NDIS\_MINIPORT\_ADAPTER\_HARDWARE\_ASSIST\_ATTRIBUTES contains a pointer to an [**NDIS\_HD\_SPLIT\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff565694) structure that specifies the header-data split capabilities that a miniport adapter provides.

-   The **HardwareCapabilities** member of NDIS\_HD\_SPLIT\_ATTRIBUTES contains the header-data split capabilities that the miniport adapter supports. These capabilities can include capabilities that are currently disabled by INF file settings or through the **Advanced** properties page.

-   The **CurrentCapabilities** member of NDIS\_HD\_SPLIT\_ATTRIBUTES contains the current header-data split capabilities that the miniport adapter supports. If header-data split is enabled through the **\*HeaderDataSplit** standardized INF keyword, the miniport driver uses the same flags as the **HardwareCapabilities** member to indicate the current header-data split configuration. For more information about **\*HeaderDataSplit**, see [Standardized INF Keywords for Header-Data Split](standardized-inf-keywords-for-header-data-split.md).

-   The **HDSplitFlags** member of NDIS\_HD\_SPLIT\_ATTRIBUTES contains header-data split configuration flags. The miniport driver should set this member to zero before calling [**NdisMSetMiniportAttributes**](https://msdn.microsoft.com/library/windows/hardware/ff563672). NDIS sets this member with a bitwise OR of the configuration flags. After **NdisMSetMiniportAttributes** successfully returns, the miniport driver must check the flag settings in **HDSplitFlags** and configure the hardware accordingly.

NDIS uses the NDIS\_HD\_SPLIT\_ENABLE\_HEADER\_DATA\_SPLIT flag to enable header-data split for the miniport adapter. NDIS will not set NDIS\_HD\_SPLIT\_ENABLE\_HEADER\_DATA\_SPLIT if the miniport driver did not set the NDIS\_HD\_SPLIT\_CAPS\_SUPPORTS\_HEADER\_DATA\_SPLIT flag in the **CurrentCapabilities** member of the [**NDIS\_HD\_SPLIT\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff565694) structure. The miniport driver should enable header-data split in the NIC if NDIS sets the NDIS\_HD\_SPLIT\_ENABLE\_HEADER\_DATA\_SPLIT flag.

The miniport driver should set the **BackfillSize** member of the NDIS\_HD\_SPLIT\_ATTRIBUTES structure to zero before calling [**NdisMSetMiniportAttributes**](https://msdn.microsoft.com/library/windows/hardware/ff563672). NDIS sets the **BackfillSize** member if the miniport driver must pre-allocate backfill storage in the data buffer of the split frames. After **NdisMSetMiniportAttributes** successfully returns, the miniport driver must use the **BackfillSize** value that NDIS specified and pre-allocate the data buffers. For more information about the data buffer backfill size, see [Allocating Backfill for the Data Buffer](allocating-backfill-for-the-data-buffer.md).

The miniport driver should set the **MaxHeaderSize** member of the [**NDIS\_HD\_SPLIT\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff565694) structure to zero before calling **NdisMSetMiniportAttributes**. NDIS sets this member to the maximum size that is allowed for the header buffer of the split frames. After **NdisMSetMiniportAttributes** successfully returns, the miniport driver must use the **MaxHeaderSize** value that NDIS specified. For more information about the maximum header size, see [Allocating the Header Buffer](allocating-the-header-buffer.md).

 

 





