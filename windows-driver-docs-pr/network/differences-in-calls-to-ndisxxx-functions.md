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





A call manager calls a different set of call manager functions than an MCM driver. A call manager calls **NdisCm*Xxx*** functions, and an MCM driver calls **NdisMCm*Xxx*** functions.

An MCM driver does not call the **NdisCo*Xxx*** functions that both connection-oriented clients and call managers call. Instead, an MCM driver calls the following comparable **NdisMCm*Xxx*** functions:

-   [**NdisMCmCreateVc**](https://msdn.microsoft.com/library/windows/hardware/ff562812) instead of [**NdisCoCreateVc**](https://msdn.microsoft.com/library/windows/hardware/ff561696)

-   [**NdisMCmDeleteVc**](https://msdn.microsoft.com/library/windows/hardware/ff562819) instead of [**NdisCoDeleteVc**](https://msdn.microsoft.com/library/windows/hardware/ff561698)

-   [**NdisMCmOidRequest**](https://msdn.microsoft.com/library/windows/hardware/ff563548) instead of [**NdisCoOidRequest**](https://msdn.microsoft.com/library/windows/hardware/ff561711)

-   [**NdisMCmOidRequestComplete**](https://msdn.microsoft.com/library/windows/hardware/ff563551) instead of [**NdisCoOidRequestComplete**](https://msdn.microsoft.com/library/windows/hardware/ff561716)

An MCM driver does not require a call that is comparable to [**NdisCoSendNetBufferLists**](https://msdn.microsoft.com/library/windows/hardware/ff561728), because the send interface between the call manager and the miniport driver is internal to an MCM driver and therefore opaque to NDIS.

 

 





