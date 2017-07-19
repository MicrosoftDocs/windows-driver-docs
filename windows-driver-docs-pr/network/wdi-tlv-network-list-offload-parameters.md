---
title: WDI\_TLV\_NETWORK\_LIST\_OFFLOAD\_PARAMETERS
author: windows-driver-content
description: WDI\_TLV\_NETWORK\_LIST\_OFFLOAD\_PARAMETERS is a TLV that contains Network List Offload (NLO) parameters for OID\_WDI\_SET\_NETWORK\_LIST\_OFFLOAD.
ms.assetid: B8DD3BB6-DB90-4500-9BD5-252230F4BAAD
ms.author: windowsdriverdev 
ms.date: 0718/2017 
ms.topic: article 
ms.prod: windows-hardware 
ms.technology: windows-devices 
keywords:
 - WDI_TLV_NETWORK_LIST_OFFLOAD_PARAMETERS Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_NETWORK\_LIST\_OFFLOAD\_PARAMETERS


WDI\_TLV\_NETWORK\_LIST\_OFFLOAD\_PARAMETERS is a TLV that contains Network List Offload (NLO) parameters for [OID\_WDI\_SET\_NETWORK\_LIST\_OFFLOAD](https://msdn.microsoft.com/library/windows/hardware/dn925933).

## TLV Type


0x59

## Length


The sum (in bytes) of the sizes of all contained TLVs.

## Values


| Type                                                                                    | Multiple TLV instances allowed | Optional | Description                                                                                  |
|-----------------------------------------------------------------------------------------|--------------------------------|----------|----------------------------------------------------------------------------------------------|
| [**WDI\_TLV\_NETWORK\_LIST\_OFFLOAD\_CONFIG**](wdi-tlv-network-list-offload-config.md) |                                |          | Specifies NLO configuration.                                                                 |
| [**WDI\_TLV\_SSID\_OFFLOAD**](wdi-tlv-ssid-offload.md)                                 | X                              | X        | Specifies offload SSIDs. When this element is absent, the firmware should stop NLO scanning. |

 

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
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20WDI_TLV_NETWORK_LIST_OFFLOAD_PARAMETERS%20%20RELEASE:%20%287/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


