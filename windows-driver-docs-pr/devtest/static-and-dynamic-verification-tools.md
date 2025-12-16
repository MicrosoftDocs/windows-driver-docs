---
title: Driver Verification Tools for Windows Development
description: "Learn about Windows Driver Kit (WDK) verification tools including CodeQL, Driver Verifier, and KASAN. Detect driver errors early in development."
keywords:
- dynamic verification tools WDK
- static verification tools WDK
ms.date: 12/15/2025
ms.topic: concept-article
---

# Tools for verifying drivers

The Windows Driver Kit (WDK) provides driver verification tools that help you detect and correct errors during development. These tools include static analysis tools like CodeQL and dynamic tools like Driver Verifier that can find critical bugs before deployment. Using these verification tools early in development saves time and prevents serious driver issues in production.

The WDK documentation describes these verification tools and recommends their use because each tool detects different types of driver errors in different ways. These tools are much more efficient than manual checks. They can detect errors that aren't typically found in standard driver tests, and they embody the expertise of seasoned driver developers and Windows driver interface designers.

For best results, use all of the tools that can run on your driver. If you omit any of these tools, you might miss a serious bug in your driver.

## Static and dynamic verification tools

There are two basic types of verification tools:

- **Static verification tools** examine the driver code without running the driver. Because these tools don't rely on tests that exercise the code, they can be extremely thorough. Theoretically, static verification tools can examine all of the driver code, including code paths that are rarely executed in practice. However, because the driver isn't actually running, these tools might generate false-positive results. That is, they might report an error in a code path that doesn't occur in practice.

    [CodeQL](codeql-overview.md) is the primary static analysis tool for drivers. CodeQL provides a powerful query language that treats code as a database to be queried, making it simple to write queries for specific behaviors and patterns. The [Windows Hardware Compatibility Program](/windows-hardware/design/compatibility) requires CodeQL for Static Tool Logo (STL) Tests on our Client and Server operating systems. For more information, see [CodeQL and the Static Tools Logo Test](static-tools-and-codeql.md).

- **Dynamic verification tools** examine the driver code while the driver is running, typically by intercepting calls to commonly used driver support routines and substituting calls to their own error-checking versions of the same routines. Because the driver is actually running while the dynamic tools are doing the verification, false-positive results are rare. However, because the dynamic tools detect only the actions that occur while they're monitoring the driver, the tools can miss certain driver defects if the driver test coverage isn't adequate. At the same time, by using information available at run time - for example, information that's harder to extract statically from the source code - dynamic verification tools can detect certain classes of driver errors that are harder to detect with static analysis tools.

Use a combination of static and dynamic verification tools. Static tools allow you to check code paths that are difficult to exercise in practice, while the dynamic tools find serious errors that are occurring in the driver.

## Overview of verification tools

> [!IMPORTANT]
> The Static Driver Verifier (SDV) tool is no longer supported. It's unavailable in WDKs newer than build 26017, including the Windows 24H2 RTM WDK. Using the SDV for analysis is not recommended.

The WDK describes the following verification tools and recommends their use by driver developers and testers. They're listed in the order in which you typically use them.

### After the code compiles

- CodeQL is a powerful semantic code analysis engine. The combination of an extensive suite of high-value security queries and a robust platform makes it an invaluable tool for securing driver code. For more information, see [CodeQL and the Static Tools Logo Test](static-tools-and-codeql.md).

### When the driver runs

Use the following dynamic verification tools as soon as the driver is built and is running without obvious errors.

- [Driver Verifier](driver-verifier.md) is a dynamic verification tool written especially for Windows drivers. It includes multiple tests that you can run on several drivers simultaneously. Driver Verifier is so effective at finding serious bugs in drivers that experienced driver developers and testers configure it to run whenever their driver runs in a development or test environment. Driver Verifier is included in Windows. When you enable Driver Verifier for a driver, you must also run multiple tests on the driver. Driver Verifier can detect certain driver bugs that are difficult to detect by using static verification tools alone. Examples of these types of bugs include the following:

  - **Kernel pool buffer overruns.** When the verified driver allocates pool memory buffers, Driver Verifier guards them by using a non-accessible memory page. If the driver tries to use memory past the end of the buffer, Driver Verifier initiates a bug check.

  - **Using memory after freeing it.** Special pool memory blocks use their own memory page and don't share memory pages with other allocations. When the driver frees the block of pool memory, the corresponding memory page becomes non-accessible. If the driver attempts to use that memory after freeing it, the driver crashes instantly.

  - **Using pageable memory while running at elevated IRQL.** When a verified driver raises the IRQL at DISPATCH\_LEVEL or higher, Driver Verifier trims all pageable memory from the system working set, simulating a system under memory pressure. The driver crashes if it tries to use one of these pageable virtual addresses.

  - **Low Resources Simulation.** To simulate a system under low resources conditions, Driver Verifier can fail various operating system kernel APIs that drivers call.

  - **Memory leaks.** Driver Verifier tracks memory allocations made by a driver and makes sure the driver frees the memory before it gets unloaded.

  - **I/O operations that take too much time to complete or to be canceled.** Driver Verifier can test the driver's logic for responding to `STATUS_PENDING` return values from [**IoCallDriver**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocalldriver).

  - **DDI Compliance Checking.** (Available starting with Windows 8) Driver Verifier applies a set of device driver interface (DDI) rules that check for the proper interaction between a driver and the kernel interface of the operating system.

- The [Kernel Address Sanitizer](kasan.md) (KASAN) is a bug detection technology supported on Windows drivers that enables you to detect several classes of illegal memory accesses, such as buffer overflows and use-after-free events.

- [Application Verifier](application-verifier.md) is a dynamic verification tool for user-mode applications and drivers written in C or C++. It doesn't verify managed code.

## Related topics

- [CodeQL and the Static Tools Logo Test](static-tools-and-codeql.md)
- [Driver Verifier](driver-verifier.md)
- [DDI Compliance Rules](./static-driver-verifier-rules.md)
- [Kernel Address Sanitizer](kasan.md)
- [Application Verifier](application-verifier.md)