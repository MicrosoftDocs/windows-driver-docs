---
title: Tools for Verifying Drivers
description: Tools for Verifying Drivers
keywords:
- tools WDK , verifying drivers
- driver development tools WDK , verifying drivers
- verifying drivers WDK
- driver verification WDK
ms.date: 07/02/2024
---

# Tools for verifying drivers

The Windows Driver Kit (WDK) includes several very comprehensive tools that are designed to help you detect and correct errors in driver code during the development process. Many of these tools can be used very early in the development process where they are most critical and can save you the most time and effort.

These verification tools are described in the WDK documentation and recommended for your use because each tool detects different types of driver errors in different ways. These tools are much more efficient than manual checks. These tools can detect errors that are not typically found in standard driver tests, and they embody the expertise of seasoned driver developers and Windows driver interface designers.

For best results, use all of the tools that can run on your driver. If you omit any of these tools, you might miss a serious bug in your driver.

> [!IMPORTANT]
> Windows Hardware Compatibility Program requires CodeQL for Static Tool Logo (STL) Tests on our Client and Server Operating Systems. We will continue to maintain support for SDV and CA on older products.  Partners are highly encouraged to review the CodeQL requirements for the [Static Tool Logo Test](/windows-hardware/test/hlk/testref/6ab6df93-423c-4af6-ad48-8ea1049155ae).
> For more information about using CodeQL, see [CodeQL and the Static Tools Logo Test](static-tools-and-codeql.md).

This section begins with a brief discussion of the characteristics of code verification tools and a survey of the tools included in the WDK and in Windows or available from Microsoft.

This section includes:

[Static and Dynamic Verification Tools](static-and-dynamic-verification-tools.md)

[CodeQL and the Static Tools Logo Test](static-tools-and-codeql.md)

[Driver Verifier](driver-verifier.md)

[DDI Compliance Rules](./static-driver-verifier-rules.md)

[Kernel Address Sanitizer](kasan.md)

## Other tools

If you have access to other code or driver verification tools (from other sources), we encourage you to use them in addition to the tools in the WDK. Be sure to use tools such as [Driver Verifier](driver-verifier.md) and the [Kernel Address Sanitizer](kasan.md) because of their specific knowledge of Windows drivers, but every tool looks at the code in different ways and can therefore help you find and fix different types of problems.
