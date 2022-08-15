---
title: Standard Miniport Driver OIDs Registered with WMI
description: Standard Miniport Driver OIDs Registered with WMI
keywords:
- miniport adapters WDK networking , WMI
- adapters WDK networking , WMI
- WMI WDK networking , OIDs
- OIDs WDK networking , WMI
- Windows Management Instrumentation WDK networking , OIDs
ms.date: 04/20/2017
---

# Standard Miniport Driver OIDs Registered with WMI





NDIS registers WMI GUIDs with WMI for miniport adapters. To obtain the list of OIDs that a miniport adapter supports, NDIS issues an [OID\_GEN\_SUPPORTED\_LIST](./oid-gen-supported-list.md) query to the associated miniport driver. The miniport driver must provide the list of all of the OIDs that the miniport adapter supports. This list must contain all of the mandatory OIDs and should contain optional and custom OIDs, if any.

NDIS maps the supported OIDs to WMI GUIDs and registers the GUIDs with WMI. NDIS translates WMI GUID requests to OID requests, if necessary, for the registered OIDs.

NDIS drivers can also register custom GUIDs with WMI. For more information about custom GUIDs, see [Customized OIDs and Status Indications](customized-oids-and-status-indications.md).

NDIS also translates status indications to WMI events. For more information about translating status indications to WMI events, see [Standard Miniport Driver Status Registered with WMI](standard-miniport-driver-status-indications-registered-with-wmi.md).

 

