---
title: SysTray and SndVol32
description: SysTray and SndVol32
ms.assetid: 53f8c5be-d0a5-4364-8fac-813cf9f8318c
keywords:
- SysTray WDK audio
- SndVol32 WDK audio
- master volume settings WDK audio
- speakers WDK audio , icon display
- volume settings WDK audio
- icons WDK audio
- displaying speaker icons
- volume sliders WDK audio
- hidden speaker icons WDK audio
- mute control WDK audio
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# SysTray and SndVol32


## <span id="systray_and_sndvol32"></span><span id="SYSTRAY_AND_SNDVOL32"></span>


The SndVol32 program (Sndvol32.exe) controls both the volume settings for various sound sources (such as wave, CD, and synthesizer) and the master volume setting. The SndVol32 program is represented as a speaker icon that appears in the system-tray notification area the taskbar, which appears in the lower-right corner of the Windows screen by default.

The SysTray program (Systray.exe) is responsible for displaying the speaker icon when it is turned on and for hiding the speaker icon when it is turned off. In Windows XP, the speaker icon is hidden by default. In all other Windows versions, including Windows XP SP1, the speaker icon is visible by default.

In Windows XP, follow these steps to display the speaker icon on the taskbar:

1.  In Control Panel, click the **Sounds and Audio Devices** icon (or simply run mmsys.cpl).

2.  On the **Volume** tab, select the **Place volume icon in the taskbar** check box.

If your sound card's volume level can be changed under software control, a speaker icon appears on the taskbar. You can change the master-volume setting by single-clicking on that icon and adjusting the volume slider.

At logon time, SysTray queries the audio driver for a mixer line with a MIXERLINE\_COMPONENTTYPE\_DST\_SPEAKERS (speaker destination) or MIXERLINE\_COMPONENTTYPE\_DST\_HEADPHONES (headphone destination) component type to determine whether the speaker icon should be displayed. If neither of these component types is found, SysTray does not display the speaker icon. If it does find the line, it queries the line to determine whether it contains a mute control. SysTray completes its logon-time mixer-line processing by internally storing the **line ID** and **mute control ID** for future reference.

The SndVol32 program also provides a user interface for controlling all volume controls in the system. When a user double-clicks the speaker icon in the system tray (or simply runs Sndvol32.exe), SndVol32 displays a "Master Volume" window, which contains sliders for controlling both the master volume level and the volume levels on the various sound sources. In this case, SndVol32 uses a different algorithm to determine what it displays. For the **master volume slider**, it looks for the first volume control on the "master" destination (for example, the destination that is numbered zero). This is typically the speaker destination.

When SndVol32 runs, it queries the mixer-line driver looking for a set of controls that it knows about. To display a slider panel, the SOURCE line should have at least one of the following controls:

-   Volume control

-   Mute control

-   Advanced control (AGC, bass, or treble)

If none of these controls is found, SndVol32 does not display the panel. A source line simply being part of a MUX with no controls is not sufficient for display. This restriction is easily circumvented by inserting a fake MUTE control into the topology to get the panels to display. When the line simply feeds into a MUX, the **Select** box displayed for MUXes hides the MUTE control.

WDM Audio topology nodes that do not map well into a mixer line control are not displayed by SndVol32. Refer to [Topology Nodes](topology-nodes.md) for details on which nodes are translated into mixer-line controls. The WDM mixer-line driver translates some nodes into controls, but SndVol32 displays only the set of controls that it knows about.

For information about the volume ranges and the default volume levels in the various versions of Windows, see [Default Audio Volume Settings](default-audio-volume-settings.md).

 

 




