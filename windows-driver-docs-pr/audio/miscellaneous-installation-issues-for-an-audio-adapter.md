---
title: Miscellaneous Installation Issues for an Audio Adapter
description: Miscellaneous Installation Issues for an Audio Adapter
ms.assetid: fcfa9c41-7fad-4b22-9054-a1debb972580
keywords:
- audio adapters WDK , installing
- adapter drivers WDK audio , installing
- Port Class audio adapters WDK , installing
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Miscellaneous Installation Issues for an Audio Adapter


## <span id="miscellaneous_installation_issues_for_an_audio_adapter"></span><span id="MISCELLANEOUS_INSTALLATION_ISSUES_FOR_AN_AUDIO_ADAPTER"></span>


Listed are the most common installation issues for an audio adapter:

-   During initial installation of an audio device or when undergoing an operating system upgrade that destroys existing audio settings, the driver should ensure that the settings are initialized to reasonable default values. For more information, see [Default Audio Volume Settings](default-audio-volume-settings.md).

-   Sometimes during installation, an OEM would like to override the default audio volume level, or the default microphone boost level that is hard-coded by the Audio Class driver. This was not possible in earlier versions of Windows up to Windows 7. In Windows 8 and later, you can now customize the default values for these settings. For more information about how to do this, see [Customizing Default Audio Volume Settings](customizing-default-audio-volume-settings.md).

-   In Windows Vista and later operating systems, the default setting for the master volume level of an audio device is six decibels of attenuation, and it is set at the time of installation. This default master volume level setting, or any other level that you choose after installation, is maintained no matter how often you restart your computer. To opt out of volume level persistence you can use the AddProperty registry directive via an INF file, to set the value of the PKEY\_AudioDevice\_DontPersistControls registry key. For more information about how to do this, see [Opting Out of Volume Level Persistence](opting-out-of-volume-level-persistence.md).

-   During an operating system upgrade, an audio device's installed driver and registry settings can frequently be preserved. For guidelines on how to make this process transparent to users, see [Operating System Upgrades](operating-system-upgrades.md).

-   An audio driver is easily designed to allow multiple identical instances of an audio adapter card to be plugged into the same system. For more information, see [System-Wide Unique Device IDs](system-wide-unique-device-ids.md).

-   For a list of INF file keywords that are common to all device classes, see [INF File Sections and Directives](https://msdn.microsoft.com/library/windows/hardware/ff547433). However, this list does not contain several media-specific keywords. For more information, see [Media-Specific INF File Keywords](media-specific-inf-file-keywords.md).

-   For information about how an adapter driver or miniport driver can obtain setup information from the registry, see [Retrieving Device Setup Information](retrieving-device-setup-information.md).

-   For information about Windows Vista support for an audio adapter which does not have a physical volume control knob, see the [Windows Vista Software Volume Control Support](https://msdn.microsoft.com/library/windows/hardware/ff539263) topic.

 

 




