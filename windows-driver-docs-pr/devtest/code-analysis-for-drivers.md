---
title: Code Analysis for Drivers
description: Code Analysis for Drivers is a compile-time static verification tool that detects basic coding errors in C and C++ programs.
ms.date: 07/02/2024
ms.topic: concept-article
---

# Code Analysis for Drivers

Code Analysis for Drivers is a compile-time static verification tool that detects basic coding errors in C and C++ programs and includes a specialized module that is designed to detect errors in (primarily) kernel-mode driver code.

In previous versions of the WDK, the driver-specific module for code analysis was part of a stand-alone tool called PREfast for Drivers (PFD). PREfast for Drivers was also integrated into the WDK Build environment, as part of Microsoft Automated Code Review (OACR). Starting with Windows Driver Kit (WDK) 8, the driver-specific features have been integrated with the [Analyzing Application Quality by Using Code Analysis Tools](/previous-versions/visualstudio/visual-studio-2013/dd264897(v=vs.120)).

> [!IMPORTANT]
> Windows Hardware Compatibility Program requires CodeQL for Static Tool Logo (STL) Tests on our Client and Server Operating Systems. We will continue to maintain support for SDV and CA on older products.  Partners are highly encouraged to review the CodeQL requirements for the [Static Tool Logo Test](/windows-hardware/test/hlk/testref/6ab6df93-423c-4af6-ad48-8ea1049155ae).
> For more information about using CodeQL, see [CodeQL and the Static Tools Logo Test](static-tools-and-codeql.md).

## In this section

- [Code Analysis for drivers overview](code-analysis-for-drivers-overview.md)
- [How to run Code Analysis for drivers](how-to-run-code-analysis-for-drivers.md)
- [SAL 2 Annotations for Windows Drivers](sal-2-annotations-for-windows-drivers.md)
- [Code Analysis for Drivers Warnings](prefast-for-drivers-warnings.md)

> [!IMPORTANT]
> Code Analysis for drivers is available in the Windows 24H2 WDK and EWDK, but be advised that it is set to be retired at a future date. <br>
> Going forward, CodeQL will be the primary static analysis tool for drivers. CodeQL provides a powerful query language that treats code as a database to be queried, making it simple to write queries for specific behaviors, patterns, and more.
> For more information about using CodeQL, see [CodeQL and the Static Tools Logo Test](static-tools-and-codeql.md).

