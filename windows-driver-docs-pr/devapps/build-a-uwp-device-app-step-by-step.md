---
title: Build a UWP device app step-by-step
description: This step-by-step guide describes in detail how to build a UWP device app with Microsoft Visual Studio and the Device Metadata Authoring Wizard.
ms.assetid: 2E3B47B6-1278-48EC-A530-64B8970A0142
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# <span id="devapps.build_a_windows_store_device_app_step-by-step"></span>Build a UWP device app step-by-step


This step-by-step guide describes in detail how to build a UWP device app with Microsoft Visual Studio and the Device Metadata Authoring Wizard. For a high-level introduction to this process, see [Building UWP device apps](the-workflow.md).

A UWP device app is a special kind of UWP app that device manufacturers create to serve as a companion to their internal or peripheral device. By using device metadata, device apps can run privileged operations and automatically install when a device is plugged in. For more info about UWP device apps, see [Meet UWP device apps](meet-uwp-device-apps.md).

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
<td align="left"><p><a href="step-1--create-a-uwp-device-app.md" data-raw-source="[Step 1: Create a UWP device app](step-1--create-a-uwp-device-app.md)">Step 1: Create a UWP device app</a></p></td>
<td align="left"><p>This topic describes the basic process for creating a UWP device app by using Visual Studio. Learn about the tasks that are common to all UWP device apps.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="step-2--create-device-metadata.md" data-raw-source="[Step 2: Create device metadata](step-2--create-device-metadata.md)">Step 2: Create device metadata</a></p></td>
<td align="left"><p>This topic describes how to use the <strong>Device Metadata Authoring Wizard</strong> to create new device metadata that associates your UWP device app with a device. The wizard can also create a <strong>StoreManfest.xml</strong> file that you may need to add to your app in the next step.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="step-3--add-an-experience-id-to-the-app.md" data-raw-source="[Step 3: Add an experience ID to the app](step-3--add-an-experience-id-to-the-app.md)">Step 3: Add an experience ID to the app</a></p></td>
<td align="left"><p>This topic describes how to add the experience ID to your UWP device app. The <em>experience ID</em> is a GUID that uniquely identifies a device metadata package; it&#39;s required if your app is configured for automatic installation, as is the case with <a href="uwp-device-apps-for-printers.md" data-raw-source="[UWP device apps for printers](uwp-device-apps-for-printers.md)">UWP device apps for printers</a> and <a href="uwp-device-apps-for-webcams.md" data-raw-source="[cameras](uwp-device-apps-for-webcams.md)">cameras</a>.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="step-4--test-device-metadata.md" data-raw-source="[Step 4: Test device metadata](step-4--test-device-metadata.md)">Step 4: Test device metadata</a></p></td>
<td align="left"><p>This topic describes how you can test device metadata for your UWP device app locally before you submit it to the Windows Dev Center Dashboard.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="step-5--submit-the-app.md" data-raw-source="[Step 5: Submit the app](step-5--submit-the-app.md)">Step 5: Submit the app</a></p></td>
<td align="left"><p>This topic describes how to submit your UWP device app to the Microsoft Store dashboard.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="step-6--submit-device-metadata.md" data-raw-source="[Step 6: Submit device metadata](step-6--submit-device-metadata.md)">Step 6: Submit device metadata</a></p></td>
<td align="left"><p>This topic describes how to submit device metadata for your UWP device app to the Windows Dev Center hardware dashboard.</p></td>
</tr>
</tbody>
</table>

 

 

 





