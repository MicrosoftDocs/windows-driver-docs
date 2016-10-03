---
title: IWiaUIExtension COM Interface
author: windows-driver-content
description: IWiaUIExtension COM Interface
MS-HAID:
- 'WIA\_drv\_cus\_59d948bd-d29d-4c12-aba0-a8fa0130d9bc.xml'
- 'image.iwiauiextension\_com\_interface'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 10a8e981-889a-46f0-8bf5-da75632d4d94
---

# IWiaUIExtension COM Interface


## <a href="" id="ddk-iwiauiextension-com-interface-si"></a>


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
<td><p>[<strong>IWiaUIExtension::DeviceDialog</strong>](https://msdn.microsoft.com/library/windows/hardware/ff545069)</p></td>
<td><p>Provides a custom user interface that replaces the default system user interface.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>IWiaUIExtension::GetDeviceBitmapLogo</strong>](https://msdn.microsoft.com/library/windows/hardware/ff545073)</p></td>
<td><p>Gets a custom bitmap logo for the device.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>IWiaUIExtension::GetDeviceIcon</strong>](https://msdn.microsoft.com/library/windows/hardware/ff545075)</p></td>
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20IWiaUIExtension%20COM%20Interface%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


