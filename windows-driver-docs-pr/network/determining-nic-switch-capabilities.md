---
title: Determining NIC Switch Capabilities
description: Determining NIC Switch Capabilities
ms.assetid: 5E627E52-2D47-4EA0-80D9-6979891CCE96
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Determining NIC Switch Capabilities


This topic describes how NDIS and overlying drivers determine the NIC switch capabilities of a network adapter that supports single root I/O virtualization (SR-IOV). This topic contains the following information:

[Reporting NIC Switch Capabilities during *MiniportInitializeEx*](#report)

[Querying NIC Switch Capabilities by Overlying Drivers](#query)

**Note**  Only the miniport driver for the PCI Express (PCIe) Physical Function (PF) of an SR-IOV network adapter can report NIC switch capabilities. Miniport drivers for PCIe Virtual Functions (VFs) must not report the NIC switch capabilities of the SR-IOV adapter.

 

For more information on NIC switches, see [NIC Switches](nic-switches.md).

## Reporting NIC Switch Capabilities during *MiniportInitializeEx*


When NDIS calls the miniport driver's [*MiniportInitializeEx*](https://msdn.microsoft.com/library/windows/hardware/ff559389) function, the driver provides the following NIC switch capabilities:

-   The complete set of hardware capabilities for a NIC switch that the network adapter can support.

    **Note**  Starting with NDIS 6.30, only one NIC switch is created on the network adapter. This switch is known as the *default NIC switch*.

     

-   The NIC switch capabilities that are currently enabled on the network adapter.

The miniport driver reports the NIC switch hardware capabilities of the underlying network adapter through an [**NDIS\_NIC\_SWITCH\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff566583) structure that is initialized in the following way:

1.  The miniport driver initializes the **Header** member. The driver sets the **Type** member of **Header** to NDIS\_OBJECT\_TYPE\_DEFAULT.

    Starting with NDIS 6.30, the miniport driver sets the **Revision** member of **Header** to NDIS\_NIC\_SWITCH\_CAPABILITIES\_REVISION\_2 and the **Size** member to NDIS\_SIZEOF\_NIC\_SWITCH\_CAPABILITIES\_REVISION\_2.

2.  The miniport driver sets appropriate flags in the **NicSwitchCapabilities** member of the [**NDIS\_NIC\_SWITCH\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff566583) structure to the NIC switch capabilities of the SR-IOV network adapter. For example, the miniport driver sets the NDIS\_NIC\_SWITCH\_CAPS\_PER\_VPORT\_INTERRUPT\_MODERATION\_SUPPORTED flag if the NIC switch supports interrupt moderation on each virtual port (VPort) that is created on the switch.

3.  The miniport driver sets the other members of the [**NDIS\_NIC\_SWITCH\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff566583) structure to the range of values for the NIC switch capabilities of the SR-IOV network adapter. For example, the miniport driver sets the **MaxNumVFs** and **MaxNumVPorts** members to the maximum number of VFs and VPorts that the adapter can support.

    **Note**  Depending on the available hardware resources on the network adapter, the miniport driver can set the **MaxNumVFs** member to a value that is less than its **\*NumVFs** keyword. For more information about this keyword, see [Standardized INF Keywords for SR-IOV](standardized-inf-keywords-for-sr-iov.md).

     

When NDIS calls the miniport driver's [*MiniportInitializeEx*](https://msdn.microsoft.com/library/windows/hardware/ff559389) function, the driver registers the NIC switch capabilities of the network adapter by following these steps:

1.  The miniport driver initializes an [**NDIS\_MINIPORT\_ADAPTER\_HARDWARE\_ASSIST\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff565924) structure.

    The miniport driver sets the **HardwareNicSwitchCapabilities** member to a pointer to a previously initialized [**NDIS\_NIC\_SWITCH\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff566583) structure.

    If the registry setting for the **\*SRIOV** INF keyword has a value of one, the network adapter is currently enabled for NIC switch creation and configuration. The miniport driver sets the **CurrentNicSwitchCapabilities** members to a pointer to the same [**NDIS\_NIC\_SWITCH\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff566583) structure.

    If the registry setting for the **\*SRIOV** INF keyword has a value of zero, the network adapter is not currently enabled for NIC switch creation and configuration. The miniport driver must set the **CurrentNicSwitchCapabilities** member to NULL.

    For more information about the **\*SRIOV** INF keyword, see [Standardized INF Keywords for SR-IOV](standardized-inf-keywords-for-sr-iov.md).

2.  The driver calls [**NdisMSetMiniportAttributes**](https://msdn.microsoft.com/library/windows/hardware/ff563672) and sets the *MiniportAttributes* parameter to a pointer to the [**NDIS\_MINIPORT\_ADAPTER\_HARDWARE\_ASSIST\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff565924) structure.

For more information about the adapter initialization process, see [Initializing a Miniport Adapter](initializing-a-miniport-adapter.md).

## Querying NIC Switch Capabilities by Overlying Drivers


NDIS passes the network adapter's currently enabled NIC switch capabilities to overlying drivers that bind to the network adapter in the following way:

-   When NDIS calls an overlying filter driver's [*FilterAttach*](https://msdn.microsoft.com/library/windows/hardware/ff549905) function, NDIS passes the network adapter's NIC switch capabilities through the *AttachParameters* parameter. This parameter contains a pointer to an [**NDIS\_FILTER\_ATTACH\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff565481) structure. The **NicSwitchCapabilities** member of this structure contains a pointer to an [**NDIS\_NIC\_SWITCH\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff566583) structure.

-   When NDIS calls an overlying protocol driver's [*ProtocolBindAdapterEx*](https://msdn.microsoft.com/library/windows/hardware/ff570220) function, NDIS passes the network adapter's NIC switch capabilities through the *BindParameters* parameter. This parameter contains a pointer to an [**NDIS\_FILTER\_ATTACH\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff565481) structure. The **NicSwitchCapabilities** member of this structure contains a pointer to an [**NDIS\_NIC\_SWITCH\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff566583) structure.

NDIS also returns the [**NDIS\_NIC\_SWITCH\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff566583) structure when it handles object identifier (OID) query requests of [OID\_NIC\_SWITCH\_HARDWARE\_CAPABILITIES](https://msdn.microsoft.com/library/windows/hardware/ff569761) and [OID\_NIC\_SWITCH\_CURRENT\_CAPABILITIES](https://msdn.microsoft.com/library/windows/hardware/ff569760) that are issued by overlying protocol or filter drivers.

 

 





