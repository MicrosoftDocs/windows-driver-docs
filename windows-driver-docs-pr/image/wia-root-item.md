---
title: WIA Root Item
author: windows-driver-content
description: WIA Root Item
MS-HAID:
- 'WIA\_tree\_6edeb785-0066-4125-bc77-0973f9e53b4f.xml'
- 'image.wia\_root\_item'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: cf4d1056-3437-4ba7-8a87-421e91afd02a
---

# WIA Root Item


## <a href="" id="ddk-wia-root-item-si"></a>


A WIA root item is a folder item that represents the device itself. A WIA root item is marked with **WiaItemTypeRoot** and **WiaItemTypeDevice** and contains device attributes such as:

-   The manufacturer name

-   The device name

-   Driver attributes (including the driver version and the user interface CLSID)

Imaging applications obtain the root item in the WIA item tree by calling the **IWiaDevMgr::CreateDevice** method (described in the Microsoft Windows SDK documentation). The application then uses the root item to enumerate the tree, thereby gaining access to individual child items.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20WIA%20Root%20Item%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


