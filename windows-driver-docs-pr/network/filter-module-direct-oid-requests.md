---
title: Filter Module Direct OID Requests
description: Filter Module Direct OID Requests
ms.assetid: 0ab7079b-6578-4932-a276-40a961b55efe
keywords:
- direct OID request interface WDK networking
- direct OID request path WDK networking
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Filter Module Direct OID Requests





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
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff549931" data-raw-source="[&lt;em&gt;FilterDirectOidRequest&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff549931)"><em>FilterDirectOidRequest</em></a></p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff549954" data-raw-source="[&lt;em&gt;FilterOidRequest&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff549954)"><em>FilterOidRequest</em></a></p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff549908" data-raw-source="[&lt;em&gt;FilterCancelDirectOidRequest&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff549908)"><em>FilterCancelDirectOidRequest</em></a></p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff549911" data-raw-source="[&lt;em&gt;FilterCancelOidRequest&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff549911)"><em>FilterCancelOidRequest</em></a></p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff549933" data-raw-source="[&lt;em&gt;FilterDirectOidRequestComplete&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff549933)"><em>FilterDirectOidRequestComplete</em></a></p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff549956" data-raw-source="[&lt;em&gt;FilterOidRequestComplete&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff549956)"><em>FilterOidRequestComplete</em></a></p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff561809" data-raw-source="[&lt;strong&gt;NdisFDirectOidRequest&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff561809)"><strong>NdisFDirectOidRequest</strong></a></p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff561830" data-raw-source="[&lt;strong&gt;NdisFOidRequest&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff561830)"><strong>NdisFOidRequest</strong></a></p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff561815" data-raw-source="[&lt;strong&gt;NdisFDirectOidRequestComplete&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff561815)"><strong>NdisFDirectOidRequestComplete</strong></a></p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff561815" data-raw-source="[&lt;strong&gt;NdisFDirectOidRequestComplete&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff561815)"><strong>NdisFDirectOidRequestComplete</strong></a></p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff561788" data-raw-source="[&lt;strong&gt;NdisFCancelDirectOidRequest&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff561788)"><strong>NdisFCancelDirectOidRequest</strong></a></p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff561792" data-raw-source="[&lt;strong&gt;NdisFCancelOidRequest&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff561792)"><strong>NdisFCancelOidRequest</strong></a></p></td>
</tr>
</tbody>
</table>

 

 

 





