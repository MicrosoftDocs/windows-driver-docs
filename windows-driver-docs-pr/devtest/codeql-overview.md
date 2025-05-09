---
title: CodeQL and the Static Tools Logo Test Overview
description: Overview for the CodeQL tests required for the Windows Hardware Compatibility Program.
keywords:
- dynamic verification tools WDK
- static verification tools WDK
ms.date: 05/09/2025
---

# CodeQL and the Static Tools Logo Test

Microsoft is committed to mitigating the attack surface for the Windows operating system, and ensuring that third party drivers meet a strong security bar is critical to accomplishing that goal. One step in setting this security bar is the requirement to the [Windows Hardware Compatibility Program](/windows-hardware/design/compatibility) (WHCP) which states that all driver submissions must use the [CodeQL](https://codeql.github.com/) engine on driver source code and fix any violations that are deemed *Must-Fix* .

## CodeQL Concepts

CodeQL is a static analysis engine used by developers to perform security analysis on code outside of a live environment. CodeQL ingests code while it is compiling, and builds a database from it. The database becomes a directory containing queryable data, a source reference, and log files. Once the database is built, one can run analysis on it by utilizing CodeQL queries (also called checks or rules) which will determine if the source code contains violations or security vulnerabilities. CodeQL provides a library of standard queries which check for language correctness, semantics, and provides great value to developers who wish to ensure their code is free of bugs and vulnerabilities.

CodeQL also provides the option to build custom queries. For more information on writing custom queries, see [Writing queries](https://codeql.github.com/docs/writing-codeql-queries/codeql-queries/) in the CodeQL docs.

CodeQL also provides a [CodeQL command line tool (CLI)](https://codeql.github.com/docs/codeql-cli/) to easily perform CodeQL actions and/or perform large scale analysis.

Supplementary CodeQL CLI documentation can be found at [CodeQL Getting Started](https://codeql.github.com/docs/codeql-cli/getting-started-with-the-codeql-cli/).

## CodeQL and Driver Security

[CodeQL](https://codeql.github.com/), by GitHub, is a powerful semantic code analysis engine, and the combination of an extensive suite of high-value security queries along with a robust platform make it an invaluable tool for securing driver code.

Usage of CodeQL for the purpose of WHCP testing is acceptable under the **[Hardware Lab Kit (HLK)](/windows-hardware/test/hlk/) End User License Agreement**. For WHCP participants, the HLK's EULA overwrites GitHub's CodeQL Terms and Conditions by stating that CodeQL **can be used** during automated analysis, CI or CD, as part of normal engineering processes for the purposes of analyzing drivers to be submitted and certified as part of the WHCP.

This requirement to analyze driver source code and fix any *Must-Fix* violations is enforced by the [Static Tools Logo Test](/windows-hardware/test/hlk/testref/6ab6df93-423c-4af6-ad48-8ea1049155ae).

> [!IMPORTANT]
> Windows Hardware Compatibility Program requires CodeQL for Static Tool Logo (STL) Tests on our Client and Server Operating Systems. We will continue to maintain support for SDV and CA on older products. Partners are highly encouraged to review the CodeQL requirements for the [Static Tool Logo Test](/windows-hardware/test/hlk/testref/6ab6df93-423c-4af6-ad48-8ea1049155ae).

### HLK EULA and CodeQL

Usage of CodeQL for the purpose of certifying for the Windows Hardware Compatibility Program testing is acceptable under the [Hardware Lab Kit (HLK)](/windows-hardware/test/hlk/) End User License Agreement. For WHCP participants, the HLK's EULA overwrites GitHub's CodeQL Terms and Conditions. The HLK EULA states that CodeQL can be used during automated analysis, CI or CD, as part of normal engineering processes for the purposes of analyzing drivers to be submitted and certified as part of the Windows Hardware Compatibility Program. For those following along for general use, read the [GitHub CodeQL Terms and Conditions](https://github.com/github/codeql-cli-binaries/blob/main/LICENSE.md) and/or [contact CodeQL](https://support.github.com/contact).

## Related Content

- [Run the CodeQL analysis on your driver code](./static-tools-and-codeql.md)
- [Frequently Asked Questions for CodeQL tests](./codeql-faq.md)
- [CodeQL Queries and Suites](./codeql-queries.md)


