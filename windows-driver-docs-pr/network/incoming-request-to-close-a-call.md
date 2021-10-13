---
title: Incoming Request to Close a Call
description: Incoming Request to Close a Call
keywords:
- incoming close call requests WDK CoNDIS
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Incoming Request to Close a Call





When the remote client closes a call, the local call manager or MCM driver must indicate this incoming request to the local client. To indicate such a request, a call manager calls [**NdisCmDispatchIncomingCloseCall**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndiscmdispatchincomingclosecall) with the *CloseStatus* set to NDIS\_STATUS\_SUCCESS (see the following figure).

![diagram illustrating an incoming request through a call manager to close a call .](images/cm-22.png)

An MCM driver calls [**NdisMCmDispatchIncomingCloseCall**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismcmdispatchincomingclosecall) to indicate an incoming request to close a call (see the following figure).

![diagram illustrating an incoming request through an mcm driver to close a call .](images/fig1-22.png)

A call manager or MCM driver also can call **Ndis(M)CmDispatchIncomingCloseCall**:

-   From its [**ProtocolCmIncomingCallComplete**](/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_cm_incoming_call_complete) function if it determines that the connection-oriented client is requesting an unacceptable change in call parameters in response to an incoming call previously that is indicated by the call manager or MCM driver (see [Incoming Request to Change Call Parameters](incoming-request-to-change-call-parameters.md)).

-   If abnormal network conditions force the call manager to tear down active calls.

The call to **Ndis(M)CmDispatchIncomingCloseCall** causes NDIS to call the [**ProtocolClIncomingCloseCall**](/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_cl_incoming_close_call) function of the connection-oriented client on that connection. *ProtocolClIncomingCloseCall* should carry out any protocol-determined operations, such as notifying its own client or clients that the connection is being broken. If the call to be closed is a multipoint VC created by the client, *ProtocolClIncomingCloseCall* must call [**NdisClDropParty**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndiscldropparty) one or more times until only a single party remains on the VC (see [Dropping a Party from a Multipoint Call](dropping-a-party-from-a-multipoint-call.md)).

*ProtocolClIncomingCloseCall* must then call [**NdisClCloseCall**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisclclosecall)(with the handle to the last party on the VC if the VC is a multipoint VC created by the client) to acknowledge that the client will no longer attempt to send or expect to receive data on this particular VC. If the call manager or MCM driver created this VC, *ProtocolClIncomingCloseCall* should return control after it calls **NdisClCloseCall**. The call manager or MCM driver must also deactivate the VC (see [Deactivating a VC](deactivating-a-vc.md)).

If the client originally created this VC for an outgoing call and *CloseStatus* is NDIS\_STATUS\_SUCCESS, *ProtocolClIncomingCloseCall* can optionally tear down the VC with [**NdisCoDeleteVc**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndiscodeletevc)(see [Deleting a VC](deleting-a-vc.md)) or reuse the VC for another call. If *CloseStatus* is not NDIS\_STATUS\_SUCCESS, *ProtocolClIncomingCloseCall* must call **NdisCoDeleteVc**.

If the call manager or MCM driver originally created this VC for an incoming call, the call manager or MCM driver can optionally [delete the VC](deleting-a-vc.md) by respectively calling **NdisCoDeleteVc** or [**NdisMCmDeleteVc**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismcmdeletevc).

 

