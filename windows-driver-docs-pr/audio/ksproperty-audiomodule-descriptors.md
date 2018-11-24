---
title: KSPROPERTY\_AUDIOMODULE\_DESCRIPTORS
description: KSPROPERTY\_AUDIOMODULE\_DESCRIPTORS is used to retrieves the static data descriptor for each audio module on the endpoint wave filter.
ms.assetid: EAD613AA-005B-4751-B60E-212853CA40B4
keywords: ["KSPROPERTY_AUDIOMODULE_DESCRIPTORS Audio Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_AUDIOMODULE_DESCRIPTORS
api_type:
- NA
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_AUDIOMODULE\_DESCRIPTORS


**KSPROPERTY\_AUDIOMODULE\_DESCRIPTORS** is used to retrieves the static data descriptor for each audio module on the endpoint wave filter.

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
<td align="left"><p>Filter or Pin</p></td>
<td align="left"><p><strong>KSPROPERTY</strong></p></td>
<td align="left"><p>For filter target, a KSMULTIPLE_ITEM followed by an array of KSAUDIOMODULE_DESCRIPTOR that describe the template modules.</p>
<p>For pin target, a KSMULTIPLE_ITEM followed by an array of KSAUDIOMODULE_DESCRIPTOR for the instantiated modules in that stream path.</p></td>
</tr>
</tbody>
</table>

 

The property value is a structure, followed by zero (0) or more [**KSAUDIOMODULE\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/mt808137) structures.

### <span id="Return_Value"></span><span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

**KSPROPERTY\_AUDIOMODULE\_DESCRIPTORS** returns an array of these descriptors is returned in response to this request.

If the driver support this property but it doesn’t have any audio modules, it returns an ksmultiple\_item with zero element count.

For more information about audio modules, see [Implementing Audio Module Discovery](https://msdn.microsoft.com/windows/hardware/drivers/audio/implementing-audio-module-communication).

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
<td align="left"><p>Version</p></td>
<td align="left"><p>Windows 10, version 1703</p></td>
</tr>
</tbody>
</table>

## <span id="see_also"></span>See also


[**KSAUDIOMODULE\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/mt808137)

[KSPROPSETID\_AudioModule](kspropsetid-audiomodule.md)

 

 






