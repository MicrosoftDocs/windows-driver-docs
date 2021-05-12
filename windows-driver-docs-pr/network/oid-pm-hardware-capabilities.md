---
title: OID_PM_HARDWARE_CAPABILITIES
description: As a query, overlying drivers can use the OID_PM_HARDWARE_CAPABILITIES OID to query the power management hardware capabilities of a network adapter.
ms.date: 08/08/2017
keywords: 
 -OID_PM_HARDWARE_CAPABILITIES Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_PM\_HARDWARE\_CAPABILITIES


As a query, overlying drivers can use the OID\_PM\_HARDWARE\_CAPABILITIES OID to query the power management hardware capabilities of a network adapter. After a successful return from the OID query request, the **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_oid_request) structure contains a pointer to an [**NDIS\_PM\_CAPABILITIES**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_pm_capabilities) structure.

## Remarks

NDIS handles the query for miniport drivers. Starting with NDIS 6.20, miniport drivers supply the power management hardware capabilities during initialization in the **PowerManagementCapabilitiesEx** member of the [**NDIS\_MINIPORT\_ADAPTER\_GENERAL\_ATTRIBUTES**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_miniport_adapter_general_attributes) structure.

The miniport driver must issue an [**NDIS\_STATUS\_PM\_CAPABILITIES\_CHANGE**](./ndis-status-pm-capabilities-change.md) status indication to report changes in the power management hardware capabilities of a network adapter to NDIS and overlying drivers.

NDIS returns one of the following status codes for the request:

<a href="" id="ndis-status-success"></a>NDIS\_STATUS\_SUCCESS  
The request completed successfully. The **InformationBuffer** points to an [**NDIS\_PM\_CAPABILITIES**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_pm_capabilities) structure.

<a href="" id="ndis-status-pending"></a>NDIS\_STATUS\_PENDING  
The request is pending completion. NDIS will pass the final status code and results to the OID request completion handler of the caller after the request is complete.

<a href="" id="ndis-status-buffer-too-short"></a>NDIS\_STATUS\_BUFFER\_TOO\_SHORT  
The information buffer was too short. NDIS set the **DATA.QUERY\_INFORMATION.BytesNeeded** member in the NDIS\_OID\_REQUEST structure to the minimum buffer size that is required.

<a href="" id="ndis-status-failure"></a>NDIS\_STATUS\_FAILURE  
The request failed for reasons other than the preceding reasons.

## Requirements

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


[**NDIS\_MINIPORT\_ADAPTER\_GENERAL\_ATTRIBUTES**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_miniport_adapter_general_attributes)

[**NDIS\_OID\_REQUEST**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_oid_request)

[**NDIS\_PM\_CAPABILITIES**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_pm_capabilities)

[**NDIS\_STATUS\_PM\_CAPABILITIES\_CHANGE**](./ndis-status-pm-capabilities-change.md)

 

