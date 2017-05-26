---
title: Installation of Callout Drivers
description: Installation of Callout Drivers
ms.assetid: 3baefd81-04bc-4a34-b4cd-afa544308a90
keywords:
- Windows Filtering Platform callout drivers WDK , installing
- callout drivers WDK Windows Filtering Platform , installing
- installing callout drivers WDK Windows Filtering Platform
- loading drivers WDK Windows Filtering Platform
- INF files WDK Windows Filtering Platform
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Installation of Callout Drivers


A callout driver can be installed by right-clicking the driver's setup information file (INF) file and selecting **Install** from the pop-up menu that appears.

After a callout driver has been successfully installed, it can be loaded (started) by typing the following at the command prompt:

```
net start drivername
```

Depending on the value specified for the **StartType** entry in the \[*drivername*.Services\] section of the INF file, the callout driver might be automatically loaded the next time that the system is restarted. A callout driver should usually specify zero (SERVICE\_BOOT\_START) for this value so that the driver is loaded and its callouts are registered before the filter engine is started. See the [**INF AddService Directive**](https://msdn.microsoft.com/library/windows/hardware/ff546326) for more information.

A callout driver that is currently loaded can be unloaded (stopped) by typing the following at the command prompt:

```
net stop drivername
```

After a callout driver has been installed and loaded, it will appear in Device Manager. Device Manager can be used to load (start), unload (stop), and uninstall callout drivers. Callout drivers are listed in Device Manager under the **Non-Plug and Play Drivers** category, which, by default, is not usually displayed. For more information about how to use Device Manager, see [Using Device Manager](https://msdn.microsoft.com/library/windows/hardware/ff553570). For more information about how to view the **Non-Plug and Play Drivers** category in Device Manager, see [Viewing Hidden Devices](https://msdn.microsoft.com/library/windows/hardware/ff553955).

A callout driver can also be installed, loaded (started), unloaded (stopped), and/or uninstalled by writing a user-mode application that calls the Win32 Service Control Manager API. For more information about Win32 service control functions, such as **CreateService**, **OpenService**, **StartService**, **ControlService**, and **DeleteService**, see the [Microsoft Windows SDK](http://go.microsoft.com/fwlink/p/?linkid=122165).

 

 





