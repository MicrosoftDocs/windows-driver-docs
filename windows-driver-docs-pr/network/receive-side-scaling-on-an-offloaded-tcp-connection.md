---
title: Receive Side Scaling on an Offloaded TCP Connection
description: Receive Side Scaling on an Offloaded TCP Connection
ms.assetid: bc389304-c8e0-463e-adcd-61b866f58292
keywords:
- data I/O WDK TCP chimney offload , receive side scaling
- I/O WDK TCP chimney offload , receive side scaling
- received data processing WDK TCP chimney offload , receive side scaling
- receive side scaling WDK TCP chimney offload
- RSS WDK TCP chimney offload
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Receive Side Scaling on an Offloaded TCP Connection


\[The TCP chimney offload feature is deprecated and should not be used.\]




An offload target can implement receive side scaling (RSS). For more information about RSS processing, see [NDIS 6.0 Receive-Side Scaling](ndis-receive-side-scaling2.md).

In standard RSS processing, the network interface card (NIC) calculates the RSS hash value for each incoming packet. An offload target, however, does not need to calculate an RSS hash value. Instead, the host stack calculates an RSS hash value for each TCP connection when that connection is established. When the host stack offloads a TCP connection to an offload target, the host stack supplies the RSS hash value for the connection. The RSS hash value is the value of the **HashValue** member of the [**TCP\_OFFLOAD\_STATE\_CONST**](https://msdn.microsoft.com/library/windows/hardware/ff570938) structure. The RSS hash value that is supplied by the host stack applies to all data that is received on the offloaded TCP connection.

An offload target must deliver receive data to the host stack in the order that the offload target received it. This requirement applies even if the CPU to which receive processing is assigned changes because of an update to the indirection table that the offload target uses for RSS processing. (For more information about the indirection table, see [Introduction to Receive Side Scaling](introduction-to-receive-side-scaling.md).)

The example in the following paragraphs illustrates the difference between standard packet-based receive side scaling and receive side scaling on an offloaded TCP connection.

Assume that a NIC has two receive queues, designated Queue A and Queue B. The NIC uses these queues to balance the load of incoming data. Also assume that the NIC is processing data for a single TCP connection. The NIC processes data in the queues as follows:

1.  The NIC fills a buffer with data from packet 0 and uses the hash value to find the CPU number in the indirection table. The indirection table indicates that data that is received on the connection should be processed on CPU 1. Through an implementation-specific algorithm, the NIC determines that it should place data from packet 0 in Queue A. Data from Queue A is processed on CPU 1.

2.  The host stack or other overlying driver sets the [OID\_GEN\_RECEIVE\_SCALE\_PARAMETERS](https://msdn.microsoft.com/library/windows/hardware/ff569637) OID to update the NIC's indirection table. This update reassigns the processing of data for the connection's hash value from CPU 1 to CPU 3.

3.  The NIC fills a buffer with data from packet 1 and, through an implementation-specific algorithm, determines that it should place data from packet 1 in Queue B. Data from Queue B is processed on CPU 3. The offload target places data from packet 1 in Queue B. CPU 3 processes its queue before CPU 1.

4.  The NIC, which is not performing receive side scaling on an offloaded TCP connection, can deliver the data from packet 1 and the data from packet 0 in any order without any difference. An offload target, however, that is performing receive side scaling on an offloaded TCP connection, must deliver data from packet 0 to the host stack before delivering data from packet 1, even though, after the update to the indirection table, data (from packet 1) in Queue B is processed before data (from packet 0) in Queue A.

To deliver the data from either queue, the offload target calls either the [**NdisTcpOffloadReceiveComplete**](https://msdn.microsoft.com/library/windows/hardware/ff564599) function, the [**NdisTcpOffloadReceiveHandler**](https://msdn.microsoft.com/library/windows/hardware/ff564606) function, or both. For more information about the algorithm that the offload target uses to deliver received data, see [Delivery Algorithm](delivery-algorithm.md).)

The preceding example is not prescriptive. An offload target can implement another way of accomplishing the task. The only requirement is that the offload target deliver the data in the order in which it received the data.

 

 





