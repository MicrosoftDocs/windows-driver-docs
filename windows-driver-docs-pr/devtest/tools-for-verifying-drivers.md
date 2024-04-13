---
title: Tools for Verifying Drivers
description: Tools for Verifying Drivers
keywords:
- tools WDK , verifying drivers
- driver development tools WDK , verifying drivers
- verifying drivers WDK
- driver verification WDK
ms.date: 02/18/2022
---

# Tools for verifying drivers

The Windows Driver Kit (WDK) includes several very comprehensive tools that are designed to help you detect and correct errors in driver code during the development process. Many of these tools can be used very early in the development process where they are most critical and can save you the most time and effort.

These verification tools are described in the WDK documentation and recommended for your use because each tool detects different types of driver errors in different ways. These tools are much more efficient than manual checks. These tools can detect errors that are not typically found in standard driver tests, and they embody the expertise of seasoned driver developers and Windows driver interface designers.

For best results, use all of the tools that can run on your driver. If you omit any of these tools, you might miss a serious bug in your driver.

This section begins with a brief discussion of the characteristics of code verification tools and a survey of the tools included in the WDK and in Windows or available from Microsoft.

This section includes:

[Static and Dynamic Verification Tools](static-and-dynamic-verification-tools.md)

[Code Analysis for Drivers](code-analysis-for-drivers.md)

[Driver Verifier](driver-verifier.md)

[Static Driver Verifier](static-driver-verifier.md)

[DDI Compliance Rules](./static-driver-verifier-rules.md)

[CodeQL and the Static Tools Logo Test](static-tools-and-codeql.md)

## Other tools

If you have access to other code or driver verification tools (from other sources), we encourage you to use them in addition to the tools in the WDK. Be sure to use [Code Analysis for Drivers](code-analysis-for-drivers.md), [Static Driver Verifier](static-driver-verifier.md), and [Driver Verifier](driver-verifier.md) because of their specific knowledge of Windows drivers, but every tool looks at the code in different ways and can therefore help you find and fix different types of problems.
