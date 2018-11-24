---
title: KSPROPERTY\_AUDIO\_WAVERT\_CURRENT\_WRITE\_POSITION
description: The KSPROPERTY\_AUDIO\_WAVERT\_CURRENT\_WRITE\_POSITION property request specifies the current write position of the WaveRT buffer in bytes. The offload driver can use this write position information to know how much valid data is in the WaveRT buffer.
ms.assetid: 05C62E23-2460-4E92-BEE8-08D31A8BFD86
keywords: ["KSPROPERTY_AUDIO_WAVERT_CURRENT_WRITE_POSITION Audio Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_AUDIO_WAVERT_CURRENT_WRITE_POSITION
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_AUDIO\_WAVERT\_CURRENT\_WRITE\_POSITION


The KSPROPERTY\_AUDIO\_WAVERT\_CURRENT\_WRITE\_POSITION property request specifies the current write position of the WaveRT buffer in bytes. The offload driver can use this write position information to know how much valid data is in the WaveRT buffer.

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

The KSPROPERTY\_AUDIO\_WAVERT\_CURRENT\_WRITE\_POSITION property request returns STATUS\_SUCCESS to indicate that it has completed successfully. Otherwise, the request returns an appropriate error status code.

Remarks
-------

To better understand how to interpret the information provided by this property request, assume a circular buffer of size n bytes. The initial write position, before any data is written, is 0. Data is written to the buffer in chunks that are a multiple of [**WAVEFORMATEX.nBlockAlign**](https://msdn.microsoft.com/library/windows/hardware/ff538799) bytes.

For example, the buffer might contain 20 ms of 16-bit PCM stereo data, sampled at 48000 Hz. So based on the description for the nBlockAlign member of the **WAVEFORMATEX** structure, in this example nBlockAlign = 2 \* 16 / 8 = 4 bytes. This means that the length of the buffer would be 48000 \* 20 / 1000 = 960 frames, or 960 \* 4 = 3840 bytes.

The first **Set** request will specify the number of bytes were written to the buffer. And since the “write position” is expressed in bytes, a value of 1920 would specify half the buffer size, whereas a value of 3840 would indicate the full buffer size. To determine the number of new bytes written, for making subsequent **Set** requests, the following pseudo code shows how the calculation is performed:

``` syntax
if new write position > old write position:
     bytes written = new write position – old write position
if new write position < old write position, we’ve wrapped:
     bytes written = (new write position + buffer size) – old write position
if new write position = old write position, we’ve had a glitch
     log a "duplicate write position" glitch event
```

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


[**WAVEFORMATEX**](https://msdn.microsoft.com/library/windows/hardware/ff538799)

 

 






