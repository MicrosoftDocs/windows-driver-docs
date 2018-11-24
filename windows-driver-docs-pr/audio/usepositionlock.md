---
title: UsePositionLock
description: The UsePositionLock registry value changes how PortCls serializes its I/O.
ms.assetid: AD5AF873-4129-4C82-B251-0469CF6149E9
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# UsePositionLock


The *UsePositionLock* registry value changes how PortCls serializes its I/O. Enabling this setting may be helpful if your audio driver suffers from glitches attributed to the global device lock that portcls uses for serialization. Be aware that when *UsePositionLock* is enabled, it will be up to the audio driver to apply any serialization between the listed callbacks below and other property callbacks (if needed). This flag is not enabled by default. Before turning it on, make sure to review your driver for any race conditions between your driver’s callbacks.

Use the following INF setting to enable this behavior.

```inf
 
[MyAudioDevice.AddReg]
HKR, DispatchSettings, UsePositionLock, 3, 01, 00, 00, 00
```

This INF setting creates the following registry value. The media GUID of {4d36e96c-e325-11ce-bfc1-08002be10318} and the &lt;instance\#&gt; of your audio device are used in the registry entry path.

```text
\HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Class\{4d36e96c-e325-11ce-bfc1-08002be10318}\<instance#>\DispatchSettings\UsePositionLock 
```

When this value is set to 1 or above, portcls uses the streaming position lock to serialize the callbacks listed below. If it is not present or set to zero, the default behavior is to use the global device lock. This value is read the first time the device is added.

The *UsePositionLock* setting is only supported on WaveRT and Topology filters. Portcls reads this registry value at device-add time and the setting persists until the functional device object (FDO) is removed.

If portcls detects that this flag is on, it does not serialize the following properties with the global device lock.

-   {KSPROPSETID\_RtAudio, [**KSPROPERTY\_RTAUDIO\_GETREADPACKET**](ksproperty-rtaudio-getreadpacket.md)}

-   {KSPROPSETID\_RtAudio, [**KSPROPERTY\_RTAUDIO\_SETWRITEPACKET**](ksproperty-rtaudio-setwritepacket.md)}

-   {KSPROPSETID\_RtAudio, [**KSPROPERTY\_RTAUDIO\_PRESENTATION\_POSITION**](ksproperty-rtaudio-presentation-position.md)}

-   {KSPROPSETID\_RtAudio, [**KSPROPERTY\_RTAUDIO\_PACKETCOUNT**](ksproperty-rtaudio-packetcount.md)}

-   {KSPROPSETID\_Audio,[**KSPROPERTY\_AUDIO\_POSITION**](ksproperty-audio-position.md)}

-   {KSPROPSETID\_Audio, [**KSPROPERTY\_AUDIO\_POSITIONEX**](ksproperty-audio-positionex.md)}

This means that the following miniport’s callbacks are not serialized with the other property requests (including set-state requests).

-   [**IMiniportWaveRTInputStream::GetReadPacket**](https://msdn.microsoft.com/library/windows/hardware/dn946533)

-   [**IMiniportWaveRTOutputStream::SetWritePacket**](https://msdn.microsoft.com/library/windows/hardware/dn946537)

-   [**IMiniportWaveRTOutputStream::GetOutputStreamPresentationPosition**](https://msdn.microsoft.com/library/windows/hardware/dn946535)

-   [**IMiniportWaveRTOutputStream::GetPacketCount**](https://msdn.microsoft.com/library/windows/hardware/dn946536)

-   [**IMiniportWaveRTStream::GetPosition**](https://msdn.microsoft.com/library/windows/hardware/ff536749)

 

 





