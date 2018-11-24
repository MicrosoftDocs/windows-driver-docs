---
title: KSPROPERTY\_JACK\_DESCRIPTION
description: The KSPROPERTY\_JACK\_DESCRIPTION property is implemented as a multi-item, pin-wise property that is accessed through the filter handle.
ms.assetid: 005c7edc-8eb2-4387-b818-edef9b9dd4ee
keywords: ["KSPROPERTY_JACK_DESCRIPTION Audio Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_JACK_DESCRIPTION
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_JACK\_DESCRIPTION


The KSPROPERTY\_JACK\_DESCRIPTION property is implemented as a multi-item, pin-wise property that is accessed through the filter handle.

In Windows Vista and later, this property can be supported on any bridge pin that is associated with one or more physical jacks. It is used to get a description of the physical characteristics and usage of a particular jack.

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
<td align="left"><p>No</p></td>
<td align="left"><p>Pin factory (via Filter handle)</p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff566722" data-raw-source="[&lt;strong&gt;KSP_PIN&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff566722)"><strong>KSP_PIN</strong></a></p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff563441.aspx" data-raw-source="[&lt;strong&gt;KSMULTIPLE_ITEM&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff563441.aspx)"><strong>KSMULTIPLE_ITEM</strong></a> followed by an array of <a href="ksjack-description.md" data-raw-source="[&lt;strong&gt;KSJACK_DESCRIPTION&lt;/strong&gt;](ksjack-description.md)"><strong>KSJACK_DESCRIPTION</strong></a> structures</p></td>
</tr>
</tbody>
</table>

 

The property value (instance data) is a KSMULTIPLE\_ITEM, followed by an array of KSJACK\_DESCRIPTION structures.

### <span id="Return_Value"></span><span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

A KSPROPERTY\_JACK\_DESCRIPTION property request returns a KSMULTIPLE\_ITEM followed by an array of *N* KSJACK\_DESCRIPTION structures, where *N* = the number of jacks associated with the specified bridge pin. The members returned by the property request would thus be:

KSMULTIPLE\_ITEM.Size = sizeof(KSMULTIPLE\_ITEM) + N \* sizeof(KSJACK\_DESCRIPTION)

KSMULTIPLE\_ITEM.Count = N

KSJACK\_DESCRIPTION\[0\]

...

KSJACK\_DESCRIPTION\[N-1\]

Remarks
-------

Each KSJACK\_DESCRIPTION structure must have information about one jack. For example, an output bridge pin that supports 5.1 audio over three stereo jacks, would require a data buffer of size

sizeof(KSMULTIPLE\_ITEM) + 3 \* sizeof(KSJACK\_DESCRIPTION)

and each KSJACK\_DESCRIPTION structure would have a two-bit ChannelMapping value.

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
<td align="left"><p>Windows Vista</p></td>
</tr>
<tr class="even">
<td align="left"><p>Minimum supported server</p></td>
<td align="left"><p>Windows Server 2003</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Header</p></td>
<td align="left">Ksmedia.h</td>
</tr>
</tbody>
</table>

## <span id="see_also"></span>See also


[**KSJACK\_DESCRIPTION**](ksjack-description.md)

[KSMULTIPLE\_ITEM](https://msdn.microsoft.com/library/windows/hardware/ff563441.aspx)

[KSPROPERTY](https://msdn.microsoft.com/library/windows/hardware/ff564262.aspx)

 

 






