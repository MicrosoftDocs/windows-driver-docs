---
title: Setting the Current Header-Data Split Configuration
description: Setting the Current Header-Data Split Configuration
ms.assetid: b5b20ce8-1522-4729-8d0a-bc2d2c5afff2
keywords:
- header-data split WDK , configuration
- current header-data split configuration WDK networking
- status information WDK header-data split
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Setting the Current Header-Data Split Configuration





NDIS and overlying drivers or user-mode applications use the [OID\_GEN\_HD\_SPLIT\_PARAMETERS](https://msdn.microsoft.com/library/windows/hardware/ff569587) OID to set the current header-data split settings of a miniport adapter. NDIS 6.1 and later miniport drivers that provide header-data split services must support this OID. Otherwise, this OID is optional.

A system administrator can use the GUID that is associated with this OID through the WMI interface. For more information about header-data split WMI GUIDs, see [WMI Support for Header-Data Split](wmi-support-for-header-data-split.md).

The **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure contains an [**NDIS\_HD\_SPLIT\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff565701) structure.

If the NDIS\_HD\_SPLIT\_COMBINE\_ALL\_HEADERS flag in the **HDSplitCombineFlags** member of NDIS\_HD\_SPLIT\_PARAMETERS is set, the miniport adapter must combine all split frames. If header-data split is enabled in the hardware, the miniport driver must combine the header and data before the driver indicates the frame to NDIS.

For example, NDIS might use the OID\_GEN\_HD\_SPLIT\_PARAMETERS OID to set the NDIS\_HD\_SPLIT\_COMBINE\_ALL\_HEADERS flag when an NDIS 5.*x* protocol driver binds to an NDIS 6.1 miniport adapter. NDIS processes this OID before it passes the OID to the miniport driver and updates the miniport adapter's **\*HeaderDataSplit** standardized keyword, if required. If header-data split is disabled, NDIS does not send this OID to the miniport adapter.

 

 





