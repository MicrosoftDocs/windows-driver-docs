---
title: OID_WDI_TASK_SET_RADIO_STATE
description: OID_WDI_TASK_SET_RADIO_STATE is used to set the Wi-Fi radio state for the adapter.
ms.assetid: d7981df2-d3e5-49fd-8414-ca350775828b
ms.date: 07/18/2017
keywords:
 - OID_WDI_TASK_SET_RADIO_STATE Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_WDI\_TASK\_SET\_RADIO\_STATE


OID\_WDI\_TASK\_SET\_RADIO\_STATE is used to set the Wi-Fi radio state for the adapter.

| Object  | Abort capable | Default priority (host driver policy) | Normal execution time (seconds) |
|---------|---------------|---------------------------------------|---------------------------------|
| Adapter | No            | 1                                     | 1                               |

 

The task must be completed only after the disconnect activity has been completed.

The IHV component may also send unsolicited indications about radio state changes to the host.

Before the host turns off the radio, it disconnects all peers and stops any Group Owner that is running. The adapter is not expected to remember the station/GO profile information across a radio OFF/ON transition.

## Task parameters


| TLV                                                                               | Multiple TLV instances allowed | Optional | Description                                                                                                           |
|-----------------------------------------------------------------------------------|--------------------------------|----------|-----------------------------------------------------------------------------------------------------------------------|
| [**WDI\_TLV\_RADIO\_STATE\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/dn898043) |                                |          | The desired state of the radio. If this set to 1, the radio is enabled. If this is set to 0, the radio is turned off. |

 

## Task completion indication


[NDIS\_STATUS\_WDI\_INDICATION\_SET\_RADIO\_STATE\_COMPLETE](ndis-status-wdi-indication-set-radio-state-complete.md)
## Unsolicited indication


[NDIS\_STATUS\_WDI\_INDICATION\_RADIO\_STATUS](ndis-status-wdi-indication-radio-status.md)
This indication is used to report changes in the radio state for the adapter. This is sent both when a software radio change is triggered by the host and when a hardware radio state change is detected by the adapter.

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

 

 




