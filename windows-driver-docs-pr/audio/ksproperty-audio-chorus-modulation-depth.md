---
title: KSPROPERTY\_AUDIO\_CHORUS\_MODULATION\_DEPTH
description: The KSPROPERTY\_AUDIO\_CHORUS\_MODULATION\_DEPTH property specifies the chorus modulation depth. This is a property of a chorus node (KSNODETYPE\_CHORUS).
ms.assetid: A14DA707-7ED6-4E86-87C7-9A4E40062FE8
keywords: ["KSPROPERTY_AUDIO_CHORUS_MODULATION_DEPTH Audio Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_AUDIO_CHORUS_MODULATION_DEPTH
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

# KSPROPERTY\_AUDIO\_CHORUS\_MODULATION\_DEPTH


The KSPROPERTY\_AUDIO\_CHORUS\_MODULATION\_DEPTH property specifies the chorus modulation depth. This is a property of a chorus node ([**KSNODETYPE\_CHORUS**](ksnodetype-chorus.md)).

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
<td align="left"><p>KSNODEPROPERTY</p></td>
<td align="left"><p>ULONG</p></td>
</tr>
</tbody>
</table>

 

The property value is of type ULONG and it specifies the chorus modulation depth. It is expressed in milliseconds and sets the speed (frequency) of the modulator. The value can range from 0 to 255.9961 in 1/256th increments. To accommodate this, the property value should be expressed as a fixed point 16.16 value, where the following is true:

-   The value 0x00010000 represents 1 ms
-   The value 0xFFFFFFFF represents (65536-1/65536) ms

### <span id="Return_Value"></span><span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

A KSPROPERTY\_AUDIO\_CHORUS\_MODULATION\_DEPTH property request returns STATUS\_SUCCESS to indicate that it has completed successfully. Otherwise, the request returns an appropriate error status code.

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
<td align="left"><p>Windows Vista</p></td>
</tr>
<tr class="even">
<td align="left"><p>Header</p></td>
<td align="left">Ksmedia.h</td>
</tr>
</tbody>
</table>

## <span id="see_also"></span>See also


[**KSNODETYPE\_CHORUS**](ksnodetype-chorus.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20KSPROPERTY_AUDIO_CHORUS_MODULATION_DEPTH%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





