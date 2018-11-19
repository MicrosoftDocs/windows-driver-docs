---
title: Summary of NDIS 6.0 Task Offload Porting Issues for Protocol Drivers
description: Summary of NDIS 6.0 Task Offload Porting Issues for Protocol Drivers
ms.assetid: 76462948-db97-4d06-8bb0-153db6284593
keywords:
- task offload porting WDK networking , protocol drivers
- TCP/IP offload service porting WDK networking , protocol drivers
- offload service porting WDK networking , protocol drivers
- porting task offload services WDK networking , protocol drivers
- protoc
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Summary of NDIS 6.0 Task Offload Porting Issues for Protocol Drivers





The following list summarizes the issues that you must consider when you port offload-capable protocol drivers to NDIS 6.0:

-   All of the general NDIS 6.0 porting issues apply to porting task offload drivers. For general issues about porting protocol drivers to NDIS 6.0, see [Porting Protocol Drivers to NDIS 6.0](porting-a-protocol-driver-to-ndis-6-0.md).

-   NDIS provides the default offload configuration of the underlying miniport adapter in the **DefaultOffloadConfiguration** member of the [**NDIS\_BIND\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff564832) structure. Protocol drivers should avoid using object identifier (OID) queries and should use the information in **NDIS\_BIND\_PARAMETERS** instead.

-   Protocol drivers can support the following NDIS 6.0 offload OIDs:

    <a href="" id="---------oid-tcp-offload-current-config"></a>[OID\_TCP\_OFFLOAD\_CURRENT\_CONFIG](https://msdn.microsoft.com/library/windows/hardware/ff569805)  
    As a query request, use the [OID\_TCP\_OFFLOAD\_CURRENT\_CONFIG](https://msdn.microsoft.com/library/windows/hardware/ff569805) OID to determine the task offload capabilities of an underlying miniport adapter.

    <a href="" id="---------oid-tcp-offload-hardware-capabilities"></a>[OID\_TCP\_OFFLOAD\_HARDWARE\_CAPABILITIES](https://msdn.microsoft.com/library/windows/hardware/ff569806)  
    As a query request, use the [OID\_TCP\_OFFLOAD\_HARDWARE\_CAPABILITIES](https://msdn.microsoft.com/library/windows/hardware/ff569806) OID to report what capabilities a miniport adapter's hardware can support. Protocol drivers or user-mode applications can query this OID to obtain the task offload hardware capabilities. A system administrator can use this OID through the Windows Management Instrumentation (WMI) interface.

    <a href="" id="oid-tcp-offload-parameters"></a>[OID\_TCP\_OFFLOAD\_PARAMETERS](https://msdn.microsoft.com/library/windows/hardware/ff569807)  
    As a set request, use the [OID\_TCP\_OFFLOAD\_PARAMETERS](https://msdn.microsoft.com/library/windows/hardware/ff569807) OID to set the current offload capabilities of a miniport adapter. Protocol drivers or user-mode applications can set this OID to change the current task offload capabilities. A system administrator can use this OID through the WMI interface.

    <a href="" id="oid-offload-encapsulation"></a>[OID\_OFFLOAD\_ENCAPSULATION](https://msdn.microsoft.com/library/windows/hardware/ff569762)  
    As a set request, use the [OID\_OFFLOAD\_ENCAPSULATION](https://msdn.microsoft.com/library/windows/hardware/ff569762) OID to set the task offload encapsulation settings of an underlying miniport adapter.

    As a query request, use the [OID\_OFFLOAD\_ENCAPSULATION](https://msdn.microsoft.com/library/windows/hardware/ff569762) OID to obtain the current task offload encapsulation settings of an underlying miniport adapter.

    <a href="" id="---------oid-tcp-connection-offload-current-config"></a>[OID\_TCP\_CONNECTION\_OFFLOAD\_CURRENT\_CONFIG](https://msdn.microsoft.com/library/windows/hardware/ff569802)  
    As a query request, use the [OID\_TCP\_CONNECTION\_OFFLOAD\_CURRENT\_CONFIG](https://msdn.microsoft.com/library/windows/hardware/ff569802) OID to determine the current connection offload capabilities of an underlying miniport adapter.

    <a href="" id="---------oid-tcp-connection-offload-hardware-capabilities"></a>[OID\_TCP\_CONNECTION\_OFFLOAD\_HARDWARE\_CAPABILITIES](https://msdn.microsoft.com/library/windows/hardware/ff569803)  
    As a query request, use the [OID\_TCP\_CONNECTION\_OFFLOAD\_HARDWARE\_CAPABILITIES](https://msdn.microsoft.com/library/windows/hardware/ff569803) OID to determine the current connection offload hardware capabilities of an underlying miniport adapter.

    <a href="" id="---------oid-tcp-connection-offload-parameters"></a>[OID\_TCP\_CONNECTION\_OFFLOAD\_PARAMETERS](https://msdn.microsoft.com/library/windows/hardware/ff569804)  
    As a set request, use the [OID\_TCP\_CONNECTION\_OFFLOAD\_PARAMETERS](https://msdn.microsoft.com/library/windows/hardware/ff569804) OID to set the connection offload configuration parameters of an underlying miniport adapter.

    As a query request, use the [OID\_TCP\_CONNECTION\_OFFLOAD\_PARAMETERS](https://msdn.microsoft.com/library/windows/hardware/ff569804) OID to determine the current connection offload settings of an underlying miniport adapter.

-   All task offload capabilities that a miniport adapter supports are enabled by default. The available services are first activated when the protocol driver sets the [OID\_OFFLOAD\_ENCAPSULATION](https://msdn.microsoft.com/library/windows/hardware/ff569762) OID. Connection offload services are separate from the task offload services; their operations are enabled by a set request of [OID\_TCP\_CONNECTION\_OFFLOAD\_HARDWARE\_CAPABILITIES](https://msdn.microsoft.com/library/windows/hardware/ff569803).

-   Protocol drivers must handle changes in the task offload capabilities that underlying drivers report. Miniport drivers can report changes in task offload capabilities in the [**NDIS\_STATUS\_TASK\_OFFLOAD\_CURRENT\_CONFIG**](https://msdn.microsoft.com/library/windows/hardware/ff567424) status indication. For example, consider a load balance failover (LBFO) driver that is configured over two network interface cards (NICs). If an offload-capable NIC fails and send requests must go to a non-offload-capable NIC, the task offload capabilities in the driver stack must be updated.

-   Protocol drivers must support large send offload version 1 (LSOV1) and large send offload version 2 (LSOV2) out-of-band (OOB) information. The information is stored in the [**NDIS\_TCP\_LARGE\_SEND\_OFFLOAD\_NET\_BUFFER\_LIST\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff567882) structure that is part of the OOB information that is included in a [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structure.

 

 





