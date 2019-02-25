---
title: NDIS Selective Suspend Idle Notifications
description: NDIS Selective Suspend Idle Notifications
ms.assetid: 958A2588-A847-4699-9906-95FB47CA1CDC
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# NDIS Selective Suspend Idle Notifications


When the miniport driver has enabled and registered support for NDIS selective suspend, NDIS monitors the I/O activity of the underlying network adapter. If NDIS determines that the driver and adapter are idle, NDIS performs a selective suspend operation. This operation suspends the network adapter by transitioning the adapter to a low-power state.

NDIS starts the selective suspend operation by issuing an idle notification to the miniport driver. When the network adapter is suspended in a low-power state, the adapter can resume to a full-power state only when the idle notification is canceled. After the notification is canceled and the adapter is in a full-power state, the selective suspend operation is complete.

The following topics provide more information on the NDIS selective suspend operation and idle notifications:

[How NDIS Detects Idle Network Adapters](how-ndis-detects-idle-network-adapters.md)

[Handling the NDIS Selective Suspend Idle Notification](handling-the-ndis-selective-suspend-idle-notification.md)

[Canceling the NDIS Selective Suspend Idle Notification](canceling-the-ndis-selective-suspend-idle-notification.md)

[Completing the NDIS Selective Suspend Idle Notification](completing-the-ndis-selective-suspend-idle-notification.md)

 

 





