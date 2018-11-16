---
title: WDI_TLV_NETWORK_LIST_OFFLOAD_PARAMETERS
description: WDI_TLV_NETWORK_LIST_OFFLOAD_PARAMETERS is a TLV that contains Network List Offload (NLO) parameters for OID_WDI_SET_NETWORK_LIST_OFFLOAD.
ms.assetid: B8DD3BB6-DB90-4500-9BD5-252230F4BAAD
ms.date: 07/18/2017
keywords:
 - WDI_TLV_NETWORK_LIST_OFFLOAD_PARAMETERS Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
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

 

 




