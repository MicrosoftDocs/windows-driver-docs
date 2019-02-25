---
title: OIDs for connection-oriented call managers and clients
description: This topic describes OIDs for connection-oriented call managers and clients.
ms.assetid: a2ffbfd4-a63e-41d1-ab57-0c23661148ca
keywords:
- OIDs for connection-oriented call managers and clients
ms.date: 11/02/2017
ms.localizationpriority: medium
---

# OIDs for connection-oriented call managers and clients

The following table summarizes the OIDs that connection-oriented clients can send to call managers or MCM drivers and that call managers or MCM drivers can send to connection-oriented clients. 

In this table, M indicates an OID is mandatory, while O indicates it is optional.

| Length | Query | Set | Name |
| --- | --- | --- | --- |
| Varies |   | O | [OID_CO_ADD_ADDRESS](oid-co-add-address.md) |
| Varies |   | O | [OID_CO_ADD_PVC](oid-co-add-pvc.md) |
| 0 |   | O | [OID_CO_ADDRESS_CHANGE](oid-co-address-change.md) |
| 0 |   | M | [OID_CO_AF_CLOSE](oid-co-af-close.md) |
| Varies |   | O | [OID_CO_DELETE_ADDRESS](oid-co-delete-address.md) |
| Varies |   | O | [OID_CO_DELETE_PVC](oid-co-delete-pvc.md) |
| Varies | O |   | [OID_CO_GET_ADDRESSES](oid-co-get-addresses.md) |
|   |   |   | [OID_CO_GET_CALL_INFORMATION](oid-co-get-call-information.md) |
| 0 |   | O | [OID_CO_SIGNALING_DISABLED](oid-co-signaling-disabled.md) |
| 0 |   | O | [OID_CO_SIGNALING_ENABLED](oid-co-signaling-enabled.md) |

