---
title: OID_DOT11_VIRTUAL_STATION_CAPABILITY
author: windows-driver-content
description: OID_DOT11_VIRTUAL_STATION_CAPABILITY
ms.assetid: 589b0f06-ddb5-4771-98e3-26b52f07ac66
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -OID_DOT11_VIRTUAL_STATION_CAPABILITY Network Drivers Starting with Windows Vista
---

# OID\_DOT11\_VIRTUAL\_STATION\_CAPABILITY


**Important**  The [Native 802.11 Wireless LAN](https://msdn.microsoft.com/library/windows/hardware/ff560690) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](https://msdn.microsoft.com/library/windows/hardware/dn897672).

 

The OID\_DOT11\_VIRTUAL\_STATION\_CAPABILITY object identifier (OID) requests that the NIC driver return the capabilities of a virtual 802.11 station.

Support for this OID is optional. If the driver supports a Virtual Station MAC, it must also support this OID.

The data type for this OID is the [**DOT11\_EXTSTA\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff547688) structure.

The DOT11\_EXTSTA\_ATTRIBUTES structure that this OID returns must not contain any embedded pointers. The memory that this structure uses should be contiguous, and any pointers should point within this contiguous memory.

The miniport driver must report support for the standard **DOT11\_AUTH\_ALGO\_80211\_OPEN** and **DOT11\_CIPHER\_ALGO\_NONE** authentication and cipher algorithms. The miniport driver can additionally report one or more IHV-defined authentication/cipher algorithm pairs. The operating system will block any IHV-defined network profiles that attempt to set the **DOT11\_AUTH\_ALGO\_80211\_OPEN**/ **DOT11\_CIPHER\_ALGO\_NONE** authentication/cipher algorithm pair on the virtual station adapter.

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
<td><p>Available in Windows 7 and later versions of the Windows operating systems.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Windot11.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[Native 802.11 Wireless LAN OIDs](https://msdn.microsoft.com/library/windows/hardware/ff560691)

 

 




