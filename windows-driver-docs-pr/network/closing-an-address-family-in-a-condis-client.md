---
title: Closing an Address Family in a CoNDIS Client
description: Closing an Address Family in a CoNDIS Client
ms.assetid: 06e8128a-f3da-48f2-a045-6c4be5f85889
keywords:
- client closed AFs WDK CoNDIS
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Closing an Address Family in a CoNDIS Client





To close AFs, a CoNDIS client must provide a [**ProtocolClNotifyCloseAf**](https://msdn.microsoft.com/library/windows/hardware/ff570234) function. NDIS calls *ProtocolClNotifyCloseAf* when a stand-alone call manager or MCM calls the [**NdisCmNotifyCloseAddressFamily**](https://msdn.microsoft.com/library/windows/hardware/ff561680) function or the [**NdisMCmNotifyCloseAddressFamily**](https://msdn.microsoft.com/library/windows/hardware/ff563546) function, respectively.

From within *ProtocolClNotifyCloseAf*, the client finishes closing the specified AF, or it returns NDIS\_STATUS\_PENDING and calls the [**NdisClNotifyCloseAddressFamilyComplete**](https://msdn.microsoft.com/library/windows/hardware/ff561638) function to complete the operation. After the client calls **NdisClNotifyCloseAddressFamilyComplete**, NDIS calls the [**ProtocolCmNotifyCloseAfComplete**](https://msdn.microsoft.com/library/windows/hardware/ff570248) function to notify the call manager that the client closed the AF.

To close the AF, the client should:

1.  If the client has active multipoint connections, call the [**NdisClDropParty**](https://msdn.microsoft.com/library/windows/hardware/ff561629) function as many times as necessary until only a single party remains active on each multipoint virtual connection (VC).

2.  Call the [**NdisClCloseCall**](https://msdn.microsoft.com/library/windows/hardware/ff561627) function as many times as necessary to close all of the calls that are still open and are associated with the address family.

3.  Call the [**NdisClDeregisterSap**](https://msdn.microsoft.com/library/windows/hardware/ff561628) function as many times as necessary to deregister all of the service access points (SAPs) that the client registered with the call manager.

4.  Call the [**NdisClCloseAddressFamily**](https://msdn.microsoft.com/library/windows/hardware/ff561626) function to close the AF.

 

 





