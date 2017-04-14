---
title: Creating an INF File
author: windows-driver-content
description: Creating an INF File
ms.assetid: c45fb42c-f0d6-4ab8-9a19-4bbf98c4cf8c
keywords: ["joysticks WDK HID , INF files", "virtual joystick drivers WDK HID , INF files", "VJoyD WDK HID , INF files", "INF files WDK joysticks", "INF files WDK joysticks , creating"]
---

# Creating an INF File


## <a href="" id="ddk-creating-an-inf-file-di"></a>


All minidrivers and OEM-defined joysticks should be installed using an INF file to provide all the necessary information to the system. An INF file describes a device installation in terms of the class of the device, the files that need to be copied, any compatible devices, any system resources the device requires, and changes to the registry. INF files for customizing the standard analog driver do not need to copy any files, state compatible devices, or specify system resources. The INF file can specify other actions, such as modifying the Autoexec.bat file, but this is not usually necessary for a joystick minidriver.

The INF file contains the elements described in the following topics:

[Setting the Device Class](setting-the-device-class.md)

[Selecting Source Files](selecting-source-files.md)

[Setting the Manufacturer-Specific Data](setting-the-manufacturer-specific-data.md)

[Setting Up LogConfig Entries](setting-up-logconfig-entries.md)

[Setting Up AddReg Entries](setting-up-addreg-entries.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bhid\hid%5D:%20Creating%20an%20INF%20File%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


