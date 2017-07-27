---
title: WDI_TLV_CIPHER_KEY_TYPE_INFO
author: windows-driver-content
description: WDI_TLV_CIPHER_KEY_TYPE_INFO is a TLV that contains cipher key type information for OID_WDI_SET_ADD_CIPHER_KEYS and OID_WDI_SET_DELETE_CIPHER_KEYS.
ms.assetid: 1168D53D-A837-4E3F-8E31-FB86CF866BA3
ms.author: windowsdriverdev 
ms.date: 0718/2017 
ms.topic: article 
ms.prod: windows-hardware 
ms.technology: windows-devices 
keywords:
 - WDI_TLV_CIPHER_KEY_TYPE_INFO Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_CIPHER\_KEY\_TYPE\_INFO


WDI\_TLV\_CIPHER\_KEY\_TYPE\_INFO is a TLV that contains cipher key type information for [OID\_WDI\_SET\_ADD\_CIPHER\_KEYS](https://msdn.microsoft.com/library/windows/hardware/dn925855) and [OID\_WDI\_SET\_DELETE\_CIPHER\_KEYS](https://msdn.microsoft.com/library/windows/hardware/dn925929).

## TLV Type


0x4E

## Length


The sum (in bytes) of the sizes of all contained elements.

## Values


| Type                                                                 | Description                                                                                                                                                                                                                                                                                     |
|----------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**WDI\_CIPHER\_ALGORITHM**](https://msdn.microsoft.com/library/windows/hardware/dn897802)          | Specifies the cipher algorithm that uses the key.                                                                                                                                                                                                                                               |
| [**WDI\_CIPHER\_KEY\_DIRECTION**](https://msdn.microsoft.com/library/windows/hardware/dn897803) | Specifies whether the key should be used for transmit only, receive only, or both.                                                                                                                                                                                                              |
| UINT8                                                                | Specifies whether the port should delete the key on a roam. If this value is set to 0, the key must be deleted when the port disconnects from the BSS network or connects to the BSS network. If this value is set to 1, the key should be deleted on an explicit delete or on a reset request. |
| [**WDI\_CIPHER\_KEY\_TYPE**](https://msdn.microsoft.com/library/windows/hardware/dn897806)           | Specifies the type of key being published.                                                                                                                                                                                                                                                      |

 

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Minimum supported client</p></td>
<td><p>Windows 10</p></td>
</tr>
<tr class="even">
<td><p>Minimum supported server</p></td>
<td><p>Windows Server 2016</p></td>
</tr>
<tr class="odd">
<td><p>Header</p></td>
<td>Wditypes.hpp</td>
</tr>
</tbody>
</table>

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20WDI_TLV_CIPHER_KEY_TYPE_INFO%20%20RELEASE:%20%287/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


