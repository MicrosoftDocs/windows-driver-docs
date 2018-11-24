---
title: NDIS_STATUS_WDI_INDICATION_RADIO_STATUS
description: Miniport drivers use NDIS_STATUS_WDI_INDICATION_RADIO_STATUS to indicate changes in the adapter's radio state.
ms.assetid: c2f90a52-ce55-4819-a66a-cfcc591cb3e9
ms.date: 07/18/2017
keywords:
 - NDIS_STATUS_WDI_INDICATION_RADIO_STATUS Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# NDIS\_STATUS\_WDI\_INDICATION\_RADIO\_STATUS


Miniport drivers use NDIS\_STATUS\_WDI\_INDICATION\_RADIO\_STATUS to indicate changes in the adapter's radio state. This unsolicited indication is sent when a software radio change is triggered by the host, and when a hardware radio state change is detected by the adapter.

| Object |
|--------|
| Port   |

 

## Payload data


| Type                                                                  | Multiple TLV instances allowed | Optional | Description                                              |
|-----------------------------------------------------------------------|--------------------------------|----------|----------------------------------------------------------|
| [**WDI\_TLV\_RADIO\_STATE**](https://msdn.microsoft.com/library/windows/hardware/dn898043) |                                |          | The current state of the radio in hardware and software. |

 

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
<td>Dot11wdi.h</td>
</tr>
</tbody>
</table>

## See also


[WDI\_TASK\_SET\_RADIO\_STATE](oid-wdi-task-set-radio-state.md)

 

 




