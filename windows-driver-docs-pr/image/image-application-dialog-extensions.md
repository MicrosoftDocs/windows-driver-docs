---
title: Image Application Dialog Extensions
author: windows-driver-content
description: Image Application Dialog Extensions
MS-HAID:
- 'WIA\_drv\_cus\_614f0450-60a6-4cd6-a9ec-04e9d1f68179.xml'
- 'image.image\_application\_dialog\_extensions'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 4bb7d2f9-58c3-4cfa-aa6b-a4bd9335d2ac
---

# Image Application Dialog Extensions


## <a href="" id="ddk-image-application-dialog-extensions-si"></a>


There are three mechanisms for extending WIA image application dialogs. These include:

-   Supplying a device icon to be used in place of the system-provided icon in any place where an icon needs to be displayed for the device. To do this, implement the [**IWiaUIExtension::GetDeviceIcon**](https://msdn.microsoft.com/library/windows/hardware/ff545075) method.

-   Providing [property sheet extensions](property-sheet-extensions.md) that extend the system-provided property pages, which are displayed when the user views the advanced settings or properties for a device in the common WIA acquisition dialog or in Windows Explorer. To do this, implement the **IShellExtInit** and **IShellPropSheetExt** interfaces (see the Microsoft Windows SDK documentation).

-   Providing a complete replacement for the system-provided dialogs displayed in response to a call to **IWiaItem::DeviceDlg** (see the Windows SDK documentation). To do this, implement the [**IWiaUIExtension::DeviceDialog**](https://msdn.microsoft.com/library/windows/hardware/ff545069) method.

The remainder of this section contains additional information about the [IWiaUIExtension COM interface](iwiauiextension-com-interface.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Image%20Application%20Dialog%20Extensions%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


