---
title: Customized Printer Setup Operations
description: Customized Printer Setup Operations
keywords:
- customized printer setup operations WDK
- INF files WDK print , customized setup operations
ms.date: 06/16/2023
---

# Customized Printer Setup Operations

[!include[Print Support Apps](../includes/print-support-apps.md)]

To provide customized printer setup operations for printers that are installed using Ntprint.dll, the default Windows 2000 and later printer class installer, you can include a **VendorSetup** INF entry in the printer's INF file.

> [!CAUTION]
> Be aware that **VendorSetup** is now deprecated and should not be used by any *new* v3 or v4 drivers that you develop. This topic is provided for reference only, or for the maintenance of existing v3 drivers that already use this INF directive.

 If you plan to display user interface elements during the installation of a printer driver, you must use a **VendorSetup** INF entry. However, you should use a **VendorSetup** INF entry only if it's necessary. A significant disadvantage is that its use prevents an ordinary user from installing a printer with Plug and Play (the user must be an Administrator in this case).

It isn't possible to install a device using a server-side installation when either the device driver is unsigned, or when the (signed or unsigned) driver's INF file contains a **VendorSetup** INF entry. When the driver is unsigned, Setup adds 0x8000 to the rank that the driver would have if it were a signed driver. If the driver's INF file contains a **VendorSetup** entry, Setup determines that device installation requires user interaction (which can't occur in a server-side installation) and halts the installation.

Setup also stops a server-side installation if the driver's rank is 0x8000 or larger. The installation can proceed when a user with administrative privileges logs on, at which time Setup restarts the device installation as a client-side installation. For a driver whose rank is 0x1000 or larger, and isn't, therefore, a hardware ID match, Setup launches the Found New Hardware Wizard in the New Device DLL, which prompts the user for a driver to install.

If the INF file for a signed driver contains a **VendorSetup** entry, and the rank of the driver is less than 0x1000, Setup doesn't launch the Found New Hardware Wizard. For more information, see [How Setup Selects Drivers](../install/how-windows-selects-a-driver-for-a-device.md).

The format for the **VendorSetup** entry is as follows:

VendorSetup= *FileName*, *FunctionName*

where *FileName* is the name of a DLL containing a setup function, and *FunctionName* is the name of the function. The DLL must be installed in the %windir%\\system32 directory. The printer class installer calls the setup function in this DLL only when the printer is installed by Plug and Play or by the Add Printer Wizard. The setup function isn't called when only a driver is installed (for example, by use of the Add Printer Driver Wizard).

To copy one or more files to the %windir%\\system32 directory, you can add the name of an INF-writer-defined section to the INF **DestinationDirs** section. In the following example, the OEMVendorFiles section lists all of the files that are to be copied.

```inf
[DestinationDirs]
OEMVendorFiles = 11
...
[OEMVendorFiles]
vendor.dll
```

The function specified by *FunctionName* must match the following prototype:

`VOID WINAPI` *FunctionName* `(HWND hWnd, HINSTANCE hInstance, LPSTR lpszCmdLine, UINT  nCmdShow);`

where *FunctionName* is the name of the setup function. The function's parameters and their descriptions are shown in the following table.

| Parameter | Description |
|--|--|
| *hWnd* | Specifies the handle of the parent window. |
| *hInstance* | Specifies the instance handle of the calling process. |
| *lpszCmdLine* | Specifies an ANSI string containing the name of the printer that was installed. This string is parsed by *FunctionName*. |
| *nCmdShow* | Specifies how the window is to be shown. The flags that control how the window is shown are defined in Winuser.h. |

The printer class installer calls the setup function as one of the final steps in the installation operation.
