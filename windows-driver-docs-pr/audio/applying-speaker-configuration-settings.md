---
title: Applying Speaker-Configuration Settings
description: Applying Speaker-Configuration Settings
ms.assetid: 98fe96cc-8436-4400-9b39-86d188e085c9
keywords:
- failed speaker-configuration requests WDK audio
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Applying Speaker-Configuration Settings


## <span id="applying_speaker_configuration_settings"></span><span id="APPLYING_SPEAKER_CONFIGURATION_SETTINGS"></span>


**Note**  This information applies to Windows XP and earlier operating systems. Starting with Windows Vista, **IDirectSound::GetSpeakerConfig** and **IDirectSound::SetSpeakerConfig** have been deprecated.

 

DirectSound keeps track of its current speaker-configuration setting in the registry and applies that setting to the audio hardware each time a new DirectSound device is created.

An application program can change the system-wide speaker configuration by calling the **IDirectSound::SetSpeakerConfig** method, which updates the speaker-configuration setting in the registry. The method also attempts to apply the new setting immediately to the hardware, although audio devices are typically unable to change speaker settings while the DirectSound object exists. For a list of the speaker configurations that DirectSound defines for this method, see [Translating Speaker-Configuration Requests](translating-speaker-configuration-requests.md).

A user can change the configuration through the speaker-configuration dialog in the **Multimedia Properties** page (mmsys.cpl) in Control Panel. To locate the DirectSound speaker-configuration dialog under Windows XP, for example, follow these steps:

1.  In Control Panel, double-click the **Sounds and Audio Devices** icon.

2.  On the **Audio** tab, select a device from the **Sound Playback** list.

3.  Click the **Advanced** button.

4.  Click the **Speakers** tab.

At this point, you should see the label **Speaker Setup** next to a list of the speaker configurations that you can select from.

DirectSound uses a [**KSPROPERTY\_AUDIO\_CHANNEL\_CONFIG**](https://msdn.microsoft.com/library/windows/hardware/ff537250) set-property request to send the speaker-configuration information to a 3D node or DAC node ([**KSNODETYPE\_3D\_EFFECTS**](https://msdn.microsoft.com/library/windows/hardware/ff537148) or [**KSNODETYPE\_DAC**](https://msdn.microsoft.com/library/windows/hardware/ff537158)) in an audio filter graph. For a 3D node, the target for the property request is actually the pin (3D-stream object) that feeds the node. For a DAC node, the target is the filter object that contains the DAC node. In either case, the speaker-configuration setting is global and affects the audio device as a whole. All audio applications that subsequently run are subject to the new setting until DirectSound changes the setting again.

Note that only versions of DirectSound that ship with Windows Me, and with Windows XP and later, send speaker-configuration property requests to DAC nodes--earlier versions of DirectSound do not support this feature. However, all versions of DirectSound send these requests to 3D nodes.

If an application program has created more than one 3D node, DirectSound sends speaker-configuration requests only to the first 3D node to be created.

DirectSound sends speaker-configuration requests to the 3D and DAC nodes each time an application creates a DirectSound object or calls the **IDirectSound::SetSpeakerConfig** method. Audio devices are typically unable to change their speaker configuration while they are managing active streams, and DirectSound tries to avoid this limitation where possible. For example, when creating a DirectSound object, DirectSound sends the speaker-configuration requests after instantiating the filter but before instantiating any pins on the filter--that is, before creating any streams.

This limitation is more difficult to avoid in the case of a call to **SetSpeakerConfig**. When an application calls **SetSpeakerConfig**, the adapter driver typically fails DirectSound's speaker-configuration request. This is because the DirectSound object already exists, which means that the device already has active streams to manage.

In this situation, the adapter driver has two options for dealing with a speaker-configuration request that it has failed:

-   The driver can remember the requested configuration and apply it just as soon as all its streams are destroyed.

-   The driver can ignore the request and rely on DirectSound to send another speaker-configuration request the next time that a DirectSound object is created.

The first option gives a better user experience because if the user selects a new setting through the speaker-configuration dialog, the change takes effect immediately in all applications--not just DirectSound applications. (Of course, if any audio applications are running at the time that the new setting is selected, the change is deferred until all audio applications terminate.) With the second option, however, the change does not take effect until a DirectSound application runs. For example, if an application that uses the Windows multimedia waveOut API is the first application to run after changing a Control Panel setting, the user may wonder why the new setting has no apparent effect.

In response to a speaker-configuration request sent to a 3D or DAC node, a typical adapter driver updates the speaker configuration in the audio hardware only if no pins are currently instantiated by any audio application. That means that if a waveOut application, for example, has one or more pins open at the time that a second application calls **DirectSoundCreate**, the driver might need to defer any pending changes to the audio device's speaker configuration until a later time.

If your driver is unable to fulfill a request to change the device's speaker-configuration, it should simply fail the request. Failing a speaker-configuration request during DirectSound object creation or a **SetSpeakerConfig** call does not cause the DirectSound object creation or **SetSpeakerConfig** call to fail.

At boot time, an audio adapter driver initializes the hardware's speaker configuration to its default setting, which is typically stereo. As soon as any application creates a DirectSound object, DirectSound applies the setting stored in the registry to the hardware. An application program must create a DirectSound device before it can call **SetSpeakerConfig** to change the speaker-configuration setting in the registry, but this registry setting typically takes effect in the hardware only after the DirectSound device is released and a second DirectSound device is created.

Immediately after installing an audio device or when a speaker-configuration error occurs, the DirectSound speaker configuration defaults to stereo.

 

 




