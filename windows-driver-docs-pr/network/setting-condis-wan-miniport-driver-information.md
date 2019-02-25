---
title: Setting CoNDIS WAN Miniport Driver Information
description: Setting CoNDIS WAN Miniport Driver Information
ms.assetid: 950cb2cb-7f02-4f3c-924a-0d1e7bb19b55
keywords:
- CoNDIS WAN drivers WDK networking , information setting
- OID_WAN_CO_SET_LINK_INFO
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Setting CoNDIS WAN Miniport Driver Information





This topic provides an overview of the requirements for setting information in a CoNDIS WAN miniport driver. An upper-layer driver calls [**NdisCoOidRequest**](https://msdn.microsoft.com/library/windows/hardware/ff561711) with a set request to change information that a CoNDIS WAN miniport driver and the miniport driver's NIC maintain.

After the NDISWAN intermediate driver forwards the set request, NDIS calls the WAN miniport driver's [**MiniportCoOidRequest**](https://msdn.microsoft.com/library/windows/hardware/ff559362) function. In a CoNDIS WAN miniport driver, this function is the same as in any CoNDIS miniport driver, except that the CoNDIS WAN miniport driver supports [CoNDIS WAN Objects](https://msdn.microsoft.com/library/windows/hardware/ff545146).

No other requests will be submitted to the CoNDIS WAN miniport driver until the current set request is complete. If the miniport driver does not immediately complete the set request, it returns NDIS\_STATUS\_PENDING from *MiniportCoOidRequest* and must later call [**NdisCoOidRequestComplete**](https://msdn.microsoft.com/library/windows/hardware/ff561716) to complete the request.

A CoNDIS WAN miniport driver must recognize and respond properly to the following CoNDIS WAN OIDs.

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff569822" data-raw-source="[OID_WAN_CO_SET_LINK_INFO](https://msdn.microsoft.com/library/windows/hardware/ff569822)">OID_WAN_CO_SET_LINK_INFO</a>
Set information for a VC.</td>
<td align="left"><p>Required</p></td>
</tr>
</tbody>
</table>

 

A CoNDIS WAN miniport driver also supports the NDIS [General Objects](https://msdn.microsoft.com/library/windows/hardware/ff546510). To learn more about setting information in a CoNDIS miniport driver, see [Querying or Setting Information](querying-or-setting-information.md).

 

 





