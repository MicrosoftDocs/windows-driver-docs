---
title: Closing a CoNDIS Call Manager or MCM
description: Closing a CoNDIS Call Manager or MCM
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





When a stand-alone call manager is unbinding from an underlying miniport adapter, the call manager must notify all of the affected CoNDIS clients that they must close the associated AF. To notify each client, NDIS stand-alone call managers call the [**NdisCmNotifyCloseAddressFamily**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndiscmnotifycloseaddressfamily) function.

If a CoNDIS miniport adapter that an MCM manages is halting, the MCM must notify all of the affected clients that they must close the associated AF. To notify each client, the MCMs call the [**NdisMCmNotifyCloseAddressFamily**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismcmnotifycloseaddressfamily) function.

If a stand-alone call manager or MCM calls **NdisCmNotifyCloseAddressFamily** or **NdisMCmNotifyCloseAddressFamily**, respectively, NDIS calls the [**ProtocolClNotifyCloseAf**](/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_cl_notify_close_af) function of the CoNDIS client that is associated with the handle in the *NdisAfHandle* parameter of **NdisCmNotifyCloseAddressFamily** or **NdisMCmNotifyCloseAddressFamily**. This call notifies the client to close the AF. If **NdisCmNotifyCloseAddressFamily** or **NdisMCmNotifyCloseAddressFamily** returns NDIS\_STATUS\_PENDING, NDIS will call the call manager's [**ProtocolCmNotifyCloseAfComplete**](/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_cm_notify_close_af_complete) function when the close notification operation is complete.

For more information about closing an address family in a CoNDIS client, see [Closing an Address Family in a CoNDIS Client](closing-an-address-family-in-a-condis-client.md).

 

