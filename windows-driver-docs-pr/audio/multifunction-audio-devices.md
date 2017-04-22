---
title: Multifunction Audio Devices
description: Multifunction Audio Devices
ms.assetid: 6ef54b12-d0ea-4e55-afee-61f834375b92
keywords:
- WDM audio drivers WDK , multifunction devices
- audio drivers WDK , multifunction devices
- multifunction audio devices WDK
- subdevices WDK audio
- multifunction audio devices WDK , about multifunction audio devices
- multiple function audio devices WDK audio
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Multifunction Audio Devices


## <span id="multifunction_audio_devices"></span><span id="MULTIFUNCTION_AUDIO_DEVICES"></span>


A multifunction device is a single adapter card that incorporates two or more separate functions (or subdevices). A multifunction device can contain two or more audio subdevices. It may also span device classes. A device containing audio and modem subdevices, for instance, belongs to both the media class and the modem class. For more information, see [Supporting Multifunction Devices](https://msdn.microsoft.com/library/windows/hardware/ff542743).

The WavePci port driver in PortCls places special requirements on multifunction devices. In particular, an adapter driver must provide a way to configure each subdevice so that it can be controlled independently of the other subdevices in a multifunction device. This can be accomplished by setting up the PCI configuration space for your multifunction device in one of two ways:

1.  The preferred method is to assign a separate device ID to each logically distinct subdevice on your multifunction device. If your multifunction device contains modem, audio, and joystick subdevices, for example, the system should be able to represent each subdevice as an independent devnode in the [device tree](https://msdn.microsoft.com/library/windows/hardware/ff543194). The subdevice represented by each device ID has its own set of PCI configuration registers and is orthogonal to and independent of the other subdevices. For instance, enabling or disabling one subdevice (the audio subdevice, for example) should have no effect on any other subdevice (the modem, for example). This type of multifunction device requires no special hardware-specific driver support apart from the proprietary drivers for the subdevices themselves.

2.  A second way to design a multifunction device is to assign a single device ID to the device as a whole and to provide separate PCI base-address registers (BARs) for the individual subdevices. In this scheme, the subdevices share a common set of configuration registers but each subdevice has its own BAR or BARs. The system multifunction driver (for example, *Mf.sys* on Microsoft Windows 2000 and later; see [Using the System-Supplied Multifunction Bus Driver](https://msdn.microsoft.com/library/windows/hardware/ff542778)) can configure the base address for each subdevice's status, command, and data registers independently of the registers for the other functions. If your device's BARs are not logically separable by subdevice, you cannot use PortCls to manage your device.

The remainder of this section describes the steps necessary to implement approach (2) in the preceding list. The following topics are discussed:

[Multiple Audio Subdevices](multiple-audio-subdevices.md)

[Multifunction Device Limits](multifunction-device-limits.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20Multifunction%20Audio%20Devices%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


