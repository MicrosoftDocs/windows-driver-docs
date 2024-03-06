---
title: Axis Selection
description: Axis selection
keywords:
- joysticks WDK HID , axes
- virtual joystick drivers WDK HID , axes
- VJoyD WDK HID , axes
- axes WDK joysticks
ms.date: 01/11/2024
---

# Axis selection

This section contains information about how DirectInput maps axes for use by DirectInput and Windows multimedia applications.

## Windows 2000, legacy interfaces

When using the DirectX 7.0 API on Windows 2000, axis assignments are made in the order in which the axes are exposed by the device driver, shown in the following table:

| Usage Page                | Usage                            | DirectInput Axis |
|---------------------------|----------------------------------|------------------|
| HID_USAGE_PAGE_GENERIC    | HID_USAGE_GENERIC_X              | GUID_XAxis       |
| HID_USAGE_PAGE_GENERIC    | HID_USAGE_GENERIC_Y              | GUID_YAxis       |
| HID_USAGE_PAGE_GENERIC    | HID_USAGE_GENERIC_Z              | GUID_ZAxis       |
| HID_USAGE_PAGE_GENERIC    | HID_USAGE_GENERIC_WHEEL          | GUID_ZAxis       |
| HID_USAGE_PAGE_GENERIC    | HID_USAGE_GENERIC_RX             | GUID_RxAxis      |
| HID_USAGE_PAGE_GENERIC    | HID_USAGE_GENERIC_RY             | GUID_RyAxis      |
| HID_USAGE_PAGE_GENERIC    | HID_USAGE_GENERIC_RZ             | GUID_RzAxis      |
| HID_USAGE_PAGE_GENERIC    | HID_USAGE_GENERIC_HATSWITCH      | GUID_POV         |
| HID_USAGE_PAGE_GENERIC    | HID_USAGE_GENERIC_SLIDER         | GUID_Slider      |
| HID_USAGE_PAGE_GENERIC    | HID_USAGE_GENERIC_DIAL           | GUID_Slider      |
| HID_USAGE_PAGE_SIMULATION | HID_USAGE_SIMULATION_STEERING    | GUID_XAxis       |
| HID_USAGE_PAGE_SIMULATION | HID_USAGE_SIMULATION_ACCELERATOR | GUID_YAxis       |
| HID_USAGE_PAGE_SIMULATION | HID_USAGE_SIMULATION_BRAKE       | GUID_RzAxis      |
| HID_USAGE_PAGE_SIMULATION | HID_USAGE_SIMULATION_RUDDER      | GUID_RzAxis      |
| HID_USAGE_PAGE_SIMULATION | HID_USAGE_SIMULATION_THROTTLE    | GUID_Slider      |
| HID_USAGE_PAGE_GAME       | HID_USAGE_ SIMULATION_POV        | GUID_POV         |

These GUIDs are used by SetDataFormat to match the requested data format to the device objects. For applications that are compiled with DIRECTINPUT_VERSION less than 0x0600, if the data format specifies a GUID_ZAxis before a GUID_Slider (as the default joystick data format does) and a Slider is found on the device before a Z-axis, then the Slider will be matched as a Z-axis. This is intended to give better compatibility with HID.

## Windows 9x platforms

Through the DirectX 7.0 interfaces on Windows 95/98/Me, the mapping of a WinMM axis to a DirectInput axis is one-dimensional:

| WinMM Axis | DirectInput Assignment |
|------------|------------------------|
| X          | GUID_XAxis             |
| Y          | GUID_YAxis             |
| Z          | GUID_ZAxis             |
| R          | GUID_RzAxis            |
| U          | GUID_Slider            |
| V          | GUID_Slider            |

WinMM axes are mapped differently through DirectX 8.0 interfaces, as described below.

> [!NOTE]
> Although JoyHID.VxD does not yet map the vehicle control usages for steering, accelerate and brake, it does check for a steering usage and if one is found it treats the device as a WinMM car controller. Also, the DirectX 8.0 version of JoyHID.VxD copies any IHV supplied WinMM controller type flags (JOY_HWS_ISYOKE, JOY_HWS_ISGAMEPAD, JOY_HWS_ISCARCTRL or JOY_HWS_ISHEADTRACKER) and button counts, so these types can be set by the IHV in the OEMData registry value.

The mappings made by the DirectX 8.0 interfaces are different from those made by the legacy interfaces. The following table describes mappings in the DirectX 8.0 interfaces.

For data retrieved through WinMM, the default mapping is:

| WinMM Axis | DirectInput Assignment |
|------------|------------------------|
| X          | GUID_XAxis             |
| Y          | GUID_YAxis             |
| Z          | GUID_Slider            |
| R          | GUID_RzAxis            |
| U          | GUID_Slider            |
| V          | GUID_Slider            |

Because the third axis on a gaming device is rarely a Z-axis, these mappings help provide better compatibility with Windows 2000, Windows XP and Windows 95/98/Me HID.
