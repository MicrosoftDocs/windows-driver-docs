---
title: Forwarding OID Requests from a Hyper-V Child Partition
description: Forwarding OID Requests from a Hyper-V Child Partition
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Forwarding OID Requests from a Hyper-V Child Partition


Multicast object identifier (OID) requests, including [OID\_802\_3\_ADD\_MULTICAST\_ADDRESS](./oid-802-3-add-multicast-address.md) and [OID\_802\_3\_DELETE\_MULTICAST\_ADDRESS](./oid-802-3-delete-multicast-address.md), are issued by overlying protocol and filter drivers that run in the following:

-   The management operating system that runs in the Hyper-V parent partition.

-   The guest operating system that runs Windows Vista or a later version of the Windows operating system in the Hyper-V child partition.

The extensible switch interface forwards these OID requests down the extensible switch control path. This allows the extensions to obtain configuration information about the network interface that is used in the partition.

For example, the protocol edge of the extensible switch forwards an OID set request of [OID\_802\_3\_ADD\_MULTICAST\_ADDRESS](./oid-802-3-add-multicast-address.md) from a child partition down the extensible switch control path. This allows extensions to obtain the multicast address configuration that is used by the networking interface in that partition.

When these multicast OID requests arrive at the extensible switch interface, the protocol edge of the extensible switch encapsulates the OID request within an [**NDIS\_SWITCH\_NIC\_OID\_REQUEST**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_switch_nic_oid_request) structure. The protocol edge also sets the members of this structure in the following way:

-   The **SourcePortId** and **SourceNicIndex** members are set to the corresponding values for the port and network adapter used by the partition from which the OID request originated.

    **Note**  If the multicast OID request was originated from the management operating system, the protocol edge sets these members to the values for the extensible switch internal network adapter.

     

-   The **DestinationPortId** and **DestinationNicIndex** members are set to zero. This specifies that the encapsulated OID request is to be delivered to extensions in the control path.

-   The **OidRequest** member is set to the address of an [**NDIS\_OID\_REQUEST**](/windows-hardware/drivers/ddi/oidrequest/ns-oidrequest-ndis_oid_request) structure for the encapsulated OID request.

The protocol edge then issues the [OID\_SWITCH\_NIC\_REQUEST](./oid-switch-nic-request.md) request to forward the encapsulated OID request down the extensible switch control path. Underlying forwarding extensions can inspect these encapsulated OID requests and retain the multicast address information that they specify. For example, the extension may need this information if it originates multicast packets that it forwards to an extensible switch port.

For more information about the extensible switch control path, see [Hyper-V Extensible Switch Control Path](hyper-v-extensible-switch-control-path.md).

 

