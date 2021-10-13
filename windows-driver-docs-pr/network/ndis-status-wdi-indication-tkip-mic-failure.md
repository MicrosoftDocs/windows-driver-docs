---
title: NDIS_STATUS_WDI_INDICATION_TKIP_MIC_FAILURE
description: Miniport drivers use NDIS_STATUS_WDI_INDICATION_TKIP_MIC_FAILURE to indicate when a received packet that was successfully decrypted by the TKIP cipher algorithm fails the message integrity code (MIC) verification.
ms.date: 07/18/2017
keywords:
 - NDIS_STATUS_WDI_INDICATION_TKIP_MIC_FAILURE Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# NDIS\_STATUS\_WDI\_INDICATION\_TKIP\_MIC\_FAILURE


Miniport drivers use NDIS\_STATUS\_WDI\_INDICATION\_TKIP\_MIC\_FAILURE to indicate when a received packet that was successfully decrypted by the TKIP cipher algorithm fails the message integrity code (MIC) verification.

| Object |
|--------|
| Port   |

 

## Payload data


| Type                                                                             | Multiple TLV instances allowed | Optional | Description                       |
|----------------------------------------------------------------------------------|--------------------------------|----------|-----------------------------------|
| [**WDI\_TLV\_TKIP\_MIC\_FAILURE\_INFO**](./wdi-tlv-tkip-mic-failure-info.md) |                                |          | The TKIP MIC failure information. |

 

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
<td>Dot11wdi.h</td>
</tr>
</tbody>
</table>

 

