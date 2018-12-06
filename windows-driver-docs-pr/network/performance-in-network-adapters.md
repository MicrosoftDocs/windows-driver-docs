---
title: Performance in Network Adapters
description: There are always tradeoffs in deciding which hardware functions to implement on a network adapter.
ms.assetid: 7BE3FC13-DEE1-41A2-9B4A-D04CF5D0FC9B
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Performance in Network Adapters


There are always tradeoffs in deciding which hardware functions to implement on a network adapter. It is becoming increasingly important to consider adding task offload features that allow for interrupt moderation, dynamic tuning on the hardware, improving the use of the PCI bus, and supporting Jumbo Frames. These are particularly important for the high-end network adapter that will be used in configurations requiring top performance.

-   [Supporting TCP and IP checksum offload](#supporting-tcp-and-ip-checksum-offload)
-   [Supporting large send offload (LSO)](#supporting-large-send-offload-lso)
-   [Supporting IP security (IPSec) offload](#supporting-ip-security-ipsec-offload)
-   [Improving interrupt moderation](#improving-interrupt-moderation)
-   [Using the PCI bus efficiently](#using-the-pci-bus-efficiently)
-   [Supporting jumbo frames](#supporting-jumbo-frames)

## Supporting TCP and IP checksum offload


For most common network traffic, offloading checksum calculation to the network adapter hardware offers a significant performance advantage by reducing the number of CPU cycles required per byte. Checksum calculation is the most expensive function in the networking stack for two reasons:

-   It contributes to long path length.
-   It causes cache churning effects (typically on the sender).

Offloading checksum calculation to the sender improves the overall system performance by reducing the load on the host CPU and increasing cache effectiveness.

In the Windows Performance Lab, we have measured TCP throughput improvements of 19% when checksum was offloaded during network-intensive workloads. Analysis of this improvement shows that 11% of the total improvement is due to the path length reduction, and 8% is due to increasing the caches effectiveness.

Offloading checksum on the receiver has the same advantages as offloading checksum on the sender. Increased benefit can be seen on systems that act as both client and server, such as a sockets proxy server. On systems where the CPU is not necessarily busy, such as a client system, the benefit of offloading checksum may be seen in better network response times, rather than in noticeably improved throughput.

## Supporting large send offload (LSO)


Windows offers the ability for the network adapter/driver to advertise a larger Maximum Segment Size (MSS) than the MTU to TCP up to 64K. This allows TCP to allocate a buffer of up to 64K to the driver, which divides the large buffer into packets that fit within the network MTU.

The TCP segmenting work is done by the network adapter/driver hardware instead of the host CPU . This results in a significant performance improvement if the network adapter CPU is able to handle the additional work.

For many of the network adapters tested, there was little improvement seen for pure networking activities when the host CPU was more powerful than the network adapter hardware. However, for typical business workloads, an overall system performance improvement of up to 9% of the throughput has been measured, because the host CPU uses most of its cycles to execute transactions. In these cases, offloading TCP segmentation to the hardware frees the host CPU from the load of segmentation, allowing it extra cycles to perform more transactions.

## Supporting IP security (IPSec) offload


Windows offers the ability to offload the encryption work of IPSec to the network adapter hardware. Encryption, especially 3 DES (also known as triple DES), has a very high cycles/byte ratio. Therefore, it is no surprise that offloading IPSec to the network adapter hardware measured a 30% performance boost in secure Internet and VPN tests.

## Improving interrupt moderation


A simple network adapter generates a hardware interrupt on the host upon the arrival of a packet or to signal completion of a packet send request. Interrupt latency and resulting cache churning effects add overhead to the overall networking performance. In many scenarios (for example, heavy system usage or heavy network traffic), it is best to reduce the cost of the hardware interrupt by processing several packets for each interrupt.

With heavy network workloads, up to 9% performance improvement in throughput has been measured over network-intensive workloads. However, tuning Interrupt Moderation parameters only for throughput improvements may result in a performance hit on the response time. To maintain optimum settings and accommodate for different workloads, it is best to allow for dynamically adjusted parameters as described in the Auto-tuning later in this article.

## Using the PCI bus efficiently


One of the most important factors in the network adapter hardware performance is how efficiently it uses the PCI bus. Further, the network adapter's DMA performance affects the performance of all PCI cards that are on the same PCI bus. The following guidelines must be considered when optimizing PCI usage:

-   Streamline DMA transfers by aggregating target pages where appropriate.

-   Reduce PCI protocol overhead by performing DMA in large chunks (at least 256 bytes). If possible, time the flow of data so that entire packets are transferred in a single PCI transaction. However, consider how the transfer should take place. For example, do not wait for all of the data to arrive before initiating transfers, because waiting will increase latency and consume additional buffer space.

-   It is better to pad the DMA packet transfer with additional bytes, rather than requiring a short extra transfer to "clean up" by transferring the last few bytes of the packet.

-   Use the Memory Read, Memory Read Line, and Memory Read Multiple transactions as recommended by the PCI specification.

-   The network adapter bus interface hardware should detect limitations in the host memory controller and adjust behavior accordingly. In example, the network adapter bus interface hardware should detect memory-controller pre-fetch limitations on a DMA Memory Reads and wait for a short period before attempting the transaction again. The hardware should detect excessive retries on the part of the network adapter and increase the time before the first retry on future transactions when cut off by the host. There is no point in continuing to submit transactions to the memory controller when you are certain that it is still busy fetching the next sequential set of data.

-   Minimize the insertion of wait states, especially during data transfers. It is better to relinquish the bus and let another PCI adapter using the bus get some work done if more than one or two wait states are going to be inserted.

-   Use Memory Mapped I/O instead of Programmed I/O. This is also true for drivers.

## Supporting jumbo frames


Supporting larger Maximum Transmission Units (MTUs) and thus larger frame sizes, specifically Jumbo Frames, will reduce the network stack overhead incurred per byte. A 20% TCP throughput increase has been measured when the MTU was changed from 1514 to 9000. Also, a significant reduction of CPU utilization is obtained due to the fewer number of calls from the network stack to the network driver.

 

 





