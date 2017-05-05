---
title: Filter Module Direct OID Requests
description: Filter Module Direct OID Requests
ms.assetid: 0ab7079b-6578-4932-a276-40a961b55efe
keywords:
- direct OID request interface WDK networking
- direct OID request path WDK networking
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Filter Module Direct OID Requests


## <a href="" id="ddk-filter-module-direct-oid-requests-ng"></a>


To support the direct OID request path, filter drivers provide *FilterXxx* function entry points in the [**NDIS\_FILTER\_DRIVER\_CHARACTERISTICS**](https://msdn.microsoft.com/library/windows/hardware/ff565515) structure and NDIS provides **NdisF*Xxx*** functions for filter drivers.

The *direct OID request interface* is similar to the standard OID request interface. For example, the [**NdisFDirectOidRequest**](https://msdn.microsoft.com/library/windows/hardware/ff561809) and [*FilterDirectOidRequest*](https://msdn.microsoft.com/library/windows/hardware/ff549931) functions are similar to the [**NdisFOidRequest**](https://msdn.microsoft.com/library/windows/hardware/ff561830) and [*FilterOidRequest*](https://msdn.microsoft.com/library/windows/hardware/ff549954) functions.

**Note**  NDIS 6.1 and later support specific OIDs for use with the direct OID request interface. OIDs that existed before NDIS 6.1 and some NDIS 6.1 OIDs are not supported. To determine if an OID can be used in the direct OIDs interface, see the OID reference page. For example, see the note in the [OID\_TCP\_TASK\_IPSEC\_OFFLOAD\_V2\_ADD\_SA](https://msdn.microsoft.com/library/windows/hardware/ff569812) OID.

 

Filter drivers must be able to handle direct OID requests that are not serialized. Unlike the standard OID request interface, NDIS does not serialize direct OID requests with other requests that are sent with the direct OID interface or with the standard OID request interface. Also, filter drivers must be able to handle direct OID requests at IRQL &lt;= DISPATCH\_LEVEL.

To support the direct OIDs request interface, use the documentation for the standard OID request interface. The following table shows the relationship between the functions in the direct OID request interface and the standard OID request interface.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Direct OID function</th>
<th align="left">Standard OID function</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>[<em>FilterDirectOidRequest</em>](https://msdn.microsoft.com/library/windows/hardware/ff549931)</p></td>
<td align="left"><p>[<em>FilterOidRequest</em>](https://msdn.microsoft.com/library/windows/hardware/ff549954)</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<em>FilterCancelDirectOidRequest</em>](https://msdn.microsoft.com/library/windows/hardware/ff549908)</p></td>
<td align="left"><p>[<em>FilterCancelOidRequest</em>](https://msdn.microsoft.com/library/windows/hardware/ff549911)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<em>FilterDirectOidRequestComplete</em>](https://msdn.microsoft.com/library/windows/hardware/ff549933)</p></td>
<td align="left"><p>[<em>FilterOidRequestComplete</em>](https://msdn.microsoft.com/library/windows/hardware/ff549956)</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>NdisFDirectOidRequest</strong>](https://msdn.microsoft.com/library/windows/hardware/ff561809)</p></td>
<td align="left"><p>[<strong>NdisFOidRequest</strong>](https://msdn.microsoft.com/library/windows/hardware/ff561830)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>NdisFDirectOidRequestComplete</strong>](https://msdn.microsoft.com/library/windows/hardware/ff561815)</p></td>
<td align="left"><p>[<strong>NdisFDirectOidRequestComplete</strong>](https://msdn.microsoft.com/library/windows/hardware/ff561815)</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>NdisFCancelDirectOidRequest</strong>](https://msdn.microsoft.com/library/windows/hardware/ff561788)</p></td>
<td align="left"><p>[<strong>NdisFCancelOidRequest</strong>](https://msdn.microsoft.com/library/windows/hardware/ff561792)</p></td>
</tr>
</tbody>
</table>

 

 

 





