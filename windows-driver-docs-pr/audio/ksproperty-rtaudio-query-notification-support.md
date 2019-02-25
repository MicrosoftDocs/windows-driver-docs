---
title: KSPROPERTY\_RTAUDIO\_QUERY\_NOTIFICATION\_SUPPORT
description: The client application uses the KSPROPERTY\_RTAUDIO\_QUERY\_NOTIFICATION\_SUPPORT property to determine whether the audio driver can notify the client application when a process that is performed on the submitted buffer is completed.
ms.assetid: 7e0910df-4b76-4e61-9f88-8953860f3abe
keywords: ["KSPROPERTY_RTAUDIO_QUERY_NOTIFICATION_SUPPORT Audio Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_RTAUDIO_QUERY_NOTIFICATION_SUPPORT
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_RTAUDIO\_QUERY\_NOTIFICATION\_SUPPORT


The client application uses the `KSPROPERTY_RTAUDIO_QUERY_NOTIFICATION_SUPPORT` property to determine whether the audio driver can notify the client application when a process that is performed on the submitted buffer is completed.

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
<td align="left"><p>Pin</p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff564262" data-raw-source="[&lt;strong&gt;KSPROPERTY&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564262)"><strong>KSPROPERTY</strong></a></p></td>
<td align="left"><p>BOOL</p></td>
</tr>
</tbody>
</table>

 

The property value is a variable of type BOOL.

### <span id="Return_Value"></span><span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

In response to a `KSPROPERTY_RTAUDIO_QUERY_NOTIFICATION_SUPPORT` property request, the driver returns a **TRUE** or **FALSE** value. This value depends on whether the driver supports the property.

Remarks
-------

None

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
<td align="left"><p>Available in Windows 7 and later versions of the Windows operating systems.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Header</p></td>
<td align="left">Ksmedia.h (include Ksmedia.h)</td>
</tr>
</tbody>
</table>

## <span id="see_also"></span>See also


[**KSPROPERTY**](https://msdn.microsoft.com/library/windows/hardware/ff564262)

 

 






