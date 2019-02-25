---
title: KSPROPERTY\_RTAUDIO\_PACKETCOUNT
description: KSPROPERTY\_RTAUDIO\_PACKETCOUNT returns the (1-based) count of packets completely transferred from the WaveRT buffer into hardware.
ms.assetid: 904896DE-D135-43B6-AA1F-F49D0748952D
keywords: ["KSPROPERTY_RTAUDIO_PACKETCOUNT Audio Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_RTAUDIO_PACKETCOUNT
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 06/19/2018
ms.localizationpriority: medium
---

# KSPROPERTY\_RTAUDIO\_PACKETCOUNT


KSPROPERTY\_RTAUDIO\_PACKETCOUNT returns the (1-based) count of packets completely transferred from the WaveRT buffer into hardware.

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
<td align="left"><p><a href="https://docs.microsoft.com/dotnet/csharp/language-reference/keywords/ulong" data-raw-source="[&lt;strong&gt;ULONG&lt;/strong&gt;](https://docs.microsoft.com/dotnet/csharp/language-reference/keywords/ulong)"><strong>ULONG</strong></a></p></td>
</tr>
</tbody>
</table>

 

The property descriptor (instance data) is a [**KSPROPERTY**](https://msdn.microsoft.com/library/windows/hardware/ff564262) structure. Before sending the request, the client loads the structure with the (1-based) count of packets completely transferred from the WaveRT buffer into hardware.

The property value is a variable of type ULONG.

### <span id="Return_Value"></span><span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

A KSPROPERTY\_RTAUDIO\_PACKETCOUNT property request returns STATUS\_SUCCESS to indicate that it has completed successfully. Otherwise, the request returns an appropriate failure status code.

Remarks
-------

From the packet count, the OS can derive the stream position of the packets it writes into the WaveRT buffer. The OS can also derive the WaveRT buffer position of the next packet to write within the WaveRT buffer. For WaveRT drivers, the driver signals a single notification event as it transfers data from each packet of the WaveRT buffer. Therefore the event alone cannot indicate which packet within the WaveRT buffer is being transferred. In normal operation this is not a concern but in underflow cases correction is more easily achieved by querying the packet count from which the OS can determine which packet to write next.

The returned PacketCount indicates the (1-based) count of packets completely transferred from the WaveRT buffer into hardware. From this, the OS can determine the 0-based number of the packet currently being transferred, and ensure that it writes ahead of that packet. For example, if the packet count is 5, then 5 packets have completely transferred. That is, packets 0-4 have completely transferred. Therefore packet 5 is in progress, and the OS should write packet 6. If the notification count for the WaveRT buffer is 2, then packet 6 would be at offset 0 within the WaveRT buffer (because 6 modulo 2 is 0, and 0 times the packet size is 0).

The OS may get this property at any time. However it generally gets this property only periodically or after the driver returns a dataflow error (STATUS\_DATA\_LATE\_ERROR, STATUS\_DATA\_OVERRUN) from SetWritePacket() in order to resynchronize with the driver.

The driver should reset the packet count to 0 when the stream is in KSSTATE\_STOP.

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


[KSPROPSETID\_RTAudio](kspropsetid-rtaudio.md)

 

 






