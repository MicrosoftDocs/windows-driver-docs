---
title: GPIO Buttons and Indicators Implementation Guide
description: Windows 8 introduced support for general-purpose I/O (GPIO) buttons and indicators by using a HID miniport class driver.
ms.date: 10/17/2018
---

# GPIO buttons and indicators implementation guide


Windows 8 introduced support for general-purpose I/O (GPIO) buttons and indicators by using a HID miniport class driver. The goal was to provide support for key buttons (Power, Windows, volume and rotation lock) in a standardized way, together with associated corresponding Windows Engineering Guidance (WEG). Windows 8.1 is focused on enhancing the quality of the end-to-end user experience and unifying the behavior across various innovative form factors.

## <span id="in_this_section"></span>In this section


<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Topic</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><a href="state-indicators.md" data-raw-source="[State indicators](state-indicators.md)">State indicators</a></p></td>
<td align="left"><p>This section describes the states of the mode and docking indicators.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="physical-buttons.md" data-raw-source="[Physical buttons](physical-buttons.md)">Physical buttons</a></p></td>
<td align="left"><p>Hardware buttons let users perform many common tasks that do not have a convenient user interface alternative. For the scenarios addressed in this section, the hardware buttons are typically used for tasks that occur while the physical keyboard is not available to the user, on form factors such as convertibles or slates.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="interface-implementation-guidance.md" data-raw-source="[Interface implementation guidance](interface-implementation-guidance.md)">Interface implementation guidance</a></p></td>
<td align="left"><p>This section provides guidance for interface implementation.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="code-samples.md" data-raw-source="[Code samples](code-samples.md)">Code samples</a></p></td>
<td align="left"><p>This section includes code samples and sample descriptors for interface implementation.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="implement-the-unattended-windows-setup-setting.md" data-raw-source="[Implement the unattended Windows Setup setting](implement-the-unattended-windows-setup-setting.md)">Implement the unattended Windows Setup setting</a></p></td>
<td align="left"><p>This topic describes how to set the unattended Windows Setup component setting.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="logging-and-investigations.md" data-raw-source="[Logging and investigations](logging-and-investigations.md)">Logging and investigations</a></p></td>
<td align="left"><p>This topic describes logging and investigations for GPIO implementations.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="running-test-passes.md" data-raw-source="[Running test passes](running-test-passes.md)">Running test passes</a></p></td>
<td align="left"><p>The MITT platform can test GPIO buttons by offering both test automation and the option to customize the GPIO patterns that are sent for targeted investigations.</p></td>
</tr>
</tbody>
</table>

 

As part of Windows 8.1 investments, the **msgpio** button driver brings important enhancements:

-   Augmented logging to speed up investigations.
-   Improved synchronization and error handling to enhance the robustness.
-   The new ConvertibleSlateMode [Unattended Windows Setup](/previous-versions/windows/it-pro/windows-8.1-and-8/ff699026(v=win.10)) to be used on non-GPIO laptops to statically set the mode to laptop as part of the OEM image customization.

For questions about GPIO buttons and indicator implementation, send an e-mail to the Microsoft support group at dockingsupport@microsoft.com.

## <span id="related_topics"></span>Related topics
[Power Button Behaviors and Implementation](/collaborate/connect-redirect?DownloadID=47452)  
[Connected Standby Wake Sources](/collaborate/connect-redirect?DownloadID=49891)  
[ACPI Design Guide](/collaborate/connect-redirect?DownloadID=48755)  
[GetSystemMetrics function](/windows/win32/api/winuser/nf-winuser-getsystemmetrics)  
[Keyboard Enhancements in Windows 8](/previous-versions/windows/hardware/design/dn613956(v=vs.85))  
[Windows Hardware Compatibility Program](/windows-hardware/design/compatibility/index)  
[Certification requirements for Windows desktop apps](/windows/win32/win_cert/certification-requirements-for-windows-desktop-apps)  
[HID over I²C](../hid/hid-over-i2c-guide.md)  
[GPIO tests in MITT](../spb/gpio-tests-in-mitt.md)  
[Windows System Image Manager Technical Reference](/previous-versions/windows/it-pro/windows-vista/cc722301(v=ws.10))  
[Unattended Windows Setup Reference](/previous-versions/windows/it-pro/windows-8.1-and-8/ff699026(v=win.10))  
[Windows Driver Kit (WDK) 8.1](https://go.microsoft.com/fwlink/p/?linkid=310164)
