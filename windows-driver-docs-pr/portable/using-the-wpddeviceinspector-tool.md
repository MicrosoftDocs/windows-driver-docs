---
Description: Using the WpdDeviceInspector Tool
title: Using the WpdDeviceInspector Tool
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Using the WpdDeviceInspector Tool


The WpdDeviceInspector tool is a console application that generates a comprehensive HTML report. This report describes three categories of device and driver information, which are listed in the following table.

| Category                 | Description                                                                                              |
|--------------------------|----------------------------------------------------------------------------------------------------------|
| Installation Information | Specifies device and driver data that is used by the Windows installer.                                  |
| Device Capabilities      | Identifies commands, objects, content types, formats, and events that are supported by the device.       |
| Device Content           | Lists object identifier strings and the corresponding Persistent Unique Object Identifier (PUID) values. |

 

## <span id="Viewing_the_Command-Line_Options_for_WpdDeviceInspector"></span><span id="viewing_the_command-line_options_for_wpddeviceinspector"></span><span id="VIEWING_THE_COMMAND-LINE_OPTIONS_FOR_WPDDEVICEINSPECTOR"></span>Viewing the Command-Line Options for WpdDeviceInspector


To view the command-line options for *WpdDeviceInspector.exe*, type the following command at the command prompt:

```cmd
WpdDeviceInspector.exe /?
```

## <span id="Generating_a_Report_for_a_Specific_Device"></span><span id="generating_a_report_for_a_specific_device"></span><span id="GENERATING_A_REPORT_FOR_A_SPECIFIC_DEVICE"></span>Generating a Report for a Specific Device


You can generate a report for a particular device by running *WpdDeviceInspector.exe* without any parameters, and entering the index for the selected device.

```cpp
> WpdDeviceInspector.exe


1 Windows Portable Device(s) found on the system

[0]     Dev Interface: \\?\root#wpd#0001#{6ac27878-a6fa-4155-ba85-f98f491d4f33}
        Friendly Name: Hello World!
        Manufacturer:  Windows Portable Devices Group
        Description:   Hello World!

Enter the index of the device you want to Inspect.
>
```

Alternatively, if you know the device identifier, you can tell*WpdDeviceInspector.exe* to always generate a report for that device by typing the device identifier directly after the /Device switch at the command prompt:

```cmd
WpdDeviceInspector.exe /Device:\\?\root#wpd#0000#{6ac27878-a6fa-4155-ba85-f98f491d4f33}
```

The device identifier is listed under the *Dev Interface*entry for each device when you launch *WpdDeviceInspector.exe* without any parameters.

## <span id="Operating_WpdDeviceInspector_in_Snapshot_Mode"></span><span id="operating_wpddeviceinspector_in_snapshot_mode"></span><span id="OPERATING_WPDDEVICEINSPECTOR_IN_SNAPSHOT_MODE"></span>Operating WpdDeviceInspector in Snapshot Mode


You can operate *WpdDeviceInspector.exe* in snapshot mode and capture a directory structure that mirrors the object hierarchy on a given device. When the tool operates in snapshot mode, it creates .opt files in each folder in which it stores the given object's properties and attributes.

In snapshot mode, the binary resources are saved to files that are named for the resource key (GUID.pid). These files can be renamed and opened as appropriate. For example, the default resource for a JPEG image would be saved to {E81E79BE-34F0-41BF-B53F-F1A06AE87842}.0, but could easily be renamed to device\_image.jpg so that the image could be viewed in a graphics tool.

To operate in snapshot mode, use the /Snapshot switch at the command prompt:

```cmd
WpdDeviceInspector.exe /Snapshot
```

## <span id="Operating_WpdDeviceInspector_in_WPD_Automation_Mode"></span><span id="operating_wpddeviceinspector_in_wpd_automation_mode"></span><span id="OPERATING_WPDDEVICEINSPECTOR_IN_WPD_AUTOMATION_MODE"></span>Operating WpdDeviceInspector in WPD Automation Mode


You can operate *WpdDeviceInspector.exe* to dump the JScript properties and methods of a given device. This is useful when you are using WPD Automation to access a WPD device from a Device Stage™ HostedSiteWithDevice task. For more information about authoring Device Stage™ tasks for WPD devices, see the Windows Device Experience Portal. This feature is only available in Windows 7.

To operate in WPD Automation mode, use the /Automation switch at the command prompt:

```cpp
WpdDeviceInspector.exe /Automation
```

 

 




