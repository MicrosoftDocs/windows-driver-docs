---
title: Differences in Calls to NdisXxx Functions
description: Differences in Calls to NdisXxx Functions
keywords:
- NdisCmXxx functions WDK networking
ms.date: 04/20/2017
---

# Differences in Calls to NdisXxx Functions





A call manager calls a different set of call manager functions than an MCM driver. A call manager calls **NdisCm_Xxx_** functions, and an MCM driver calls **NdisMCm_Xxx_** functions.

An MCM driver does not call the **NdisCo_Xxx_** functions that both connection-oriented clients and call managers call. Instead, an MCM driver calls the following comparable **NdisMCm_Xxx_** functions:

-   [**NdisMCmCreateVc**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismcmcreatevc) instead of [**NdisCoCreateVc**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndiscocreatevc)

-   [**NdisMCmDeleteVc**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismcmdeletevc) instead of [**NdisCoDeleteVc**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndiscodeletevc)

-   [**NdisMCmOidRequest**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismcmoidrequest) instead of [**NdisCoOidRequest**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndiscooidrequest)

-   [**NdisMCmOidRequestComplete**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismcmoidrequestcomplete) instead of [**NdisCoOidRequestComplete**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndiscooidrequestcomplete)

An MCM driver does not require a call that is comparable to [**NdisCoSendNetBufferLists**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndiscosendnetbufferlists), because the send interface between the call manager and the miniport driver is internal to an MCM driver and therefore opaque to NDIS.

 

