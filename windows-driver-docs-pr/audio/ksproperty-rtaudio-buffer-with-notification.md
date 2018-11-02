---
title: KSPROPERTY\_RTAUDIO\_BUFFER\_WITH\_NOTIFICATION
description: The KSPROPERTY\_RTAUDIO\_BUFFER\_WITH\_NOTIFICATION property specifies a driver-allocated cyclic buffer for audio data and identifies event notification requirements.The following table summarizes the features of this property.
ms.assetid: a66727ae-03d6-41b5-b5c9-3b04352b3b83
keywords: ["KSPROPERTY_RTAUDIO_BUFFER_WITH_NOTIFICATION Audio Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_RTAUDIO_BUFFER_WITH_NOTIFICATION
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_RTAUDIO\_BUFFER\_WITH\_NOTIFICATION


The KSPROPERTY\_RTAUDIO\_BUFFER\_WITH\_NOTIFICATION property specifies a driver-allocated cyclic buffer for audio data and identifies event notification requirements.

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
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff537495" data-raw-source="[&lt;strong&gt;KSRTAUDIO_BUFFER_PROPERTY_WITH_NOTIFICATION&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff537495)"><strong>KSRTAUDIO_BUFFER_PROPERTY_WITH_NOTIFICATION</strong></a></p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff537493" data-raw-source="[&lt;strong&gt;KSRTAUDIO_BUFFER&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff537493)"><strong>KSRTAUDIO_BUFFER</strong></a></p></td>
</tr>
</tbody>
</table>

 

The property descriptor (instance data) consists of a KSRTAUDIO\_BUFFER\_PROPERTY\_WITH\_NOTIFICATION structure that contains a [**KSPROPERTY**](https://msdn.microsoft.com/library/windows/hardware/ff564262) structure along with other members. The client writes its requested buffer size into the structure. The client must specify the base address as **NULL** unless a specific base address is needed.

This property is used when you want DMA-driven event notification. Based on the **NotificationCount** member, registered events are signaled once (at the end) or twice (at the mid-point and the end) per cycle through the cyclic buffer. Events are registered using [**KSPROPERTY\_RTAUDIO\_REGISTER\_NOTIFICATION\_EVENT**](ksproperty-rtaudio-register-notification-event.md) after successfully calling KSPROPERTY\_RTAUDIO\_BUFFER\_WITH\_NOTIFICATION.

The property value (operation data) is a structure of type [**KSRTAUDIO\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff537493). The driver fills this structure with the actual buffer size, base address, and memory barrier flag for the cyclic buffer that it has allocated.

### <span id="Return_Value"></span><span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

A KSPROPERTY\_RTAUDIO\_BUFFER\_WITH\_NOTIFICATION property request returns STATUS\_SUCCESS to indicate that it has completed successfully. Otherwise, the request returns an appropriate failure status code. The following table shows some of the possible failure status codes.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Status code</th>
<th align="left">Meaning</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>STATUS_UNSUCCESSFUL</p></td>
<td align="left"><p>A cyclic buffer with the specified combination of buffer attributes cannot be allocated.</p></td>
</tr>
<tr class="even">
<td align="left"><p>STATUS_INSUFFICIENT_RESOURCES</p></td>
<td align="left"><p>Memory for the buffer cannot be allocated.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>STATUS_DEVICE_NOT_READY</p></td>
<td align="left"><p>The device is not ready.</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

The base address is the virtual memory address at the start of the cyclic buffer. The client can directly access the buffer at this address. The buffer is contiguous in virtual memory. The driver determines whether the buffer is contiguous in physical memory.

The client sets the base address in the property descriptor to **NULL**. The driver sets the base address in the property value to the virtual address of the allocated audio buffer.

Typically, audio hardware requires that either the audio buffer begins and ends on sample boundaries or it meets other types of hardware-dependent alignment constraints. If sufficient memory is available, the actual size of the buffer is the requested size rounded (up or down) to the nearest sample or other hardware-constrained boundary. Otherwise, the actual size can be less than the requested size.

If a KSPROPERTY\_RTAUDIO\_BUFFER\_WITH\_NOTIFICATION property request succeeds, the property value, which is a structure of type KSRTAUDIO\_BUFFER, contains the address and size of the driver-allocated buffer.

Closing the pin automatically frees the buffer that was allocated through this property.

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

[**KSRTAUDIO\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff537493)

[**KSRTAUDIO\_BUFFER\_PROPERTY\_WITH\_NOTIFICATION**](https://msdn.microsoft.com/library/windows/hardware/ff537495)

[**KSPROPERTY\_RTAUDIO\_REGISTER\_NOTIFICATION\_EVENT**](ksproperty-rtaudio-register-notification-event.md)

 

 






