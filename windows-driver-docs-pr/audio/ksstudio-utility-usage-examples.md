---
title: KsStudio - Usage examples
description: This topic provides three usage examples for troubleshooting WDM audio issues using  the KSStudio utility.
keywords:
- KsStudio utility WDK audio
- audio filters WDK audio , KsStudio utility
- KS filter graphs WDK audio , KsStudio utility
- filter graphs WDK audio , KsStudio utility
- testing KS filter graphs WDK audio
- audio filter graphs WDK
- graphical representation WDK audio
ms.date: 04/22/2021
ms.localizationpriority: medium
---

# KsStudio - Usage examples

This topic provides three usage examples for troubleshooting WDM audio issues using  the KSStudio utility. For more information, see [KSStudio Utility](ksstudio-utility.md).

## Example 1: Audio does not appear to work 

**Scenario:** 

Developer installs audio device driver, but player app (for example Windows Media Player) indicates that no audio device is available. 

**Troubleshooting:** 

1) *Does the device appear in device manager?* If yes, go to step (2), else there is a problem with the INF file used to install the device. 

2) *Does the device have a yellow exclamation mark?* If yes, then the device was not successfully installed (view the properties of the device for further information), else goto step (3). 

3) Launch KSStudio. Enumerate filters of class KSCATEGORY_AUDIO and KSCATEGORY_AUDIO_DEVICE. Do(es) the filter(s) corresponding to the audio device show up under KSCATEGORY_AUDIO? If yes, goto (4), else the filter factory is not being registered correctly. The most common cause of this is a mismatch between the XXX guid in the INF and the XXX guid in the source code for the filter. 

4) KSCATEGORY_AUDIO_DEVICE filters are virtual filters that represent portions of the system-built audio graph. For more information see [Kernel-Mode WDM Audio Components](kernel-mode-wdm-audio-components.md) and [Virtual Audio Devices](virtual-audio-devices.md). In general these virtual filters are what the higher level APIs access. 

*Does a virtual filter factory corresponding to the aforementioned _AUDIO filter factory exist (it will be obvious if they do)?* If yes, go to (5), else the driver has a problem that caused sysaudio to reject it. Instantiate the corresponding _AUDIO device. This will cause KSStudio to profile the filter. Look for errors (red text) in the logging windows. Examine the filter in the "Instantiated objects" view. Compare with a filter (perhaps one of the DDK sample drivers or one from another manufacturer) that is working. 

5) Run mmsys.cpl and see if any devices corresponding to the filter under development are shown. This is the view of the device through the MMSystem APIs. If no device is shown here, then there is something peculiar about the device that caused MMSystem to reject it. Go back to KSStudio and instantiate the KSCATEGORY_AUDIO_DEVICE virtual filter factory corresponding to your device. Look for errors (red text) in the logging windows. Examine the filter in the "Instantiated objects" view. Compare with a filter (perhaps one of the WDK sample audio drivers or one from another manufacturer) that is working. 

## Example 2: Audio mixer lines are missing 

**Scenario:** 

Audio device is installed. One or more expected mixer lines is missing from SndVol32 (or other mixer application) 

**Troubleshooting:** 

1) *Does the filter's topology look correct in KSStudio?* Lauch KSStudio and enumerate KSCATEGORY_AUDIO. Instantiate your Topology filter and choose the View Nodes option in the Object Topology View. Does the filter topology look correct? If so repeat for the corresponding KSCATEGORY_AUDIO_DEVICE filter. If this topology looks reasonable go to (2), else there is some problem in your topology filter that prevents expression of the topology to components higher in the audio stack. For more information on how filter topology is translated into mixer lines, see the DDK documentation. 

2) *Do the mixer lines show up as expected in MixApp?* MixApp is a very simple but useful Windows SDK sample app. If the mixer lines look correct in MixApp, but not in the problematic mixer application cited earlier, then it is likely an app bug. 

## Example 3: Audio mixer controls are missing or non-functional 

**Scenario:** 

Mixer controls (MMSystem mixer API) are either not showing up, or do not appear to work in SndVol32 or another mixer application. 

**Troubleshooting:** 

1) Go through the troubleshooting in Example 2 above. 

2) *Does hardware event support appear to work in KSStudio?* Find the node or pin that supports the KSEVENT_CONTROL_CHANGE event and enable it as described in [KSStudio - KSProperties and Events](ksstudio-utility-ksproperties-and-events.md). Toggle the hardware controls. This should cause the event lightbulb icon to flash. 


## See also

[KSStudio Utility](ksstudio-utility.md)

[KSStudio - Filters and Filter Factories](ksstudio-utility-filters-and-filter-factories.md)

[KSStudio - Pins and Nodes](ksstudio-utility-pins-and-nodes.md)

[KSStudio - KSProperties and Events](ksstudio-utility-ksproperties-and-events.md)

[KSStudio - KS Monitor](ksstudio-utility-ks-monitor.md)

 




