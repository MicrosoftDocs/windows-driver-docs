---
title: KSPROPERTY\_JACK\_SINK\_INFO
description: The KSPROPERTY\_JACK\_SINK\_INFO property is implemented as a pin-wise property that is accessed by using the filter handle.
keywords: ["KSPROPERTY_JACK_SINK_INFO Audio Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- KSPROPERTY_JACK_SINK_INFO
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 03/06/2023
---


# KSPROPERTY\_JACK\_SINK\_INFO


The KSPROPERTY\_JACK\_SINK\_INFO property is implemented as a pin-wise property that is accessed by using the filter handle.

In Windows 7 and later operating systems, this property can be supported on any bridge pin that is associated with one or more physical jacks. KSPROPERTY\_JACK\_SINK\_INFO is used to get the description and capabilities of a jack sink for a display-related digital audio device, such as an HDMI device or a display port.

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
<td align="left"><p>Pin factory (via filter handle)</p></td>
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ks/ns-ks-ksp_pin" data-raw-source="[&lt;strong&gt;KSP_PIN&lt;/strong&gt;](/windows-hardware/drivers/ddi/ks/ns-ks-ksp_pin)"><strong>KSP_PIN</strong></a></p></td>
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-_tagksjack_sink_information" data-raw-source="[&lt;strong&gt;KSJACK_SINK_INFORMATION&lt;/strong&gt;](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-_tagksjack_sink_information)"><strong>KSJACK_SINK_INFORMATION</strong></a></p></td>
</tr>
</tbody>
</table>

 

The property value (instance data) is a KSJACK\_SINK\_INFORMATION structure.

### <span id="Return_Value"></span><span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

A KSPROPERTY\_JACK\_SINK\_INFO property request returns information in a **KSJACK\_SINK\_INFORMATION** structure.

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Minimum supported client</p></td>
<td align="left"><p>Windows 7</p></td>
</tr>
<tr class="even">
<td align="left"><p>Minimum supported server</p></td>
<td align="left"><p>Windows Server 2008</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Header</p></td>
<td align="left">Ksmedia.h</td>
</tr>
</tbody>
</table>

## <span id="see_also"></span>See also


[**KSJACK\_SINK\_INFORMATION**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-_tagksjack_sink_information)

