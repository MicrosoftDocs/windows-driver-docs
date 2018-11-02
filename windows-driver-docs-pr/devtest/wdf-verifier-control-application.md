---
title: WDF Verifier Control Application
description: The Windows Driver Frameworks (WDF) Verifier control application (WdfVerifier.exe) is a tool for debugging KMDF and UMDF drivers.
ms.assetid: 896b63db-69c6-4fcb-a50f-0c4aed394b0b
keywords:
- WDF Verifier control application WDK , features
- WDF Verifier WDK
- tools WDK , verifying drivers
- testing drivers WDK WDF
- debugging drivers WDK WDF
- verifying drivers WDK WDF
- verifier WDK KMDF
- verifier WDK UMDF
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# WDF Verifier Control Application


The Windows Driver Frameworks (WDF) Verifier control application (WdfVerifier.exe) is a tool for debugging Kernel-Mode Driver Framework (KMDF) and User-Mode Driver Framework (UMDF) drivers. You can use the tool for a quick assessment of drivers on a machine, and to make changes to their debugger settings.

This documentation describes options found in the version of the application that ships as part of Windows Driver Kit (WDK) 8.1.

**Important**  To use WDF Verifier, you must have administrative privileges on the computer.

 

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
<td align="left"><p><a href="wdf-drivers-tab.md" data-raw-source="[WDF Drivers Tab](wdf-drivers-tab.md)">WDF Drivers Tab</a></p></td>
<td align="left"><p>This topic provides detailed information about WDF Verifier&#39;s <strong>WDF Drivers</strong> page. This page lists all WDF drivers on the computer, and you can change their verification settings and the settings of devices that use them. Start here if you&#39;re interested in a specific driver.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="devices-using-wdf-tab.md" data-raw-source="[Devices Using WDF Tab](devices-using-wdf-tab.md)">Devices Using WDF Tab</a></p></td>
<td align="left"><p>This topic discusses WDF Verifier&#39;s <strong>Devices using WDF</strong> page. This page lists all devices that are using WDF drivers. When you highlight a device, you see the WDF driver stack for the highlighted device. You can also change verification settings from this screen.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="global-wdf-settings-tab.md" data-raw-source="[Global WDF Settings Tab](global-wdf-settings-tab.md)">Global WDF Settings Tab</a></p></td>
<td align="left"><p>This topic provides detailed information about WDF Verifier&#39;s <strong>Global WDF Settings</strong> page. This page presents global (system-wide) WDF verification options, and shows UMDF host processes with hosted drivers.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="umdf-settings-test-use-only-tab.md" data-raw-source="[UMDF Settings (Test Use Only) Tab](umdf-settings-test-use-only-tab.md)">UMDF Settings (Test Use Only) Tab</a></p></td>
<td align="left"><p>This topic details WDF Verifier&#39;s <strong>UMDF Settings (Test Use Only)</strong> page. On this page, you can change settings that can help test an overall system with one or more UMDF drivers.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="my-preferences-tab.md" data-raw-source="[My Preferences Tab](my-preferences-tab.md)">My Preferences Tab</a></p></td>
<td align="left"><p>This topic describes WDF Verifier&#39;s <strong>My Preferences</strong> page. On this page, you can set preferences for some of the control panel&#39;s features.</p></td>
</tr>
</tbody>
</table>

 

 

 





