---
title: ISNMP Automation Interface
description: ISNMP Automation Interface
MS-HAID:
- 'webfnc\_4ff82461-8ece-4336-8f86-9461ad4ec8d7.xml'
- 'print.isnmp\_automation\_interface'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# ISNMP Automation Interface

The Automation interface for the **ISNMP** object is essentially an OLE automation wrapper for the functions in the Simple Network Management Protocol (SNMP) Management API. The **ISNMP** interface enables an ASP Web page to set and retrieve values associated with SNMP object identifiers (OIDs). For more information about the SNMP Management API, see the Windows SDK documentation.

The **ISNMP** interface works only with printers that use Microsoft's standard TCIP/IP [port monitor](./port-monitors.md). 

The programmatic identifier for the **ISNMP** object is OlePrn.OleSNMP.

For more information about how to access printers from ASP Web pages, see [Internet Printing](./internet-printing.md).

The methods in the **ISNMP** interface are described in the following section:

[ISNMP Methods](isnmp-methods.md)
