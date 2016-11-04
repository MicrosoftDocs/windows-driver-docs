---
title: DRM Overview
description: DRM Overview
ms.assetid: 81f47eca-aa8a-43c4-96c9-7446cba50d00
keywords: ["Digital Rights Management WDK audio , about DRM", "DRM WDK audio , about DRM", "DRMK system driver WDK audio", "decryption WDK audio"]
---

# DRM Overview


## <span id="drm_overview"></span><span id="DRM_OVERVIEW"></span>


DRM for digital audio is implemented on Microsoft Windows 2000 and later, and Windows Me/98. However, only Microsoft Windows XP and later, and Windows Me, implement DRM security within the kernel. Currently, Windows provides no DRM security for MIDI streams or for DLS sets.

DRM-protected digital content is stored in encrypted form on a disk or other storage-media type. The encryption algorithm scrambles the content to make it unintelligible until it has been decrypted. During playback, the content remains scrambled as it is read from the disk and buffered in memory. Near the end of the data path, the [DRMK system driver](kernel-mode-wdm-audio-components.md#drmk_system_driver) (Drmk.sys) unscrambles the data and feeds it directly to the audio driver to be played. By limiting the extent of the data path over which unscrambled content is transmitted, DRMK makes the content less vulnerable to unauthorized copying.

In Windows 2000 and Windows 98, a security loophole allows users to easily load rogue drivers that route the playback of secure content to disk in unencrypted form. Windows XP and later, and Windows Me, close this loophole by allowing only trusted audio drivers to play DRM-protected content.

In Windows XP and later, and Windows Me, secure content remains scrambled while it traverses the audio-data path until it enters the protected environment of the kernel. Within the kernel, protected components unscramble the data and feed the unscrambled data to a trusted driver for playback. When configuring a filter graph to play back an unscrambled audio stream, DRMK authenticates the adapter driver for each KS filter that it places in the graph. The system informs the driver of the usage rules for the protected content. The driver, in turn, advises DRMK of any downstream filters to which it routes the content, and the system authenticates those filters as well. This process continues until the graph is complete. The system rejects the entire graph if the digital playback stream passes through any component that is not DRM-compliant.

A DRM-compliant driver must prevent unauthorized copying while digital content is being played. In addition, the driver must disable all digital outputs that can transmit the content over a standard interface (such as S/PDIF) through which the decrypted content can be captured. Note that this requirement does not apply to USB devices. Currently, DRMK plays secure content only through a USB speaker device with no digital outputs.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20DRM%20Overview%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


