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
ms.date: 04/20/2017
ms.localizationpriority: medium
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

 

 




