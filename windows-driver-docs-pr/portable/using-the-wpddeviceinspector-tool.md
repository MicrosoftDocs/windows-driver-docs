---
Description: Using the WpdDeviceInspector Tool
MS-HAID: 'wpddk.using\_the\_wpddeviceinspector\_tool'
MSHAttr: 'PreferredLib:/library/windows/hardware'
title: Using the WpdDeviceInspector Tool
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

```
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

```
WpdDeviceInspector.exe /Automation
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[wpd_dk\wpddk]:%20Using%20the%20WpdDeviceInspector%20Tool%20%20RELEASE:%20%281/5/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")



