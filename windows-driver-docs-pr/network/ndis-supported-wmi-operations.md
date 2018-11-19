---
title: NDIS-Supported WMI Operations
description: NDIS-Supported WMI Operations
ms.assetid: 78dfe8a6-25aa-40d4-bc32-19bd1d4a41b1
keywords:
- Windows Management Instrumentation WDK networking , NDIS operations
- WMI WDK networking , NDIS operations
- virtual connections WDK NDIS WMI
- VCs WDK NDIS WMI
- miniport adapters WDK networking , enumerating
- adapters WDK networking , enumerating
- QU
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# NDIS-Supported WMI Operations





NDIS supports the following WMI operations:

-   Enumerate adapter and enumerate virtual connection (VC).

    NDIS registers global GUIDs ( [GUID\_NDIS\_ENUMERATE\_ADAPTER\_EX](https://msdn.microsoft.com/library/windows/hardware/ff552617) and GUID\_NDIS\_ENUMERATE\_VC) with WMI that enable WMI clients to enumerate all miniport adapters (that is, miniport driver instances) and all named VCs. Because NDIS track all of the loaded miniport drivers and all of the named VCs, NDIS does not query miniport drivers for such information.

-   QUERY SINGLE INSTANCE and SET SINGLE INSTANCE

    Through NDIS, a WMI client can query or set a single instance of a data block, which corresponds to a single OID. For a query, NDIS returns all of the information that is associated with an adapter or VC. A WMI client cannot query or set a data item that is within an OID. For example, a query of the GUID\_NDIS\_GEN\_CO\_LINK\_SPEED GUID returns both the outbound and inbound speed. A WMI client cannot query only the outbound speed or only the inbound speed.

-   QUERY ALL DATA

    NDIS satisfies a QUERY ALL DATA request on a particular GUID by obtaining the appropriate data and returning the combined data for all of the instances of the GUID to WMI. For example, in response to a QUERY ALL DATA request on [GUID\_NDIS\_ENUMERATE\_ADAPTER\_EX](https://msdn.microsoft.com/library/windows/hardware/ff552617), NDIS returns a list of all of the loaded miniport drivers to WMI. For a QUERY ALL DATA on the GUID that maps to OID\_GEN\_CO\_XMIT\_PDUS\_OK, NDIS queries that OID for each VC on each connection-oriented miniport driver and returns the combined data to WMI. Because the overhead for a QUERY ALL DATA request might be very high, WMI clients should use a QUERY ALL DATA request only to enumerate adapters and VCs. After determining the adapter or VC interest, the client can then query individual GUID instances.

-   EVENT NOTIFICATION

    WMI clients can register with NDIS to be notified for a particular status indication. When such a status indication occurs, NDIS passes the status information with the appropriate GUID to WMI for delivery to the clients as a WMI event.

-   EXECUTE METHOD

    Through NDIS, a WMI client can run a method that is associated with a data block, which corresponds to a single OID. WMI clients provide the information that NDIS requires to run the method. Method requests can be associated with miniport adapters, NDIS ports, or VCs. NDIS returns the resulting information after the method is successfully run.

 

 





