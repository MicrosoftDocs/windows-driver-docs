---
title: OID_PM_REMOVE_WOL_PATTERN
ms.topic: reference
description: As a set, NDIS and protocol drivers use the OID_PM_REMOVE_WOL_PATTERN OID to remove a power management wake on LAN (WOL) pattern from a network adapter.
ms.date: 08/08/2017
keywords: 
 -OID_PM_REMOVE_WOL_PATTERN Network Drivers Starting with Windows Vista
---

# OID\_PM\_REMOVE\_WOL\_PATTERN


As a set, NDIS and protocol drivers use the OID\_PM\_REMOVE\_WOL\_PATTERN OID to remove a power management wake on LAN (WOL) pattern from a network adapter. The **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](/windows-hardware/drivers/ddi/oidrequest/ns-oidrequest-ndis_oid_request) structure contains a pointer to a ULONG pattern identifier.

## Remarks

NDIS and protocol drivers use OID\_PM\_REMOVE\_WOL\_PATTERN to remove a wake on LAN (WOL) pattern from the underlying network adapter.

The **DATA.SET\_INFORMATION.InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](/windows-hardware/drivers/ddi/oidrequest/ns-oidrequest-ndis_oid_request) structure must point to a ULONG value for a previously added WOL pattern identifier. NDIS set this pattern identifier in the **PatternId** member of the [**NDIS\_PM\_WOL\_PATTERN**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_pm_wol_pattern) structure when NDIS sent the prior [OID\_PM\_ADD\_WOL\_PATTERN](oid-pm-add-wol-pattern.md) OID request to the underlying network adapter.

### Return Status Codes

The miniport driver's [*MiniportOidRequest*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_oid_request) function returns one of the following values for this request:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Term</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>NDIS_STATUS_SUCCESS</strong></p></td>
<td><p>The miniport driver completed the request successfully.</p></td>
</tr>
<tr class="even">
<td><p><strong>NDIS_STATUS_PENDING</strong></p></td>
<td><p>The miniport driver will complete the request asynchronously. After the miniport driver has completed all processing, it must succeed the request by calling the <a href="/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismoidrequestcomplete" data-raw-source="[&lt;strong&gt;NdisMOidRequestComplete&lt;/strong&gt;](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismoidrequestcomplete)"><strong>NdisMOidRequestComplete</strong></a> function, passing <strong>NDIS_STATUS_SUCCESS</strong> for the <em>Status</em> parameter.</p></td>
</tr>
<tr class="odd">
<td><p><strong>NDIS_STATUS_NOT_ACCEPTED</strong></p></td>
<td><p>The miniport driver is resetting.</p></td>
</tr>
<tr class="even">
<td><p><strong>NDIS_STATUS_REQUEST_ABORTED</strong></p></td>
<td><p>The miniport driver stopped processing the request. For example, NDIS called the <a href="/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_reset" data-raw-source="[&lt;em&gt;MiniportResetEx&lt;/em&gt;](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_reset)"><em>MiniportResetEx</em></a> function.</p></td>
</tr>
</tbody>
</table>

 

NDIS returns one of the following status codes for this request:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Term</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>NDIS_STATUS_SUCCESS</strong></p></td>
<td><p>The OID request completed successfully.</p></td>
</tr>
<tr class="even">
<td><p><strong>NDIS_STATUS_NOT_SUPPORTED</strong></p></td>
<td><p>The NDIS version of the miniport driver is less than NDIS 6.20.</p></td>
</tr>
<tr class="odd">
<td><p><strong>NDIS_STATUS_FILE_NOT_FOUND</strong></p></td>
<td><p>The pattern identifier in the OID request is invalid.</p></td>
</tr>
<tr class="even">
<td><p><strong>NDIS_STATUS_INVALID_LENGTH</strong></p></td>
<td><p>The information buffer is too small. NDIS sets the <strong>DATA.SET_INFORMATION.BytesNeeded</strong> member in the <a href="/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_oid_request" data-raw-source="[&lt;strong&gt;NDIS_OID_REQUEST&lt;/strong&gt;](/windows-hardware/drivers/ddi/oidrequest/ns-oidrequest-ndis_oid_request)"><strong>NDIS_OID_REQUEST</strong></a> structure to the minimum buffer size that is required.</p></td>
</tr>
</tbody>
</table>

 

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Version</p></td>
<td><p>Supported in NDIS 6.20 and later. Mandatory for miniport drivers.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Ntddndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[**NDIS\_OID\_REQUEST**](/windows-hardware/drivers/ddi/oidrequest/ns-oidrequest-ndis_oid_request)

[**NDIS\_PM\_WOL\_PATTERN**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_pm_wol_pattern)

[OID\_PM\_ADD\_WOL\_PATTERN](oid-pm-add-wol-pattern.md)

[**NDIS\_STATUS\_PM\_WOL\_PATTERN\_REJECTED**](./ndis-status-pm-wol-pattern-rejected.md)

