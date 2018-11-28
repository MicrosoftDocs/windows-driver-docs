---
title: Context Menu Extensions
description: Context Menu Extensions
ms.assetid: 6c52dd43-7f47-476e-acbc-15269d23ea71
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Context Menu Extensions





In both the Scanners and Cameras Control Panel folder for devices (root items), and in the My Computer folder, the user can choose various actions to perform on a selected item, based on the actions exposed on its context menu. To find these actions, the user right-clicks the thumbnail or icon of the given image.

A way to add to the actions on the context menu is to implement the **IContextMenu** interface (see the Microsoft Windows SDK documentation). A vendor can provide an in-process server that implements the **IContextMenu** interface for **IWiaItem** (see the Windows SDK documentation) items that the device provides. Whenever WIA queries for the context menu of an image, the vendor-supplied UI extension in turn calls **IContextMenu::QueryContextMenu** from the handlers registered for the given imaging device. Calls to **IContextMenu::InvokeCommand** for items not handled by the default UI are passed in turn to the appropriate vendor-supplied extension.

 

 




