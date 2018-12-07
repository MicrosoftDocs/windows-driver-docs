---
title: WDI_TLV_P2P_CONFIG_METHODS
description: WDI_TLV_P2P_CONFIG_METHODS is a TLV that contains Wi-Fi Direct configuration methods.
ms.assetid: 95F81FBB-CF78-47EC-8DB3-90F639C30865
ms.date: 07/18/2017
keywords:
 - WDI_TLV_P2P_CONFIG_METHODS Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_P2P\_CONFIG\_METHODS


WDI\_TLV\_P2P\_CONFIG\_METHODS is a TLV that contains Wi-Fi Direct configuration methods.

## TLV Type


0xEB

## Length


The size (in bytes) of a UINT16.

## Values


| Type   | Description                                                                                                                                                              |
|--------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| UINT16 | Configuration methods as defined in [**WDI\_WPS\_CONFIGURATION\_METHOD**](https://msdn.microsoft.com/library/windows/hardware/dn898198). Only PIN display, PIN keypad, and WFDS are applicable. |

 

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

 

 




