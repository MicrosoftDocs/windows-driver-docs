---
title: Handling Invalidated State Objects
description: Handling Invalidated State Objects
ms.assetid: 83104164-e5f2-4aa4-aea2-1a1c1e6abe9c
keywords:
- invalidating offloaded state WDK TCP chimney offload , offload target response
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Handling Invalidated State Objects


\[The TCP chimney offload feature is deprecated and should not be used.\]




If the host stack requests to invalidate state, an offload target should respond as follows:

1.  Mark the state as invalid in the offload context area that contains the state. (For more information about the offload context area, see [Storing and Referencing Offloaded State](storing-and-referencing-offloaded-state.md).)

2.  Immediately stop processing send segments on any invalidated TCP connections or any valid TCP connections that depend on invalidated neighbor or path state objects.

3.  Request that the host stack terminate the offload of any invalidated TCP connections or any valid TCP connections that depend on invalidated state. The offload target requests such terminations by calling the [**NdisTcpOffloadEventHandler**](https://msdn.microsoft.com/library/windows/hardware/ff564595) function with the *EventSpecificInformation* parameter set to **InvalidState**.

4.  Must not free the resources for the invalidated state until the host stack has [terminated the offload of the invalidated state object](terminating-offload-state.md). The offload target owns the invalidated state object until the offload of the state object has been terminated.

Alternatively, the offload target can continue processing as normal until the host stack terminates the offload of the effected TCP connections.

 

 





