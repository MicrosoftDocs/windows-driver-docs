---
title: WDI_TLV_PM_PROTOCOL_OFFLOAD_80211RSN_REKEY
ms.topic: reference
description: WDI_TLV_PM_PROTOCOL_OFFLOAD_80211RSN_REKEY is a TLV that contains RSN Rekey protocol offload parameters.
ms.date: 03/02/2023
keywords:
 - WDI_TLV_PM_PROTOCOL_OFFLOAD_80211RSN_REKEY Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_PM\_PROTOCOL\_OFFLOAD\_80211RSN\_REKEY


WDI\_TLV\_PM\_PROTOCOL\_OFFLOAD\_80211RSN\_REKEY is a TLV that contains RSN Rekey protocol offload parameters. If TCK/iGTK key info is configured, drivers must return it when queried in [OID_WDI_GET_PM_PROTOCOL_OFFLOAD](oid-wdi-get-pm-protocol-offload.md) via this TLV.

## TLV Type


0x63

## Length


The sum (in bytes) of the sizes of all contained elements.

## Values


| Type | Description  |
| --- | --- |
| [WDI_TLV_RSN_KEY_INFO](wdi-tlv-rsn-key-info.md) | Rsn Eapol key parameters. |
| LIST<[WDI_TLV_CONFIGURED_CIPHER_KEY](wdi-tlv-configured-cipher-key.md)> | A list of configured ciphers to be set in [OID_WDI_GET_PM_PROTOCOL_OFFLOAD](oid-wdi-get-pm-protocol-offload.md). Drivers must return any GTK or iGTK keys that are currently configured. |

## Requirements

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

 

 




