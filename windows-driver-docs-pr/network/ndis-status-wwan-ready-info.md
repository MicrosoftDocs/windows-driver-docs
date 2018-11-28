---
title: NDIS_STATUS_WWAN_READY_INFO
description: Miniport drivers use the NDIS_STATUS_WWAN_READY_INFO notification to inform the MB Service of device ready-state changes in response to OID_WWAN_READY_INFO \ 160;query requests.
ms.assetid: 92ddf95f-8829-4259-b53a-c7ce56ee53f0
ms.date: 08/08/2017
keywords: 
 -NDIS_STATUS_WWAN_READY_INFO Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# NDIS\_STATUS\_WWAN\_READY\_INFO


Miniport drivers use the NDIS\_STATUS\_WWAN\_READY\_INFO notification to inform the MB Service of device ready-state changes in response to [OID\_WWAN\_READY\_INFO](oid-wwan-ready-info.md) query requests.

Miniport drivers can also send unsolicited events with this notification.

This notification uses the [**NDIS\_WWAN\_READY\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff567916) structure.

Remarks
-------

Miniport drivers must report all device ready-state changes as an unsolicited event. When the miniport driver initializes the MB device, the miniport driver must set the WWAN\_READY\_INFO **ReadyState** member to **WwanReadyStateOff**. Thereafter, miniport drivers must report any device ready-state change to the MB Service through this notification. For example, miniport drivers must report a device ready-state change when the **ReadyState** member changes from **WwanReadyStateOff** to **WwanReadyStateDeviceLocked**, or **WwanReadyStateBadSim**, or **WwanReadyStateSimNotInserted**, or any other different device ready-state.

Most device ready-state changes happen when the device initializes the radio stack and the SIM card (if required). A change can also happen during the course of a session between the MB Service and the miniport driver, such as user changing the SIM card. The behavior of the MB Service shall change accordingly based on the new device ready-state.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Version</p></td>
<td><p>Available in Windows 7 and later versions of Windows.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Ndis.h</td>
</tr>
</tbody>
</table>

## See also


[**NDIS\_WWAN\_READY\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff567916)

[OID\_WWAN\_READY\_INFO](oid-wwan-ready-info.md)

 

 




