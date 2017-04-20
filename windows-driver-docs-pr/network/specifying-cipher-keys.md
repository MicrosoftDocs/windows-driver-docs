---
title: Specifying Cipher Keys
description: Specifying Cipher Keys
ms.assetid: 7580c84d-7f4c-49af-9513-96d62a293beb
keywords:
- cipher keys WDK Native 802.11
- cipher operations WDK Native 802.11 , cipher keys
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Specifying Cipher Keys


**Important**  The [Native 802.11 Wireless LAN](native-802-11-wireless-lan4.md) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](wifi-universal-driver-model.md).

 

When the miniport driver is operating in Extensible Station (ExtSTA) mode, the following object identifiers (OIDs) set the cipher keys used by the 802.11 station.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Name</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>[OID_DOT11_CIPHER_DEFAULT_KEY](https://msdn.microsoft.com/library/windows/hardware/ff569119)</p></td>
<td align="left"><p>Sets a cipher key in either the default key table (if the set request specifies a <strong>NULL</strong> media access control (MAC) address) or the per-station (STA) default key table.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[OID_DOT11_CIPHER_KEY_MAPPING_KEY](https://msdn.microsoft.com/library/windows/hardware/ff569121)</p></td>
<td align="left"><p>Sets a cipher key in the key-mapping key table.</p></td>
</tr>
</tbody>
</table>

 

When a cipher key is set, the following actions can be specified in the set request:

-   The key at the specified index within the table can be added or deleted. If a key at the specified index already exists and the requested action is to add the key, the miniport driver replaces the key with the new key material defined in the set request.

-   The key at the specified index within the table can be static and must persist across connection, roam, and disconnection operations to a basic service set (BSS) network. The miniport driver removes these keys only when one of the following occurs:
    -   The operating system deletes the key through a set request of [OID\_DOT11\_CIPHER\_DEFAULT\_KEY](https://msdn.microsoft.com/library/windows/hardware/ff569119) or [OID\_DOT11\_CIPHER\_KEY\_MAPPING\_KEY](https://msdn.microsoft.com/library/windows/hardware/ff569121).
    -   The miniport driver is reset through a method request of [OID\_DOT11\_RESET\_REQUEST](https://msdn.microsoft.com/library/windows/hardware/ff569409).

When the miniport driver is operating in Extensible Station (ExtSTA) mode, the following OIDs set or query how the 802.11 station uses cipher keys.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Name</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>[OID_DOT11_CIPHER_DEFAULT_KEY_ID](https://msdn.microsoft.com/library/windows/hardware/ff569120)</p></td>
<td align="left"><p>Sets or queries the index of the key in the default key and per-STA default key tables that the 802.11 station uses for data encryption. The station uses this key for transmitted packets unless a key-mapping key exists for the destination MAC address.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[OID_DOT11_UNICAST_USE_GROUP_ENABLED](https://msdn.microsoft.com/library/windows/hardware/ff569433)</p></td>
<td align="left"><p>Sets or queries the support by the 802.11 station for the &quot;Use Group Key&quot; cipher suite. For more information about the &quot;Use Group Key&quot; cipher suite, refer to Clause 7.3.2.9.1 of the IEEE 802.11i-2004 standard.</p></td>
</tr>
</tbody>
</table>

 

 

 





