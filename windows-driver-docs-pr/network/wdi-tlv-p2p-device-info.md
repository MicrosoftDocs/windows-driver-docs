---
title: WDI_TLV_P2P_DEVICE_INFO
description: WDI_TLV_P2P_DEVICE_INFO is a TLV that contains Wi-Fi Direct device information.
ms.assetid: 6B68F334-4C21-4088-AD47-9EB41F9A1CB8
ms.date: 07/18/2017
keywords:
 - WDI_TLV_P2P_DEVICE_INFO Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_P2P\_DEVICE\_INFO


WDI\_TLV\_P2P\_DEVICE\_INFO is a TLV that contains Wi-Fi Direct device information.

## TLV Type


0x96

## Length


The sum (in bytes) of the sizes of all contained TLVs.

## Values


| Type                                                                                  | Multiple TLV instances allowed | Optional | Description                                                                                                              |
|---------------------------------------------------------------------------------------|--------------------------------|----------|--------------------------------------------------------------------------------------------------------------------------|
| [**WDI\_TLV\_P2P\_DEVICE\_INFO\_PARAMETERS**](wdi-tlv-p2p-device-info-parameters.md) |                                |          | The device information, including Wi-Fi Direct device address, supported configuration methods, and primary device type. |
| [**WDI\_TLV\_P2P\_DEVICE\_NAME**](wdi-tlv-p2p-device-name.md)                        |                                |          | The device name for this device.                                                                                         |

 

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

 

 




