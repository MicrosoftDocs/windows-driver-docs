---
title: WDI_TLV_VIRTUALIZATION_CAPABILITIES
description: WDI_TLV_VIRTUALIZATION_CAPABILITIES is a TLV that contains virtualization capabilities.
ms.assetid: D72E9984-7193-406C-8BA3-006E54400B30
ms.date: 07/18/2017
keywords:
 - WDI_TLV_VIRTUALIZATION_CAPABILITIES Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_VIRTUALIZATION\_CAPABILITIES


WDI\_TLV\_VIRTUALIZATION\_CAPABILITIES is a TLV that contains virtualization capabilities.

## TLV Type


0x10

## Length


The sum (in bytes) of the sizes of all contained elements.

## Values


| Type  | Description                                                                                                                                                                                                                       |
|-------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| UINT8 | The number of supported ExtSTA ports.                                                                                                                                                                                             |
| UINT8 | The number of supported Wi-Fi Direct Group ports. This count should only include Role ports. If this value is non-zero, it is assumed that a Wi-Fi Direct Device port is available.                                               |
| UINT8 | The number of supported legacy ExtAP ports.                                                                                                                                                                                       |
| UINT8 | The maximum number of supported simultaneous AP/WFD Group Owners.                                                                                                                                                                 |
| UINT8 | The maximum number of separate channels that the device can operate in and maintain data connections on simultaneously. This limit should not include temporary multichannel operations like scans and Wi-Fi Direct negotiations. |
| UINT8 | The maximum number of supported simultaneous STA/WFD clients.                                                                                                                                                                     |

 

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

 

 




