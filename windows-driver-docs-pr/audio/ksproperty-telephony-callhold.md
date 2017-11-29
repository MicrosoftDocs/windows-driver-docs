---
title: KSPROPERTY\_TELEPHONY\_CALLHOLD
description: The KSPROPERTY\_TELEPHONY\_CALLHOLD property is used to control the hold state of a phone call.
ms.assetid: C683A6AA-35E5-43D3-B882-B13B8A0A4043
keywords: ["KSPROPERTY_TELEPHONY_CALLHOLD Audio Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_TELEPHONY_CALLHOLD
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

# KSPROPERTY\_TELEPHONY\_CALLHOLD


The **KSPROPERTY\_TELEPHONY\_CALLHOLD** property is used to control the hold state of a phone call.

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
<td align="left"><p>Yes</p></td>
<td align="left"><p>Yes</p></td>
<td align="left"><p>Filter</p></td>
<td align="left"><p>[<strong>KSPROPERTY</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564262)</p></td>
<td align="left"><p>BOOL</p></td>
</tr>
</tbody>
</table>

 

The property value is of type BOOL and specifies whether the phone call is on hold.

### <span id="Return_Value"></span><span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

A **KSPROPERTY\_TELEPHONY\_CALLHOLD** property request returns **TRUE** if the call in on hold; otherwise, it returns **FALSE**.

Remarks
-------

If you set the **KSPROPERTY\_TELEPHONY\_CALLHOLD** property with a value of **TRUE**, the phone call will be placed on hold. The expected behavior is that both transmission and reception will be muted. No data will be sent or received in this case. The audio driver will update the call state ([**TELEPHONY\_CALLSTATE**](https://msdn.microsoft.com/library/windows/hardware/mt169896)) to **TELEPHONY\_CALLSTATE\_HOLD**. If you set the **KSPROPERTY\_TELEPHONY\_CALLHOLD** property with a value of **FALSE**, the phone call will be taken off of hold state, and the call state will be updated to **TELEPHONY\_CALLSTATE\_ENABLED**.

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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20KSPROPERTY_TELEPHONY_CALLHOLD%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




