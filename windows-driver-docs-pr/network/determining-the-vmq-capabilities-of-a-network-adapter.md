---
title: Determining the VMQ Capabilities of a Network Adapter
description: Determining the VMQ Capabilities of a Network Adapter
ms.assetid: a8efc393-60fd-4ff8-ba9a-53846f5fbba4
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Determining the VMQ Capabilities of a Network Adapter





NDIS provides the interface to determine the VMQ capabilities of a network adapter, such as:

-   The generic filtering capabilities of a network adapter.

-   Supported VM queue capabilities.

-   Lookahead support to allow splitting of the networking data memory into two separate buffers.

    **Note**  Starting with NDIS 6.30, splitting packet data into separate lookahead buffers is no longer supported.

     

Miniport drivers provide the following information to NDIS during network adapter initialization:

-   The VMQ hardware capabilities that the network adapter can support.

-   The VMQ capabilities that are currently enabled.

-   The global receive filtering features that are enabled or disabled on a network adapter.

Overlying drivers and applications can use the following OID query requests to obtain the network adapter capabilities.

[OID\_RECEIVE\_FILTER\_HARDWARE\_CAPABILITIES](https://msdn.microsoft.com/library/windows/hardware/ff569791)

[OID\_RECEIVE\_FILTER\_CURRENT\_CAPABILITIES](https://msdn.microsoft.com/library/windows/hardware/ff569786)

[OID\_RECEIVE\_FILTER\_GLOBAL\_PARAMETERS](https://msdn.microsoft.com/library/windows/hardware/ff569790)

NDIS handles these OID query requests for miniport drivers. Therefore, the query is not requested for miniport drivers. NDIS reports the currently enabled receive VMQ capabilities of a network adapter during initialization. Therefore, overlying drivers do not have to query these OIDs.

The [**NDIS\_RECEIVE\_FILTER\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff566864) structure specifies the filtering capabilities of a network adapter. This structure is used in the following ways:

-   When NDIS calls the [*MiniportInitializeEx*](https://msdn.microsoft.com/library/windows/hardware/ff559389) function, the miniport driver registers its filtering capabilities by initializing an [**NDIS\_RECEIVE\_FILTER\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff566864) structure. The driver then sets the **HardwareReceiveFilterCapabilities** member of the [**NDIS\_MINIPORT\_ADAPTER\_HARDWARE\_ASSIST\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff565924) structure to point to the **NDIS\_RECEIVE\_FILTER\_CAPABILITIES** structure. The driver next calls the [**NdisMSetMiniportAttributes**](https://msdn.microsoft.com/library/windows/hardware/ff563672) function and then sets the *MiniportAttributes* parameter to a pointer to the **NDIS\_MINIPORT\_ADAPTER\_HARDWARE\_ASSIST\_ATTRIBUTES** structure.

-   An overlying protocol driver receives the [**NDIS\_RECEIVE\_FILTER\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff566864) structure in the [**NDIS\_BIND\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff564832) structure when NDIS calls the driver's [*ProtocolBindAdapterEx*](https://msdn.microsoft.com/library/windows/hardware/ff570220) function.

-   An overlying filter driver receives the [**NDIS\_RECEIVE\_FILTER\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff566864) structure in the [**NDIS\_FILTER\_ATTACH\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff565481) structure when NDIS calls the driver's [*FilterAttach*](https://msdn.microsoft.com/library/windows/hardware/ff549905) function.

-   Overlying drivers receive the [**NDIS\_MINIPORT\_ADAPTER\_HARDWARE\_ASSIST\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff565924) structure by issuing an OID query request of [OID\_RECEIVE\_FILTER\_CURRENT\_CAPABILITIES](https://msdn.microsoft.com/library/windows/hardware/ff569786) or [OID\_RECEIVE\_FILTER\_HARDWARE\_CAPABILITIES](https://msdn.microsoft.com/library/windows/hardware/ff569791). The **HardwareReceiveFilterCapabilities** and **CurrentReceiveFilterCapabilities** members point to an [**NDIS\_RECEIVE\_FILTER\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff566864) structure.

The [**NDIS\_RECEIVE\_FILTER\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff566864) structure includes the following information:

<a href="" id="enabledfiltertypes"></a>**EnabledFilterTypes**  
The types of the supported receive filters. The NDIS\_RECEIVE\_FILTER\_VMQ\_FILTERS\_ENABLED flag specifies that virtual machine queue (VMQ) filters are enabled.

<a href="" id="enabledqueuetypes"></a>**EnabledQueueTypes**  
The types of supported receive queues. The NDIS\_RECEIVE\_FILTER\_VM\_QUEUES\_ENABLED flag specifies that virtual machine (VM) queues are enabled.

<a href="" id="numqueues"></a>**NumQueues**  
The number of receive queues that the network adapter supports. To support VMQ, this number must be equal to or less than the number of unicast MAC addresses that the NIC supports. This number must not include the default queue.

**Note**  The number of unicast MAC addresses or VM queues that a network adapter supports does not include the MAC address of the associated NIC.

 

<a href="" id="supportedqueueproperties"></a>**SupportedQueueProperties**  
The queue properties that the network adapter supports. The NDIS\_RECEIVE\_FILTER\_VM\_QUEUE\_SUPPORTED flag specifies that the network adapter provides the minimum requirements to support VMQ filtering. A VMQ-capable NIC must provide an MSI-X table entry for each receive queue. Therefore, a VMQ miniport driver must set the NDIS\_RECEIVE\_FILTER\_MSI\_X\_SUPPORTED flag.

<a href="" id="supportedfiltertests"></a>**SupportedFilterTests**  
The filter test operations that a miniport driver supports. For example, the network adapter supports testing the selected header field to determine whether it is equal to a given value. A VMQ miniport driver must set the NDIS\_RECEIVE\_FILTER\_TEST\_HEADER\_FIELD\_EQUAL\_SUPPORTED flag.

<a href="" id="supportedheaders"></a>**SupportedHeaders**  
The types of network packet headers that a miniport driver can inspect. For example, the network adapter can inspect the MAC header of a network packet. The MAC header includes the packet type, destination and source MAC addresses, the VLAN identifier, and the priority tag fields. A VMQ miniport driver must set the NDIS\_RECEIVE\_FILTER\_MAC\_HEADER\_SUPPORTED flag.

<a href="" id="supportedmacheaderfields"></a>**SupportedMacHeaderFields**  
The types of MAC header fields that a miniport driver can inspect. A VMQ miniport driver must set the NDIS\_RECEIVE\_FILTER\_MAC\_HEADER\_DEST\_ADDR\_SUPPORTED flag.

<a href="" id="maxmacheaderfilters"></a>**MaxMacHeaderFilters**  
The maximum number of MAC header filters that the miniport driver supports. There should be at least as many header filters as there are VM queues.

<a href="" id="maxqueuegroups"></a>**MaxQueueGroups**  
This member is reserved for NDIS.

<a href="" id="maxqueuesperqueuegroup"></a>**MaxQueuesPerQueueGroup**  
This member is reserved for NDIS.

<a href="" id="minlookaheadsplitsize"></a>**MinLookaheadSplitSize**  
The minimum size, in bytes, that the network adapter supports for lookahead packet segments.

**Note**  Starting with NDIS 6.30, splitting packet data into separate lookahead buffers is no longer supported. Miniport drivers that support NDIS 6.30 or later versions must set this member to zero.

 

<a href="" id="maxlookaheadsplitsize"></a>**MaxLookaheadSplitSize**  
The maximum size, in bytes, that the network adapter supports for lookahead packet segments.

**Note**  Starting with NDIS 6.30, splitting packet data into separate lookahead buffers is no longer supported. Miniport drivers that support NDIS 6.30 or later versions must set this member to zero.

 

After a successful return from the [OID\_RECEIVE\_FILTER\_HARDWARE\_CAPABILITIES](https://msdn.microsoft.com/library/windows/hardware/ff569791) OID query, the **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure contains a pointer to an NDIS\_RECEIVE\_FILTER\_CAPABILITIES structure. These capabilities can include VMQ hardware capabilities that are currently disabled by INF file settings or through the **Advanced** properties page. For more information about VMQ INF files settings, see [VMQ Standard INF Entries](https://msdn.microsoft.com/library/windows/hardware/hh205410).

NDIS miniport drivers supply the receive-filtering hardware capabilities during initialization in the **HardwareReceiveFilterCapabilities** member of the [**NDIS\_MINIPORT\_ADAPTER\_HARDWARE\_ASSIST\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff565924) structure.

After a successful return from the [OID\_RECEIVE\_FILTER\_CURRENT\_CAPABILITIES](https://msdn.microsoft.com/library/windows/hardware/ff569786) OID query, the **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure contains a pointer to an [**NDIS\_RECEIVE\_FILTER\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff566864) structure. These capabilities include the currently enabled VMQ capabilities.

NDIS miniport drivers supply the currently enabled receive filtering capabilities during initialization in the **CurrentReceiveFilterCapabilities** member of the [**NDIS\_MINIPORT\_ADAPTER\_HARDWARE\_ASSIST\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff565924) structure.

NDIS reports the currently enabled receive filtering capabilities of an underlying network adapter to overlying protocol drivers in the **ReceiveFilterCapabilities** member of the [**NDIS\_BIND\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff564832) structure during the bind operation.

The [**NDIS\_RECEIVE\_FILTER\_GLOBAL\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff567171) structure is used in the [OID\_RECEIVE\_FILTER\_GLOBAL\_PARAMETERS](https://msdn.microsoft.com/library/windows/hardware/ff569790) query OID to obtain the current global receive filter settings.

NDIS\_RECEIVE\_FILTER\_GLOBAL\_PARAMETERS includes the following information:

<a href="" id="enabledfiltertypes"></a>**EnabledFilterTypes**  
The types of enabled receive filters. The NDIS\_RECEIVE\_FILTER\_VMQ\_FILTERS\_ENABLED flag specifies that virtual machine queue (VMQ) filters are enabled.

<a href="" id="enabledqueuetypes"></a>**EnabledQueueTypes**  
The types of enabled receive queues. The NDIS\_RECEIVE\_FILTER\_VM\_QUEUES\_ENABLED flag specifies that virtual machine (VM) queues are enabled.

After a successful return from the [OID\_RECEIVE\_FILTER\_GLOBAL\_PARAMETERS](https://msdn.microsoft.com/library/windows/hardware/ff569790) OID query, the **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure contains a pointer to an [**NDIS\_RECEIVE\_FILTER\_GLOBAL\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff567171) structure. The NDIS\_RECEIVE\_FILTER\_GLOBAL\_PARAMETERS structure specifies the receive-filtering features that are enabled or disabled on a network adapter.

NDIS protocol drivers use OID\_RECEIVE\_FILTER\_GLOBAL\_PARAMETERS to query the current global configuration parameters for receive filtering on a network adapter. For example, protocol drivers can use this OID to determine whether types of receive filters or receive queues are enabled or disabled.

 

 





