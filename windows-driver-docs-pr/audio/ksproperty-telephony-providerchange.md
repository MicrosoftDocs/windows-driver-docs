---
title: KSPROPERTY\_TELEPHONY\_PROVIDERCHANGE
description: The KSPROPERTY\_TELEPHONY\_PROVIDERCHANGE property is used to communicate to the audio driver that single-radio voice call continuity (SRVCC) is beginning or ending.
ms.assetid: 9CEDAFE7-014F-4670-958D-6D3687D2D24A
keywords: ["KSPROPERTY_TELEPHONY_PROVIDERCHANGE Audio Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_TELEPHONY_PROVIDERCHANGE
api_location:
- ksmedia.h
api_type:
- HeaderDef
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# KSPROPERTY\_TELEPHONY\_PROVIDERCHANGE


The **KSPROPERTY\_TELEPHONY\_PROVIDERCHANGE** property is used to communicate to the audio driver that single-radio voice call continuity (SRVCC) is beginning or ending.

### <span id="Usage_Summary_Table"></span><span id="usage_summary_table"></span><span id="USAGE_SUMMARY_TABLE"></span>Usage Summary Table

<table>
<colgroup>
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Get</th>
<th align="left">Set</th>
<th align="left">Target</th>
<th align="left">Property descriptor type</th>
<th align="left">Property value type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>No</p></td>
<td align="left"><p>Yes</p></td>
<td align="left"><p>Filter</p></td>
<td align="left"><p>[<strong>KSPROPERTY</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564262)</p></td>
<td align="left"><p>[<strong>KSTELEPHONY_PROVIDERCHANGE</strong>](https://msdn.microsoft.com/library/windows/hardware/mt169885)</p></td>
</tr>
</tbody>
</table>

 

The property value is of type [**KSTELEPHONY\_PROVIDERCHANGE**](https://msdn.microsoft.com/library/windows/hardware/mt169885), which specifies the phone call type and the type of provider change operation.

### <span id="Return_Value"></span><span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

A **KSPROPERTY\_TELEPHONY\_PROVIDERCHANGE** property request returns STATUS\_SUCCESS to indicate that it has completed successfully. Otherwise, the request returns an appropriate error status code.

Remarks
-------

The audio stack uses the [**KSTELEPHONY\_PROVIDERCHANGE**](https://msdn.microsoft.com/library/windows/hardware/mt169885) property to indicate the start and the end of SRVCC to the audio driver. This property communicates the call type (LTE packet-switched, WLAN packet-switched, or circuit-switched) and the provider change operation (begin, end, or cancel) to driver. The call type is ignored when the provider operation is for ending the SRVCC.

When the provider change operation is **TELEPHONY\_PROVIDERCHANGEOP\_BEGIN**, the driver updates that provider’s call state to **TELEPHONY\_CALLSTATE\_PROVIDERTRANSITION**. When the provider change operation is **TELEPHONY\_PROVIDERCHANGEOP\_END**, the driver updates that provider’s call state to **TELEPHONY\_CALLSTATE\_ENABLED**. During SRVCC, the driver must continue to use the associated [**KSNODETYPE\_TELEPHONY\_BIDI**](ksnodetype-telephony-bidi.md) endpoint, and it does not change the jack states of this endpoint. When the provider change operation is **TELEPHONY\_PROVIDERCHANGEOP\_CANCEL**, SRVCC is being canceled, and the driver should revert back to a pre-SRVCC call.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Minimum supported client</p></td>
<td align="left"><p>Windows 10</p></td>
</tr>
<tr class="even">
<td align="left"><p>Minimum supported server</p></td>
<td align="left"><p>None supported</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Client</p></td>
<td align="left"><p>Windows 10 Mobile</p></td>
</tr>
<tr class="even">
<td align="left"><p>Header</p></td>
<td align="left">Ksmedia.h</td>
</tr>
</tbody>
</table>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20KSPROPERTY_TELEPHONY_PROVIDERCHANGE%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




