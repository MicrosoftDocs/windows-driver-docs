---
title: OID_PNP_REMOVE_WAKE_UP_PATTERN
description: OID_PNP_REMOVE_WAKE_UP_PATTERN
ms.assetid: 493019d0-9cd9-4712-8d18-5ee0264be9e1
ms.date: 08/08/2017
keywords: 
 -OID_PNP_REMOVE_WAKE_UP_PATTERN Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_PNP\_REMOVE\_WAKE\_UP\_PATTERN





The OID\_PNP\_REMOVE\_WAKE\_UP\_PATTERN OID requests the miniport driver to delete a wake-up pattern that it previously received in an [OID\_PNP\_ADD\_WAKE\_UP\_PATTERN](oid-pnp-add-wake-up-pattern.md) request. The wake-up pattern, along with its mask, is described by an [**NDIS\_PM\_PACKET\_PATTERN**](https://msdn.microsoft.com/library/windows/hardware/ff566756) structure.

The **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure contains the following:

-   An [**NDIS\_PM\_PACKET\_PATTERN**](https://msdn.microsoft.com/library/windows/hardware/ff566756) structure that provides information about the pattern and its mask.

-   A mask that indicates which bytes of an incoming packet should be compared with corresponding bytes in the pattern. The mask starts with the first byte of the packet. The mask immediately follows the [**NDIS\_PM\_PACKET\_PATTERN**](https://msdn.microsoft.com/library/windows/hardware/ff566756) structure in the **InformationBuffer**.

-   A wake-up pattern, which begins **PatternOffset** bytes from the beginning of the **InformationBuffer**.

An intermediate driver in which the upper edge receives this OID request must always propagate the request to the underlying miniport driver by calling Ndis(Co)Request.

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
<td><p>Supported in NDIS 6.0 and 6.1. For NDIS 6.20 and later, use <a href="oid-pm-remove-wol-pattern.md" data-raw-source="[OID_PM_REMOVE_WOL_PATTERN](oid-pm-remove-wol-pattern.md)">OID_PM_REMOVE_WOL_PATTERN</a> instead.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Ntddndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[**NDIS\_PM\_PACKET\_PATTERN**](https://msdn.microsoft.com/library/windows/hardware/ff566756)

[OID\_PNP\_ADD\_WAKE\_UP\_PATTERN](oid-pnp-add-wake-up-pattern.md)

[OID\_PM\_REMOVE\_WOL\_PATTERN](oid-pm-remove-wol-pattern.md)

 

 




