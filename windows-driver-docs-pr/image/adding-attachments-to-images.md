---
title: Adding Attachments to Images
author: windows-driver-content
description: Adding Attachments to Images
ms.assetid: 704f541b-b98c-44a8-bb19-5d5d0d1eab78
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Adding Attachments to Images


## <a href="" id="ddk-adding-attachments-to-images-si"></a>


When an item is marked with **WiaItemTypeHasAttachments**, this means that the item has associated attachments, which are stored as child items. This is not the same as an item of type **WiaItemTypeFolder**. The main differences are:

-   Items of type **WiaItemTypeHasAttachments** have only one level of children. Items of type **WiaItemTypeFolder** can have any number of levels of children.

-   All children of an item of type **WiaItemTypeHasAttachments** are related to that item. For example, if an image item has associated audio data, the audio data would be stored as a child of the image item, and the image item would be marked with **WiaItemTypeHasAttachments**.

An item cannot be both of type **WiaItemTypeHasAttachments** and type **WiaItemTypeFolder**. However, an item can be of type **WiaItemTypeHasAttachments** and type **WiaItemTypeFile**. This is because an item of type **WiaItemTypeHasAttachments** is conceptually treated as a single entity. The following diagram illustrates the WIA Camera item tree with attachments.

![diagram illustrating a wia camera item tree with attachments](images/camera-tree-attachments.png)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Adding%20Attachments%20to%20Images%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


