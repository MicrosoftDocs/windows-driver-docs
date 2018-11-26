---
title: Terminal Server Printing
description: Terminal Server Printing
ms.assetid: 627d05f6-1499-4645-ad9a-b1a09f41b0c9
keywords:
- printer drivers WDK , terminal servers
- terminal server printing WDK
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Terminal Server Printing





Microsoft Windows 2000 and later supports Terminal Services, a technology that allows multiple users to connect to a single server system. This server system is called a terminal server. For a detailed discussion of Terminal Services, see the Windows SDK documentation.

If you are developing a printer minidriver or driver for Windows 2000 or later, you do not have to do anything special to support printers connected to terminal servers. However, you must follow all design, implementation, and installation guidelines specified in the Windows Driver Kit (WDK). Specifically, you must use the following rules:

-   If possible, support your printer by simply providing a minidriver that works with one of the following Microsoft-supplied drivers:

    [Microsoft XPS Printer Driver](xpsdrv-printer-driver.md)

    [Microsoft Universal Printer Driver](microsoft-universal-printer-driver.md)

    [Microsoft PostScript Printer Driver](microsoft-postscript-printer-driver.md)

    [Microsoft Plotter Driver](microsoft-plotter-driver.md)

-   In Windows Vista, you must design a printer graphics DLL to execute in user mode. See [Choosing User Mode or Kernel Mode](choosing-user-mode-or-kernel-mode.md).

-   If your device must be supported by a custom driver, your driver must adhere exactly to Microsoft's [printer driver architecture](printer-driver-architecture.md). Specifically:
    1.  You must create a [printer interface DLL](printer-interface-dll.md).
    2.  You must create a [printer graphics DLL](printer-graphics-dll.md). This DLL can execute in either user mode or kernel mode, but user mode is preferred.
    3.  If you create kernel-mode code, you must test the code using [Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff545448).
    4.  You must provide an installation procedure based on setup INF files, as described in [Installing and Configuring Printer Drivers](installing-and-configuring-printer-drivers.md).

All custom driver code must be reentrant. User-mode code should employ critical section objects (described in the Windows SDK documentation). Kernel-mode code should use semaphores (see [**EngCreateSemaphore**](https://msdn.microsoft.com/library/windows/hardware/ff564760) and related functions).

Printer drivers and custom spooler components must access the registry only through interfaces provided specifically for these drivers and spooler components, as described in appropriate sections of the WDK.

### Installation Considerations

Usually, all you need to do for installation is provide an INF file that can be read by Microsoft's printer class installer when a user invokes the **Add Printer** wizard. Sometimes, custom setup code (a co-installer or class installer) is also needed. If you must create custom setup code, remember the following:

-   Either the user or the setup code must put the terminal server into installation mode. (For more information, see the Microsoft Windows SDK documentation.)

-   Do not attempt to replace system files. Windows file protection prohibits system file replacement.

-   Avoid requiring system reboots as much as possible. Use the following guidelines:
    1.  Do not replace driver files that have not changed. For example, files shared by several devices should not be updated if the most current version is already installed.
    2.  If a file must be replaced, the setup code should take steps to unload the old version and then load the new version (for example, by stopping the driver service, replacing the file, then restarting the service).
    3.  Requiring a user to log off, then re-log on, is preferable to requiring a system reboot.

For more information about co-installers and class installers, see [Writing Class Installers and Co-Installers](https://msdn.microsoft.com/library/windows/hardware/ff819060).

**Note**   Before writing custom setup code, it is important to read the Terminal Services programming guidelines provided in the Windows SDK documentation.

 

### User Interface Considerations

Custom setup code that is run by a user can display a user interface.

Almost all printer driver code runs in the spooler's execution context and therefore cannot display a user interface. User interfaces can be displayed only by printer interface DLLs, and only from within the following functions:

-   The [**DrvDevicePropertySheets**](https://msdn.microsoft.com/library/windows/hardware/ff548542) and [**DrvDocumentPropertySheets**](https://msdn.microsoft.com/library/windows/hardware/ff548548) functions, which create property pages.

-   The [**DrvPrinterEvent**](https://msdn.microsoft.com/library/windows/hardware/ff548564) function, which receives event codes identifying printer events. Note that the function can display a user interface only for the PRINTER\_EVENT\_ADD\_CONNECTION and PRINTER\_EVENT\_DELETE\_CONNECTION event codes.

All other printer driver code executes in the spooler's context. From this context, calling **MessageBox** or **MessageBoxEx** is allowed, but you must set MB\_SERVICE\_NOTIFICATION. These functions are described in the Windows SDK documentation.

 

 




