---
title: Crash Dump Filter Drivers
author: windows-driver-content
description: Crash Dump Filter Drivers
ms.assetid: d91c00d7-ad17-4fa8-9e78-fee0698d9049
---

# Crash Dump Filter Drivers


To extend the usefulness of the crash dump interface, for Windows Vista with Service Pack 1 (SP1) and Windows Server 2008 and later operating systems, Microsoft has defined filter driver support in the crash dump driver stack.

The crash dump driver does not use the typical runtime storage driver stack to write dump data to the disk. By adding filter driver support in the crash dump driver stack, new functionality can be added without changing the kernel. For example, it becomes possible to encrypt the contents of the hibernation or crash dump file.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20Crash%20Dump%20Filter%20Drivers%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


