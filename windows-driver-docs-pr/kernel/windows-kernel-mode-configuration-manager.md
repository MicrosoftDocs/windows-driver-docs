---
title: Windows Kernel-Mode Configuration Manager
description: Windows Kernel-Mode Configuration Manager
ms.date: 10/17/2018
---

# Windows Kernel-Mode Configuration Manager


In the earlier days of Microsoft Windows, applications and the operating system stored configuration values in "INI" (initialization) files. This provided a simple way to store state values that could be preserved from one Windows session to the next. However, as the Windows environment became more complex, a new system of storing persistent information about the operating system and applications was needed. The Windows Registry was created to store data about hardware and software.

The Windows kernel-mode configuration manager manages the registry. If your driver needs to know about changes in the registry, it can use the routines of the configuration manager to do so by registering callbacks on specific registry data. Then, when the data in the registry changes, the callback is triggered and you can run code to process the callback information in your driver.

Routines that provide a direct interface to the configuration manager are prefixed with the letters "**Cm**"; for example, **CmRegisterCallback**. For a list of configuration manager routines, see [Configuration Manager Routines](/windows-hardware/drivers/ddi/_kernel/#configuration-manager-routines).

In addition to directly calling the configuration manager, there are other ways you will want to work with the registry in your driver. For more information about using the registry in a driver, see [Registry Key Object Routines](registry-key-object-routines.md) and [Registry Keys for Drivers](../install/overview-of-registry-trees-and-keys.md).

 

