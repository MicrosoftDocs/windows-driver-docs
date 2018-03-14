---
title: OID_DOT11_MAXIMUM_LIST_SIZE
author: windows-driver-content
description: OID_DOT11_MAXIMUM_LIST_SIZE
ms.assetid: f4403b06-a8c7-4c0a-8db1-82c87976175b
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -OID_DOT11_MAXIMUM_LIST_SIZE Network Drivers Starting with Windows Vista
---

# OID\_DOT11\_MAXIMUM\_LIST\_SIZE


**Important**  The [Native 802.11 Wireless LAN](https://msdn.microsoft.com/library/windows/hardware/ff560690) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](https://msdn.microsoft.com/library/windows/hardware/dn897672).

 

When queried, the OID\_DOT11\_MAXIMUM\_LIST\_SIZE object identifier (OID) requests that the miniport driver return the maximum number of multicast addresses supported by the 802.11 station.

The data type for this OID is a ULONG value.

For more information about how multicast addresses are added or deleted, see [OID\_DOT11\_MULTICAST\_LIST](oid-dot11-multicast-list.md).

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
<td><p>Available in Windows Vista and later versions of the Windows operating systems.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Windot11.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[Native 802.11 Wireless LAN OIDs](https://msdn.microsoft.com/library/windows/hardware/ff560691)

 

 




