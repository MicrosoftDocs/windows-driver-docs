---
title: OID_WWAN_PIN_LIST
ms.topic: reference
description: OID_WWAN_PIN_LIST returns a list of all the different types of Personal Identification Numbers (PINs) that are supported by the MB device and additional details for each PIN type, such as the length of the PIN (minimum and maximum lengths), PIN format, PIN-entry mode (enabled/disabled/not-available). This OID also specifies the current mode of each PIN supported by the device. Set requests are not supported. Miniport drivers must process query requests asynchronously, initially returning NDIS_STATUS_INDICATION_REQUIRED to the original request, and later sending an NDIS_STATUS_WWAN_PIN_LIST status notification containing an NDIS_WWAN_PIN_LIST structure to return a list of PINs with corresponding descriptions when completing query requests.
ms.date: 08/08/2017
keywords: 
 -OID_WWAN_PIN_LIST Network Drivers Starting with Windows Vista
---

# OID\_WWAN\_PIN\_LIST


OID\_WWAN\_PIN\_LIST returns a list of all the different types of Personal Identification Numbers (PINs) that are supported by the MB device and additional details for each PIN type, such as the length of the PIN (minimum and maximum lengths), PIN format, PIN-entry mode (enabled/disabled/not-available). This OID also specifies the current mode of each PIN supported by the device.

Set requests are not supported.

Miniport drivers must process query requests asynchronously, initially returning NDIS\_STATUS\_INDICATION\_REQUIRED to the original request, and later sending an [**NDIS\_STATUS\_WWAN\_PIN\_LIST**](ndis-status-wwan-pin-list.md) status notification containing an [**NDIS\_WWAN\_PIN\_LIST**](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-_ndis_wwan_pin_list) structure to return a list of PINs with corresponding descriptions when completing query requests.

## Remarks

For more information about using this OID, see [WWAN Pin Operations](./mb-pin-operations.md).

Miniport drivers can access the Subscriber Identity Module (SIM card) when processing query operations, but should not access the provider network.

Miniport drivers must report all the PINs supported by their device. If the device does not support listing PINs, the miniport driver must report this list from a static (hard-coded) list maintained in the miniport driver itself for all the devices it supports.

Any PIN that provides device power-on verification or identification functionality should be reported as PIN1 and must be compliant to PIN1 guidelines.

Miniport drivers must return this information when the device ready-state changes to *WwanReadyStateInitialized* or when the device ready-state is *WwanReadyStateDeviceLocked* (PIN locked). Miniport drivers should also return this information in other device ready-states, wherever possible.

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
<td>Ntddndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[**NDIS\_WWAN\_PIN\_LIST**](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-_ndis_wwan_pin_list)

[**NDIS\_STATUS\_WWAN\_PIN\_LIST**](ndis-status-wwan-pin-list.md)

[WWAN Pin Operations](./mb-pin-operations.md)

 

