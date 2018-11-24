---
title: Creating Export Drivers
description: Creating Export Drivers
ms.assetid: 60ce7d0d-0eab-4af6-890a-45ab206816aa
keywords: ["export drivers WDK kernel", "loading export drivers WDK kernel", "importing export driver functions", "module-definition files WDK kernel", ".def files", "def files", "kernel-mode drivers WDK , export drivers"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Creating Export Drivers





Microsoft Windows drivers are typically defined as a pair of components, such as a port/miniport driver pair, or a class/miniclass driver pair. Typically, Microsoft provides a hardware-independent class or port driver, and a vendor supplies a hardware-dependent miniclass or miniport driver.

Kernel-mode export drivers are especially well suited for implementing the part of a driver pair that is independent of underlying stack and hardware characteristics, because an export driver is a kernel-mode DLL that can be loaded by a variety of other hardware-specific or device-stack-specific components. Microsoft ships several drivers together with the Windows operating system that fall into this category. For example, the SCSI port driver, the tape class driver, the IDE controller driver are all system-supplied export drivers that are loaded by other drivers.

An export driver is missing many of the characteristics of a complete kernel-mode driver. An export driver does not have a dispatch table, it does not have a place in the driver stack, and it does not have an entry in the service control manager's database that defines it as a system service. An export driver does have a [**DriverEntry**](https://msdn.microsoft.com/library/windows/hardware/ff544113) routine, but its **DriverEntry** routine is never called. (The routine is only a stub to satisfy the requirements of the build scripts.)

Note that, while an export driver does not have a dispatch table, it can supply dispatch routines to a standard driver. The standard driver inserts the dispatch routines into its own dispatch table.

Standard drivers can also function as export drivers. For a driver to function in both ways, it must be built as an export driver and loaded as a regular driver.

### Building an Export Driver

To build a driver as an export driver you must define several Build utility macros in the driver's Sources file.

First, you must assign the appropriate value to the **TARGETTYPE** macro, as follows:

```cpp
TARGETTYPE=EXPORT_DRIVER
```

You must also specify a module-definition (.def) file using the **DLLDEF** macro. For example:

```cpp
DLLDEF="c:\project\driver.def"
```

The module-definition file provides the compiler and linker with a list of exported routines along with other information. For more information about module-definition files, see the Microsoft Visual C++ documentation.

Many of the Build utility macros employed in building a user-mode DLL cannot be used when building a kernel-mode DLL. 

For instance, the entry point for a kernel-mode DLL is always **DllInitialize**. The system calls a kernel-mode DLL's DllInitialize routine immediately after the DLL is loaded. Export drivers must provide **DllInitialize** routines. You can use the **DllInitialize** routine to acquire or initialize resources required by other routines in the DLL. 

You cannot specify the entry point using the **DLLENTRY** macro. 

```cpp
NTSTATUS DllInitialize(
  _In_ PUNICODE_STRING RegistryPath
);
```
RegistryPath is a pointer to a counted Unicode string specifying the path to the DLL's registry key, **HKEY_LOCAL_MACHINE\CurrentControlSet\Services\DllName**. DLL routines can use this key to store DLL-specific information. The buffer pointed to by RegistryPath is freed once **DllInitialize** exits. Therefore, if the DLL makes use of the key, **DllInitialize** must duplicate the key name. 


The build process generates an export library with a .lib extension, and an export driver with a .sys extension.

### Importing Functions from an Export Driver

To import functions that are exported by an export driver, you should declare the functions using the DECLSPEC\_IMPORT macro, which is defined in Ntdef.h. For example:

```cpp
DECLSPEC_IMPORT int LoadPrinterDriver (int arg1); 
```

This macro resolves to a **\_\_declspec**(dllimport) storage class declaration on those platforms where required and to nothing on those platforms where not required.

In the export driver, the function to be exported should be declared with the DECLSPEC\_EXPORT macro. This macro resolves to a **\_\_declspec**(dllexport) storage class declaration on those platforms where required and to nothing on those platforms where not required. If an export driver supplies a dispatch routine to a standard driver, that routine does not have to be exported.

### Loading and Unloading an Export Driver

Export drivers must be installed in the %Windir%\\System32\\Drivers directory. Starting with Windows 2000, the operating system keeps a reference count that indicates the number of times that the export driver's functions have been imported by other drivers. The system decrements this count whenever one of the importing drivers unloads. When the reference count falls to zero, the system unloads the export driver. However, the export driver must contain the standard entry point and unload routines, **DllInitialize** and **DllUnload**, or the operating system will not activate this reference count mechanism.

The system calls a kernel-mode DLL's DllUnload routine when it unloads the DLL.

```cpp
NTSTATUS DllUnload(void);
```
Export drivers must provide DllUnload routines. You can use the DllUnload routine to release any resources used by the routines in the DLL. 








