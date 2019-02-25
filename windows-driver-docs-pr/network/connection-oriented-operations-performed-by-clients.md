---
title: Connection-Oriented Operations Performed by Clients
description: Connection-Oriented Operations Performed by Clients
ms.assetid: 342f534e-d203-4823-a4d8-a8a51b7ff0bd
keywords:
- connection-oriented clients WDK
- client operations WDK CoNDIS
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Connection-Oriented Operations Performed by Clients





A connection-oriented client:

-   **Opens and closes an address family.**

    On receiving notification from NDIS that a call manager or MCM driver has registered an address family, a connection-oriented driver can [open that address family](registering-and-opening-an-address-family.md) with the call manager or MCM driver. The client can then use the call manager services provided by the call manager or MCM driver. A client releases the association between itself and a call manager or MCM driver by [closing the address family](closing-an-address-family.md).

-   **Registers and deregisters SAPs.**

    After opening an address family with a call manager or an MCM driver, a connection-oriented client can [register one or more SAPs](registering-a-sap.md) with the call manager or MCM driver. The call manager or MCM driver will then indicate to the client any incoming calls addressed to the registered SAPs. A client releases an SAP by [deregistering the SAP](deregistering-a-sap.md).

-   **Adds and deletes PVCs.**

    A connection-oriented client can monitor when an operator manually configures or deconfigures a permanent VC (PVC). In response to such an action, the client can request a call manager or MCM driver to add a PVC to its list of configured PVCs or to delete a PVC from such a list (see [OID\_CO\_ADD\_PVC](https://msdn.microsoft.com/library/windows/hardware/ff569087) and [OID\_CO\_DELETE\_PVC](https://msdn.microsoft.com/library/windows/hardware/ff569090)).

-   **Makes outgoing calls.**

    Before making an outgoing call, a client must initiate the [creation of a VC](creating-a-vc.md) for the call. A client can then [make an outgoing call](making-a-call.md). To make a point-to-multipoint call, a client specifies a party when making the call.

-   **Adds a party to or drops a party from a point-to-multipoint call.**

    A client can [add a party to a point-to-multipoint call](adding-a-party-to-a-multipoint-call.md) and [delete a party from a point-to-multipoint call](dropping-a-party-from-a-multipoint-call.md). A client can also respond to an incoming [request to drop a party from a point-to-multipoint call](incoming-request-to-drop-a-party-from-a-multipoint-call.md).

-   **Accepts or rejects an incoming call.**

    A client can [accept or reject an incoming call](indicating-an-incoming-call.md) that is addressed to a SAP that the client previously registered with a call manager or MCM driver.

-   **Negotiates the call parameters for an active VC.**

    Depending on what is allowed by the signaling protocol, a client can negotiate the call parameters for an active VC. A client can [request a change in quality of service (QoS)](client-initiated-request-to-change-call-parameters.md) and respond to an incoming request to change the QoS for an active VC. A client can also respond to a [request from the remote party to change the QoS for a call](incoming-request-to-change-call-parameters.md).

-   **Sends and receives packets.**

    A client can send packets through a connection-oriented miniport driver or MCM driver. A client can also receive packets through a connection-oriented miniport driver or MCM driver.

-   **Initiates the deletion of a VC.**

    A client can initiate the [deletion of a VC](deleting-a-vc.md) that it created.

-   **Initiates the tear-down of a call.**

    A client can [initiate the tear-down of a outgoing call](client-initiated-request-to-close-a-call.md) that it made or an incoming call that it accepted.

-   **Queries or sets information.**

    A client can query or set information maintained by a bound call manager or the call manager portion of an MCM driver. A client can also respond to [queries and sets](querying-or-setting-information.md) from a bound call manager or MCM driver.

    In addition, a client can query or set information maintained by a bound miniport driver or the miniport driver portion of a bound MCM driver.

-   **Inputsminiport driver status indications.**

    A client can input [status indicated by a connection-oriented miniport driver](indicating-miniport-driver-status.md) or an MCM driver.

 

 





