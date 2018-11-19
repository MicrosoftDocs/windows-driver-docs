---
title: Handling Status Indications in a CoNDIS Protocol Driver
description: Handling Status Indications in a CoNDIS Protocol Driver
ms.assetid: 948df51b-0561-4b67-b87f-e1652bb18772
keywords:
- protocol drivers WDK networking , CoNDIS
- NDIS protocol drivers WDK , CoNDIS
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Handling Status Indications in a CoNDIS Protocol Driver





Protocol drivers must supply a [**ProtocolCoStatusEx**](https://msdn.microsoft.com/library/windows/hardware/ff570258) function that NDIS calls when an underlying driver reports status.

NDIS calls a protocol driver's *ProtocolCoStatusEx* function after an underlying driver calls a status indication function (for example, [**NdisMCoIndicateStatusEx**](https://msdn.microsoft.com/library/windows/hardware/ff563562)). For more information about indicating status from a miniport driver, see [CoNDIS Miniport Driver Status Indications](condis-miniport-driver-status-indications.md).

If the status indication is associated with an OID request, the underlying driver can set the **DestinationHandle** and **RequestId** members of the [**NDIS\_STATUS\_INDICATION**](https://msdn.microsoft.com/library/windows/hardware/ff567373) structure that contains the status information so that NDIS can provide the status indication to a specific protocol binding. For more information about OID requests, see [CoNDIS Protocol Driver OID Requests](condis-protocol-driver-oid-requests.md).

 

 





