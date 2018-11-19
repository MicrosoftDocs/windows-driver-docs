---
title: OID_WWAN_VISIBLE_PROVIDERS
description: OID_WWAN_VISIBLE_PROVIDERS returns a list of network providers currently visible within the MB device's range.
ms.assetid: 4dfd4477-6332-4163-8b3e-a1604b11d175
ms.date: 08/08/2017
keywords: 
 -OID_WWAN_VISIBLE_PROVIDERS Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_WWAN\_VISIBLE\_PROVIDERS


OID\_WWAN\_VISIBLE\_PROVIDERS returns a list of network providers currently visible within the MB device's range.

Set requests are not supported.

Miniport drivers must process query requests asynchronously, initially returning NDIS\_STATUS\_INDICATION\_REQUIRED to the original request, and later sending an [**NDIS\_STATUS\_WWAN\_VISIBLE\_PROVIDERS**](ndis-status-wwan-visible-providers.md) status notification containing an [**NDIS\_WWAN\_VISIBLE\_PROVIDERS**](https://msdn.microsoft.com/library/windows/hardware/ff567948) structure to provide information about visible network providers when completing query requests.

*Query* requests specify NDIS\_WWAN\_GET\_VISIBLE\_PROVIDERS structure as input. When the **Action** member in WWAN\_GET\_VISIBLE\_PROVIDERS is set to WWAN\_GET\_VISIBLE\_PROVIDERS\_ALL the miniport should return all visible providers. When the **Action** member in WWAN\_GET\_VISIBLE\_PROVIDERS is set to WWAN\_GET\_VISIBLE\_PROVIDERS\_MULTICARRIER the miniport should only return visible multi-carrier providers that can be set as the home provider.

The visible provider list returned by the device should have the provider state set correctly for each of the providers. For example, the multicarrier preferred providers should be tagged as WWAN\_PROVIDER\_STATE\_PREFERRED\_MULTICARRIER, the current home provider if any should be tagged as WWAN\_PROVIDER\_STATE\_HOME, The current registered provider if any should be tagged as WWAN\_PROVIDER\_STATE\_REGISTERED.

The **Rssi** and **ErrorRate** members of WWAN\_PROVIDER2 structure should be set if available.

Remarks
-------

For more information about using this OID, see [WWAN Provider Operations](https://msdn.microsoft.com/library/windows/hardware/ff559101).

Miniport drivers can access the Subscriber Identity Module (SIM card) when processing query operations, but should not access the provider network.

Miniport drivers should set the **VisibleListHeader.ElementType** member to *WwanStructProvider*.

For CDMA-based networks, miniport driver should return only the home provider, if any of the networks in the Preferred Roaming List (PRL) is currently visible. For GSM-based networks, more than one provider may be present in the visible provider list.

Devices that do not support scanning for visible providers while connected should return the WWAN\_STATUS\_BUSY error value in the **uStatus** member of the NDIS\_WWAN\_VISIBLE\_PROVIDERS structure.

Both GSM-based and CDMA-based devices must support scanning for visible providers while in registered mode. However, miniport drivers are not required to support scanning for visible provider while a Packet Data Protocol (PDP) context is active (for example, the device is connected to the provider's network).

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
<td>Ntddndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[**NDIS\_WWAN\_VISIBLE\_PROVIDERS**](https://msdn.microsoft.com/library/windows/hardware/ff567948)

[**NDIS\_STATUS\_WWAN\_VISIBLE\_PROVIDERS**](ndis-status-wwan-visible-providers.md)

[WWAN Provider Operations](https://msdn.microsoft.com/library/windows/hardware/ff559101)

 

 




