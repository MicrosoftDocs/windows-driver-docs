---
title: WDM Device Names for Smart Card Readers
description: WDM Device Names for Smart Card Readers
ms.assetid: 06f15b0d-d759-4cfe-a558-883f7f0d2581
keywords:
- smart card drivers WDK , device names
- device names WDK smart card
- names WDK smart card
- symbolic-link names WDK smart card
- kernel device names WDK smart card
- WDM device names WDK smart card
ms.date: 04/20/2017
ms.localizationpriority: medium
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

 

 





