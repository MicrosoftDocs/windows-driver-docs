---
title: WIA DDI Interfaces
description: WIA DDI Interfaces
ms.assetid: 738a87e2-9c74-4215-85dc-ec793f10ce05
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# WIA DDI Interfaces





The WIA device driver interface (DDI) supplies the following interfaces and functions to developers of WIA minidrivers:

-   [IWiaMiniDrv COM Interface](iwiaminidrv-com-interface.md), which provides the minidriver communication methods. These methods are the entry points for all communication between the WIA service and the minidriver. These methods enable the WIA service to control the device.

-   [WIA driver services library](wia-driver-services-library.md) (**wias***Xxx* functions), which provides helper functions for WIA minidrivers. You can use these functions to perform many common tasks for which you would otherwise have to write custom functions.

-   [WIA utility library](wia-utility-library.md), which provides additional helper functions and three classes that WIA minidrivers can use.

-   [IWiaMiniDrvCallBack COM interface](iwiaminidrvcallback-com-interface.md), which provides a callback method for WIA minidrivers to use during a callback data transfer.

-   [IWiaDrvItem COM interface](iwiadrvitem-com-interface.md), which provides methods for a minidriver to maintain the device's tree of **IWiaDrvItem** objects.

-   [User interface extensions](user-interface-extensions.md), which enable vendors to supply features for their devices that are not available through the default WIA user interfaces.

-   [IWiaLog COM interface](iwialog-com-interface.md), which provides methods and macros that enable WIA minidrivers to log messages to a diagnostic log file.

 

 




