---
title: Install a Battery Driver
description: Explore how to install a battery driver by using an INF file (.inf), including the necessary sections and directives.
ms.date: 07/11/2025
ms.topic: install-set-up-deploy
---

# Install a battery driver

A battery driver's INF (_.inf_) file specifies information about the driver and the devices it controls. All battery devices belong to the `Battery` class, and the battery class installer installs the driver. The sections in a battery driver's INF file include Version, DestinationDirs, Manufacturer, Models, DDInstall, and DDInstall.Services.

This article describes the battery-specific entries in the INF file. For more information about creating and distributing INF files and installing drivers, see [Creating an INF File](../install/overview-of-inf-files.md) and [INF File Sections and Directives](../install/index.md).

## Version section

A battery driver's INF file specifies the `Battery` class and the class GUID value by using the [INF Version section](../install/inf-version-section.md).

The following example shows how to specify the Version section:

```INF
[Version]
Signature="$WINDOWS NT$"
Class=Battery
ClassGuid={72631e54-78a4-11d0-bcf7-00aa00b7b32a}
Provider=%MyCo%
CatalogFile=ExampleCatalog.cat
PnpLockdown=1
```

The `%MyCo%` value must be defined in an [INF Strings section](../install/inf-strings-section.md), which isn't demonstrated in the example.

## DestinationDirs section

In the [INF DestinationDirs section](../install/inf-destinationdirs-section.md), a battery driver's INF specifies the [driver store](../develop/run-from-driver-store.md) as the default for all files. 

The following example shows how to specify the DestinationDirs section where the [driver store value is 13](../develop/run-from-driver-store.md#quick-reference-for-destination-directory-updates):

```INF
[DestinationDirs]
DefaultDestDir = 13
```

## Manufacturer section

The [INF Manufacturer section](../install/inf-manufacturer-section.md) defines the manufacturer of the device, as shown in the following example:

```INF
[Manufacturer]
%MyCo%=MyCompany,NTamd64.10.0...16299
```

## Models section

The [INF Models section](../install/inf-models-section.md) specifies the PnP hardware ID of the battery (shown as the ID `pnpid` in the example). If the device is enumerated through an Advanced Configuration and Power Interface (ACPI), this INF section must also specify the EISA-style ID (shown as the ID `acpidevnum` in the example).

For information about creating these identifiers, see the ACPI Specification on the [ACPI / Power Management](https://uefi.org/acpi/specs) website.

The following example shows how to specify the Models section:

```INF
[MyCompany.NTamd64.10.0...16299]
%pnpid.DeviceDesc% = NewBatt_Inst,pnpid
%ACPI\acpidevnum.DeviceDesc% = NewBatt_Inst,ACPI\acpidevnum
```

## DDInstall section

In the [INF DDInstall section](../install/inf-ddinstall-section.md), an [INF CopyFiles directive](../install/inf-copyfiles-directive.md) copies the new miniclass driver to the destination specified in the **DestinationDirs** directive. In the following exmaple, the DDInstall section is named `NewBatt_Inst`, and the miniclass driver is `NewBatt.sys`. The specification also uses the `Include` and `Needs` directives to specify a dependency on the battery class driver by using the `Battery_Inst` definition from the _battery.inf_ file.

The following example shows how to specify the DDInstall section:

```INF
[NewBatt_Inst]
CopyFiles = @NewBatt.sys
Include = battery.inf
Needs = Battery_Inst
```

## DDInstall.Services section

The [INF DDInstall.Services section](../install/inf-ddinstall-services-section.md) includes an [INF AddService directive](../install/inf-addservice-directive.md) that specifies more information about the battery driver. A battery driver's INF file should indicate the driver is a kernel driver that uses normal error handling and starts during initialization of the operating system. Battery drivers specify the load order group Extended Base.

The following example shows how to specify the DDInstall.Services section:

```INF
[NewBatt_Inst.Services]
AddService = NewBatt,2,NewBatt_Service_Inst    ; function driver for the device
 
[NewBatt_Service_Inst]
DisplayName    = %NewBatt.SvcDesc%
ServiceType    = 1 ;    SERVICE_KERNEL_DRIVER
StartType      = 3 ;    SERVICE_DEMAND_START
ErrorControl   = 1 ;    SERVICE_ERROR_NORMAL%
ServiceBinary  = %13%\NewBatt.sys
```