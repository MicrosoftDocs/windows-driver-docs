---
title: WDI_TLV_P2P_DEVICE_INFO_PARAMETERS
description: WDI_TLV_P2P_DEVICE_INFO_PARAMETERS is a TLV that contains Wi-Fi Direct device information parameters.
ms.assetid: A0B1AC85-5F99-4674-A1C4-E25554BDD89F
ms.date: 07/18/2017
keywords:
 - WDI_TLV_P2P_DEVICE_INFO_PARAMETERS Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_P2P\_DEVICE\_INFO\_PARAMETERS


WDI\_TLV\_P2P\_DEVICE\_INFO\_PARAMETERS is a TLV that contains Wi-Fi Direct device information parameters.

## TLV Type


0x86

## Length


The sum (in bytes) of the sizes of all contained elements.

## Values


| Type       | Description                                            |
|------------|--------------------------------------------------------|
| UINT8\[6\] | The Wi-Fi Direct Device Address of the peer.           |
| UINT16     | The configuration methods supported by the device.     |
| UINT16     | Primary device type: Main type category identifier.    |
| UINT8\[4\] | Primary device type: OUI assigned to this device type. |
| UINT16     | Primary device type: Subcategory type identifier.      |

 

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

 

 




