---
title: USB Audio Class System Driver (Usbaudio.sys)
description: The USB Audio class system driver (Usbaudio.sys) is an AVStream minidriver that provides driver support for audio devices that comply with the Universal Serial Bus (USB) Device Class Definition for Audio Devices.
ms.assetid: 7ECE8006-3181-451C-B047-A3D767A7B98A
---

# USB Audio Class System Driver (Usbaudio.sys)


The USB Audio class system driver (Usbaudio.sys) is an AVStream minidriver that provides driver support for audio devices that comply with the Universal Serial Bus (USB) Device Class Definition for Audio Devices.

## <span id="usbaudio_class_system_driver"></span><span id="USBAUDIO_CLASS_SYSTEM_DRIVER"></span>


The USB Device Class Definition for Audio Devices specification (release 1.0) is available at the [USB Implementers Forum](http://go.microsoft.com/fwlink/p/?linkid=8780) website. Usbaudio.sys supports a subset of the features that are described in the USB Audio specification. In addition to Usbaudio.sys, there are several other kernel-mode audio components in the Windows Driver Model (WDM). For more information, see [Kernel-Mode WDM Audio Components](kernel-mode-wdm-audio-components.md).

In Windows 98 Usbaudio.sys introduced support for USB devices such as speakers and microphones. Support for MIDI devices was added in Windows Me.

When an audio device identifies itself as USB Audio-compliant during Plug and Play device enumeration, the system automatically loads the USBAudio driver to drive the device. USBAudio drives the device directly, without the aid of a proprietary adapter driver. This means that a device that complies with the USB audio specifications requires no proprietary adapter driver.

Microsoft recommends that hardware vendors use the USBAudio driver for their USB Audio devices instead of writing proprietary adapter drivers.

In Windows 98, the USBAudio driver supports the following features:

-   All Type I formats (except 8-bit signed PCM)

-   AC-3 Type II format

-   Synchronization types synchronous and adaptive

-   Multichannel devices

However, USBAudio in Windows 98 does not support:

-   8-bit signed PCM format

-   MPEG Type II format

-   Type III formats

-   USB MIDI

-   [**WAVEFORMATEXTENSIBLE**](https://msdn.microsoft.com/library/windows/hardware/ff538802) wave format (USBAudio uses packed WAVE\_FORMAT\_PCM for 24-bit data instead.)

In Windows 98 Second Edition (SE), Windows Me, and Windows 2000 and later, USBAudio supports all the same features as Windows 98, with one exception: USBAudio supports WAVEFORMATEXTENSIBLE but does not support packed WAVE\_FORMAT\_PCM for 24-bit data.

In Windows Me, and Windows XP and later, USBAudio supports all the features that are supported in Windows 98 SE and Windows 2000. In addition, Windows Me and Windows XP support USB MIDI but do not support USB MIDI Elements.

The following figure shows the driver hierarchy for a USB audio device. All of the driver components shown in the figure are provided by Microsoft with the operating system.

![diagram illustrating the driver hierarchy for a usb audio device](images/usbaudio.png)

For more information about the driver components in the figure, see the following sections:

[AVStream Overview](https://msdn.microsoft.com/library/windows/hardware/ff554240)

[System-Supplied USB Drivers](https://msdn.microsoft.com/library/windows/hardware/ff538853)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20USB%20Audio%20Class%20System%20Driver%20%28Usbaudio.sys%29%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


