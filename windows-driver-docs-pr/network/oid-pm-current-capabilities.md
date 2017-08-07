---
title: OID\_PM\_CURRENT\_CAPABILITIES
author: windows-driver-content
description: As a query, overlying drivers can use the OID\_PM\_CURRENT\_CAPABILITIES OID to query the currently available power management capabilities of a network adapter.
ms.assetid: b35ce325-a1aa-43e0-bf68-cb2ab89dff76
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords:
 - OID_PM_CURRENT_CAPABILITIES Network Drivers Starting with Windows Vista
---

# OID\_PM\_CURRENT\_CAPABILITIES


As a query, overlying drivers can use the OID\_PM\_CURRENT\_CAPABILITIES OID to query the currently available power management capabilities of a network adapter. After a successful return from the OID query request, the **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](ndis-oid-request.md) structure contains a pointer to an [**NDIS\_PM\_CAPABILITIES**](ndis-pm-capabilities.md) structure.

Remarks
-------

NDIS handles the query for miniport drivers. Starting with NDIS 6.20, miniport drivers supply the power management hardware capabilities during initialization. However, NDIS can hide some capabilities from the protocol driver. For example, NDIS might report different capabilities when a user disables some or all of the power management capabilities.

Note that the current power management capabilities that NDIS reports to a protocol driver are not necessarily the same as the hardware capabilities that the miniport driver reported to NDIS.

NDIS reports the power management capabilities of an underlying network adapter to overlying protocol drivers in the **PowerManagementCapabilitiesEx** member of the [**NDIS\_BIND\_PARAMETERS**](ndis-bind-parameters.md) structure during the bind operation. Therefore, protocol drivers do not have to query the OID.

NDIS issues an [**NDIS\_STATUS\_PM\_CAPABILITIES\_CHANGE**](https://msdn.microsoft.com/library/windows/hardware/ff567410) status indication to report changes in the power management capabilities that are available to overlying drivers.

If the underlying network adapter has an NDIS 6.1 or older miniport driver, NDIS translates the power management capabilities of the underlying network adapter to an [**NDIS\_PM\_CAPABILITIES**](ndis-pm-capabilities.md) structure.

NDIS returns one of the following status codes for the request:

<a href="" id="ndis-status-success"></a>NDIS\_STATUS\_SUCCESS  
The request completed successfully. The **InformationBuffer** points to an [**NDIS\_PM\_CAPABILITIES**](ndis-pm-capabilities.md) structure.

<a href="" id="ndis-status-pending"></a>NDIS\_STATUS\_PENDING  
The request is pending completion. NDIS will pass the final status code and results to the OID request completion handler of the caller after the request is complete.

<a href="" id="ndis-status-buffer-too-short"></a>NDIS\_STATUS\_BUFFER\_TOO\_SHORT  
The information buffer was too short. NDIS set the **DATA.QUERY\_INFORMATION.BytesNeeded** member in the NDIS\_OID\_REQUEST structure to the minimum buffer size that is required.

<a href="" id="ndis-status-failure"></a>NDIS\_STATUS\_FAILURE  
The request failed for reasons other than the preceding reasons.

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
<td><p>Supported in NDIS 6.20 and later. Not requested for miniport drivers. (See Remarks section.)</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Ntddndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[**NDIS\_BIND\_PARAMETERS**](ndis-bind-parameters.md)

[**NDIS\_OID\_REQUEST**](ndis-oid-request.md)

[**NDIS\_PM\_CAPABILITIES**](ndis-pm-capabilities.md)

[**NDIS\_STATUS\_PM\_CAPABILITIES\_CHANGE**](https://msdn.microsoft.com/library/windows/hardware/ff567410)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_PM_CURRENT_CAPABILITIES%20%20RELEASE:%20%288/3/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


