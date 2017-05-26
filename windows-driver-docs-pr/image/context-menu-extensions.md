---
title: Context Menu Extensions
author: windows-driver-content
description: Context Menu Extensions
ms.assetid: 6c52dd43-7f47-476e-acbc-15269d23ea71
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Context Menu Extensions


## <a href="" id="ddk-context-menu-extensions-si"></a>


In both the Scanners and Cameras Control Panel folder for devices (root items), and in the My Computer folder, the user can choose various actions to perform on a selected item, based on the actions exposed on its context menu. To find these actions, the user right-clicks the thumbnail or icon of the given image.

A way to add to the actions on the context menu is to implement the **IContextMenu** interface (see the Microsoft Windows SDK documentation). A vendor can provide an in-process server that implements the **IContextMenu** interface for **IWiaItem** (see the Windows SDK documentation) items that the device provides. Whenever WIA queries for the context menu of an image, the vendor-supplied UI extension in turn calls **IContextMenu::QueryContextMenu** from the handlers registered for the given imaging device. Calls to **IContextMenu::InvokeCommand** for items not handled by the default UI are passed in turn to the appropriate vendor-supplied extension.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Context%20Menu%20Extensions%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


