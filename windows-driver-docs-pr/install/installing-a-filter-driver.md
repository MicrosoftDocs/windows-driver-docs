---
title: Installing a Filter Driver
description: Installing a Filter Driver
ms.assetid: 48ffa6db-3254-4108-b8bb-5884b9168a9d
keywords:
- Device setup WDK device installations , filter drivers
- device installations WDK , filter drivers
- installing devices WDK , filter drivers
- filter drivers WDK device installations
- device-specific filter drivers WDK device installations
- class filter drivers WDK device installations
- SetupInstallFilesFromInfSection
- UpperFilters
- LowerFilters
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Installing a Filter Driver





A PnP filter driver can support a specific device or all devices in a setup class and can attach below a device's function driver (a lower filter) or above a device's function driver (an upper filter). See [Types of WDM Drivers](https://msdn.microsoft.com/library/windows/hardware/ff564862) for more information about PnP driver layers.

### <a href="" id="ddk-installing-a-device-specific-filter-driver-dg"></a>Installing a Device-Specific Filter Driver

To register a device-specific filter driver, create a registry entry through an **AddReg** entry in the <em>DDInstall</em>**.HW** section of the device's INF file. For a device-specific upper filter, create an entry named **UpperFilters**. For a device-specific lower filter, create an entry named **LowerFilters**. For example, the following INF excerpt installs *cdaudio* as an upper filter on the *cdrom* driver:

```cpp
:
; Installation section for cdaudio. Sets cdrom as the service 
; and adds cdaudio as a PnP upper filter driver. 
;
[cdaudio_install]
CopyFiles=cdaudio_copyfiles, cdrom_copyfiles
 
[cdaudio_install.HW]
AddReg=cdaudio_addreg
 
[cdaudio_install.Services]
AddService=cdrom,0x00000002,cdrom_ServiceInstallSection
AddService=cdaudio,,cdaudio_ServiceInstallSection
: 

[cdaudio_addreg] 
HKR,,"UpperFilters",0x00010000,"cdaudio" ; REG_MULTI_SZ value 
:

[cdaudio_ServiceInstallSection]
DisplayName    = %cdaudio_ServiceDesc%
ServiceType    = 1     ; SERVICE_KERNEL_DRIVER
StartType      = 3     ; SERVICE_DEMAND_START
ErrorControl   = 1     ; SERVICE_ERROR_NORMAL
ServiceBinary  = %12%\cdaudio.sys
:
```

### <a href="" id="ddk-installing-a-class-filter-driver-dg"></a>Installing a Class Filter Driver

To install a class-wide upper- or lower-filter for a [device setup class](device-setup-classes.md), you can supply a [*device installation application*](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-device-installation-application) that installs the necessary services. The application can then register the service as being an upper- or lower-filter for the desired device setup classes. To copy the service binaries, the application can use **SetupInstallFilesFromInfSection**. To install the services, the application can use **SetupInstallServicesFromInfSection**. To register the services as upper- and/or lower-filters for particular device setup classes, the application calls **SetupInstallFromInfSection** for each device setup class of interest, using the registry key handle they retrieved from [**SetupDiOpenClassRegKey**](https://msdn.microsoft.com/library/windows/hardware/ff552065) for the *RelativeKeyRoot* parameter. For example, consider the following INF sections:

```cpp
:

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
:
```

The device installation application would:

1.  Call **SetupInstallFilesFromInfSection** for the \[upperfilter_inst\] section.

2.  Call **SetupInstallServicesFromInfSection** for the \[upperfilter_inst.Services\] section.

3.  Call **SetupInstallFromInfSection** for the \[upperfilter_inst\] section, once for each class key it wants to register the *upperfilt* service for.

Each call would specify **SPINST_REGISTRY** for the *Flags* argument, to indicate that only registry modifications need to be performed.

 

 





