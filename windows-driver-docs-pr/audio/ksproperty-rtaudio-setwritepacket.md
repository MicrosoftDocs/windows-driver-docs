---
title: KSPROPERTY\_RTAUDIO\_SETWRITEPACKET
description: KSPROPERTY\_RTAUDIO\_SETWRITEPACKET informs the driver that the OS has written valid data to the WaveRT buffer.
ms.assetid: 2827D6BC-B669-4AAC-967C-99B068DCC29B
keywords: ["KSPROPERTY_RTAUDIO_SETWRITEPACKET Audio Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_RTAUDIO_SETWRITEPACKET
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

# KSPROPERTY\_RTAUDIO\_SETWRITEPACKET


KSPROPERTY\_RTAUDIO\_SETWRITEPACKET informs the driver that the OS has written valid data to the WaveRT buffer.

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
<td align="left"><p>Pin</p></td>
<td align="left"><p>[<strong>KSPROPERTY</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564262)</p></td>
<td align="left"><p>[<strong>KSRTAUDIO_SETWRITEPACKET_INFO</strong>](https://msdn.microsoft.com/library/windows/hardware/ff537497)</p></td>
</tr>
</tbody>
</table>

 

The property descriptor (instance data) is a [**KSPROPERTY**](https://msdn.microsoft.com/library/windows/hardware/ff564262) structure. Before sending the request, the client loads the structure with values that indicate the preferred base address for the register.

The property value is a structure of type [**KSRTAUDIO\_SETWRITEPACKET\_INFO**](https://msdn.microsoft.com/library/windows/hardware/mt786977).

### <span id="Return_Value"></span><span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

A KSPROPERTY\_RTAUDIO\_SETWRITEPACKET property request returns STATUS\_SUCCESS to indicate that it has completed successfully. Otherwise, the request returns an appropriate failure status code.

Remarks
-------

If this KSPROPERTY is supported, the driver may optionally use the provided information to optimize the hardware transfer. For example, the driver might optimize DMA transfers, or program hardware to stop transfer at the end of the specified packet in case the OS does not call this routine again to inform the driver of another packet. This can mitigate audible effects of underflow, for example introducing an audible gap rather than repeating a circular buffer. The driver however is still obligated to increase its internal packet counter and signal notification events at a nominal real time rate.

Except when the OS specifies the *KSSTREAM\_HEADER\_OPTIONSF\_ENDOFSTREAM* flag, the packet size is the WaveRT buffer size divided by the NotificationCount passed to [**KSPROPERTY\_RTAUDIO\_BUFFER\_WITH\_NOTIFICATION**](ksproperty-rtaudio-buffer-with-notification.md).

Depending on hardware capabilities, if the *KSSTREAM\_HEADER\_OPTIONSF\_ENDOFSTREAM* flag is specified, the driver may silence-fill a portion of the WaveRT buffer that follows the EOS packet in case the hardware transfers data beyond the EOS position.

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
<td align="left"><p>Available in Windows 10 and later Windows operating systems.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Header</p></td>
<td align="left">Ksmedia.h</td>
</tr>
</tbody>
</table>

## <span id="see_also"></span>See also


[**KSPROPERTY\_RTAUDIO\_GETREADPACKET**](ksproperty-rtaudio-getreadpacket.md)

[UsePositionLock](usepositionlock.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20KSPROPERTY_RTAUDIO_SETWRITEPACKET%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





