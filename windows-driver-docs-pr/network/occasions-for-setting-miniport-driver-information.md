---
title: Occasions for Setting Miniport Driver Information
description: Occasions for Setting Miniport Driver Information
ms.assetid: 46834d76-e1b9-440c-af18-a4b564d1a76e
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Occasions for Setting Miniport Driver Information





The [*MiniportOidRequest*](https://msdn.microsoft.com/library/windows/hardware/ff559416) function in a connectionless miniport driver and the [**MiniportCoOidRequest**](https://msdn.microsoft.com/library/windows/hardware/ff559362) function in a connection-oriented miniport driver are called during initialization. These functions can also be called:

-   During a hardware reset,

-   If a protocol calls [**NdisCloseAdapterEx**](https://msdn.microsoft.com/library/windows/hardware/ff561640).

*MiniportOidRequest* or *MiniportCoOidRequest* is called during [hardware reset operation](hardware-reset.md). In this case, *MiniportOidRequest* or *MiniportCoOidRequest* is called to reset the miniport driver to its initial state with respect to its addresses.

NDIS calls *MiniportOidRequest* or *MiniportCoOidRequest* when a miniport driver's NIC is closed by a protocol's [**NdisCloseAdapterEx**](https://msdn.microsoft.com/library/windows/hardware/ff561640) call. Such a miniport driver will be requested to update its addressing information.

 

 





