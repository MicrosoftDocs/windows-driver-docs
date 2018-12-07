---
title: Special Case Mappings
description: Special Case Mappings
ms.assetid: 1691e0e5-7b05-40e1-8747-40926f2eba9c
keywords: ["joysticks WDK HID , axes", "virtual joystick drivers WDK HID , axes", "VJoyD WDK HID , axes", "axes WDK joysticks", "special case mappings WDK joysticks", "case mappings WDK joysticks", "Z-axis case mapping WDK joysticks", "car controller case mapping WDK joysticks", "mapping axes"]
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# Special Case Mappings





Because of the complexity and variety of input devices available today, no single set of mappings can be used for all types of devices. DirectInput supports two special cases that are described in this section.

### Special Case Mapping for Z-Axes

In the rare cases where a Z-Axis described in HID is the desired WinMM mapping, there are two available overrides. If the device is a six-degree-of-freedom device, setting a type and subtype override (described in the references for **DIJOYTYPEINFO**) to DI8DEVTYPE\_1STPERSON and DI8DEVTYPE1STPERSON\_SIXDOF respectively, invokes the following alternative mapping:

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
<td><p>GUID_RyAxis</p></td>
</tr>
<tr class="even">
<td><p>V</p></td>
<td><p>GUID_RxAxis</p></td>
</tr>
</tbody>
</table>



If the device is not a six-degree-of-freedom device, but still requires a Z-axis to be portrayed through DirectInput, the type override should be set to include JOYTYPE\_INFOZISZ. This type override causes DirectInput to revert to the DirectX 7.0 mapping.

The default mapping for devices reporting through HID has not changed except that GUID\_Slider axes are no longer substituted for GUID\_ZAxis matches by the SetDataFormat method. Because HID axes are by nature more fully described than WinMM axes, the defaults should work in most cases. In rare cases, a slider axis (often used as a throttle) has been described as HID\_USAGE\_PAGE\_GENERIC, HID\_USAGE\_Z because the axis would be used in the same way as a WinMM Z-axis. To make sure such devices can be used consistently the device override flag JOYTYPE\_INFOZISSLIDER can be used.

### Special-case Mappings for Car Controllers

Another set of special-case mappings are those needed for car controllers that declare more than two axes. Unfortunately, there is little consistency within the industry in this area. There presently exist three common ways to represent separate accelerator and brake pedals. DirectInput attempts to detect which method a car controller is using with logic similar to that shown in the following pseudocode:

```cpp
    if( has_r and has_Z )
        use mappings:
        X => GUID_XAxis
        Z => GUID_YAxis
        R => GUID_RzAxis
    else if( has_r )
        use mappings:
        X => GUID_XAxis
        Y => GUID_YAxis
        R => GUID_RzAxis
    else if( has_z )
        use mappings:
        X => GUID_XAxis
        Y => GUID_RzAxis
        Z => GUID_YAxis
    else
        use default mappings.

   // If the device declares any other axes, they are mapped to sliders.
```

The preceding logic results in all three known types of pedal mappings being reported to applications in the same way. If the default mappings fail, you can set override flags to select which type of mapping should be used. The override flags JOYTYPE\_INFOYYPEDALS, JOYTYPE\_INFOZYPEDALS, JOYTYPE\_INFOYRPEDALS and JOYTYPE\_INFOZRPEDALS are described elsewhere in this documentation.

As with WinMM, car controllers require special-case mapping when being used through the HID data-path. Mappings are made in the same way in this case as in the WinMM case, but with extra variations due to the possibility of the correct simulation page usages being reported in the device firmware.

Devices that report generic axes receive the same mappings and can use the same override mechanisms in both the HID and WinMM data paths. However, these overrides affect only the generic axes; they do not change the mapping table that is used for all axes on the device.

### Axis Overrides under Windows 95/98/Me

The following interfaces are affected by axis overrides:

-   WinMM JoyGetPos()
-   WinMM JoyGetPosEx()
-   **IDirectInput2**
-   **IDirectInput7**
-   **IDirectInput8**

### To perform an axis override:

1.  Plug in the device whose axis is to be overridden. Run joy.cpl or any other DirectInput application to initialize the registry keys for this device. Unplug the device.

2.  Open the registry and find HKEY\_LOCAL\_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\MediaProperties\\PrivateProperties\\Joystick\\OEM

3.  Locate the key for the device whose axis is to be overridden. The key should be located under this key, specified by its VID&PID combination.

4.  Create the following subkeys:

    -   Axes
    -   Under the "Axes" key, specify one key for each axis that you want to override (Axis key). The key is specified by a one-digit number from zero to 7 that describes GUID and axis information:

        <table>
        <colgroup>
        <col width="33%" />
        <col width="33%" />
        <col width="33%" />
        </colgroup>
        <thead>
        <tr class="header">
        <th>Key Name</th>
        <th>DirectX GUID</th>
        <th>WinMM Axis</th>
        </tr>
        </thead>
        <tbody>
        <tr class="odd">
        <td><p>0</p></td>
        <td><p>GUID_XAxis</p></td>
        <td><p>X</p></td>
        </tr>
        <tr class="even">
        <td><p>1</p></td>
        <td><p>GUID_YAxis</p></td>
        <td><p>Y</p></td>
        </tr>
        <tr class="odd">
        <td><p>2</p></td>
        <td><p>GUID_ZAxis</p></td>
        <td><p>Z</p></td>
        </tr>
        <tr class="even">
        <td><p>3</p></td>
        <td><p>GUID_RxAxis</p></td>
        <td><p>-</p></td>
        </tr>
        <tr class="odd">
        <td><p>4</p></td>
        <td><p>GUID_RyAxis</p></td>
        <td><p>-</p></td>
        </tr>
        <tr class="even">
        <td><p>5</p></td>
        <td><p>GUID_RzAxis</p></td>
        <td><p>R</p></td>
        </tr>
        <tr class="odd">
        <td><p>6</p></td>
        <td><p>GUID_Slider</p></td>
        <td><p>U</p></td>
        </tr>
        <tr class="even">
        <td><p>7</p></td>
        <td><p>GUID_Slider</p></td>
        <td><p>V</p></td>
        </tr>
        </tbody>
        </table>




-   Under each Axis key specify the Axis that you want to override. Create a binary value named **Attributes** and set it to: 00 00 00 00 HUP 00 HU 00. HUP is a two-digit hexadecimal number specifying the HID usage page of the device object (axis) that you want to override. HU is a two-digit hexadecimal number specifying the HID usage of the device object. Use DIQuick to determine these values, or see the HID specification.
-   Plug the device back in and use any program to check whether the overrides work.


### Meaning of the registry keys

First of all you need to differentiate between the axis mapping of the DirectX interfaces and the WinMM interfaces.

The DirectX interfaces interpret the Axiskeys to match GUIDs that are used to identify objects. The object GUIDs are used to read data from the device and specified in **IDirectInputDevice8::SetDataFormat()**. When data for an object is read by a program and this object is overridden, then DirectInput returns the data from the overriding object.

As you can see, there is no differentiation between slider 0 and slider 1 in the DirectInput interfaces. This means that, when overriding axis 6 or 7, you always override the first available slider. If slider 0 is not yet defined as an axis and you map an axis to 7, slider 0 is overridden.

In contrast, the WinMM interfaces do differentiate between the U and V axes, so if axis 7 is overridden, the V axis receives the data from the overriding object; if axis 6 is overridden, the data is converted to be sent by the U axis.

### Rules to keep in mind

To guarantee the equal behavior of the interfaces, restrictive rules must be followed. These rules are provided by the behavior of WinMM interfaces.

Mappings that do not conform to these rules may result in failure of the WinMM interface to report any data for this device.

These rules do not apply to differences in slider mappings; such differences are acceptable.

Any mapping that does not fall within the following rules is unsupported.

-   No Holes.

    The axis mapping must be continuous after applying the overrides. Only one axis can exist in an unmapped state, that is, "2"=GUID\_ZAxis=Z. You cannot skip axis entries. For example, X, Y, Z, R, U, V is a valid sequence, but X, Z, R, U, V is not because there is a "hole" between X and Z.

-   All Axes exist.

    All axes that are used to perform override operations (specified by the Attributes value) must exist on the device.

-   Do not move axes "upwards" without mapping to them.

    You cannot map an axis A to an axis B without mapping axis C to axis A if axis A would have a lower Key Name in the table above.

    Moving an axis upward without mapping to it results in a hole.

### If the mapping is not reflected by the interfaces

-   Always unplug the device before you change the mapping. Plug the device back in after you edit the mapping in order to reinitialize DirectInput.

-   DirectInput could deny special overrides. Check the key: HKEY\_LOCAL\_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\MediaProperties\\PrivateProperties\\DirectInput\\VID&PID , where VID&PID is the VID-PID-combination for the device. If there is a value Flags2 set, then DirectInput internally maps axes to axes and you cannot override these mappings. For example, you may not be able to move the mapping of a slider away from the Z-axis in the DInput7/2 and WinMM interfaces.

-   If the user installs and calibrates a joystick, the resulting calibration information is stored in the registry. If a driver is now installed that sets the axis overrides that differ from those previously stored in the registry, DirectInput applies the overrides stored in the Registry. Because the calibration information in the registry does not reflect the axis mapping changes, the data might be reported incorrectly or might not be reported at all on the overridden axes.

    There are two ways to prevent this:

    -   The user can recalibrate the device.
    -   The driver vendor's installation can delete the calibration information in the registry.

If the device does not use joyhid.vxd as its driver, the wUsage and wUsagePage values are only used to describe what usage and usage page the object should be reported as, rather than being any form of override. The device uses joyhid.vxd only if the registry key HKEY\_LOCAL\_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\MediaProperties\\PrivateProperties\\Joystick\\OEM\\VID&PID\\OEMCallout equals joyhid.vxd.








