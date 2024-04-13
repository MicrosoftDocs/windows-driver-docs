---
title: Incoming Request to Drop a Party from a Multipoint Call
description: Incoming Request to Drop a Party from a Multipoint Call
keywords:
- parties WDK CoNDIS
- multipoint calls WDK CoNDIS
- dropping party from multipoint calls
- removing party from multipoint calls
- incoming drop party requests WDK CoNDIS
ms.date: 04/20/2017
---

# Incoming Request to Drop a Party from a Multipoint Call





A call manager or MCM driver is alerted to an incoming request from a remote party to drop that party from a multipoint call by signaling messages from the network. A call manager or MCM driver can also signal an incoming request to drop a party if it detects network problems that prevent further data transfers on the VC.

If the party that is being dropped from the call is not the last party on the VC, a call manager calls [**NdisCmDispatchIncomingDropParty**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndiscmdispatchincomingdropparty). An MCM driver calls [**NdisMCmDispatchIncomingDropParty**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismcmdispatchincomingdropparty). If the party that is being dropped is the last party on the VC, a call manager calls [**NdisCmDispatchIncomingCloseCall**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndiscmdispatchincomingclosecall), and an MCM driver calls [**NdisMCmDispatchIncomingCloseCall**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismcmdispatchincomingclosecall)(see [Incoming Request to Close a Call](incoming-request-to-close-a-call.md)).

A call to **Ndis(M)CmDispatchIncomingDropParty** causes NDIS to call the client's [**ProtocolClIncomingDropParty**](/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_cl_incoming_drop_party) function.

The following shows an incoming request through a call manager to drop a party through a multipoint call.

:::image type="content" source="images/cm-19.png" alt-text="Diagram illustrating an incoming request to drop a party through a multipoint call via a call manager.":::

The next figure shows an incoming request through an MCM driver to drop a party through a multipoint call.

:::image type="content" source="images/fig1-19.png" alt-text="Diagram illustrating an incoming request to drop a party through a multipoint call via an MCM driver.":::

*ProtocolClIncomingDropParty* should carry out any protocol-determined operations for dropping the party from the client's multipoint VC. If the party that is being dropped is not the last party on the VC, *ProtocolClIncomingDropParty* must call **NdisClDropParty**(see [Dropping a Party from a Multipoint Call](dropping-a-party-from-a-multipoint-call.md)). If the party being dropped is the last party on the VC, *ProtocolClIncomingDropParty* must call **NdisClCloseCall**(see [Client-Initiated Request to Close a Call](client-initiated-request-to-close-a-call.md)).

 

