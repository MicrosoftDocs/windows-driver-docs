---
title: Windows network architecture and the OSI model
description: Windows network architecture and how Windows network drivers implement the bottom four layers of the OSI model.
ms.date: 12/15/2023
---

# Windows network architecture and the OSI model

This article explores the Windows network architecture and how Windows network drivers implement the *bottom four* layers of the OSI model.

For general information on all seven layers of the model, see the [OSI model](https://en.wikipedia.org/wiki/OSI_model).

The Microsoft Windows operating systems use a network architecture that is based on the seven-layer networking model developed by the International Organization for Standardization (ISO) in 1978. 

The ISO Open Systems Interconnection (OSI) Reference model describes networking as "a series of protocol layers with a specific set of functions allocated to each layer. Each layer offers specific services to higher layers while shielding these layers from the details of how the services are implemented. A well-defined interface between each pair of adjacent layers defines the services offered by the lower layer to the higher one and how those services are accessed." 

The following diagram illustrates the OSI model.

:::image type="content" source="images/101osi.png" alt-text="Diagram that shows the seven layers of the OSI reference model.":::

Windows [network drivers](ndis-drivers.md) implement the bottom four layers of the OSI model. 

## Physical layer  
The physical layer is the lowest layer of the OSI model. This layer manages the reception and transmission of the unstructured raw bit stream over a physical medium. It describes the electrical/optical, mechanical, and functional interfaces to the physical medium. The physical layer carries the signals for all of the higher layers. 

In Windows, the network interface card (NIC) implements the physical layer, its transceiver, and the medium to which the NIC is attached.

## Data link layer  

The data link layer sends frames between physical addresses and is responsible for error detection and recovery occurring in the physical layer. 

The data link layer is further divided by the Institute of Electrical and Electronics Engineers (IEEE) into two sublayers: media access control (MAC) and logical link control (LLC).

### MAC

The MAC sublayer manages access to the physical layer, checks frame errors, and manages address recognition of received frames.

In the Windows network architecture, the MAC sublayer is implemented in the NIC. The NIC is controlled by a software device driver called the [miniport driver](ndis-miniport-drivers2.md). Windows supports several variations of miniport drivers including WDM miniport drivers, miniport call managers (MCMs), and miniport [intermediate drivers](ndis-intermediate-drivers.md).

### LLC

The LLC sublayer provides error-free transfer of data frames from one node to another. The LLC sublayer establishes and terminates logical links, controls frame flow, sequences frames, acknowledges frames, and retransmits unacknowledged frames. The LLC sublayer uses frame acknowledgment and retransmission to provide virtually error free transmission over the link to the layers above.

In Windows, a software driver known as a [protocol driver](./roadmap-for-developing-ndis-protocol-drivers.md) implements the LLC sublayer.

## Network layer
The network layer controls the operation of the subnet. This layer determines the physical path that the data should take, based on the following:

-   Network conditions

-   Priority of service

-   Other factors, such as routing, traffic control, frame fragmentation and reassembly, logical-to-physical address mapping, and usage accounting

A [protocol driver](./roadmap-for-developing-ndis-protocol-drivers.md) implements the network layer.

## Transport layer

The transport layer ensures that messages are delivered error free, in sequence, and with no loss or duplication. This layer relieves the higher-layer protocols from being concerned about data transfer with their peers. 

A minimal transport layer is required in protocol stacks that include a reliable network or LLC sublayer that provides virtual circuit capability. For example, because the NetBEUI transport driver for Windows is an OSI-compliant LLC sublayer, its transport layer functions are minimal. If the protocol stack doesn't include an LLC sublayer, and if the network layer is unreliable or supports datagrams (as with TCP/IP's IP layer or NWLink's IPX layer), the transport layer should include frame sequencing and acknowledgment, as well as retransmission of unacknowledged frames.

In the Windows network architecture, a [protocol driver](./roadmap-for-developing-ndis-protocol-drivers.md), sometimes referred to a *transport driver*, implements the transport layer.
