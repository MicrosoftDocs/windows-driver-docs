---
title: Terminate Offload Initiated by the Host Stack
description: Terminate Offload Initiated by the Host Stack
ms.assetid: 5ccb5621-b483-4520-8971-5e110c80bc82
keywords:
- terminating offload state WDK TCP chimney offload , initiated by host stack
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Terminate Offload Initiated by the Host Stack


\[The TCP chimney offload feature is deprecated and should not be used.\]




The host stack can terminate the offload of an individual neighbor, path, or TCP connection state object. After terminating all of the state objects that depend on a neighbor or path state object, the host stack terminates the offload of that neighbor or path state object. For example, after terminating all of the TCP connection state objects that are linked to a path state object, the host stack terminates the offload of the path state object, which is no longer serving a useful purpose.

The host stack can also terminate the offload of any combination of state objects. If the host stack terminates the offload of a combination of state objects that includes neighbor or path state objects or both, the host stack also terminates the offload of all of the dependent state objects that are linked to the neighbor or path state objects or both.

The host stack can terminate the offload of a TCP connection for a variety of reasons, including the following:

-   Higher priority TCP connections need to be offloaded.

-   An offload target requests the termination. (For more information about this type of termination, see [Terminate Offload Requested by an Offload Target](terminate-offload-requested-by-an-offload-target.md).)

-   The host stack detects that not enough data is being sent or received on the connection.

-   The media connection to the network interface card (NIC) is lost.

    When the network media is disconnected from the NIC or the link goes down for other reasons, the miniport driver calls the [**NdisMIndicateStatusEx**](https://msdn.microsoft.com/library/windows/hardware/ff563600) function to indicate the event. NDIS then calls the host stack's [*ProtocolNetPnPEvent*](https://msdn.microsoft.com/library/windows/hardware/ff570263) function, and the host stack determines whether the best course of action is to terminate the offload of the TCP connection. The offload target should not make the decision in this situation.

-   A protocol receives NetEventPause event.

Note that the preceding list of reasons is not complete.

For each neighbor state object and path state object, the host stack maintains a reference count of dependent state objects. The host stack terminates the offload of a neighbor state object and path state object only when the reference count for that object is zero. The host stack never terminates the offload of a state object that still has dependent state objects linked to it.

 

 





