---
title: KSPROPERTY\_AUDIOENGINE\_BUFFER\_SIZE\_RANGE
description: The KSPROPERTY\_AUDIOENGINE\_BUFFER\_SIZE\_RANGE property indicates the minimum and maximum size of buffer that the hardware audio engine can support for a given data format, at the instance when it is called. The buffer size is specified in bytes.
ms.assetid: 6A5DF24C-A328-4814-A410-2B1E13402A2B
keywords: ["KSPROPERTY_AUDIOENGINE_BUFFER_SIZE_RANGE Audio Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_AUDIOENGINE_BUFFER_SIZE_RANGE
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_AUDIOENGINE\_BUFFER\_SIZE\_RANGE


The **KSPROPERTY\_AUDIOENGINE\_BUFFER\_SIZE\_RANGE** property indicates the minimum and maximum size of buffer that the hardware audio engine can support for a given data format, at the instance when it is called. The buffer size is specified in bytes.

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
<td align="left"><p>Node via filter</p></td>
<td align="left"><p>KSP_NODE</p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/hh450864" data-raw-source="[&lt;strong&gt;KSAUDIOENGINE_BUFFER_SIZE_RANGE&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/hh450864)"><strong>KSAUDIOENGINE_BUFFER_SIZE_RANGE</strong></a></p></td>
</tr>
</tbody>
</table>

 

### <span id="Return_Value"></span><span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

A **KSPROPERTY\_AUDIOENGINE\_BUFFER\_SIZE\_RANGE** property request returns **STATUS\_SUCCESS** to indicate that it has completed successfully. Otherwise, the request returns an appropriate error status code.

Remarks
-------

It is important to note that before a caller calls the **KSPROPERTY\_AUDIOENGINE\_BUFFER\_SIZE\_RANGE** property, the caller fills in the fields of a [**KSDATAFORMAT\_WAVEFORMATEX**](https://msdn.microsoft.com/library/windows/hardware/ff537095) structure. So when **KSPROPERTY\_AUDIOENGINE\_BUFFER\_SIZE\_RANGE** is called, the audio driver receives a KSP\_NODE followed by a filled-in **KSDATAFORMAT\_WAVEFORMATEX** structure from the caller. The driver uses the data format information in this structure to determine the min and max buffer sizes to accommodate the specified data format. Upon a successful call to this property, the kernel streaming (KS) filter then fills in the **MinBufferBytes** and **MaxBufferBytes** fields of the [**KSAUDIOENGINE\_BUFFER\_SIZE\_RANGE**](https://msdn.microsoft.com/library/windows/hardware/hh450864) structure.

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


[**KSAUDIOENGINE\_BUFFER\_SIZE\_RANGE**](https://msdn.microsoft.com/library/windows/hardware/hh450864)

[**KSDATAFORMAT\_WAVEFORMATEX**](https://msdn.microsoft.com/library/windows/hardware/ff537095)

[**KSPROPERTY\_AUDIOENGINE**](ksproperty-audioengine.md)

 

 






