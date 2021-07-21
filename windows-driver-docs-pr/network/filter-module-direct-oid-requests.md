---
title: Filter Module Direct OID Requests
description: Filter Module Direct OID Requests
keywords:
- direct OID request interface WDK networking
- direct OID request path WDK networking
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Filter Module Direct OID Requests





To support the direct OID request path, filter drivers provide *FilterXxx* function entry points in the [**NDIS\_FILTER\_DRIVER\_CHARACTERISTICS**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_filter_driver_characteristics) structure and NDIS provides **NdisF*Xxx*** functions for filter drivers.

The *direct OID request interface* is similar to the standard OID request interface. For example, the [**NdisFDirectOidRequest**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisfdirectoidrequest) and [*FilterDirectOidRequest*](/windows-hardware/drivers/ddi/ndis/nc-ndis-filter_direct_oid_request) functions are similar to the [**NdisFOidRequest**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisfoidrequest) and [*FilterOidRequest*](/windows-hardware/drivers/ddi/ndis/nc-ndis-filter_oid_request) functions.

**Note**  NDIS 6.1 and later support specific OIDs for use with the direct OID request interface. OIDs that existed before NDIS 6.1 and some NDIS 6.1 OIDs are not supported. To determine if an OID can be used in the direct OIDs interface, see the OID reference page. For example, see the note in the [OID\_TCP\_TASK\_IPSEC\_OFFLOAD\_V2\_ADD\_SA](./oid-tcp-task-ipsec-offload-v2-add-sa.md) OID.

 

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
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ndis/nc-ndis-filter_direct_oid_request" data-raw-source="[&lt;em&gt;FilterDirectOidRequest&lt;/em&gt;](/windows-hardware/drivers/ddi/ndis/nc-ndis-filter_direct_oid_request)"><em>FilterDirectOidRequest</em></a></p></td>
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ndis/nc-ndis-filter_oid_request" data-raw-source="[&lt;em&gt;FilterOidRequest&lt;/em&gt;](/windows-hardware/drivers/ddi/ndis/nc-ndis-filter_oid_request)"><em>FilterOidRequest</em></a></p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ndis/nc-ndis-filter_cancel_direct_oid_request" data-raw-source="[&lt;em&gt;FilterCancelDirectOidRequest&lt;/em&gt;](/windows-hardware/drivers/ddi/ndis/nc-ndis-filter_cancel_direct_oid_request)"><em>FilterCancelDirectOidRequest</em></a></p></td>
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ndis/nc-ndis-filter_cancel_oid_request" data-raw-source="[&lt;em&gt;FilterCancelOidRequest&lt;/em&gt;](/windows-hardware/drivers/ddi/ndis/nc-ndis-filter_cancel_oid_request)"><em>FilterCancelOidRequest</em></a></p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ndis/nc-ndis-filter_direct_oid_request_complete" data-raw-source="[&lt;em&gt;FilterDirectOidRequestComplete&lt;/em&gt;](/windows-hardware/drivers/ddi/ndis/nc-ndis-filter_direct_oid_request_complete)"><em>FilterDirectOidRequestComplete</em></a></p></td>
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ndis/nc-ndis-filter_oid_request_complete" data-raw-source="[&lt;em&gt;FilterOidRequestComplete&lt;/em&gt;](/windows-hardware/drivers/ddi/ndis/nc-ndis-filter_oid_request_complete)"><em>FilterOidRequestComplete</em></a></p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisfdirectoidrequest" data-raw-source="[&lt;strong&gt;NdisFDirectOidRequest&lt;/strong&gt;](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisfdirectoidrequest)"><strong>NdisFDirectOidRequest</strong></a></p></td>
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisfoidrequest" data-raw-source="[&lt;strong&gt;NdisFOidRequest&lt;/strong&gt;](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisfoidrequest)"><strong>NdisFOidRequest</strong></a></p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisfdirectoidrequestcomplete" data-raw-source="[&lt;strong&gt;NdisFDirectOidRequestComplete&lt;/strong&gt;](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisfdirectoidrequestcomplete)"><strong>NdisFDirectOidRequestComplete</strong></a></p></td>
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisfdirectoidrequestcomplete" data-raw-source="[&lt;strong&gt;NdisFDirectOidRequestComplete&lt;/strong&gt;](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisfdirectoidrequestcomplete)"><strong>NdisFDirectOidRequestComplete</strong></a></p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisfcanceldirectoidrequest" data-raw-source="[&lt;strong&gt;NdisFCancelDirectOidRequest&lt;/strong&gt;](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisfcanceldirectoidrequest)"><strong>NdisFCancelDirectOidRequest</strong></a></p></td>
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisfcanceloidrequest" data-raw-source="[&lt;strong&gt;NdisFCancelOidRequest&lt;/strong&gt;](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisfcanceloidrequest)"><strong>NdisFCancelOidRequest</strong></a></p></td>
</tr>
</tbody>
</table>

 

