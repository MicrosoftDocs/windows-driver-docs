---
title: KSPROPERTY\_JACK\_DESCRIPTION2
description: The KSPROPERTY\_JACK\_DESCRIPTION2 property is implemented as a pin-wise property that is accessed by using the filter handle.
ms.assetid: 6856060b-f735-4ed8-99bd-5896c87d581f
keywords: ["KSPROPERTY_JACK_DESCRIPTION2 Audio Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_JACK_DESCRIPTION2
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_JACK\_DESCRIPTION2


The KSPROPERTY\_JACK\_DESCRIPTION2 property is implemented as a pin-wise property that is accessed by using the filter handle.

In Windows 7 and later Windows operating systems, this property can be supported on any bridge pin that is associated with one or more physical jacks. KSPROPERTY\_JACK\_DESCRIPTION2 is used to get the state and the jack-related capabilities of the device.

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
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff566722" data-raw-source="[&lt;strong&gt;KSP_PIN&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff566722)"><strong>KSP_PIN</strong></a></p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff563441.aspx" data-raw-source="[&lt;strong&gt;KSMULTIPLE_ITEM&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff563441.aspx)"><strong>KSMULTIPLE_ITEM</strong></a> followed by an array of <a href="ksjack-description2.md" data-raw-source="[&lt;strong&gt;KSJACK_DESCRIPTION2&lt;/strong&gt;](ksjack-description2.md)"><strong>KSJACK_DESCRIPTION2</strong></a> structures</p></td>
</tr>
</tbody>
</table>

 

The property value (instance data) is a KSMULTIPLE\_ITEM, followed by an array of KSJACK\_DESCRIPTION2 structures.

### <span id="Return_Value"></span><span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

A KSPROPERTY\_JACK\_DESCRIPTION2 property request returns a KSMULTIPLE\_ITEM followed by an array of *N* KSJACK\_DESCRIPTION2 structures, where *N* = the number of jacks that are associated with the specified bridge pin. The following list shows the items that are returned by the property request.

KSMULTIPLE\_ITEM.Size = sizeof(KSMULTIPLE\_ITEM) + N \* sizeof(KSJACK\_DESCRIPTION2)

KSMULTIPLE\_ITEM.Count = N

KSJACK\_DESCRIPTION2\[0\]

...

KSJACK\_DESCRIPTION2\[N-1\]

Remarks
-------

Each KSJACK\_DESCRIPTION2 structure must only contain information about one jack.

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


[**KSJACK\_DESCRIPTION2**](ksjack-description2.md)

[KSMULTIPLE\_ITEM](https://msdn.microsoft.com/library/windows/hardware/ff563441.aspx)

 

 






