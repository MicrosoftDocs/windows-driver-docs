---
title: Occasions for Setting Miniport Driver Information
description: Occasions for Setting Miniport Driver Information
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Occasions for Setting Miniport Driver Information





The [*MiniportOidRequest*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_oid_request) function in a connectionless miniport driver and the [**MiniportCoOidRequest**](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_co_oid_request) function in a connection-oriented miniport driver are called during initialization. These functions can also be called:

-   During a hardware reset,

-   If a protocol calls [**NdisCloseAdapterEx**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndiscloseadapterex).

*MiniportOidRequest* or *MiniportCoOidRequest* is called during [hardware reset operation](hardware-reset.md). In this case, *MiniportOidRequest* or *MiniportCoOidRequest* is called to reset the miniport driver to its initial state with respect to its addresses.

NDIS calls *MiniportOidRequest* or *MiniportCoOidRequest* when a miniport driver's NIC is closed by a protocol's [**NdisCloseAdapterEx**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndiscloseadapterex) call. Such a miniport driver will be requested to update its addressing information.

 

