---
title: WIA Root Item
description: WIA Root Item
ms.assetid: cf4d1056-3437-4ba7-8a87-421e91afd02a
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# WIA Root Item





A WIA root item is a folder item that represents the device itself. A WIA root item is marked with **WiaItemTypeRoot** and **WiaItemTypeDevice** and contains device attributes such as:

-   The manufacturer name

-   The device name

-   Driver attributes (including the driver version and the user interface CLSID)

Imaging applications obtain the root item in the WIA item tree by calling the **IWiaDevMgr::CreateDevice** method (described in the Microsoft Windows SDK documentation). The application then uses the root item to enumerate the tree, thereby gaining access to individual child items.

 

 




