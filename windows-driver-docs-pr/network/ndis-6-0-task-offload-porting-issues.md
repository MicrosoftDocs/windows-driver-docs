---
title: NDIS 6.0 Task Offload Porting Issues
description: NDIS 6.0 Task Offload Porting Issues
ms.assetid: f8da32a6-3c44-48c4-a43b-886638a63105
keywords:
- task offload porting WDK networking , about porting task offload services
- TCP/IP offload service porting WDK networking , about porting task offload services
- offload service porting WDK networking , about porting task offload services
- porting task of
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# NDIS 6.0 Task Offload Porting Issues





This section summarizes how you can port NDIS drivers that provide offload services to NDIS 6.0. NDIS 6.0 supports the task offload services that NDIS 5.1 supports, enhances the NDIS 5.1 services, and provides additional offload services that are not included in NDIS 5.1 and earlier versions. To enable NDIS 5.1 and earlier drivers to exist in a driver stack with NDIS 6.0 drivers, NDIS provides translation services.

To port a task offload capable NDIS driver from NDIS 5.1 to NDIS 6.0, you should be familiar with the NDIS 5.1 task offload implementation. For more information about NDIS 5.1 task offload, see [Task Offload (NDIS 5.1)](https://msdn.microsoft.com/library/windows/hardware/ff564239).

This section includes:

[NDIS 6.0 Support for Task Offload](ndis-6-0-support-for-task-offload.md)

[NDIS 6.0 Task Offload Backward Compatibility](ndis-6-0-task-offload-backward-compatibility.md)

[Summary of NDIS 6.0 Task Offload Porting Issues for Protocol Drivers](summary-of-ndis-6-0-task-offload-porting-issues-for-protocol-drivers.md)

[Summary of NDIS 6.0 Task Offload Porting Issues for Miniport Drivers](summary-of-ndis-6-0-task-offload-porting-issues-for-miniport-drivers.md)

[Summary of Task Offload Support in NDIS 6.0 Filter Drivers](summary-of-task-offload-support-in-ndis-6-0-filter-drivers.md)

 

 





