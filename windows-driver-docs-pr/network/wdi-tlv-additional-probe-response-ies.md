---
title: WDI_TLV_ADDITIONAL_PROBE_RESPONSE_IES
description: WDI_TLV_ADDITIONAL_PROBE_RESPONSE_IES is a TLV that contains probe response IEs.
ms.assetid: BDEDAD4D-A35B-4AE9-BC90-184CD75002B2
ms.date: 07/18/2017
keywords:
 - WDI_TLV_ADDITIONAL_PROBE_RESPONSE_IES Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_ADDITIONAL\_PROBE\_RESPONSE\_IES


WDI\_TLV\_ADDITIONAL\_PROBE\_RESPONSE\_IES is a TLV that contains probe response IEs.

## TLV Type


0x93

## Length


The size (in bytes) of the array of UINT8 elements. The array must contain 1 or more elements.

## Values


| Type      | Description                                                                                                                                                                                                                                                  |
|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| UINT8\[\] | The array of probe response IEs. The Wi-Fi Direct port must add these additional IEs to the probe response packets when it is acting as a Wi-Fi Direct device or Group Owner. This member is ignored when the Wi-Fi Direct port is operating in client mode. |

 

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

 

 




