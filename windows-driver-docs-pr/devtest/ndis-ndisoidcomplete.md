---
title: NdisOidComplete Rule (NDIS)
description: The NdisOidComplete rule verifies that an NDIS miniport driver completes an OID correctly.
ms.date: 05/21/2018
keywords: ["NdisOidComplete rule (ndis)"]
topic_type:
- apiref
ms.topic: reference
api_name:
- NdisOidComplete
api_type:
- NA
---

# NdisOidComplete rule (ndis)


The **NdisOidComplete** rule verifies that an NDIS miniport driver completes an OID correctly.

The miniport driver must complete the OID request operations with the allowable NTSTATUS values.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">If the OID is:</th>
<th align="left">Can only be completed with the following NTSTATUS values:</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>OID_PNP_SET_POWER</p></td>
<td align="left"><p>NDIS_STATUS_NOT_ACCEPTED</p>
<p>NDIS_STATUS_SUCCESS</p>
<p>NDIS_STATUS_PENDING</p></td>
</tr>
<tr class="even">
<td align="left"><p>OID_RECEIVE_FILTER_CLEAR_FILTER</p>
<p>OID_TCP_TASK_IPSEC_OFFLOAD_V2_DELETE_SA</p>
<p>OID_RECEIVE_FILTER_FREE_QUEUE</p>
<p>OID_NIC_SWITCH_FREE_VF</p>
<p>OID_NIC_SWITCH_DELETE_SWITCH</p>
<p>OID_802_3_DELETE_MULTICAST_ADDRESS</p>
<p>OID_PM_REMOVE_WOL_PATTERN</p>
<p>OID_PM_REMOVE_PROTOCOL_OFFLOAD</p>
<p>OID_TUNNEL_INTERFACE_RELEASE_OID</p></td>
<td align="left"><p>NDIS_STATUS_NOT_ACCEPTED</p>
<p>NDIS_STATUS_REQUEST_ABORTED</p>
<p>NDIS_STATUS_SUCCESS</p>
<p>NDIS_STATUS_PENDING</p></td>
</tr>
</tbody>
</table>

 

A miniport driver must not call the [**NdisMOidRequestComplete**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismoidrequestcomplete) function with the final status of the request operation as NDIS\_STATUS\_PENDING.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">In addition, if the OID is:</th>
<th align="left">Can only be completed with the following NTSTATUS values:</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>OID_PNP_SET_POWER</p></td>
<td align="left"><p>NDIS_STATUS_NOT_ACCEPTED</p>
<p>NDIS_STATUS_SUCCESS</p></td>
</tr>
<tr class="even">
<td align="left"><p>OID_RECEIVE_FILTER_CLEAR_FILTER</p>
<p>OID_TCP_TASK_IPSEC_OFFLOAD_V2_DELETE_SA</p>
<p>OID_RECEIVE_FILTER_FREE_QUEUE</p>
<p>OID_NIC_SWITCH_FREE_VF</p>
<p>OID_NIC_SWITCH_DELETE_SWITCH</p>
<p>OID_802_3_DELETE_MULTICAST_ADDRESS</p>
<p>OID_PM_REMOVE_WOL_PATTERN</p>
<p>OID_PM_REMOVE_PROTOCOL_OFFLOAD</p>
<p>OID_TUNNEL_INTERFACE_RELEASE_OID</p></td>
<td align="left"><p>NDIS_STATUS_NOT_ACCEPTED</p>
<p>NDIS_STATUS_REQUEST_ABORTED</p>
<p>NDIS_STATUS_SUCCESS</p></td>
</tr>
</tbody>
</table>

 

**Driver model: NDIS**

**Bug check(s) found with this rule**: [**Bug Check 0xC4: DRIVER\_VERIFIER\_DETECTED\_VIOLATION**](../debugger/bug-check-0xc4--driver-verifier-detected-violation.md) (0x00091001)


## How to test

<table>
<colgroup>
<col width="100%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">At run time</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Run <a href="/windows-hardware/drivers/devtest/driver-verifier" data-raw-source="[Driver Verifier](./driver-verifier.md)">Driver Verifier</a> and select the <a href="/windows-hardware/drivers/devtest/ndis-wifi-verification" data-raw-source="[NDIS/WIFI verification](./ndis-wifi-verification.md)">NDIS/WIFI verification</a> option. This rule is also tested with the <a href="/windows-hardware/drivers/devtest/ddi-compliance-checking" data-raw-source="[DDI compliance checking](./ddi-compliance-checking.md)">DDI compliance checking</a> option.</p></td>
</tr>
</tbody>
</table>

 

## Applies to

[**MiniportDevicePnPEventNotify**](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_device_pnp_event_notify)
[**MiniportOidRequest**](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_oid_request)
[**NdisMOidRequestComplete**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismoidrequestcomplete)
