---
title: KSPROPERTY\_RTAUDIO\_BUFFER
description: The KSPROPERTY\_RTAUDIO\_BUFFER property specifies a driver-allocated cyclic buffer for audio data.The following table summarizes the features of this property.
ms.assetid: e2c78849-1a34-446c-9f44-012f36ddafa5
keywords: ["KSPROPERTY_RTAUDIO_BUFFER Audio Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_RTAUDIO_BUFFER
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

# KSPROPERTY\_RTAUDIO\_BUFFER


The KSPROPERTY\_RTAUDIO\_BUFFER property specifies a driver-allocated cyclic buffer for audio data.

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
<td align="left"><p>[<strong>KSRTAUDIO_BUFFER_PROPERTY</strong>](ksrtaudio-buffer-property.md)</p></td>
<td align="left"><p>[<strong>KSRTAUDIO_BUFFER</strong>](https://msdn.microsoft.com/library/windows/hardware/ff537493)</p></td>
</tr>
</tbody>
</table>

 

The property descriptor (instance data) consists of a KSRTAUDIO\_BUFFER\_PROPERTY structure that contains a [**KSPROPERTY**](https://msdn.microsoft.com/library/windows/hardware/ff564262) structure along with other members. The client writes its requested buffer size into the structure. If the client does not have to work with a specific base address, it must specify the base address as **NULL**.

The property value (operation data) is a structure of type KSRTAUDIO\_BUFFER. The driver fills this structure with the actual buffer size, base address, and memory barrier flag for the cyclic buffer that it has allocated.

### <span id="Return_Value"></span><span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

A KSPROPERTY\_RTAUDIO\_BUFFER property request returns STATUS\_SUCCESS to indicate that it has completed successfully. Otherwise, the request returns an appropriate failure status code. The following table shows some of the possible failure status codes.

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
<td align="left"><p>The device is not ready</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

The base address is the virtual memory address at the start of the cyclic buffer. The client can directly access the buffer at this address. The buffer is contiguous in virtual memory. The decision whether to make the buffer contiguous in physical memory is left up to the driver.

The client should set the base address in the property descriptor to **NULL**. The driver sets the base address in the property value to the virtual address of the allocated audio buffer.

Typically, audio hardware requires the audio buffer either to begin and end on sample boundaries or meet other types of hardware-dependent alignment constraints. If sufficient memory is available, the actual size of the buffer is the requested size rounded (up or down) to the nearest sample or other hardware-constrained boundary. The actual size must be at least the requested size; otherwise, the Audio Session API (WASAPI) audio engine won't use the buffer, and stream creation will fail.

If a KSPROPERTY\_RTAUDIO\_BUFFER property request is successful, the property value, which is a structure of type KSRTAUDIO\_BUFFER, contains the address and size of the driver-allocated buffer.

Closing the pin automatically frees the buffer that was allocated through this property.

If you want event notifications, you must call [**KSPROPERTY\_RTAUDIO\_BUFFER\_WITH\_NOTIFICATION**](ksproperty-rtaudio-buffer-with-notification.md) instead of KSPROPERTY\_RTAUDIO\_BUFFER.

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


[**KSRTAUDIO\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff537493)

[**KSRTAUDIO\_BUFFER\_PROPERTY**](ksrtaudio-buffer-property.md)

[**KSPROPERTY\_RTAUDIO\_BUFFER\_WITH\_NOTIFICATION**](ksproperty-rtaudio-buffer-with-notification.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20KSPROPERTY_RTAUDIO_BUFFER%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





