---
title: Packet Flow over a Virtual Port
description: Packet Flow over a Virtual Port
ms.assetid: 1E4B1987-3288-4082-B8A8-0F275C61597F
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Packet Flow over a Virtual Port


The default NIC switch is a component of a network adapter that supports the single root I/O virtualization (SR-IOV) interface. The switch always attaches the default virtual port (VPort) to the PCI Express (PCIe) Physical Function (PF). The switch can attach one or more nondefault VPorts to the PF. For more information, see [Creating a Virtual Port](creating-a-virtual-port.md).

The following points apply to packets that are sent or received on a VPort that is attached to the PF:

-   Packets sent or received over the default VPort are specified with a VPort identifier value of **DEFAULT\_VPORT\_ID**.

    Packets sent or received over nondefault VPorts are specified with the VPort identifier that was returned when the VPort was created through an OID method request of [OID\_NIC\_SWITCH\_CREATE\_VPORT](https://msdn.microsoft.com/library/windows/hardware/hh451816). When the driver handles this OID request, it obtains the VPort identifier from the **VPortId** member of the [**NDIS\_NIC\_SWITCH\_VPORT\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh451597) structure that is associated with the OID request.

    **Note**  When a VPort is deleted, it is possible for the miniport driver to receive an NBL that contains an invalid **VPortId** value. If this happens, the miniport should ignore the invalid VPort ID and use **DEFAULT\_VPORT\_ID** instead. The **VPortId** is found in the **NetBufferListFilteringInfo** portion of the NBL's OOB data, and is retrieved by using the [**NET\_BUFFER\_LIST\_RECEIVE\_FILTER\_VPORT\_ID**](https://msdn.microsoft.com/library/windows/hardware/hh439946) macro.

     

-   The PF miniport driver calls [**NdisMIndicateReceiveNetBufferLists**](https://msdn.microsoft.com/library/windows/hardware/ff563598) to indicate packets received from a VPort. Before the PF miniport driver calls **NdisMIndicateReceiveNetBufferLists**, it must set the VPort identifier in the out-of-band (OOB) data in the [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structure for the packet. The driver does this by using the [**NET\_BUFFER\_LIST\_RECEIVE\_FILTER\_VPORT\_ID**](https://msdn.microsoft.com/library/windows/hardware/hh439946) macro.

-   The virtualization stack calls [**NdisSendNetBufferLists**](https://msdn.microsoft.com/library/windows/hardware/ff564535) to transmit packets to a VPort. Before the virtualization stack calls **NdisSendNetBufferLists**, it sets the VPort identifier in the OOB data in the [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structure for the packet.

    The miniport driver obtains the VPort identifier by using the [**NET\_BUFFER\_LIST\_RECEIVE\_FILTER\_VPORT\_ID**](https://msdn.microsoft.com/library/windows/hardware/hh439946) macro.

    The miniport driver must queue the transmit packet on the hardware transmit queue of the specified VPort.

**Note**  The miniport driver for the PCIe Virtual Function (VF) does not set or query the VPort identifier in the OOB data of the [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structure for a packet. When the VF miniport driver sends a packet, it queues the packet on the hardware transmit queue for the single nondefault VPort that is attached to the VF.

 

 

 





