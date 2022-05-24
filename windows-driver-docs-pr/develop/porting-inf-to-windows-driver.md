---
title: Porting an INF to follow driver package isolation
description: This page provides tips on how to port an INF from old syntax to conform to driver package isolation
ms.date: 05/19/2022
---

# Porting an INF to follow driver package isolation

This page is intended to be a quick look up guide to help you update an INF file to follow [driver package isolation](driver-isolation.md) as part of updating your driver package to be a [Windows Driver](getting-started-with-windows-drivers.md). The following sections provide examples of some of the more common things you may have in your driver package INF file with references to information on how to update those to be driver package isolation compliant.  If your driver package needs to support the old way of doing something for older operating system versions while using the new way on newer operating system versions, see [Combining Platform Extensions with Operating System Versions](../install/combining-platform-extensions-with-operating-system-versions.md) for how to achieve that in an INF.

## DestinationDirs is not DIRID 13

If your [DestinationDirs section](../install/inf-destinationdirs-section.md) specifies a destination for files that is not [DIRID](../install/using-dirids.md) 13, then the INF is not compliant with driver package isolation. All files in the driver package must be [run from the Driver Store](run-from-driver-store.md) which means using DIRID 13. Note that this may require updates to more than just the DestinationDirs section.  Other operations performed by the INF that refer to files payloaded by the INF may need updating also. For example, you may need to update the ServiceBinary directive in a service install section referenced by an AddService directive or a registry value written by an AddReg directive. In general, run from Driver Store is supported on Windows 10 1709 and later versions of Windows, but some device stacks may not support files that plug into those stacks being run from the Driver Store until a later release.  See [run from the Driver Store](run-from-driver-store.md) for more details.

## Using AddReg to register ETW providers and EventLog channels

If your INF uses an AddReg directive to register an ETW provider and EventLog channels, then the INF is not compliant with driver package isolation.  For example, your INF may have:
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

If your INF uses an AddReg directive to register or modify an ETW AutoLogger, then the INF is not compliant with driver package isolation. For example, your INF may have:
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

## CoInstaller that launches UI

If your INF uses a CoInstaller to install an application that the user should interact with, then the INF is not compliant with driver package isolation. For example, your INF may register a CoInstaller like this:
```inf
[ExampleDDInstall.CoInstallers]
CopyFiles = CoInstallerCopyFilesSection
AddReg = Example_CoInstallers_AddReg

[CoInstallerCopyFilesSection]
ExampleCoInstall.dll

[Example_CoInstallers_AddReg]
HKR,,CoInstallers32,0x00010000,"ExampleCoInstall.dll,ExampleCoInstallEntryPoint"
```

Instead, your application should be a Universal Windows Platform application and installed using an [AddSoftware directive](../install/inf-addsoftware-directive.md) from a [DDInstall.Software section](../install/inf-ddinstall-software-section.md). See [Pairing a driver with a Universal Windows Platform (UWP) app](../install/pairing-app-and-driver-versions.md) for more information. An [AddSoftware directive](../install/inf-addsoftware-directive.md) is supported on Windows 10 1703 and later versions of Windows.

## Using AddReg to modify a service that is not added by the INF

If your INF uses an AddReg directive to modify the state of a service that is not added by an AddService directive in your INF, then the INF is not compliant with driver package isolation.  For example, your INF may have:
```inf
[ExampleDDInstall]
AddReg= Example_Registry

[Example_ Registry]
HKLM,SYSTEM\CurrentControlSet\Services\ServiceNotCreatedByThisInf\ExampleKey, ExampleValue, %REG_DWORD%, 1
```

This is not supported. An INF should only be changing settings on services created by that INF and the INF should remove this AddReg.

## Using AddReg to modify state in the root of a service

If your INF uses an AddReg directive to create keys or values in the root of a service’s state, then the INF is not compliant with driver package isolation.  For example, your INF may have:
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

To be driver package isolation compliant, an AddReg directive supplying service registry keys and values can only modify keys and values under the service’s Parameters subkey.  The settings need to be moved under the service’s Parameters subkey and the Parameters subkey can be accessed at runtime with [IoOpenDriverRegistryKey](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioopendriverregistrykey) using a RegKeyType of DriverRegKeyParameters. IoOpenDriverRegistryKey is supported on Windows 10 1803 and later versions of Windows.

## Using HKCR AddReg to register an APO

If your INF uses an AddReg directive with an HKCR registry root to register an Audio Processing Object (APO), then the INF is not compliant with driver package isolation. For example, your INF may have:
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

Instead, the APO registration information should be in a section referenced by an AddReg directive from a DDInstall section. The HKCR registry root should be changed to an HKR registry root to put the settings relative to the device’s “software” (aka “driver”) registry state location.  See [Registering APOs for Processing Modes and Effects in the INF File](../audio/implementing-audio-processing-objects.md#registering-apos-for-processing-modes-and-effects-in-the-inf-file) for more information.
