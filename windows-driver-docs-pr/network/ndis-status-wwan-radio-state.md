---
title: NDIS_STATUS_WWAN_RADIO_STATE
description: Miniport drivers use the NDIS_STATUS_WWAN_RADIO_STATE notification to inform the MB Service when the user changes the hardware radio power, or the device's software-based radio power state changes in response to an OID query or set request of OID_WWAN_RADIO_STATE. Miniport drivers can also send unsolicited events with this notification.This notification uses the NDIS_WWAN_RADIO_STATE structure.
ms.date: 08/08/2017
keywords: 
 -NDIS_STATUS_WWAN_RADIO_STATE Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# NDIS\_STATUS\_WWAN\_RADIO\_STATE


Miniport drivers use the NDIS\_STATUS\_WWAN\_RADIO\_STATE notification to inform the MB Service when the user changes the hardware radio power, or the device's software-based radio power state changes in response to an OID query or set request of [OID\_WWAN\_RADIO\_STATE](oid-wwan-radio-state.md).

Miniport drivers can also send unsolicited events with this notification.

This notification uses the [**NDIS\_WWAN\_RADIO\_STATE**](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-_ndis_wwan_radio_state) structure.

## Remarks

Miniport drivers should return both the current hardware-based and software-based radio power states in response to a query request

## Requirements

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


[**NDIS\_WWAN\_RADIO\_STATE**](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-_ndis_wwan_radio_state)

[OID\_WWAN\_RADIO\_STATE](oid-wwan-radio-state.md)

 

