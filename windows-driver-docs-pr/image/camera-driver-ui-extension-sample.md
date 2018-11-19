---
title: Camera Driver UI Extension Sample
description: Camera Driver UI Extension Sample
ms.assetid: 21ddf804-fff5-4cdc-adb5-f85d769ccc1f
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Camera Driver UI Extension Sample





The *extend* directory in the WDK contains a sample user interface extension for WIA digital still camera drivers.

This sample shows how to write WIA user interface (UI) extensions. It adds tabs to the device properties dialog (accessible from Windows Explorer) and adds commands to the context menu for the sample camera device's icon. These extensions are applied to the WIA sample camera from the WDK by providing implementations of the **IShellPropSheetExt** and **IContextMenu** COM interfaces (described in the Microsoft Windows SDK documentation).

 

 




