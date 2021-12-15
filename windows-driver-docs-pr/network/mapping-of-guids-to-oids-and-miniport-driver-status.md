---
title: Mapping of GUIDs to OIDs and Miniport Driver Status
description: Mapping of GUIDs to OIDs and Miniport Driver Status
keywords:
- WMI WDK networking , GUIDs
- OIDs WDK networking , WMI
- GUIDs WDK networking
- Windows Management Instrumentation WDK networking , GUIDs
ms.date: 04/20/2017
---

# Mapping of GUIDs to OIDs and Miniport Driver Status





When WMI sends a WMI request to a miniport adapter (that is, when WMI sends an I/O request packet \[IRP\] to a functional device object that NDIS created), NDIS intercepts the request. NDIS does not forward the request to the miniport driver if NDIS already has the information that it requires to service the request. Otherwise, NDIS maps the WMI GUID to an OID and then queries or sets the OID.

If the miniport driver is a connectionless miniport driver, NDIS can call the miniport driver's [*MiniportOidRequest*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_oid_request) function to handle the OID request. If the miniport driver is a connection-oriented miniport driver, NDIS can call the miniport driver's [**MiniportCoOidRequest**](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_co_oid_request) function to handle the OID request. NDIS returns the results of the query or set request to WMI.

Miniport drivers generate status indications with the [**NdisMIndicateStatusEx**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismindicatestatusex) or [**NdisMCoIndicateStatusEx**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismcoindicatestatusex) function. If a WMI client registers for a WMI event and a miniport driver generates an associated status indication, NDIS maps that status indication to a WMI GUID and passes a WMI event indication to WMI. WMI then passes the WMI event indication to all of the WMI clients that have registered for the WMI event.

 

