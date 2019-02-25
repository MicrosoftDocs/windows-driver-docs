---
title: Customized OIDs and Status Indications
description: Customized OIDs and Status Indications
ms.assetid: 675aff2c-8e4a-4a02-8d08-0f59b8fcd4a2
keywords:
- status indications WDK networking , WMI
- WMI WDK networking , status indications
- Windows Management Instrumentation WDK networking , status indications
- custom OIDs WDK networking
- custom status indications WDK networking
- WMI WDK networking , OID
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Customized OIDs and Status Indications





You can create a custom OID that NDIS maps to a custom GUID that you create. NDIS registers the custom GUID with WMI for the miniport driver so that WMI clients can query or set the associated information.

To provide a custom status indication, NDIS miniport drivers must use the NDIS\_STATUS\_MEDIA\_SPECIFIC\_INDICATION\_EX status indication. The WMI clients must use the data that is included with the WMI event to identify the custom event. NDIS does not register custom GUIDs for status indications.

To obtain a miniport adapter's custom OIDs and the associated WMI GUIDs, NDIS issues OID requests to the miniport driver after the miniport driver has completed initialization. NDIS issues an [OID\_GEN\_SUPPORTED\_LIST](https://msdn.microsoft.com/library/windows/hardware/ff569642) query to obtain the list of the OIDs that the miniport driver supports. The miniport driver includes both custom OIDs and standard OIDs in its response. To obtain the GUIDs that are associated with the custom OIDs, NDIS issues an [OID\_GEN\_SUPPORTED\_GUIDS](https://msdn.microsoft.com/library/windows/hardware/ff569641) query to connectionless miniport drivers or an [OID\_GEN\_CO\_SUPPORTED\_GUIDS](https://msdn.microsoft.com/library/windows/hardware/ff569566) query to connection-oriented miniport drivers.

The query to OID\_GEN\_SUPPORTED\_GUIDS or OID\_GEN\_CO\_SUPPORTED\_GUIDS returns an array of [NDIS\_GUID](filling-in-an-ndis-guid-structure.md) structures to NDIS. Each NDIS\_GUID structure maps a custom GUID to a custom OID.

To support custom OIDs and status indications, you must fill in NDIS\_GUID structures. You must also create a managed object format (MOF) file that describes the GUID and build this file with the miniport driver.

This section includes:

[Filling in an NDIS\_GUID Structure](filling-in-an-ndis-guid-structure.md)

[Including a MOF File](including-a-mof-file.md)

 

 





