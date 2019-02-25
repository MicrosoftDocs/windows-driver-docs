---
title: Connection-Oriented Operations Performed by Miniport Drivers
description: Connection-Oriented Operations Performed by Miniport Drivers
ms.assetid: c49f93b2-6a51-45b6-8b02-93f3bef8dcde
keywords:
- miniport drivers WDK networking , CoNDIS
- connection-oriented NDIS WDK , miniport drivers
- CoNDIS WDK networking , miniport drivers
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Connection-Oriented Operations Performed by Miniport Drivers





In addition to controlling NIC hardware, a connection-oriented miniport driver:

-   **Sends and receives packets.**

    A connection-oriented miniport driver sends and receives packets on behalf of connection-oriented clients or call managers.

-   **Creates (sets up) VCs.**

    At the request of a connection-oriented client, a connection-oriented miniport driver [allocates and initializes the resources for a VC](creating-a-vc.md) for an outgoing call. At the request of a call manager, a connection-oriented miniport driver allocates and initializes the resources for a VC for an incoming call or on which the call manager will send or receive signaling messages.

-   **Activates VCs.**

    At the request of a call manager, a connection-oriented miniport driver communicates with a NIC to prepare the NIC to receive or transmit data across a VC (see [Activating a VC](activating-a-vc.md)).

-   **Deactivates VCs.**

    At the request of a call manager, a connection-oriented miniport driver communicates with a NIC to terminate all communication across a VC (see [Deactivating a VC](deactivating-a-vc.md)).

-   **Deletes VCs.**

    At the request of a connection-oriented client, a connection-oriented miniport driver deallocates the resources for a VC whose creation was initiated by that client (see [Deleting a VC](deleting-a-vc.md)). At the request of a call manager, a connection-oriented miniport driver deallocates the resources for a VC whose creation was initiated by that call manager.

-   **Responds to information queries or sets.**

    A connection-oriented miniport driver responds to [query and set operations](querying-or-setting-information.md) by a bound connection-oriented client or call manager.

-   **Indicates status.**

    A connection-oriented miniport driver can [indicate changes in its status or the status of a NIC](indicating-miniport-driver-status.md) to bound connection-oriented clients and call managers.

-   **Resets the NIC.**

    At the request of NDIS, a connection-oriented miniport driver [resets](reset.md) a NIC.

 

 





