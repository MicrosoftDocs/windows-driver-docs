---
title: Differences in Calls to NdisXxx Functions
description: Differences in Calls to NdisXxx Functions
ms.assetid: 967ad913-24ca-4f05-b10b-1daa88845ed3
keywords:
- NdisCmXxx functions WDK networking
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Differences in Calls to NdisXxx Functions





A call manager calls a different set of call manager functions than an MCM driver. A call manager calls **NdisCm_Xxx_** functions, and an MCM driver calls **NdisMCm_Xxx_** functions.

An MCM driver does not call the **NdisCo_Xxx_** functions that both connection-oriented clients and call managers call. Instead, an MCM driver calls the following comparable **NdisMCm_Xxx_** functions:

-   [**NdisMCmCreateVc**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismcmcreatevc) instead of [**NdisCoCreateVc**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/nf-ndis-ndiscocreatevc)

-   [**NdisMCmDeleteVc**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismcmdeletevc) instead of [**NdisCoDeleteVc**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/nf-ndis-ndiscodeletevc)

-   [**NdisMCmOidRequest**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismcmoidrequest) instead of [**NdisCoOidRequest**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/nf-ndis-ndiscooidrequest)

-   [**NdisMCmOidRequestComplete**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismcmoidrequestcomplete) instead of [**NdisCoOidRequestComplete**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/nf-ndis-ndiscooidrequestcomplete)

An MCM driver does not require a call that is comparable to [**NdisCoSendNetBufferLists**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/nf-ndis-ndiscosendnetbufferlists), because the send interface between the call manager and the miniport driver is internal to an MCM driver and therefore opaque to NDIS.

 

 





