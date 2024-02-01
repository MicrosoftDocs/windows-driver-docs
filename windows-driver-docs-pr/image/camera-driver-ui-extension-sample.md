---
title: Camera Driver UI Extension Sample
description: Camera driver UI extension sample
ms.date: 03/27/2023
---

# Camera driver UI extension sample

The *extend* directory in the WDK contains a sample user interface extension for WIA digital still camera drivers.

This sample shows how to write WIA user interface (UI) extensions. It adds tabs to the device properties dialog (accessible from Windows Explorer) and adds commands to the context menu for the sample camera device's icon. These extensions are applied to the WIA sample camera from the WDK by providing implementations of the **IShellPropSheetExt** and **IContextMenu** COM interfaces (described in the Microsoft Windows SDK documentation).
