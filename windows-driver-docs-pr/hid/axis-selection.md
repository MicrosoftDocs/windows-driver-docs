---
title: Axis Selection
author: windows-driver-content
description: Axis Selection
MS-HAID:
- 'di\_a7b86bc9-7508-4de4-9391-c8cc8ed063d0.xml'
- 'hid.axis\_selection'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 5ba78609-d5e7-44b1-86e8-5a677a19aadd
keywords: ["joysticks WDK HID , axes", "virtual joystick drivers WDK HID , axes", "VJoyD WDK HID , axes", "axes WDK joysticks"]
---

# Axis Selection


## <a href="" id="ddk-axis-selection-di"></a>


This section contains information about how DirectInput maps axes for use by DirectInput and Windows multimedia applications.

This section includes:

[Axis Selection Overrides](axis-selection-overrides.md)

[Special Case Mappings](special-case-mappings.md)

### Windows 2000, Legacy Interfaces

When using the DirectX 7.0 API on Windows 2000, axis assignments are made in the order in which the axes are exposed by the device driver, shown in the following table:

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th>Usage Page</th>
<th>Usage</th>
<th>DirectInput Axis</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>HID_USAGE_PAGE_GENERIC</p></td>
<td><p>HID_USAGE_GENERIC_X</p></td>
<td><p>GUID_XAxis</p></td>
</tr>
<tr class="even">
<td><p>HID_USAGE_PAGE_GENERIC</p></td>
<td><p>HID_USAGE_GENERIC_Y</p></td>
<td><p>GUID_YAxis</p></td>
</tr>
<tr class="odd">
<td><p>HID_USAGE_PAGE_GENERIC</p></td>
<td><p>HID_USAGE_GENERIC_Z</p></td>
<td><p>GUID_ZAxis</p></td>
</tr>
<tr class="even">
<td><p>HID_USAGE_PAGE_GENERIC</p></td>
<td><p>HID_USAGE_GENERIC_WHEEL</p></td>
<td><p>GUID_ZAxis</p></td>
</tr>
<tr class="odd">
<td><p>HID_USAGE_PAGE_GENERIC</p></td>
<td><p>HID_USAGE_GENERIC_RX</p></td>
<td><p>GUID_RxAxis</p></td>
</tr>
<tr class="even">
<td><p>HID_USAGE_PAGE_GENERIC</p></td>
<td><p>HID_USAGE_GENERIC_RY</p></td>
<td><p>GUID_RyAxis</p></td>
</tr>
<tr class="odd">
<td><p>HID_USAGE_PAGE_GENERIC</p></td>
<td><p>HID_USAGE_GENERIC_RZ</p></td>
<td><p>GUID_RzAxis</p></td>
</tr>
<tr class="even">
<td><p>HID_USAGE_PAGE_GENERIC</p></td>
<td><p>HID_USAGE_GENERIC_HATSWITCH</p></td>
<td><p>GUID_POV</p></td>
</tr>
<tr class="odd">
<td><p>HID_USAGE_PAGE_GENERIC</p></td>
<td><p>HID_USAGE_GENERIC_SLIDER</p></td>
<td><p>GUID_Slider</p></td>
</tr>
<tr class="even">
<td><p>HID_USAGE_PAGE_GENERIC</p></td>
<td><p>HID_USAGE_GENERIC_DIAL</p></td>
<td><p>GUID_Slider</p></td>
</tr>
<tr class="odd">
<td><p>HID_USAGE_PAGE_SIMULATION</p></td>
<td><p>HID_USAGE_SIMULATION_STEERING</p></td>
<td><p>GUID_XAxis</p></td>
</tr>
<tr class="even">
<td><p>HID_USAGE_PAGE_SIMULATION</p></td>
<td><p>HID_USAGE_SIMULATION_ACCELERATOR</p></td>
<td><p>GUID_YAxis</p></td>
</tr>
<tr class="odd">
<td><p>HID_USAGE_PAGE_SIMULATION</p></td>
<td><p>HID_USAGE_SIMULATION_BRAKE</p></td>
<td><p>GUID_RzAxis</p></td>
</tr>
<tr class="even">
<td><p>HID_USAGE_PAGE_SIMULATION</p></td>
<td><p>HID_USAGE_SIMULATION_RUDDER</p></td>
<td><p>GUID_RzAxis</p></td>
</tr>
<tr class="odd">
<td><p>HID_USAGE_PAGE_SIMULATION</p></td>
<td><p>HID_USAGE_SIMULATION_THROTTLE</p></td>
<td><p>GUID_Slider</p></td>
</tr>
<tr class="even">
<td><p>HID_USAGE_PAGE_GAME</p></td>
<td><p>HID_USAGE_ SIMULATION_POV</p></td>
<td><p>GUID_POV</p></td>
</tr>
</tbody>
</table>

 

These GUIDs are used by SetDataFormat to match the requested data format to the device objects. For applications that are compiled with DIRECTINPUT\_VERSION &lt; 0x0600, if the data format specifies a GUID\_ZAxis before a GUID\_Slider (as the default joystick data format does) and a Slider is found on the device before a Z-axis, then the Slider will be matched as a Z-axis. This is intended to give better compatibility with HID.

### Windows 9x Platforms

Through the DirectX 7.0 interfaces on Windows 95/98/Me, the mapping of a WinMM axis to a DirectInput axis is one-dimensional:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>WinMM Axis</th>
<th>DirectInput Assignment</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>X</p></td>
<td><p>GUID_XAxis</p></td>
</tr>
<tr class="even">
<td><p>Y</p></td>
<td><p>GUID_YAxis</p></td>
</tr>
<tr class="odd">
<td><p>Z</p></td>
<td><p>GUID_ZAxis</p></td>
</tr>
<tr class="even">
<td><p>R</p></td>
<td><p>GUID_RzAxis</p></td>
</tr>
<tr class="odd">
<td><p>U</p></td>
<td><p>GUID_Slider</p></td>
</tr>
<tr class="even">
<td><p>V</p></td>
<td><p>GUID_Slider</p></td>
</tr>
</tbody>
</table>

 

WinMM axes are mapped differently through DirectX 8.0 interfaces, as described below.

**Note**   Although JoyHID.VxD does not yet map the vehicle control usages for steering, accelerate and brake, it does check for a steering usage and if one is found it treats the device as a WinMM car controller. Also, the DirectX 8.0 version of JoyHID.VxD copies any IHV supplied WinMM controller type flags (JOY\_HWS\_ISYOKE, JOY\_HWS\_ISGAMEPAD, JOY\_HWS\_ISCARCTRL or JOY\_HWS\_ISHEADTRACKER) and button counts, so these types can be set by the IHV in the OEMData registry value.

 

The mappings made by the DirectX 8.0 interfaces are different from those made by the legacy interfaces. The following table describes mappings in the DirectX 8.0 interfaces.

For data retrieved through WinMM, the default mapping is:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>WinMM Axis</th>
<th>DirectInput Assignment</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>X</p></td>
<td><p>GUID_XAxis</p></td>
</tr>
<tr class="even">
<td><p>Y</p></td>
<td><p>GUID_YAxis</p></td>
</tr>
<tr class="odd">
<td><p>Z</p></td>
<td><p>GUID_Slider</p></td>
</tr>
<tr class="even">
<td><p>R</p></td>
<td><p>GUID_RzAxis</p></td>
</tr>
<tr class="odd">
<td><p>U</p></td>
<td><p>GUID_Slider</p></td>
</tr>
<tr class="even">
<td><p>V</p></td>
<td><p>GUID_Slider</p></td>
</tr>
</tbody>
</table>

 

Because the third axis on a gaming device is rarely a Z-axis, these mappings help provide better compatibility with Windows 2000, Windows XP and Windows 95/98/Me HID.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bhid\hid%5D:%20Axis%20Selection%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


