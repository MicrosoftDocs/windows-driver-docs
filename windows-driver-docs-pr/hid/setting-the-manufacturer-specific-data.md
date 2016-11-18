---
title: Setting the Manufacturer-Specific Data
author: windows-driver-content
description: Setting the Manufacturer-Specific Data
MS-HAID:
- 'di\_100a2e20-fbc2-4fa0-a47d-e90b812d7f86.xml'
- 'hid.setting\_the\_manufacturer\_specific\_data'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 57787e7a-2a80-476c-8027-b7c154b2f407
keywords: ["INF files WDK joysticks , manufacturer-specific data"]
---

# Setting the Manufacturer-Specific Data


## <a href="" id="ddk-setting-the-manufacturer-specific-data-di"></a>


The manufacturer-specific section that the INF file points to contains one entry for each device that can be installed. Each entry contains the name of the device followed by the name of the install section, the device ID, and any compatible devices. If the device has been registered as Plug and Play compatible, then the Plug and Play ID (starting with an asterisk) should be used for the device ID. If the device has not been registered, then a device ID that is not Plug and Play compatible (that is, one not starting with an asterisk) should be used. When registering this type of device, avoid choosing an ID that conflicts with other device IDs ("Joystick," for example, would not be a good ID).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bhid\hid%5D:%20Setting%20the%20Manufacturer-Specific%20Data%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


