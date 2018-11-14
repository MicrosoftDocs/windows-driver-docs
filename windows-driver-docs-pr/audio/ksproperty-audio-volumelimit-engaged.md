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
ms.date: 11/28/2017
ms.localizationpriority: medium
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

 

 





