---
title: Overview of Hyper-V Extensible Switch Ports
description: Overview of Hyper-V Extensible Switch Ports
ms.assetid: FD6B6014-B840-4EC8-96F4-34C08EC303EA
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Overview of Hyper-V Extensible Switch Ports


Each network connection to the Hyper-V extensible switch is represented by a port. The extensible switch interface creates and configures a port before a network connection is made. After the network connection is torn down, the interface may delete the port or reuse it for another network connection.

Every Hyper-V child partition that is configured with a network interface is assigned a port on the extensible switch. When a Hyper-V child partition is started, the extensible switch interface creates a port before the virtual machine (VM) network adapter is exposed within the guest operating system. After the VM network adapter is exposed and initialized, the extensible switch interface creates a network connection between the VM network adapter and the extensible switch port. If the child partition is stopped, the extensible switch interface first deletes the network connection and then deletes the extensible switch port.

When an extensible switch port is created, it is configured with a unique identifier and name. After it is created, the extensible switch port can be provisioned with policies that define various attributes for the management of packet traffic over the port. For example, standard port policies can be defined for virtual LAN (VLAN) attributes and access restrictions for port traffic. In addition, independent software vendors (ISVs) can define custom policies that individual ports can be provisioned with. For more information, see [Port Policies](port-policies.md).

Extensible switch ports consist of the following types:

<a href="" id="validation-ports"></a>Validation ports  
Validation ports are used to validate and verify port settings. These ports are temporary and are created under certain conditions.

For example, when a Hyper-V child partition is created or reconfigured for network access, the extensible switch interface creates a validation port. The interface uses this port to verify the settings for the network connection to the virtual machine (VM) network adapter of the partition. After the verification is completed, the validation port is deleted and an operational port is created.

For more information, see [Validation Ports](validation-ports.md).

<a href="" id="operational-ports"></a>Operational ports  
Operational ports are created to host an extensible switch network adapter connection. When an operational port is created, it is assigned a port type. This port type is in effect after the port is created and before it is torn down. For ports assigned to Hyper-V child partitions, the operational port type stays in effect while the partition is running and operational.

For more information, see [Operational Ports](operational-ports.md).

Extensible switch extensions are notified of port creation, update and deletion through the following extensible switch object identifier (OID) requests:

<a href="" id="oid-switch-port-create"></a>[OID\_SWITCH\_PORT\_CREATE](https://msdn.microsoft.com/library/windows/hardware/hh598272)  
The protocol edge of the extensible switch issues an OID set request of [OID\_SWITCH\_PORT\_CREATE](https://msdn.microsoft.com/library/windows/hardware/hh598272) to notify extensible switch extensions about the creation of an extensible switch port.

The extension can veto the creation notification by returning STATUS\_DATA\_NOT\_ACCEPTED for the OID request. For example, if an extension cannot allocate resources to enforce its configured policies on the port, the extension vetoes the creation notification.

If the extension accepts the creation notification, it must forward the OID request down the extensible switch driver stack. The extension monitors the completion status of this OID request to determine whether underlying extensions have vetoed the port creation notification.

Extensions cannot forward packets to the newly created port until a network connection is created. For more information on this process, see [Hyper-V Extensible Switch Network Adapters](hyper-v-extensible-switch-network-adapters.md).

<a href="" id="oid-switch-port-updated"></a>[OID\_SWITCH\_PORT\_UPDATED](https://msdn.microsoft.com/library/windows/hardware/hh846217)  
The protocol edge of the extensible switch issues an OID set request of [OID\_SWITCH\_PORT\_UPDATED](https://msdn.microsoft.com/library/windows/hardware/hh846217) to notify extensible switch extensions that an extensible switch port’s parameters are being updated. The OID will only be issued for ports that have already been created, and have not yet begun the teardown/delete process. Currently only the *PortFriendlyName* field is subject to update after creation.

The protocol edge of the extensible switch issues this OID request when the previous network connection to the port has been torn down and all OID requests to the port have been completed.

**Note**  This OID request could be issued if a network adapter connection was not previously made to the port.

 

The extension must always forward this OID set request down the extensible switch driver stack. The extension must not fail the request.

<a href="" id="oid-switch-port-teardown"></a>[OID\_SWITCH\_PORT\_TEARDOWN](https://msdn.microsoft.com/library/windows/hardware/hh598279)  
The protocol edge of the extensible switch issues an OID set request of [OID\_SWITCH\_PORT\_TEARDOWN](https://msdn.microsoft.com/library/windows/hardware/hh598279) to notify extensible switch extensions that an extensible switch port is being deleted. The protocol edge of the extensible switch issues this OID request when the previous network connection to the port has been torn down and all OID requests to the port have been completed.

**Note**  This OID request could be issued if a network adapter connection was not previously made to the port.

 

The extension must always forward this OID set request down the extensible switch driver stack. The extension must not fail the request.

After the extension forwards this OID request, it can no longer issue OID requests for the port being deleted.

<a href="" id="oid-switch-port-delete"></a>[OID\_SWITCH\_PORT\_DELETE](https://msdn.microsoft.com/library/windows/hardware/hh598273)  
The protocol edge of the extensible switch issues an OID set request of [OID\_SWITCH\_PORT\_DELETE](https://msdn.microsoft.com/library/windows/hardware/hh598273) to notify extensible switch extensions that an extensible switch port has been deleted. The protocol edge of the extensible switch issues this OID request after it issues the [OID\_SWITCH\_PORT\_TEARDOWN](https://msdn.microsoft.com/library/windows/hardware/hh598279) request and OID requests that target the port have been completed.

The extension must always forward this OID set request down the extensible switch driver stack. The extension must not fail the request.

All extensible switch ports that are created for network connections are assigned an identifier greater than **NDIS\_SWITCH\_DEFAULT\_PORT\_ID**. The **NDIS\_SWITCH\_DEFAULT\_PORT\_ID** identifier is reserved and used in the following ways:

-   The source port identifier for a packet is stored in the packet's out-of-band (OOB) forwarding context that is associated with its [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structure. A source port identifier of **NDIS\_SWITCH\_DEFAULT\_PORT\_ID** specifies that the packet originated from the extensible switch extension and not from an extensible switch port. A packet with a source port identifier of **NDIS\_SWITCH\_DEFAULT\_PORT\_ID** is trusted and bypasses the extensible switch port policies, such as access control lists (ACLs) and quality of service (QoS).

    The extension may want the packet to be treated as if it originated from a particular port. This allows the policies for that port to be applied to the packet. The extension calls [*SetNetBufferListSource*](https://msdn.microsoft.com/library/windows/hardware/hh598300) to change the source port for the packet.

    However, there may be situations where the extension may want to assign the packet's source port identifier to **NDIS\_SWITCH\_DEFAULT\_PORT\_ID**. For example, the extension may want to set the source port identifier to **NDIS\_SWITCH\_DEFAULT\_PORT\_ID** for proprietary control packets that are sent to a device on the external network.

    For more information about the forwarding context, see [Hyper-V Extensible Switch Forwarding Context](hyper-v-extensible-switch-forwarding-context.md).

-   Object identifier (OID) requests of [OID\_SWITCH\_NIC\_REQUEST](https://msdn.microsoft.com/library/windows/hardware/hh598266) are issued by the extensible switch interface to encapsulate OID requests that are issued to the extensible switch external network adapter. For example, hardware offload OID requests are encapsulated by the interface before they are issued down the extensible switch driver stack.

    An extension can also issue encapsulated OID requests in order to forward requests down the extensible switch control path. This allows extensions to query or configure the capabilities of an underlying physical network adapter.

    The **InformationBuffer** member of the **NDIS\_OID\_REQUEST** structure for this OID request contains a pointer to an [**NDIS\_SWITCH\_NIC\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/hh598214) structure. If the **SourcePortId** member is set to **NDIS\_SWITCH\_DEFAULT\_PORT\_ID**, this specifies that the OID request was originated by the extensible switch interface. If the **DestinationPortId** is set to **NDIS\_SWITCH\_DEFAULT\_PORT\_ID**, this specifies that the OID request is targeted for processing by an extension in the extensible switch driver stack.

    For more information about the control path for OID requests, see [Hyper-V Extensible Switch Control Path for OID Requests](hyper-v-extensible-switch-control-path-for-oid-requests.md).

-   NDIS status indications of [**NDIS\_STATUS\_SWITCH\_NIC\_STATUS**](https://msdn.microsoft.com/library/windows/hardware/hh598205) are issued by the miniport edge of the extensible switch to encapsulate a status indication from the extensible switch external network adapter.

    An extension can also issue encapsulated NDIS status indications in order to forward indications up the extensible switch control path. This allows extensions to change the reported capabilities of an underlying physical network adapter.

    The **StatusBuffer** member of the [**NDIS\_STATUS\_INDICATION**](https://msdn.microsoft.com/library/windows/hardware/ff567373) structure for this indication contains a pointer to an [**NDIS\_SWITCH\_NIC\_STATUS\_INDICATION**](https://msdn.microsoft.com/library/windows/hardware/hh598217) structure. If the **SourcePortId** member is set to **NDIS\_SWITCH\_DEFAULT\_PORT\_ID**, this specifies that the status indication was originated by the extensible switch interface. If the **DestinationPortId** is set to **NDIS\_SWITCH\_DEFAULT\_PORT\_ID**, this specifies that the OID request is targeted for processing by an extension in the extensible switch driver stack.

    For more information about the control path for NDIS status indications, see [Hyper-V Extensible Switch Control Path for NDIS Status Indications](hyper-v-extensible-switch-control-path-for-ndis-status-indications.md).

The extensible switch interface maintains a reference counter for each port that has been created. A port will not be deleted if its reference counter has a nonzero value. The interface provides the following handler functions for incrementing or decrementing an extensible switch port's reference counters:

<a href="" id="referenceswitchport"></a>[*ReferenceSwitchPort*](https://msdn.microsoft.com/library/windows/hardware/hh598295)  
The extensible switch extension calls this function to increment a port's reference counter. While the reference counter has a nonzero value, the protocol edge of the extensible switch will not issue an object identifier (OID) set request of [OID\_SWITCH\_PORT\_DELETE](https://msdn.microsoft.com/library/windows/hardware/hh598273) to delete the extensible switch port.

The extension must call [*ReferenceSwitchPort*](https://msdn.microsoft.com/library/windows/hardware/hh598295) before it performs any operation that requires the port to be in an active state. For example, the extension must call *ReferenceSwitchPort* before it issues an OID method request of [OID\_SWITCH\_PORT\_PROPERTY\_ENUM](https://msdn.microsoft.com/library/windows/hardware/hh598277).

**Note**  The extension must not call [*ReferenceSwitchPort*](https://msdn.microsoft.com/library/windows/hardware/hh598295) for a port after it receives an OID set request of [OID\_SWITCH\_PORT\_TEARDOWN](https://msdn.microsoft.com/library/windows/hardware/hh598279) for that port.

 

<a href="" id="dereferenceswitchport"></a>[*DereferenceSwitchPort*](https://msdn.microsoft.com/library/windows/hardware/hh598295)  
The extensible switch extension calls this function to decrement a port's reference counter.

The extension must call [*DereferenceSwitchPort*](https://msdn.microsoft.com/library/windows/hardware/hh598295) after the operation being performed on the port has completed. For example, if the extension called *ReferenceSwitchPort* before if issued an [OID\_SWITCH\_PORT\_PROPERTY\_ENUM](https://msdn.microsoft.com/library/windows/hardware/hh598277) request, the extension must call *DereferenceSwitchPort* after the OID request has completed.

**Note**  NDIS ports and extensible switch ports are different objects. Packets that move through the extensible switch data path are always assigned to the NDIS port number of **NDIS\_DEFAULT\_PORT\_NUMBER**. However, the packet's source and destination extensible switch port number can be a value of **NDIS\_SWITCH\_DEFAULT\_PORT\_ID** or greater. For more information, see [Hyper-V Extensible Switch Data Path](hyper-v-extensible-switch-data-path.md).

 

 

 





