---
title: Installing Customized Driver Components
author: windows-driver-content
description: Installing Customized Driver Components
MS-HAID:
- 'custdrvr\_b80b941b-4f53-416c-b20b-2940696f3d86.xml'
- 'print.installing\_customized\_driver\_components'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 88f189bd-97f5-4bc6-ba3e-3d9da18e2102
keywords: ["printer driver customizing WDK , installing components", "customizing printer drivers WDK , installing components", "installing custom printer driver components WDK", "INF files WDK print , customized driver components"]
---

# Installing Customized Driver Components


## <a href="" id="ddk-installing-customized-driver-components-gg"></a>


When you provide customized components for Microsoft's printer drivers, you must also provide an .ini file for installation of the component. (If your printer is not supported by ntprint.inf, you must also provide a [printer INF file](printer-inf-files.md).)

The .ini file must contain an OEMFiles section. In this section, each customized component is described by using one of the following entries:

<a href="" id="oemdriverfilen"></a>OEMDriverFile*n*  
Names a rendering plug-in.

<a href="" id="oemconfigfilen"></a>OEMConfigFile*n*  
Names a user interface plug-in.

where *n* specifies the order in which the installer installs the files. Numbers specified for *n* must be contiguous, starting with 1, for both types of plug-ins.

For example, if you are providing two rendering plug-ins and one user interface plug-in, and your printer model is XYZ, your .ini file might appear as follows:

```
[OEMFiles]
OEMDriverFile1=XYZDRV1.DLL
OEMConfigFile1=XYZUI1.DLL
OEMDriverFile2=XYZDRV2.DLL
```

Spaces are not allowed before or after the equal sign (=). File names cannot include path specifications.

In the example, two rendering plug-ins are specified. Based on the *n* values for OEMDriverFile*n*, xyzdrv1.dll is installed before xyzdrv2.dll. The Unidrv and Pscript5 drivers call plug-ins in the order they are installed, so later, when a driver needs to call graphics DDI hooking functions and COM methods supplied by these plug-ins, xyzdrv1.dll is called before xyzdrv2.dll.

The .ini file name should reflect the printer product name. The .ini file name should be distinct from the names of .ini files for other printers to avoid name conflicts. Note that if you are back-porting a rendering plug-in or user interface plug-in to Windows NT 4.0, your .ini file name must match your .gpd or .ppd file name. (That is, xyz.ini must be used for xyz.gpd or xyz.ppd.) This restriction does not apply to Windows 2000 or later versions of Windows operating system.

An .ini file can contain either ANSI or Unicode text, but Unicode text is recommended. Within an .ini file, lines beginning with the pound sign (\#) are comments.

For more information, see [General Guidelines for INF Files](https://msdn.microsoft.com/library/windows/hardware/ff544975) and [Installing a Unidrv Minidriver](installing-a-unidrv-minidriver.md).

If you provide a printer INF file, a convenient way to install and register a customized component is to make the component a *dependent file* of the printer driver. In addition, the associated .inf file can be installed as a dependent file. For more information about dependent files for printer drivers, see [Printer INF File Entries](printer-inf-file-entries.md).

Alternatively, you can install a customized component by making the component a dependent file for another print component such as a port monitor or a status application. However, this method might create difficulties because [point-and-print](introduction-to-point-and-print.md) operations install only the driver and driver-dependent files on the client. If a customized component is not listed as a dependent file of the printer driver, the component must be installed on the client in some way other than as part of the point-and-print operation.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Installing%20Customized%20Driver%20Components%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


