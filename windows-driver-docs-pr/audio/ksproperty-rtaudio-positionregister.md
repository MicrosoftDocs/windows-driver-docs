---
title: KSPROPERTY\_RTAUDIO\_POSITIONREGISTER
description: The KSPROPERTY\_RTAUDIO\_POSITIONREGISTER property maps the position register of an audio device for a particular stream into a virtual memory location that the client can access.The following table summarizes the features of this property.
ms.assetid: 812072ec-d2a5-4e84-aebe-f24ca0d3cb21
keywords: ["KSPROPERTY_RTAUDIO_POSITIONREGISTER Audio Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_RTAUDIO_POSITIONREGISTER
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_RTAUDIO\_POSITIONREGISTER


The KSPROPERTY\_RTAUDIO\_POSITIONREGISTER property maps the position register of an audio device for a particular stream into a virtual memory location that the client can access.

The following table summarizes the features of this property.

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
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff537498" data-raw-source="[&lt;strong&gt;KSRTAUDIO_HWREGISTER_PROPERTY&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff537498)"><strong>KSRTAUDIO_HWREGISTER_PROPERTY</strong></a></p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff537497" data-raw-source="[&lt;strong&gt;KSRTAUDIO_HWREGISTER&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff537497)"><strong>KSRTAUDIO_HWREGISTER</strong></a></p></td>
</tr>
</tbody>
</table>

 

The property descriptor (instance data) is a KSRTAUDIO\_HWREGISTER\_PROPERTY structure, which contains a [**KSPROPERTY**](https://msdn.microsoft.com/library/windows/hardware/ff564262) structure. Before sending the request, the client loads the structure with values that indicate the preferred base address for the register.

The property value (operation data) is a KSRTAUDIO\_HWREGISTER structure into which the property handler writes the virtual address to which it has mapped the hardware position register. The client can directly read the register from this address. The KSRTAUDIO\_HWREGISTER structure also specifies the rate at which the position register increments itself.

### <span id="Return_Value"></span><span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

A KSPROPERTY\_RTAUDIO\_POSITIONREGISTER property request returns STATUS\_SUCCESS to indicate that it has completed successfully. Otherwise, the request returns an appropriate failure status code.

Remarks
-------

Typically, audio applications must monitor the current position of an audio stream. This position is specified as a byte offset from the beginning of the stream:

-   In the case of a rendering stream, the stream's position is the byte offset of the audio frame that is currently playing through the digital-to-analog converters (DACs).

-   In the case of a capture stream, the stream's position is the byte offset of the audio frame that is currently being recorded through the analog-to-digital converters (ADCs).

Some audio devices contain position registers that increment continually while the stream is running. For an audio device that incorporates all digital and analog functions into a single chip, the position register typically indicates the current stream position directly.

However, for a chipset that divides digital and analog functions into separate bus-controller and codec chips, the position register is typically located in the bus-controller chip and indicates the following:

-   In the case of a rendering stream, the position register indicates the byte offset of the last audio frame that the bus controller wrote to the codec.

-   In the case of a capture stream, the position register indicates the byte offset of the last audio frame that the bus controller read from the codec.

In both cases, the position register value does not include the delay through the codec. If the client has determined the codec delay, it can add this delay to the position register value to estimate the true stream position (at the DACs or ADCs). For a CodecDelay value that specifies the worst-case delay through the codec, you can query the [**KSPROPERTY\_RTAUDIO\_HWLATENCY**](ksproperty-rtaudio-hwlatency.md) property.

If successful, a KSPROPERTY\_RTAUDIO\_POSITIONREGISTER property request maps the position register to a virtual memory address that is accessible to the client from either user-mode or kernel-mode, as specified by the client. Thereafter, the client reads from this address to obtain the current value of the position register.

The property request fails if the audio hardware does not support a position register that can be mapped to a virtual address. In this case, the client must determine the position from the [**KSPROPERTY\_AUDIO\_POSITION**](ksproperty-audio-position.md) property.

The mapping of the position register is destroyed when the pin closes. The client can map the register only once in the lifetime of an opened pin, and any subsequent call to remap the position register for the pin fails.

It is typically faster to read the position register than it is to send a KSPROPERTY\_AUDIO\_POSITION request, which requires transitions between user-mode and kernel-mode for user-mode clients.

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
<td align="left"><p>Available in Windows Vista and later Windows operating systems.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Header</p></td>
<td align="left">Ksmedia.h</td>
</tr>
</tbody>
</table>

## <span id="see_also"></span>See also


[**KSPROPERTY**](https://msdn.microsoft.com/library/windows/hardware/ff564262)

[**KSRTAUDIO\_HWREGISTER**](https://msdn.microsoft.com/library/windows/hardware/ff537497)

[**KSRTAUDIO\_HWREGISTER\_PROPERTY**](https://msdn.microsoft.com/library/windows/hardware/ff537498)

[**KSPROPERTY\_AUDIO\_POSITION**](ksproperty-audio-position.md)

[**KSPROPERTY\_RTAUDIO\_HWLATENCY**](ksproperty-rtaudio-hwlatency.md)

 

 






