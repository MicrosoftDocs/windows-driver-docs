---
title: KSPROPERTY\_AUDIO\_VOLUMELIMIT\_ENGAGED
description: KSPROPERTY\_AUDIO\_VOLUMELIMIT\_ENGAGED, is a new KS property that has been added into the KSPROPSETID\_Audio property set in Windows 8.1.
ms.assetid: 0DAC584A-EC17-4280-B90D-2D9DDB620479
keywords: ["KSPROPERTY_AUDIO_VOLUMELIMIT_ENGAGED Audio Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_AUDIO_VOLUMELIMIT_ENGAGED
api_location:
- Ksmedia.h
api_type:
- HeaderDef
---

# KSPROPERTY\_AUDIO\_VOLUMELIMIT\_ENGAGED


KSPROPERTY\_AUDIO\_VOLUMELIMIT\_ENGAGED, is a new KS property that has been added into the KSPROPSETID\_Audio property set in Windows 8.1.

The KSPROPERTY\_AUDIO\_VOLUMELIMIT\_ENGAGED property request passes an end user’s volume level limit preference to the underlying driver. The scope of this property is per pin (or per audio endpoint, from an end-user’s point of view).

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
<td align="left"><p>Pin instance</p></td>
<td align="left"><p>KSP_PIN</p></td>
<td align="left"><p>BOOL</p></td>
</tr>
</tbody>
</table>

 

The property value is of type BOOL, and it indicates whether an end-user allows the max volume to be over a certain limit. A value of TRUE indicates that an end-user has allowed the volume level to be over the posted limit, whereas FALSE indicates the opposite. In the case of a child account, the value will always be FALSE.

The driver stores the value of this property in an internal variable and initializes the value to TRUE during startup. While this property is TRUE, the driver limits the maximum volume level. When the property is set to FALSE the driver can remove these limits.

The driver can also change the value of this property automatically. For example, the driver can automatically switch the property value from TRUE to FALSE, and then begin limiting the volume level after some amount of time above certain sound levels has elapsed.

Whenever the value of the property changes, regardless of whether it is automatic or due to a caller setting the property value, the driver should generate the KSEVENT\_PINCAPS\_VOLUMELIMITCHANGE event.

### <span id="Return_Value"></span><span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

The KSPROPERTY\_AUDIO\_VOLUMELIMIT\_ENGAGED property request returns STATUS\_SUCCESS when the request is successful.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Version</p></td>
<td align="left"><p>Windows 8.1</p></td>
</tr>
<tr class="even">
<td align="left"><p>Header</p></td>
<td align="left">Ksmedia.h (include Ksmedia.h)</td>
</tr>
</tbody>
</table>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20KSPROPERTY_AUDIO_VOLUMELIMIT_ENGAGED%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




