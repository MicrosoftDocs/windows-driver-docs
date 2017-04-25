---
title: NDIS Interface Information
description: NDIS Interface Information
ms.assetid: 35187fda-a239-4801-b0be-53fcbee7d24e
keywords:
- management information base WDK networking
- MIBs WDK networking
- NDIS WDK , interfaces
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# NDIS Interface Information


## <a href="" id="ddk-ndis-interface-information-ng"></a>


A standardized interface for querying NDIS management information bases (MIBs) makes it easier for overlying drivers and user-mode applications to query information about network interfaces. A MIB client calls NDIS-supplied functions to request information from an underlying NDIS interface provider. This causes NDIS to issue OID requests to retrieve the information. To supply the information to the client, NDIS calls a callback function that the client registered with NDIS.

For more information about NDIS network interface services, see [NDIS Network Interfaces](https://msdn.microsoft.com/library/windows/hardware/ff566525).

NDIS provides enhanced support for Management Instrumentation (WMI). For more information about NDIS 6.0 support for WMI, see [NDIS Support for WMI](ndis-support-for-wmi.md).

## Related topics


[**NDIS\_INTERFACE\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff565736)

 

 






