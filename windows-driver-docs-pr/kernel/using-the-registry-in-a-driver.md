---
title: Using the Registry in a Driver
author: windows-driver-content
description: Using the Registry in a Driver
ms.assetid: 69d2d491-3cc1-4fd0-a1c9-0cc8e73e69b2
keywords: ["registry WDK kernel", "driver registry information WDK kernel", "storage WDK registry", "storing registry information", "registry WDK kernel , about registry in drivers", "driver registry information WDK kernel , about registry in drivers", "manipulating registry entries WDK kernel", "keys WDK kernel registry", "subkeys WDK kernel registry", "kernel-mode drivers WDK , registry"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Using the Registry in a Driver


## <a href="" id="ddk-using-the-registry-in-a-driver-kg"></a>


Drivers, like other system components, rely on the registry to store configuration information. The system itself uses the registry to store information about devices and drivers, and a driver can store additional information there for its own use.

The Microsoft Windows executive provides the following two sets of routines for manipulating the registry:

[Registry Key Object Routines](registry-key-object-routines.md)

[Registry Run-Time Library Routines](registry-run-time-library-routines.md)

[Plug and Play Registry Routines](plug-and-play-registry-routines.md)

For additional information about the registry, see:

[**INF AddReg Directive**](https://msdn.microsoft.com/library/windows/hardware/ff546320)

[Registry Keys for Drivers](https://msdn.microsoft.com/library/windows/hardware/ff549538)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Using%20the%20Registry%20in%20a%20Driver%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


