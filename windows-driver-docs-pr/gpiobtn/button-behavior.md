---
title: Button behavior
description: This topic describes the expected behavior of hardware buttons.
ms.assetid: 057A4F21-3514-4CCA-BCE2-279E8228B5A9
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# Button behavior


This topic describes the expected behavior of hardware buttons.

## <span id="Required_and_optional__buttons_in_Windows_10"></span><span id="required_and_optional__buttons_in_windows_10"></span><span id="REQUIRED_AND_OPTIONAL__BUTTONS_IN_WINDOWS_10"></span>Required and optional buttons in Windows 10


<table>
<colgroup>
<col width="14%" />
<col width="14%" />
<col width="14%" />
<col width="14%" />
<col width="14%" />
<col width="14%" />
<col width="14%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left">Operating system/device</td>
<td align="left">Power</td>
<td align="left">Volume up/Volume down</td>
<td align="left">Start</td>
<td align="left">Back/Search</td>
<td align="left">Camera</td>
<td align="left">Rotation lock</td>
</tr>
<tr class="even">
<td align="left">Windows 10 Mobile</td>
<td align="left">Required</td>
<td align="left">Required</td>
<td align="left"><p>Required for phones that use a WVGA display</p>
<p>Optional for all other devices</p></td>
<td align="left"><p>Required for phones that use a WVGA display</p>
<p>Optional for all other devices</p></td>
<td align="left">Optional</td>
<td align="left">Not supported</td>
</tr>
<tr class="odd">
<td align="left">Windows 10 for desktop editions (Home, Pro, Enterprise, and Education)/Tablets</td>
<td align="left">Required</td>
<td align="left">Required</td>
<td align="left">Optional</td>
<td align="left">Not supported</td>
<td align="left">Not supported</td>
<td align="left">Optional</td>
</tr>
<tr class="even">
<td align="left">Windows 10 for desktop editions/Other devices</td>
<td align="left">Required</td>
<td align="left">Required for devices with detachable keyboards. Optional for all other devices.</td>
<td align="left">Optional</td>
<td align="left">Not supported</td>
<td align="left">Not supported</td>
<td align="left">Optional</td>
</tr>
</tbody>
</table>

 

For more information about button requirements:

-   For Windows 10 Mobile, see section 2.6 in the [Minimum Hardware Requirements](https://msdn.microsoft.com/library/windows/hardware/dn915086.aspx).
-   For Windows 10 for desktop editions, see section 3.6 in the [Minimum Hardware Requirements](https://msdn.microsoft.com/library/windows/hardware/dn915086.aspx).

## <span id="Button_behavior_in_Windows_10"></span><span id="button_behavior_in_windows_10"></span><span id="BUTTON_BEHAVIOR_IN_WINDOWS_10"></span>Button behavior in Windows 10


### <span id="Single_button_behavior_in_Windows_10"></span><span id="single_button_behavior_in_windows_10"></span><span id="SINGLE_BUTTON_BEHAVIOR_IN_WINDOWS_10"></span>Single button behavior in Windows 10

Button
Windows 10 for desktop editions
Windows 10 Mobile
Power
Press and release
Toggle On/Off
Toggle On/Off
Press and hold
Launch Shutdown Curtain
Launch Shutdown Curtain
Long press and hold
Hard shutdown
Hardware reset
Search
Press and release
Not supported
Launch Cortana (in enabled markets)/Search
Press and hold
Not supported
Launch Cortana or Search with Voice
Volume up
Press and release
Increment volume
Increment volume
Press and hold
Auto-repeat volume increment
Auto-repeat volume increment
Volume down
Press and release
Decrement volume
Decrement volume
Press and hold
Auto-repeat volume decrement
Auto-repeat volume decrement
Back
Press and release
Previous app page/close app
Previous app page/close app
Press and hold
Launch Task switcher
Launch switcher UI
Start
Toggle Start screen
Show Start screen
Rotation lock
Not supported
Not supported (there is a UI option)
Camera focus
Launch Camera application
Handled by Camera app (focus)
Camera shutter
Handled by Camera application
Launch Camera app / take picture
 

### <span id="Button_combination_behavior_in_Windows_10"></span><span id="button_combination_behavior_in_windows_10"></span><span id="BUTTON_COMBINATION_BEHAVIOR_IN_WINDOWS_10"></span>Button combination behavior in Windows 10

As noted, some button combinations in Windows 10 apply to the [Windows 10 button architecture](https://msdn.microsoft.com/library/windows/hardware/dn957423%28v=vs.85%29.aspx) or the Windows 8.1 button architecture. All other button combinations in Windows 10 apply to either button architecture. It is recommended to describe hardware buttons using the Windows 10 architecture.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left">Button combination</td>
<td align="left">Windows 10 for desktop editions</td>
<td align="left">Windows 10 Mobile</td>
</tr>
<tr class="even">
<td align="left">Start + Volume Up</td>
<td align="left">Toggle on-screen narrator</td>
<td align="left">Toggle on-screen narrator (provided that the corresponding ease-of-access setting is enabled)</td>
</tr>
<tr class="odd">
<td align="left">Start + Volume Down</td>
<td align="left">Take screenshot</td>
<td align="left">Not supported</td>
</tr>
<tr class="even">
<td align="left">Start + Power</td>
<td align="left">Ctrl+Alt+Del (only if using Windows 8.1 button architecture)</td>
<td align="left">Not supported</td>
</tr>
<tr class="odd">
<td align="left">Power + Volume Up</td>
<td align="left">Take screenshot (only if using Windows 10 button architecture)</td>
<td align="left">Take screenshot</td>
</tr>
<tr class="even">
<td align="left">Power + Volume Down</td>
<td align="left">Ctrl+Alt+Del (only if using Windows 10 button architecture)</td>
<td align="left"><p>Launch the Windows Feedback app</p>
<p>Hardware reset (after 10 sec)</p></td>
</tr>
</tbody>
</table>

 

## <span id="button_behavior_in_windows_8.1"></span><span id="BUTTON_BEHAVIOR_IN_WINDOWS_8.1"></span>Button behavior in Windows 8.1


### <span id="Single_button_behavior_in_Windows_8.1"></span><span id="single_button_behavior_in_windows_8.1"></span><span id="SINGLE_BUTTON_BEHAVIOR_IN_WINDOWS_8.1"></span>Single button behavior in Windows 8.1

Button
Windows 8.1
Windows 8.1 Phone
Power
Press and release
Toggle On/Off
Toggle On/Off
Press and hold
Launch Shutdown Curtain
Launch Shutdown Curtain
Long press and hold
Hard shutdown
Hardware reset
Search
Press and release
Not supported
Launch Cortana
Press and hold
Not supported
Launch Cortana with Voice
Volume up
Press and release
Increment volume
Increment volume
Press and hold
Auto-repeat volume increment
Auto-repeat volume increment
Volume down
Press and release
Decrement volume
Decrement volume
Press and hold
Auto-repeat volume decrement
Auto-repeat volume decrement
Back
Not supported
Not supported
Start
Toggle Start screen
Toggle Start screen
Rotation lock
Release: Lock rotation
Lock rotation
Camera focus
Not supported
Not applicable
Camera shutter
Not supported
Not applicable
 

### <span id="Button_combination_behavior_in_Windows_8.1"></span><span id="button_combination_behavior_in_windows_8.1"></span><span id="BUTTON_COMBINATION_BEHAVIOR_IN_WINDOWS_8.1"></span>Button combination behavior in Windows 8.1

|                     |                           |                               |
|---------------------|---------------------------|-------------------------------|
| Button combination  | Windows 8.1               | Windows 8.1 Phone             |
| Start + Volume Up   | Toggle on-screen narrator | Not supported                 |
| Start + Volume Down | Take screenshot           | Not supported                 |
| Start + Power       | Ctrl+Alt+Del              | Not supported                 |
| Power + Volume Up   | Not supported             | Take screenshot               |
| Power + Volume Down | Not supported             | Hardware reset (after 10 sec) |

 

## <span id="related_topics"></span>Related topics
[Windows 10 button architecture](https://msdn.microsoft.com/library/windows/hardware/dn957423%28v=vs.85%29.aspx)  
[Minimum Hardware Requirements](https://msdn.microsoft.com/library/windows/hardware/dn915086.aspx)  



