---
title: WDI_TLV_P2P_SECONDARY_DEVICE_TYPE_LIST
description: WDI_TLV_P2P_SECONDARY_DEVICE_TYPE_LIST is a TLV that contains a list of secondary device types.
ms.assetid: 278F3D2B-6729-4F7A-B3B2-B12D79C04530
ms.date: 07/18/2017
keywords:
 - WDI_TLV_P2P_SECONDARY_DEVICE_TYPE_LIST Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_P2P\_SECONDARY\_DEVICE\_TYPE\_LIST


WDI\_TLV\_P2P\_SECONDARY\_DEVICE\_TYPE\_LIST is a TLV that contains a list of secondary device types.

## TLV Type


0x94

## Length


The size (in bytes) of the array of WDI\_P2P\_DEVICE\_TYPE elements. An array length of 0 is allowed.

**Note**  WDI\_P2P\_DEVICE\_TYPE is not a WDI structure. It is defined in the WDI TLV parser generator, and is used for documentation purposes only.

 

## Values


| Type                       | Description                            |
|----------------------------|----------------------------------------|
| WDI\_P2P\_DEVICE\_TYPE\[\] | An array of Wi-Fi Direct device types. |

 

WDI\_P2P\_DEVICE\_TYPE consists of the following elements.

| Type       | Description                                   |
|------------|-----------------------------------------------|
| UINT16     | The main type category ID.                    |
| UINT8\[4\] | The OUI that is assigned to this device type. |
| UINT16     | The subcategory ID.                           |

 

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

 

 




