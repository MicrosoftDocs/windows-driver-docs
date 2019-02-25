---
title: OID_PM_PARAMETERS
description: As a query, protocol drivers can use the OID_PM_PARAMETERS OID to query the power management hardware capabilities of a network adapter that are currently enabled.
ms.assetid: c3431724-1b5f-4634-8b1e-27fed9031f01
ms.date: 08/08/2017
keywords: 
 -OID_PM_PARAMETERS Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_PM\_PARAMETERS


As a query, protocol drivers can use the OID\_PM\_PARAMETERS OID to query the power management hardware capabilities of a network adapter that are currently enabled. After a successful return from the OID query request, the **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure contains a pointer to an [**NDIS\_PM\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff566759) structure.

As a set, protocol drivers can use the OID\_PM\_PARAMETERS OID to enable or disable the current hardware capabilities of a network adapter. The protocol driver provides a pointer to an [**NDIS\_PM\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff566759) structure in the **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure.

Remarks
-------

Starting with NDIS 6.20, overlying protocol and filter drivers use OID\_PM\_PARAMETERS to query and set the power management hardware capabilities of a network adapter that are currently enabled.

When an overlying driver queries the OID\_PM\_PARAMETERS OID, NDIS completes the request without forwarding it to the miniport driver. NDIS stores the requested settings and combines them with the settings from other such requests. Before NDIS transitions the network adapter to the low power state, NDIS sends a set request to the miniport driver that contains the combined settings from all of the requests that NDIS stored.

The capabilities that are currently enabled can be a subset of the capabilities that the hardware supports. For more information about the capabilities that the hardware supports, see [OID\_PM\_HARDWARE\_CAPABILITIES](oid-pm-hardware-capabilities.md).

**Note**  If NDIS sets the NDIS\_PM\_SELECTIVE\_SUSPEND\_ENABLED flag in the **WakeUpFlags** member of [**NDIS\_PM\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff566759) structure, it issues the OID set request of OID\_PM\_PARAMETERS directly to the miniport driver. This allows NDIS to bypass the processing by filter drivers in the networking driver stack.

 

NDIS or the miniport driver returns one of the following status codes for the request:

<a href="" id="ndis-status-success"></a>NDIS\_STATUS\_SUCCESS  
The request completed successfully.

<a href="" id="ndis-status-pending"></a>NDIS\_STATUS\_PENDING  
The request is pending completion. NDIS will pass the final status code and results to the OID request completion handler of the caller after the request is complete.

<a href="" id="ndis-status-buffer-too-short"></a>NDIS\_STATUS\_BUFFER\_TOO\_SHORT  
The information buffer was too short. NDIS set the **DATA.QUERY\_INFORMATION.BytesNeeded** member in the NDIS\_OID\_REQUEST structure to the minimum buffer size that is required.

<a href="" id="ndis-status-invalid-parameter"></a>NDIS\_STATUS\_INVALID\_PARAMETER  
The request failed because it tried to enable a capability that the underlying network adapter does not support.

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
<td><p>Supported in NDIS 6.20 and later.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Ntddndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710)

[**NDIS\_PM\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff566759)

[OID\_PM\_HARDWARE\_CAPABILITIES](oid-pm-hardware-capabilities.md)

 

 




