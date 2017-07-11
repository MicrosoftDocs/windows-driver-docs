---
title: WDI\_TLV\_PRIVACY\_EXEMPTION\_ENTRY
description: WDI\_TLV\_PRIVACY\_EXEMPTION\_ENTRY is a TLV that contains a privacy exemption entry.
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 086BD366-F54C-4BF4-8544-CC2AB2472EB2
keywords: ["WDI_TLV_PRIVACY_EXEMPTION_ENTRY Network Drivers Starting with Windows Vista"]
topic_type:
- apiref
api_name:
- WDI_TLV_PRIVACY_EXEMPTION_ENTRY
api_location:
- wditypes.hpp
api_type:
- HeaderDef
---

# WDI\_TLV\_PRIVACY\_EXEMPTION\_ENTRY


WDI\_TLV\_PRIVACY\_EXEMPTION\_ENTRY is a TLV that contains a privacy exemption entry.

## TLV Type


0x48

## Length


The sum (in bytes) of the sizes of all contained elements.

## Values


| Type                                                                   | Description                                                 |
|------------------------------------------------------------------------|-------------------------------------------------------------|
| UINT16                                                                 | Specifies the IEEE EtherType in big-endian byte order.      |
| [**WDI\_EXEMPTION\_ACTION\_TYPE**](https://msdn.microsoft.com/library/windows/hardware/dn897820) | Specifies the action type of the exemption.                 |
| [**WDI\_EXEMPTION\_PACKET\_TYPE**](https://msdn.microsoft.com/library/windows/hardware/dn897823) | Specifies the type of packet that the exemption applies to. |

 

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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20WDI_TLV_PRIVACY_EXEMPTION_ENTRY%20%20RELEASE:%20%287/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




