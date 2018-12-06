---
title: Terminate Offload Requested by an Offload Target
description: Terminate Offload Requested by an Offload Target
ms.assetid: 2e0254c9-9dc4-4a85-b014-806974dbaabe
keywords:
- terminating offload state WDK TCP chimney offload , requested by offload target
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Terminate Offload Requested by an Offload Target


\[The TCP chimney offload feature is deprecated and should not be used.\]




An offload target can request the host stack to terminate the offload of either a single TCP connection or all TCP connections.

### Requesting the Termination of a Single TCP Connection

To request the termination of the offload of a single TCP connection, the offload target calls the [**NdisTcpOffloadEventHandler**](https://msdn.microsoft.com/library/windows/hardware/ff564595) function with the *EventType* parameter set to **TcpIndicateRetrieve**. The offload target specifies the reason for the termination request as a TCP\_UPLOAD\_REASON value in the *EventSpecificInformation* parameter that it passes to the *NdisTcpOffloadEventHandler* function. In response, the host stack calls the offload target's [**MiniportTerminateOffload**](https://msdn.microsoft.com/library/windows/hardware/ff559468) function as soon as possible.

The offload target can request the termination of only one TCP connection with each call to the *NdisTcpOffloadEventHandler* function. The offload target cannot request the termination of a neighbor state object or a path state object. For a description of events or circumstances that can cause an offload target to request the termination of the offload of a TCP connection, see the *NdisTcpOffloadEventHandler* function.There is no restriction on how many times an offload target can request the termination of the offload of a TCP connection.

Note that the host stack can terminate the offload of a TCP connection regardless of the state of that connection. In all such situations, the offload should comply with the termination request, if possible.

### Requesting the Termination of All Offloaded TCP Connections

An offload target can request the termination of all TCP connections that have been offloaded to it. To request such a termination, an offload target calls the [**NdisMIndicateStatusEx**](https://msdn.microsoft.com/library/windows/hardware/ff563600) function with the NDIS\_STATUS\_INDICATION-&gt; **StatusCode** member set to NDIS\_STATUS\_UPLOAD\_ALL. After completing the termination operation, the offload target can call the **NdisMIndicateStatusEx** function with the NDIS\_STATUS\_INDICATION-&gt; **StatusCode** member set to NDIS\_STATUS\_OFFLOAD\_RESUME. This value indicates to the host stack that the host stack can resume offloading TCP connections to the offload target.

This functionality might be used by an 802.3ad-capable intermediate driver when failing over from one network interface card (NIC) to another NIC.

 

 





