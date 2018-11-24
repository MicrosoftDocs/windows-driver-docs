---
title: Remote NDIS OIDs
description: Remote NDIS OIDs
ms.assetid: c97592e8-f395-475e-8e6c-6366d1605075
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Remote NDIS OIDs





This section lists the required and optional NDIS OIDs for Remote NDIS Ethernet devices. The list takes into account the unique properties of a Remote NDIS device and the Remote NDIS miniport driver, so the list is not identical to the list that a normal NDIS connectionless miniport driver would support. Some OIDs are both *set* and *query* OIDs; if a mandatory OID is defined as both, then it must be supported by a Remote NDIS device for both [REMOTE\_NDIS\_SET\_MSG](remote-ndis-set-msg.md) and [REMOTE\_NDIS\_QUERY\_MSG](remote-ndis-query-msg.md). For a detailed explanation of the OIDs, see the Microsoft Windows Driver Development Kit (DDK).

The following lists of Remote NDIS OIDs are broken down into two groups -- general OID and 802.3 specific OID. Additionally, each group includes a subsection of statistic OID queries. The general OIDs are required for any networking device.

-   [General OIDs](general-oids2.md)
-   [General Statistic OIDs](general-statistic-oids.md)
-   [802.3 OIDs](802-3-oids.md)
-   [802.3 Statistic OIDs](802-3-statistic-oids.md)
-   [Optional Power Management OIDs](optional-power-management-oids.md)
-   [Optional Network Wake Up OIDs](optional-network-wake-up-oids.md)

 

 





