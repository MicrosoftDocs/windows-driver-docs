---
title: WIA Item Tree Architecture
description: WIA Item Tree Architecture
ms.assetid: 7e0f2b65-7150-4f8a-9780-abdaf93e44d6
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# WIA Item Tree Architecture





The WIA item tree that an application can see is separate from the tree that is created and maintained by a WIA minidriver. When a minidriver creates a tree of items, the WIA service uses this WIA item tree as a guide to create identical copies that can be viewed by imaging applications. Items in the copied tree are called application items. Items in the tree created by a minidriver are called driver items.

More information is available in the following sections:

[Application Items and Driver Items](application-items-and-driver-items.md)

[Describing a WIA Device Using WIA Items](describing-a-wia-device-using-wia-items.md)

[Changing the WIA Item Tree Structure](changing-the-wia-item-tree-structure.md)

 

 




