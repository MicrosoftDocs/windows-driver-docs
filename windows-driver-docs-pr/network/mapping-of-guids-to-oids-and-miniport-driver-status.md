---
title: Mapping of GUIDs to OIDs and Miniport Driver Status
description: Mapping of GUIDs to OIDs and Miniport Driver Status
ms.assetid: b3c9bb40-2906-4059-b9fa-06f6ababd3f2
keywords:
- WMI WDK networking , GUIDs
- OIDs WDK networking , WMI
- GUIDs WDK networking
- Windows Management Instrumentation WDK networking , GUIDs
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Mapping of GUIDs to OIDs and Miniport Driver Status





When WMI sends a WMI request to a miniport adapter (that is, when WMI sends an I/O request packet \[IRP\] to a functional device object that NDIS created), NDIS intercepts the request. NDIS does not forward the request to the miniport driver if NDIS already has the information that it requires to service the request. Otherwise, NDIS maps the WMI GUID to an OID and then queries or sets the OID.

If the miniport driver is a connectionless miniport driver, NDIS can call the miniport driver's [*MiniportOidRequest*](https://msdn.microsoft.com/library/windows/hardware/ff559416) function to handle the OID request. If the miniport driver is a connection-oriented miniport driver, NDIS can call the miniport driver's [**MiniportCoOidRequest**](https://msdn.microsoft.com/library/windows/hardware/ff559362) function to handle the OID request. NDIS returns the results of the query or set request to WMI.

Miniport drivers generate status indications with the [**NdisMIndicateStatusEx**](https://msdn.microsoft.com/library/windows/hardware/ff563600) or [**NdisMCoIndicateStatusEx**](https://msdn.microsoft.com/library/windows/hardware/ff563562) function. If a WMI client registers for a WMI event and a miniport driver generates an associated status indication, NDIS maps that status indication to a WMI GUID and passes a WMI event indication to WMI. WMI then passes the WMI event indication to all of the WMI clients that have registered for the WMI event.

 

 





