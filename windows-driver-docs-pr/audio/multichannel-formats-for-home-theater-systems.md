---
title: Multichannel Formats for Home-Theater Systems
description: Multichannel Formats for Home-Theater Systems
ms.assetid: b8bd1dc7-c9a8-4f4f-8014-d31f1ae5361a
keywords:
- data formats WDK audio
- formats WDK audio , data
- audio data formats WDK
- formats WDK audio , multichannel
- multichannel formats WDK audio
- home-theater systems WDK audio
- speakers WDK audio , home-threater systems
- audio drivers WDK , home-theater systems
- WDM audio drivers WDK , home-theater systems
- 7.1 home theater speakers WDK audio
- 7.1 wide configuration speakers WDK audio
- wide configuration speakers WDK audio
- 5.1 surround sound speakers WDK audio
- surround sound speakers
- Sony Dynamic Digital Sound
- SDDS configuration WDK audio
- stream formats WDK audio , multichannel
- positions WDK audio
- WDM audio data formats WDK
- data formats WDK audio , multichannel
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Multichannel Formats for Home-Theater Systems


A relatively inexpensive solution for a home-theater system is to connect a set of surround-sound speakers to an audio adapter on a computer that is running the Windows operating system. Alternately, the user can connect an external audio/video (A/V) receiver between the adapter outputs and the speakers. In response to the popularity of home-theater systems, 5.1- and 7.1-channel audio content that has been authored for these systems is becoming increasingly available.

To accurately render multichannel audio content on a home-theater system requires an audio-format descriptor that can assign speaker positions to audio channels in multichannel streams. As discussed previously, the [**WAVEFORMATEXTENSIBLE**](https://msdn.microsoft.com/library/windows/hardware/ff538802) structure can specify such speaker assignments.

To help provide audio driver support for home-theater systems, Microsoft has defined a new 7.1-channel speaker configuration for Microsoft Windows XP and later. This configuration is supported in Windows Vista, Windows XP with Service Pack 2 (SP2), and Windows Server 2003 with Service Pack 1 (SP1). It is not supported in Windows Server 2003 with no service packs installed, Windows XP with Service Pack 1, or Windows XP with no service packs installed.

The new 7.1-channel speaker configuration is shown in the following figure, which is taken from the Windows multimedia control panel (Mmsys.cpl) in Windows XP with SP2.

![figure of the new 7.1-channel speaker configuration ](images/spkrcfg1new.gif)

The Windows multimedia control panel assigns the name "7.1 home theater speakers" to the new 7.1-channel wide speaker configuration shown in the preceding figure.

The following figure shows the older 7.1-channel configuration, which is supported in Windows 2000 and later and in Windows Me/98.

![figure of the older 7.1-channel wide configuration](images/spkrcfg1old.gif)

In Windows XP with SP2, the multimedia control panel assigns the name "7.1 wide configuration speakers" to the older configuration shown in the preceding figure.

In Windows XP with SP2, you can find the two configurations shown in the two preceding figures by following these steps:

1.  In Control Panel (Category View), click **Sounds, Speech, and Audio Devices**.

2.  In the **Sounds, Speech, and Audio Devices** pane, under **Pick a task**, click **Adjust the system volume**.

3.  In the **Sounds and Audio Devices Properties** property sheet, on the **Volume** tab, under **Speaker settings**, click **Advanced**.

4.  In the **Advanced Audio Properties** property sheet, under **Speaker setup**, open the drop-down list and select one of the two 7.1 speaker configurations.

The configuration shown in the 7.1 Wide Configuration Speakers figure is the Sony Dynamic Digital Sound (SDDS) configuration, which was introduced in 1993 for use in motion picture theaters. However, few, if any, home-theater systems use this configuration. Instead, 8-speaker home-theater systems are likely to use the new 7.1 configuration shown in the 7.1 Home Theater Speakers figure. In addition, minimal home theater content has been authored for the SDDS configuration, and users can expect most of the available 7.1-channel content to be formatted for the new 7.1 configuration.

Although the new "7.1 home theaters speakers" configuration largely supplants the old "7.1 wide configuration speakers" configuration, Windows will continue to support the old configuration, to provide backward compatibility.

In Windows 2000 and later and in Windows Me/98, the 5.1-channel speaker configuration assigns channels 5 and 6 to the back-left and back-right speakers, respectively. In Windows Vista, Windows Server 2003 with SP1, and Windows XP with SP2, the 5.1-channel configuration remains unchanged. In contrast to the 7.1-channel configuration, these Windows versions do not define a new 5.1 format descriptor to distinguish the 5.1 side-speaker configuration from the 5.1 back-speaker configuration. Because the two configurations are so similar, defining two 5.1 configurations might have caused confusion among users regarding which configuration to use and whether to play content authored for one configuration on the other configuration. When positioning the speakers in a 6-speaker home-theater system, users tend not to distinguish between side and back speaker positions. Instead, speaker positioning is more likely to be determined by the shape of the room and the placement of the furniture in the room.

The 5.1-channel surround-sound speaker configuration is shown in the following figure, which is taken from the Windows multimedia control panel in Windows XP with SP2.

![figure of the 5.1-channel surround-sound speaker configuration ](images/spkrcfg2.gif)

The Windows multimedia control panel assigns the name "5.1 surround sound speakers" to the 5.1-channel speaker configuration shown in the preceding figure.

Although the differences between the 5.1-channel side-speaker and back-speaker configurations might be transparent to users, they are not transparent to audio hardware vendors. As mentioned previously, 5.1-channel content is typically authored for side speakers rather than for back speakers. Thus, when playing 5.1-channel content through the "7.1 home theater speakers" configuration, the vendor should ensure that the two side-speaker channels in the 5.1-channel stream play through the side speakers rather than the back speakers. Similarly, when playing content authored for the "7.1 home theater speakers" configuration through a 5.1 speaker configuration with side speakers, the channels for the 7.1 side speakers most naturally map to the side speakers in the 5.1 configuration. For an audio device with stream-processing capabilities, another alternative is for the device to attempt to preserve the content in channels 4 and 5 by mixing them with channels 6 and 7 before playing them through the side speakers in the 5.1 configuration.

This section includes:

[Channel Mask](channel-mask.md)

[Mapping Stream Formats to Speaker Configurations](mapping-stream-formats-to-speaker-configurations.md)

[Header File Changes](header-file-changes.md)

 

 




