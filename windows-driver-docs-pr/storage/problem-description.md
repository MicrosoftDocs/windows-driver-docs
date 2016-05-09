---
title: Problem Description
description: Problem Description
ms.assetid: 5e811011-9848-43fc-969d-abdf1ad45acf
---

# Problem Description


In Windows computer systems, crash dump and hibernation support is provided by the crash dump driver that has support from special storage drivers, both port and miniport. When the system crashes, dump data is written to the disk using these special sets of drivers instead of the typical storage stack. These drivers write the data without using file system or volume manager drivers and they did not previously support adding any drivers in the crash dump stack.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20Problem%20Description%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




