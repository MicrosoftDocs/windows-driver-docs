---
title: Common Control Nodes and Filters
author: windows-driver-content
description: Common Control Nodes and Filters
ms.assetid: 33e0605b-0fd1-4506-a48b-427976e94dfc
keywords:
- control nodes WDK BDA
- nodes WDK BDA
- network provider filters WDK BDA
- tuner control nodes WDK BDA
- demodulator control nodes WDK BDA
- capture filters WDK BDA
- PID Filter control node WDK BDA
- IPSink WDK BDA
- NDISIP WDK BDA
- Broadcast Driver Architecture WDK AVStream , control nodes
- BDA WDK AVStream , control nodes
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Common Control Nodes and Filters


## <a href="" id="ddk-common-control-nodes-and-filters-ksg"></a>


The types of control nodes and filters that are shown in the figures in the [Control Nodes, Filters and Hardware](control-nodes--filters-and-hardware.md) section are common to the reception of digital satellite, terrestrial, and cable broadcasts. However, you can create other node types and filters for a wide variety of broadcast media and devices as well. It is important to remember that each control node need not correspond to a single BDA device filter. In some cases, a single BDA device filter can encapsulate more than one control node.

The following list describes control nodes and filters that are commonly found in Broadcast Architecture:

<a href="" id="network-provider"></a>**Network Provider**  
A *network provider filter* (or *network provider*) routes a digital television signal to and through BDA devices. A variety of broadcast providers currently transmit digital television signals over three basic network types--satellite, cable and antenna. These digital signals are transmitted in formats defined by multiple standards, including ATSC, DVB-S, DVB-C, and DVB-T. BDA devices receive and manage these digital signals.

A network provider:

-   is the source filter in a filter graph, although no data actually passes through it.

-   exists for each network type or can be created for a new network type.

-   participates in the graph building process.

-   communicates with other filters in the graph through property and method sets of BDA minidrivers that initialized such filters.

Each network provider can build a different graph configuration for its associated network type. Applications pass tune requests to a network provider, which in turn passes the information to a BDA minidriver. See the Broadcast Architecture section of the Microsoft Windows SDK documentation for more information.

<a href="" id="tuner"></a>**Tuner**  
This control node filters the particular frequency that carries the transport stream. It can appear inside a filter by itself or together with other control nodes.

<a href="" id="demodulator"></a>**Demodulator**  
A control node that translates the analog signal into a digital bit stream. It can appear inside a filter by itself or together with other control nodes.

<a href="" id="capture"></a>**Capture**  
A filter that moves the data into host memory.

<a href="" id="pid-filter"></a>**PID Filter**  
A control node that selects one or more elementary data streams from the transport stream. This is the primary function of a demultiplexer. It can appear inside a filter by itself or together with other control nodes.

<a href="" id="mpe-parser"></a>**MPE Parser**  
A filter that parses IP data from a stream containing MPEG-2 private sections.

<a href="" id="ipsink"></a>**IPSink**  
A filter that accepts IP packets as data samples and forwards the data to the NDIS TCP/IP stack.

<a href="" id="ndisip"></a>**NDISIP**  
An NDIS miniport driver that acts as a receiver for a network adapter for the data that the IPSink filter passes.

**Note**   Starting with Windows Vista, the IPSink filter is not supported.

 

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20Common%20Control%20Nodes%20and%20Filters%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


