---
title: IWiaUIExtension COM Interface
description: IWiaUIExtension COM Interface
ms.assetid: 10a8e981-889a-46f0-8bf5-da75632d4d94
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# IWiaUIExtension COM Interface





If you implement the [IWiaUIExtension interface](https://msdn.microsoft.com/library/windows/hardware/ff545078), you can implement none, some, or all the **IWiaUIExtension** methods. If a particular method returns E\_NOTIMPL, the system-provided alternative, and one is available, it is used instead.

The **IWiaUIExtension** interface provides the following methods:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Method</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff545069" data-raw-source="[&lt;strong&gt;IWiaUIExtension::DeviceDialog&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff545069)"><strong>IWiaUIExtension::DeviceDialog</strong></a></p></td>
<td><p>Provides a custom user interface that replaces the default system user interface.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff545073" data-raw-source="[&lt;strong&gt;IWiaUIExtension::GetDeviceBitmapLogo&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff545073)"><strong>IWiaUIExtension::GetDeviceBitmapLogo</strong></a></p></td>
<td><p>Gets a custom bitmap logo for the device.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff545075" data-raw-source="[&lt;strong&gt;IWiaUIExtension::GetDeviceIcon&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff545075)"><strong>IWiaUIExtension::GetDeviceIcon</strong></a></p></td>
<td><p>Gets a custom device icon.</p></td>
</tr>
</tbody>
</table>

 

[**IWiaUIExtension::DeviceDialog**](https://msdn.microsoft.com/library/windows/hardware/ff545069) accepts a pointer to a [**DEVICEDIALOGDATA**](https://msdn.microsoft.com/library/windows/hardware/ff540560) structure (declared in *wiadevd.h*), which contains all the data needed to implement the device dialog box.

The device dialog must be implemented as a modal Win32 dialog box, subject to the following four constraints:

1.  The array of items returned in *pDeviceDialogData*--&gt;**ppWiaItems** must be allocated using **CoTaskMemAlloc**, and is freed by the application using **CoTaskMemFree** (see the Microsoft Windows SDK documentation for both functions).

2.  You must not destroy or release the root item stored in *pDeviceDialogData* --&gt;**pIWiaItemRoot**. You also must not cause the root item to become invalid. For instance, you must not call the WIA\_CMD\_SYNCHRONIZE device command.

3.  Return S\_OK to indicate that the user requested a data transfer, and S\_FALSE to indicate that the user canceled the transfer.

4.  Take care to ensure that memory or resource leaks are not introduced in this component, because it runs in-process in the application.

[**IWiaUIExtension::GetDeviceIcon**](https://msdn.microsoft.com/library/windows/hardware/ff545075) allows the application to use a driver-specified icon. To avoid resource leaks, this icon should be loaded with **LoadImage**, using the LR\_SHARED flag (see the Windows SDK documentation).

[**IWiaUIExtension::GetDeviceBitmapLogo**](https://msdn.microsoft.com/library/windows/hardware/ff545073) allows the application to present device and vendor logos as appropriate. Currently, no system components use this method. The bitmap should be a DIB-allocated bitmap using **CreateDIBSection**, or loaded using **LoadImage** with the LR\_CREATEDIBSECTION flag (see the Windows SDK documentation for more information). This allows the application to extract any palette information and adapt to the current or changing display color depths.

To implement a custom scanning dialog box in a WIA scanner driver, use the **IWiaUIExtension::DeviceDialog** method (with the four constraints listed above) to create a Win32 modal dialog box and pass the DEVICEDIALOGDATA structure to the *dwInitParam* parameter of the DialogBoxParam function as an LPARAM.

It is important to remember that the device dialog box itself does not manage the data transfers. The dialog box merely returns a pointer to an array of **IWiaItem** interface pointers (with properties set) from the driver to the application. It is then up to the application to negotiate the transfer mechanism and format.

 

 




