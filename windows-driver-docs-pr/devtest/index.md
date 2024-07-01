---
title: Driver Development Tools
description: Driver Development Tools
ms.assetid: 1d384d73-d1d2-445f-8077-40eed1f99a8c
keywords:
- tools WDK
- driver development tools WDK
- WsdCodeGen tool WDK
- tools WDK , developing drivers
- Web Services for Devices WDK WIA , tools
ms.date: 06/26/2024
ms.topic: article
---

# Driver Development Tools

## Purpose

The Windows Driver Kit (WDK) provides a set of tools that you can use to develop, analyze, build, install, and test your driver. The WDK includes powerful verification tools that are designed to help you detect, analyze, and correct errors in driver code during the development process. Many of these tools can be used very early in the development process where they are most critical and can save you the most time and effort.

## Driver Development Tools Documentation

This section describes the tools and techniques that can help you during development:

<a href="tools-for-verifying-drivers.md" data-raw-source="[Tools for Verifying Drivers](tools-for-verifying-drivers.md)">Tools for Verifying Drivers</a>

<a href="additional-driver-verification-tools.md" data-raw-source="[Additional Driver Verification Tools](additional-driver-verification-tools.md)">Additional Driver Verification Tools</a>

<a href="tools-for-testing-drivers.md" data-raw-source="[Tools for Testing Drivers](tools-for-testing-drivers.md)">Tools for Testing Drivers</a>

<a href="tools-for-software-tracing.md" data-raw-source="[Tools for Software Tracing](tools-for-software-tracing.md)">Tools for Software Tracing</a>

<a href="additional-driver-tools.md" data-raw-source="[Additional Driver Tools](additional-driver-tools.md)">Additional Driver Tools</a>

<a href="/windows-hardware/drivers/develop/validating-windows-drivers#apivalidator" data-raw-source="[ApiValidator](/windows-hardware/drivers/develop/validating-windows-drivers#apivalidator)">ApiValidator</a>
You can use the ApiValidator.exe tool to verify that the APIs that your driver calls are valid for a Universal Windows driver.

<a href="/windows-hardware/drivers/develop/" data-raw-source="[Developing, Testing, and Deploying Drivers](/windows-hardware/drivers/develop/)">Developing, Testing, and Deploying Drivers</a>

> [!IMPORTANT]
> Windows Hardware Compatibility Program requires CodeQL for Static Tool Logo (STL) Tests on our Client and Server Operating Systems. We will continue to maintain support for SDV and CA on older products.  Partners are highly encouraged to review the CodeQL requirements for the [Static Tool Logo Test](/windows-hardware/test/hlk/testref/6ab6df93-423c-4af6-ad48-8ea1049155ae).
> For more information about using CodeQL, see [CodeQL and the Static Tools Logo Test](static-tools-and-codeql.md).