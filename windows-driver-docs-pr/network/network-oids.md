---
title: Network OIDs
description: Network OIDs
keywords:
- OIDs WDK networking
- network OIDs WDK
- object identifiers WDK networking
- OIDs WDK networking , about OIDs
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Network OIDs





A miniport driver maintains information about its capabilities and current status, as well as information about each miniport adapter that it manages. Each information type is identified by an object identifier (OID). OIDs are system-defined. NDIS handles many of the OID requests for miniport drivers and NDIS does not pass such requests on to the miniport driver. The miniport driver reports many of its capabilities, which were formerly reported in response to OID queries, in its attributes during initialization. For more information about reporting attributes, see [Initializing an Adapter](initializing-a-miniport-adapter.md).

NDIS and higher level drivers can query and, in some cases, set information by using OIDs.

-   Higher level drivers for connectionless media call [**NdisOidRequest**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisoidrequest) to query or set information in a connectionless miniport driver. To perform a query or a set operation, NDIS calls the miniport driver's [*MiniportOidRequest*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_oid_request) function.

-   Higher level drivers for connection-oriented media call [**NdisCoOidRequest**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndiscooidrequest) to query or set information in a connection-oriented miniport driver. To perform both query and set operations, NDIS calls the miniport driver's [**MiniportCoOidRequest**](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_co_oid_request) function.

NDIS maps many of the system-defined OIDs for miniport drivers to globally unique identifiers (GUIDs). NDIS registers these GUIDs with the kernel-mode Microsoft Windows Management Instrumentation (WMI) that supports user-mode Web-Based Enterprise Management (WBEM) applications. When a WMI client queries or sets one of these GUIDs, NDIS translates the request to a query OID operation or a set OID operation, as appropriate, and then passes any returned information and the status back to WMI. You can map custom GUIDs to custom OIDs or miniport driver status. A miniport driver must register custom GUID-to-OID or GUID-to-status mappings with NDIS during initialization.

For more information about querying and setting OIDs, creating custom OIDs, and NDIS support for WMI, see [Obtaining and Setting Miniport Driver Information and NDIS Support for WMI](ndis-management-information-and-oids.md).

 

