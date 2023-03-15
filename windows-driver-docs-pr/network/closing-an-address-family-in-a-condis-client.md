---
title: Closing an Address Family in a CoNDIS Client
description: Closing an Address Family in a CoNDIS Client
keywords:
- client closed AFs WDK CoNDIS
ms.date: 03/02/2023
---

# Closing an Address Family in a CoNDIS Client





To close AFs, a CoNDIS client must provide a [**ProtocolClNotifyCloseAf**](/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_cl_notify_close_af) function. NDIS calls *ProtocolClNotifyCloseAf* when a stand-alone call manager or MCM calls the [**NdisCmNotifyCloseAddressFamily**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndiscmnotifycloseaddressfamily) function or the [**NdisMCmNotifyCloseAddressFamily**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismcmnotifycloseaddressfamily) function, respectively.

From within *ProtocolClNotifyCloseAf*, the client finishes closing the specified AF, or it returns NDIS\_STATUS\_PENDING and calls the [**NdisClNotifyCloseAddressFamilyComplete**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisclnotifycloseaddressfamilycomplete) function to complete the operation. After the client calls **NdisClNotifyCloseAddressFamilyComplete**, NDIS calls the [**ProtocolCmNotifyCloseAfComplete**](/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_cm_notify_close_af_complete) function to notify the call manager that the client closed the AF.

To close the AF, the client should:

1.  If the client has active multipoint connections, call the [**NdisClDropParty**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndiscldropparty) function as many times as necessary until only a single party remains active on each multipoint virtual connection (VC).

2.  Call the [**NdisClCloseCall**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisclclosecall) function as many times as necessary to close all of the calls that are still open and are associated with the address family.

3.  Call the [**NdisClDeregisterSap**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisclderegistersap) function as many times as necessary to deregister all of the service access points (SAPs) that the client registered with the call manager.

4.  Call the [**NdisClCloseAddressFamily**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisclcloseaddressfamily) function to close the AF.

 

