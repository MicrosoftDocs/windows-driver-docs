---
title: Summary of Task Offload Support in NDIS 6.0 Filter Drivers
description: Summary of Task Offload Support in NDIS 6.0 Filter Drivers
ms.assetid: 7df5beb4-b694-4550-87a1-cf3c0f2d965c
keywords:
- task offload porting WDK networking , filter drivers
- TCP/IP offload service porting WDK networking , filter drivers
- offload service porting WDK networking , filter drivers
- porting task offload services WDK networking , filter drivers
- filter drivers
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Summary of Task Offload Support in NDIS 6.0 Filter Drivers





NDIS 6.0 filter drivers can modify the task offload services that an underlying driver stack reports. You must consider the following issues when you create offload-aware filter drivers:

-   Filter drivers are provided with the offload capabilities of an underlying miniport adapter in the [**NDIS\_FILTER\_ATTACH\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff565481) structure when they are attached to the driver stack. Filter drivers must handle the [**NDIS\_STATUS\_TASK\_OFFLOAD\_CURRENT\_CONFIG**](https://msdn.microsoft.com/library/windows/hardware/ff567424) status indication to receive updated capabilities.

-   Filter drivers can monitor offload object identifiers (OIDs) and modify the responses of underlying drivers. For more information about NDIS 6.0 offload OIDs, see [NDIS 6.0 Task Offload OIDs](https://msdn.microsoft.com/library/windows/hardware/ff567879).

-   NDIS 6.0 filter drivers must not issue [OID\_TCP\_TASK\_OFFLOAD](https://msdn.microsoft.com/library/windows/hardware/ff569815) OID requests.

For general information about NDIS 6.0 filter drivers, see [Introduction to NDIS Filter Drivers](introduction-to-ndis-filter-drivers.md).

 

 





