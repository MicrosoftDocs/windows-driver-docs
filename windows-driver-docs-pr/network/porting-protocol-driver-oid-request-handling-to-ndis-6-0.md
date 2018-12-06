---
title: Porting Protocol Driver OID Request Handling to NDIS 6.0
description: Porting Protocol Driver OID Request Handling to NDIS 6.0
ms.assetid: fb99f2a9-df4e-436b-9607-f6ae777e1166
keywords:
- NDIS protocol drivers WDK , OID requests
- protocol drivers WDK networking , OID requests
- OID request porting WDK networking
- OIDs WDK networking , request operation porting
- object identifiers WDK networking
- porting protocol drivers WDK networkin
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Porting Protocol Driver OID Request Handling to NDIS 6.0





In NDIS 6.0, the [**NdisOidRequest**](https://msdn.microsoft.com/library/windows/hardware/ff563710) function replaces the NDIS 5.x [**NdisRequest**](https://msdn.microsoft.com/library/windows/hardware/ff554681) function. Also, the [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure replaces the [**NDIS\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff557179) structure.

A protocol driver's calls **NdisOidRequest** function to send an OID request to the underlying miniport adapter. As is the case with NDIS 5.*x* protocol drivers, NDIS serializes OID requests so it does not pass the request to the underlying driver until any pending request is completed.

NDIS 6.0 protocol drivers can call [**NdisCancelOidRequest**](https://msdn.microsoft.com/library/windows/hardware/ff561622) to cancel an OID request. In NDIS 6.0, calls to the [**NdisReset**](https://msdn.microsoft.com/library/windows/hardware/ff554691) function are not allowed. NDIS 6.0 protocol drivers cannot reset the underlying miniport driver.

If the [**NdisOidRequest**](https://msdn.microsoft.com/library/windows/hardware/ff563710) function returns NDIS\_STATUS\_PENDING, NDIS subsequently calls the [**ProtocolOidRequestComplete**](https://msdn.microsoft.com/library/windows/hardware/ff570264)(formerly [**ProtocolRequestComplete**](https://msdn.microsoft.com/library/windows/hardware/ff563254)) function to complete the request.

To improve system performance, NDIS 6.0 protocol drivers should avoid OID requests when possible. For example, during bind operations, much of the information that was formerly available only through OID requests is available in the [**NDIS\_BIND\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff564832) structure. To determine link status, use the status indications from underlying drivers instead of OID queries.

The [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure differs from [**NDIS\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff557179) in that it can specify a time-out and a request identifier.

For more information about OID requests in a protocol driver, see [Protocol Driver OID Requests](protocol-driver-oid-requests.md).

 

 





