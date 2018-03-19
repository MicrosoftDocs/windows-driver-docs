---
title: DOT11_COUNTRY_STRING
author: windows-driver-content
description: Important  The Native 802.11 Wireless LAN interface is deprecated in Windows 10 and later.
ms.assetid: e04c31aa-4b1d-4368-ab72-763b45a1ac59
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -DOT11_COUNTRY_STRING
---

# DOT11\_COUNTRY\_STRING


**Important**  The [Native 802.11 Wireless LAN](https://msdn.microsoft.com/library/windows/hardware/ff560690) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](https://msdn.microsoft.com/library/windows/hardware/dn897672).

 

The **DOT11\_COUNTRY\_STRING** array defines an 802.11 regulatory domain. For more information about country strings and regulatory domains, refer to the IEEE 802.11d-2001 standard.

```ManagedCPlusPlus
typedef UCHAR DOT11_COUNTRY_STRING[3];
```

**DOT11\_COUNTRY\_STRING**  
A 3-byte string that identifies the country in which the 802.11 station is operating.

****  

Remarks
-------

The first two bytes of the **DOT11\_COUNTRY\_STRING** array are the country code as described in the ISO/IEC 3166-1 standard. The third byte must be one of the following:

-   An ASCII space character (0x20) if the regulations under which the 802.11 station is operating encompass all environments in the country.

-   An ASCII 'O' character (0x4F) if the regulations under which the 802.11 station is operating are for an outdoor environment only.

-   An ASCII 'I' character (0x49) if the regulations under which the 802.11 station is operating are for an indoor environment only.

A **DOT11\_COUNTRY\_STRING** array with a value of all zeros is used to specify a null country string.

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


[OID\_DOT11\_COUNTRY\_STRING](oid-dot11-country-string.md)

 

 




