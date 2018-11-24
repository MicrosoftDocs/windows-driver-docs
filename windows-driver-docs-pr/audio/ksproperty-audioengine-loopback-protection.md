---
title: KSPROPERTY\_AUDIOENGINE\_LOOPBACK\_PROTECTION
description: The KSPROPERTY\_AUDIOENGINE\_LOOPBACK\_PROTECTION property request allows the audio driver to set the loopback protection status of the audio engine node.
ms.assetid: E798582C-7662-413C-B25C-6A129FDEEE38
keywords: ["KSPROPERTY_AUDIOENGINE_LOOPBACK_PROTECTION Audio Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_AUDIOENGINE_LOOPBACK_PROTECTION
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_AUDIOENGINE\_LOOPBACK\_PROTECTION


The **KSPROPERTY\_AUDIOENGINE\_LOOPBACK\_PROTECTION** property request allows the audio driver to set the loopback protection status of the audio engine node.

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
<td align="left"><p>Node via Pin instance</p></td>
<td align="left"><p>KSP_NODE</p></td>
<td align="left"><p>ULONG</p></td>
</tr>
</tbody>
</table>

 

### <span id="Return_Value"></span><span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

The KSPROPERTY\_AUDIOENGINE\_LOOPBACK\_PROTECTION property request returns STATUS\_SUCCESS to indicate that it has completed successfully. Otherwise, the request returns an appropriate error status code.

Remarks
-------

The input buffer that is associated with this property call is populated with an enumeration value of type CONSTRICTOR\_OPTION. So the input buffer is either set to CONSTRICTOR\_OPTION\_DISABLE or CONSTRICTOR\_OPTION\_MUTE.

If there are any active streams with CONSTRICTOR\_OPTION\_MUTE in effect, then the KS loopback tap for this audio output will emit silence. If all the active streams have CONSTRICTOR\_OPTION\_DISABLE in effect (which is the default state), then and only then does the loopback tap contain meaningful data.

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


[**KSPROPERTY\_AUDIOENGINE**](ksproperty-audioengine.md)

 

 






