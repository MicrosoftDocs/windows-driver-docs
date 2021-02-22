---
title: Image Application Dialog Extensions
description: Image Application Dialog Extensions
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Image Application Dialog Extensions





There are three mechanisms for extending WIA image application dialogs. These include:

-   Supplying a device icon to be used in place of the system-provided icon in any place where an icon needs to be displayed for the device. To do this, implement the [**IWiaUIExtension::GetDeviceIcon**](/previous-versions/windows/hardware/drivers/ff545075(v=vs.85)) method.

-   Providing [property sheet extensions](property-sheet-extensions.md) that extend the system-provided property pages, which are displayed when the user views the advanced settings or properties for a device in the common WIA acquisition dialog or in Windows Explorer. To do this, implement the **IShellExtInit** and **IShellPropSheetExt** interfaces (see the Microsoft Windows SDK documentation).

-   Providing a complete replacement for the system-provided dialogs displayed in response to a call to **IWiaItem::DeviceDlg** (see the Windows SDK documentation). To do this, implement the [**IWiaUIExtension::DeviceDialog**](/previous-versions/windows/hardware/drivers/ff545069(v=vs.85)) method.

The remainder of this section contains additional information about the [IWiaUIExtension COM interface](iwiauiextension-com-interface.md).

 

