---
title: Customized Printer Setup Operations
author: windows-driver-content
description: Customized Printer Setup Operations
ms.assetid: 888125e9-a057-4e86-9df8-0086cedb368d
keywords:
- customized printer setup operations WDK
- INF files WDK print , customized setup operations
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Customized Printer Setup Operations


## <a href="" id="ddk-customized-printer-setup-operations-gg"></a>


To provide customized printer setup operations for printers that are installed using Ntprint.dll, the default Windows 2000 and later printer class installer, you can include a **VendorSetup** INF entry in the printer's INF file.

**Important**  : Be aware that **VendorSetup** is now deprecated and should not be used by any *new* v3 or v4 drivers that you develop. This topic is provided for reference only, or for the maintenance of existing v3 drivers that already use this INF directive.

 

**Note**   If you plan to display user interface elements during the installation of a printer driver, you must use a **VendorSetup** INF entry. However, you should use a **VendorSetup** INF entry only if it is absolutely necessary. A significant disadvantage is that its use prevents an ordinary user from installing a printer by means of Plug and Play (the user must be an Administrator in this case).
It is not possible to install a device using a server-side installation when either the device driver is unsigned, or when the (signed or unsigned) driver's INF file contains a **VendorSetup** INF entry. When the driver is unsigned, Setup adds 0x8000 to the rank that the driver would have if it were a signed driver. If the driver's INF file contains a **VendorSetup** entry, Setup determines that device installation requires user interaction (which cannot occur in a server-side installation) and halts the installation. Setup also stops a server-side installation if the driver's rank is 0x8000 or larger. The installation can proceed when a user with administrative privileges logs on, at which time Setup restarts the device installation as a client-side installation. For a driver whose rank is 0x1000 or larger, and is not, therefore, a hardware ID match, Setup launches the Found New Hardware Wizard in the New Device DLL, which prompts the user for a driver to install. If the INF file for a signed driver contains a **VendorSetup** entry, and the rank of the driver is less than 0x1000, Setup does not launch the Found New Hardware Wizard. For more information, see [Device Installation Components](https://msdn.microsoft.com/library/windows/hardware/ff541277) and [How Setup Selects Drivers](https://msdn.microsoft.com/library/windows/hardware/ff546228).

 

The format for the **VendorSetup** entry is as follows:

VendorSetup= *FileName*, *FunctionName*

where *FileName* is the name of a DLL containing a setup function, and *FunctionName* is the name of the function. The DLL must be installed in the %windir%\\system32 directory. The printer class installer calls the setup function in this DLL only when the printer is installed by Plug and Play or by the Add Printer Wizard. The setup function is not called when only a driver is installed (for example, by use of the Add Printer Driver Wizard).

To copy one or more files to the %windir%\\system32 directory, you can add the name of an INF-writer-defined section to the INF **DestinationDirs** section. In the following example, the OEMVendorFiles section lists all of the files that are to be copied.

```
[DestinationDirs]
OEMVendorFiles = 11
...
[OEMVendorFiles]
vendor.dll
```

The function specified by *FunctionName* must match the following prototype:

`VOID WINAPI         `*FunctionName*`(HWND         hWnd, HINSTANCE hInstance, LPSTR lpszCmdLine, UINT  nCmdShow);`

where *FunctionName* is the name of the setup function. The function's parameters and their descriptions are shown in the following table.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Parameter</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><em>hWnd</em></p></td>
<td><p>Specifies the handle of the parent window.</p></td>
</tr>
<tr class="even">
<td><p><em>hInstance</em></p></td>
<td><p>Specifies the instance handle of the calling process.</p></td>
</tr>
<tr class="odd">
<td><p><em>lpszCmdLine</em></p></td>
<td><p>Specifies an ANSI string containing the name of the printer that was just installed. This string is parsed by <em>FunctionName</em>.</p></td>
</tr>
<tr class="even">
<td><p><em>nCmdShow</em></p></td>
<td><p>Specifies how the window is to be shown. The flags that control how the window is shown are defined in Winuser.h.</p></td>
</tr>
</tbody>
</table>

 

The printer class installer calls the setup function as one of the final steps in the installation operation.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Customized%20Printer%20Setup%20Operations%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


