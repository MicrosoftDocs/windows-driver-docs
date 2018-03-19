---
title: OID_DOT11_FLUSH_BSS_LIST
author: windows-driver-content
description: OID_DOT11_FLUSH_BSS_LIST
ms.assetid: e56d9b5b-1f06-400a-8c9d-39fffb068a10
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -OID_DOT11_FLUSH_BSS_LIST Network Drivers Starting with Windows Vista
---

# OID\_DOT11\_FLUSH\_BSS\_LIST


**Important**  The [Native 802.11 Wireless LAN](https://msdn.microsoft.com/library/windows/hardware/ff560690) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](https://msdn.microsoft.com/library/windows/hardware/dn897672).

 

When set, the OID\_DOT11\_FLUSH\_BSS\_LIST object identifier (OID) requests that the miniport driver clear its cached basic service set (BSS) list.

The miniport driver updates the cached BSS list when it performs a network scan. For more information about the cached BSS list, see [OID\_DOT11\_ENUM\_BSS\_LIST](oid-dot11-enum-bss-list.md).

This OID does not require any data.

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

 

 




