---
title: HID Collections
description: A HID collection is a meaningful grouping of HID controls and their respective HID usages.
ms.assetid: 2d3efb38-4eba-43db-8cff-9fac30209952
keywords:
- Human Interface Devices WDK , collections
- HID WDK , collections
- interactive input devices WDK , collections
- input devices WDK , collections
- collections WDK HID
- collections WDK HID , about HID collections
- subcollections WDK HID
- Human Interface Devices WDK , controls
- HID WDK , controls
- interactive input devices WDK , controls
- input devices WDK , controls
- controls WDK HID
- HID collections WDK
- HID collections WDK , about HID collections
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# HID Collections


A *HID collection* is a meaningful grouping of HID controls and their respective [HID usages](hid-usages.md).

Controls should be grouped together if they are logically related or are functionally dependent on one another. For instance, a SHIFT key and a letter key on a keyboard should not belong to separate collections. Collections can have nested *subcollections*, also referred to as [link collections](link-collections.md). Report descriptors define one or more [top-level collections](top-level-collections.md), and the report items, associated with each collection, define one or more HID reports.




Windows extends the concept of a HID collection to include the following:

[Top-level collections](top-level-collections.md)

[Top-level collections opened by Windows for system use](top-level-collections-opened-by-windows-for-system-use.md)

[Preparsed data](preparsed-data.md)

[Link collections](link-collections.md)

[Collection capability](collection-capability.md)

[Button capability arrays](button-capability-arrays.md)

[Value capability arrays](value-capability-arrays.md)

[Data indices](data-indices.md)

 

 




