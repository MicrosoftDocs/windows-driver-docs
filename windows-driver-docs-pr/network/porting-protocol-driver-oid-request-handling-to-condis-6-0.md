---
title: Porting Protocol Driver OID Request Handling to CoNDIS 6.0
description: Porting Protocol Driver OID Request Handling to CoNDIS 6.0
ms.assetid: d5f0b700-775d-4eb5-ac7a-01385be71a0d
keywords:
- porting OID requests WDK networking
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Porting Protocol Driver OID Request Handling to CoNDIS 6.0





In NDIS 6.0, the [**NdisCoOidRequest**](https://msdn.microsoft.com/library/windows/hardware/ff561711) function replaces the NDIS 5.x [**NdisCoRequest**](https://msdn.microsoft.com/library/windows/hardware/ff551877) function, and the [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure replaces the [**NDIS\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff557179) structure.

To send an OID request to an underlying driver, a call manager or client calls [**NdisCoOidRequest**](https://msdn.microsoft.com/library/windows/hardware/ff561711) and specifies a **NULL** address family. If **NdisCoOidRequest** returns NDIS\_STATUS\_PENDING, NDIS subsequently calls the [**ProtocolCoOidRequestComplete**](https://msdn.microsoft.com/library/windows/hardware/ff570255)(formerly [**ProtocolCoRequestComplete**](https://msdn.microsoft.com/library/windows/hardware/ff563227)) function to complete the request.

To send an OID request to another protocol driver in NDIS 6.0, a call manager or client specifies a valid address family when it calls [**NdisCoOidRequest**](https://msdn.microsoft.com/library/windows/hardware/ff561711). In this case, NDIS calls the other protocol driver's [**ProtocolCoOidRequest**](https://msdn.microsoft.com/library/windows/hardware/ff570254) function (formerly [**ProtocolCoRequest**](https://msdn.microsoft.com/library/windows/hardware/ff563225)). If *ProtocolCoOidRequest* returns NDIS\_STATUS\_PENDING, the protocol driver that received the request must later call the [**NdisCoOidRequestComplete**](https://msdn.microsoft.com/library/windows/hardware/ff561716) function (formerly [**NdisCoRequestComplete**](https://msdn.microsoft.com/library/windows/hardware/ff551884)) to complete the operation. NDIS subsequently calls the [**ProtocolCoOidRequestComplete**](https://msdn.microsoft.com/library/windows/hardware/ff570255)(formerly [**ProtocolCoRequestComplete**](https://msdn.microsoft.com/library/windows/hardware/ff563227)) function to complete the request.

NDIS 6.0 protocol drivers can call [**NdisCancelOidRequest**](https://msdn.microsoft.com/library/windows/hardware/ff561622) to cancel an OID request to a miniport driver. Protocol drivers cannot cancel requests that they send to other protocol drivers. In NDIS 6.0, drivers should not call the [**NdisReset**](https://msdn.microsoft.com/library/windows/hardware/ff554691) function, and NDIS 6.0 protocol drivers cannot reset the underlying miniport driver.

To improve computer performance, NDIS 6.0 protocol drivers should avoid OID requests when possible. For example, during bind operations, much of the information that was formerly available only through OID requests is available in the [**NDIS\_BIND\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff564832) structure. To determine link status, use the status indications from underlying drivers instead of OID queries.

The [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure differs from [**NDIS\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff557179) in that NDIS\_OID\_REQUEST can specify a time-out and a request identifier.

For more information about OID requests in a protocol driver, see [CoNDIS Protocol Driver OID Requests](condis-protocol-driver-oid-requests.md).

 

 





