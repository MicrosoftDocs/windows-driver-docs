---
title: Supporting NDIS 6.0 Protocol Binding Pause and Restart Operations
description: Supporting NDIS 6.0 Protocol Binding Pause and Restart Operations
ms.assetid: ba328a35-49af-4398-adb1-30d855520be0
keywords:
- protocol drivers WDK networking , binding operations
- NDIS protocol drivers WDK , binding operations
- protocol bindings WDK networking
- binding operations WDK networking
- porting protocol drivers WDK networking , binding operations
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Supporting NDIS 6.0 Protocol Binding Pause and Restart Operations





NDIS 6.0 introduces driver stack pause and restart capabilities. A pause operation transitions a protocol binding to the *Paused* state. A restart operation transitions a protocol binding to the *Running* state. For an overview of binding states, see [Binding States of a Protocol Driver](binding-states-of-a-protocol-driver.md).

NDIS can pause the driver stack during Plug and Play operations, such as adding or removing a filter driver or binding or unbinding a protocol driver. To stop protocol driver data flow before performing a Plug and Play operation, NDIS calls a protocol driver's [*ProtocolNetPnPEvent*](https://msdn.microsoft.com/library/windows/hardware/ff570263) function and specifies a pause event. The protocol binding remains in the *Pausing* state until the pause operation has been completed.

NDIS calls the protocol driver's [*ProtocolNetPnPEvent*](https://msdn.microsoft.com/library/windows/hardware/ff570263) function and specifies a restart event to return the protocol binding to the *Running* state.

For more information about pause and restart operations, see [Driver Stack Management](driver-stack-management.md).

For more information about NDIS 6.0 protocol driver Plug and Play events, see [Porting Protocol Driver Plug and Play Event Notification Handling to NDIS 6.0](porting-protocol-driver-plug-and-play-event-notification-handling-to-n.md).

 

 





