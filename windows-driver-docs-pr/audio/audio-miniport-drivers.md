---
Description: Audio Miniport Drivers
MS-HAID: 'audio.audio\_miniport\_drivers'
MSHAttr: 'PreferredLib:/library/windows/hardware'
title: Audio Miniport Drivers
---

# Audio Miniport Drivers


## <span id="audio_miniport_drivers"></span><span id="AUDIO_MINIPORT_DRIVERS"></span>


This section describes audio miniport driver interfaces and explains how to develop adapter drivers for audio hardware whose registers are directly accessible to the system processor over a system bus. This class of hardware includes all ISA/DMA, PCMCIA, and PCI audio adapters.

This documentation does not discuss how to support audio devices that reside on an external bus. For information about supporting audio devices on external buses, see [USBAudio Class System Driver](kernel-mode-wdm-audio-components.md#usbaudio-class-system-driver) and [AVCAudio Class System Driver](kernel-mode-wdm-audio-components.md#avcaudio-class-system-driver).

The following discussion assumes that the reader is familiar with kernel streaming (KS) concepts. For background information, see [Kernel Streaming](stream.kernel_streaming).

The WDM audio driver model divides the implementation of a KS filter into port and miniport drivers that are complementary but separate. This division makes audio hardware drivers easier to write by isolating generic filter-implementation issues from device-specific hardware-interface issues. Hardware vendors write miniport drivers to directly control their hardware devices, but the port drivers that implement the KS filters are provided with the operating system. The port and miniport drivers communicate with each other through well-defined software interfaces.

Various aspects of miniport driver development are discussed in the following topics:

[Introduction to Port Class](introduction-to-port-class.md)

[Supporting a Device](supporting-a-device.md)

[COM in the Kernel](com-in-the-kernel.md)

[Adapter Driver Construction](adapter-driver-construction.md)

[Miniport Driver Types by Operating System](miniport-driver-types-by-operating-system.md)

[Miniport Interfaces](miniport-interfaces.md)

[Installing a Port Class Audio Adapter](installing-a-port-class-audio-adapter.md)

[Port Driver Helper Objects](port-driver-helper-objects.md)

[Power Management for Audio Devices](power-management-for-audio-devices.md)

[Version Numbers for Audio Drivers](version-numbers-for-audio-drivers.md)

[Other Implementation Issues for Audio Drivers](other-implementation-issues-for-audio-drivers.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20Audio%20Miniport%20Drivers%20%20RELEASE:%20%287/14/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")


