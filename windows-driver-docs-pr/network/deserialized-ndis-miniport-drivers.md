---
title: Deserialized NDIS Miniport Drivers
description: Deserialized NDIS Miniport Drivers
ms.assetid: d133370a-48f4-425b-a2bd-d95ec8b5c369
keywords:
- miniport drivers WDK networking , types
- NDIS miniport drivers WDK , types
- deserialized NDIS miniport drivers WDK networking
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Deserialized NDIS Miniport Drivers





All NDIS 6.0 and later drivers are *deserialized*.

A *deserialized NDIS miniport driver* serializes the operation of its own *MiniportXxx* functions and queues internally all send requests rather than relying on NDIS to perform these functions. As a result, a deserialized miniport driver can achieve significantly better full-duplex performance than a serialized miniport driver.

The deserialized driver model is the default model for NDIS miniport drivers. Connection-oriented miniport drivers, as well as miniport drivers with a WDM lower edge, must be deserialized drivers. When writing a new NDIS miniport driver, you should write a deserialized driver. If possible, you should also port older drivers to NDIS 6.0 or later. For more information about porting drivers, see:

-   [Porting NDIS 5.x Drivers to NDIS 6.0](porting-ndis-5-x-drivers-to-ndis-6-0.md)
-   [Porting NDIS 6.x Drivers to NDIS 6.20](porting-ndis-6-x-drivers-to-ndis-6-20.md)
-   [Porting NDIS 6.x Drivers to NDIS 6.30](porting-ndis-6-x-drivers-to-ndis-6-30.md)

A deserialized miniport driver must meet the following requirements when it interfaces with NDIS:

-   A deserialized miniport driver must identify itself as such to NDIS during initialization.

-   A deserialized miniport driver must complete all send requests asynchronously. To complete a send request, connectionless NDIS 6.0 and later miniport drivers call the **NdisMSendNetBufferListsComplete** function. Connection-oriented NDIS 6.0 and later miniport drivers call the **NdisMCoSendNetBufferListsComplete** function.

-   A deserialized miniport driver that supports NDIS 6.0 or later sets the **Status** member of the NET\_BUFFER\_LIST structure that it will pass to **NdisMSendNetBufferListsComplete**.

-   If a deserialized miniport driver cannot immediately complete send requests, it cannot return the requests to NDIS for requeuing. Instead, the miniport driver must queue send requests internally until sufficient resources are available to transmit the data.

-   A deserialized miniport driver must not examine the structures that it passes to NDIS in receive indications until after NDIS returns them. NDIS returns NET\_BUFFER\_LIST structures to a miniport driver's *MiniportReturnNetBufferLists* function.

A deserialized miniport driver must meet the following driver-internal requirements:

-   A deserialized miniport driver must protect its network buffer queues with [spin locks](https://msdn.microsoft.com/library/windows/hardware/ff548114). A deserialized miniport driver must also protect its shared state from simultaneous access by its own *MiniportXxx* functions.

-   A deserialized miniport driver's *MiniportXxx* functions can run at IRQL &lt;= DISPATCH\_LEVEL. Consequently, the driver writer cannot assume that *MiniportXxx* functions will be called in the sequence in which they process requests. One *MiniportXxx* function can preempt another *MiniportXxx* function that is running at a lower IRQL.

-   A deserialized miniport driver is responsible for network buffer-queue management. When the miniport driver experiences a resource problem, it cannot return send requests to NDIS for requeuing. Instead, the miniport driver must queue internally all send requests until sufficient resources are available to send the data.

-   A deserialized miniport driver should complete send requests in the protocol-determined order.

For more information about send and receive requirements for NDIS drivers, see [Send and Receive Operations](send-and-receive-operations.md).

Note that a deserialized miniport driver usually completes send requests in protocol-determined order. However, a miniport driver that supports packet priority (for example, IEEE 802.1p) can reorder send requests based on priority information.

 

 





