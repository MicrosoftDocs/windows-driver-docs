---
title: Closing a CoNDIS Call Manager or MCM
description: Closing a CoNDIS Call Manager or MCM
ms.assetid: 6ef64e4c-eec4-4477-a06c-f80e21d5b1c7
keywords:
- call managers WDK networking , CoNDIS
- MCMs WDK networking , closing
- miniport call managers WDK networking , closing
- closing call managers
- closing miniport call managers
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Closing a CoNDIS Call Manager or MCM





When a stand-alone call manager is unbinding from an underlying miniport adapter, the call manager must notify all of the affected CoNDIS clients that they must close the associated AF. To notify each client, NDIS stand-alone call managers call the [**NdisCmNotifyCloseAddressFamily**](https://msdn.microsoft.com/library/windows/hardware/ff561680) function.

If a CoNDIS miniport adapter that an MCM manages is halting, the MCM must notify all of the affected clients that they must close the associated AF. To notify each client, the MCMs call the [**NdisMCmNotifyCloseAddressFamily**](https://msdn.microsoft.com/library/windows/hardware/ff563546) function.

If a stand-alone call manager or MCM calls **NdisCmNotifyCloseAddressFamily** or **NdisMCmNotifyCloseAddressFamily**, respectively, NDIS calls the [**ProtocolClNotifyCloseAf**](https://msdn.microsoft.com/library/windows/hardware/ff570234) function of the CoNDIS client that is associated with the handle in the *NdisAfHandle* parameter of **NdisCmNotifyCloseAddressFamily** or **NdisMCmNotifyCloseAddressFamily**. This call notifies the client to close the AF. If **NdisCmNotifyCloseAddressFamily** or **NdisMCmNotifyCloseAddressFamily** returns NDIS\_STATUS\_PENDING, NDIS will call the call manager's [**ProtocolCmNotifyCloseAfComplete**](https://msdn.microsoft.com/library/windows/hardware/ff570248) function when the close notification operation is complete.

For more information about closing an address family in a CoNDIS client, see [Closing an Address Family in a CoNDIS Client](closing-an-address-family-in-a-condis-client.md).

 

 





