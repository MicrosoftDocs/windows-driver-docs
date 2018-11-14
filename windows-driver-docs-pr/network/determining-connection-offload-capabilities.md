---
title: Determining Connection Offload Capabilities
description: Determining Connection Offload Capabilities
ms.assetid: 9a7c40dd-7151-462f-b30b-0444a4177ff9
keywords:
- connection offload WDK TCP/IP transport , capabilities
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Determining Connection Offload Capabilities





NDIS supports two categories of offload services: TCP/IP offload services that are enhanced forms of the NDIS 5.1 and earlier task offload services and connection offload services.

NDIS provides the offload hardware capabilities and the current configuration of the underlying miniport adapter to protocol drivers in the [**NDIS\_BIND\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff564832) structure. NDIS provides the task offload hardware capabilities and current configuration of the underlying miniport adapter to filter drivers in the [**NDIS\_FILTER\_ATTACH\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff565481) structure.

Administrative applications use object identifier (OID) queries to obtain TCP/IP offload capabilities of a miniport adapter. However, overlying drivers should avoid using OID queries. Protocol drivers must handle changes in the TCP/IP offload capabilities that underlying drivers report. Miniport drivers can report changes in task offload capabilities in status indications. For a list of status indications, see [NDIS TCP/IP Offload Status Indications](https://msdn.microsoft.com/library/windows/hardware/ff567880).

Administrative applications (or overlying drivers) can determine the current connection offload configuration of a NIC by querying the [OID\_TCP\_CONNECTION\_OFFLOAD\_CURRENT\_CONFIG](https://msdn.microsoft.com/library/windows/hardware/ff569802) OID. The [**NDIS\_TCP\_CONNECTION\_OFFLOAD**](https://msdn.microsoft.com/library/windows/hardware/ff567875) structure that is associated with OID\_TCP\_CONNECTION\_OFFLOAD\_CURRENT\_CONFIG specifies the miniport adapter's current connection-offload configuration.

 

 





