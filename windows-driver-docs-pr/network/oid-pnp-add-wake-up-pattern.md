---
title: OID_PNP_ADD_WAKE_UP_PATTERN
author: windows-driver-content
description: OID_PNP_ADD_WAKE_UP_PATTERN
ms.assetid: 96b95d1d-d557-4012-b95f-b1c43e2c590f
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -OID_PNP_ADD_WAKE_UP_PATTERN Network Drivers Starting with Windows Vista
---

# OID\_PNP\_ADD\_WAKE\_UP\_PATTERN


## <a href="" id="ddk-oid-pnp-add-wake-up-pattern-nr"></a>


The OID\_PNP\_ADD\_WAKE\_UP\_PATTERN OID is sent by a protocol driver to a miniport driver to specify a wake-up pattern. The wake-up pattern, along with its mask, is described by an [**NDIS\_PM\_PACKET\_PATTERN**](https://msdn.microsoft.com/library/windows/hardware/ff566756) structure.

A protocol that enables pattern-match wake-up for a miniport driver (see [OID\_PNP\_ENABLE\_WAKE\_UP](oid-pnp-enable-wake-up.md)) uses OID\_PNP\_ADD\_WAKE\_UP\_PATTERN to specify a wake-up pattern. The wake-up pattern can be stored in host memory or on the network adapter, depending on the capabilities of the network adapter.

The **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure contains the following:

-   An [**NDIS\_PM\_PACKET\_PATTERN**](https://msdn.microsoft.com/library/windows/hardware/ff566756) structure that provides information about the pattern and its mask.

-   A mask that indicates which bytes of an incoming packet should be compared with corresponding bytes in the pattern. The mask starts with the first byte of the packet. The mask immediately follows the [**NDIS\_PM\_PACKET\_PATTERN**](https://msdn.microsoft.com/library/windows/hardware/ff566756) structure in the *InformationBuffer*. For more information about how this mask works, see the [Network Device Class Power Management Reference specification](http://go.microsoft.com/fwlink/p/?linkid=27255).

-   A wake-up pattern, which begins **PatternOffset** bytes from the beginning of the *InformationBuffer*. For more information about wake-up patterns, see the [Network Device Class Power Management Reference specification](http://go.microsoft.com/fwlink/p/?linkid=27255).

The number of wake-up patterns that the miniport driver can accept from a protocol might depend on the availability of resources, such as the host memory that the miniport driver has allocated for such patterns, or the available storage in the network adapter. If a miniport driver cannot add a wake-up pattern due to insufficient resources, the miniport driver returns **NDIS\_STATUS\_RESOURCES** in response to OID\_PNP\_ADD\_WAKE\_UP\_PATTERN.

If a protocol driver tries to add a duplicate pattern, the miniport driver should return **NDIS\_STATUS\_INVALID\_DATA** in response to OID\_PNP\_ADD\_WAKE\_UP\_PATTERN.

An intermediate driver in which the upper edge receives this OID request must always propagate the request to the underlying miniport driver by calling [**NdisRequest**](https://msdn.microsoft.com/library/windows/hardware/ff554681) or [**NdisCoRequest**](https://msdn.microsoft.com/library/windows/hardware/ff551877).

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
<td><p>Supported in NDIS 6.0 and NDIS 6.1. For NDIS 6.20 and later, use [OID_PM_ADD_WOL_PATTERN](oid-pm-add-wol-pattern.md) instead.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Ntddndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[**NDIS\_PM\_PACKET\_PATTERN**](https://msdn.microsoft.com/library/windows/hardware/ff566756)

[OID\_PM\_ADD\_WOL\_PATTERN](oid-pm-add-wol-pattern.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_PNP_ADD_WAKE_UP_PATTERN%20%20RELEASE:%20%288/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


