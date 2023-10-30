---
title: Install a battery driver
description: This guide shows you how to install a battery driver using an INF file, including the necessary sections and directives.
ms.date: 10/05/2023
---

# Install a battery driver

A battery driver's INF file specifies information about the driver and the devices it controls. All battery devices belong to the Battery class, and the battery class installer installs the driver.

This section describes battery-specific entries in the INF file. For more information about creating and distributing INF files and installing drivers, see [Creating an INF File](../install/overview-of-inf-files.md) and [INF File Sections and Directives](../install/index.md).

A battery driver's INF file includes the sections described below.

## Version

A battery driver's INF file specifies the Battery class and its GUID, using the [**INF Version section**](../install/inf-version-section.md), as shown in the following example:

``` syntax
[Version]
Signature="$WINDOWS NT$"
Class=Battery
ClassGuid={72631e54-78a4-11d0-bcf7-00aa00b7b32a}
Provider=%MyCo%
CatalogFile=ExampleCatalog.cat
PnpLockdown=1
```

Note that %MyCo% must be defined in an [**INF Strings section**](../install/inf-strings-section.md) (not shown).

## DestinationDirs

In the [**INF DestinationDirs section**](../install/inf-destinationdirs-section.md), a battery driver's INF specifies the Drivers directory (12) as the default for all files.

``` syntax
[DestinationDirs]
DefaultDestDir = 12
```

## Manufacturer

The [**INF Manufacturer section**](../install/inf-manufacturer-section.md) defines the manufacturer of the device.

``` syntax
[Manufacturer]
%MyCo%=MyCompany,NTamd64
```

## Models

The [**INF *Models* section**](../install/inf-models-section.md) specifies the PnP hardware ID of the battery (shown as *pnpid* in the example). If the device is enumerated through ACPI, this section must also specify the EISA-style ID (shown as *acpidevnum*). For information about creating these IDs, see the *Advanced Configuration and Power Interface Specification*, which is available through the [ACPI / Power Management](https://uefi.org/acpi/specs) website.

``` syntax
[MyCompany.NTamd64]
%pnpid.DeviceDesc% = NewBatt_Inst,pnpid
%ACPI\acpidevnum.DeviceDesc% = NewBatt_Inst,ACPI\acpidevnum
```

## DDInstall

In the [**INF *DDInstall* section**](../install/inf-ddinstall-section.md) (named NewBatt_Inst in the example), an [**INF CopyFiles directive**](../install/inf-copyfiles-directive.md) copies the battery class driver (*Battc.sys*) and the new miniclass driver (*NewBatt.sys*) to the destination specified in the **DestinationDirs** directive.

``` syntax
[NewBatt_Inst]
CopyFiles = @NewBatt.sys
CopyFiles = @battc.sys
```

## DDInstall.Services

The [**INF *DDInstall*.Services section**](../install/inf-ddinstall-services-section.md) includes an [**INF AddService directive**](../install/inf-addservice-directive.md) that specifies additional information about the battery driver. A battery driver's INF file should indicate that the driver is a kernel driver that uses normal error handling and starts during initialization of the operating system. Battery drivers specify the load order group Extended Base.

``` syntax
[NewBatt_Inst.Services]
AddService = NewBatt,2,NewBatt_Service_Inst    ; function driver for the device
 
[NewBatt_Service_Inst]
DisplayName    = %NewBatt.SvcDesc%
ServiceType    = 1 ;    SERVICE_KERNEL_DRIVER
StartType      = 3 ;    SERVICE_DEMAND_START
ErrorControl   = 1 ;    SERVICE_ERROR_NORMAL%
ServiceBinary  = %12%\NewBatt.sys
```
