---
title: Storage Virtual Miniport Drivers When Are They Appropriate
description: Storage Virtual Miniport Drivers When Are They Appropriate
ms.assetid: 45b9eab9-15b8-4244-bd16-e8850211b8bf
---

# Storage Virtual Miniport Drivers: When Are They Appropriate?


A virtual miniport driver is appropriate when it completely simulates one or more devices, or it has no hardware of its own to control but it communicates with another device using its device driver as a transport for I/O requests. For example, a disk device that uses Random Access Memory (RAM) to store its data is commonly called a RAMDISK. This is a good example of an appropriate use of a virtual miniport driver. Another example would be the use of some type of network adapter that provides a communication link to send and receive storage commands and data. The network adapter has its own device driver that controls its hardware, but the virtual miniport communicates only with the driver, and not the underlying hardware.

A virtual miniport is inappropriate when it is directly controlling real hardware, for example, a host bus adapter.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20Storage%20Virtual%20Miniport%20Drivers:%20When%20Are%20They%20Appropriate?%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




