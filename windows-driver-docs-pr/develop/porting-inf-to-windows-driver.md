---
title: Porting an INF to Follow Driver Package Isolation
description: This article provides tips on how to port an INF from old syntax to conform to driver package isolation
ms.date: 01/05/2024
---

# Porting an INF to follow driver package isolation

This article is intended to be a quick lookup guide to help you update an INF file to follow [driver package isolation](driver-isolation.md) as part of updating your driver package to be a [Windows Driver](getting-started-with-windows-drivers.md). The following sections provide examples of some of the more common things you may have in your driver package INF file with references to information on how to update those to be driver package isolation compliant.  If your driver package needs to support the old way of doing something for older operating system versions while using the new way on newer operating system versions, see [Combining Platform Extensions with Operating System Versions](../install/combining-platform-extensions-with-operating-system-versions.md) for how to achieve that in an INF.

## DestinationDirs isn't DIRID 13

If your [DestinationDirs section](../install/inf-destinationdirs-section.md) specifies a destination for files that isn't [DIRID](../install/using-dirids.md) 13, then the INF isn't compliant with driver package isolation. All files in the driver package must be [run from the Driver Store](run-from-driver-store.md) which means using DIRID 13. This may require updates to more than just the DestinationDirs section.  Other operations performed by the INF that refer to files payloaded by the INF may need updating also. For example, you may need to update the ServiceBinary directive in a service install section referenced by an AddService directive or a registry value written by an AddReg directive. In general, run from Driver Store is supported on Windows 10 1709 and later versions of Windows, but some device stacks may not support files that plug into those stacks being run from the Driver Store until a later release.  For more information, see [run from the Driver Store](run-from-driver-store.md).

## Using AddReg to register ETW providers and EventLog channels

If your INF uses an [AddReg directive](../install/inf-addreg-directive.md) to register an ETW provider and EventLog channels, then the INF isn't compliant with driver package isolation.  For example, your INF may have:

```inf
HKLM,"SOFTWARE\Microsoft\Windows\CurrentVersion\WINEVT\Channels\ExampleProvider/Analytic", "OwningPublisher", 0x0, "{35356277-0b54-43da-b324-671006d74759}"
HKLM,"SOFTWARE\Microsoft\Windows\CurrentVersion\WINEVT\Channels\ExampleProvider/Analytic", "Enabled", 0x00010001, 1
HKLM,"SOFTWARE\Microsoft\Windows\CurrentVersion\WINEVT\Channels\ExampleProvider/Analytic", "Isolation", 0x00010001, 1
HKLM,"SOFTWARE\Microsoft\Windows\CurrentVersion\WINEVT\Channels\ExampleProvider/Analytic", "ChannelAccess",0x0, \
"O:BAG:SYD:(A;;0xf0007;;;SY)(A;;0x7;;;BA)(A;;0x3;;;BO)(A;;0x5;;;SO)(A;;0x1;;;IU)(A;;0x3;;;SU)(A;;0x1;;;S-1-5-3)(A;;0x2;;;S-1-5-33)(A;;0x1;;;S-1-5-32-573)"
HKLM,"SOFTWARE\Microsoft\Windows\CurrentVersion\WINEVT\Channels\ExampleProvider/Analytic", "Type", 0x00010001, 2
HKLM,"SOFTWARE\Microsoft\Windows\CurrentVersion\WINEVT\Publishers\{35356277-0b54-43da-b324-671006d74759}" , , 0x0, "ExampleProvider"
HKLM,"SOFTWARE\Microsoft\Windows\CurrentVersion\WINEVT\Publishers\{35356277-0b54-43da-b324-671006d74759}", "ResourceFileName", 0x00020000, "%13%\ExampleBinary.sys"
HKLM,"SOFTWARE\Microsoft\Windows\CurrentVersion\WINEVT\Publishers\{35356277-0b54-43da-b324-671006d74759}", "MessageFileName", 0x00020000, "%13%\ExampleBinary.sys"
HKLM,"SOFTWARE\Microsoft\Windows\CurrentVersion\WINEVT\Publishers\{35356277-0b54-43da-b324-671006d74759}\ChannelReferences\0", , 0x0, "ExampleProvider/Analytic"
HKLM,"SOFTWARE\Microsoft\Windows\CurrentVersion\WINEVT\Publishers\{35356277-0b54-43da-b324-671006d74759}\ChannelReferences\0", "Id", 0x00010001, 16
HKLM,"SOFTWARE\Microsoft\Windows\CurrentVersion\WINEVT\Publishers\{35356277-0b54-43da-b324-671006d74759}\ChannelReferences\0", "Flags", 0x00010001, 0
HKLM,"SOFTWARE\Microsoft\Windows\CurrentVersion\WINEVT\Publishers\{35356277-0b54-43da-b324-671006d74759}\ChannelReferences", Count, 0x00010001, 1
```

Instead of using an AddReg to register ETW providers and EventLog channels, they should be registered using an [AddEventProvider directive](../install/inf-addeventprovider-directive.md) from a [DDInstall.Events section](../install/inf-ddinstall-events-section.md). For example:

```inf
[ExampleDDInstall.Events]
AddEventProvider={35356277-0b54-43da-b324-671006d74759}, Example_EVvntProvider_Inst

[Example_EventProvider_Inst]
ProviderName=ExampleProvider
ResourceFile=%13%\ExampleBinary.sys
MessageFile=%13%\ExampleBinary.sys
AddChannel=ExampleProvider/Analytic,0x3,Example_Channel_Inst ; Note that the type of the channel here is different than in the raw AddReg. Please see the AddEventProvider documentation for appropriate values

[Example_Channel_Inst]
Isolation=1
Access="O:BAG:SYD:(A;;0xf0007;;;SY)(A;;0x7;;;BA)(A;;0x3;;;BO)(A;;0x5;;;SO)(A;;0x1;;;IU)(A;;0x3;;;SU)(A;;0x1;;;S-1-5-3)(A;;0x2;;;S-1-5-33)(A;;0x1;;;S-1-5-32-573)"
Enabled=1
Value=16
```

Using an [AddEventProvider directive](../install/inf-addeventprovider-directive.md) from a [DDInstall.Events section](../install/inf-ddinstall-events-section.md) is supported on Windows 10 1809 and later versions of Windows.

## Using AddReg to register an AutoLogger

If your INF uses an [AddReg directive](../install/inf-addreg-directive.md) to register or modify an ETW AutoLogger, then the INF isn't compliant with driver package isolation. For example, your INF may have:

```inf
HKLM,SYSTEM\CurrentControlSet\Control\WMI\Autologger\ExampleAutoLogger, BufferSize, %REG_DWORD%, 0x00000040
HKLM,SYSTEM\CurrentControlSet\Control\WMI\Autologger\ExampleAutoLogger, GUID, %REG_SZ%, "{6f1373c7-eec8-495c-bfe5-1270336368df}"
HKLM,SYSTEM\CurrentControlSet\Control\WMI\Autologger\ExampleAutoLogger, Start, %REG_DWORD%, 0x00000001
HKLM,SYSTEM\CurrentControlSet\Control\WMI\Autologger\ExampleAutoLogger, MaximumBuffers, %REG_DWORD%, 0x00000040
HKLM,SYSTEM\CurrentControlSet\Control\WMI\Autologger\ExampleAutoLogger, LogFileMode, %REG_DWORD%, 0x400
HKLM,SYSTEM\CurrentControlSet\Control\WMI\Autologger\ExampleAutoLogger\{35356277-0b54-43da-b324-671006d74759}, EnableLevel, %REG_DWORD%, 0x00000004
HKLM,SYSTEM\CurrentControlSet\Control\WMI\Autologger\ExampleAutoLogger\{35356277-0b54-43da-b324-671006d74759}, MatchAnyKeyword, %REG_QWORD%, 0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00
HKLM,SYSTEM\CurrentControlSet\Control\WMI\Autologger\ExampleAutoLogger\{35356277-0b54-43da-b324-671006d74759}, Enabled, %REG_DWORD%, 0x00000001
```

Instead of using an AddReg to register or update an AutoLogger, it should be registered or updated using an [AddAutoLogger or UpdateAutoLogger directive](../install/inf-addupdateautologger-directive.md) from a [DDInstall.Events section](../install/inf-ddinstall-events-section.md). For example:

```inf
[ExampleDDInstall.Events]
AddAutoLogger=ExampleAutoLogger,{6f1373c7-eec8-495c-bfe5-1270336368df},Example_AutoLogger_Inst

[Example_AutoLogger_Inst]
Start=1
BufferSize = 0x40
LogFileMode=0x400
MaximumBuffers=0x40
AddAutoLoggerProvider={35356277-0b54-43da-b324-671006d74759},Example_AutoLoggerProvider_Inst

[Example_AutoLoggerProvider_Inst]
Enabled=1
EnableLevel=0x4
MatchAnyKeyword=0
```

Using an [AddAutoLogger or UpdateAutoLogger directive](../install/inf-addupdateautologger-directive.md) from a [DDInstall.Events section](../install/inf-ddinstall-events-section.md) is supported on Windows 11 and later versions of Windows.

## Using AddReg to add an entry to the RunOnce key

If your INF uses an [AddReg directive](../install/inf-addreg-directive.md) to add an entry to the RunOnce key, then the INF isn't compliant with driver package isolation. For example, your INF may have:

```inf
[ExampleDDInstall]
AddReg = Example_Registry

[Example_Registry]
HKLM, Software\Microsoft\Windows\CurrentVersion\RunOnce, ExampleEntry, ,"application.exe"
```

This isn't supported. An INF shouldn't be modifying global registry entries.  If a one-time setup action is needed when the driver package is installed, you can use an [AddSoftware directive](../install/inf-addsoftware-directive.md) from within a [component INF file](../install/using-a-component-inf-file.md) to launch it.  This is only for non-critical actions.  Critical functionality for the device or devices installed with this driver package shouldn't depend on actions being run that are external to the device installation.

## Using AddReg to add an entry to the Run key

If your INF uses an [AddReg directive](../install/inf-addreg-directive.md) to add an entry to the Run key, then the INF isn't compliant with driver package isolation. For example, your INF may have:

```inf
[ExampleDDInstall]
AddReg = Example_Registry

[Example_Registry]
HKLM, Software\Microsoft\Windows\CurrentVersion\Run, ExampleEntry, ,"application.exe"
```

This isn't supported. An INF shouldn't be modifying global registry entries.  If the Run entry is to add value add software to the system, your application should be a Universal Windows Platform application and installed using an [AddSoftware directive](../install/inf-addsoftware-directive.md) from a [DDInstall.Software section](../install/inf-ddinstall-software-section.md). For more information, see [Pairing a driver with a Universal Windows Platform (UWP) app](../install/pairing-app-and-driver-versions.md).  If this software is a service that doesn't need to present any UI, then a Win32 service can be registered from the driver package with an [AddService directive](../install/inf-addservice-directive.md). When registering a service that is associated with a device, the service should only be running when the device is present.  The service should have a start type of 'demand start' and should use an AddTrigger directive from the service install section to set up the triggers that will cause the service to be started when the device is present on the system.  This is done by identifying a device interface that the driver on the device will expose and using the AddTrigger directive to specify that the service should be started when that hardware appears.  At runtime, the service should monitor for the device going away.  If the device is removed from the system so the service doesn't need to continue running, the service should stop itself. To register for device interface arrival and removal notifications, see [CM_Register_Notification](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_register_notification).

## Using CopyFiles to add files to the 'Program Files' directories

If your INF uses a [CopyFiles directive](../install/inf-copyfiles-directive.md) to add files to the 'Program Files' directories, then the INF is not compliant with driver package isolation. This includes, but is not limited to, usage of the [DIRIDs](../install/using-dirids.md) 16422, 16426, 16427, and 16428. For example, your INF may have:
```inf
[DestinationDirs]
Example_CopyFiles = 16422, Contoso

[ExampleDDInstall]
CopyFiles = Example_CopyFiles

[Example_CopyFiles]
ExampleFile.exe
```

This is not supported. An INF should not be copying files out to global locations.  The 'Program Files' directories are typically used to install software applications, not drivers.  If your goal is to build and supply a companion application for your device that communicates with your driver, then please see the [Hardware Support App guidance](../devapps/hardware-support-app--hsa--steps-for-driver-developers.md). For example, your application can be a Universal Windows Platform application and installed using an [AddSoftware directive](../install/inf-addsoftware-directive.md) from a [DDInstall.Software section](../install/inf-ddinstall-software-section.md). See [Pairing a driver with a Universal Windows Platform (UWP) app](../install/pairing-app-and-driver-versions.md) for more information.  If the CopyFiles entry is not to add a companion application to the system and the files should remain as part of the driver package, they need to be made to be '[run from the Driver Store](run-from-driver-store.md)'.

## CoInstaller that launches UI

If your INF uses a CoInstaller to install an application that the user should interact with, then the INF isn't compliant with driver package isolation. For example, your INF may register a CoInstaller like this:

```inf
[ExampleDDInstall.CoInstallers]
CopyFiles = CoInstallerCopyFilesSection
AddReg = Example_CoInstallers_AddReg

[CoInstallerCopyFilesSection]
ExampleCoInstall.dll

[Example_CoInstallers_AddReg]
HKR,,CoInstallers32,0x00010000,"ExampleCoInstall.dll,ExampleCoInstallEntryPoint"
```

For information on how to handle this situation, see [Removing Co-installers from Driver Packages](./removing-coinstallers.md).

## Using AddReg to modify a service that isn't added by the INF

If your INF uses an [AddReg directive](../install/inf-addreg-directive.md) to modify the state of a service that isn't added by an AddService directive in your INF, then the INF isn't compliant with driver package isolation.  For example, your INF may have:

```inf
[ExampleDDInstall]
AddReg = Example_Registry

[Example_Registry]
HKLM,SYSTEM\CurrentControlSet\Services\ServiceNotCreatedByThisInf\ExampleKey, ExampleValue, %REG_DWORD%, 1
```

This isn't supported. An INF should only be changing settings on services created by that INF and the INF should remove this AddReg.

## Using AddReg to modify state in the root of a service

If your INF uses an [AddReg directive](../install/inf-addreg-directive.md) to create keys or values in the root of a service's state, then the INF isn't compliant with driver package isolation.  For example, your INF may have:

```inf
[ExampleDDInstall.Services]
AddService = ExampleService,0x2,Example_Service_Inst

[Example_Service_Inst]
DisplayName   = %SvcDesc%
ServiceType   = %SERVICE_KERNEL_DRIVER%
StartType     = %SERVICE_DEMAND_START%
ErrorControl  = %SERVICE_ERROR_NORMAL%
ServiceBinary = %13%\ExampleBinary.sys
AddReg = Example_Service_Registry

[Example_Service_Registry]
HKR,,ExampleValue,%REG_DWORD%,0x00000040
HKR,CustomSubkey,ExampleValue,%REG_DWORD%,0x00000040
```

To be driver package isolation compliant, an AddReg directive supplying service registry keys and values can only modify keys and values under the service's Parameters subkey.  The settings need to be moved under the service's Parameters subkey and the Parameters subkey can be accessed at runtime with [IoOpenDriverRegistryKey](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioopendriverregistrykey) using a RegKeyType of DriverRegKeyParameters. IoOpenDriverRegistryKey is supported on Windows 10 1803 and later versions of Windows.

## Using HKCR AddReg to register an APO

If your INF uses an [AddReg directive](../install/inf-addreg-directive.md) with an HKCR registry root to register an Audio Processing Object (APO), then the INF isn't compliant with driver package isolation. For example, your INF may have:

```inf
HKCR,AudioEngine\AudioProcessingObjects\%EXAMPLE_CLSID%, "FriendlyName", , %APO_FriendlyName%
HKCR,AudioEngine\AudioProcessingObjects\%EXAMPLE_CLSID%, "Copyright", , %MfgName%
HKCR,AudioEngine\AudioProcessingObjects\%EXAMPLE_CLSID%, "MajorVersion", 0x00010001, 1
HKCR,AudioEngine\AudioProcessingObjects\%EXAMPLE_CLSID%, "MinorVersion", 0x00010001, 1
HKCR,AudioEngine\AudioProcessingObjects\%EXAMPLE_CLSID%, "Flags", 0x00010001, 0x0000000d
HKCR,AudioEngine\AudioProcessingObjects\%EXAMPLE_CLSID%, "MinInputConnections", 0x00010001, 1
HKCR,AudioEngine\AudioProcessingObjects\%EXAMPLE_CLSID%, "MaxInputConnections", 0x00010001, 1
HKCR,AudioEngine\AudioProcessingObjects\%EXAMPLE_CLSID%, "MinOutputConnections", 0x00010001, 1
HKCR,AudioEngine\AudioProcessingObjects\%EXAMPLE_CLSID%, "MaxOutputConnections", 0x00010001, 1
HKCR,AudioEngine\AudioProcessingObjects\%EXAMPLE_CLSID%, "MaxInstances", 0x00010001, 0xffffffff
HKCR,AudioEngine\AudioProcessingObjects\%EXAMPLE_CLSID%, "NumAPOInterfaces", 0x00010001, 1
HKCR,AudioEngine\AudioProcessingObjects\%EXAMPLE_CLSID%, "APOInterface0", , "{b0a50980-ded6-4f45-84cb-19d2d1245f6d}"
```

Instead, the APO registration information should be in a section referenced by an AddReg directive from a DDInstall section. The HKCR registry root should be changed to an HKR registry root to put the settings relative to the device's "software" (also known as "driver") registry state location. For more information, see [Registering APOs for Processing Modes and Effects in the INF File](../audio/implementing-audio-processing-objects.md#registering-apos-for-processing-modes-and-effects-in-the-inf-file).

## UMDF driver version is less than 2

If your driver package payloads a [User-Mode Driver Framework (UMDF)](../wdf/getting-started-with-umdf-version-2.md) driver that uses a UMDF version earlier than version 2, then it isn't compliant with "Windows Drivers". For more information on how to move your UMDF driver to a more recent UMDF version, see [Porting a Driver from UMDF 1 to UMDF 2](../wdf/porting-a-driver-from-umdf-1-to-umdf-2.md).


## Using AddReg to add an upper or lower filter to a device stack

If your INF uses an [AddReg directive](../install/inf-addreg-directive.md) to add an upper or lower filter to a device stack, then the INF isn't compliant with driver package isolation. For example, your INF may have:

```inf
[ExampleDDInstall.HW]
AddReg = FilterAddReg

[FilterAddReg]
HKR,,"UpperFilters",0x00010000,"ExampleFilterDriver" ; REG_MULTI_SZ value
```

Instead, the filter should be added to the device stack using the [AddFilter](../install/inf-addfilter-directive.md) directive. For example:

```inf
[ExampleDDInstall.Filters]
AddFilter = ExampleFilterDriver,, ExampleFilterSection

[ExampleFilterSection]
FilterPosition = Upper
```

See [Device filter driver ordering](device-filter-driver-ordering.md) for more details on adding device filters.

## Using AddReg to register Media Category Name values

If your INF uses an [AddReg directive](../install/inf-addreg-directive.md) to register a Media Category Name value, then the INF isn't compliant with driver package isolation. For example, your INF may have:

```inf
[ExampleDDInstall]
AddReg=MediaCategoryRegistration

[MediaCategoryRegistration]
HKLM,SYSTEM\CurrentControlSet\Control\MediaCategories\%ExampleGuid%,Name,,%ExampleName%
```

Instead of using an AddReg to register a Media Category name under the global registry location, they should be registered in device relative state using an HKR AddReg from the [DDInstall section](../install/inf-ddinstall-section.md). For example:

```inf
[ExampleDDInstall]
AddReg=MediaCategoryRegistration

[MediaCategoryRegistration]
HKR,MediaCategories\%ExampleGuid%,Name,,%ExampleName%
```

Using device relative state to register Media Category names is supported on Windows 10, version 1809 and later versions of Windows. See [Friendly Names for Audio Endpoint Devices](../audio/friendly-names-for-audio-endpoint-devices.md) for more information.

## Using AddReg to register Media Category Display values

If your INF uses an [AddReg directive](../install/inf-addreg-directive.md) to register a Media Category Display value, then the INF isn't compliant with driver package isolation. For example, your INF may have:

```inf
[ExampleDDInstall]
AddReg=MediaCategoryRegistration

[MediaCategoryRegistration]
HKLM,SYSTEM\CurrentControlSet\Control\MediaCategories\%ExampleGuid%,Display,1,00,00,00,00
```

This value is not used and should be removed from the INF.