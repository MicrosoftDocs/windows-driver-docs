---
title: Differences in Virtual Connections
description: Differences in Virtual Connections
keywords:
- virtual connections WDK CoNDIS , MCM drivers vs. call managers
- signaling VCs WDK CoNDIS
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Differences in Virtual Connections





A call manager uses *signaling VCs* to send and receive signaling messages to and from network entities, such as switches. A call manager's signaling VCs are visible to NDIS. The call manager must create, activate, deactivate, and delete all VCs with calls to NDIS. An MCM driver's signaling VCs, however, are opaque to NDIS. An MCM driver does not create, activate, deactivate, and delete signaling VCs with calls to NDIS. Instead, an MCM driver performs such operations internally. An MCM driver must call NDIS to perform operations on VCs that are used to send or receive client data. This is because NDIS must keep track of client VCs.

Because MCM driver is both a call manager and a miniport driver, certain connection-oriented functions are redundant. Specifically, [**MiniportCoCreateVc**](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_co_create_vc) and [**MiniportCoDeleteVc**](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_co_delete_vc) are redundant and are therefore not supplied by an MCM driver. VC operations are handled by:

-   An MCM driver's [**ProtocolCoCreateVc**](/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_co_create_vc) and [**ProtocolCoDeleteVc**](/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_co_delete_vc) functions when a client requests the creation or deletion of a VC.

-   [**NdisMCmCreateVc**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismcmcreatevc) and [**NdisMCmDeleteVc**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismcmdeletevc) when the MCM driver creates or deletes a VC.

-   [**NdisMCmActivateVc**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismcmactivatevc) and [**NdisCmDeactivateVc**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndiscmdeactivatevc) when the MCM driver activates or deactivates a VC.

An MCM driver must supply a [**MiniportCoOidRequest**](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_co_oid_request) function for a client to use in querying or setting miniport driver information, and a [**MiniportCoSendNetBufferLists**](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_co_send_net_buffer_lists) function to handle send operations from a client.

 

