---
title: Installation of Callout Drivers
description: Installation of Callout Drivers
keywords:
- Windows Filtering Platform callout drivers WDK , installing
- callout drivers WDK Windows Filtering Platform , installing
- installing callout drivers WDK Windows Filtering Platform
- loading drivers WDK Windows Filtering Platform
- INF files WDK Windows Filtering Platform
ms.date: 04/20/2017
---

# Installation of Callout Drivers


A callout driver can be installed by right-clicking the driver's setup information file (INF) file and selecting **Install** from the pop-up menu that appears.

After a callout driver has been successfully installed, it can be loaded (started) by typing the following at the command prompt:

```cpp
net start drivername
```

Depending on the value specified for the **StartType** entry in the \[*drivername*.Services\] section of the INF file, the callout driver might be automatically loaded the next time that the system is restarted. A callout driver should usually specify zero (SERVICE\_BOOT\_START) for this value so that the driver is loaded and its callouts are registered before the filter engine is started. See the [**INF AddService Directive**](../install/inf-addservice-directive.md) for more information.

A callout driver that is currently loaded can be unloaded (stopped) by typing the following at the command prompt:

```cpp
net stop drivername
```

A callout driver can also be installed, loaded (started), unloaded (stopped), and/or uninstalled by writing a user-mode application that calls the Win32 Service Control Manager API. For more information about Win32 service control functions, such as **CreateService**, **OpenService**, **StartService**, **ControlService**, and **DeleteService**, see the [Microsoft Windows SDK](/windows/win32/services/service-reference).

> [!NOTE]
> Starting in Windows 8 and later, callout drivers cannot be viewed or managed in the Device Manager because the Plug-and-Play (PnP) manager no longer creates device representations for non-PnP (legacy) devices.
