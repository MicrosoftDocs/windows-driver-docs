---
title: Object Handle and Event Order
description: Object Handle and Event Order
ms.assetid: 5abbcda2-66cc-4460-99b6-e7796e65af68
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Object Handle and Event Order





When the Microsoft PTP WIA minidriver issues the **GetObjectHandles** command (see the PIMA 15740 standard), the camera must return the object handles in a specific order for the WIA Minidriver to build the WIA item tree correctly.

-   Objects that have child objects must appear in the list before their children.

    The numerical order of the handles does not matter. As an example, if object 5 has child objects 4, 6, and 7, the list should be ordered 5, 4, 6, 7. The ordering 4, 5, 6, 7 will not work.

-   For ancillary associations, the image object must be located in the object handle list ahead of the other objects in the association.

-   ObjectRemoved events (see the PIMA 15740 standard) must occur in a bottom-up order.

    In other words, an ObjectRemoved event for an object should not occur until all of its children have been removed as a result of ObjectRemoved events. If the image inside an ancillary association is to be removed, the other objects in the association must be removed in response to ObjectRemoved events before the image itself is removed.

 

 




