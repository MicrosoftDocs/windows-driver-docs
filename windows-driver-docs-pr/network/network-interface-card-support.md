---
title: Network Interface Card Support
description: Network Interface Card Support
ms.assetid: de673a37-3870-4995-b4f1-647b502e0773
keywords: ["miniport drivers WDK networking , NIC support", "NDIS miniport drivers WDK , NIC support", "NICs WDK networking , types", "network interface cards WDK networking , types", "bus-master DMA NICs WDK networking", "non-bus-master DMA NICs WDK networking"]
---

# Network Interface Card Support


## <a href="" id="ddk-network-interface-card-support-ng"></a>


Windows Vista and later versions of the operating system support the following types of network interface cards:

-   Ethernet (802.3)

-   Token Ring (802.5) (not supported on NDIS 6.0 drivers)

-   LocalTalk

-   WAN (point-to-point and WAN cards)

-   Connection-oriented WAN

-   Wireless

-   ATM (not supported or NDIS 6.0 drivers)

-   IrDA

To report a medium type, a miniport driver passes a pointer to an [**NDIS\_MINIPORT\_ADAPTER\_GENERAL\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff565923) structure in the *MiniportAttributes* parameter of the [**NdisMSetMiniportAttributes**](https://msdn.microsoft.com/library/windows/hardware/ff563672) function. A miniport driver calls **NdisMSetMiniportAttributes** from its [*MiniportInitializeEx*](https://msdn.microsoft.com/library/windows/hardware/ff559389) function during initialization. Miniport drivers should set the *MiniportAttributes* attributes after setting the registration attributes in the [**NDIS\_MINIPORT\_ADAPTER\_REGISTRATION\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff565934) structure and before setting any other attributes. Setting the *MiniportAttributes* attributes is mandatory.

When an overlying NDIS protocol driver calls [**NdisOpenAdapterEx**](https://msdn.microsoft.com/library/windows/hardware/ff563715) to bind to a specified miniport adapter, it provides a list of medium types on which it can operate. NDIS uses the information from the miniport driver and from the protocol driver to set up a binding. This binding provides the path for transferring network data up and down the driver stack.

### Types of NICs

The steps that a miniport driver completes to initialize a miniport adapter and to send and receive network data can depend on the features of a physical device, as follows.

-   Bus-master DMA NICs

    These NICs can directly access host memory through an on-board DMA controller that manages the transfer of data between the network and host memory without using the host CPU.

    To send, the miniport driver sets up the NIC to map the outgoing buffers. The miniport driver then causes the device to start its transfer from this memory. The NIC DMA controller transfers the data from shared system memory onto the network and interrupts the CPU when the send is complete. To receive, the DMA controller transfers incoming data to host memory before notifying the host with an interrupt.

    A bus-master DMA NIC typically has an onboard ring buffer that the miniport driver maps to a set of buffers in system memory. Typically, the NIC can be programmed to efficiently handle several packets. A miniport driver that manages such a NIC typically supports multipacket sends and receives because the NIC can efficiently handle several packets and thereby improve its I/O throughput.

-   Nonbusmaster DMA NICs

    These NICs include three general types of NICs:

    -   NICs that contain onboard shared memory

        A miniport driver that manages such a NIC must map the NIC's shared memory to host memory and then copy outgoing packets to the NIC memory or copy incoming frames from NIC memory to buffers that upper layer protocol drivers or other drivers supply. Such a miniport driver cannot typically improve its performance by supporting multipacket sends and receives.

    -   Subordinate DMA NICs

        A miniport driver that manages such a NIC uses the system DMA controller to manage the transfer of packet data to and from the network. Transfer of the data requires the cooperation of the host CPU.

    -   NICs that use programmed I/O

        The miniport driver that manages a PIO device uses NDIS functions to move outgoing frames byte by byte, word by word, or long by long to device registers and then causes the device to send the data. The driver for such a device does not benefit from NDIS support for multipacket sends and receives.

 

 





