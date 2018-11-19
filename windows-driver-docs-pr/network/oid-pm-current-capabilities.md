---
title: OID_PM_CURRENT_CAPABILITIES
description: As a query, overlying drivers can use the OID_PM_CURRENT_CAPABILITIES OID to query the currently available power management capabilities of a network adapter.
ms.assetid: b35ce325-a1aa-43e0-bf68-cb2ab89dff76
ms.date: 08/08/2017
keywords: 
 -OID_PM_CURRENT_CAPABILITIES Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_PM\_CURRENT\_CAPABILITIES


As a query, overlying drivers can use the OID\_PM\_CURRENT\_CAPABILITIES OID to query the currently available power management capabilities of a network adapter. After a successful return from the OID query request, the **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure contains a pointer to an [**NDIS\_PM\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff566748) structure.

Remarks
-------

NDIS handles the query for miniport drivers. Starting with NDIS 6.20, miniport drivers supply the power management hardware capabilities during initialization. However, NDIS can hide some capabilities from the protocol driver. For example, NDIS might report different capabilities when a user disables some or all of the power management capabilities.

Note that the current power management capabilities that NDIS reports to a protocol driver are not necessarily the same as the hardware capabilities that the miniport driver reported to NDIS.

NDIS reports the power management capabilities of an underlying network adapter to overlying protocol drivers in the **PowerManagementCapabilitiesEx** member of the [**NDIS\_BIND\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff564832) structure during the bind operation. Therefore, protocol drivers do not have to query the OID.

NDIS issues an [**NDIS\_STATUS\_PM\_CAPABILITIES\_CHANGE**](https://msdn.microsoft.com/library/windows/hardware/ff567410) status indication to report changes in the power management capabilities that are available to overlying drivers.

If the underlying network adapter has an NDIS 6.1 or older miniport driver, NDIS translates the power management capabilities of the underlying network adapter to an [**NDIS\_PM\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff566748) structure.

NDIS returns one of the following status codes for the request:

<a href="" id="ndis-status-success"></a>NDIS\_STATUS\_SUCCESS  
The request completed successfully. The **InformationBuffer** points to an [**NDIS\_PM\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff566748) structure.

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


[**NDIS\_BIND\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff564832)

[**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710)

[**NDIS\_PM\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff566748)

[**NDIS\_STATUS\_PM\_CAPABILITIES\_CHANGE**](https://msdn.microsoft.com/library/windows/hardware/ff567410)

 

 




