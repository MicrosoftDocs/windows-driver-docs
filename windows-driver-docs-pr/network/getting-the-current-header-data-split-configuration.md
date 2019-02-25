---
title: Getting the Current Header-Data Split Configuration
description: Getting the Current Header-Data Split Configuration
ms.assetid: 62c5e362-4e19-465d-85a8-a8277cb46f5d
keywords:
- header-data split WDK , configuration
- current header-data split configuration WDK networking
- status information WDK header-data split
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Getting the Current Header-Data Split Configuration





To get the current header-data split settings of a miniport adapter, overlying drivers or user-mode applications can query the [OID\_GEN\_HD\_SPLIT\_CURRENT\_CONFIG](https://msdn.microsoft.com/library/windows/hardware/ff569586) OID. However, overlying drivers should use the information that NDIS provides to them during initialization and with status indications.

A system administrator can use the GUID that is associated with the OID\_GEN\_HD\_SPLIT\_CURRENT\_CONFIG OID through the WMI interface. For more information about header-data split WMI GUIDs, see [WMI Support for Header-Data Split](wmi-support-for-header-data-split.md).

NDIS handles [OID\_GEN\_HD\_SPLIT\_CURRENT\_CONFIG](https://msdn.microsoft.com/library/windows/hardware/ff569586) on behalf of the miniport driver. NDIS maintains the current header-data split configuration information based on the miniport driver initialization attributes and the [**NDIS\_STATUS\_HD\_SPLIT\_CURRENT\_CONFIG**](https://msdn.microsoft.com/library/windows/hardware/ff567370) status indication.

The **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure contains an [**NDIS\_HD\_SPLIT\_CURRENT\_CONFIG**](https://msdn.microsoft.com/library/windows/hardware/ff565696) structure. NDIS also provides the NDIS\_HD\_SPLIT\_CURRENT\_CONFIG structure to overlying drivers during initialization and with the status indication.

When a miniport driver receives an [OID\_GEN\_HD\_SPLIT\_PARAMETERS](https://msdn.microsoft.com/library/windows/hardware/ff569587) set request, the driver must use the contents of the [**NDIS\_HD\_SPLIT\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff565701) structure to update the current configuration of the miniport adapter. After the update, the miniport driver must report the changes with the [**NDIS\_STATUS\_HD\_SPLIT\_CURRENT\_CONFIG**](https://msdn.microsoft.com/library/windows/hardware/ff567370) status indication. The status indication ensures that all of the overlying drivers are updated with the new information.

When NDIS calls the [*ProtocolBindAdapterEx*](https://msdn.microsoft.com/library/windows/hardware/ff570220) function of NDIS 6.1 or later protocol drivers, NDIS provides an [**NDIS\_BIND\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff564832) structure with a pointer to an [**NDIS\_HD\_SPLIT\_CURRENT\_CONFIG**](https://msdn.microsoft.com/library/windows/hardware/ff565696) structure.

When NDIS calls the [*FilterAttach*](https://msdn.microsoft.com/library/windows/hardware/ff549905) function of NDIS 6.1 or later filter drivers, NDIS provides an [**NDIS\_FILTER\_ATTACH\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff565481) structure with a pointer to an NDIS\_HD\_SPLIT\_CURRENT\_CONFIG structure.

 

 





