---
title: UsePositionLock
description: The UsePositionLock registry value changes how PortCls serializes its I/O.
ms.date: 09/29/2022
---

# UsePositionLock


The *UsePositionLock* registry value changes how PortCls serializes its I/O. Enabling this setting may be helpful if your audio driver suffers from glitches attributed to the global device lock that portcls uses for serialization. Be aware that when *UsePositionLock* is enabled, it will be up to the audio driver to apply any serialization between the listed callbacks below and other property callbacks (if needed). This flag is not enabled by default. Before turning it on, make sure to review your driver for any race conditions between your driver’s callbacks.

Use the following INF setting to enable this behavior.

```inf
[MyAudioDevice.AddReg]
HKR, DispatchSettings, UsePositionLock, 3, 01, 00, 00, 00
```
When this value is set to 1 or above, portcls uses the streaming position lock to serialize the callbacks listed below. If it is not present or set to zero, the default behavior is to use the global device lock. This value is read the first time the device is added.

This INF setting will be stored under the device instance in the registry whose path contains the media GUID of {4d36e96c-e325-11ce-bfc1-08002be10318}.

This INF setting creates a registry value that contains the media GUID of {4d36e96c-e325-11ce-bfc1-08002be10318} that includes the instance of your audio device.

The *UsePositionLock* setting is only supported on WaveRT and Topology filters. Portcls reads this registry value at device-add time and the setting persists until the functional device object (FDO) is removed.

If portcls detects that this flag is on, it does not serialize the following properties with the global device lock.

-   {KSPROPSETID\_RtAudio, [**KSPROPERTY\_RTAUDIO\_GETREADPACKET**](ksproperty-rtaudio-getreadpacket.md)}

-   {KSPROPSETID\_RtAudio, [**KSPROPERTY\_RTAUDIO\_SETWRITEPACKET**](ksproperty-rtaudio-setwritepacket.md)}

-   {KSPROPSETID\_RtAudio, [**KSPROPERTY\_RTAUDIO\_PRESENTATION\_POSITION**](ksproperty-rtaudio-presentation-position.md)}

-   {KSPROPSETID\_RtAudio, [**KSPROPERTY\_RTAUDIO\_PACKETCOUNT**](ksproperty-rtaudio-packetcount.md)}

-   {KSPROPSETID\_Audio,[**KSPROPERTY\_AUDIO\_POSITION**](ksproperty-audio-position.md)}

-   {KSPROPSETID\_Audio, [**KSPROPERTY\_AUDIO\_POSITIONEX**](ksproperty-audio-positionex.md)}

This means that the following miniport’s callbacks are not serialized with the other property requests (including set-state requests).

-   [**IMiniportWaveRTInputStream::GetReadPacket**](/windows-hardware/drivers/ddi/portcls/nf-portcls-iminiportwavertinputstream-getreadpacket)

-   [**IMiniportWaveRTOutputStream::SetWritePacket**](/windows-hardware/drivers/ddi/portcls/nf-portcls-iminiportwavertoutputstream-setwritepacket)

-   [**IMiniportWaveRTOutputStream::GetOutputStreamPresentationPosition**](/windows-hardware/drivers/ddi/portcls/nf-portcls-iminiportwavertoutputstream-getoutputstreampresentationposition)

-   [**IMiniportWaveRTOutputStream::GetPacketCount**](/windows-hardware/drivers/ddi/portcls/nf-portcls-iminiportwavertoutputstream-getpacketcount)

-   [**IMiniportWaveRTStream::GetPosition**](/windows-hardware/drivers/ddi/portcls/nf-portcls-iminiportwavertstream-getposition)

 

