---
title: Porting MCM OID Request Handling to CoNDIS 6.0
description: Porting MCM OID Request Handling to CoNDIS 6.0
ms.assetid: 2d2ff7c8-9ae0-4d99-b4aa-38ccec21f534
keywords:
- miniport call managers WDK networking , OID requests
- MCMs WDK networking , OID requests
- porting OID requests WDK networking
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Porting MCM OID Request Handling to CoNDIS 6.0





Miniport call managers (MCMs) must service OID requests that are associated with miniport parameters and also OID requests that are associated with call manager parameters. This topic describes porting MCM OID request handling for the call manager parameters. For more information about porting OID request handling for the miniport parameters, see [Porting OID Requests for CoNDIS 6.0 Miniport Drivers](porting-oid-requests-for-condis-6-0-miniport-drivers.md).

In NDIS 6.0, the [**NdisMCmOidRequest**](https://msdn.microsoft.com/library/windows/hardware/ff563548) function replaces the NDIS 5.x [**NdisMCmRequest**](https://msdn.microsoft.com/library/windows/hardware/ff553438) function, and the [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure replaces the [**NDIS\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff557179) structure.

To send an OID request to a CoNDIS client in NDIS 6.0, an MCM calls **NdisMCmOidRequest** and specifies a valid address family. If **NdisMCmOidRequest** returns NDIS\_STATUS\_PENDING, NDIS subsequently calls the [**ProtocolCoOidRequestComplete**](https://msdn.microsoft.com/library/windows/hardware/ff570255) function (formerly [**ProtocolCoRequestComplete**](https://msdn.microsoft.com/library/windows/hardware/ff563227)) of the MCM to complete the request.

To send an OID request for call manager parameters to an MCM, a CoNDIS 6.0 client specifies a valid address family when it calls [**NdisCoOidRequest**](https://msdn.microsoft.com/library/windows/hardware/ff561711). In this case, NDIS calls the MCM's [**ProtocolCoOidRequest**](https://msdn.microsoft.com/library/windows/hardware/ff570254) function (formerly [**ProtocolCoRequest**](https://msdn.microsoft.com/library/windows/hardware/ff563225)). If *ProtocolCoOidRequest* returns NDIS\_STATUS\_PENDING, the MCM must later call the [**NdisMCmOidRequestComplete**](https://msdn.microsoft.com/library/windows/hardware/ff563551) function (formerly [**NdisMCmRequestComplete**](https://msdn.microsoft.com/library/windows/hardware/ff553443)) to complete the operation. NDIS subsequently calls the client's [**ProtocolCoOidRequestComplete**](https://msdn.microsoft.com/library/windows/hardware/ff570255) function (formerly [**ProtocolCoRequestComplete**](https://msdn.microsoft.com/library/windows/hardware/ff563227)) to complete the request.

For more information about MCM OID requests, see [CoNDIS MCM OID Requests](condis-mcm-oid-requests.md).

 

 





