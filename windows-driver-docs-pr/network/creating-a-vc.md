---
title: Creating a VC
description: Creating a VC
keywords:
- virtual connections WDK CoNDIS , creating
ms.date: 04/20/2017
---

# Creating a VC





Before making an outgoing call, a connection-oriented client initiates the creation a virtual connection (VC). Before indicating an incoming call to a connection-oriented client, a call manager or an MCM driver initiates the creation of a VC . After the VC has been set up and activated, client data can be transmitted or received on the VC.

A call manager or an MCM driver can also initiate the creation of a VC on which signaling messages are exchanged with network components, such as a network switch.

### Client-Initiated Creation of a VC

Before [making a call](making-a-call.md) with [**NdisClMakeCall**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisclmakecall), a connection-oriented client calls [**NdisCoCreateVc**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndiscocreatevc) to initiate the creation of a VC.

The following figure shows a client of a call manager initiating the creation of a VC.

:::image type="content" source="images/cm-05.png" alt-text="Diagram showing a client of a call manager initiating the creation of a VC.":::

The following figure shows a client of an MCM driver initiating the creation of a VC.

:::image type="content" source="images/fig1-05.png" alt-text="Diagram showing a client of an MCM driver initiating the creation of a VC.":::

When a connection-oriented client of a call manager calls **NdisCoCreateVc**, NDIS calls, as a synchronous operation, the [**ProtocolCoCreateVc**](/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_co_create_vc) function of the call manager and the [**MiniportCoCreateVc**](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_co_create_vc) function of the underlying miniport driver (see the first figure in this topic). NDIS passes an *NdisVcHandle* that represents the VC to both *ProtocolCoCreateVc* and *MiniportCoCreateVc*. If the call to **NdisCoCreateVc** is successful, NDIS returns the *NdisVcHandle* to **NdisCoCreateVc**.

*ProtocolCoCreateVc* allocates and initializes any dynamic resources and structures that the call manager requires to perform subsequent operations on a VC that will be activated. *MiniportCoCreateVc* allocates and initializes any resources that the miniport driver requires to maintain state information about the VC. Both *ProtocolCoCreateVc* and *MiniportCoCreateVc* store the *NdisVcHandle* .

When a connection-oriented client of an MCM driver, the call to **NdisCoCreateVc** causes NDIS to call the MCM driver's *ProtocolCoCreateVc* function (see Client-Initiated Creation of a VC (MCM Driver Present)). In this case, *ProtocolCoCreateVc* performs the necessary allocation and initialization of resources for the VC. There is no call (internal or otherwise) to *MiniportCoCreateVc*, because an MCM driver does not supply such a function.

### Call Manager-Initiated Creation of a VC

Before [indicating an incoming call](indicating-an-incoming-call.md) to a connection-oriented client with [**NdisCmDispatchIncomingCall**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndiscmdispatchincomingcall), a call manager calls **NdisCoCreateVc** to initiate the creation of a VC (see the following figure).

:::image type="content" source="images/cm-06.png" alt-text="Diagram showing a call manager initiating the creation of a VC.":::

When a call manager calls [**NdisCoCreateVc**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndiscocreatevc), NDIS calls, as a synchronous operation, the [**ProtocolCoCreateVc**](/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_co_create_vc) function of the connection-oriented client that registered the SAP on which the call is being received, as well as the [**MiniportCoCreateVc**](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_co_create_vc) function of the underlying miniport. NDIS passes an *NdisVcHandle* that represents the VC to both *ProtocolCoCreateVc* and *MiniportCoCreateVc*. If the call to **NdisCoCreateVc** is successful, NDIS returns the *NdisVcHandle* to **NdisCoCreateVc**.

### MCM Driver-Initiated Creation of a VC

Before [indicating an incoming call](indicating-an-incoming-call.md) to a connection-oriented client with [**NdisMCmDispatchIncomingCall**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismcmdispatchincomingcall), an MCM driver calls [**NdisMCmCreateVc**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismcmcreatevc) to initiate the creation of a VC (see the following figure).

:::image type="content" source="images/fig1-06.png" alt-text="Diagram showing an MCM driver initiating the creation of a VC.":::

When an MCM driver calls **NdisMCmCreateVc**, NDIS calls, as a synchronous operation before **NdisMCmCreateVc** returns, the [**ProtocolCoCreateVc**](/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_co_create_vc) function of the connection-oriented client that registered the SAP on which the call is being received. NDIS passes an *NdisVcHandle* that represents the VC to *ProtocolCoCreateVc*. If the call to **NdisMCmCreateVc** is successful, NDIS returns the *NdisVcHandle* to **NdisMCmCreateVc**.

*ProtocolCoCreateVc* allocates and initializes any dynamic resources and structures that the client requires to perform subsequent operations on the VC. *ProtocolCoCreateVc* also stores the *NdisVcHandle* .

Note that when an MCM driver creates a VC for exchanging signaling messages with a network component, it does not use **Ndis*Xxx*** calls to create a VC. In fact, an MCM driver does not use **Ndis*Xxx*** calls to create, activate, deactivate, or delete such VCs. Instead, an MCM driver performs these operations internally. Such VCs are therefore opaque to NDIS.

 

