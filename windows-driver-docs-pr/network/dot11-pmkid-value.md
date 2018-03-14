---
title: DOT11_PMKID_VALUE
author: windows-driver-content
description: Important  The Native 802.11 Wireless LAN interface is deprecated in Windows 10 and later.
ms.assetid: 8b23bb59-251a-4898-b929-b97ff6802744
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -DOT11_PMKID_VALUE
---

# DOT11\_PMKID\_VALUE


**Important**  The [Native 802.11 Wireless LAN](https://msdn.microsoft.com/library/windows/hardware/ff560690) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](https://msdn.microsoft.com/library/windows/hardware/dn897672).

 

The **DOT11\_PMKID\_VALUE** array defines a pairwise master key identifier (PMKID).

```ManagedCPlusPlus
typedef UCHAR DOT11_PMKID_VALUE[16];
```

**DOT11\_PMKID\_VALUE**  
The PMKID value. For more information about the format of the PMKID value, refer to Clause 8.5.1.2 of the IEEE 802.11i-2004 standard.

****  

Remarks
-------

An 802.11 station that supports RSNA authentication algorithms uses PMKID values for pre-authentication when it connects to an infrastructure basic service set (BSS) network.

For more information about the PMKID, refer to Clause 8.5.1.2 of the IEEE 802.11i-2004 standard.

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


[OID\_DOT11\_PMKID\_LIST](oid-dot11-pmkid-list.md)

 

 




