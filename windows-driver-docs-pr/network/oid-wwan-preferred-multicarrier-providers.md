---
title: OID_WWAN_PREFERRED_MULTICARRIER_PROVIDERS
author: windows-driver-content
description: OID\_WWAN\_PREFERRED\_MULTICARRIER\_PROVIDERS is used to set or query the list of preferred multi-carrier network providers. Multi-carrier providers are ones that can be set as home providers.
ms.assetid: BA78E0B9-1B57-412C-83E7-328F8304C82D
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -OID_WWAN_PREFERRED_MULTICARRIER_PROVIDERS Network Drivers Starting with Windows Vista
---

# OID\_WWAN\_PREFERRED\_MULTICARRIER\_PROVIDERS


OID\_WWAN\_PREFERRED\_MULTICARRIER\_PROVIDERS is used to *set* or *query* the list of preferred multi-carrier network providers. Multi-carrier providers are ones that can be *set* as home providers.

Both *set* and *query* requests are supported. Miniport drivers must process *set* and *query* requests asynchronously, initially returning NDIS\_STATUS\_INDICATION\_REQUIRED to the original request, and later sending a [**NDIS\_STATUS\_WWAN\_PREFERRED\_MULTICARRIER\_PROVIDERS**](https://msdn.microsoft.com/library/windows/hardware/hh846211) status notification containing an [**NDIS\_WWAN\_PREFERRED\_MULTICARRIER\_PROVIDERS**](https://msdn.microsoft.com/library/windows/hardware/hh831864) structure.

Miniport drivers should set the **PreferredListHeader.ElementType** member to **WwanStructProvider2** and the **PreferredListHeader.ElementCount** member to the number of providers in the list when responding to OID\_WWAN\_PREFERRED\_PROVIDERS *query* requests. The multi-carrier providers returned in a *query* must be able to be set as the home provider at the time the preferred multi-carrier list is returned to the service.

Miniport drivers should set the **PreferredListHeader.ElementType** member to **WwanStructProvider2** and the **PreferredListHeader.ElementCount** member to 0 when responding to OID\_WWAN\_PREFERRED\_PROVIDERS *set* requests.

On error miniports should set the **uStatus** member of NDIS\_WWAN\_PREFERRED\_MULTICARRIER\_PROVIDERS structure with the failure status and **PreferredListHeader.ElementCount** to 0 and **PreferredLIstHeader.ElementType** to **WwanStructProvider2**.

The **Rssi** and **ErrorRate** members of WWAN\_PROVIDER2 structure should be set if available.

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
<td><p>Versions: Supported in Windows 8 and later versions of Windows.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Ntddndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[**NDIS\_WWAN\_PREFERRED\_MULTICARRIER\_PROVIDERS**](https://msdn.microsoft.com/library/windows/hardware/hh831864)

[**NDIS\_STATUS\_WWAN\_PREFERRED\_MULTICARRIER\_PROVIDERS**](https://msdn.microsoft.com/library/windows/hardware/hh846211)

[MB Provider Operations](https://msdn.microsoft.com/library/windows/hardware/ff559101)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_WWAN_PREFERRED_MULTICARRIER_PROVIDERS%20%20RELEASE:%20%288/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


