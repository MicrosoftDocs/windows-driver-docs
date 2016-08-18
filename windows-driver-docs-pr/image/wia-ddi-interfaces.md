---
title: WIA DDI Interfaces
author: windows-driver-content
description: WIA DDI Interfaces
MS-HAID:
- 'WIA\_arch\_9e0ef36b-dea7-4da4-98e9-c5f241aa256e.xml'
- 'image.wia\_ddi\_interfaces'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 738a87e2-9c74-4215-85dc-ec793f10ce05
---

# WIA DDI Interfaces


## <a href="" id="ddk-wia-ddi-interfaces-si"></a>


The WIA device driver interface (DDI) supplies the following interfaces and functions to developers of WIA minidrivers:

-   [IWiaMiniDrv COM Interface](iwiaminidrv-com-interface.md), which provides the minidriver communication methods. These methods are the entry points for all communication between the WIA service and the minidriver. These methods enable the WIA service to control the device.

-   [WIA driver services library](wia-driver-services-library.md) (**wias***Xxx* functions), which provides helper functions for WIA minidrivers. You can use these functions to perform many common tasks for which you would otherwise have to write custom functions.

-   [WIA utility library](wia-utility-library.md), which provides additional helper functions and three classes that WIA minidrivers can use.

-   [IWiaMiniDrvCallBack COM interface](iwiaminidrvcallback-com-interface.md), which provides a callback method for WIA minidrivers to use during a callback data transfer.

-   [IWiaDrvItem COM interface](iwiadrvitem-com-interface.md), which provides methods for a minidriver to maintain the device's tree of **IWiaDrvItem** objects.

-   [User interface extensions](user-interface-extensions.md), which enable vendors to supply features for their devices that are not available through the default WIA user interfaces.

-   [IWiaLog COM interface](iwialog-com-interface.md), which provides methods and macros that enable WIA minidrivers to log messages to a diagnostic log file.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20WIA%20DDI%20Interfaces%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


