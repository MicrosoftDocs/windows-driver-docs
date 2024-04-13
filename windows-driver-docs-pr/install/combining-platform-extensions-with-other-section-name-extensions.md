---
title: Combining Platform Extensions with Other Section Name Extensions
description: Combining Platform Extensions with Other Section Name Extensions
keywords:
- INF files WDK device installations , platform extensions
- platform extensions WDK INF files
- extensions WDK INF platform
- combining platform extensions WDK INF files
- install-section-name WDK INF files
- decorated INF WDK
- operating systems WDK
ms.date: 02/02/2022
---

# Combining Platform Extensions with Other Section Name Extensions

As indicated on [Creating INF Files for Multiple Platforms and Operating Systems](creating-inf-files-for-multiple-platforms-and-operating-systems.md), platform extension decorations are required for [**INF Models sections**](inf-models-section.md), but there are other sections where they are optional. Whether or not platform extension decorations are used on these sections where it is optional generally depends on if the INF is attempting to support different platforms or not and if the installation instructions (including the exact files to copy) are the same on each platform.

When using platform extensions on a [**INF DDInstall Section**](inf-ddinstall-section.md), all related DDInstall sections, such as <em>DDInstall</em>**.Services**, <em>DDInstall</em>**.HW**, and <em>DDInstall</em>**.Interfaces** sections, must use the same platform extension.

INF files that contain *install-section-name* platform extensions can also include platform extensions with their [**INF SourceDisksNames section**](inf-sourcedisksnames-section.md) and [**INF SourceDisksFiles section**](inf-sourcedisksfiles-section.md) entries, to specify installation file locations in a platform-specific manner.

## Example: Multiple platforms with same installation instructions and same files copied

This excerpt from an example INF file demonstrates how an INF might be structured if it should support multiple platforms where the files copied (if any) and installation instructions are the same for each platform.

```inf
[SourceDisksFiles]
ArchitectureAgnosticFile.txt=1

[ExampleModelsSection.NTx86]
%DeviceDesc%=ExampleInstallSection,ExampleHardwareId

[ExampleModelsSection.NTamd64]
%DeviceDesc%=ExampleInstallSection,ExampleHardwareId

[ExampleInstallSection]
CopyFiles=FilesToCopy

[FilesToCopy]
ArchitectureAgnosticFile.txt

[ExampleInstallSection.Hw]
...
```

## Example: Multiple platforms with same installation instructions and different files copied

This excerpt from an example INF file demonstrates how an INF might be structured if it should support multiple platforms where the files copied are different for each platform. The files to be copied can be differentiated by architecture specific [SourceDisksFiles] sections, but the installation sections can still be the same.

```inf
[SourceDisksFiles.x86]
ArchitectureSpecificBinary.sys=1,x86

[SourceDisksFiles.amd64]
ArchitectureSpecificBinary.sys=1,amd64

[ExampleModelsSection.NTx86]
%DeviceDesc%=ExampleInstallSection,ExampleHardwareId

[ExampleModelsSection.NTamd64]
%DeviceDesc%=ExampleInstallSection,ExampleHardwareId

[ExampleInstallSection]
CopyFiles=FilesToCopy

[FilesToCopy]
ArchitectureSpecificBinary.sys

[ExampleInstallSection.Services]
AddService=ExampleService,2,ExampleServiceInstallSection

[ExampleServiceInstallSection]
...
```

## Example: Multiple platforms with different installation instructions and different files copied

This excerpt from an example INF file demonstrates how an INF might be structured if it should support multiple platforms where the files copied are different for each platform and there are different installation instructions.

```inf
[SourceDisksFiles.x86]
ArchitectureSpecificBinary.sys=1,x86
x86OnlyBinary.dll=1,x86

[SourceDisksFiles.amd64]
ArchitectureSpecificBinary.sys=1,amd64

[ExampleModelsSection.NTx86]
%DeviceDesc%=ExampleInstallSection,ExampleHardwareId

[ExampleModelsSection.NTamd64]
%DeviceDesc%=ExampleInstallSection,ExampleHardwareId

[ExampleInstallSection.NTx86]
CopyFiles=FilesToCopy_x86

[FilesToCopy_x86]
ArchitectureSpecificBinary.sys
x86OnlyBinary.dll

[ExampleInstallSection.NTx86.Services]
AddService=ExampleService,2,ExampleServiceInstallSection

[ExampleInstallSection.NTamd64]
CopyFiles=FilesToCopy_amd64

[FilesToCopy_amd64]
ArchitectureSpecificBinary.sys

[ExampleInstallSection.NTamd64.Services]
AddService=ExampleService,2,ExampleServiceInstallSection

[ExampleServiceInstallSection]
...
```
