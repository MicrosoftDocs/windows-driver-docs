---
title: Multipage IStream Transfers
author: windows-driver-content
description: Multipage IStream Transfers
ms.assetid: 0d17cfa8-f200-4d87-a2cb-cfd8dbc24e1e
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Multipage IStream Transfers


Typically, when a data transfer is requested on an item, the data from that item is transferred, using the settings that the item's properties specify. For example, if an application is on the "Flatbed" item for a scanner, a data transfer will result in a scan from the Flatbed, using the settings that are stored in the WIA properties on the "Flatbed" item.

However, in Windows Vista, another type of transfer is available: a multi-item transfer, also known as *folder acquisition*. In this kind of transfer, an application requests a transfer from a folder item by using a specified flag (WIA\_TRANSFER\_ACQUIRE\_CHILDREN), and the transfer results in a transfer from each of the leaf nodes in that folder item's subtree.

This section includes:

[Driver Behavior During Multipage Transfers](driver-behavior-during-multipage-transfers.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Multipage%20IStream%20Transfers%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


