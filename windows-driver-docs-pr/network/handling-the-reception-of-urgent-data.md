---
title: Handling the Reception of Urgent Data
description: Handling the Reception of Urgent Data
ms.assetid: 2a2e4209-6d11-433a-90df-bdbb7a60503b
keywords:
- non-standard packets and messages WDK TCP chimney offload , urgent data
- urgent data WDK TCP chimney offload
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Handling the Reception of Urgent Data


\[The TCP chimney offload feature is deprecated and should not be used.\]

If an offload target receives urgent data (that is, a TCP segment in which the URG flag of the TCP header is set) on an offloaded TCP connection, it does the following:

1.  Verifies that the received segment's sequence number is in the window and validates the ACK number in the segment. If one or both of these numbers is invalid, the offload target should discard the packet and continue normal processing on the offloaded connection. If these numbers are both valid, the offload target continues with step 2.

2.  Calls the [**NdisTcpOffloadEventHandler**](https://msdn.microsoft.com/library/windows/hardware/ff564595) function with the *EventType* parameter set to **TcpIndicateRetrieve** and the *EventSpecificInformation* parameter set to **ReceivedUrgentData**. This action requests the host stack to terminate the offload of the connection.

3.  Does not send acknowledgements for any subsequent TCP segments that are received on the connection.

4.  Queues the urgent data, and any subsequently received data on the connection.

5.  Terminates the offload of the connection when the offload target's [**MiniportTerminateOffload**](https://msdn.microsoft.com/library/windows/hardware/ff559468) function is called.

6.  Indicates the urgent data, and any subsequently received data on the connection, to the host stack through the non-offload NDIS interface.

At any time, the host stack can pass urgent data, as buffered receive data, to an offload target when offloading a TCP connection. (For more information about this situation, see [Handling Buffered Receive Data During and After an Offload Operation](handling-buffered-receive-data-during-and-after-an-offload-operation.md).) An offload target must process such urgent data by using the preceding procedure. That is, an offload target must process the urgent data that is received in this way in the same way that it processes urgent data that is received from the network.

 

 





