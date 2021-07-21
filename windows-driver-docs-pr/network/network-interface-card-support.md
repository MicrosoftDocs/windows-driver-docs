---
title: Network Interface Card Support
description: Network Interface Card Support
keywords:
- miniport drivers WDK networking , NIC support
- NDIS miniport drivers WDK , NIC support
- NICs WDK networking , types
- network interface cards WDK networking , types
- bus-master DMA NICs WDK networking
- non-bus-master DMA NICs WDK networking
ms.date: 06/11/2018
ms.localizationpriority: medium
---

# Network Interface Card Support

This topic describes the types of Network Interface Cards (NICs) that an NDIS miniport driver can manage, as well as how the different kinds of NICs affect the way a driver transfers network data.

## Reporting a NIC's medium type to NDIS

To report a medium type for a NIC, a miniport driver passes a pointer to an [**NDIS\_MINIPORT\_ADAPTER\_GENERAL\_ATTRIBUTES**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_miniport_adapter_general_attributes) structure in the *MiniportAttributes* parameter of the [**NdisMSetMiniportAttributes**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismsetminiportattributes) function. A miniport driver calls **NdisMSetMiniportAttributes** from its [*MiniportInitializeEx*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_initialize) function during initialization. Miniport drivers should set the *MiniportAttributes* attributes after setting the registration attributes in the [**NDIS\_MINIPORT\_ADAPTER\_REGISTRATION\_ATTRIBUTES**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_miniport_adapter_registration_attributes) structure and before setting any other attributes. Setting the *MiniportAttributes* attributes is mandatory. The driver sets the **MediaType** member of the **NDIS_MINIPORT_ADAPTER_GENERAL_ATTRIBUTES** structure to the appropriate media type when setting the *MiniportAttributes* attributes.

When an overlying NDIS protocol driver calls [**NdisOpenAdapterEx**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisopenadapterex) to bind to a specified miniport adapter, it provides a list of medium types on which it can operate. NDIS uses the information from the miniport driver and from the protocol driver to set up a binding. This binding provides the path for transferring network data up and down the driver stack.

## Physical NICs

The steps that a miniport driver completes to initialize a miniport adapter and to send and receive network data can depend on the features of a physical device, as follows.

- NDIS-WDM NICs

    With NDIS-WDM NICs, such as USB-based NICs, the way the miniport driver manages memory with DMA does not matter to NDIS and is not visible to it.

- Bus-master DMA NICs

    These NICs can directly access host memory through an on-board DMA controller that manages the transfer of data between the network and host memory without using the host CPU.

    To send, the miniport driver sets up the NIC to map the outgoing buffers. The miniport driver then causes the device to start its transfer from this memory. The NIC DMA controller transfers the data from shared system memory onto the network and interrupts the CPU when the send is complete. To receive, the DMA controller transfers incoming data to host memory before notifying the host with an interrupt.

    A bus-master DMA NIC typically has an onboard ring buffer that the miniport driver maps to a set of buffers in system memory. Typically, the NIC can be programmed to efficiently handle several packets. A miniport driver that manages such a NIC typically supports multipacket sends and receives because the NIC can efficiently handle several packets and thereby improve its I/O throughput.

- Nonbusmaster DMA NICs

    Currently, nonbusmaster DMA NICs include the following:

    -   System DMA NICs

        A miniport driver that manages such a NIC uses the system DMA controller to manage the transfer of packet data to and from the network. Transfer of the data requires the cooperation of the host CPU.

## Virtual NICs and miniports

In a virtual machine, NDIS miniport drivers can manage either software-only resources as a virtual miniport, or they can manage a virtual NIC that represents hardware resources. The following table explains the differences between a virtual miniport and a virtual NIC.

|  Attribute | Virtual miniport | Virtual NIC |
| --- | --- | --- |
| Definition | An NDIS miniport driver that maps to a software-enumerated PnP device. | A NIC managed by the host OS hypervisor. The hypervisor makes the virtual machine think that it has some hardware, but no such hardware actually exists in the physical world. |
| Has interrupts | No | Yes |
| Can use DMA | No | Yes |
| Is created or destroyed by... | The guest OS | The host OS |
| Can reach outside of a guest VM | No | Yes |
