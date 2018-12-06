---
title: CoNDIS Miniport Driver OID Requests
description: CoNDIS Miniport Driver OID Requests
ms.assetid: a283d430-f90c-4704-868b-f4086922737b
keywords:
- miniport drivers WDK networking , CoNDIS
- NDIS miniport drivers WDK , CoNDIS
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# CoNDIS Miniport Driver OID Requests





NDIS calls a CoNDIS miniport driver's [**MiniportCoOidRequest**](https://msdn.microsoft.com/library/windows/hardware/ff559362) function to submit an OID request to query or set information in the driver. NDIS calls *MiniportCoOidRequest* either on its own behalf or on behalf of an overlying driver that called the [**NdisCoOidRequest**](https://msdn.microsoft.com/library/windows/hardware/ff561711) function.

NDIS passes *MiniportCoOidRequest* a pointer to an [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure that contains the request information. The request structure contains an OID\_*Xxx* identifier that indicates the type of request and other members to define the request data.

The **Timeout** member specifies a time-out, in seconds, for the request. NDIS can reset the driver or cancel the request if the time-out expires before the driver completes the request.

The **RequestId** member specifies an optional identifier for the request. Miniport drivers can set the **RequestId** member of a status indication to the value that the driver obtained from the **RequestId** member of an associated OID request. Typically, miniport drivers can ignore this member. If a driver must set this member, the driver must use one of the required values, which are specified in the reference page for the particular OID. For more information about status indications, see [CoNDIS Miniport Driver Status Indications](condis-miniport-driver-status-indications.md).

A miniport driver can complete an OID request synchronously by returning a success or failure status. The driver can complete an OID request asynchronously by returning NDIS\_STATUS\_PENDING. In this case, the driver must call the [**NdisMCoOidRequestComplete**](https://msdn.microsoft.com/library/windows/hardware/ff563568) function to complete the operation.

If the *MiniportCoOidRequest* function returns NDIS\_STATUS\_PENDING, NDIS can call *MiniportCoOidRequest* with another request for the adapter before the pending request is completed. You should note that this is different from the connectionless NDIS interface where all OID requests are serialized.

NDIS can call a miniport driver's [*MiniportCancelOidRequest*](https://msdn.microsoft.com/library/windows/hardware/ff559339) function to cancel a CoNDIS OID request.

 

 





