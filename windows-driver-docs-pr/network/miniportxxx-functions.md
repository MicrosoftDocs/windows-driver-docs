---
title: MiniportXxx Functions
description: MiniportXxx Functions
keywords:
- MiniportXxx functions WDK networking
ms.date: 04/20/2017
---

# MiniportXxx Functions





The typical miniport driver uses a small number of functions to communicate through NDIS with the upper layers and hardware. Not all of these functions are required. For more information about which functions are optional, which are required, and why, see [Initializing a Miniport Driver](initializing-a-miniport-driver.md).

NDIS miniport drivers and upper-layer drivers use the NDIS Library (Ndis.sys) to communicate with each other through calls to **Ndis*Xxx*** functions.

Many miniport driver functions can operate either synchronously or asynchronously. The asynchronous functions have **Ndis*Xxx*Complete** functions that must be called when an operation is finished. For example, if a protocol driver calls [**NdisOidRequest**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisoidrequest) to query miniport driver information, the miniport driver's *MiniportOidRequest* function can pend the reset operation by returning NDIS\_STATUS\_PENDING. Eventually, the miniport driver must call [**NdisMOidRequestComplete**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismoidrequestcomplete) to indicate the final status of the query request.

 

