---
title: InfVerif Error 1330
description: InfVerif (InfVerif.exe) is a tool that you can use to test a driver INF file. In addition to reporting INF syntax problems, the tool reports if the INF file is universal.
ms.date: 03/05/2019
ms.localizationpriority: medium
---

# InfVerif Error 1330 - 1333

InfVerif Error 1330 helps prevent a functional error where one destination file gets overwritten by multiple source files. For example:

```command
[CopyFiles.A]
DesiredFileName1,SourceFile1A ; Used by DDInstallSection A

[CopyFiles.B]
DesiredFileName1,SourceFile1B ; Used by DDInstallSection B
```

When multiple [DDInstall sections](../install/inf-ddinstall-section.md) copy different source files to a single destination file using the [CopyFiles](../install/inf-copyfiles-directive.md) directive, these **CopyFiles** could conflict if the **DDInstall sections** all get processed on the same system. Examples of this is if two different devices are using the same driver but different install sections, or in some offline driver imaging and deployment scenarios. Because multiple source files from the different **DDInstall sections** get copied to the same exact single destination file, the different source files from different **DDInstall sections** overwrite each other so that the last file copied is the one placed in the destination, which may not be the expected results.

## Cases

This document provides guidance for how to update the old syntax to methods that remove the functional error for the following cases. Not all cases are listed below, as there could be other reasons specific to each INF.

* Different **DDInstall sections** rename a service binary for one service

* Different **DDInstall sections** rename a source file to get copied over to a destination file location accessed by the driver or a User Mode application

### Different **DDInstall sections** rename a service binary for one service

The following code is an example of how different **DDInstall sections** might rename a service binary for one service:

```command
[DDInstallSection_A]
CopyFiles = CopyFiles.A

[DDInstallSection_B]
CopyFiles = CopyFiles.B

[CopyFiles.A]
ServiceBinaryFile, ServiceBinaryA

[CopyFiles.B]
ServiceBinaryFile, ServiceBinaryB

[DDInstallSection_A.Services]
AddService = ServiceName, 0x00000002, ServiceName_Install

[DDInstallSection_B.Services]
AddService = ServiceName, 0x00000002, ServiceName_Install

[ServiceName_Install]
ServiceType    = 1
StartType      = 3
ErrorControl   = 0
ServiceBinary  = %12%\ServiceBinaryFile
```

To update this code, create different service names for the different binaries:

```command
[DDInstallSection_A]
CopyFiles = CopyFiles.A

[DDInstallSection_B]
CopyFiles = CopyFiles.B

[CopyFiles.A]
ServiceBinaryA

[CopyFiles.B]
ServiceBinaryB

[DDInstallSection_A.Services]
AddService = ServiceName1, 0x00000002, ServiceName1_Install

[DDInstallSection_B.Services]
AddService = ServiceName2, 0x00000002, ServiceName2_Install

[ServiceName1_Install]
ServiceType    = 1
StartType      = 3
ErrorControl   = 0
ServiceBinary  = %12%\ServiceBinaryA

[ServiceName2_Install]
ServiceType    = 1
StartType      = 3
ErrorControl   = 0
ServiceBinary  = %12%\ServiceBinaryB
```

### Different **DDInstall sections** rename a source file to get copied over to a destination file location accessed by the driver or a User Mode application

In this case, the driver is accessing a fixed file location that is being used as a dynamic file location. To have one dynamic variable that keeps track of multiple source files, you can use an [AddReg](../install/inf-addreg-directive.md) HKR entry to store the path which can be retrieved at runtime. This works because **AddReg** HKR entries are stored relative to a device.

The **AddReg** HKR entry specifies the file locations for source files instead of choosing a single destination file to copy the source files to:

```command
[A.AddReg]
HKR,, FileName1Path, "%13%\SourceFile1A"

[B.AddReg]
HKR,, FileName1Path, "%13%\SourceFile1B"
```

Rather than access a fixed file location, the location of the target file can be retrieved from a setting on the device. The target file
location is stored in a registry value by the INF and retrieved through API calls in the driver.

To provision the values through an INF, use the [INF AddReg directive](../install/inf-addreg-directive.md) using HKR *reg-root* entries in an *add-registry-section* referenced from an [INF DDInstall section](../install/inf-ddinstall-section.md) or [INF DDInstall.HW section](../install/inf-ddinstall-hw-section.md).

Because registry values keep track of the target file instead of a single destination file location, the driver will have to access those
files differently. To access the target file, the driver now needs to call into one of the following APIs to open the registry value and have it return the location of that source file:

#### WDM

* [**IoOpenDeviceRegistryKey**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioopendeviceregistrykey)

#### WDF

* [**WdfDeviceOpenRegistryKey**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceopenregistrykey)

* [**WdfFdoInitOpenRegistryKey**](/windows-hardware/drivers/ddi/wdffdo/nf-wdffdo-wdffdoinitopenregistrykey)

#### Other User Mode code

* [**CM_Open_DevNode_Key**](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_open_devnode_key)

> [!NOTE]
> In this example, the destination location of the files the INF payloads does not affect the solution.  However, to use best practices, the example uses [DIRID](../install/using-dirids.md) 13 since it provides faster installs through fewer file copies.  Please see “[Using DIRIDs](../install/using-dirids.md)” and “[Run from the driver store](../develop/dch-example.md#run-from-the-driver-store)” for more information.

The following example code shows how to update an INF that uses old syntax.

### Details for different source files mapped to one destination file

<table>
<thead>
<tr>
<th>Source Code</th>
<th>Comment</th>
</tr>
</thead>
<tbody>
<tr><td><pre>[DestinationDirs]
CopyFiles.A = 12
CopyFiles.B = 12</br>
[DDInstallSection_A]
CopyFiles  = CopyFiles.A</br>
[DDInstallSection_B]
CopyFiles = CopyFiles.B
</td>
</pre>
<td></br>Pick where files go manually</td>
</tr>
<tr>
<td><pre>[CopyFiles.A]
DesiredFileName1,SourceFile1A ; HW Version A
DesiredFileName2,SourceFile2A ; HW Version A</br>
[CopyFiles.B]
DesiredFileName1,SourceFile1B ; HW Version B
DesiredFileName2,SourceFile2B ; HW Version B
</pre></td>
<td></br><u>File copy technique</u>:
Renaming files so the DDInstall Section being installed picks the source file to get copied over to the destination file path that the driver is linked to.

This doesn’t work in the case that all files for all DDInstall Sections get copied over before install.
</td>
</tr>
</tbody>
</table>

### Details for udating by using AddReg HKR entries

<table>
<thead>
<tr>
<th>Source Code</th>
<th>Comment</th>
</tr>
</thead>
<tbody>
<tr>
<td><pre>[DestinationDirs]
CopyFiles.A = 13
CopyFiles.B = 13
</td>
</pre>
<td></br>Best practice is to leave everything in the driver store directory (Dirid 13)</td>
</tr>
<tr>
<td><pre>[DDInstallSection_A]
CopyFiles = CopyFiles.A</br>
[DDInstallSection_A.HW]
AddReg = A.AddReg</br>
[DDInstallSection_B]
CopyFiles = CopyFiles.B</br>
[DDInstallSection_B.HW]
AddReg = B.AddReg  

</pre></td>

<td></br>Add an AddReg section for each DDInstall Section.HW to keep track of the files needed for that install.

</td>
</tr>

<tr>
<td><pre>[A.AddReg]
HKR,, FileName1Path, "%13%\SourceFile1A"
HKR,, FileName2Path, "%13%\SourceFile2A"</br>
[B.AddReg]
HKR,, FileName1Path, "%13%\SourceFile1A"
HKR,, FileName2Path, "%13%\SourceFile2A"

</pre></td>
<td></br>Multiple source file locations mapped to one registry value. This works because HKR AddReg from a DDInstall or DDInstall.HW section are stored in device settings.  When a device is installed with this driver package, it will only be using one of the DDInstall sections so only one of the HKR AddReg will be used and there will not be a conflict.
</td>
</tr>

<tr>
<td><pre>[CopyFiles.A]
SourceFile1A ; HW Version A
SourceFile2A ; HW Version A</br>
[CopyFiles.B]
SourceFile1B ; HW Version B
SourceFile2B ; HW Version B
</pre></td>
<td></br>All files map to their own location so no functionality errors and INF passes InfVerif.
</br>
Don’t use CopyFiles to rename a file for which DestinationDirs includes Dirid 13.

</td>
</tr>
</tbody>
</table>

### Accessing the file location from the driver (pseudo-code)

```command
Before (Fixed Filename):
    OpenFile(Path\DesiredFileName1)

After (Dynamic Filename):
    OpenDeviceRegistryKey(Device, &KeyHandle)
    RegistryKeyQueryValue(KeyHandle, FileNamePath1, &SourceFile)
    OpenFile(SourceFile)
```

### Accessing the file location from User Mode

When accessing the target file from User Mode, you won't have the device context that a driver has. In this case you need to add an additional step. Before opening the key handle, find the device that contains the registry value indicating what file to load.

See [Run from the driver store](../develop/dch-example.md#run-from-the-driver-store) to learn how to filter a device list to find your device and open the handle to the registry location in user mode, using Dirid 13 for best practices.

## Errors 1331 - 1333

Errors 1331 - 1333 are all the same problem but relating to registy values, registry values within services, and services respectively. The examples in documentation for error 1330 cover techniques to resolve errors 1331 - 1333.
