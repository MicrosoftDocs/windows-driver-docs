---
title: Virtual Connection Context
description: Virtual Connection Context
ms.assetid: 9b318f9d-70f4-41b5-acab-5a193f7d2ab4
keywords:
- virtual connections WDK networking , context
- VCs WDK networking , context
- context WDK virtual connection
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Virtual Connection Context





Before making a call, a connection-oriented client requests a connection-oriented miniport driver to set up a virtual connection (VC) over which packets can be transmitted or received. Similarly, before indicating an incoming call to a connection-oriented client, a call manager or integrated miniport call manager (MCM) driver requests the miniport driver to set up a VC for the incoming call.

A VC is a logical connection between two connection-oriented entities. Connection-oriented transmissions and receptions always occur on a specific VC.

A connection-oriented miniport driver maintains state information in a miniport driver-allocated context area about each VC that it sets up. This per-VC context is maintained by the miniport driver and is opaque to NDIS and to protocol drivers. In its [**MiniportCoCreateVc**](https://msdn.microsoft.com/library/windows/hardware/ff559354) function, a connection-oriented miniport driver passes a handle to the VC context area to NDIS, and NDIS passes an *NdisVcHandle* that uniquely identifies the created VC back to the miniport driver, to the appropriate connection-oriented client, and to the call manager or integrated miniport call manager (MCM) driver.

Before data can be sent or received on a VC, the VC must be activated. The call manager initiates activation of the VC by calling **Ndis(M)CmActivateVc** and passing call parameters that include the characteristics of the VC to be activated. In response to this call, NDIS calls the miniport driver's [**MiniportCoActivateVc**](https://msdn.microsoft.com/library/windows/hardware/ff559351) function, which activates the VC.

After a call is complete or a VC is otherwise not needed, the call manager can deactivate the VC by calling [**Ndis(M)CmDeactivateVc**](https://msdn.microsoft.com/library/windows/hardware/ff561657), which causes NDIS to call the miniport driver's [**MiniportCoDeactivateVc**](https://msdn.microsoft.com/library/windows/hardware/ff559356) function. Either the connection-oriented client or the call manager can initiate the deletion of the VC by calling [**NdisCoDeleteVc**](https://msdn.microsoft.com/library/windows/hardware/ff561698), which causes NDIS to call the miniport driver's [**MiniportCoDeleteVc**](https://msdn.microsoft.com/library/windows/hardware/ff559358) function.

For more information about miniport driver operations on VCs, see [Operations on VCs](operations-on-vcs.md).

 

 





