---
title: Multipage IStream Transfers
description: Multipage IStream Transfers
ms.assetid: 0d17cfa8-f200-4d87-a2cb-cfd8dbc24e1e
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Multipage IStream Transfers


Typically, when a data transfer is requested on an item, the data from that item is transferred, using the settings that the item's properties specify. For example, if an application is on the "Flatbed" item for a scanner, a data transfer will result in a scan from the Flatbed, using the settings that are stored in the WIA properties on the "Flatbed" item.

However, in Windows Vista, another type of transfer is available: a multi-item transfer, also known as *folder acquisition*. In this kind of transfer, an application requests a transfer from a folder item by using a specified flag (WIA\_TRANSFER\_ACQUIRE\_CHILDREN), and the transfer results in a transfer from each of the leaf nodes in that folder item's subtree.

This section includes:

[Driver Behavior During Multipage Transfers](driver-behavior-during-multipage-transfers.md)

 

 




