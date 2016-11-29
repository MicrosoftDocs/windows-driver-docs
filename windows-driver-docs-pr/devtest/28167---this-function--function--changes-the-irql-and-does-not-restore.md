---
title: C28167
description: Warning C28167 The function changes the IRQL and does not restore the IRQL before it exits. It should be annotated to reflect the change or the IRQL should be restored.
ms.assetid: 289bb3c9-f9b2-4e7f-a406-22e365e5316a
keywords: ["warnings listed WDK PREfast for Drivers", "errors listed WDK PREfast for Drivers"]
---

# C28167


warning C28167: The function changes the IRQL and does not restore the IRQL before it exits. It should be annotated to reflect the change or the IRQL should be restored.

This warning indicates that the following conditions are true:

-   The function changes the IRQL at which the driver is running.

-   There is at least one path through a function that does not, by function exit, restore the IRQL to the original IRQL that the driver was running at function entry.

This warning occurs when an IRQL annotation on a function is required, but one doesn't exist.

To avoid this warning, the driver must correctly save the initial IRQL value and restore the same IRQL value at function exit if it did not intend to change the IRQL.

Functions that intentionally change the IRQL to a value that is different than the IRQL at which the driver was running at function entry should be annotated to indicate this behavior. For example, you could use the **\_IRQL\_raises\_**(*irql*) annotation to indicate that the function changes the IRQL from the IRQL at which the function was called. You could also save and restore the IRQL value and apply the corresponding annotations (**\_IRQL\_saves\_**, **\_IRQL\_restores\_**). The annotation will suppress this warning. For more information, see [IRQL annotations for drivers](irql-annotations-for-drivers.md). Functions that change the IRQL by mistake should be fixed.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20C28167%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




