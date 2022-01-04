---
title: INF Files for Callout Drivers
description: INF Files for Callout Drivers
keywords:
- Windows Filtering Platform callout drivers WDK , installing
- callout drivers WDK Windows Filtering Platform , installing
- installing callout drivers WDK Windows Filtering Platform
- INF files WDK Windows Filtering Platform
ms.date: 04/20/2017
---

# INF Files for Callout Drivers

A Windows Filtering Platform callout driver is installed by a setup information file (INF) file. INF files for callout drivers contain only the following INF file sections:

[**INF Version Section**](../install/inf-version-section.md)

[**INF SourceDisksNames Section**](../install/inf-sourcedisksnames-section.md)

[**INF SourceDisksFiles Section**](../install/inf-sourcedisksfiles-section.md)

[**INF DestinationDirs Section**](../install/inf-destinationdirs-section.md)

[**INF DefaultInstall Section**](../install/inf-defaultinstall-section.md)

[**INF DefaultInstall.Services Section**](../install/inf-defaultinstall-services-section.md)

[**INF Strings Section**](../install/inf-strings-section.md)

For example:

```INF
;
; Example callout driver INF file
;

[Version]
Signature = "$Windows NT$"
Provider = %Msft%
CatalogFile = "ExampleCalloutDriver.cat"
DriverVer = 01/15/05,1.0

[SourceDisksNames]
1 = %DiskName%

[SourceDisksFiles]
ExampleCalloutDriver.sys = 1

[DestinationDirs]
DefaultDestDir = 12 ; %windir%\system32\drivers
ExampleCalloutDriver.DriverFiles = 12 ; %windir%\system32\drivers

[DefaultInstall]
OptionDesc = %Description%
CopyFiles = ExampleCalloutDriver.DriverFiles

[DefaultInstall.Services]
AddService = %ServiceName%,,ExampleCalloutDriver.Service

[DefaultUninstall]
DelFiles = ExampleCalloutDriver.DriverFiles

[DefaultUninstall.Services]
DelService = ExampleCalloutDriver,0x200 ; SPSVCINST_STOPSERVICE

[ExampleCalloutDriver.DriverFiles]
ExampleCalloutDriver.sys,,,0x00000040 ; COPYFLG_OVERWRITE_OLDER_ONLY

[ExampleCalloutDriver.Service]
DisplayName = %ServiceName%
Description = %ServiceDesc%
ServiceType = 1  ; SERVICE_KERNEL_DRIVER
StartType = 0    ; SERVICE_BOOT_START
ErrorControl = 1 ; SERVICE_ERROR_NORMAL
ServiceBinary = %12%\ExampleCalloutDriver.sys

[Strings]
Msft = "Microsoft Corporation"
DiskName = "Example Callout Driver Installation Disk"
Description = "Example Callout Driver"
ServiceName = "ExampleCalloutDriver"
ServiceDesc = "Example Callout Driver"
```
