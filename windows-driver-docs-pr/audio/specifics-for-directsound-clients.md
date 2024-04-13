---
title: Specifics for DirectSound Clients
description: Specifics for DirectSound Clients
keywords:
- DirectSound WDK audio , non-PCM wave formats
- non-PCM audio formats WDK , DirectSound
ms.date: 04/20/2017
---

# Specifics for DirectSound Clients


## <span id="specifics_for_directsound_clients"></span><span id="SPECIFICS_FOR_DIRECTSOUND_CLIENTS"></span>


On Microsoft Windows 2000 and Windows 98, DirectSound does not support non-PCM formats, regardless of the DirectSound version. (However, DirectSound 8 does support non-PCM formats on both Windows 2000 SP2 and Windows 98 SE + hotfix. Also, the versions of DirectSound that ship with Windows XP and later, and Windows Me, support non-PCM formats.)

To determine whether a WDM driver supports a particular wave format, a client can attempt to create a DSBCAPS\_LOCHARDWARE buffer in that format on the driver and see whether the attempt succeeds. The DirectSound API provides no other way to discover which non-PCM data formats are supported.

DirectSound allows secondary DSBCAPS\_LOCHARDWARE buffers to have any valid [**WAVEFORMATEX**](/windows/win32/api/mmreg/ns-mmreg-waveformatex) or [**WAVEFORMATEXTENSIBLE**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-waveformatextensible) format that the selected driver supports. When searching for the format in the driver's list of supported formats, DirectSound checks only for formats containing the KSDATAFORMAT\_SPECIFIER\_DSOUND specifier.

You can extend a DirectSound application to use a non-PCM format by first creating a WAVEFORMATEX or WAVEFORMATEXTENSIBLE structure that describes the format. Next, load a pointer to the structure into the **lpwfxFormat** member of the DSBUFFERDESC structure that is passed to the **CreateSoundBuffer** method. No other changes to existing DirectSound code are needed to use a non-PCM format. Note that the controls that a driver typically supports for PCM data are unlikely to be supported for some non-PCM formats. For example, a card that supports digital output of data that is encoded in an AC-3 or WMA Pro format is unlikely to support the DSBCAPS\_CTRLPAN or DSBCAPS\_CTRLVOLUME controls on that data. Thus, attempting to create the DirectSound buffer with those flags might fail.

DirectSound playback through VxD drivers or legacy waveOut drivers is still limited to PCM; non-PCM formats are not supported.

 

