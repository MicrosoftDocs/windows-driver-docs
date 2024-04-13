---
title: Terminal Server Printing
description: Terminal Server Printing
keywords:
- printer drivers WDK , terminal servers
- terminal server printing WDK
ms.date: 03/24/2023
---

# Terminal Server Printing

> [!IMPORTANT]
> Starting with the WDK for Windows 11, version 22H2, WDF redistributable co-installers are no longer supported.
> To learn how to work around this change, see [WDF redistributable co-installers don't work](/windows-hardware/drivers/wdk-known-issues#wdf-redistributable-co-installers-dont-work) in the *WDK known issues* article.

Microsoft Windows supports Terminal Services, a technology that allows multiple users to connect to a single server system. This server system is called a terminal server. For a detailed discussion of Terminal Services, see the Windows SDK documentation.

If you're developing a printer minidriver or driver for Windows, you don't have to do anything special to support printers connected to terminal servers. However, you must follow all design, implementation, and installation guidelines specified in the Windows Driver Kit (WDK). Specifically, you must use the following rules:

- If possible, support your printer by providing a minidriver that works with one of the following Microsoft-supplied drivers:

    [Microsoft XPS Printer Driver](xpsdrv-printer-driver.md)

    [Microsoft Universal Printer Driver](microsoft-universal-printer-driver.md)

    [Microsoft PostScript Printer Driver](microsoft-postscript-printer-driver.md)

    [Microsoft Plotter Driver](microsoft-plotter-driver.md)

- You must design a printer graphics DLL to execute in user mode. See [Choosing User Mode or Kernel Mode](choosing-user-mode-or-kernel-mode.md).

- If your device must be supported by a custom driver, your driver must adhere exactly to Microsoft's [printer driver architecture](printer-driver-architecture.md). Specifically:

    1. You must create a [printer interface DLL](printer-interface-dll.md).

    1. You must create a [printer graphics DLL](printer-graphics-dll.md). This DLL can execute in either user mode or kernel mode, but user mode is preferred.

    1. If you create kernel-mode code, you must test the code using [Driver Verifier](../devtest/driver-verifier.md).

    1. You must provide an installation procedure based on setup INF files, as described in [Installing and Configuring Printer Drivers](installing-and-configuring-printer-drivers.md).

All custom driver code must be reentrant. User-mode code should employ critical section objects (described in the Windows SDK documentation). Kernel-mode code should use semaphores (see [**EngCreateSemaphore**](/windows/win32/api/winddi/nf-winddi-engcreatesemaphore) and related functions).

Printer drivers and custom spooler components must access the registry only through interfaces provided specifically for these drivers and spooler components, as described in appropriate sections of the WDK.

## Installation Considerations

Usually, all you need to do for installation is provide an INF file that can be read by Microsoft's printer class installer when a user invokes the **Add Printer** wizard. Sometimes, custom setup code (a co-installer or class installer) is also needed. If you must create custom setup code, remember the following:

- Either the user or the setup code must put the terminal server into installation mode. (For more information, see the Microsoft Windows SDK documentation.)

- Don't attempt to replace system files. Windows file protection prohibits system file replacement.

- Avoid requiring system reboots as much as possible. Use the following guidelines:

    1. Don't replace driver files that haven't changed. For example, files shared by several devices shouldn't be updated if the most current version is already installed.

    1. If a file must be replaced, the setup code should take steps to unload the old version and then load the new version (for example, by stopping the driver service, replacing the file, then restarting the service).

    1. Requiring a user to log off, then re-log on, is preferable to requiring a system reboot.

For more information about co-installers and class installers, see [Writing Class Installers and Co-Installers](../install/writing-class-installers-and-co-installers.md).

Before writing custom setup code, it's important to read the Terminal Services programming guidelines provided in the Windows SDK documentation.

## User Interface Considerations

Custom setup code that is run by a user can display a user interface.

Almost all printer driver code runs in the spooler's execution context and therefore can't display a user interface. User interfaces can be displayed only by printer interface DLLs, and only from within the following functions:

- The [**DrvDevicePropertySheets**](/windows-hardware/drivers/ddi/winddiui/nf-winddiui-drvdevicepropertysheets) and [**DrvDocumentPropertySheets**](/windows-hardware/drivers/ddi/winddiui/nf-winddiui-drvdocumentpropertysheets) functions, which create property pages.

- The [**DrvPrinterEvent**](/windows-hardware/drivers/ddi/winddiui/nf-winddiui-drvprinterevent) function, which receives event codes identifying printer events. The function can display a user interface only for the PRINTER_EVENT_ADD_CONNECTION and PRINTER_EVENT_DELETE_CONNECTION event codes.

All other printer driver code executes in the spooler's context. From this context, calling **MessageBox** or **MessageBoxEx** is allowed, but you must set MB_SERVICE_NOTIFICATION. These functions are described in the Windows SDK documentation.
