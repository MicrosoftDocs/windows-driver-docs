---
title: Overview of Hyper-V Extensible Switch Network Adapters
description: Overview of Hyper-V Extensible Switch Network Adapters
ms.assetid: 61403FDE-90BF-4D0A-83E1-5AF8ADBD37A5
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Overview of Hyper-V Extensible Switch Network Adapters


The Hyper-V extensible switch supports connections from various types of virtual or physical network adapters. The connection to these types of network adapters is made through an extensible switch port. Ports are created before a virtual network adapter connection is made, and are deleted after the network adapter connection is torn down.

For example, when a Hyper-V child partition is started, the extensible switch interface creates a port before the virtual machine (VM) network adapter is exposed within the guest operating system. After the VM network adapter is exposed and enumerated, the extensible switch interface creates a network connection between the VM network adapter and the extensible switch port. If the child partition is stopped, the extensible switch interface first deletes the network connection and then deletes the extensible switch port.

The Hyper-V extensible switch supports connections from the following types of virtual network adapters:

<a href="" id="external-network-adapters"></a>External network adapters  
This is an extensible switch network adapter that is exposed in the management operating system that runs in the Hyper-V parent partition. Each extensible switch supports only one external network adapter connection.

The external network adapter provides a connection to the physical network interface that is available on the host. The external network adapter can be accessed by the Hyper-V parent partition and all child partitions.

For more information about this type of network adapter, see [External Network Adapters](external-network-adapters.md).

<a href="" id="internal-network-adapters"></a>Internal network adapters  
This is an extensible switch network adapter that is exposed in the management operating system that runs in the Hyper-V parent partition. Each extensible switch supports only one internal network adapter connection.

The internal network adapter provides access to an extensible switch for processes that run in the management operating system. This allows these processes to send or receive packets over the extensible switch.

For more information about this type of network adapter, see [Internal Network Adapters](internal-network-adapters.md).

<a href="" id="virtual-machine--vm--network-adapters"></a>Virtual machine (VM) network adapters  
This is an extensible switch network adapter that is exposed in the guest operating system that runs in the Hyper-V child partition.

**Note**  In Hyper-V, a child partition is also known as a VM.

 

The VM network adapter supports the following virtualization types:

-   The VM network adapter could be a synthetic virtualization of a network adapter (*synthetic network adapter*). In this case, the network virtual service client (NetVSC) that runs in the VM exposes this virtual network adapter. NetVSC forwards packets to and from the extensible switch port over the VM bus (VMBus).

-   The VM network adapter could be an emulated virtualization of a physical network adapter (*emulated network adapter*). In this case, the VM network adapter mimics an Intel network adapter and uses hardware emulation to forward packets to and from the extensible switch port.

For more information about this type of network adapter, see [Virtual Machine Network Adapters](virtual-machine-network-adapters.md).

Extensible switch network adapter connections are created, updated, and deleted through the following extensible switch OID requests:

<a href="" id="oid-switch-nic-create"></a>[OID\_SWITCH\_NIC\_CREATE](https://msdn.microsoft.com/library/windows/hardware/hh598263)  
The protocol edge of the extensible switch issues an OID set request of [OID\_SWITCH\_NIC\_CREATE](https://msdn.microsoft.com/library/windows/hardware/hh598263) to notify extensible switch extensions about the creation of a network adapter connection to an extensible switch port. The port must have been previously created through an OID set request of [OID\_SWITCH\_PORT\_CREATE](https://msdn.microsoft.com/library/windows/hardware/hh598272).

The [OID\_SWITCH\_NIC\_CREATE](https://msdn.microsoft.com/library/windows/hardware/hh598263) request only notifies the extension that a new extensible switch network adapter connection is being brought up and that packet traffic may soon begin to occur over the specified port.

The extension can veto the creation notification by returning STATUS\_DATA\_NOT\_ACCEPTED for the OID request. For example, if an extension cannot satisfy its configured policies on the port that is used for the network adapter connection, the extension should veto the creation notification.

If the extension accepts the creation notification, it must forward the OID request down the extensible switch driver stack. The extension monitors the completion status of this OID request to determine whether underlying extensions have vetoed the creation notification.

When the network adapter connection is created, it is assigned an NDIS\_SWITCH\_NIC\_INDEX value. This index value identifies the network adapter connection on an extensible switch port. Connections to the external, internal, and VM network adapters are assigned an NDIS\_SWITCH\_NIC\_INDEX value of **NDIS\_SWITCH\_DEFAULT\_NIC\_INDEX**. Each physical or virtual network adapter that is bound to the external network adapter is assigned an NDIS\_SWITCH\_NIC\_INDEX value in the following way:

-   If the physical or virtual network adapter is directly bound to the external network adapter, it is assigned an NDIS\_SWITCH\_NIC\_INDEX value of one.

-   If the physical network adapter is part of an extensible switch team, it is assigned an NDIS\_SWITCH\_NIC\_INDEX value that is greater than or equal to one. An extensible switch team is a configuration in which a team of one or more physical network adapters are bound to the extensible switch external network adapter.

For more information about the different configurations in which physical network adapters can be bound to the external network adapter, see [Types of Physical Network Adapter Configurations](types-of-physical-network-adapter-configurations.md).

For more information on NDIS\_SWITCH\_NIC\_INDEX values, see [Network Adapter Index Values](network-adapter-index-values.md).

**Note**  The extension cannot generate or forward packets over the network adapter connection until the protocol edge of the extensible switch issues an OID set request of [OID\_SWITCH\_NIC\_CONNECT](https://msdn.microsoft.com/library/windows/hardware/hh598262).

 

<a href="" id="oid-switch-nic-connect"></a>[OID\_SWITCH\_NIC\_CONNECT](https://msdn.microsoft.com/library/windows/hardware/hh598262)  
The protocol edge of the extensible switch issues an OID set request of [OID\_SWITCH\_NIC\_CONNECT](https://msdn.microsoft.com/library/windows/hardware/hh598262) to notify extensible switch extensions that an extensible switch network adapter connection is fully operational.

The extension must always forward this OID set request down the extensible switch driver stack. The extension must not fail the request.

After the OID request has completed with NDIS\_STATUS\_SUCCESS, the network adapter connection and extensible switch port are fully operational. When the network adapter connection is in this state, the extension can do the following:

-   Generate or forward packet traffic to the port's network adapter connection.

-   Issue extensible switch OIDs or status indications that use the port as the source port.

-   Call [*ReferenceSwitchNic*](https://msdn.microsoft.com/library/windows/hardware/hh598294) to increment a reference counter for the network adapter connection. The extensible switch interface will not tear down a network adapter connection while the reference counter has a nonzero value.

<a href="" id="oid-switch-nic-updated"></a>[OID\_SWITCH\_NIC\_UPDATED](https://msdn.microsoft.com/library/windows/hardware/hh846216)  
The protocol edge of the extensible switch issues an OID set request of OID\_SWITCH\_NIC\_UPDATED to notify extensible switch extensions that the parameters for an extensible switch network adapter have been updated. The OID will only be issued for NICs that have already been connected, and have not yet begun the disconnect process. These run-time configuration changes can include *NicFriendlyName*, *MTU*, *NetCfgInstanceId*, *PermanentMacAddress*, *VMMacAddress*, *CurrentMacAddress*, and *VFAssigned.*

The extension must always forward this OID set request down the extensible switch driver stack. The extension must not fail the request.

<a href="" id="oid-switch-nic-disconnect"></a>[OID\_SWITCH\_NIC\_DISCONNECT](https://msdn.microsoft.com/library/windows/hardware/hh598265)  
The protocol edge of the extensible switch issues an OID set request of [OID\_SWITCH\_NIC\_DISCONNECT](https://msdn.microsoft.com/library/windows/hardware/hh598265) to notify extensible switch extensions that an extensible switch network adapter connection is being torn down. After the connection has been completely torn down, the protocol edge of the extensible switch issues an OID set request of [OID\_SWITCH\_NIC\_DELETE](https://msdn.microsoft.com/library/windows/hardware/hh598264).

The extension must always forward this OID set request down the extensible switch driver stack. The extension must not fail the request.

After the extension forwards this OID request, it can no longer generate or forward packets to the port on which the network adapter connection is being torn down. Also, the extension can no longer call [*ReferenceSwitchNic*](https://msdn.microsoft.com/library/windows/hardware/hh598294) for the network adapter connection.

<a href="" id="oid-switch-nic-delete"></a>[OID\_SWITCH\_NIC\_DELETE](https://msdn.microsoft.com/library/windows/hardware/hh598264)  
The protocol edge of the extensible switch issues an OID set request of [OID\_SWITCH\_NIC\_DELETE](https://msdn.microsoft.com/library/windows/hardware/hh598264) to notify extensible switch extensions that an extensible switch network adapter connection has been torn down and deleted. This OID request is only issued for network connections for which an OID set request of [OID\_SWITCH\_NIC\_DISCONNECT](https://msdn.microsoft.com/library/windows/hardware/hh598265) was previously issued.

**Note**  The extension must always forward this OID set request down the extensible switch driver stack. The extension must not fail the request.

 

After this OID request is completed, the protocol edge of the extensible switch issues an OID set request of [OID\_SWITCH\_PORT\_TEARDOWN](https://msdn.microsoft.com/library/windows/hardware/hh598279) to start the deletion process for the port that was used for the network adapter connection.

The extension must always forward this OID set request down the extensible switch driver stack. The extension must not fail the request.

The extensible switch interface maintains a reference counter for each network adapter connection that has been created. A network adapter connection will not be deleted if its reference counter has a nonzero value. The interface provides the following handler functions for incrementing or decrementing the reference counter of an extensible switch network adapter connection:

<a href="" id="referenceswitchnic"></a>[*ReferenceSwitchNic*](https://msdn.microsoft.com/library/windows/hardware/hh598294)  
The extensible switch extension calls this function to increment a network adapter connection's reference counter. Although the reference counter has a nonzero value, the extensible switch interface does not delete the network adapter connection.

The extension should call [*ReferenceSwitchNic*](https://msdn.microsoft.com/library/windows/hardware/hh598294) before it performs the following operations:

-   Forwards an [OID\_SWITCH\_NIC\_REQUEST](https://msdn.microsoft.com/library/windows/hardware/hh598266) request down the extensible switch driver stack to an underlying external adapter.

-   Forwards an [**NDIS\_STATUS\_SWITCH\_NIC\_STATUS**](https://msdn.microsoft.com/library/windows/hardware/hh598205) status indication up the extensible switch driver stack from an underlying external adapter.

**Note**  The extension must not call [*ReferenceSwitchNic*](https://msdn.microsoft.com/library/windows/hardware/hh598294) for a network adapter connection after it receives an OID set request of [OID\_SWITCH\_NIC\_DISCONNECT](https://msdn.microsoft.com/library/windows/hardware/hh598265) for that connection.

 

<a href="" id="dereferenceswitchnic"></a>[*DereferenceSwitchNic*](https://msdn.microsoft.com/library/windows/hardware/hh598141)  
The extensible switch extension calls this function to decrement a port's reference counter.

If the extension calls [*ReferenceSwitchNic*](https://msdn.microsoft.com/library/windows/hardware/hh598294), it must call [*DereferenceSwitchNic*](https://msdn.microsoft.com/library/windows/hardware/hh598141) after the [OID\_SWITCH\_NIC\_REQUEST](https://msdn.microsoft.com/library/windows/hardware/hh598266) or [**NDIS\_STATUS\_SWITCH\_NIC\_STATUS**](https://msdn.microsoft.com/library/windows/hardware/hh598205) indication have completed.

 

 





