---
title: UsePositionLock
description: The UsePositionLock registry value changes how PortCls serializes its I/O.
ms.assetid: AD5AF873-4129-4C82-B251-0469CF6149E9
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# UsePositionLock


The *UsePositionLock* registry value changes how PortCls serializes its I/O. Enabling this setting may be helpful if your audio driver suffers from glitches attributed to the global device lock that portcls uses for serialization. Be aware that when *UsePositionLock* is enabled, it will be up to the audio driver to apply any serialization between the listed callbacks below and other property callbacks (if needed). This flag is not enabled by default. Before turning it on, make sure to review your driver for any race conditions between your driver’s callbacks.

Use the following INF setting to enable this behavior.

```
 
[MyAudioDevice.AddReg]
HKR, DispatchSettings, UsePositionLock, 3, 01, 00, 00, 00
```

This INF setting creates the following registry value. The media GUID of {4d36e96c-e325-11ce-bfc1-08002be10318} and the &lt;instance\#&gt; of your audio device are used in the registry entry path.

```
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20UsePositionLock%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




