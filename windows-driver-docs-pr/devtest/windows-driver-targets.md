---
title: Windows driver targets
description: The WindowsDriver.Common.targets, WindowsDriver.masm.targets, and WindowsDriver.arm.targets files provide the targets that are necessary to build a driver.
ms.assetid: 9D04792B-2736-4871-A53E-6B90509133A7
---

# Windows driver targets


The WindowsDriver.Common.targets, WindowsDriver.masm.targets, and WindowsDriver.arm.targets files provide the targets that are necessary to build a driver.

WindowsDriver.masm.targets and WindowsDriver.arm.targets define targets specifically for building assembly files.

These targets extend the Cpp targets without directly modifying them. MSBuild provides a mechanism that is independent of the structure of the original project for you to insert the behaviors while retaining the original mechanisms that are used to guarantee the ordering between the extensions.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Windows%20driver%20targets%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




