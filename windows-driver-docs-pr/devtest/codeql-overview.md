---
title: "CodeQL and Static Tools Logo Test: Overview and Benefits"
description: Learn how CodeQL tests improve driver security for the Windows Hardware Compatibility Program. Ensure compliance with WHCP requirements.
keywords:
- dynamic verification tools WDK
- static verification tools WDK
ms.date: 05/13/2025
ms.topic: overview
---

# CodeQL and Static Tools Logo Test Overview

earn how CodeQL helps reduce the attack surface for Windows by ensuring third-party drivers meet strong security standards. This article explains the benefits of using CodeQL for WHCP compliance.

One step in setting this security bar is the requirement to the [Windows Hardware Compatibility Program](/windows-hardware/design/compatibility) (WHCP) which states that all driver submissions must use the [CodeQL](https://codeql.github.com/) engine on driver source code and fix any violations that are deemed **Must-Fix**.

## Understanding CodeQL concepts

CodeQL is a static analysis engine used by developers to perform security analysis on code outside of a live environment. 

CodeQL ingests code during compilation and builds a database from it. The database becomes a directory containing queryable data, a source reference, and log files. Once the database is built, one can run analysis on it by utilizing CodeQL queries (also called checks or rules) which will determine if the source code contains violations or security vulnerabilities. 

CodeQL provides a library of standard queries that check for language correctness and semantics, offering great value to developers who want to ensure their code is free of bugs and vulnerabilities.

CodeQL also provides the option to build custom queries. 

To learn more about writing custom queries, see [Writing queries](https://codeql.github.com/docs/writing-codeql-queries/codeql-queries/) in the CodeQL documentation.

CodeQL also provides a [CodeQL command-line tool (CLI)](https://codeql.github.com/docs/codeql-cli/) to perform CodeQL actions or large-scale analysis.

Find additional CodeQL CLI documentation at [CodeQL Getting Started](https://codeql.github.com/docs/codeql-cli/getting-started-with-the-codeql-cli/).

## How CodeQL Enhances Driver Security

[CodeQL](https://codeql.github.com/), by GitHub, is a powerful semantic code analysis engine, and the combination of an extensive suite of high-value security queries along with a robust platform make it an invaluable tool for securing driver code.

Using CodeQL for WHCP testing is allowed under the **[Hardware Lab Kit (HLK)](/windows-hardware/test/hlk/) End User License Agreement**. 

For WHCP participants, the HLK's EULA overwrites GitHub's CodeQL Terms and Conditions by stating that CodeQL **can be used** during automated analysis, CI or CD, as part of normal engineering processes for the purposes of analyzing drivers to be submitted and certified as part of the WHCP.

The [Static Tools Logo Test](/windows-hardware/test/hlk/testref/6ab6df93-423c-4af6-ad48-8ea1049155ae) enforces this requirement to analyze driver source code and fix any ***Must-Fix** violations.

> [!IMPORTANT]
> Windows Hardware Compatibility Program requires CodeQL for Static Tool Logo (STL) Tests on our Client and Server Operating Systems. We will continue to maintain support for SDV and CA on older products. We strongly encourage partners to review the CodeQL requirements for the [Static Tool Logo Test](/windows-hardware/test/hlk/testref/6ab6df93-423c-4af6-ad48-8ea1049155ae).

### HLK EULA and CodeQL

Usage of CodeQL for the purpose of certifying for the Windows Hardware Compatibility Program testing is acceptable under the [Hardware Lab Kit (HLK)](/windows-hardware/test/hlk/) End User License Agreement. 

For WHCP participants, the HLK's EULA overrides GitHub's CodeQL Terms and Conditions, allowing CodeQL **to be used** during automated analysis, CI, or CD as part of normal engineering processes to analyze drivers submitted for WHCP certification.

For those following along for general use, read the [GitHub CodeQL Terms and Conditions](https://github.com/github/codeql-cli-binaries/blob/main/LICENSE.md) and/or [contact CodeQL](https://support.github.com/contact).

## Related Content

- [Run the CodeQL analysis on your driver code](./static-tools-and-codeql.md)

- [Frequently asked questions for CodeQL tests](./codeql-faq.md)

- [CodeQL queries and suites](./codeql-queries.md)


