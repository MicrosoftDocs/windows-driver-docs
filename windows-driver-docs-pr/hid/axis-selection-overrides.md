---
title: Axis Selection Overrides
description: Axis Selection Overrides
ms.assetid: 151c3d19-2f80-4d71-a004-10c16c691fb9
keywords: ["joysticks WDK HID , axes", "virtual joystick drivers WDK HID , axes", "VJoyD WDK HID , axes", "axes WDK joysticks", "overriding axis selections WDK joysticks", "usage pages WDK HID"]
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# Axis Selection Overrides





The DirectX 8.0 release introduces a new mechanism to provide hardware vendors with limited ability to modify how DirectInput assigns axes for HID-compliant devices. The initial axis selection is made through an association between a HID usage page/usage pair on the device with an axis instance. The axis instance is described in an optional registry subkey under the **Axes** subkey for the device type key. (Note that the **Axes** subkey is also an optional key under the device type-key.) Within the **Axes** subkey, the Attributes value stores a DIOBJECTATTRIBUTES structure. Before DirectX 8.0, the **wUsagePage** and **wUsage** fields in the DIOBJECTATTRIBUTES structure assigned a HID usage page and usage to an object on a non-HID device. These members were ignored for HID-compliant devices.

With the release of DirectX 8.0, these members became relevant to HID-compliant devices as well. They describe the HID usage page and usage that DirectInput should reference to find a match for a specific DirectInput axis in the joystick data formats. Hardware vendors can take advantage of these fields to impose greater consistency in how DirectInput maps axes on different Windows operating systems. However, these are not a preferred mechanism for remapping axes.

**Note**   Axis mapping is static, so the behavior is undefined if these values are changed while the device is in use. If the suggested match for an axis cannot be made, processing continues as though no mapping had been suggested.

 

For example, imagine a joystick device designed for use on a platform with a complete implementation of the HID\_USAGE\_PAGE\_GAME controls. Such a device might describe its X and Y axes in HID as:

<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<thead>
<tr class="header">
<th>Axis</th>
<th>Usage Page</th>
<th>Usage</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>X</p></td>
<td><p>5</p></td>
<td><p>24</p></td>
<td><p>Game page, move left/right</p></td>
</tr>
<tr class="even">
<td><p>Y</p></td>
<td><p>5</p></td>
<td><p>25</p></td>
<td><p>Game page, move forward/backward</p></td>
</tr>
</tbody>
</table>

 

Because these scenarios are not directly recognized by DirectInput (or JoyHID) they are not very useful to games. To get them recognized as the X and Y axes by DirectInput, the following registry entries could be added:

```cpp
[DIRECT_INPUT_TYPES\ VID_vvvv&PID_pppp)\Axes\0]
     Binary Attributes = 00 00 00 00 05 00 24 00

[DIRECT_INPUT_TYPES\ VID_vvvv&PID_pppp)\Axes\1]
     Binary Attributes = 00 00 00 00 05 00 25 00

Where "DIRECT_INPUT_TYPES" is a token for the following root key:
HKLM\SYSTEM\CurrentControlSet\Control\MediaProperties\PrivateProperties\Joystick\OEM
```

This mechanism has been implemented in the DirectInput 7.0 and below interfaces, the DirectInput 8.0 interfaces, as well as JoyHID.Vxd, the VJoyD minidriver used for WinMM support.

On Windows 95/98/Me, there are three possible data paths for a USB game controller:

-   The IHV can provide a VJoyD minidriver VxD that reports the data in the same way any other VJoyD minidriver does. In this case, axis selection is completely under the control of the IHV.

-   DirectInput can use the HID implementation that is provided with the operating system to communicate with the device. In this case, axis selection is made according to the device firmware or the registry flags (as described previously).

-   The system default HID-to-VJoyD driver (JoyHID.VxD) can be used.

DirectInput uses JoyHID.VxD (via VJoyD.VxD) to read data for applications that specify a DIRECTINPUT\_VERSION of less than 0x0700, or if the JOYTYPE\_NOHIDDIRECT flag is specified for the device. If the DIRECT\_INPUTVERSION is greater than or equal to 0x0700, DirectInput uses HID to interact with the device.

When the JoyHID/VJoyD path is taken, the following tables match WinMM axes to HID usage page/usage pairs:

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th>WinMM Axis</th>
<th>Usage Page</th>
<th>Usage</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>X</p></td>
<td><p>HID_USAGE_PAGE_GENERIC</p></td>
<td><p>HID_USAGE_GENERIC_X</p></td>
</tr>
<tr class="even">
<td></td>
<td><p>HID_USAGE_PAGE_GENERIC</p></td>
<td><p>HID_USAGE_GENERIC_RY</p></td>
</tr>
<tr class="odd">
<td><p>Y</p></td>
<td><p>HID_USAGE_PAGE_GENERIC</p></td>
<td><p>HID_USAGE_GENERIC_Y</p></td>
</tr>
<tr class="even">
<td></td>
<td><p>HID_USAGE_PAGE_GENERIC</p></td>
<td><p>HID_USAGE_GENERIC_RX</p></td>
</tr>
<tr class="odd">
<td><p>Z</p></td>
<td><p>HID_USAGE_PAGE_GENERIC</p></td>
<td><p>HID_USAGE_GENERIC_Z</p></td>
</tr>
<tr class="even">
<td></td>
<td><p>HID_USAGE_PAGE_SIMULATION</p></td>
<td><p>HID_USAGE_SIMULATION_THROTTLE</p></td>
</tr>
<tr class="odd">
<td></td>
<td><p>HID_USAGE_PAGE_GENERIC</p></td>
<td><p>HID_USAGE_GENERIC_SLIDER</p></td>
</tr>
<tr class="even">
<td></td>
<td><p>HID_USAGE_PAGE_GENERIC</p></td>
<td><p>HID_USAGE_GENERIC_DIAL</p></td>
</tr>
<tr class="odd">
<td><p>R</p></td>
<td><p>HID_USAGE_PAGE_SIMULATION</p></td>
<td><p>HID_USAGE_SIMULATION_RUDDER</p></td>
</tr>
<tr class="even">
<td></td>
<td><p>HID_USAGE_PAGE_GENERIC</p></td>
<td><p>HID_USAGE_GENERIC_RZ</p></td>
</tr>
<tr class="odd">
<td><p>U</p></td>
<td><p>HID_USAGE_PAGE_SIMULATION</p></td>
<td><p>HID_USAGE_SIMULATION_THROTTLE</p></td>
</tr>
<tr class="even">
<td></td>
<td><p>HID_USAGE_PAGE_GENERIC</p></td>
<td><p>HID_USAGE_GENERIC_SLIDER</p></td>
</tr>
<tr class="odd">
<td></td>
<td><p>HID_USAGE_PAGE_GENERIC</p></td>
<td><p>HID_USAGE_GENERIC_DIAL</p></td>
</tr>
<tr class="even">
<td></td>
<td><p>HID_USAGE_PAGE_GENERIC</p></td>
<td><p>HID_USAGE_GENERIC_RY</p></td>
</tr>
<tr class="odd">
<td><p>V</p></td>
<td><p>HID_USAGE_PAGE_GENERIC</p></td>
<td><p>HID_USAGE_GENERIC_RX</p></td>
</tr>
</tbody>
</table>

 

**Note**  Mappings for the R, U and V axes fall through to the next axis if a mapping is not found, whereas X, Y and Z mappings are completely independent of each other. This is because VJoyD.VxD only supports contiguous sets of axes (for example, X, Y, Z, R is supported, but X, Y, Z, U is not). The only exceptions to this rule are made for joysticks that use the precise combinations of X, Y and R, or X, Y, Z, R and V. This method of mapping helps to avoid the possibility that JoyHID.VxD makes axis assignments that VJoyD.VxD cannot tolerate.

 

 

 




