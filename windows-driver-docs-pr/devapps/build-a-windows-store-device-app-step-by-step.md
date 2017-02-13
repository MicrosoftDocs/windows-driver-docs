---
title: Build a Windows Store device app step-by-step
description: This step-by-step guide describes in detail how to build a Windows Store device app with Microsoft Visual Studio 2013 and the Device Metadata Authoring Wizard.
ms.assetid: 2E3B47B6-1278-48EC-A530-64B8970A0142
---

# <span id="devapps.build_a_windows_store_device_app_step-by-step"></span>Build a Windows Store device app step-by-step


This step-by-step guide describes in detail how to build a Windows Store device app with Microsoft Visual Studio 2013 and the Device Metadata Authoring Wizard. For a high-level introduction to this process, see [Building Windows Store device apps](the-workflow.md).

A Windows Store device app is a special kind of Windows Store app that device manufacturers create to serve as a companion to their internal or peripheral device. By using device metadata, device apps can run privileged operations and automatically install when a device is plugged in. For more info about Windows Store device apps, see [Meet Windows Store device apps](meet-windows-store-device-apps.md).

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
<td align="left"><p>[Step 1: Create a Windows Store device app](step-1--create-a-windows-store-device-app.md)</p></td>
<td align="left"><p>This topic describes the basic process for creating a Windows Store device app by using Visual Studio 2013. Learn about the tasks that are common to all Windows Store device apps.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[Step 2: Create device metadata](step-2--create-device-metadata.md)</p></td>
<td align="left"><p>This topic describes how to use the <strong>Device Metadata Authoring Wizard</strong> to create new device metadata that associates your Windows Store device app with a device. The wizard can also create a <strong>StoreManfest.xml</strong> file that you may need to add to your app in the next step.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[Step 3: Add an experience ID to the app](step-3--add-an-experience-id-to-the-app.md)</p></td>
<td align="left"><p>This topic describes how to add the experience ID to your Windows Store device app. The <em>experience ID</em> is a GUID that uniquely identifies a device metadata package; it's required if your app is configured for automatic installation, as is the case with [Windows Store device apps for printers](windows-store-device-apps-for-printers.md) and [cameras](windows-store-device-apps-for-webcams.md).</p></td>
</tr>
<tr class="even">
<td align="left"><p>[Step 4: Test device metadata](step-4--test-device-metadata.md)</p></td>
<td align="left"><p>This topic describes how you can test device metadata for your Windows Store device app locally before you submit it to the Windows Dev Center Dashboard.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[Step 5: Submit the app](step-5--submit-the-app.md)</p></td>
<td align="left"><p>This topic describes how to submit your Windows Store device app to the Windows Store dashboard.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[Step 6: Submit device metadata](step-6--submit-device-metadata.md)</p></td>
<td align="left"><p>This topic describes how to submit device metadata for your Windows Store device app to the Windows Dev Center hardware dashboard.</p></td>
</tr>
</tbody>
</table>

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devapps\devapps]:%20Build%20a%20Windows%20Store%20device%20app%20step-by-step%20%20RELEASE:%20%281/20/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




