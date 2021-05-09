---
title: KSPROPERTY\_RTAUDIO\_GETREADPACKET
description: KSPROPERTY\_RTAUDIO\_GETREADPACKET returns information about captured audio packets.
keywords: ["KSPROPERTY_RTAUDIO_GETREADPACKET Audio Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_RTAUDIO_GETREADPACKET
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 12/21/2018
ms.localizationpriority: medium
---

# KSPROPERTY\_RTAUDIO\_GETREADPACKET


KSPROPERTY\_RTAUDIO\_GETREADPACKET returns information about captured audio packets.

### <span id="Usage_Summary_Table"></span><span id="usage_summary_table"></span><span id="USAGE_SUMMARY_TABLE"></span>Usage Summary Table

 
|Get|Set|Target|Property descriptor type|Property value type|
|--- |--- |--- |--- |--- |
|Yes|No|Pin|[KSPROPERTY](/previous-versions/ff564262(v=vs.85))|[KSRTAUDIO_GETREADPACKET_INFO](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksrtaudio_getreadpacket_info)|


The property descriptor (instance data) is a [**KSPROPERTY**](/previous-versions/ff564262(v=vs.85)) structure. Before sending the request, the client loads the structure with values that indicate the packet number, packet length and other information.

The property value is a variable of type [**KSRTAUDIO\_GETREADPACKET\_INFO**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksrtaudio_getreadpacket_info).

### <span id="Return_Value"></span><span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

A KSPROPERTY\_RTAUDIO\_GETREADPACKET property request returns STATUS\_SUCCESS to indicate that it has completed successfully. Otherwise, the request returns an appropriate failure status code.

STATUS\_DEVICE\_NOT\_READY - The driver returns this error if no new data is available.

## Remarks

Before reading captured audio data from the WaveRT buffer, the OS calls this routine to get information about the available data.

The packet number identifies a packet within the stream. This resets to zero when the stream is in KSSTATE\_STOP. The number advances with each captured buffer. From the packet number the OS can derive the packet location within the WaveRT buffer and can also derive the stream position of the packet relative to start of stream.

The packet size is the WaveRT buffer size divided by the NotificationCount passed to [**KSPROPERTY\_RTAUDIO\_BUFFER\_WITH\_NOTIFICATION**](ksproperty-rtaudio-buffer-with-notification.md). The OS may call this routine at any time. In normal operation, the OS calls this routine after the driver sets the buffer notification event or after a previous call returns true for MoreData. When the OS calls this routine, the driver may assume that the OS has finished reading all previous packets. If the hardware has captured enough data, the driver may immediately burst the next complete packet to the WaveRT buffer and set the buffer event again. In the case of capture overflow (when the OS does not read data quickly enough) the audio driver may drop or overwrite some audio data. The audio driver drops or overwrites oldest data first, The audio driver may continue to advance its internal packet counter even though the OS may not have read the data.

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


[**KSPROPERTY\_RTAUDIO\_SETWRITEPACKET**](ksproperty-rtaudio-setwritepacket.md)

[UsePositionLock](usepositionlock.md)

 

