---
title: WDI_TLV_P2P_DEVICE_FILTER_LIST
description: WDI_TLV_P2P_DEVICE_FILTER_LIST is a TLV that contains a list of Wi-Fi Direct devices and Group Owners to search for during Wi-Fi Direct device discovery.
ms.assetid: 56D1E6BD-41E3-4869-A821-334012B781A7
ms.date: 07/18/2017
keywords:
 - WDI_TLV_P2P_DEVICE_FILTER_LIST Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_P2P\_DEVICE\_FILTER\_LIST


WDI\_TLV\_P2P\_DEVICE\_FILTER\_LIST is a TLV that contains a list of Wi-Fi Direct devices and Group Owners to search for during Wi-Fi Direct device discovery.

## TLV Type


0xCE

## Length


The size (in bytes) of the array of [**WDI\_MAC\_ADDRESS**](https://msdn.microsoft.com/library/windows/hardware/dn926071) structures. The array must contain 1 or more structures.

## Values


| Type                                                  | Description                                                                                         |
|-------------------------------------------------------|-----------------------------------------------------------------------------------------------------|
| [**WDI\_MAC\_ADDRESS**](https://msdn.microsoft.com/library/windows/hardware/dn926071)\[\] | A list of Wi-Fi Direct devices and Group Owners to search for during Wi-Fi Direct device discovery. |

 

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

 

 




