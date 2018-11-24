---
title: Hyper-V Extensible Switch OID Requests
description: Hyper-V Extensible Switch OID Requests
ms.assetid: 0B6D1628-DD83-4EA6-B5D5-33D74AD45EFD
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Hyper-V Extensible Switch OID Requests


The Hyper-V extensible switch interface includes object identifier (OID) requests that are used in the following ways:

-   OID requests that are issued by an extensible switch extension to query the current configuration of the extensible switch. For example, the filter driver (also known as a *Hyper-V extensible switch extension*) can issue an OID query request of [OID\_SWITCH\_NIC\_ARRAY](https://msdn.microsoft.com/library/windows/hardware/hh598261) to obtain an array. Each element in the array specifies the configuration parameters of a network adapter that is associated with an extensible switch port.

    For more information, see [Querying the Hyper-V Extensible Switch Configuration](querying-the-hyper-v-extensible-switch-configuration.md).

-   OID requests that are issued by the extensible switch interface to notify underlying extensions about changes to the extensible switch configuration. For example, the protocol edge of the extensible switch issues an OID set request of [OID\_SWITCH\_PORT\_CREATE](https://msdn.microsoft.com/library/windows/hardware/hh598272) to notify extensions about the creation of an extensible switch port.

    For more information, see [Receiving OID Requests about Hyper-V Extensible Switch Configuration Changes](receiving-oid-requests-about-hyper-v-extensible-switch-configuration-changes.md).

-   OID requests from a Hyper-V child partition that are forwarded by the extensible switch interface to extensions over the extensible switch control path. This allows the extensions to obtain configuration information about the network interface that is used in the partition.

    For example, the protocol edge of the extensible switch in the extensibility interface forwards an OID set request of [OID\_802\_3\_ADD\_MULTICAST\_ADDRESS](https://msdn.microsoft.com/library/windows/hardware/ff569068) from a child partition down the extensible switch control path. This allows extensions to obtain the multicast address configuration that is used by the networking interface in that partition.

    For more information, see [Forwarding OID Requests from a Hyper-V Child Partition](forwarding-oid-requests-from-a-hyper-v-child-partition.md).

For more information on how extensions and NDIS filter drivers handle OID requests, see [Filter Module OID Requests](filter-module-oid-requests.md).

 

 





