---
title: Specifics for DirectSound Clients
description: Specifics for DirectSound Clients
ms.assetid: 95ef53d3-572d-478b-839b-0555e9051129
keywords:
- DirectSound WDK audio , non-PCM wave formats
- non-PCM audio formats WDK , DirectSound
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Specifics for DirectSound Clients


## <span id="specifics_for_directsound_clients"></span><span id="SPECIFICS_FOR_DIRECTSOUND_CLIENTS"></span>


On Microsoft Windows 2000 and Windows 98, DirectSound does not support non-PCM formats, regardless of the DirectSound version. (However, DirectSound 8 does support non-PCM formats on both Windows 2000 SP2 and Windows 98 SE + hotfix. Also, the versions of DirectSound that ship with Windows XP and later, and Windows Me, support non-PCM formats.)

To determine whether a WDM driver supports a particular wave format, a client can attempt to create a DSBCAPS\_LOCHARDWARE buffer in that format on the driver and see whether the attempt succeeds. The DirectSound API provides no other way to discover which non-PCM data formats are supported.

DirectSound allows secondary DSBCAPS\_LOCHARDWARE buffers to have any valid [**WAVEFORMATEX**](https://msdn.microsoft.com/library/windows/hardware/ff538799) or [**WAVEFORMATEXTENSIBLE**](https://msdn.microsoft.com/library/windows/hardware/ff538802) format that the selected driver supports. When searching for the format in the driver's list of supported formats, DirectSound checks only for formats containing the KSDATAFORMAT\_SPECIFIER\_DSOUND specifier.

You can extend a DirectSound application to use a non-PCM format by first creating a WAVEFORMATEX or WAVEFORMATEXTENSIBLE structure that describes the format. Next, load a pointer to the structure into the **lpwfxFormat** member of the DSBUFFERDESC structure that is passed to the **CreateSoundBuffer** method. No other changes to existing DirectSound code are needed to use a non-PCM format. Note that the controls that a driver typically supports for PCM data are unlikely to be supported for some non-PCM formats. For example, a card that supports digital output of data that is encoded in an AC-3 or WMA Pro format is unlikely to support the DSBCAPS\_CTRLPAN or DSBCAPS\_CTRLVOLUME controls on that data. Thus, attempting to create the DirectSound buffer with those flags might fail.

DirectSound playback through VxD drivers or legacy waveOut drivers is still limited to PCM; non-PCM formats are not supported.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20Specifics%20for%20DirectSound%20Clients%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


