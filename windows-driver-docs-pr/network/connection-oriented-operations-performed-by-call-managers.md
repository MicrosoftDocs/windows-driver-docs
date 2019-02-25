---
title: Connection-Oriented Operations Performed by Call Managers
description: Connection-Oriented Operations Performed by Call Managers
ms.assetid: 6df23eb2-df02-4d24-88b3-c02b87edb38b
keywords:
- connection-oriented NDIS WDK , call managers
- CoNDIS WDK networking , call managers
- call managers WDK networking , connection-oriented operations
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Connection-Oriented Operations Performed by Call Managers





A call manager performs:

-   **Registers and deregisters one or more address families (AFs).**

    A call manager [registers one or more address families](registering-and-opening-an-address-family.md) with NDIS . By registering an address family, a call manager advertises its call manager services (specifically, a signaling protocol) to bound connection-oriented clients. For information about registering entry points with NDIS, see [CoNDIS Registration](condis-registration.md).

-   **Registers and deregisters SAPs at the request of a connection-oriented client.**

    A call manager receives a bound connection-oriented client's requests to [register SAPs](registering-a-sap.md) and to [deregister SAPs](deregistering-a-sap.md). The call manager sends signaling messages over the network to register or deregister SAPs on behalf of clients.

-   **Sets up an outgoing call at the request of a connection-oriented client.**

    When a connection-oriented client [makes an outgoing call](making-a-call.md), the call manager communicates (exchanges signaling messages) with network control devices, as necessary, to make a connection. If the call is accepted by the remote party, the call manager [activates the VC](activating-a-vc.md) that is created for the call.

-   **Sets up and indicates an incoming call to a connection-oriented client.**

    A call manager indicates to a bound connection-oriented client all calls that are addressed to a SAP registered by that client. Before [indicating the incoming call](indicating-an-incoming-call.md) to the client, the call manager initiates [creation of a VC](creating-a-vc.md) for the call then initiates [activation of the VC](activating-a-vc.md).

-   **Communicates requests for a change in QoS.**

    Depending on the signaling protocol, the call manager can communicate a [request from the local client to change the QoS for an outgoing or incoming call](client-initiated-request-to-change-call-parameters.md) or a [request from the remote party to change the QoS for a call](incoming-request-to-change-call-parameters.md).

-   **Communicates requests to add and drop parties.**

    A call manager communicates a local client's request to [add a party](adding-a-party-to-a-multipoint-call.md) to or [drop a party](dropping-a-party-from-a-multipoint-call.md) from a point-to-multipoint call. A call manager also communicates a remote party's [incoming request to drop itself from a point-to-multipoint call](incoming-request-to-drop-a-party-from-a-multipoint-call.md).

-   **Tears down a call.**

    At the request of a connection-oriented client, a call manager closes a call by communicating with network control devices to [terminate a connection](client-initiated-request-to-close-a-call.md). At the request of a remote party, a call manager indicates to a local connection-oriented client a remote party's [request to close a call](incoming-request-to-close-a-call.md). In the process of tearing down a call, the call manager [deactivates the VC](deactivating-a-vc.md) that is used for the call. If the call manager created the VC (for an incoming call), the call manager can also [delete the VC](deleting-a-vc.md).

-   **Queries or sets information.**

    A call manager can [query or set information](querying-or-setting-information.md) maintained by a bound connection-oriented client. A call manager can also respond to query and set operations from a bound connection-oriented client.

    In addition, a call manager can query or set information maintained by a bound miniport driver or by the miniport driver portion of a bound MCM driver.

-   **Inputsminiport driver status indications.**

    A call manager inputs [status indications from a bound connection-oriented miniport driver](indicating-miniport-driver-status.md).

 

 





