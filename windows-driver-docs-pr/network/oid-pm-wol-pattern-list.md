---
title: OID_PM_WOL_PATTERN_LIST
description: As a query, overlying drivers can use the OID_PM_WOL_PATTERN_LIST OID to enumerate the wake on LAN patterns that are set on an underlying network adapter.
ms.assetid: 7e5a65d8-39ec-4624-aede-97df945ef5e5
ms.date: 08/08/2017
keywords: 
 -OID_PM_WOL_PATTERN_LIST Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_PM\_WOL\_PATTERN\_LIST


As a query, overlying drivers can use the OID\_PM\_WOL\_PATTERN\_LIST OID to enumerate the wake on LAN patterns that are set on an underlying network adapter. After a successful return from the query, the **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure contains a pointer to a list of [**NDIS\_PM\_WOL\_PATTERN**](https://msdn.microsoft.com/library/windows/hardware/ff566768) structures that describe the currently added WOL patterns.

Remarks
-------

NDIS handles the query for miniport drivers. NDIS drivers can use the OID\_PM\_WOL\_PATTERN\_LIST OID to get a list of wake on LAN patterns that are set on an underlying network adapter.

For each [**NDIS\_PM\_WOL\_PATTERN**](https://msdn.microsoft.com/library/windows/hardware/ff566768) structure in the list, NDIS sets the **NextWoLPatternOffset** member to the offset from the beginning of the OID information buffer (that is, the beginning of the buffer that the **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure points to) to the beginning of the next **NDIS\_PM\_WOL\_PATTERN** structure in the list. The offset in the **NextWoLPatternOffset** member of the last structure in the list is zero.

For offsets in an [**NDIS\_PM\_WOL\_PATTERN**](https://msdn.microsoft.com/library/windows/hardware/ff566768) structure other than **NextWoLPatternOffset** (for example, **NameBufferOffset**), NDIS provides offsets that are relative to the beginning of each **NDIS\_PM\_WOL\_PATTERN** structure.

If there are no WOL patterns that are set on the network adapter, NDIS sets the **DATA.QUERY\_INFORMATION.BytesWritten** member of the [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure to zero and returns **NDIS\_STATUS\_SUCCESS** for the request. The data within the **DATA.QUERY\_INFORMATION.InformationBuffer** member is not modified by NDIS.

NDIS returns one of the following status codes for the request:

<a href="" id="ndis-status-success"></a>NDIS\_STATUS\_SUCCESS  
The request completed successfully. The **InformationBuffer** contains a pointer to a list of WOL patterns, if any.

<a href="" id="ndis-status-pending"></a>NDIS\_STATUS\_PENDING  
The request is pending completion. The final status code and results will be passed to the OID request completion handler of the caller.

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


[**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710)

[**NDIS\_PM\_WOL\_PATTERN**](https://msdn.microsoft.com/library/windows/hardware/ff566768)

[OID\_PM\_ADD\_WOL\_PATTERN](oid-pm-add-wol-pattern.md)

[OID\_PM\_REMOVE\_WOL\_PATTERN](oid-pm-remove-wol-pattern.md)

[OID\_PNP\_WAKE\_UP\_PATTERN\_LIST](oid-pnp-wake-up-pattern-list.md)

 

 




