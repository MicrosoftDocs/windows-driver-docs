---
title: Software Volume Control Support
description: Software Volume Control Support
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Software Volume Control Support


In Windows Vista and later, software volume support is provided for audio hardware that does not include and amplifier with an associated physical volume control.

The following diagram shows a simplified representation of the Windows software volume support.

![diagram illustrating the windows vista software volume support .](images/audio-volume-architecture.png)

The diagram shows two separate audio data paths. One when an amplifier is present and one when the Windows APO software volume control is used. If an amplifier is present, the driver advertises, KSPROPERTY\_AUDIO\_VOLUMELEVEL. If the audio driver does not indicate that it supports KSPROPERTY\_AUDIO\_VOLUMELEVEL, the Windows audio engine creates a software volume control APO.

On a typical PC, only one of these data paths will be present, since there will typically be one set of audio components in the computer. The two paths are shown here for illustrative purposes.

The [**IAudioEndpointVolume**](/windows/win32/api/endpointvolume/nn-endpointvolume-iaudioendpointvolume) interface represents the volume controls on the audio stream to or from an audio endpoint device.

If Bluetooth or USB audio is present, their volume controls will be controlled separately.

## <span id="Data_path_with_amplifier_present"></span><span id="data_path_with_amplifier_present"></span><span id="DATA_PATH_WITH_AMPLIFIER_PRESENT"></span>Data path with amplifier present


When a client application calls the [**IAudioEndpointVolume**](/windows/win32/api/endpointvolume/nn-endpointvolume-iaudioendpointvolume) interface in a configuration where there is an amplifier and a physical volume control present, the audio driver exposes a KSNODETYPE\_VOLUME node in the topology filter. The presence of the volume node makes **IAudioEndpointVolume** aware that the volume level of the audio signal will be modified by the hardware.

## <span id="Data_path_with_no_amplifier_present"></span><span id="data_path_with_no_amplifier_present"></span><span id="DATA_PATH_WITH_NO_AMPLIFIER_PRESENT"></span>Data path with no amplifier present


When there is no amplifier present, [**IAudioEndpointVolume**](/windows/win32/api/endpointvolume/nn-endpointvolume-iaudioendpointvolume) works with the audio engine to initialize the Windows software volume support APO.

Since there is no physical volume control to be modeled, a KSNODETYPE\_VOLUME node is not exposed in the topology filter. Volume attenuation and gain are performed by the APO software volume support component.

For information about the volume ranges and the default volume levels for the different versions of Windows, see [Default Audio Volume Settings](default-audio-volume-settings.md).

 

