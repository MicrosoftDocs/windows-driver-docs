---
title: Button reporting
author: windows-driver-content
description: The in-box general-purpose I/O (GPIO) button driver reports to Windows, based on the interrupts that are received on the defined GPIO resources of the button array.
ms.assetid: 7D96E1CB-3406-4D61-9D5C-65BC6BFD1FFA
---

# Button reporting


The in-box general-purpose I/O (GPIO) button driver reports to Windows, based on the interrupts that are received on the defined GPIO resources of the button array.

The in-box GPIO button driver reports the button presses and combinations listed in *Table 1 GPIO Button Reporting*.

**Table 1 GPIO Button Reporting**

| Button        | Requires \_CRS Wakeable | Requires On-SOC GPIO | Edge Reporting (assuming ActiveLow) |
|---------------|-------------------------|----------------------|-------------------------------------|
| Windows       | Yes                     | Yes                  | Both                                |
| Volume Up     | Yes                     | Yes                  | Both                                |
| Volume Down   | Yes                     | Yes                  | Both                                |
| Rotation Lock | No                      | Yes                  | Both                                |
| Power         | Yes                     | Yes                  | Both                                |

 

All non-GPIO based implementations must follow the same reporting scheme.

The order of definition is Power, Windows, Volume Up, Volume Down, and Rotation Lock. For examples of how to create HID descriptors for these, see [HID button report descriptors](hid-button-report-descriptors.md).

**Note**  
Previous requirements described the use of **Win + O** for Rotation Lock. Although this combination is still functional, it is not impervious to keyboard layout changes, whereas **Win + F14** is layout-agnostic.

 

**Table 2 Report Triggers for non-GPIO Buttons**

| Individual button reporting | Source              | Usage requirements      | Report trigger         | Repeated |
|-----------------------------|---------------------|-------------------------|------------------------|----------|
| Power                       | System Control      | 0x84 (Power)            | Physical Button – Up   | No       |
| Windows                     | Keyboard            | 0xE3 (Win)              | Physical Button – Up   | No       |
| Volume Up                   | Consumer Collection | 0xE9 (Volume Up)        | Physical Button – Down | Yes      |
| Volume Down                 | Consumer Collection | 0xEA (Volume Down)      | Physical Button – Down | Yes      |
| Rotation Lock               | Keyboard            | 0xE3 = 0x69 (Win + F14) | Physical Button – Down | No       |

 

The following keyboard combinations must be reported based on their completion, and should not be repeated if the combination is held.

**Table 3 Report Triggers for non-GPIO Button Combinations**

<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Button combination reporting</th>
<th align="left">Usage requirements</th>
<th align="left">Report trigger</th>
<th align="left">Repeated</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left">Windows + Power</td>
<td align="left"><p>0xE0 + 0xE2 + 0x4C</p>
<p>(<strong>Ctrl + Alt + Del</strong>)</p></td>
<td align="left">Physical Power Button – Down</td>
<td align="left">No</td>
</tr>
<tr class="even">
<td align="left">Windows + Volume Up</td>
<td align="left"><p>0xE3 + 0xE0 + 0x69</p>
<p>(<strong>Win + Ctrl + F14</strong>)</p></td>
<td align="left">Physical Volume Button - Down</td>
<td align="left">No</td>
</tr>
<tr class="odd">
<td align="left">Windows + Volume Down</td>
<td align="left"><p>0xE3 + 0x6A</p>
<p>(<strong>Win + F15</strong>)</p></td>
<td align="left">Physical Volume Button - Down</td>
<td align="left">No</td>
</tr>
</tbody>
</table>

 

**Note**  
-   For full guidance and implementation for the Power button, see [Power Button Behaviors and implementation](http://connect.microsoft.com/site1304/Downloads/DownloadDetails.aspx?DownloadID=47452).
-   For Connected Standby guidance for buttons, see [Connected Standby Wake Sources](http://connect.microsoft.com/site1304/Downloads/DownloadDetails.aspx?DownloadID=49891).
-   For additional guidance on ACPI implementation, see [ACPI Design Guide](http://connect.microsoft.com/site1304/Downloads/DownloadDetails.aspx?DownloadID=48755).

 

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[gpiobtn\gpiobtn]:%20Button%20reporting%20%20RELEASE:%20%289/25/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


