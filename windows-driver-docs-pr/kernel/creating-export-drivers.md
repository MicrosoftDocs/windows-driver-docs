---
title: Creating Export Drivers
author: windows-driver-content
description: Creating Export Drivers
ms.assetid: 60ce7d0d-0eab-4af6-890a-45ab206816aa
keywords: ["export drivers WDK kernel", "loading export drivers WDK kernel", "importing export driver functions", "module-definition files WDK kernel", ".def files", "def files", "kernel-mode drivers WDK , export drivers"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Creating Export Drivers


## <a href="" id="ddk-creating-export-drivers-kg"></a>


Microsoft Windows drivers are typically defined as a pair of components, such as a port/miniport driver pair, or a class/miniclass driver pair. Typically, Microsoft provides a hardware-independent class or port driver, and a vendor supplies a hardware-dependent miniclass or miniport driver.

Kernel-mode export drivers are especially well suited for implementing the part of a driver pair that is independent of underlying stack and hardware characteristics, because an export driver is a kernel-mode DLL that can be loaded by a variety of other hardware-specific or device-stack-specific components. Microsoft ships several drivers together with the Windows operating system that fall into this category. For example, the SCSI port driver, the tape class driver, the IDE controller driver are all system-supplied export drivers that are loaded by other drivers.

An export driver is missing many of the characteristics of a complete kernel-mode driver. An export driver does not have a dispatch table, it does not have a place in the driver stack, and it does not have an entry in the service control manager's database that defines it as a system service. An export driver does have a [**DriverEntry**](https://msdn.microsoft.com/library/windows/hardware/ff544113) routine, but its **DriverEntry** routine is never called. (The routine is only a stub to satisfy the requirements of the build scripts.)

Note that, while an export driver does not have a dispatch table, it can supply dispatch routines to a standard driver. The standard driver inserts the dispatch routines into its own dispatch table.

Standard drivers can also function as export drivers. For a driver to function in both ways, it must be built as an export driver and loaded as a regular driver.

### Building an Export Driver

To build a driver as an export driver you must define several Build utility macros in the driver's Sources file.

First, you must assign the appropriate value to the **TARGETTYPE** macro, as follows:

```
TARGETTYPE=EXPORT_DRIVER
```

You must also specify a module-definition (.def) file using the **DLLDEF** macro. For example:

```
DLLDEF="c:\project\driver.def"
```

The module-definition file provides the compiler and linker with a list of exported routines along with other information. For more information about module-definition files, see the Microsoft Visual C++ documentation.

Many of the Build utility macros employed in building a user-mode DLL cannot be used when building a kernel-mode DLL. For instance, the entry point for a kernel-mode DLL is always [**DllInitialize**](https://msdn.microsoft.com/library/windows/hardware/ff544049). You cannot specify the entry point using the **DLLENTRY** macro.

The build process generates an export library with a .lib extension, and an export driver with a .sys extension.

### Importing Functions from an Export Driver

To import functions that are exported by an export driver, you should declare the functions using the DECLSPEC\_IMPORT macro, which is defined in Ntdef.h. For example:

```
DECLSPEC_IMPORT int LoadPrinterDriver (int arg1); 
```

This macro resolves to a **\_\_declspec**(dllimport) storage class declaration on those platforms where required and to nothing on those platforms where not required.

In the export driver, the function to be exported should be declared with the DECLSPEC\_EXPORT macro. This macro resolves to a **\_\_declspec**(dllexport) storage class declaration on those platforms where required and to nothing on those platforms where not required. If an export driver supplies a dispatch routine to a standard driver, that routine does not have to be exported.

### Loading an Export Driver

Export drivers must be installed in the %Windir%\\System32\\Drivers directory. Starting with Windows 2000, the operating system keeps a reference count that indicates the number of times that the export driver's functions have been imported by other drivers. The system decrements this count whenever one of the importing drivers unloads. When the reference count falls to zero, the system unloads the export driver. However, the export driver must contain the standard entry point and unload routines, [**DllInitialize**](https://msdn.microsoft.com/library/windows/hardware/ff544049) and [**DllUnload**](https://msdn.microsoft.com/library/windows/hardware/ff544054), or the operating system will not activate this reference count mechanism.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Creating%20Export%20Drivers%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


