---
title: Porting Protocol Driver Status Indication Handling to NDIS 6.0
description: Porting Protocol Driver Status Indication Handling to NDIS 6.0
ms.assetid: a8049122-2a49-4a49-b3f6-cbe2af47a903
keywords:
- NDIS protocol drivers WDK , status indications
- protocol drivers WDK networking , status indications
- status indications WDK networking , porting
- porting protocol drivers WDK networking , status indications
- porting status indications WDK networking
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Porting Protocol Driver Status Indication Handling to NDIS 6.0





In NDIS 6.0, the [**ProtocolStatusEx**](https://msdn.microsoft.com/library/windows/hardware/ff570270) function replaces the [**ProtocolStatus**](https://msdn.microsoft.com/library/windows/hardware/ff563257) function. Status indication parameters are packaged within an [**NDIS\_STATUS\_INDICATION**](https://msdn.microsoft.com/library/windows/hardware/ff567373) structure that contains the source handle, status code, buffer, and size.

The NDIS\_STATUS\_INDICATION structure can also specify a request identifier that connects the indication to an OID request.

NDIS 6.0 serializes status indications for each protocol binding. To determine link status, use the status indications from underlying drivers instead of OID queries. This will improve system performance and avoid possible race conditions.

For more information about status indications in a protocol driver, see [Handling Status Indications in a Protocol Driver](handling-status-indications-in-a-protocol-driver.md).

 

 





