---
title: Proprietary Speaker-Configuration Utilities
description: Proprietary Speaker-Configuration Utilities
ms.assetid: d04b8c1b-13c6-422f-b13a-909f7074ac75
keywords:
- proprietary speaker-configuration utilities WDK audio
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Proprietary Speaker-Configuration Utilities


## <span id="proprietary_speaker_configuration_utilities"></span><span id="PROPRIETARY_SPEAKER_CONFIGURATION_UTILITIES"></span>


**Note**  This information applies to Windows XP and earlier operating systems. Starting with Windows Vista, **IDirectSound::GetSpeakerConfig** and **IDirectSound::SetSpeakerConfig** have been deprecated.

 

Hardware vendors occasionally provide proprietary speaker-configuration utilities to be used with their audio drivers in place of the speaker dialog in Control Panel. Such utilities have a potential problem: they sometimes change the speaker configuration in a proprietary way that fails to notify Windows of the change. This can result in a bad user experience if the settings in the proprietary utility do not match those in Control Panel. If you believe that your device requires a proprietary utility, you should take the following steps to integrate your utility with Windows:

1.  Implement a DAC node in your driver that supports the [**KSPROPERTY\_AUDIO\_CHANNEL\_CONFIG**](https://msdn.microsoft.com/library/windows/hardware/ff537250) property. Through this node, Windows informs the driver immediately of changes made by the user in Control Panel.

2.  Design your configuration utility to manage the speaker configuration by calling the DirectSound methods **GetSpeakerConfig** and **SetSpeakerConfig**.

The **SetSpeakerConfig** call informs DirectSound (and Windows) of changes that your utility makes to the speaker configuration. Also, your utility's initialization code should call **GetSpeakerConfig** to determine if the user has changed any settings through Control Panel. If so, the utility should reflect these changes in its user interface.

If your device supports multichannel formats that have no precise Windows equivalents, your configuration utility should do the following:

-   When changing to a speaker configuration that has no precise Windows equivalent, call **SetSpeakerConfig** with the closest Windows equivalent. This is in addition to making any proprietary calls that are needed to configure the driver.

-   When changing to a speaker configuration that does have a precise Windows equivalent, call **SetSpeakerConfig** to update the speaker mode.

If you make Windows more aware of your device's capabilities, DirectSound can enable some features that it could not otherwise enable (for example, multichannel 3D panning).

 

 




