---
title: Object Handle and Event Order
author: windows-driver-content
description: Object Handle and Event Order
ms.assetid: 5abbcda2-66cc-4460-99b6-e7796e65af68
---

# Object Handle and Event Order


## <a href="" id="ddk-object-handle-and-event-order-si"></a>


When the Microsoft PTP WIA minidriver issues the **GetObjectHandles** command (see the PIMA 15740 standard), the camera must return the object handles in a specific order for the WIA Minidriver to build the WIA item tree correctly.

-   Objects that have child objects must appear in the list before their children.

    The numerical order of the handles does not matter. As an example, if object 5 has child objects 4, 6, and 7, the list should be ordered 5, 4, 6, 7. The ordering 4, 5, 6, 7 will not work.

-   For ancillary associations, the image object must be located in the object handle list ahead of the other objects in the association.

-   ObjectRemoved events (see the PIMA 15740 standard) must occur in a bottom-up order.

    In other words, an ObjectRemoved event for an object should not occur until all of its children have been removed as a result of ObjectRemoved events. If the image inside an ancillary association is to be removed, the other objects in the association must be removed in response to ObjectRemoved events before the image itself is removed.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Object%20Handle%20and%20Event%20Order%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


