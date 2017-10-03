---
title: USB 2.0 Audio Driver
description: Starting with Windows 10, release 1703, a USB 2.0 driver is shipped with Windows. This driver provides basic functionality.
ms.author: windowsdriverdev
ms.date: 04/25/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

### Overview

Starting with Windows 10, release 1703, a USB 2.0 driver is shipped with Windows. This driver provides basic functionality including:

- The driver is designed to support the USB Audio 2.0 device class. For more information see [http://www.usb.org/developers/docs/devclass_docs/](http://www.usb.org/developers/docs/devclass_docs/)
- The driver is a WaveRT Audio Port Class
- The driver supports power management including USB selective suspend
- DRM and copy protected content is not supported 

The driver is named: _usbaudio2.sys_ and the associated inf file is _usbaudio2.inf_.

The driver will identify in device manager as "USB Audio Class 2 Device". This name will be overwritten with USB Product string, if it is available.

The driver is automatically enabled for when a compatible device is attached to the system.

 
### Additional Information for OEM and IHVs

OEMs and IHVs should test their existing and new devices against the supplied in-box driver.

There is not and any specific partner customization that is associated with the in-box USB Audio 2.0 driver.

This INF file entry (provided in a update to Windows Release 1703), is used to indentify that the in-box driver is a generic device driver. 

    GenericDriverInstalled,,,,1

The in-box driver registers for the following compatible IDs

    Class_01 SubClass_00 Prot_20
    Class_01 SubClass_01 Prot_20
    Class_01 SubClass_02 Prot_20
    Class_01 SubClass_03 Prot_20

### IHV USB 2.0 Audio Drivers and Updates
For IHV provided third party driver USB 2.0 drivers, those drivers will continue to be preferred for their devices over our in-box driver unless they update their driver to explicitly override this behavior and use the in-box driver. 


### Driver Development 

This driver was developed by Thesycon and is supported by Microsoft.

--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20USB%20Audio%20Class%20System%20Driver%20%28Usbaudio.sys%29%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


