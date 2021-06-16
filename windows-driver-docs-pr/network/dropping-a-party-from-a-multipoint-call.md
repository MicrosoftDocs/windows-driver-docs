---
title: Dropping a Party from a Multipoint Call
description: Dropping a Party from a Multipoint Call
keywords:
- parties WDK CoNDIS
- multipoint calls WDK CoNDIS
- dropping party from multipoint calls
- removing party from multipoint calls
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Dropping a Party from a Multipoint Call





A connection-oriented client that serves as the root of a multipoint call must eventually drop each party from that call with [**NdisClDropParty**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndiscldropparty) or [**NdisClCloseCall**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisclclosecall).

A client drops a party from a call in the following situations:

-   Before initiating the tear down of a multipoint call with **NdisClCloseCall**(see [Client-Initiated Request to Close a Call](client-initiated-request-to-close-a-call.md)), a client must drop all but the last party with successive calls to **NdisClDropParty**. The client specifies the last party to drop from the call with **NdisClCloseCall**.

-   In response to a remote party's request to be dropped from a multipoint call (see [Incoming Request to Drop a Party from a Multipoint Call](incoming-request-to-drop-a-party-from-a-multipoint-call.md)), a client, from its [**ProtocolClIncomingDropParty**](/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_cl_incoming_drop_party) function, calls **NdisClDropParty**.

A client's call to **NdisClDropParty** causes NDIS to call the [**ProtocolCmDropParty**](/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_cm_drop_party) function of the call manager or MCM driver that shares the same *NdisVcHandle* to the multipoint VC.

The following figure shows the client of a call manager requesting to drop a party from a multipoint call.

![diagram illustrating the client of a call manager requesting to drop a party from a multipoint call.](images/cm-18.png)

The next figure shows the client of an MCM driver requesting to drop a party from a multipoint call.

![diagram illustrating the client of an mcm driver requesting to drop a party from a multipoint call.](images/fig1-18.png)

*ProtocolCmDropParty* communicates with network control devices to drop a party from an existing multipoint call. NDIS can pass to *ProtocolCmDropParty* a pointer to a buffer that contains data (supplied to the client in the call to **NdisClDropParty**). *ProtocolCmDropParty* must send any such data across the network before the connection is dropped.

*ProtocolCmDropParty* can complete synchronously, or more probably, asynchronously with [**NdisCmDropPartyComplete**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndiscmdroppartycomplete), in the case of a call manager, or [**NdisMCmDropPartyComplete**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismcmdroppartycomplete), in the case of an MCM driver.

The call to **Ndis(M)CmDropPartyComplete** causes NDIS to call the client's [**ProtocolClDropPartyComplete**](/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_cl_drop_party_complete) function. If the client is in the process of tearing down a multipoint VC that it created, *ProtocolClDropPartyComplete* can call **NdisClDropParty** with any valid *NdisPartyHandle* to one of the remaining parties on the client's active multipoint VC. If only one party remains on its multipoint VC, the client should drop that party by passing its *NdisPartyHandle* to **NdisClCloseCall**(see [Client-Initiated Request to Close a Call](client-initiated-request-to-close-a-call.md)).

 

