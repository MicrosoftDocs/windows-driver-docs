---
title: Exposing Your Synthesizer as a Legacy Device
description: Exposing Your Synthesizer as a Legacy Device
ms.assetid: 25e5e14f-1db5-45dc-9048-674420d79824
keywords:
- synthesizers WDK audio , legacy devices
- legacy device support WDK DirectMusic
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Exposing Your Synthesizer as a Legacy Device


## <span id="exposing_your_synthesizer_as_a_legacy_device"></span><span id="EXPOSING_YOUR_SYNTHESIZER_AS_A_LEGACY_DEVICE"></span>


You may want to write a single device driver that exposes your synth hardware as both a DirectMusic device and a legacy MIDI device (that is, through the Windows Multimedia midiOut*Xxx* API). This technique can be useful in the following three cases:

1.  If the device does not support DLS. Examples include the MPU-401 driver (see the mpu401 sample in the Windows Driver Kit \[WDK\]), a device that has only a ROM set, and a fixed-function software synth (for example, FM).

    In this case, the device can expose a legacy MIDI interface as well as a DirectMusic interface. It should expose only one legacy MIDI pin. It is important to list the pin with the legacy interface first so that WDM Audio enumerates it as a legacy MIDI device.

2.  If the device does support DLS, but powers up in a loaded state. This device has both RAM for DLS and ROM containing GM/GS/XG wave tables.

    In this case, the device can also expose both interfaces. If the two interfaces are mutually exclusive (that is, if once you download something, the ROM is not visible), then it should be a single pin with two interfaces to choose from (as opposed to two pins).

3.  When the device does support DLS, but powers up "empty" (for example, the DirectMusic software synth) and thus needs DLS downloads to initialize its wave table.

    This initialization is unnecessary if the device does not require DLS downloads (if it has a default sample set in ROM, for example) or if a DirectMusic pin is opened (the DirectMusic APIs ensure that DLS downloads occur).

    Exposing your DLS device through the legacy APIs requires some extra work. When a legacy pin is opened on a device that requires DLS instruments, the driver should locate and open a file containing the DLS collection to be used. The driver should then intercept update and bank changes, retrieve the appropriate data from the DLS file, and perform the necessary DLS downloads to the device.

    This case is problematic because the [WDMAud system driver](user-mode-wdm-audio-components.md#wdmaud_system_driver) and other clients are not aware that they need to download a collection. They just start sending MIDI update changes and notes.

 

 




