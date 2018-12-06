---
title: KSPROPERTY\_AUDIOENGINE\_DEVICEFORMAT
description: The KSPROPERTY\_AUDIOENGINE\_DEVICEFORMAT property request retrieves or alters the state of the audio engine node, regarding its device format setting.
ms.assetid: 07821ACC-F561-4A40-9E2C-CB30B25521CB
keywords: ["KSPROPERTY_AUDIOENGINE_DEVICEFORMAT Audio Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_AUDIOENGINE_DEVICEFORMAT
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_AUDIOENGINE\_DEVICEFORMAT


The **KSPROPERTY\_AUDIOENGINE\_DEVICEFORMAT** property request retrieves or alters the state of the audio engine node, regarding its device format setting.

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
<td align="left"><p>Node via filter</p></td>
<td align="left"><p>KSP_NODE</p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff561656" data-raw-source="[&lt;strong&gt;KSDATAFORMAT&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff561656)"><strong>KSDATAFORMAT</strong></a></p></td>
</tr>
</tbody>
</table>

 

### <span id="Return_Value"></span><span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

The **KSPROPERTY\_AUDIOENGINE\_DEVICEFORMAT** property request returns **STATUS\_SUCCESS** to indicate that it has completed successfully. Otherwise, the request returns an appropriate error status code.

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
<td align="left"><p>Windows 8</p></td>
</tr>
<tr class="even">
<td align="left"><p>Header</p></td>
<td align="left">Ksmedia.h</td>
</tr>
</tbody>
</table>

## <span id="see_also"></span>See also


[**KSDATAFORMAT**](https://msdn.microsoft.com/library/windows/hardware/ff561656)

[**KSPROPERTY\_AUDIOENGINE**](ksproperty-audioengine.md)

 

 






