---
Description: Vendor Audio Driver Options
MS-HAID: 'audio.vendor\_audio\_driver\_options'
MSHAttr: 'PreferredLib:/library/windows/hardware'
title: Vendor Audio Driver Options
---

# Vendor Audio Driver Options


## <span id="vendor_audio_driver_options"></span><span id="VENDOR_AUDIO_DRIVER_OPTIONS"></span>


To take advantage of the built-in system support for audio devices, Microsoft recommends that vendors use one of the following:

-   A port class adapter driver (see [Audio Miniport Drivers](audio-miniport-drivers.md)) for an ISA or PCI adapter card

-   The USB Audio class driver (see [USBAudio Class System Driver](kernel-mode-wdm-audio-components.md#usbaudio-class-system-driver)) for a USB Audio device

-   A custom IEEE 1394 device driver (see [AVCAudio Class System Driver](kernel-mode-wdm-audio-components.md#avcaudio-class-system-driver)) for an IEEE 1394 audio device

However, if these options are not sufficient, a vendor can implement one of the following:

-   A proprietary KS filter (see [KS Filters](stream.ks_filters))

-   Microsoft does not recommend a proprietary KS filter because they are difficult to implement, and are unnecessary for most ISA, PCI, and USB devices.

-   Stream class minidriver (see [Streaming Minidrivers](stream.streaming_minidrivers2))

-   Microsoft does not recommend a proprietary stream class minidriver because it is difficult to implement, although it can be appropriate for devices that integrate audio and video.

For an in-depth discussion of the available options for providing driver support for an audio device, see [Getting Started with WDM Audio Drivers](getting-started-with-wdm-audio-drivers.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20Vendor%20Audio%20Driver%20Options%20%20RELEASE:%20%287/14/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")


