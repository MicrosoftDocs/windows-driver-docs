---
title: NDIS Interface Information
description: NDIS Interface Information
keywords:
- management information base WDK networking
- MIBs WDK networking
- NDIS WDK , interfaces
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# NDIS Interface Information





A standardized interface for querying NDIS management information bases (MIBs) makes it easier for overlying drivers and user-mode applications to query information about network interfaces. A MIB client calls NDIS-supplied functions to request information from an underlying NDIS interface provider. This causes NDIS to issue OID requests to retrieve the information. To supply the information to the client, NDIS calls a callback function that the client registered with NDIS.

For more information about NDIS network interface services, see [NDIS Network Interfaces](/windows-hardware/drivers/ddi/_netvista/).

NDIS provides enhanced support for Management Instrumentation (WMI). For more information about NDIS 6.0 support for WMI, see [NDIS Support for WMI](ndis-support-for-wmi.md).

## Related topics


[**NDIS\_INTERFACE\_INFORMATION**](/windows/win32/api/ifdef/ns-ifdef-ndis_interface_information)

 

