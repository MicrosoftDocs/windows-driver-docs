---
title: Invoking a Device Properties Dialog Box from Command-line Prompt
description: Invoking a Device Properties Dialog Box from a Command-line Prompt
ms.assetid: 616c93ee-8360-4bab-8e08-48a55cd617f1
keywords:
- device properties dialog box WDK device installations
- invoking device properties dialog box
- DeviceProperties_RunDLL WDK device installations
- machine-name-parameter field WDK device installations
- device-instance-ID-parameter field WDK device inst
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Invoking a Device Properties Dialog Box from a Command-line Prompt


The [DeviceProperties_RunDLL](deviceproperties-rundll-function-prototype.md) function in Device Manager can be invoked from a command-line prompt using *rundll32.exe*. The following code example demonstrates the format for invoking **DeviceProperties_RunDLL** from a command prompt.

```cpp
rundll32.exe devmgr.dll, DeviceProperties_RunDLL machine-name-parameter device-instance-ID-parameter
```

The format and requirements for the *machine-name-parameter* field is the same as that described for the command-line string supplied by the *lpCmdLine* parameter of **DeviceProperties_RunDLL**. The format and requirements for the *device-instance-ID-parameter* field is also the same as that described for the *lpCmdLine* command-line string, subject to the following additional requirement: if the *device-instance-ID* subfield includes an ampersand (&), the *device-instance-ID* subfield must be enclosed in quotation marks (").

The following code examples illustrate the format and requirements for supplying a *machine-name-parameter* and *device-instance-ID-parameter* to invoke **DeviceProperties_RunDLL** from a command-line prompt. These examples correspond to the examples provided in [Invoking a Device Properties Dialog Box Programmatically in an Installation Application](invoking-a-device-properties-dialog-box-programmatically-in-an-install.md).

-   (Windows XP and later) An optional *machine-name-parameter* field is not supplied, which indicates, by default, that the computer is the local computer. A required *device-instance-ID-parameter* field supplies the [device instance identifier](device-instance-ids.md) "root\\system\\0000".
    ```cpp
    rundll32.exe devmgr.dll,DeviceProperties_RunDLL /DeviceID root\system\0000
    ```

-   (Windows XP and later) An optional *machine-name-parameter* field is not supplied, which indicates, by default, that the computer is the local computer. A required *device-instance-ID-parameter* field supplies the device instance identifier "PCI\\VEN_8086&DEV_2445 &SUBSYS_010E1028&REV_12\\3&172E68DD&0&FD". Because the device instance identifier includes an ampersand (&), the *device-instance-ID* subfield is enclosed in quotation marks (").
    ```cpp
    rundll32.exe devmgr.dll,DeviceProperties_RunDLL /DeviceID "PCI\VEN_8086&DEV_2445&SUBSYS_010E1028&REV_12\3&172E68DD&0&FD" 
    ```

-   (Windows 2000 and later) A required *machine-name-parameter* field supplies a pair of quotation marks ("") as *machine-name*, which indicates that the computer is the local computer. A required *device-instance-ID-parameter* field supplies the device instance identifier "root\\system\\0000".
    ```cpp
    rundll32.exe devmgr.dll,DeviceProperties_RunDLL /MachineName "" /DeviceID root\system\0000
    ```

-   (Windows 2000 and later) A required *machine-name-parameter* field supplies the remote machine name "\\\\RemoteMachineAbc". A required *device-instance-ID-parameter* field supplies the device instance identifier "root\\system\\0000".
    ```cpp
    rundll32.exe devmgr.dll,DeviceProperties_RunDLL /MachineName \\RemoteMachineAbc /DeviceID root\system\0000
    ```

 

 





