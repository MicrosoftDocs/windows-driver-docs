---
title: Setting Device Object Properties in the Registry
author: windows-driver-content
description: Setting Device Object Properties in the Registry
ms.assetid: a2cfe098-0d5d-42fb-bbdc-25376ce50a9b
keywords: ["device objects WDK kernel , registry", "registry WDK device objects"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Setting Device Object Properties in the Registry


## <a href="" id="ddk-setting-device-object-properties-in-the-registry-kg"></a>


Properties of device objects can be set in the registry as follows:

-   For WDM drivers, properties can be set for each model of a device, or for a whole device setup class. (For more information about device setup classes, see [Device Setup Classes](https://msdn.microsoft.com/library/windows/hardware/ff541509).)

-   For non-WDM drivers, properties can be set for a named device object's device setup class. The driver specifies the device setup class when it creates the device object with **IoCreateDeviceSecure**. For more information about how to specify a device setup class, see [**IoCreateDeviceSecure**](https://msdn.microsoft.com/library/windows/hardware/ff548407).

Any settings in the registry override the properties supplied when the driver created the device object.

Registry settings are specified by an INF file that is used during device installation, or they can be specified after installation by an application that calls the [device installation functions](https://msdn.microsoft.com/library/windows/hardware/ff541299).

This section contains the following subsections:

[Setting Device Object Registry Properties During Installation](setting-device-object-registry-properties-during-installation.md)

[Setting Device Object Registry Properties After Installation](setting-device-object-registry-properties-after-installation.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Setting%20Device%20Object%20Properties%20in%20the%20Registry%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


