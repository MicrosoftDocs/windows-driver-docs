---
title: OID_DOT11_WFD_START_GO_REQUEST
author: windows-driver-content
description: When set, the OID_DOT11_WFD_START_GO_REQUEST object identifier (OID) requests that the Wi-Fi Direct (WFD) Group Owner (GO) start the group.
ms.assetid: 1512E48E-5498-4261-BA04-14581F1FD70F
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -OID_DOT11_WFD_START_GO_REQUEST Network Drivers Starting with Windows Vista
---

# OID\_DOT11\_WFD\_START\_GO\_REQUEST


**Important**  The [Native 802.11 Wireless LAN](https://msdn.microsoft.com/library/windows/hardware/ff560690) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](https://msdn.microsoft.com/library/windows/hardware/dn897672).

 

When set, the OID\_DOT11\_WFD\_START\_GO\_REQUEST object identifier (OID) requests that the Wi-Fi Direct (WFD) Group Owner (GO) start the group. The WFD port should use port configuration information to create beacons, start beaconing, and respond to probe requests.

The miniport behavior for this OID on a WFD GO port is identical to the behavior of an Extensible Access Point port for an [OID\_DOT11\_START\_AP\_REQUEST](oid-dot11-start-ap-request.md) request.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Version</p></td>
<td><p>Supported starting with Windows 8.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Windot11.h (include Windot11.h)</td>
</tr>
</tbody>
</table>

## See also


[OID\_DOT11\_START\_AP\_REQUEST](oid-dot11-start-ap-request.md)

 

 




