---
title: INF AddSoftware directive
description: An AddSoftware directive describes the installation of standalone software.
ms.date: 07/08/2022
---

# INF AddSoftware directive

Each **AddSoftware** directive describes the installation of standalone software.  This directive should be used in an INF file of the **SoftwareComponent** setup class. For more details on software components, see [Using a Component INF File](using-a-component-inf-file.md).  This directive is supported for Windows 10 version 1703 and later.

Valid installation types depend on the [target platform](../develop/target-platforms.md). For example, Desktop supports MSI installers and setup EXEs.  

> [!NOTE]
> Type 2 is supported in Universal Drivers, Type 1 is desktop-only.

When a software component INF file specifies **AddSoftware**, the system queues software to be installed after device installation.  There is no guarantee when or if the software will be installed. If referenced software fails to install, the system tries again when the referencing software component is updated.

An **AddSoftware** directive is used within an [**INF *DDInstall*.Software**](inf-ddinstall-software-section.md) section.

```inf
[DDInstall.Software]
AddSoftware=SoftwareName,[flags],software-install-section
```

## Entries

*SoftwareName*  
Specifies the name of the software to be installed.  This name must be unique system-wide, regardless of the INF or section name.  The processing of an **AddSoftware** directive checks the version against previous software installed with the same name by an **AddSoftware** directive from any driver package.  We recommend prefacing the SoftwareName with the vendor name, for example `ContosoControlPanel`.

*flags*  
Specifies one or more (ORed) flags.

**0x00000000**  
The **AddSoftware** directive is processed only once.

**0x00000001**  
The **AddSoftware** directive is processed once for each component device that specifies **AddSoftware** with the same unique *SoftwareName*.

For example, consider a configuration in which three devices are installed using the same INF file. The software installation process runs only once for *flags* 0x00000000 but three times for *flags* 0x00000001.

*software-install-section*  
References an INF-writer-defined section that contains information for installing software.

## Remarks

Each INF-writer-created section name must be unique within the INF file and must follow the general rules for defining section names.  For more information about these rules, see [General Syntax Rules for INF Files](general-syntax-rules-for-inf-files.md).

An **AddSoftware** directive must reference a named *software-install-section* elsewhere in the INF file.  Each such section has the following form:

```inf
[software-install-section]

SoftwareType=type-code
[SoftwareBinary=path-to-binary]
[SoftwareArguments=argument[, argument] …]
[SoftwareVersion=w.x.y.z]
[SoftwareID=pfn://x.y.z]
```

> [!NOTE]
> See **SoftwareType** for information about constraints on section entries and values.

Any software installed using **AddSoftware** must be installed silently (or quietly). In other words, no user interface can be shown to the user during installation.

Any software installed using **AddSoftware** will **not** be uninstalled if the virtual software component device or its parent devices are uninstalled. If your software is not a UWP app (i.e. you're using **AddSoftware** with a SoftwareType of 1), please make sure users can easily uninstall it without leaving a trace in the registry. To do so:

- If you're using an MSI installer, set up an [Add/Remove Programs](/windows/desktop/Msi/configuring-add-remove-programs-with-windows-installer) entry in the application's Windows Installer package.

- If you're using a custom EXE that installs global registry/file state (instead of supplementing local device settings), use the [Uninstall Registry Key](/windows/desktop/Msi/uninstall-registry-key).

### Software-install-section entries and values

**SoftwareType**=*{type-code}*  
**SoftwareType** specifies the type of software installation and is a required entry.

A value of 1 indicates that the associated software is an MSI or EXE binary.  When this value is set, the **SoftwareBinary** entry is also required.  A value of 1 is not supported on Windows 10 S.

If **SoftwareType** is set to 1, **SoftwareBinary** and **SoftwareVersion** are also required, but **SoftwareArguments** and *flags* (in the **AddSoftware** directive) are optional.

Starting in Windows 10 version 1709, a value of 2 indicates that the associated software is a Microsoft Store link.  Use a value of 1 only for device-specific software that has no graphical user interface.  If you have a device-specific app with graphical elements, it should come from the Microsoft Store, and the driver should reference it using a **SoftwareType** value of 2.

If **SoftwareType** is set to 2, **SoftwareID** is required, and *flags* (in the **AddSoftware** directive) are optional. If **SoftwareType** is set to 2, **SoftwareBinary** and **SoftwareVersion** are not used.

> [!NOTE]
> When using SoftwareType 2 of the AddSoftware directive, it is not required to utilize a Component INF.  The directive can be used in any INF successfully.  An AddSoftware directive of Type 1, however, must be used from a Component INF.

Do not use AddSoftware to distribute software that is unrelated to a device. For example, an OEM-specific PC utility program should not be installed with AddSoftware. Instead, use one of the following options to preinstall an app in an OEM image of Windows 10:

- To preinstall a Win32 app, boot to audit mode and install the app. For details, see [Audit Mode Overview](/windows-hardware/manufacture/desktop/audit-mode-overview).

- To preinstall a Microsoft Store (UWP) app, see [Preinstallable apps for desktop devices](/windows-hardware/customize/preinstall/preinstallable-apps-for-windows-10-desktop)

For info about pairing a driver with a Universal Windows Platform (UWP) app, see [Pairing a driver with a Universal Windows Platform (UWP) app](pairing-app-and-driver-versions.md) and [Hardware Support App (HSA): Steps for Driver Developers](../devapps/hardware-support-app--hsa--steps-for-driver-developers.md).

**SoftwareBinary**=*{filename}*  
Specifies the path to the executable.  The system generates command lines like the following:

`MSI: msiexec /i "<SoftwareBinary>" ALLUSERS=1 /quiet /qn /promptrestart [<SoftwareArguments>]`

`EXE: <SoftwareBinary> [<SoftwareArguments>]`

If you use this entry, you must add the executable to the DriverStore by specifying the [INF CopyFiles Directive](inf-copyfiles-directive.md) with  a **DestinationDirs** value of 13.

> [!NOTE]
> See **SoftwareType** for information about constraints on **SoftwareBinary** entries and values.

**SoftwareArguments**=*{argument1[, argument2[, … argumentN]]}*  
Specifies extension-specific arguments to append to the command line.  You can specify command line arguments that the system simply passes through into the generated command line.  You can also specify special strings called *runtime context variables*.  When you specify a runtime context variable, the system converts it into a device-specific value before appending it to the generated command line.  You can mix and match literal string arguments with runtime context variables.  Supported runtime context variables are:

`<<DeviceInstanceID>>`

The system replaces the string above with the device instance ID of the software component.

For example:

```inf
    [DDInstall.Software]
    AddSoftware=ContosoControlPanel,,Contoso_ControlPanel_Software

    [Contoso_ControlPanel_Software]
    SoftwareType=1
    SoftwareBinary=ContosoControlPanel.exe
    SoftwareArguments=<<DeviceInstanceID>>
    SoftwareVersion=1.0.0.0
```

The above example results in a command line like this:

`<DriverStorePath>\ContosoControlPanel.exe PCI\VEN_0000&DEV_0001&SUBSYS_00000000&REV_00\0123`

If SoftwareArguments contains multiple arguments:

```inf
    SoftwareArguments=arg1,<<DeviceInstanceID>>,arg2
```

The above results in:

`<DriverStorePath>\ContosoControlPanel.exe arg1 PCI\VEN_0000&DEV_0001&SUBSYS_00000000&REV_00\0123 arg2`

> [!NOTE]
> See **SoftwareType** for information about constraints on **SoftwareArguments** entries and values.

**SoftwareVersion**=*{w.x.y.z}*  
Specifies the software version.  Each value should not exceed 65535.  When the system encounters a duplicate **SoftwareName**, it checks the **SoftwareVersion** against the previous **SoftwareVersion**.  If it is greater, Windows runs the software.

> [!NOTE]
> See **SoftwareType** for information about constraints on **SoftwareVersion** entries and values.

**SoftwareID**=*{x.y.z}*  
Specifies a Microsoft Store identifier and identifier type.  Currently, only Package Family Name (PFN) is supported.  Use a PFN to reference a Universal Windows Platform (UWP) app using the form `pfn://<x.y.z>`.

> [!NOTE]
> See **SoftwareType** for information about constraints on **SoftwareID** entries and values.

## See Also

[Using a Component INF File](using-a-component-inf-file.md)

[INF DDInstall.Software Section](inf-ddinstall-software-section.md)

[INF AddComponent Directive](inf-addcomponent-directive.md)

[Pairing a driver with a Universal Windows Platform (UWP) app](pairing-app-and-driver-versions.md)

[Hardware Support App (HSA): Steps for Driver Developers](../devapps/hardware-support-app--hsa--steps-for-driver-developers.md)
