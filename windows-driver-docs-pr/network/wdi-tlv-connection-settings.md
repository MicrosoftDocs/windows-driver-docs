---
title: WDI_TLV_CONNECTION_SETTINGS
ms.topic: reference
description: WDI_TLV_CONNECTION_SETTINGS is a TLV that contains connection settings for OID_WDI_TASK_CONNECT.
ms.date: 03/02/2023
keywords:
 - WDI_TLV_CONNECTION_SETTINGS Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_CONNECTION\_SETTINGS

[!INCLUDE [WDI topic note](../includes/wdi-version-warning.md)]


WDI\_TLV\_CONNECTION\_SETTINGS is a TLV that contains connection settings for [OID\_WDI\_TASK\_CONNECT](./oid-wdi-task-connect.md).

## TLV Type


0x3F

## Length


The sum (in bytes) of the sizes of all contained elements.

## Values


| Type                                                         | Description                                                                                                                                                                                                               |
|--------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| UINT8                                                        | Specifies if this is a first-time connection request (value of 0) or a roaming connection (value of 1).                                                                                                                   |
| UINT8                                                        | Specifies if this is a connection to a network with hidden/non-broadcast SSIDs. This value is 1 when connecting to a hidden network.                                                                                      |
| UINT8                                                        | This sets the dot11ExcludeUnencrypted MIB. When this value is false (0) and the cipher algorithm is WEP, the port must connect to APs that do not set the privacy field in management frames.                             |
| UINT8                                                        | Specifies if MFP is enabled (1) or disabled (0). The station must advertise its 802.11w capabilities in the association request if and only if this value is set to 1 (enabled).                                          |
| UINT8                                                        | Specifies if host-FIPS mode is enabled (1) or disabled (0).                                                                                                                                                               |
| [**WDI\_ASSOC\_STATUS**](/windows-hardware/drivers/ddi/wditypes/ne-wditypes-_wdi_assoc_status) (UINT32) | Specifies the roaming needed reason. If this is triggered due to [NDIS\_STATUS\_WDI\_INDICATION\_ROAMING\_NEEDED](./ndis-status-wdi-indication-roaming-needed.md), this contains the reason from the roam indication. |
| [**WDI\_ROAM\_TRIGGER**](/windows-hardware/drivers/ddi/wditypes/ne-wditypes-_wdi_roam_trigger) (UINT32) | Specifies whether this roam is a critical roam because the AP has set the Disassociation Imminent bit in its BSS Transition Request action frame.                                                                         |
| UINT8                                                        | Specifies if 802.11v BSS transition is supported. If this bit is set to 1, the Station must set the BSS Transition field of the Extended capabilities element (Bit 19) to 1 in the association request.                   |

 

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

 

