---
title: Prefetch Offsets
description: Prefetch Offsets
ms.assetid: 92a0163f-29b1-4e15-88ab-67e1097d015e
keywords:
- hardware acceleration WDK DirectSound , prefetch offsets
- prefetch offsets WDK audio
- write cursor offsets WDK audio
- play cursor offsets WDK audio
- offsets WDK audio
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Prefetch Offsets


## <span id="prefetch_offsets"></span><span id="PREFETCH_OFFSETS"></span>


A WavePci miniport driver calls the [**IPreFetchOffset::SetPreFetchOffset**](https://msdn.microsoft.com/library/windows/hardware/ff536952) method to specify the prefetch offset of a hardware-accelerated DirectSound output stream. This offset is the number of bytes of data separating the write cursor from the play cursor in the audio device's hardware buffer. The write cursor specifies the buffer position into which a DirectSound application can safely write the next sound sample. The play cursor specifies the buffer position of the sound sample that is currently being played by the audio device.

DirectSound queries the WavePci port driver for the current positions of the play and write cursors by sending a [**KSPROPERTY\_AUDIO\_POSITION**](https://msdn.microsoft.com/library/windows/hardware/ff537297) property request. In response to this request, the port driver obtains the current play position from the miniport driver by calling [**IMiniportWavePciStream::GetPosition**](https://msdn.microsoft.com/library/windows/hardware/ff536727). How the port driver determines the write position depends on whether [**SetPreFetchOffset**](https://msdn.microsoft.com/library/windows/hardware/ff536952) has been called.

By default, the port driver positions the write cursor in the last mapping requested by the miniport driver. With each call to [**IPortWavePciStream::GetMapping**](https://msdn.microsoft.com/library/windows/hardware/ff536909), the default prefetch offset grows larger. If the WavePci miniport driver acquires a large number of mappings, the default offset can grow very large.

Calling [**SetPreFetchOffset**](https://msdn.microsoft.com/library/windows/hardware/ff536952) overrides the default. Following this call, the port driver calculates the write position by adding the specified prefetch offset to the play position (taking into account the wraparound at the end of the DirectSound buffer).

A miniport driver might allocate a large number of mappings for a couple of reasons. One is to reduce the overhead of audio operations on the system processor. With more mappings, the driver requires fewer interrupts to keep the audio device continuously supplied with data. Another reason is that allocating more mappings decreases the likelihood that audio playback will suffer glitches when badly behaved device drivers tie up the system for short periods.

One problem with a large prefetch offset is that some DirectSound applications can become confused about the relative positions of the play and write cursors. In Windows 95/98, audio VxDs maintain a relatively small prefetch offset, and DirectSound applications written for these operating systems might not run correctly if the offset is larger than they expect.

For example, an application might divide the DirectSound buffer into an upper half and a lower half and then "ping pong" the two halves between the application and the device. When the write cursor first enters the upper or lower half of the buffer, it writes a half buffer's worth of data to that half of the buffer. This scheme assumes that the play cursor is always positioned in the other half of the buffer--the half that is not being written to. Note that this assumption is incorrect if the prefetch offset exceeds half the buffer size. In that case, when the write cursor reaches the end of the DirectSound buffer and wraps around to the beginning of the buffer, it will be in the same half of the buffer as the play cursor. When the application writes a half buffer's worth of data to the new write cursor position, it ends up overwriting the play cursor position and destroying data that has not been played yet.

Although the application itself can certainly be blamed for this type of failure, a WavePci miniport driver can eliminate the failure mode simply by calling [**SetPreFetchOffset**](https://msdn.microsoft.com/library/windows/hardware/ff536952) to set the prefetch offset to a smaller value.

Setting the prefetch offset to a smaller value moves the resulting write cursor closer to the play cursor. You should set the prefetch offset to the FIFO size of your hardware. A typical prefetch offset is about 64 samples, depending on the DMA engine's hardware design.

To remain compatible with certain older DirectSound applications, DirectSound currently pads the write cursors of hardware-accelerated pins by 10 milliseconds. Note that the amount of padding might change in the future.

For additional information about managing write cursors and play cursors at the driver level, see [Audio Position Property](audio-position-property.md).

 

 




