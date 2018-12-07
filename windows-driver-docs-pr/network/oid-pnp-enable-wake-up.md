---
title: OID_PNP_ENABLE_WAKE_UP
description: OID_PNP_ENABLE_WAKE_UP
ms.assetid: 9afe774b-a429-413f-a7b6-3a3d79d2b95f
ms.date: 08/08/2017
keywords: 
 -OID_PNP_ENABLE_WAKE_UP Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_PNP\_ENABLE\_WAKE\_UP





As a set, the OID\_PNP\_ENABLE\_WAKE\_UP OID specifies the wake-up capabilities that a miniport driver should enable in a network adapter.

As a query, OID\_PNP\_ENABLE\_WAKE\_UP obtains the current wake-up capabilities that are enabled for a network adapter.

The **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure is a bitmask of flags that can be used to enable a combination of wake-up events:

<a href="" id="ndis-pnp-wake-up-magic-packet"></a>**NDIS\_PNP\_WAKE\_UP\_MAGIC\_PACKET**  
When set, specifies that the miniport driver should enable a network adapter to signal a wake-up event on receipt of a magic packet. (A *magic packet* is a packet that contains 16 contiguous copies of the receiving network adapter's Ethernet address.) When cleared, specifies that the miniport driver should disable the network adapter from signaling such a wake-up event.

<a href="" id="ndis-pnp-wake-up-pattern-match"></a>**NDIS\_PNP\_WAKE\_UP\_PATTERN\_MATCH**  
When set, specifies that the miniport driver should enable a network adapter to signal a wake-up event on receipt of a packet that contains a pattern specified by the protocol with [OID\_PNP\_ADD\_WAKE\_UP\_PATTERN](oid-pnp-add-wake-up-pattern.md). When cleared, specifies that the miniport driver should disable the network adapter from signaling such a wake-up event.

<a href="" id="ndis-pnp-wake-up-link-change"></a>**NDIS\_PNP\_WAKE\_UP\_LINK\_CHANGE**  
Reserved. NDIS ignores this flag.

A protocol driver uses the network adapter's wake-up capabilities in [**NDIS\_BIND\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff564832) to enable the associated network adapter's wake-up capabilities. A protocol driver can also query this OID to determine which wake-up capabilities are enabled for a network adapter.

NDIS does not immediately enable the wake-up capabilities that a protocol driver specifies. Instead, NDIS keeps tracks of the wake-up capabilities that the protocol driver enabled and, just before the network adapter transitions to a low-power state, NDIS sends an OID\_PNP\_ENABLE\_WAKE\_UP set request to the miniport driver to enable the appropriate wake-up events.

Before the network adapter transitions to a low-power state (that is, before NDIS sends the miniport driver an [OID\_PNP\_SET\_POWER](oid-pnp-set-power.md) request), NDIS sends the miniport driver an OID\_PNP\_ENABLE\_WAKE\_UP request to enable the appropriate wake-up capabilities.

The miniport driver must take the appropriate device-dependent steps to enable or disable wake-up events on the network adapter.

The miniport driver should clear the wake-up capabilities that NDIS set with OID\_PNP\_ENABLE\_WAKE\_UP when the system is resumed. The wake-up capabilities should not be persisted across resumes. If wake-up capabilities are enabled, NDIS explicitly sets OID\_PNP\_ENABLE\_WAKE\_UP before the miniport transitions to the low-power state.

An intermediate driver in which the upper edge receives this OID request must always propagate the request to the underlying miniport driver by calling the [**NdisOidRequest**](https://msdn.microsoft.com/library/windows/hardware/ff563710) or [**NdisCoOidRequest**](https://msdn.microsoft.com/library/windows/hardware/ff561711) function.

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
<td><p>Supported in NDIS 6.0 and 6.1. For NDIS 6.20 and later, use <a href="oid-pm-parameters.md" data-raw-source="[OID_PM_PARAMETERS](oid-pm-parameters.md)">OID_PM_PARAMETERS</a> instead).</p></td>
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

[**NdisCoOidRequest**](https://msdn.microsoft.com/library/windows/hardware/ff561711)

[**NdisOidRequest**](https://msdn.microsoft.com/library/windows/hardware/ff563710)

[OID\_PM\_PARAMETERS](oid-pm-parameters.md)

[OID\_PNP\_ADD\_WAKE\_UP\_PATTERN](oid-pnp-add-wake-up-pattern.md)

 

 




