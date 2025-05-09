---
title: CodeQL FAQ
description: Frequently asked questions for the CodeQL testing requirements for the Windows Hardware Compatibility Program.
keywords:
- dynamic verification tools WDK
- static verification tools WDK
ms.date: 05/09/2025
---

# Frequently Asked Questions for CodeQL tests

## When will this be required for device certification?

See the [Windows Hardware Compatibility Program Certification Process](/windows-hardware/design/compatibility/whcp-certification-process) to for requirement details.

## What is the motivation behind requiring CodeQL be run on driver source code?

The motivation for requiring CodeQL to be run on driver source code can be summarized by two main reasons:

1. Security of Windows is paramount and requiring CodeQL to be run on driver source code is one step in helping improve the security of components which get certified by Microsoft.
1. CodeQL queries are actively developed by security engineers at Microsoft, as Microsoft is committed to ensuring that its hardware ecosystem benefits from the same high-quality tooling that is used at Microsoft.

## What types of drivers do CodeQL and the Static Tools Logo test apply to?

At present, the Static Tools Logo test requires that CodeQL be run and the *Must-Fix* set of queries passed for all kernel-mode drivers excluding graphics drivers. Note that running CodeQL on graphics drivers is **highly recommended** even though it is not currently required. Some queries may also find useful defects in user-mode components.

We anticipate extending the test and its queries to require results for graphics drivers, user-mode drivers and driver components, and other driver package components in the future. If you encounter unexpected behavior or false positives running CodeQL on graphics drivers or user-mode drivers, please file an issue on the [Windows-Driver-Developer-Supplemental-Tools repo](https://github.com/microsoft/Windows-Driver-Developer-Supplemental-Tools).

## Which license governs the usage of CodeQL for driver developers?

Usage of CodeQL for the purpose of WHCP testing is acceptable under the **[Hardware Lab Kit (HLK)](/windows-hardware/test/hlk/) End User License Agreement**. For WHCP participants, the HLK's EULA overwrites GitHub's CodeQL Terms and Conditions. The HLK EULA states that CodeQL **can be used** during automated analysis, CI or CD, as part of normal engineering processes for the purposes of analyzing drivers to be submitted and certified as part of the WHCP.

## Do I need to use Visual Studio or msbuild to run CodeQL?

CodeQL **does not require MSBuild or Visual Studio to be used**. See [supported languages and frameworks](https://codeql.github.com/docs/codeql-overview/supported-languages-and-frameworks/) for a list of which compilers are supported.

## How does the HLK verify that my driver was scanned by CodeQL?

The Static Tools Logo Test in the HLK is the test that enforces this requirement. Details on the Static Tools Logo Test can be found on its [MS Docs page](/windows-hardware/test/hlk/testref/6ab6df93-423c-4af6-ad48-8ea1049155ae).

## Are all defects reported by CodeQL true defects?

Every CodeQL query has varying levels of precision. Our goal is to minimize false positives, but occasionally they will occur. Our suite of *Must-Fix*  queries have been developed and hand-picked for use with the WHCP program because our extensive testing results in nearly zero false positives. If you are seeing false positives from a query in the set of *Must-Fix*  queries, email `stlogohelp@microsoft.com` immediately or file an issue on the [Windows-Driver-Developer-Supplemental-Tools repo](https://github.com/microsoft/Windows-Driver-Developer-Supplemental-Tools/issues), and we will work to get it resolved as soon as possible.

## Does a query's classification of either "warning" or "error" matter for the purposes of the Static Tools Logo Test?

Queries are classified using statuses such as *error*, *warning*, or *proble* in CodeQL but this classification is separate from how the Windows Hardware Compatibility Program and specifically the Static Tools Logo Test will grade the results. Any driver with defects from any query within the *Must-Fix*  suite will **not pass** the Static Tools Logo Test and will **fail to be certified**, regardless of the query classification in the raw query file (for example, *warning*).

## Can I generate a DVL on Visual Studio solutions?

No, DVL generation must be run at the project level and cannot be run on [Visual Studio solutions](/visualstudio/get-started/tutorial-projects-solutions). Instructions for how to generate a DVL can be found at: [Creating a Driver Verification Log](../develop/creating-a-driver-verification-log.md).

## Can I generate a Driver Verification Log (DVL) outside of the context of msbuild or Visual Studio?

As part of the Windows Driver Kit (WDK) and Enterprise WDK (eWDK), Microsoft ships a component called *dvl.exe* which can be used to generate Driver Verification Logs (DVLs). Starting in WDK/eWDK preview versions 21342 and later, it is possible to generate a DVL from the command line outside of the context of msbuild or Visual Studio by passing a driver name and architecture. See [Creating a Driver Verification Log](../develop/creating-a-driver-verification-log.md) for more details.

## I have comments or questions around how to use CodeQL on my driver, where do I send feedback?

Send feedback and questions to [stlogohelp@microsoft.com](mailto:stlogohelp@microsoft.com). 

## Related Content

- [Run the CodeQL analysis on your driver code](./static-tools-and-codeql.md)
- [CodeQL Overview](./codeql-overview.md)
- [CodeQL Queries and Suites](./codeql-queries.md)