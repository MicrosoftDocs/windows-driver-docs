---
title: Porting a CoNDIS 5.x Driver to CoNDIS 6.0
description: Porting a CoNDIS 5.x Driver to CoNDIS 6.0
ms.assetid: 84de2618-a5cc-4fef-b036-66ba5aa71014
keywords:
- CoNDIS drivers WDK networking , porting
- connection-oriented drivers WDK networking , porting
- NDIS porting drivers WDK , CoNDIS drivers
- porting drivers WDK networking , CoNDIS drivers
- network driver porting WDK , CoNDIS drivers
- porting CoNDIS driv
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Porting a CoNDIS 5.x Driver to CoNDIS 6.0





This section describes how to port connection-oriented (CoNDIS) drivers from the NDIS 5.*x* versions to the NDIS 6.0 version. Like prior versions, NDIS 6.0 supports CoNDIS call managers, protocol drivers, miniport drivers, intermediate drivers, and miniport call managers (MCMs). For general information about CoNDIS, see [Connection-Oriented NDIS](connection-oriented-ndis.md).

NDIS 6.0 retains backward compatibility with earlier NDIS versions. For more information about backward compatibility, see [NDIS 6.0 Backward Compatibility](ndis-6-0-backward-compatibility.md).

For a summary of CoNDIS 6.0 driver porting issues, see [Summary of Changes Required to Port a CoNDIS Driver to CoNDIS 6.0](summary-of-changes-required-to-port-a-condis-driver-to-condis-6-0.md).

The following topics describe how to port a CoNDIS 5.*x* driver to CoNDIS 6.0 in more detail:

[Porting CoNDIS Driver Registration to CoNDIS 6.0](porting-condis-driver-registration-to-condis-6-0.md)

[Porting Address Family Close Operations to CoNDIS 6.0](porting-address-family-close-operations-to-condis-6-0.md)

[Porting Send and Receive Operations to CoNDIS 6.0](porting-send-and-receive-operations-to-condis-6-0.md)

[Porting OID Request Operations to CoNDIS 6.0](porting-oid-request-operations-to-condis-6-0.md)

[Porting Status Indication Operations to CoNDIS 6.0](porting-status-indication-operations-to-condis-6-0.md)

 

 





