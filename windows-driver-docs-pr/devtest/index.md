---
title: Driver Development Tools for Windows
description: Learn about Windows Driver Kit (WDK) tools for developing, testing, and verifying drivers. Includes verification, tracing, and testing tools.
ms.assetid: 1d384d73-d1d2-445f-8077-40eed1f99a8c
keywords:
- tools WDK
- driver development tools WDK
- WsdCodeGen tool WDK
- tools WDK , developing drivers
- Web Services for Devices WDK WIA , tools
ms.date: 12/15/2025
ms.topic: overview
---

# Driver development tools

## Purpose

Windows Driver Kit (WDK) provides driver development tools that help you build, test, and verify Windows drivers. The WDK includes verification tools to detect and correct driver code errors early in development, saving time and effort. Use these tools to analyze, install, and test drivers throughout the development process.

## Driver development tools documentation

This section describes the tools and techniques that can help you during development:

- [Tools for Verifying Drivers](static-and-dynamic-verification-tools.md)

- [Additional Driver Verification Tools](additional-driver-verification-tools.md)

- [Tools for Testing Drivers](static-and-dynamic-verification-tools.md)

- [Tools for Software Tracing](tools-for-software-tracing.md)

- [Additional Driver Tools](additional-driver-tools.md)

- [ApiValidator](/windows-hardware/drivers/develop/validating-windows-drivers#apivalidator)
You can use the ApiValidator.exe tool to verify that the APIs that your driver calls are valid for a Universal Windows driver.

- [Developing, Testing, and Deploying Drivers](/windows-hardware/drivers/develop/)

> [!IMPORTANT]
> The Windows Hardware Compatibility Program requires CodeQL for Static Tool Logo (STL) Tests on our Client and Server Operating Systems. The program continues to maintain support for SDV and CA on older products. Partners are highly encouraged to review the CodeQL requirements for the [Static Tool Logo Test](/windows-hardware/test/hlk/testref/6ab6df93-423c-4af6-ad48-8ea1049155ae).
> For more information about using CodeQL, see [CodeQL and the Static Tools Logo Test](static-tools-and-codeql.md).