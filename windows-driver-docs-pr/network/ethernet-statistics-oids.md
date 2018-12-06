---
title: Ethernet statistics OIDs
description: This topic describes Ethernet statistics OIDs 
ms.assetid: b38ec79d-d8f3-46fa-9e6f-d42fa18f467c
keywords:
- Ethernet statistics OIDs, Ethernet NDIS OIDs, Ethernet OIDs WDK, Ethernet OIDs networking
ms.date: 11/01/2017
ms.localizationpriority: medium
---

# Ethernet statistics OIDs

The following table summarizes the OIDs used to get Ethernet statistics for Network Interface Controllers (NICs).

| Length | Query | Set | Name |
| --- | --- | --- | --- |
| 4 | O |   | [OID_802_3_RCV_OVERRUN](oid-802-3-rcv-overrun.md) |
| 4 | O |   | [OID_802_3_XMIT_DEFERRED](oid-802-3-xmit-deferred.md) |
| 4 | O |   | [OID_802_3_XMIT_HEARTBEAT_FAILURE](oid-802-3-xmit-heartbeat-failure.md) |
| 4 | O |   | [OID_802_3_XMIT_LATE_COLLISIONS](oid-802-3-xmit-late-collisions.md) |
| 4 | O |   | [OID_802_3_XMIT_MAX_COLLISIONS](oid-802-3-xmit-max-collisions.md) |
| 4 | O |   | [OID_802_3_XMIT_TIMES_CRS_LOST](oid-802-3-xmit-times-crs-lost.md) |
| 4 | O |   | [OID_802_3_XMIT_UNDERRUN](oid-802-3-xmit-underrun.md) |

> [!NOTE]
> The following OIDs are obsolete in NDIS 6.0 and later:
> - OID_802_3_RCV_ERROR_ALIGNMENT
> - OID_802_3_XMIT_MORE_COLLISIONS
> - OID_802_3_XMIT_ONE_COLLISION

