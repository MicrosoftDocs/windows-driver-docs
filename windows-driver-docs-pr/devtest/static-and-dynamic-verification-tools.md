---
title: Static and Dynamic Verification Tools
description: Static and Dynamic Verification Tools
ms.assetid: 8bdf1f11-5deb-427b-b058-b9173e167f8d
keywords:
- dynamic verification tools WDK
- static verification tools WDK
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Static and Dynamic Verification Tools


There are two basic types of verification tools:

-   **Static verification tools** examine the driver code without running the driver. Because these tools do not rely on tests that exercise the code, they can be extremely thorough. Theoretically, static verification tools can examine all of the driver code, including code paths that are rarely executed in practice. However, because the driver is not actually running, they could generate false-positive results. That is, they might report an error in a code path that might not occur in practice.

-   **Dynamic verification tools** examine the driver code while the driver is running, typically by intercepting calls to commonly used [driver support routines](https://msdn.microsoft.com/library/windows/hardware/ff544200) and substituting calls to their own error-checking versions of the same routines. Because the driver is actually running while the dynamic tools are doing the verification, false-positive results are rare. However, because the dynamic tools detect only the actions that occur while they are monitoring the driver, the tools can miss certain driver defects if the driver test coverage is not adequate. At the same time, by using information available at run time, for example, information that is harder to extract statically from the source code, dynamic verification tools can detect certain classes of driver errors that are harder to detect with static analysis tools.

The best practice is to use a combination of static and dynamic verification tools. Static tools allow you to check code paths that are difficult to exercise in practice, while the dynamic tools find serious errors that are occurring in the driver.

 

 





