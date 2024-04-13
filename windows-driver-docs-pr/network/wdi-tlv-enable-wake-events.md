---
title: WDI_TLV_ENABLE_WAKE_EVENTS
ms.topic: reference
description: WDI_TLV_ENABLE_WAKE_EVENTS is a TLV that contains the enabled wake events.
ms.date: 03/02/2023
keywords:
 - WDI_TLV_ENABLE_WAKE_EVENTS Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_ENABLE\_WAKE\_EVENTS


WDI\_TLV\_ENABLE\_WAKE\_EVENTS is a TLV that contains the enabled wake events.

## TLV Type


0x60

## Length


The sum (in bytes) of the sizes of all contained elements.

## Values


| Type   | Description                                                                                                                                                          |
|--------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| UINT32 | Specifies the enabled wake-on-LAN packet patterns using the flags as documented in [**NDIS\_PM\_PARAMETERS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_pm_parameters).EnabledWoLPacketPatterns. |
| UINT32 | Specifies the enabled protocol offloads using the flags as documented in [**NDIS\_PM\_PARAMETERS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_pm_parameters).EnabledProtocolOffloads.            |
| UINT32 | Specifies the wake-up flags using the flags as documented in [**NDIS\_PM\_PARAMETERS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_pm_parameters).WakeUpFlags.                                    |
| UINT32 | Specifies the media-specific wake up events using the flags as documented in [**NDIS\_PM\_PARAMETERS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_pm_parameters).MediaSpecificWakeUpEvents.      |

 

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

 

