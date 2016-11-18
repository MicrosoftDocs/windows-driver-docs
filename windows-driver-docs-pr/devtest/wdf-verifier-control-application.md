---
title: WDF Verifier Control Application
description: The Windows Driver Frameworks (WDF) Verifier control application (WdfVerifier.exe) is a tool for debugging Kernel-Mode Driver Framework (KMDF) and User-Mode Driver Framework (UMDF) drivers.
ms.assetid: 896b63db-69c6-4fcb-a50f-0c4aed394b0b
keywords: ["WDF Verifier control application WDK , features", "WDF Verifier WDK", "tools WDK , verifying drivers", "testing drivers WDK WDF", "debugging drivers WDK WDF", "verifying drivers WDK WDF", "verifier WDK KMDF", "verifier WDK UMDF"]
---

# WDF Verifier Control Application


The Windows Driver Frameworks (WDF) Verifier control application (WdfVerifier.exe) is a tool for debugging Kernel-Mode Driver Framework (KMDF) and User-Mode Driver Framework (UMDF) drivers. You can use the tool for a quick assessment of drivers on a machine, and to make changes to their debugger settings.

This documentation describes options found in the version of the application that ships as part of Windows Driver Kit (WDK) 8.1.

**Important**   To use WDF Verifier, you must have administrative privileges on the computer.

 

### <span id="wdf_verifier_features"></span><span id="WDF_VERIFIER_FEATURES"></span>What can I do with it?

-   Get quick information about all WDF drivers on a computer. You can organize the list by driver or by device.
-   Manage registry settings for debugging WDF drivers.
-   View UMDF driver host processes and drivers they host.
-   Manage diagnostic output.
-   Start user-mode debugging sessions, either manually or automatically.

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
<td align="left"><p>[WDF Drivers Tab](wdf-drivers-tab.md)</p></td>
<td align="left"><p>This topic provides detailed information about WDF Verifier's <strong>WDF Drivers</strong> page. This page lists all WDF drivers on the computer, and you can change their verification settings and the settings of devices that use them. Start here if you're interested in a specific driver.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[Devices Using WDF Tab](devices-using-wdf-tab.md)</p></td>
<td align="left"><p>This topic discusses WDF Verifier's <strong>Devices using WDF</strong> page. This page lists all devices that are using WDF drivers. When you highlight a device, you see the WDF driver stack for the highlighted device. You can also change verification settings from this screen.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[Global WDF Settings Tab](global-wdf-settings-tab.md)</p></td>
<td align="left"><p>This topic provides detailed information about WDF Verifier's <strong>Global WDF Settings</strong> page. This page presents global (system-wide) WDF verification options, and shows UMDF host processes with hosted drivers.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[UMDF Settings (Test Use Only) Tab](umdf-settings-test-use-only-tab.md)</p></td>
<td align="left"><p>This topic details WDF Verifier's <strong>UMDF Settings (Test Use Only)</strong> page. On this page, you can change settings that can help test an overall system with one or more UMDF drivers.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[My Preferences Tab](my-preferences-tab.md)</p></td>
<td align="left"><p>This topic describes WDF Verifier's <strong>My Preferences</strong> page. On this page, you can set preferences for some of the control panel’s features.</p></td>
</tr>
</tbody>
</table>

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20WDF%20Verifier%20Control%20Application%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




