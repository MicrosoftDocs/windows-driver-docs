---
title: CodeQL FAQ for the Windows Hardware Compatibility Program.
description: Learn about CodeQL testing requirements for the Windows Hardware Compatibility Program. Improve driver certification with these FAQs.
keywords:
- dynamic verification tools WDK
- static verification tools WDK
ms.date: 05/13/2025
---

# CodeQL FAQs for Windows Hardware Compatibility Program

This article answers frequently asked questions about CodeQL testing requirements for the Windows Hardware Compatibility Program. Learn how CodeQL improves driver certification and ensures high-security standards.

## When is CodeQL required for device certification?

See the [Windows Hardware Compatibility Program Certification Process](/windows-hardware/design/compatibility/whcp-certification-process) for requirement details.

## hy is CodeQL required for driver source code?

The motivation for requiring CodeQL on driver source code is based on two main reasons:

1. Improving Windows security by ensuring that components certified by Microsoft meet high-security standards.

1. Providing the hardware ecosystem with high-quality tooling actively developed by Microsoft's security engineers.

## What types of drivers do CodeQL and the Static Tools Logo test apply to?

Currently, the Static Tools Logo test requires running CodeQL and passing the **Must-Fix** set of queries for all kernel-mode drivers, except graphics drivers.

Running CodeQL on graphics drivers is **highly recommended**, even though it isn't currently required. Some queries can also identify useful defects in user-mode components.

## Which license governs the usage of CodeQL for driver developers?

Using CodeQL for WHCP testing is allowed under the **[Hardware Lab Kit (HLK)](/windows-hardware/test/hlk/) End User License Agreement**.

For WHCP participants, the HLK's EULA overwrites GitHub's CodeQL Terms and Conditions. The HLK EULA states that CodeQL **can be used** during automated analysis, CI or CD, as part of normal engineering processes for the purposes of analyzing drivers to be submitted and certified as part of the WHCP.

## Do I need to use Visual Studio or msbuild to run CodeQL?

CodeQL **does not require MSBuild or Visual Studio to be used**.

See [supported languages and frameworks](https://codeql.github.com/docs/codeql-overview/supported-languages-and-frameworks/) for a list of which compilers are supported.

## How does the HLK verify that my driver was scanned by CodeQL?

The Static Tools Logo Test in the HLK is the test that enforces this requirement.

Details on the Static Tools Logo Test can be found on its [MS Docs page](/windows-hardware/test/hlk/testref/6ab6df93-423c-4af6-ad48-8ea1049155ae).

## Are all defects reported by CodeQL true defects?

Every CodeQL query has varying levels of precision.

Our goal is to minimize false positives, but occasionally they will occur. Our suite of **Must-Fix** queries have been developed and hand-picked for use with the WHCP program because our extensive testing results in nearly zero false positives.

If you are seeing false positives from a query in the set of **Must-Fix** queries, email `stlogohelp@microsoft.com` immediately or file an issue on the [Windows-Driver-Developer-Supplemental-Tools repo](https://github.com/microsoft/Windows-Driver-Developer-Supplemental-Tools/issues), and we will work to get it resolved as soon as possible.

## Does a query's classification of either "warning" or "error" matter for the purposes of the Static Tools Logo Test?

CodeQL classifies queries as *error*, *warning*, or *problem*, but this classification is separate from how the Windows Hardware Compatibility Program and the Static Tools Logo Test grade the results.

Drivers with defects in any **Must-Fix** query don't pass the Static Tools Logo Test and fail certification, regardless of the query classification (for example, *warning*).

## Can I generate a DVL on Visual Studio solutions?

No, DVL generation must be run at the project level and cannot be run on [Visual Studio solutions](/visualstudio/get-started/tutorial-projects-solutions).

For full instructions to generate a DVL, see [Creating a Driver Verification Log](../develop/creating-a-driver-verification-log.md).

## Can I generate a Driver Verification Log (DVL) outside of the context of msbuild or Visual Studio?

As part of the Windows Driver Kit (WDK) and Enterprise WDK (eWDK), Microsoft ships a component called *dvl.exe* which can be used to generate Driver Verification Logs (DVLs).

In WDK/eWDK preview versions 21342 and later, you can generate a DVL from the command line without using msbuild or Visual Studio by specifying a driver name and architecture.

See [Creating a Driver Verification Log](../develop/creating-a-driver-verification-log.md) for more details.

## I have comments or questions around how to use CodeQL on my driver, where do I send feedback?

Send your feedback and questions to [stlogohelp@microsoft.com](mailto:stlogohelp@microsoft.com).

## Related Content

- [Run the CodeQL analysis on your driver code](./static-tools-and-codeql.md)

- [CodeQL overview](./codeql-overview.md)

- [CodeQL queries and suites](./codeql-queries.md)