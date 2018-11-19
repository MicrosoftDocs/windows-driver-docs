---
title: Default Sound Sample Sets
description: Default Sound Sample Sets
ms.assetid: 9ffcb7ef-173f-4db9-85e8-2af7eb64cb75
keywords:
- hardware acceleration WDK audio
- miniport drivers WDK audio , kernel-mode hardware acceleration
- synthesizers WDK audio , kernel-mode hardware acceleration
- DirectMusic kernel-mode WDK audio , default sound sample sets
- kernel-mode synths WDK audio , default sound sample sets
- default sound sample sets
- sound sample sets WDK audio
- synthesizers WDK audio , default sound sets
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Default Sound Sample Sets


## <span id="default_sound_sample_sets"></span><span id="DEFAULT_SOUND_SAMPLE_SETS"></span>


Some synthesizers ship with a default sound set that conforms to General MIDI or some extension thereof. This sound set is provided for applications that do not support sample downloading or desire a default sound set to use in conjunction with downloaded samples. There are two possible delivery mechanisms for such a sound set: as a prepackaged DLS set, or as a ROM set.

In the case of the prepackaged DLS set, management of the set is delegated to DirectMusic. Microsoft provides a default DLS set based on the Roland GS samples. Manufacturers wishing to use a different default set with their hardware should contact the DirectMusic group at Microsoft. Sample sets provided in this manner should not set the capabilities bits indicating hardware support for a sample set; only ROM sets should set these bits.

ROM sets are also managed by the system. In order to preserve maximum sample memory for use by downloadable samples, the miniport driver should not load the entire ROM set into sample RAM. (This is not an issue for hardware that can play samples directly out of ROM.) The system provides instrument download requests for needed updates before the update change itself is delivered. If an instrument download refers to an update in the ROM sample set, then the **dwDLId** member of the DMUS\_DOWNLOADINFO structure (described in the Microsoft Windows SDK documentation) contains the tag DOWNLOAD\_ID\_ROMSET (defined as 0xFFFFFFFF).

 

 




