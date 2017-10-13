---
title: WDI_TLV_INDICATION_STOP_AP
author: windows-driver-content
description: WDI_TLV_INDICATION_STOP_AP is a TLV that contains the reason for a Stop AP indication.
ms.assetid: 49FA6AF6-68BE-437B-9715-5090F52F0109
ms.author: windowsdriverdev 
ms.date: 07/18/2017 
ms.topic: article 
ms.prod: windows-hardware 
ms.technology: windows-devices 
keywords:
 - WDI_TLV_INDICATION_STOP_AP Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_INDICATION\_STOP\_AP


WDI\_TLV\_INDICATION\_STOP\_AP is a TLV that contains the reason for a Stop AP indication.

## TLV Type


0xE6

## Length


The size (in bytes) of a UINT32.

## Values


| Type   | Description                                                                                                  |
|--------|--------------------------------------------------------------------------------------------------------------|
| UINT32 | The Stop AP reason. See [**WDI\_STOP\_AP\_REASON**](https://msdn.microsoft.com/library/windows/hardware/dn926116) for possible reason values. |

 

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

## See also


[NDIS\_STATUS\_WDI\_INDICATION\_STOP\_AP](https://msdn.microsoft.com/library/windows/hardware/dn925661)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20WDI_TLV_INDICATION_STOP_AP%20%20RELEASE:%20%287/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


