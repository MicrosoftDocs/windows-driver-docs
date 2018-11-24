---
title: KSPROPERTY\_AUDIO\_WIDENESS
description: The KSPROPERTY\_AUDIO\_WIDENESS property specifies the wideness (apparent width) of the stereo image.
ms.assetid: 56b18337-c29b-437f-b52f-8d804d857729
keywords: ["KSPROPERTY_AUDIO_WIDENESS Audio Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_AUDIO_WIDENESS
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_AUDIO\_WIDENESS


The KSPROPERTY\_AUDIO\_WIDENESS property specifies the wideness (apparent width) of the stereo image.

## <span id="ddk_ksproperty_audio_wideness_ks"></span><span id="DDK_KSPROPERTY_AUDIO_WIDENESS_KS"></span>


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
<td align="left"><a href="https://msdn.microsoft.com/library/windows/hardware/ff537143" data-raw-source="[&lt;strong&gt;KSNODEPROPERTY&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff537143)"><strong>KSNODEPROPERTY</strong></a></td>
<td align="left"><p>ULONG</p></td>
</tr>
</tbody>
</table>

 

The property value (operation data) is of type ULONG and specifies the wideness. Wideness is expressed as an unsigned, fixed-point value with a 16-bit fraction. Wideness values follow a linear range from zero to 0xFFFFFFFF:

-   The value 0x00010000 represents unity (100 percent), which indicates that the width of the stereo image should coincide with the region that is framed by the left and right speakers.

-   For a value greater than unity, the stereo image should appear to extend outside the region that is framed by the left and right speakers.

-   For a value less than unity, the perceived width of the stereo image should be smaller than the space between the left and right speakers.

-   A value of zero indicates that the sound should appear to originate from a position midway between the left and right speakers.

The apparent width of the stereo image should increase linearly with linear increases in the wideness value.

### <span id="Return_Value"></span><span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

A KSPROPERTY\_AUDIO\_WIDENESS property request returns STATUS\_SUCCESS to indicate that it has completed successfully. Otherwise, the request returns an appropriate error status code.

Remarks
-------

This is a property of a wideness node ([**KSNODETYPE\_STEREO\_WIDE**](ksnodetype-stereo-wide.md)). A wideness node can add spaciousness to an existing stereo (two-channel) stream. To achieve this effect, the node processes the stream to make some sounds appear to originate from positions outside the region that is framed by the left and right speakers.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Header</p></td>
<td align="left">Ksmedia.h (include Ksmedia.h)</td>
</tr>
</tbody>
</table>

## <span id="see_also"></span>See also


[**KSNODEPROPERTY**](https://msdn.microsoft.com/library/windows/hardware/ff537143)

[**KSNODETYPE\_STEREO\_WIDE**](ksnodetype-stereo-wide.md)

 

 






