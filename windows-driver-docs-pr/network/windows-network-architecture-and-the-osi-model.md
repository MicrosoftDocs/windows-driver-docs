---
title: Windows Network Architecture and the OSI Model
description: Windows Network Architecture and the OSI Model
keywords:
- OSI reference model WDK networking
- transport layer WDK networking
- data link layer WDK networking
- MAC layer WDK networking
- physical layer WDK networking
- Windows network architecture WDK
ms.date: 09/04/2020
ms.localizationpriority: medium
ms.custom: contperf-fy21q1
---

# Windows Network Architecture and the OSI Model

This topic discusses the Windows network architecture and how Windows network drivers implement the bottom four layers of the OSI model.

If you are looking for general information on all seven layers of the model, see the [OSI model](https://en.wikipedia.org/wiki/OSI_model).

The Microsoft Windows operating systems use a network architecture that is based on the seven-layer networking model developed by the International Organization for Standardization (ISO). 

Introduced in 1978, the ISO Open Systems Interconnection (OSI) Reference model describes networking as "a series of protocol layers with a specific set of functions allocated to each layer. Each layer offers specific services to higher layers while shielding these layers from the details of how the services are implemented. A well-defined interface between each pair of adjacent layers defines the services offered by the lower layer to the higher one and how those services are accessed." 

The following diagram illustrates the OSI model.

![diagram illustrating the osi reference model.](images/101osi.png)

Microsoft Windows network drivers implement the bottom four layers of the OSI model.

## Physical Layer  
The physical layer is the lowest layer of the OSI model. This layer manages the reception and transmission of the unstructured raw bit stream over a physical medium. It describes the electrical/optical, mechanical, and functional interfaces to the physical medium. The physical layer carries the signals for all of the higher layers. 

In Windows, the physical layer is implemented by the network interface card (NIC), its transceiver, and the medium to which the NIC is attached.

## Data Link Layer  

The data link layer sends frames between physical addresses and is responsible for error detection and recovery occurring in the physical layer. 

The data link layer is further divided by the Institute of Electrical and Electronics Engineers (IEEE) into two sublayers: media access control (MAC) and logical link control (LLC).

### MAC

The MAC sublayer manages access to the physical layer, checks frame errors, and manages address recognition of received frames.

In the Windows network architecture, the MAC sublayer is implemented in the NIC. The NIC is controlled by a software device driver called the [miniport driver](ndis-miniport-drivers2.md). Windows supports several variations of miniport drivers including WDM miniport drivers, miniport call managers (MCMs), and miniport [intermediate drivers](ndis-intermediate-drivers.md).

### LLC

The LLC sublayer provides error-free transfer of data frames from one node to another. The LLC sublayer establishes and terminates logical links, controls frame flow, sequences frames, acknowledges frames, and retransmits unacknowledged frames. The LLC sublayer uses frame acknowledgement and retransmission to provide virtually error free transmission over the link to the layers above.

In Windows, the LLC sublayer is implemented by a software driver known as a [protocol driver](./roadmap-for-developing-ndis-protocol-drivers.md).

## Network Layer
The network layer controls the operation of the subnet. This layer determines the physical path that the data should take, based on the following:

-   Network conditions

-   Priority of service

-   Other factors, such as routing, traffic control, frame fragmentation and reassembly, logical-to-physical address mapping, and usage accounting

The network layer is implemented by a [protocol driver](./roadmap-for-developing-ndis-protocol-drivers.md).

## Transport Layer

The transport layer ensures that messages are delivered error free, in sequence, and with no loss or duplication. This layer relieves the higher-layer protocols from being concerned about data transfer with their peers. 

A minimal transport layer is required in protocol stacks that include a reliable network or LLC sublayer that provides virtual circuit capability. For example, because the NetBEUI transport driver for Windows is an OSI-compliant LLC sublayer, its transport layer functions are minimal. If the protocol stack does not include an LLC sublayer, and if the network layer is unreliable and/or supports datagrams (as with TCP/IP's IP layer or NWLink's IPX layer), the transport layer should include frame sequencing and acknowledgment, as well as retransmission of unacknowledged frames.

In the Windows network architecture, the transport layer is implemented by a [protocol driver](./roadmap-for-developing-ndis-protocol-drivers.md), which is sometimes referred to a *transport driver*.

 

