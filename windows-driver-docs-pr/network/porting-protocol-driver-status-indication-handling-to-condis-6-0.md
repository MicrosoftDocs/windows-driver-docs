---
title: Porting Protocol Driver Status Indication Handling to CoNDIS 6.0
description: Porting Protocol Driver Status Indication Handling to CoNDIS 6.0
ms.assetid: a5cfcbd4-a5ce-431c-8e07-10f7f4682d0c
keywords:
- porting status indications WDK networking
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Porting Protocol Driver Status Indication Handling to CoNDIS 6.0





In CoNDIS 6.0, the [**ProtocolCoStatusEx**](https://msdn.microsoft.com/library/windows/hardware/ff570258) function replaces the NDIS 5.x [**ProtocolCoStatus**](https://msdn.microsoft.com/library/windows/hardware/ff563235) function. Status indication parameters are packaged within an [**NDIS\_STATUS\_INDICATION**](https://msdn.microsoft.com/library/windows/hardware/ff567373) structure that contains the source handle, status code, buffer, and size.

The NDIS\_STATUS\_INDICATION structure can also specify a request identifier and destination handle that connect the indication to an OID request.

To determine link status, use the status indications from underlying drivers instead of OID queries. Using status indications improves computer performance and avoid possible race conditions.

For more information about handling status indications in a CoNDIS protocol driver, see [Handling Status Indications in a CoNDIS Protocol Driver](handling-status-indications-in-a-condis-protocol-driver.md).

 

 





