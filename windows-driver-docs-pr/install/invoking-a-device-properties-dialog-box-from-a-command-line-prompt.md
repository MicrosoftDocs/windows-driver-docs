---
title: Invoking a Device Properties Dialog Box from a Command-line Prompt
description: Invoking a Device Properties Dialog Box from a Command-line Prompt
ms.assetid: 616c93ee-8360-4bab-8e08-48a55cd617f1
keywords: ["device properties dialog box WDK device installations", "invoking device properties dialog box", "DeviceProperties_RunDLL WDK device installations", "machine-name-parameter field WDK device installations", "device-instance-ID-parameter field WDK device inst"]
---

# Invoking a Device Properties Dialog Box from a Command-line Prompt


The [DeviceProperties\_RunDLL](deviceproperties-rundll-function-prototype.md) function in Device Manager can be invoked from a command-line prompt using *rundll32.exe*. The following code example demonstrates the format for invoking **DeviceProperties\_RunDLL** from a command prompt.

```
rundll32.exe devmgr.dll, DeviceProperties_RunDLL machine-name-parameter device-instance-ID-parameter
```

The format and requirements for the *machine-name-parameter* field is the same as that described for the command-line string supplied by the *lpCmdLine* parameter of **DeviceProperties\_RunDLL**. The format and requirements for the *device-instance-ID-parameter* field is also the same as that described for the *lpCmdLine* command-line string, subject to the following additional requirement: if the *device-instance-ID* subfield includes an ampersand (&), the *device-instance-ID* subfield must be enclosed in quotation marks (").

The following code examples illustrate the format and requirements for supplying a *machine-name-parameter* and *device-instance-ID-parameter* to invoke **DeviceProperties\_RunDLL** from a command-line prompt. These examples correspond to the examples provided in [Invoking a Device Properties Dialog Box Programmatically in an Installation Application](invoking-a-device-properties-dialog-box-programmatically-in-an-install.md).

-   (Windows XP and later) An optional *machine-name-parameter* field is not supplied, which indicates, by default, that the computer is the local computer. A required *device-instance-ID-parameter* field supplies the [device instance identifier](device-instance-ids.md) "root\\system\\0000".
    ```
    rundll32.exe devmgr.dll,DeviceProperties_RunDLL /DeviceID root\system\0000
    ```

-   (Windows XP and later) An optional *machine-name-parameter* field is not supplied, which indicates, by default, that the computer is the local computer. A required *device-instance-ID-parameter* field supplies the device instance identifier "PCI\\VEN\_8086&DEV\_2445 &SUBSYS\_010E1028&REV\_12\\3&172E68DD&0&FD". Because the device instance identifier includes an ampersand (&), the *device-instance-ID* subfield is enclosed in quotation marks (").
    ```
    rundll32.exe devmgr.dll,DeviceProperties_RunDLL /DeviceID "PCI\VEN_8086&amp;DEV_2445&amp;SUBSYS_010E1028&amp;REV_12\3&amp;172E68DD&amp;0&amp;FD" 
    ```

-   (Windows 2000 and later) A required *machine-name-parameter* field supplies a pair of quotation marks ("") as *machine-name*, which indicates that the computer is the local computer. A required *device-instance-ID-parameter* field supplies the device instance identifier "root\\system\\0000".
    ```
    rundll32.exe devmgr.dll,DeviceProperties_RunDLL /MachineName "" /DeviceID root\system\0000
    ```

-   (Windows 2000 and later) A required *machine-name-parameter* field supplies the remote machine name "\\\\RemoteMachineAbc". A required *device-instance-ID-parameter* field supplies the device instance identifier "root\\system\\0000".
    ```
    rundll32.exe devmgr.dll,DeviceProperties_RunDLL /MachineName \\RemoteMachineAbc /DeviceID root\system\0000
    ```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Invoking%20a%20Device%20Properties%20Dialog%20Box%20from%20a%20Command-line%20Prompt%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




