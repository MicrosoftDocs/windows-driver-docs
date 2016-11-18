---
title: Exposing Your Synthesizer as a Legacy Device
description: Exposing Your Synthesizer as a Legacy Device
ms.assetid: 25e5e14f-1db5-45dc-9048-674420d79824
keywords: ["synthesizers WDK audio , legacy devices", "legacy device support WDK DirectMusic"]
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20Exposing%20Your%20Synthesizer%20as%20a%20Legacy%20Device%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


