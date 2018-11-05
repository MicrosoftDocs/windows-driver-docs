---
title: Porting Address Family Close Operations to CoNDIS 6.0
description: Porting Address Family Close Operations to CoNDIS 6.0
ms.assetid: bafba536-2da0-45b0-ad5c-737635fabe3a
keywords:
- address families WDK networking
- call managers WDK networking , address families
- CoNDIS call managers WDK networking
- porting CoNDIS drivers WDK networking , address families
- closing address families
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Porting Address Family Close Operations to CoNDIS 6.0





In CoNDIS 5.*x*, before a call manager closes a binding to an underlying miniport adapter, it issues an [OID\_CO\_AF\_CLOSE](https://msdn.microsoft.com/library/windows/hardware/ff569088) request to each CoNDIS client that has the associated address family (AF). When the clients receive the OID request, the clients close the address family.

CoNDIS 6.0 drivers do not use the OID\_CO\_AF\_CLOSE OID request. In NDIS 6.0, a call manager calls the [**NdisCmNotifyCloseAddressFamily**](https://msdn.microsoft.com/library/windows/hardware/ff561680) function or, if it is a miniport call manager (MCM), the [**NdisMCmNotifyCloseAddressFamily**](https://msdn.microsoft.com/library/windows/hardware/ff563546) function to request that each client close the AF.

CoNDIS 6.0 clients must register a [**ProtocolClNotifyCloseAf**](https://msdn.microsoft.com/library/windows/hardware/ff570234) function. If a call manager or MCM calls **NdisCmNotifyCloseAddressFamily** or **NdisMCmNotifyCloseAddressFamily**, NDIS calls the *ProtocolClNotifyCloseAf* function of any client that is associated with the specified AF. A client can close the AF from within the call to *ProtocolClNotifyCloseAf* or it can return NDIS\_STATUS\_PENDING and call the [**NdisClNotifyCloseAddressFamilyComplete**](https://msdn.microsoft.com/library/windows/hardware/ff561638) function to complete the operation. If the client completes the operation by calling **NdisClNotifyCloseAddressFamilyComplete**, NDIS calls the call manager's [**ProtocolCmNotifyCloseAfComplete**](https://msdn.microsoft.com/library/windows/hardware/ff570248) function to complete the operation.

For more information about closing an address family in a call manager or MCM, see [Closing a CoNDIS 6.0 Call Manager or MCM](closing-a-condis-call-manager-or-mcm.md). For more information about closing an address family in a client, see [Closing an Address Family in a CoNDIS 6.0 Client](closing-an-address-family-in-a-condis-client.md).

 

 





