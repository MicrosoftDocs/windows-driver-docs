---
title: OID_WWAN_PROVISIONED_CONTEXTS
description: OID_WWAN_PROVISIONED_CONTEXTS reads or updates the provisioned context entries stored on the MB device or the Subscriber Identity Module (SIM).
ms.assetid: 7634fc32-9059-4f89-a591-7aa663b0c188
ms.date: 08/08/2017
keywords: 
 -OID_WWAN_PROVISIONED_CONTEXTS Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_WWAN\_PROVISIONED\_CONTEXTS


OID\_WWAN\_PROVISIONED\_CONTEXTS reads or updates the provisioned context entries stored on the MB device or the Subscriber Identity Module (SIM).

Miniport drivers must process set and query requests asynchronously, initially returning NDIS\_STATUS\_INDICATION\_REQUIRED to the original request, and later sending an [**NDIS\_STATUS\_WWAN\_PROVISIONED\_CONTEXTS**](ndis-status-wwan-provisioned-contexts.md) status notification containing an [**NDIS\_WWAN\_PROVISIONED\_CONTEXTS**](https://msdn.microsoft.com/library/windows/hardware/ff567914) structure to provide information about provisioned context entries stored on the MB device or the Subscriber Identity Module (SIM) regardless of completing set or query requests.

Remarks
-------

For more information about using this OID, see [WWAN Packet Context Management](https://msdn.microsoft.com/library/windows/hardware/ff559086).

Miniport drivers should return NDIS\_STATUS\_NOT\_SUPPORTED if the MB device they support does not support retrieval of provisioned contexts.

GSM-based devices can optionally support query and set operations. CDMA-based devices can optionally support query operations reporting Simple IP (WWAN\_CTRL\_CAPS\_CDMA\_SIMPLE\_IP).

The provisioned context entries stored on the MB device or the SIM are local to the device. Miniport drivers should not connect to the network to read in these fields.

The input structure for a set request is NDIS\_WWAN\_SET\_PROVISIONED\_CONTEXT and status indication of this object is NDIS\_STATUS\_WWAN\_PROVISIONED\_CONTEXTS.

Provisioned contexts are not same as that of the GPRS context definitions in 3GPP that caches the list of APNs. Provisioned contexts are the connectivity parameters (AccessString, UserName, and Password) that are either pre-provisioned by the Operators or OTA provisioned by the device and can be stored either in the device memory or SIM. The connectivity parameters returned by the Provisioned contexts will be used by the MB Service for PDP activation.

Both query and set form of this object is used.

Processing of this request does not require network access, but requires access to the SIM or auxiliary memory on the MB device.

The miniport driver sends NDIS\_STATUS\_WWAN\_PROVISIONED\_CONTEXTS notification to the operating system. The **ContextListHeader.ElementType** member shall be set to *WwanStructContext*. Miniport driver should set the **ContextListHeader.ElementCount** member to 0 when notification is sent in response to a set request.

The MB Service should retrieve the list of provisioned contexts from the device before conducting any individual context activation or deactivation. The list of provisioned contexts must be restricted only to the home provider network even though the device may have the capability to store multiple network provider contexts. The context list must always be the home provider network specific even in case of roaming.

SET OID\_WWAN\_PROVISIONED\_CONTEXT operation should associate the context with the network provider that is specified in the set request in **ProviderId** member of the WWAN\_SET\_CONTEXT structure. Provisioned context stored through set OID\_WWAN\_PROVISIONED\_CONTEXT requests must persist across system restarts and device power recycles.

All the empty contexts need to be reported on a query along with the provisioned contexts applicable to the home provider network.

CDMA devices that are configured for SimpleIP, reporting in WWAN\_CTRL\_CAPS\_CDMA\_SIMPLE\_IP in WwanControlCaps can optionally return at least one provisioned context filled with the correct **AccessString**, **UserName**, and **Password** members for the query request from MB Service.

Provisioned context list should be pre-provisioned in the device, updated by set OID\_WWAN\_PROVISIONED\_CONTEXT operations, or updated by device/operator using SMS or OTA. It must not be updated dynamically based on the context information provided in the OID\_WWAN\_CONNECT operation by MB Service.

For more information about how to access AccessString, UserName, and Password from the MB device for each provisioned context in the list, see [**WWAN\_CONTEXT**](https://msdn.microsoft.com/library/windows/hardware/ff571201).

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


[WWAN Packet Context Management](https://msdn.microsoft.com/library/windows/hardware/ff559086)

 

 




