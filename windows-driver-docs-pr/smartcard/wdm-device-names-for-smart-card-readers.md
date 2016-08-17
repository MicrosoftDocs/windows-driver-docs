---
title: WDM Device Names for Smart Card Readers
description: WDM Device Names for Smart Card Readers
ms.assetid: 06f15b0d-d759-4cfe-a558-883f7f0d2581
keywords: ["smart card drivers WDK , device names", "device names WDK smart card", "names WDK smart card", "symbolic-link names WDK smart card", "kernel device names WDK smart card", "WDM device names WDK smart card"]
---

# WDM Device Names for Smart Card Readers


## <span id="_ntovr_wdm_device_names_for_smart_card_readers"></span><span id="_NTOVR_WDM_DEVICE_NAMES_FOR_SMART_CARD_READERS"></span>


For WDM device drivers, the kernel device name is a name that is known only in the name space of the kernel. The symbolic-link name is the name that a Microsoft Win32 application uses to communicate with the driver.

Because the kernel device name is known only within the kernel name space, the driver developer can choose the name, but it must comply with the naming conventions for device names in Windows operating systems. In particular, a device name must look like this:

*\\Device\\DeviceName\[Unit\]*

where *DeviceName* is a name that reflects the type of driver, and *Unit* is the zero-based unit number of that driver. The unit number is used to distinguish one device from another when there is more than one device of that type installed in a system.

Because every driver must communicate with the smart card resource manager, the device must have a name that is accessible in the Win32 name space. This symbolic-link name must look like this:

*\\DosDevices\\SCReader\[Unit\]*

The unit number for the device in the Win32 name space does not have to be the same as the one used to form the kernel device name. It should be the first available unit number. Use [**SmartcardCreateLink (WDM)**](https://msdn.microsoft.com/library/windows/hardware/ff548935) to automatically generate a symbolic-link name.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[smartcrd\smartcrd]:%20WDM%20Device%20Names%20for%20Smart%20Card%20Readers%20%20RELEASE:%20%287/20/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




