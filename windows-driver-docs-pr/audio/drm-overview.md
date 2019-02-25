---
title: DRM Overview
description: DRM Overview
ms.assetid: 81f47eca-aa8a-43c4-96c9-7446cba50d00
keywords:
- Digital Rights Management WDK audio , about DRM
- DRM WDK audio , about DRM
- DRMK system driver WDK audio
- decryption WDK audio
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# DRM Overview


## <span id="drm_overview"></span><span id="DRM_OVERVIEW"></span>


DRM for digital audio is implemented on Microsoft Windows 2000 and later, and Windows Me/98. However, only Microsoft Windows XP and later, and Windows Me, implement DRM security within the kernel. Currently, Windows provides no DRM security for MIDI streams or for DLS sets.

DRM-protected digital content is stored in encrypted form on a disk or other storage-media type. The encryption algorithm scrambles the content to make it unintelligible until it has been decrypted. During playback, the content remains scrambled as it is read from the disk and buffered in memory. Near the end of the data path, the [DRMK system driver](kernel-mode-wdm-audio-components.md#drmk_system_driver) (Drmk.sys) unscrambles the data and feeds it directly to the audio driver to be played. By limiting the extent of the data path over which unscrambled content is transmitted, DRMK makes the content less vulnerable to unauthorized copying.

In Windows 2000 and Windows 98, a security loophole allows users to easily load rogue drivers that route the playback of secure content to disk in unencrypted form. Windows XP and later, and Windows Me, close this loophole by allowing only trusted audio drivers to play DRM-protected content.

In Windows XP and later, and Windows Me, secure content remains scrambled while it traverses the audio-data path until it enters the protected environment of the kernel. Within the kernel, protected components unscramble the data and feed the unscrambled data to a trusted driver for playback. When configuring a filter graph to play back an unscrambled audio stream, DRMK authenticates the adapter driver for each KS filter that it places in the graph. The system informs the driver of the usage rules for the protected content. The driver, in turn, advises DRMK of any downstream filters to which it routes the content, and the system authenticates those filters as well. This process continues until the graph is complete. The system rejects the entire graph if the digital playback stream passes through any component that is not DRM-compliant.

A DRM-compliant driver must prevent unauthorized copying while digital content is being played. In addition, the driver must disable all digital outputs that can transmit the content over a standard interface (such as S/PDIF) through which the decrypted content can be captured. Note that this requirement does not apply to USB devices. Currently, DRMK plays secure content only through a USB speaker device with no digital outputs.

 

 




