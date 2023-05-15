---
title: IWiaUIExtension COM interface
description: IWiaUIExtension COM interface
ms.date: 05/03/2023
---

# IWiaUIExtension COM interface

If you implement the [**IWiaUIExtension**](/previous-versions/windows/hardware/drivers/ff545078(v=vs.85)) interface, you can implement none, some, or all the **IWiaUIExtension** methods.

If a particular method returns E_NOTIMPL, the system-provided alternative, and one is available, it is used instead.

The **IWiaUIExtension** interface provides the following methods:P

| Method | Description |
|--|--|
| [**IWiaUIExtension::DeviceDialog**](/previous-versions/windows/hardware/drivers/ff545069(v=vs.85)) | Provides a custom user interface that replaces the default system user interface. |
| [**IWiaUIExtension::GetDeviceBitmapLogo**](/previous-versions/windows/hardware/drivers/ff545073(v=vs.85)) | Gets a custom bitmap logo for the device. |
| [**IWiaUIExtension::GetDeviceIcon**](/previous-versions/windows/hardware/drivers/ff545075(v=vs.85)) | Gets a custom device icon. |

[**IWiaUIExtension::DeviceDialog**](/previous-versions/windows/hardware/drivers/ff545069(v=vs.85)) accepts a pointer to a [**DEVICEDIALOGDATA**](/windows-hardware/drivers/ddi/wiadevd/ns-wiadevd-tagdevicedialogdata) structure (declared in *wiadevd.h*), which contains all the data needed to implement the device dialog box.

The device dialog must be implemented as a modal Win32 dialog box, subject to the following four constraints:

1. The array of items returned in *pDeviceDialogData*--&gt;**ppWiaItems** must be allocated using **CoTaskMemAlloc**, and is freed by the application using **CoTaskMemFree** (see the Microsoft Windows SDK documentation for both functions).

1. You must not destroy or release the root item stored in *pDeviceDialogData* --&gt;**pIWiaItemRoot**. You also must not cause the root item to become invalid. For instance, you must not call the WIA_CMD_SYNCHRONIZE device command.

1. Return S_OK to indicate that the user requested a data transfer, and S_FALSE to indicate that the user canceled the transfer.

1. Take care to ensure that memory or resource leaks are not introduced in this component, because it runs in-process in the application.

[**IWiaUIExtension::GetDeviceIcon**](/previous-versions/windows/hardware/drivers/ff545075(v=vs.85)) allows the application to use a driver-specified icon. To avoid resource leaks, this icon should be loaded with **LoadImage**, using the LR_SHARED flag (see the Windows SDK documentation).

[**IWiaUIExtension::GetDeviceBitmapLogo**](/previous-versions/windows/hardware/drivers/ff545073(v=vs.85)) allows the application to present device and vendor logos as appropriate. Currently, no system components use this method. The bitmap should be a DIB-allocated bitmap using **CreateDIBSection**, or loaded using **LoadImage** with the LR_CREATEDIBSECTION flag (see the Windows SDK documentation for more information). This allows the application to extract any palette information and adapt to the current or changing display color depths.

To implement a custom scanning dialog box in a WIA scanner driver, use the **IWiaUIExtension::DeviceDialog** method (with the four constraints listed above) to create a Win32 modal dialog box and pass the DEVICEDIALOGDATA structure to the *dwInitParam* parameter of the DialogBoxParam function as an LPARAM.

It is important to remember that the device dialog box itself does not manage the data transfers. The dialog box merely returns a pointer to an array of **IWiaItem** interface pointers (with properties set) from the driver to the application. It is then up to the application to negotiate the transfer mechanism and format.
