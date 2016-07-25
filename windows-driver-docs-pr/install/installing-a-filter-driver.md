---
title: Installing a Filter Driver
description: Installing a Filter Driver
ms.assetid: 48ffa6db-3254-4108-b8bb-5884b9168a9d
keywords: ["Device setup WDK device installations , filter drivers", "device installations WDK , filter drivers", "installing devices WDK , filter drivers", "filter drivers WDK device installations", "device-specific filter drivers WDK device installations", "class filter drivers WDK device installations", "SetupInstallFilesFromInfSection", "UpperFilters", "LowerFilters"]
---

# Installing a Filter Driver


## <a href="" id="ddk-installing-a-filter-driver-dg"></a>


A PnP filter driver can support a specific device or all devices in a setup class and can attach below a device's function driver (a lower filter) or above a device's function driver (an upper filter). See [Types of WDM Drivers](https://msdn.microsoft.com/library/windows/hardware/ff564862) for more information about PnP driver layers.

### <a href="" id="ddk-installing-a-device-specific-filter-driver-dg"></a>Installing a Device-Specific Filter Driver

To register a device-specific filter driver, create a registry entry through an **AddReg** entry in the *DDInstall***.HW** section of the device's INF file. For a device-specific upper filter, create an entry named **UpperFilters**. For a device-specific lower filter, create an entry named **LowerFilters**. For example, the following INF excerpt installs *cdaudio* as an upper filter on the *cdrom* driver:

```
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

```
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

1.  Call **SetupInstallFilesFromInfSection** for the \[upperfilter\_inst\] section.

2.  Call **SetupInstallServicesFromInfSection** for the \[upperfilter\_inst.Services\] section.

3.  Call **SetupInstallFromInfSection** for the \[upperfilter\_inst\] section, once for each class key it wants to register the *upperfilt* service for.

Each call would specify **SPINST\_REGISTRY** for the *Flags* argument, to indicate that only registry modifications need to be performed.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Installing%20a%20Filter%20Driver%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




