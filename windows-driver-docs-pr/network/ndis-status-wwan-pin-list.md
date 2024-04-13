---
title: NDIS_STATUS_WWAN_PIN_LIST
ms.topic: reference
description: Miniport drivers use the NDIS_STATUS_WWAN_PIN_LIST notification to respond to OID query requests of OID_WWAN_PIN_LIST. Miniport drivers cannot use this notification to send unsolicited events.This notification uses the NDIS_WWAN_PIN_LIST structure.
ms.date: 03/02/2023
keywords: 
 -NDIS_STATUS_WWAN_PIN_LIST Network Drivers Starting with Windows Vista
---

# NDIS\_STATUS\_WWAN\_PIN\_LIST


Miniport drivers use the NDIS\_STATUS\_WWAN\_PIN\_LIST notification to respond to OID query requests of [OID\_WWAN\_PIN\_LIST](oid-wwan-pin-list.md).

Miniport drivers cannot use this notification to send unsolicited events.

This notification uses the [**NDIS\_WWAN\_PIN\_LIST**](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-_ndis_wwan_pin_list) structure.

## Remarks

This INDICATION is a response only notification to OID query requests of OID\_WWAN\_PIN\_LIST. Unsolicited indications are not expected for this INDICATION.

Any change in the PIN-entry mode caused as a result of an OID\_WWAN\_PIN enable or disable operation will not result in an NDIS\_STATUS\_WWAN\_PIN\_LIST INDICATION.

Note that the current PinMode for all of the PINs that the device supports must be updated to reflect the current state by the miniport driver on each query request.

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


[OID\_WWAN\_PIN\_LIST](oid-wwan-pin-list.md)

[**NDIS\_WWAN\_PIN\_LIST**](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-_ndis_wwan_pin_list)

 

