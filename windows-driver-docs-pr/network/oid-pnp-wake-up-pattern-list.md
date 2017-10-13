---
title: OID_PNP_WAKE_UP_PATTERN_LIST
author: windows-driver-content
description: OID\_PNP\_WAKE\_UP\_PATTERN\_LIST
ms.assetid: 36e4243f-5df6-4231-b1e3-63fcb2e2ec04
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -OID_PNP_WAKE_UP_PATTERN_LIST Network Drivers Starting with Windows Vista
---

# OID\_PNP\_WAKE\_UP\_PATTERN\_LIST


## <a href="" id="ddk-oid-pnp-wake-up-pattern-list-nr"></a>


The OID\_PNP\_WAKE\_UP\_PATTERN\_LIST OID is used by a protocol to query a list of the wake-up patterns currently set for the miniport driver's network adapter. A protocol specifies a wake-up pattern with [OID\_PNP\_ADD\_WAKE\_UP\_PATTERN](oid-pnp-add-wake-up-pattern.md).

OID\_PNP\_WAKE\_UP\_PATTERN\_LIST is handled by NDIS rather than the miniport driver.

NDIS returns to the protocol a description of each wake-up pattern set in the miniport driver. Each wake-up pattern, along with its mask, is described by an [**NDIS\_PM\_PACKET\_PATTERN**](https://msdn.microsoft.com/library/windows/hardware/ff566756) structure.

For each wake-up pattern, the **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure contains the following:

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
<td><p>Supported in NDIS 6.0 and 6.1. For NDIS 6.20 and later, use [OID_PM_WOL_PATTERN_LIST](oid-pm-wol-pattern-list.md) instead.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Ntddndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[**NDIS\_PM\_PACKET\_PATTERN**](https://msdn.microsoft.com/library/windows/hardware/ff566756)

[**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710)

[OID\_PM\_WOL\_PATTERN\_LIST](oid-pm-wol-pattern-list.md)

[OID\_PNP\_ADD\_WAKE\_UP\_PATTERN](oid-pnp-add-wake-up-pattern.md)

[OID\_PNP\_REMOVE\_WAKE\_UP\_PATTERN](oid-pnp-remove-wake-up-pattern.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_PNP_WAKE_UP_PATTERN_LIST%20%20RELEASE:%20%288/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


