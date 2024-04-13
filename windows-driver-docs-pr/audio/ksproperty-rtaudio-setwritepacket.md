---
title: KSPROPERTY\_RTAUDIO\_SETWRITEPACKET
description: KSPROPERTY\_RTAUDIO\_SETWRITEPACKET informs the driver that the OS has written valid data to the WaveRT buffer.
keywords: ["KSPROPERTY_RTAUDIO_SETWRITEPACKET Audio Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- KSPROPERTY_RTAUDIO_SETWRITEPACKET
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 12/21/2018
---

# KSPROPERTY\_RTAUDIO\_SETWRITEPACKET


KSPROPERTY\_RTAUDIO\_SETWRITEPACKET informs the driver that the OS has written valid data to the WaveRT buffer.

### <span id="Usage_Summary_Table"></span><span id="usage_summary_table"></span><span id="USAGE_SUMMARY_TABLE"></span>Usage Summary Table

|Get|Set|Target|Property descriptor type|Property value type|
|--- |--- |--- |--- |--- |
|No|Yes|Pin|[**KSPROPERTY**](../stream/ksproperty-structure.md)|[KSRTAUDIO_SETWRITEPACKET_INFO](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksrtaudio_setwritepacket_info)|


The property descriptor (instance data) is a [**KSPROPERTY**](../stream/ksproperty-structure.md) structure. Before sending the request, the client loads the structure with values that include the packet number, packet length and other information.

The property value is a structure of type [**KSRTAUDIO\_SETWRITEPACKET\_INFO**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksrtaudio_setwritepacket_info).

### <span id="Return_Value"></span><span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

A KSPROPERTY\_RTAUDIO\_SETWRITEPACKET property request returns STATUS\_SUCCESS to indicate that it has completed successfully. Otherwise, the request returns an appropriate failure status code.

## Remarks

If this KSPROPERTY is supported, the driver may optionally use the provided information to optimize the hardware transfer. For example, the driver might optimize DMA transfers, or program hardware to stop transfer at the end of the specified packet in case the OS does not call this routine again to inform the driver of another packet. This can mitigate audible effects of underflow, for example introducing an audible gap rather than repeating a circular buffer. The driver however is still obligated to increase its internal packet counter and signal notification events at a nominal real time rate.

Except when the OS specifies the *KSSTREAM\_HEADER\_OPTIONSF\_ENDOFSTREAM* flag, the packet size is the WaveRT buffer size divided by the NotificationCount passed to [**KSPROPERTY\_RTAUDIO\_BUFFER\_WITH\_NOTIFICATION**](ksproperty-rtaudio-buffer-with-notification.md).

Depending on hardware capabilities, if the *KSSTREAM\_HEADER\_OPTIONSF\_ENDOFSTREAM* flag is specified, the driver may silence-fill a portion of the WaveRT buffer that follows the EOS packet in case the hardware transfers data beyond the EOS position.

## Requirements

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

