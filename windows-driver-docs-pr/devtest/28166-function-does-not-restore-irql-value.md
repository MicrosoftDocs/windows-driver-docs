---
title: C28166
description: Warning C28166 The function does not restore the IRQL to the value that was current at function entry and is required to do so.
ms.assetid: 5835b2e7-0a66-474c-ba1b-40618403075d
keywords: ["warnings listed WDK PREfast for Drivers", "errors listed WDK PREfast for Drivers"]
---

# C28166


warning C28166: The function does not restore the IRQL to the value that was current at function entry and is required to do so.

This warning indicates that a function has the **\_IRQL\_requires\_same\_** annotation and there is at least one path through the function that does not, by function exit, restore the IRQL to the IRQL at which the driver was running at function entry.

Typically, the **\_IRQL\_requires\_same\_** annotation is used on callback functions.

To avoid this warning, the driver must properly save the initial IRQL value and restore the same IRQL value at function exit, which is what the **\_IRQL\_requires\_same\_** annotation asserts.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20C28166%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




