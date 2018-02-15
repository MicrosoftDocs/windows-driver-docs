---
title: NdisOidComplete rule (ndis)
description: The NdisOidComplete rule verifies that an NDIS miniport driver completes an OID correctly.
ms.assetid: 344DECA8-F72A-4962-80D0-DDC648A4FC21
keywords: ["NdisOidComplete rule (ndis)"]
topic_type:
- apiref
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

 

A miniport driver must not call the [**NdisMOidRequestComplete**](https://msdn.microsoft.com/library/windows/hardware/ff563622) function with the final status of the request operation as NDIS\_STATUS\_PENDING.

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

 

|              |      |
|--------------|------|
| Driver model | NDIS |

|                                   |                                                                                                                                       |
|-----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| Bug check(s) found with this rule | [**Bug Check 0xC4: DRIVER\_VERIFIER\_DETECTED\_VIOLATION**](https://msdn.microsoft.com/library/windows/hardware/ff560187) (0x00091001) |

How to test
-----------

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
<td align="left"><p>Run [Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff545448) and select the [NDIS/WIFI verification](https://msdn.microsoft.com/library/windows/hardware/dn312128) option. This rule is also tested with the [DDI compliance checking](https://msdn.microsoft.com/library/windows/hardware/hh454208) option.</p></td>
</tr>
</tbody>
</table>

 

Applies to
----------

[**MiniportDevicePnPEventNotify**](https://msdn.microsoft.com/library/windows/hardware/ff559369)
[**MiniportOidRequest**](https://msdn.microsoft.com/library/windows/hardware/ff559416)
[**NdisMOidRequestComplete**](https://msdn.microsoft.com/library/windows/hardware/ff563622)
 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevtest\devtest%5D:%20NdisOidComplete%20rule%20%28ndis%29%20%20RELEASE:%20%281/17/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




