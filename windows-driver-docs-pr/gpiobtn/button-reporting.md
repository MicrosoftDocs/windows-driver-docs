---
title: Button Reporting
description: The in-box general-purpose I/O (GPIO) button driver reports to Windows, based on the interrupts that are received on the defined GPIO resources of the button array.
ms.date: 02/15/2023
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

The order of definition is Power, Windows, Volume Up, Volume Down, and Rotation Lock. For examples of how to create HID descriptors for these functions, see [HID button report descriptors](../hid/acpi-button-device.md).

**Note**  
Previous requirements described the use of **Win + O** for Rotation Lock. Although this combination is still functional, it isn't impervious to keyboard layout changes, whereas **Win + F14** is layout-agnostic.

 

**Table 2 Report Triggers for non-GPIO Buttons**

| Individual button reporting | Source              | Usage requirements      | Report trigger         | Repeated |
|-----------------------------|---------------------|-------------------------|------------------------|----------|
| Power                       | System Control      | 0x81 (Power)            | Physical Button – Up   | No       |
| Windows                     | Keyboard            | 0xE3 (Win)              | Physical Button – Up   | No       |
| Volume Up                   | Consumer Collection | 0xE9 (Volume Up)        | Physical Button – Down | Yes      |
| Volume Down                 | Consumer Collection | 0xEA (Volume Down)      | Physical Button – Down | Yes      |
| Rotation Lock               | Keyboard            | 0xE3 + 0x69 (Win + F14) | Physical Button – Down | No       |

 

The following keyboard combinations must be reported based on their completion, and shouldn't be repeated if the combination is held.

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
-   For full guidance and implementation for the Power button, see [Power button and lid settings overview](/windows-hardware/customize/power-settings/power-button-and-lid-settings).
-   For Connected Standby guidance for buttons, see [Wake sources](/windows-hardware/design/device-experiences/modern-standby-wake-sources).
-   For more information on ACPI implementation, see [ACPI design guide](../acpi/index.md).

