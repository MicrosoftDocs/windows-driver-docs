---
title: Static and Dynamic Verification Tools
description: Static and Dynamic Verification Tools
ms.assetid: 8bdf1f11-5deb-427b-b058-b9173e167f8d
keywords: ["dynamic verification tools WDK", "static verification tools WDK"]
---

# Static and Dynamic Verification Tools


There are two basic types of verification tools:

-   **Static verification tools** examine the driver code without running the driver. Because these tools do not rely on tests that exercise the code, they can be extremely thorough. Theoretically, static verification tools can examine all of the driver code, including code paths that are rarely executed in practice. However, because the driver is not actually running, they could generate false-positive results. That is, they might report an error in a code path that might not occur in practice.

-   **Dynamic verification tools** examine the driver code while the driver is running, typically by intercepting calls to commonly used [driver support routines](https://msdn.microsoft.com/library/windows/hardware/ff544200) and substituting calls to their own error-checking versions of the same routines. Because the driver is actually running while the dynamic tools are doing the verification, false-positive results are rare. However, because the dynamic tools detect only the actions that occur while they are monitoring the driver, the tools can miss certain driver defects if the driver test coverage is not adequate. At the same time, by using information available at run time, for example, information that is harder to extract statically from the source code, dynamic verification tools can detect certain classes of driver errors that are harder to detect with static analysis tools.

The best practice is to use a combination of static and dynamic verification tools. Static tools allow you to check code paths that are difficult to exercise in practice, while the dynamic tools find serious errors that are occurring in the driver.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Static%20and%20Dynamic%20Verification%20Tools%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




