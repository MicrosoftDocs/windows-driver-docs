---
title: WIA Root Item
author: windows-driver-content
description: WIA Root Item
ms.assetid: cf4d1056-3437-4ba7-8a87-421e91afd02a
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# WIA Root Item


## <a href="" id="ddk-wia-root-item-si"></a>


A WIA root item is a folder item that represents the device itself. A WIA root item is marked with **WiaItemTypeRoot** and **WiaItemTypeDevice** and contains device attributes such as:

-   The manufacturer name

-   The device name

-   Driver attributes (including the driver version and the user interface CLSID)

Imaging applications obtain the root item in the WIA item tree by calling the **IWiaDevMgr::CreateDevice** method (described in the Microsoft Windows SDK documentation). The application then uses the root item to enumerate the tree, thereby gaining access to individual child items.

 

 




