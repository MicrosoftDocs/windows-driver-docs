---
title: WDI_TLV_P2P_INCLUDE_LISTEN_CHANNEL
author: windows-driver-content
description: WDI_TLV_P2P_INCLUDE_LISTEN_CHANNEL is a TLV that specifies whether the probe request should include the Listen Channel attribute during discovery.
ms.assetid: 75662669-102A-4186-951C-58D1B36D1686
ms.author: windowsdriverdev 
ms.date: 0718/2017 
ms.topic: article 
ms.prod: windows-hardware 
ms.technology: windows-devices 
keywords:
 - WDI_TLV_P2P_INCLUDE_LISTEN_CHANNEL Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_P2P\_INCLUDE\_LISTEN\_CHANNEL


WDI\_TLV\_P2P\_INCLUDE\_LISTEN\_CHANNEL is a TLV that specifies whether the probe request should include the Listen Channel attribute during discovery.

**Note**  This TLV was added in Windows 10, version 1607, WDI version 1.0.21.

 

## TLV Type


0x128

## Length


The size (in bytes) of a UINT8.

## Values


| Type  | Description                                                                                                                                                           |
|-------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| UINT8 | This parameter specifies whether the probe request should include the Listen Channel attribute during discovery. Valid values are 0 (do not include) and 1 (include). |

 

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
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20WDI_TLV_P2P_INCLUDE_LISTEN_CHANNEL%20%20RELEASE:%20%287/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


