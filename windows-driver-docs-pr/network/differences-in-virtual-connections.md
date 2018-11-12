---
title: Differences in Virtual Connections
description: Differences in Virtual Connections
ms.assetid: 6e705f31-eec7-4b9c-a46f-ff7641d224c2
keywords:
- virtual connections WDK CoNDIS , MCM drivers vs. call managers
- signaling VCs WDK CoNDIS
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Differences in Virtual Connections





A call manager uses *signaling VCs* to send and receive signaling messages to and from network entities, such as switches. A call manager's signaling VCs are visible to NDIS. The call manager must create, activate, deactivate, and delete all VCs with calls to NDIS. An MCM driver's signaling VCs, however, are opaque to NDIS. An MCM driver does not create, activate, deactivate, and delete signaling VCs with calls to NDIS. Instead, an MCM driver performs such operations internally. An MCM driver must call NDIS to perform operations on VCs that are used to send or receive client data. This is because NDIS must keep track of client VCs.

Because MCM driver is both a call manager and a miniport driver, certain connection-oriented functions are redundant. Specifically, [**MiniportCoCreateVc**](https://msdn.microsoft.com/library/windows/hardware/ff559354) and [**MiniportCoDeleteVc**](https://msdn.microsoft.com/library/windows/hardware/ff559358) are redundant and are therefore not supplied by an MCM driver. VC operations are handled by:

-   An MCM driver's [**ProtocolCoCreateVc**](https://msdn.microsoft.com/library/windows/hardware/ff570252) and [**ProtocolCoDeleteVc**](https://msdn.microsoft.com/library/windows/hardware/ff570253) functions when a client requests the creation or deletion of a VC.

-   [**NdisMCmCreateVc**](https://msdn.microsoft.com/library/windows/hardware/ff562812) and [**NdisMCmDeleteVc**](https://msdn.microsoft.com/library/windows/hardware/ff562819) when the MCM driver creates or deletes a VC.

-   [**NdisMCmActivateVc**](https://msdn.microsoft.com/library/windows/hardware/ff562792) and [**NdisCmDeactivateVc**](https://msdn.microsoft.com/library/windows/hardware/ff561657) when the MCM driver activates or deactivates a VC.

An MCM driver must supply a [**MiniportCoOidRequest**](https://msdn.microsoft.com/library/windows/hardware/ff559362) function for a client to use in querying or setting miniport driver information, and a [**MiniportCoSendNetBufferLists**](https://msdn.microsoft.com/library/windows/hardware/ff559365) function to handle send operations from a client.

 

 





