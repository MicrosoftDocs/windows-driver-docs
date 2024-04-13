---
title: OID_WWAN_PREFERRED_MULTICARRIER_PROVIDERS
ms.topic: reference
description: OID_WWAN_PREFERRED_MULTICARRIER_PROVIDERS is used to set or query the list of preferred multi-carrier network providers. Multi-carrier providers are ones that can be set as home providers.
ms.date: 08/08/2017
keywords: 
 -OID_WWAN_PREFERRED_MULTICARRIER_PROVIDERS Network Drivers Starting with Windows Vista
---

# OID\_WWAN\_PREFERRED\_MULTICARRIER\_PROVIDERS


OID\_WWAN\_PREFERRED\_MULTICARRIER\_PROVIDERS is used to *set* or *query* the list of preferred multi-carrier network providers. Multi-carrier providers are ones that can be *set* as home providers.

Both *set* and *query* requests are supported. Miniport drivers must process *set* and *query* requests asynchronously, initially returning NDIS\_STATUS\_INDICATION\_REQUIRED to the original request, and later sending a [**NDIS\_STATUS\_WWAN\_PREFERRED\_MULTICARRIER\_PROVIDERS**](./ndis-status-wwan-preferred-multicarrier-providers.md) status notification containing an [**NDIS\_WWAN\_PREFERRED\_MULTICARRIER\_PROVIDERS**](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-_ndis_wwan_preferred_multicarrier_providers) structure.

Miniport drivers should set the **PreferredListHeader.ElementType** member to **WwanStructProvider2** and the **PreferredListHeader.ElementCount** member to the number of providers in the list when responding to OID\_WWAN\_PREFERRED\_PROVIDERS *query* requests. The multi-carrier providers returned in a *query* must be able to be set as the home provider at the time the preferred multi-carrier list is returned to the service.

Miniport drivers should set the **PreferredListHeader.ElementType** member to **WwanStructProvider2** and the **PreferredListHeader.ElementCount** member to 0 when responding to OID\_WWAN\_PREFERRED\_PROVIDERS *set* requests.

On error miniports should set the **uStatus** member of NDIS\_WWAN\_PREFERRED\_MULTICARRIER\_PROVIDERS structure with the failure status and **PreferredListHeader.ElementCount** to 0 and **PreferredLIstHeader.ElementType** to **WwanStructProvider2**.

The **Rssi** and **ErrorRate** members of WWAN\_PROVIDER2 structure should be set if available.

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Version</p></td>
<td><p>Versions: Supported in Windows 8 and later versions of Windows.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Ntddndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[**NDIS\_WWAN\_PREFERRED\_MULTICARRIER\_PROVIDERS**](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-_ndis_wwan_preferred_multicarrier_providers)

[**NDIS\_STATUS\_WWAN\_PREFERRED\_MULTICARRIER\_PROVIDERS**](./ndis-status-wwan-preferred-multicarrier-providers.md)

[MB Provider Operations](./mb-provider-operations.md)

 

