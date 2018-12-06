---
title: Porting OID Request Operations to CoNDIS 6.0
description: Porting OID Request Operations to CoNDIS 6.0
ms.assetid: 5e29966a-88e5-4270-b8ed-34cad3c019d1
keywords:
- CoNDIS WDK networking , OID requests
- connection-oriented drivers WDK networking , OID request porting WDK networking
- OIDs WDK networking , request operation porting
- object identifiers WDK networking
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Porting OID Request Operations to CoNDIS 6.0





The CoNDIS 6.0 OID request functions are similar to the CoNDIS 5.*x* OID request functions. The primary difference between the CoNDIS 6.0 and CoNDIS 5.*x* interfaces is that the [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure replaced the [**NDIS\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff557179) structure.

This section includes the following topics:

[Porting OID Requests for CoNDIS 6.0 Miniport Drivers](porting-oid-requests-for-condis-6-0-miniport-drivers.md)

[Porting Protocol Driver OID Request Handling to CoNDIS 6.0](porting-protocol-driver-oid-request-handling-to-condis-6-0.md)

[Porting MCM OID Request Handling to CoNDIS 6.0](porting-mcm-oid-request-handling-to-condis-6-0.md)

 

 





