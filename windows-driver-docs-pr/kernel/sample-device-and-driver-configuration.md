---
title: Sample Device and Driver Configuration
author: windows-driver-content
description: Sample Device and Driver Configuration
MS-HAID:
- 'WDMIntro\_847b42e8-f7ce-44b0-a34f-0cd2a6474620.xml'
- 'kernel.sample\_device\_and\_driver\_configuration'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 803262b2-0882-46d0-9c4f-63e59eb4beaa
keywords: ["WDM drivers WDK kernel , configurations", "WDM drivers WDK kernel , layered drivers", "layered drivers WDK kernel", "driver layers WDK WDM", "keyboards WDK kernel", "mouse WDK kernel", "hardware configurations WDK kernel", "intermediate drivers WDK kernel"]
---

# Sample Device and Driver Configuration


## <a href="" id="ddk-sample-device-and-driver-configuration-kg"></a>


This section illustrates the relationship between the hardware and driver configurations, using the keyboard and mouse devices as an example. Configurations differ for other devices. For complete information about any device configuration, see the device-specific documentation in the Windows Driver Kit (WDK).

### <a href="" id="keyboard-and-mouse-hardware-configurations"></a>

The following figure shows two possible hardware configurations for the keyboard and mouse devices:

-   Each connected directly somewhere on the system bus

-   Both connected through a keyboard and auxiliary device controller

![diagram illustrating keyboard and mouse hardware configurations](images/2kbdmuhw.png)

### <a href="" id="keyboard-and-mouse-driver-layers"></a>

The following figure illustrates the corresponding layered drivers for I/O operations on the devices shown in the previous figure.

![keyboard and mouse driver layers](images/2samplyr.png)

Note that drivers of keyboard and mouse devices, whatever the hardware configuration, can use the system's keyboard class and mouse class drivers to handle hardware-independent operations. These are called [*class drivers*](https://msdn.microsoft.com/library/windows/hardware/ff556274#wdkgloss-class-driver) because each supplies system-required but hardware-independent support for a particular class of device.

A corresponding [*port driver*](https://msdn.microsoft.com/library/windows/hardware/ff556325#wdkgloss-port-driver) implements the device-specific support to carry out required I/O operations on each physical device. The system's (i8042) keyboard and auxiliary device port driver for x86-based platforms manages device-specific operations for both mouse and keyboard. In a hardware configuration where each device is separately connected, as shown in the figure illustrating the keyboard and mouse hardware configurations, each system class driver can be layered over separate device-specific port drivers, or a single driver for each device could be implemented as a separate, monolithic (lowest-level) driver.

A new intermediate driver, such as a PnP filter driver, could be added to the configuration in the figure illustrating the keyboard and mouse driver layers. For example, a filter driver added above the keyboard class driver might filter keyboard input in a platform-specific manner before passing it through the I/O services to the subsystem that requested it. Such a filter driver must recognize the same IRPs and IOCTLs as the keyboard class driver.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Sample%20Device%20and%20Driver%20Configuration%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


