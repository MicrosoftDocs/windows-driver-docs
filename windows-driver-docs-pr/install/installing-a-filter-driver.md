---
title: Install a filter driver
description: Provides information about how to install a filter driver.
keywords:
- Device setup WDK device installations , filter drivers
- device installations WDK, filter drivers
- install devices WDK, filter drivers
- filter drivers WDK device installations
- device-specific filter drivers WDK device installations
- class filter drivers WDK device installations
- SetupInstallFilesFromInfSection
- UpperFilters
- LowerFilters
ms.date: 08/29/2022
---

# Install a filter driver

A PnP filter driver can support a specific device or all devices in a [device setup class](overview-of-device-setup-classes.md) and can attach below a device's function driver (a lower filter) or above a device's function driver (an upper filter). See [Types of WDM drivers](../kernel/types-of-wdm-drivers.md) for more information about PnP driver layers.

## Install a device-specific filter driver

On Windows 10 version 1903 and later, a device specific filter driver can be registered by using a [**INF AddFilter directive**](inf-addfilter-directive.md) from a [**INF DDInstall.Filters section**](inf-ddinstall-filters-section.md).  See [Device filter driver ordering](../develop/device-filter-driver-ordering.md) for more information.

For earlier versions of Windows, to register a device-specific filter driver, create a registry entry through an **AddReg** entry in the _DDInstall_**.HW** section of the device's INF file. For a device-specific upper filter, create an entry named **UpperFilters**. For a device-specific lower filter, create an entry named **LowerFilters**. For example, the following INF excerpt installs _ExampleFilterDriver_ as an upper filter on the _ExampleFunctionDriver_ driver:

```inf
[Example_install]
CopyFiles=Filter_copyfiles, Function_copyfiles
 
[Example_install.HW]
AddReg=Filter_addreg
 
[Example_install.Services]
AddService=ExampleFunctionDriver,0x00000002,Function_ServiceInstallSection
AddService=ExampleFilterDriver,,Filter_ServiceInstallSection

[Filter_addreg] 
HKR,,"UpperFilters",0x00010000,"ExampleFilterDriver" ; REG_MULTI_SZ value 

[Filter_ServiceInstallSection]
DisplayName    = %Filter_ServiceDesc%
ServiceType    = 1     ; SERVICE_KERNEL_DRIVER
StartType      = 3     ; SERVICE_DEMAND_START
ErrorControl   = 1     ; SERVICE_ERROR_NORMAL
ServiceBinary  = %13%\ExampleFilterDriver.sys
```

## Install a class filter driver

To install a class-wide upper- or lower-filter for a [device setup class](overview-of-device-setup-classes.md), you can supply a _device installation application_ that installs the necessary services. The application can then register the service as being an upper- or lower-filter for the desired device setup classes. To copy the service binaries, the application can use **SetupInstallFilesFromInfSection**. To install the services, the application can use **SetupInstallServicesFromInfSection**. To register the services as upper- and/or lower-filters for particular device setup classes, the application calls **SetupInstallFromInfSection** for each device setup class of interest, using the registry key handle they retrieved from [**SetupDiOpenClassRegKey**](/windows/win32/api/setupapi/nf-setupapi-setupdiopenclassregkey) for the _RelativeKeyRoot_ parameter. For example, consider the following INF sections:

```inf
[DestinationDirs]
upperfilter_copyfiles = 12

[upperfilter_inst]
CopyFiles = upperfilter_copyfiles
AddReg = upperfilter_addreg

[upperfilter_copyfiles]
upperfilt.sys,,,0x00004000  ; COPYFLG_IN_USE_RENAME

[upperfilter_addreg]
; append this service to existing REG_MULTI_SZ list, if any
HKR,,"UpperFilters",0x00010008,"upperfilt" 

[upperfilter_inst.Services]
AddService = upperfilt,,upperfilter_service

[upperfilter_service]
DisplayName   = %upperfilter_ServiceDesc%
ServiceType   = 1   ; SERVICE_KERNEL_DRIVER
StartType     = 3   ; SERVICE_DEMAND_START
ErrorControl  = 1   ; SERVICE_ERROR_NORMAL
ServiceBinary = %12%\upperfilt.sys
```

The device installation application would:

1. Call **SetupInstallFilesFromInfSection** for the \[upperfilter_inst\] section.

2. Call **SetupInstallServicesFromInfSection** for the \[upperfilter_inst.Services\] section.

3. Call **SetupInstallFromInfSection** for the \[upperfilter_inst\] section, once for each class key it wants to register the _upperfilt_ service for.

Each call would specify **SPINST_REGISTRY** for the _Flags_ argument, to indicate that only registry modifications need to be performed.
