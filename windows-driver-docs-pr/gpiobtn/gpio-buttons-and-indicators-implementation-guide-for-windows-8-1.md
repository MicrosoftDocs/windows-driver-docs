---
title: GPIO buttons and indicators implementation guide
author: windows-driver-content
description: Windows 8 introduced support for general-purpose I/O (GPIO) buttons and indicators by using a HID miniport class driver.
ms.assetid: E073E15A-7068-43D0-9DBA-7DD2E7FE2993
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
<td align="left"><p>[State indicators](state-indicators.md)</p></td>
<td align="left"><p>This section describes the states of the mode and docking indicators.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[Physical buttons](physical-buttons.md)</p></td>
<td align="left"><p>Hardware buttons let users perform many common tasks that do not have a convenient user interface alternative. For the scenarios addressed in this section, the hardware buttons are typically used for tasks that occur while the physical keyboard is not available to the user, on form factors such as convertibles or slates.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[Interface implementation guidance](interface-implementation-guidance.md)</p></td>
<td align="left"><p>This section provides guidance for interface implementation.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[Code samples](code-samples.md)</p></td>
<td align="left"><p>This section includes code samples and sample descriptors for interface implementation.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[Implement the unattended Windows Setup setting](implement-the-unattended-windows-setup-setting.md)</p></td>
<td align="left"><p>This topic describes how to set the unattended Windows Setup component setting.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[Logging and investigations](logging-and-investigations.md)</p></td>
<td align="left"><p>This topic describes logging and investigations for GPIO implementations.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[Running test passes](running-test-passes.md)</p></td>
<td align="left"><p>The MITT platform can test GPIO buttons by offering both test automation and the option to customize the GPIO patterns that are sent for targeted investigations.</p></td>
</tr>
</tbody>
</table>

 

As part of Windows 8.1 investments, the **msgpio** button driver brings important enhancements:

-   Augmented logging to speed up investigations.
-   Improved synchronization and error handling to enhance the robustness.
-   The new ConvertibleSlateMode [Unattended Windows Setup](http://go.microsoft.com/fwlink/p/?linkid=276788) to be used on non-GPIO laptops to statically set the mode to laptop as part of the OEM image customization.

For questions about GPIO buttons and indicator implementation, send an e-mail to the Microsoft support group at dockingsupport@microsoft.com.

## <span id="related_topics"></span>Related topics
[Power Button Behaviors and Implementation](http://connect.microsoft.com/site1304/Downloads/DownloadDetails.aspx?DownloadID=47452)  
[Connected Standby Wake Sources](http://connect.microsoft.com/site1304/Downloads/DownloadDetails.aspx?DownloadID=49891)  
[ACPI Design Guide](http://connect.microsoft.com/site1304/Downloads/DownloadDetails.aspx?DownloadID=48755)  
[GetSystemMetrics function](http://go.microsoft.com/fwlink/p/?linkid=324686)  
[Keyboard Enhancements in Windows 8](http://go.microsoft.com/fwlink/p/?linkid=324536)  
[Windows Hardware Compatibility Program](https://msdn.microsoft.com/library/windows/hardware/dn922588)  
[Certification requirements for Windows desktop apps](http://go.microsoft.com/fwlink/p/?linkid=306131)  
[HID over I²C](http://go.microsoft.com/fwlink/p/?linkid=324690)  
[GPIO tests in MITT](https://msdn.microsoft.com/library/windows/hardware/dn919780)  
[Windows System Image Manager Technical Reference](http://go.microsoft.com/fwlink/p/?linkid=324691)  
[Unattended Windows Setup Reference](http://go.microsoft.com/fwlink/p/?linkid=276788)  
[Windows Driver Kit (WDK) 8.1](http://go.microsoft.com/fwlink/p/?linkid=310164)  

--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[gpiobtn\gpiobtn]:%20GPIO%20buttons%20and%20indicators%20implementation%20guide%20%20RELEASE:%20%289/25/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


