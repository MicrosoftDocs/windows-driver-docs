---
title: Handling Queries in a CoNDIS WAN Miniport Driver
description: Handling Queries in a CoNDIS WAN Miniport Driver
ms.assetid: 634618ce-3168-4729-b74a-e69f27b62ef4
keywords:
- CoNDIS WAN drivers WDK networking , query handling
- OID_WAN_CO_GET_INFO
- OID_WAN_CO_GET_LINK_INFO
- OID_WAN_CO_GET_STATS_INFO
- queries WDK CoNDIS WAN
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Handling Queries in a CoNDIS WAN Miniport Driver





This topic provides an overview of the requirements for handling queries in a CoNDIS WAN miniport driver. An upper-layer driver calls [**NdisCoOidRequest**](https://msdn.microsoft.com/library/windows/hardware/ff561711) with a query request to determine WAN-specific capabilities and current status of a CoNDIS WAN miniport driver and the miniport driver's NIC.

After the NDISWAN intermediate driver forwards the query request, NDIS calls the miniport driver's [**MiniportCoOidRequest**](https://msdn.microsoft.com/library/windows/hardware/ff559362) function. In a CoNDIS WAN miniport driver, this function is the same as in any connection-oriented miniport driver, except that the CoNDIS WAN miniport driver supports [CoNDIS WAN Objects](https://msdn.microsoft.com/library/windows/hardware/ff545146).

If the CoNDIS WAN miniport driver completes *MiniportCoOidRequest* asynchronously by returning a status of NDIS\_STATUS\_PENDING, it must complete the query later by calling [**NdisCoOidRequestComplete**](https://msdn.microsoft.com/library/windows/hardware/ff561716).

When NDIS calls *MiniportCoOidRequest*, NDIS passes a pointer to the [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure that contains the query OID and a buffer to hold the information retrieved from the miniport driver. The miniport driver controls this buffer until the request completes. If the number of bytes specified in the **InformationBufferLength** member of NDIS\_OID\_REQUEST is insufficient for the information that the OID requires, the miniport driver should fail the query request and set the **BytesNeeded** member of NDIS\_OID\_REQUEST to the number of bytes that the OID requires.

No other requests will be submitted to the particular WAN miniport driver until the current query request completes.

The following table summarizes the OIDs used to get or set operational characteristics for CoNDIS WAN miniport drivers.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Name</th>
<th align="left">Optional or Required</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p></p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff569818" data-raw-source="[OID_WAN_CO_GET_INFO](https://msdn.microsoft.com/library/windows/hardware/ff569818)">OID_WAN_CO_GET_INFO</a>
Get information about virtual connections (VCs).</td>
<td align="left"><p>Required</p></td>
</tr>
<tr class="even">
<td align="left"><p></p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff569819" data-raw-source="[OID_WAN_CO_GET_LINK_INFO](https://msdn.microsoft.com/library/windows/hardware/ff569819)">OID_WAN_CO_GET_LINK_INFO</a>
Get information about a VC.</td>
<td align="left"><p>Required</p></td>
</tr>
<tr class="odd">
<td align="left"><p></p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff569820" data-raw-source="[OID_WAN_CO_GET_STATS_INFO](https://msdn.microsoft.com/library/windows/hardware/ff569820)">OID_WAN_CO_GET_STATS_INFO</a>
Get statistics information for a VC.</td>
<td align="left"><p>Optional</p></td>
</tr>
</tbody>
</table>

 

A CoNDIS WAN miniport driver can support all of the NDIS [General Objects](https://msdn.microsoft.com/library/windows/hardware/ff546510). To learn more about setting information in a CoNDIS miniport driver, see [Querying or Setting Information](querying-or-setting-information.md).

 

 





