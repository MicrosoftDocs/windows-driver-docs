---
Description: 'Proprietary Speaker-Configuration Utilities'
MS-HAID: 'audio.proprietary\_speaker\_configuration\_utilities'
MSHAttr: 'PreferredLib:/library/windows/hardware'
title: 'Proprietary Speaker-Configuration Utilities'
---

# Proprietary Speaker-Configuration Utilities


## <span id="proprietary_speaker_configuration_utilities"></span><span id="PROPRIETARY_SPEAKER_CONFIGURATION_UTILITIES"></span>


**Note**  This information applies to Windows XP and earlier operating systems. Starting with Windows Vista, **IDirectSound::GetSpeakerConfig** and **IDirectSound::SetSpeakerConfig** have been deprecated.

 

Hardware vendors occasionally provide proprietary speaker-configuration utilities to be used with their audio drivers in place of the speaker dialog in Control Panel. Such utilities have a potential problem: they sometimes change the speaker configuration in a proprietary way that fails to notify Windows of the change. This can result in a bad user experience if the settings in the proprietary utility do not match those in Control Panel. If you believe that your device requires a proprietary utility, you should take the following steps to integrate your utility with Windows:

1.  Implement a DAC node in your driver that supports the [**KSPROPERTY\_AUDIO\_CHANNEL\_CONFIG**](audio.ksproperty_audio_channel_config) property. Through this node, Windows informs the driver immediately of changes made by the user in Control Panel.

2.  Design your configuration utility to manage the speaker configuration by calling the DirectSound methods **GetSpeakerConfig** and **SetSpeakerConfig**.

The **SetSpeakerConfig** call informs DirectSound (and Windows) of changes that your utility makes to the speaker configuration. Also, your utility's initialization code should call **GetSpeakerConfig** to determine if the user has changed any settings through Control Panel. If so, the utility should reflect these changes in its user interface.

If your device supports multichannel formats that have no precise Windows equivalents, your configuration utility should do the following:

-   When changing to a speaker configuration that has no precise Windows equivalent, call **SetSpeakerConfig** with the closest Windows equivalent. This is in addition to making any proprietary calls that are needed to configure the driver.

-   When changing to a speaker configuration that does have a precise Windows equivalent, call **SetSpeakerConfig** to update the speaker mode.

If you make Windows more aware of your device's capabilities, DirectSound can enable some features that it could not otherwise enable (for example, multichannel 3D panning).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20Proprietary%20Speaker-Configuration%20Utilities%20%20RELEASE:%20%287/14/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")



