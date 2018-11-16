---
title: Using the Registry in a Driver
description: Using the Registry in a Driver
ms.assetid: 69d2d491-3cc1-4fd0-a1c9-0cc8e73e69b2
keywords: ["registry WDK kernel", "driver registry information WDK kernel", "storage WDK registry", "storing registry information", "registry WDK kernel , about registry in drivers", "driver registry information WDK kernel , about registry in drivers", "manipulating registry entries WDK kernel", "keys WDK kernel registry", "subkeys WDK kernel registry", "kernel-mode drivers WDK , registry"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Using the Registry in a Driver





Drivers, like other system components, rely on the registry to store configuration information. The system itself uses the registry to store information about devices and drivers, and a driver can store additional information there for its own use.

The Microsoft Windows executive provides the following two sets of routines for manipulating the registry:

[Registry Key Object Routines](registry-key-object-routines.md)

[Registry Run-Time Library Routines](registry-run-time-library-routines.md)

[Plug and Play Registry Routines](plug-and-play-registry-routines.md)

For additional information about the registry, see:

[**INF AddReg Directive**](https://msdn.microsoft.com/library/windows/hardware/ff546320)

[Registry Keys for Drivers](https://msdn.microsoft.com/library/windows/hardware/ff549538)

 

 




