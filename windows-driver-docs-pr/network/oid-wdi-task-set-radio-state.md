---
title: OID_WDI_TASK_SET_RADIO_STATE
author: windows-driver-content
description: OID_WDI_TASK_SET_RADIO_STATE is used to set the Wi-Fi radio state for the adapter.
ms.assetid: d7981df2-d3e5-49fd-8414-ca350775828b
ms.author: windowsdriverdev 
ms.date: 0718/2017 
ms.topic: article 
ms.prod: windows-hardware 
ms.technology: windows-devices 
keywords:
 - OID_WDI_TASK_SET_RADIO_STATE Network Drivers Starting with Windows Vista
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_WDI_TASK_SET_RADIO_STATE%20%20RELEASE:%20%286/30/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


