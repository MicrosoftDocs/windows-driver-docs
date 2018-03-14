---
title: OID_DOT11_SAFE_MODE_ENABLED
author: windows-driver-content
description: OID_DOT11_SAFE_MODE_ENABLED
ms.assetid: 29fa1ba3-dd32-4deb-9780-cb5b778fc72c
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -OID_DOT11_SAFE_MODE_ENABLED Network Drivers Starting with Windows Vista
---

# OID\_DOT11\_SAFE\_MODE\_ENABLED


**Important**  The [Native 802.11 Wireless LAN](https://msdn.microsoft.com/library/windows/hardware/ff560690) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](https://msdn.microsoft.com/library/windows/hardware/dn897672).

 

When set, the OID\_DOT11\_SAFE\_MODE\_ENABLED object identifier (OID) requests that the miniport driver enable 802.11 safe mode on the 802.11 station by setting the Boolean value **msDot11SafeModeEnabled** to **TRUE**.

The data type for this OID is a Boolean value.

The miniport driver must fail a set request with error code NDIS\_STATUS\_INVALID\_STATE if the 802.11 station is in any state except the initialization (INIT) state. When this OID is queried when the extensible station is in the INIT state, the miniport driver must complete the request if the NIC set the **bSafeModeImplemented** member of the [**DOT11\_EXTSTA\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff547688) structure to **TRUE**. Otherwise, the miniport driver should fail the set request.

This OID is set only if the NIC implements the 802.11 safe mode of operation, as indicated by the value of the **bSafeModeImplemented** member of [**DOT11\_EXTSTA\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff547688).

If this OID is not set, its default value is used.

Safe mode is disabled by default. The default value of **msDot11SafeModeEnabled** is **FALSE**.

When queried, OID\_DOT11\_SAFE\_MODE\_ENABLED requests that the miniport driver return the value of **msDot11SafeModeEnabled**.

When in safe mode, the miniport driver should ignore **dot11ExcludeUnencrypted**.

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


[**DOT11\_EXTSTA\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff547688)

[OID\_DOT11\_EXCLUDE\_UNENCRYPTED](oid-dot11-exclude-unencrypted.md)

[Native 802.11 Wireless LAN OIDs](https://msdn.microsoft.com/library/windows/hardware/ff560691)

 

 




