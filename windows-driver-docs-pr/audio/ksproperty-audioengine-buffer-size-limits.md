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
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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
<td align="left"><p>[<strong>KSAUDIOENGINE_BUFFER_SIZE_RANGE</strong>](https://msdn.microsoft.com/library/windows/hardware/hh450864)</p></td>
</tr>
</tbody>
</table>

 

### <span id="Return_Value"></span><span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

A **KSPROPERTY\_AUDIOENGINE\_BUFFER\_SIZE\_RANGE** property request returns **STATUS\_SUCCESS** to indicate that it has completed successfully. Otherwise, the request returns an appropriate error status code.

Remarks
-------

It is important to note that before a caller calls the **KSPROPERTY\_AUDIOENGINE\_BUFFER\_SIZE\_RANGE** property, the caller fills in the fields of a [**KSDATAFORMAT\_WAVEFORMATEX**](https://msdn.microsoft.com/library/windows/hardware/ff537095) structure. So when **KSPROPERTY\_AUDIOENGINE\_BUFFER\_SIZE\_RANGE** is called, the audio driver receives a KSP\_NODE followed by a filled-in **KSDATAFORMAT\_WAVEFORMATEX** structure from the caller. The driver uses the data format information in this structure to determine the min and max buffer sizes to accommodate the specfied data format. Upon a successful call to this property, the kernel streaming (KS) filter then fills in the **MinBufferBytes** and **MaxBufferBytes** fields of the [**KSAUDIOENGINE\_BUFFER\_SIZE\_RANGE**](https://msdn.microsoft.com/library/windows/hardware/hh450864) structure.

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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20KSPROPERTY_AUDIOENGINE_BUFFER_SIZE_RANGE%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





