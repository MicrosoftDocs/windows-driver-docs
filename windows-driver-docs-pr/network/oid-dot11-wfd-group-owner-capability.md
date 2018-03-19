---
title: OID_DOT11_WFD_GROUP_OWNER_CAPABILITY
author: windows-driver-content
description: When set, the OID_DOT11_WFD_GROUP_OWNER_CAPABILITY object identifier (OID) modifies the Peer-to-Peer (P2P) group capability bitmask that a Group Owner (GO) advertises in a P2P capability attribute.
ms.assetid: 9C28ABA0-C69F-4383-8BD5-4306D31FA27D
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -OID_DOT11_WFD_GROUP_OWNER_CAPABILITY Network Drivers Starting with Windows Vista
---

# OID\_DOT11\_WFD\_GROUP\_OWNER\_CAPABILITY


**Important**  The [Native 802.11 Wireless LAN](https://msdn.microsoft.com/library/windows/hardware/ff560690) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](https://msdn.microsoft.com/library/windows/hardware/dn897672).

 

When set, the OID\_DOT11\_WFD\_GROUP\_OWNER\_CAPABILITY object identifier (OID) modifies the Peer-to-Peer (P2P) group capability bitmask that a Group Owner (GO) advertises in a P2P capability attribute.

The data type for this OID is the [**DOT11\_WFD\_GROUP\_OWNER\_CAPABILITY**](https://msdn.microsoft.com/library/windows/hardware/hh464151) structure.

A miniport retains the updated information from the [**DOT11\_WFD\_GROUP\_OWNER\_CAPABILITY**](https://msdn.microsoft.com/library/windows/hardware/hh464151) for later use in a response.

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


[**DOT11\_WFD\_GROUP\_OWNER\_CAPABILITY**](https://msdn.microsoft.com/library/windows/hardware/hh464151)

 

 




