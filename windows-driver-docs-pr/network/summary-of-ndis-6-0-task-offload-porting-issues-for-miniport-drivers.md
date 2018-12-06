---
title: Summary of NDIS 6.0 miniport driver task offload porting issues
description: Summary of NDIS 6.0 Task Offload Porting Issues for Miniport Drivers
ms.assetid: 1f07829b-f66c-4709-ba94-77ef03821ff4
keywords:
- task offload porting WDK networking , miniport drivers
- TCP/IP offload service porting WDK networking , miniport drivers
- offload service porting WDK networking , miniport drivers
- porting task offload services WDK networking , miniport drivers
- portin
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Summary of NDIS 6.0 Task Offload Porting Issues for Miniport Drivers





The following list summarizes the issues that you must consider when you port offload-capable miniport drivers to NDIS 6.0:

-   All of the general NDIS 6.0 porting issues apply to porting task offload drivers. For general issues about porting miniport drivers to NDIS 6.0, see [Porting Miniport Drivers to NDIS 6.0](porting-a-miniport-driver-to-ndis-6-0.md).

-   Miniport drivers must provide the offload capabilities of a miniport adapter in the [**NDIS\_MINIPORT\_ADAPTER\_OFFLOAD\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff565930) structure. Miniport drivers call the [**NdisMSetMiniportAttributes**](https://msdn.microsoft.com/library/windows/hardware/ff563672) function from the [*MiniportInitializeEx*](https://msdn.microsoft.com/library/windows/hardware/ff559389) function and pass the information in NDIS\_MINIPORT\_ADAPTER\_OFFLOAD\_ATTRIBUTES.

-   Miniport drivers must support the following NDIS 6.0 offload object identifiers (OIDs):

    <a href="" id="oid-offload-encapsulation"></a>[OID\_OFFLOAD\_ENCAPSULATION](https://msdn.microsoft.com/library/windows/hardware/ff569762)  
    As a set request, use the OID\_OFFLOAD\_ENCAPSULATION OID to set the task offload encapsulation settings of a miniport adapter.

    <a href="" id="---------oid-tcp-connection-offload-hardware-capabilities"></a>[OID\_TCP\_CONNECTION\_OFFLOAD\_HARDWARE\_CAPABILITIES](https://msdn.microsoft.com/library/windows/hardware/ff569803)  
    As a set request, use the OID\_TCP\_CONNECTION\_OFFLOAD\_HARDWARE\_CAPABILITIES OID to enable or disable the connection offload services of a miniport adapter.

    <a href="" id="oid-tcp-offload-parameters"></a>[OID\_TCP\_OFFLOAD\_PARAMETERS](https://msdn.microsoft.com/library/windows/hardware/ff569807)  
    As a set request, use the OID\_TCP\_OFFLOAD\_PARAMETERS OID to set the current offload capabilities of a miniport adapter. Protocol drivers or user-mode applications can set this OID to change the current task offload capabilities. A system administrator can use this OID through the Windows Management Instrumentation (WMI) interface.

-   All of the task offload capabilities that a miniport adapter supports are enabled by default. Miniport drivers must support Ethernet encapsulation for all task offload types that they support. These drivers can also support virtual LAN (VLAN) encapsulation and logical link control (LLC) SNAP encapsulation. The available services are first activated when an overlying protocol driver sets the [OID\_OFFLOAD\_ENCAPSULATION](https://msdn.microsoft.com/library/windows/hardware/ff569762) OID. Connection offload services are separate from task offload; their operations are enabled by a set request of [OID\_TCP\_CONNECTION\_OFFLOAD\_HARDWARE\_CAPABILITIES](https://msdn.microsoft.com/library/windows/hardware/ff569803).

-   Miniport drivers must report changes in the task offload capabilities, if any, in the [**NDIS\_STATUS\_TASK\_OFFLOAD\_CURRENT\_CONFIG**](https://msdn.microsoft.com/library/windows/hardware/ff567424) status indication. For example, consider a load balance failover (LBFO) driver that is installed over two network interface cards (NICs). If an offload-capable NIC fails and send requests must go to a non-offload-capable NIC, the task offload capabilities in the driver stack must be updated.

-   Miniport drivers must handle large send offload version 1 (LSOV1) and large send offload version 2 (LSOV2) out-of-band (OOB) information. The information is stored in the [**NDIS\_TCP\_LARGE\_SEND\_OFFLOAD\_NET\_BUFFER\_LIST\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff567882) structure that is part of the OOB information that is included in a [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structure.

 

 





