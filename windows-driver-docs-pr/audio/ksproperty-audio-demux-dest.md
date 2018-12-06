---
title: KSPROPERTY\_AUDIO\_DEMUX\_DEST
description: The KSPROPERTY\_AUDIO\_DEMUX\_DEST property specifies the destination stream to which a demultiplexer directs its input stream. This is a property of a DEMUX node (KSNODETYPE\_DEMUX).
ms.assetid: 431918da-2267-4fe5-a002-12d16b5f0984
keywords: ["KSPROPERTY_AUDIO_DEMUX_DEST Audio Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_AUDIO_DEMUX_DEST
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_AUDIO\_DEMUX\_DEST


The KSPROPERTY\_AUDIO\_DEMUX\_DEST property specifies the destination stream to which a demultiplexer directs its input stream. This is a property of a DEMUX node ([**KSNODETYPE\_DEMUX**](ksnodetype-demux.md)).

## <span id="ddk_ksproperty_audio_demux_dest_ks"></span><span id="DDK_KSPROPERTY_AUDIO_DEMUX_DEST_KS"></span>


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
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff537143" data-raw-source="[&lt;strong&gt;KSNODEPROPERTY&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff537143)"><strong>KSNODEPROPERTY</strong></a></p></td>
<td align="left"><p>ULONG</p></td>
</tr>
</tbody>
</table>

 

The property value (operation data) is of type ULONG. This value is the pin ID of the selected output pin on the DEMUX node.

### <span id="Return_Value"></span><span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

A KSPROPERTY\_AUDIO\_DEMUX\_DEST property request returns STATUS\_SUCCESS to indicate that it has completed successfully. Otherwise, the request returns an appropriate error status code.

Remarks
-------

The pin ID identifies a logical pin on the DEMUX node. For a discussion of pin IDs for logical pins on a node inside a filter, see [**PCCONNECTION\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/ff537688).

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


[**KSNODETYPE\_DEMUX**](ksnodetype-demux.md)

[**KSNODEPROPERTY**](https://msdn.microsoft.com/library/windows/hardware/ff537143)

[**PCCONNECTION\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/ff537688)

 

 






