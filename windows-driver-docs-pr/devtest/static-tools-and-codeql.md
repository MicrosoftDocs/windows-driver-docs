---
title: CodeQL and the Static Tools Logo Test
description: Using Static tools and CodeQL on Windows driver source code to discover and repair any issues that are deemed Must-Fix
keywords:
- dynamic verification tools WDK
- static verification tools WDK
ms.date: 09/27/2022
---

# CodeQL and the Static Tools Logo Test

## Navigation

[Overview](#overview)

[CodeQL Concepts](#codeql-concepts)

[1. CodeQL Setup](#1-codeql-setup)

[2. Build the CodeQL Database](#2-build-the-codeql-database)

[3. Perform and View Analysis](#3-perform-analysis-and-view-results)

[4. Convert SARIF to Driver Verification Log Format (DVL)](#4-convert-sarif-to-driver-verification-log-format-dvl)

[5. Visual Studio Post Build Event (Optional)](#5-visual-studio-post-build-event-optional)

[Troubleshooting and Known Issues](#troubleshooting)

[FAQ](#frequently-asked-questions-faqs)

[Windows Driver Developer Supplemental Tools Queries and Suites](#queries-and-suites)

---


## Overview
Microsoft is committed to mitigating the attack surface for the Windows operating system, and ensuring that third party drivers meet a strong security bar is critical to accomplishing that goal. One step in setting this security bar is by adding a new requirement to the [Windows Hardware Compatibility Program](/windows-hardware/design/compatibility) (WHCP) which states that all driver submissions must use the [CodeQL](https://codeql.github.com/) engine on driver source code and fix any violations that are deemed **"Must-Fix"**.

[CodeQL](https://codeql.github.com/), by GitHub, is a powerful semantic code analysis engine, and the combination of an extensive suite of high-value security queries along with a robust platform make it an invaluable tool for securing driver code.

Usage of CodeQL for the purpose of WHCP testing is acceptable under the **[Hardware Lab Kit (HLK)](/windows-hardware/test/hlk/) End User License Agreement**. For WHCP participants, the HLK's EULA overwrites GitHub's CodeQL Terms and Conditions by stating that CodeQL **can be used** during automated analysis, CI or CD, as part of normal engineering processes for the purposes of analyzing drivers to be submitted and certified as part of the WHCP.

The requirement to analyze driver source code and fix any **"Must-Fix"** violations will be enforced by the [Static Tools Logo Test](/windows-hardware/test/hlk/testref/6ab6df93-423c-4af6-ad48-8ea1049155ae).

This page describes how to:

- Use CodeQL to analyze your driver source code for known high impact security issues.
- Ensure the Static Tools Logo Test can consume the results of running CodeQL.
- Determine which **"Must-Fix"** [queries](#must-fix-queries) must be run for WHCP certification.

> **[NOTE]** Usage of CodeQL for the purpose of certifying for the Windows Hardware Compatibility Program testing is acceptable under the [Hardware Lab Kit (HLK)](/windows-hardware/test/hlk/) End User License Agreement. For WHCP participants, the HLK's EULA overwrites GitHub's CodeQL Terms and Conditions. The HLK EULA states that CodeQL can be used during automated analysis, CI or CD, as part of normal engineering processes for the purposes of analyzing drivers to be submitted and certified as part of the Windows Hardware Compatibility Program. For those following along for general use, please read the [GitHub CodeQL Terms and Conditions](https://github.com/github/codeql-cli-binaries/blob/main/LICENSE.md) and/or [contact CodeQL](https://support.github.com/contact).

## CodeQL Concepts

CodeQL is a static analysis engine used by developers to perform security analysis on code outside of a live environment. CodeQL ingests code while it is compiling, and builds a database from it. The database becomes a directory containing queryable data, a source reference, and log files. Once the database is built, one can run analysis on it by utilizing CodeQL queries (also called checks or rules) which will determine if the source code contains violations or security vulnerabilities. CodeQL provides a library of standard queries which check for language correctness, symantics, and provides great value to developers who wish to ensure their code is free of bugs and vulnerabilities. CodeQL also provides the option to build custom queries, which is what the [Windows Driver Developer Supplemental Repository](https://github.com/microsoft/Windows-Driver-Developer-Supplemental-Tools) contains: several suites of queries which are specific to driver code and are used in the WHCP program. CodeQL also provides a [CodeQL command line tool (CLI)](https://codeql.github.com/docs/codeql-cli/) to easily perform CodeQL actions and/or perform large scale analysis.

For more information on writing custom queries, see [Writing queries](https://codeql.github.com/docs/writing-codeql-queries/codeql-queries/) in the CodeQL docs.
Supplementary CodeQL CLI documentation can be found at [CodeQL Getting Started](https://codeql.github.com/docs/codeql-cli/getting-started-with-the-codeql-cli/).

## 1. CodeQL Setup

**For General Use**
| Branch to use | CodeQL CLI version |
|---------------|--------------------|
| Main          | [2.6.3](https://github.com/github/codeql-cli-binaries/releases/tag/v2.6.3)              |

**For Windows Hardware Compatibility Program Use**
| Windows Release          | Branch to use | CodeQL CLI version |
|--------------------------|---------------|--------------------|
| Windows Server 2022      | WHCP_21H2     | [2.4.6](https://github.com/github/codeql-cli-binaries/releases/tag/v2.4.6)              |
| Windows 11               | WHCP_21H2     | [2.4.6](https://github.com/github/codeql-cli-binaries/releases/tag/v2.4.6)              |
| Windows 11, version 22H2 | WHCP_22H2     | [2.6.3](https://github.com/github/codeql-cli-binaries/releases/tag/v2.6.3)              |

### Download and Install CodeQL

1. Create a directory to contain CodeQL. This example will use C:\codeql-home\

   ```console
   C:\> mkdir C:\codeql-home
   ```

1. Refer to the tables above to select which version of CodeQL CLI to use in accordance with the desired branch of Microsoft's driver queries; if you are performing analysis as part of the WHCP program, please refer to the table **For Windows Hardware Compatibility Program Use** otherwise use Main branch and [CodeQL CLI v2.6.3](https://github.com/github/codeql-cli-binaries/releases/tag/v2.6.3). Using a different version may result in a database incompatible with these libraries.

1. Navigate to the CodeQL CLI binaries release associated with the tables above, and download the zip file in accordance with your project's architecture. For example for 64 bit Windows "codeql-win64.zip".

1. Extract Codeql CLI directory to the one you just created, for example: C:\codeql-home\codeql\.

1. Confirm that the CodeQL command works by displaying the help menu.

   ```console
   C:\codeql-home\codeql\>codeql --help
   Usage: codeql <command> <argument>...
   Create and query CodeQL databases, or work with the QL language.

   GitHub makes this program freely available for the analysis of open-source software and certain other uses, but it is
   not itself free software. Type codeql --license to see the license terms.

         --license              Show the license terms for the CodeQL toolchain.
   Common options:
     -h, --help                 Show this help text.
     -v, --verbose              Incrementally increase the number of progress messages printed.
     -q, --quiet                Incrementally decrease the number of progress messages printed.
   Some advanced options have been hidden; try --help -v for a fuller view.
   Commands:
     query     Compile and execute QL code.
     bqrs      Get information from .bqrs files.
     database  Create, analyze and process CodeQL databases.
     dataset   [Plumbing] Work with raw QL datasets.
     test      Execute QL unit tests.
     resolve   [Deep plumbing] Helper commands to resolve disk locations etc.
     execute   [Deep plumbing] Low-level commands that need special JVM options.
     version   Show the version of the CodeQL toolchain.
     generate  Generate formatted QL documentation.
   ```

### Clone Windows Driver Developer Supplemental Tools repository
> **[NOTE]** This section is under maintenance as we upgrade the version of CodeQL the Windows Driver Developer Supplemental Tools repository is compatible with. We will be utilizing the new functionality of CodeQL packs which will change the method for downloading and installing this repository. We appreciate your patience if there are issues with the install, please reach out to us if you are having trouble: stlogohelp@microsoft.com.

1. Navigate to the [Microsoft Windows Driver Developer Supplemental Tools repository](https://github.com/microsoft/Windows-Driver-Developer-Supplemental-Tools).

1. [Clone](https://github.com/git-guides/git-clone) the repository in accordance with the branch you need to use. [Find your desired branch in the tables above](#codeql-windows-setup).

   ```console
   C:\codeql-home\>git clone https://github.com/microsoft/Windows-Driver-Developer-Supplemental-Tools.git --recursive -b <BRANCH>
   ```

    If you have already cloned the repository and need to switch to a different branch, you can switch to the appropriate branch by running `git fetch` and `git checkout` from your local copy of the repository:

    ```console
    C:\codeql-home\Windows-Driver-Developer-Supplemental-Tools>git fetch --all
    C:\codeql-home\Windows-Driver-Developer-Supplemental-Tools>git checkout <BRANCH>
    ```

## 2. Build the CodeQL Database
Our examples assume use of a Windows development environment and that the installation location is C:\codeql-home, but you can use the setup that suits you. See [supported languges and frameworks](https://codeql.github.com/docs/codeql-overview/supported-languages-and-frameworks/) for a list of which compilers are supported.

1. Create a directory for CodeQL to place the databases it creates. For example: C:\codeql-home\databases

    ```console
    mkdir C:\codeql-home\databases
    ```

1. Use the CodeQL command to create a database using the following parameters:

    - the first parameter is a link to your database directory. For example: C:\codeql-home\databases\MyDriverDatabase (this command will fail if the directory already exists).
    - `--language` or `-l` is the language or languages your source code is in (this can be a comma separated list; ex: [cpp, javascript]).
    - `-- source` or `-s` is the path to your source code.
    - `--command ` or `-c` is your build command or the path to your build file.

    ```console
    codeql database create <database directory> --language=<language> --source=<path to source code> --command=<build command or path to build file>
    ```

Example using MSBuild Compiler:
```
C:\codeql-home\codeql: codeql database create C:\codeql-home\Databases\MyDriverDatabase -l=cpp -s=D:\MyDriverProject -c="msbuild /t:rebuild D:\MyDriverProject\MyDriverProject.sln"
```

Example using a build file:
```
C:\codeql-home\codeql: codeql database create C:\codeql-home\Databases\MyDriverDatabase -l=cpp -s=D:\MyDriverProject -c="D:\MyDriverProject\build-all.cmd"
```

For more information or help using the `database create` command, go to [Creating CodeQL Databases](https://codeql.github.com/docs/codeql-cli/creating-codeql-databases/) or use the following command:

```console
codeql database create --help
```

## 3. Perform Analysis and View Results

At this point, the set-up is complete and the next step is to perform the actual analysis on the driver source code.

1. Use the CodeQL command to analyze your database using the following parameters:

    - the first parameter is a link to your database directory. For example: C:\codeql-home\databases\MyDriverDatabase. (This command will fail if the directory doesn't exist.)
    - `--format` is the file type of the output file. Options include: SARIF and CSV. (**For WHCP Users** use SARIF format.)
    - `--output` is the path to where you want the output file, be sure to include the format in the file name. (This command will fail if the directory doesn't already exist.)
    - the query specifiers parameter is a space separated list of arguments which can include:
        - a path to a query file
        - a path to a directory containing query files
        - a path to a query suite file
        - the name of a CodeQL query pack

    ```console
    codeql database analyze <database directory> --format=<format> --output=<path to output file> <query specifiers>
    ```

    Example 1:
    ```
    C:\codeql-home\codeql: codeql database analyze C:\codeql-home\Databases\MyDriverDatabase --format=sarifv.2.1.0 --output=C:\codeql-home\AnalysisResults\MyDriverProjectResults.sarif C:\codeql-home\Windows-Driver-Developer-Supplemental-Tools\src\suites\windows_driver_mustfix.qls
    ```

    Example 2:
    ```
    C:\codeql-home\codeql: codeql database create D:\MyDriverDatabase --format=sarifv.2.1.0 --output=D:\mydriverresults.csv C:\codeql-home\Windows-Driver-Developer-Supplemental-Tools\src\suites\windows_driver_recommended.qls
    ```

    For more information or help using the `database analyze` command, go to [Analyzing Databases with the CodeQL CLI](https://codeql.github.com/docs/codeql-cli/analyzing-databases-with-the-codeql-cli/) or use the following command:

    ```console
    codeql database create --help
    ```

2. Interpret the Results

    We will be focusing on SARIF format for this section as it is what is required for the following steps, though you are welcome to use CSV format if it suits your needs better.

    Static Analysis Results Interchange Format (SARIF) is a JSON type format used for sharing static analysis results. Read more about the standard at [OASIS Static Analysis Results Interchange Format (SARIF)](https://github.com/oasis-tcs/sarif-spec), how CodeQL uses [SARIF Output](https://codeql.github.com/docs/codeql-cli/sarif-output/#sarif-output), and [an example of raw SARIF output](https://raw.githubusercontent.com/oasis-tcs/sarif-spec/master/Schemata/sarif-schema-2.1.0.json).

    There are several methods for interpreteing the analysis results, including manually sorting through the objects. Here are a few that we use:
    - The [Microsoft Sarif Viewer (Web)](https://microsoft.github.io/sarif-web-component/) has functionality which allows you to drag and drop your SARIF file into the viewer, then displays results categorized by rule. This is a very quick and easy way to see the count of violations or which queries have violations, but less easy to find source code information aside from the line number. Note that the page will not update if there are no violations.
    - The [Microsoft SARIF Viewer for Visual Studio](https://marketplace.visualstudio.com/items?itemName=WDGIS.MicrosoftSarifViewer) is great for displaying the results within Visual Studio for seamless transition from results to source code.
    - The [SARIF extension for Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=MS-SarifVSCode.sarif-viewer)

    The most important section of the SARIF file is the "Results" property within the "Run" object. Each query will have a Results property with details about any detected violations and where it occurred. If no violations are found, the property value will be empty. 

> **[NOTE]** Queries are classified using statuses such as "error" "warning" and "problem" but this classification is separate from how the Windows Hardware Compatibility Program and specifically the Static Tools Logo Test will grade the results. Any driver with defects from any query within the "Must-Fix" suite will **not pass** the Static Tools Logo Test and will **fail to be certified**, regardless of the query classification in the raw query file (ex. "warning").

## 4. Convert SARIF to Driver Verification Log Format (DVL)

The Static Tools Logo Test parses a [Driver Verification Log (DVL)](../develop/creating-a-driver-verification-log.md) which is the compiled results from several static analysis engines which have run on the driver source code. There are three ways to convert your SARIF file to DVL format, select the one that best fits your setup.

### Using Visual Studio (WDK Preview Build 20190 and up)

1. Place your SARIF results file in the same directory as your .vcxproj file.
2. From the Driver extension menu, select **Create Driver Verification Log**.
3. Verify the DVL UI detects your SARIF file.
    - Note: if you moved your SARIF file to the .vcxproj directory using the Visual Studio UI, it is possible Visual Studio created a *reference* to the SARIF file instead of actually moving it. Try opening the directory outside of Visual Studio to ensure it truly exists there.
4. Select **Create**.

### Using MSBuild

1. Place your SARIF results file in the same directory as your .vcxproj file.
2. Open your Visual Studio Command Prompt, Visual Studio Native Tools Command Prompt, or the Enterprise Windows Driver Kit (EWDK).
3. Use the msbuild command with the following parameters:
    - path to vcx project file
    - `/target:dvl`
    - `/p:Configuration="Release"`
    - `/P:Platform=<platform>` (Use one of the following strings only: x86, x64, arm, arm64)
    ```
    msbuild.exe <vcxprojectfile> /target:dvl /p:Configuration="Release" /P:Platform=<platform>
    ```

### Using CMD

1. Locate the dvl.exe from the WDK or a mounted eWDK.
2. Use the exe with the following parameters:
    - `/manualCreate`
    - `driver name` (Do not include the .sys file format)
    - `driver architecture` (Use one of the following strings only: x86, x64, arm, arm64)
    ```
    "C:\Program Files (x86)\Windows Kits\10\Tools\dvl\dvl.exe" /manualCreate <driver name> <driver architecture>
    ```

Further instructions for the Static Tools Logo HLK Test and guidance on where to place the DVL file can be found in [Running the test](/windows-hardware/test/hlk/testref/6ab6df93-423c-4af6-ad48-8ea1049155ae#running-the-test).

## 5. Visual Studio Post-Build Event (Optional)

If you are building the driver using Visual Studio, you can configure CodeQL queries to run as a post build event.

In this example, a small batch file is created in the target location and called as a post build event. For more information about Visual Studio C++ build events, see [Specifying build events](/cpp/build/specifying-build-events).

1. Create a small batch file which re-creates the CodeQL database then runs the desired queries on it. In this example, the batch file will be named `RunCodeQLRebuildQuery.bat`. Modify the paths shown in the example batch file to match your directory locations.

   ```console
   ECHO ">>> Running CodeQL Security Rule V 1.0 <<<"
   ECHO ">>> Removing previously created rules database <<<"
   rmdir /s/q C:\codeql-home\databases\kmdf
   CALL C:\codeql-home\codeql\codeql\codeql.cmd database create -l=cpp -s="C:\codeql-home\drivers\kmdf" -c "msbuild /p:Configuration=Release /p:Platform=x64 C:\codeql-home\drivers\kmdf\kmdfecho.sln /t:rebuild /p:PostBuildEventUseInBuild=false " "C:\codeql-home\databases\kmdf" -j 0
   CALL C:\codeql-home\codeql\codeql\codeql database analyze "C:\codeql-home\databases\kmdf" "C:\codeql-home\Windows-Driver-Developer-Supplemental-Tools\codeql\codeql-queries\cpp\ql\src\Likely Bugs\Underspecified Functions" --format=sarifv2.1.0 --output=C:\codeql-home\databases\kmdf.sarif -j 0 --rerun
   ECHO ">>> Loading SARIF Results in Visual Studio <<<"
   CALL devenv /Edit C:\codeql-home\databases\kmdf.sarif
   SET ERRORLEVEL = 0
   ```

1. The [devenv.exe / Edit](/visualstudio/ide/reference/edit-devenv-exe) option is used in the batch file to open the SARIF results file in the existing instance of Visual Studio. To view the SARIF results install the [Microsoft SARIF Viewer for Visual Studio](https://marketplace.visualstudio.com/items?itemName=WDGIS.MicrosoftSarifViewer) and refer to the instructions there for more information.

1. In the driver project, navigate to project properties. In the  **Configuration** pull down, select the build configuration that you wish to check with CodeQL, we recommend "Release. Creating the CodeQL database and running the queries takes a few minutes, so we don't recommend you run CodeQL on the Debug configuration of your project.

1. Select **Build Events** and **Post-Build Event** in the driver project properties.

1. Provide a path to the batch file and a description of the post build event.

![Visual Studio post build event configuration showing a batch file configured as a command line option.](images/codeql-visual-studio-post-build-event.png)

1. The results from the running the batch file will be displayed at the end of the build output.

   ```console
   1>Starting evaluation of codeql-cpp\Likely Bugs\Underspecified Functions\MistypedFunctionArguments.ql.
   1>Starting evaluation of codeql-cpp\Likely Bugs\Underspecified Functions\TooManyArguments.ql.
   1>Starting evaluation of codeql-cpp\Likely Bugs\Underspecified Functions\TooFewArguments.ql.
   1>Starting evaluation of codeql-cpp\Likely Bugs\Underspecified Functions\ImplicitFunctionDeclaration.ql.
   1>[1/4 eval 4.4s] Evaluation done; writing results to codeql-cpp\Likely Bugs\Underspecified Functions\TooManyArguments.bqrs.
   1>[2/4 eval 4.4s] Evaluation done; writing results to codeql-cpp\Likely Bugs\Underspecified Functions\TooFewArguments.bqrs.
   1>[3/4 eval 4.5s] Evaluation done; writing results to codeql-cpp\Likely Bugs\Underspecified Functions\ImplicitFunctionDeclaration.bqrs.
   1>[4/4 eval 5.2s] Evaluation done; writing results to codeql-cpp\Likely Bugs\Underspecified Functions\MistypedFunctionArguments.bqrs.
   1>Shutting down query evaluator.
   1>Interpreting results.
   1>">>> Loading SARIF Results in Visual Studio <<<"
   ```

## Troubleshooting

> If you are certifying with WHCP, the most common issue is version mismatch between HLK version and Windows Release version. Please ensure you are using the HLK version associated with the Windows release you are targeting, the associated branch in the Windows Driver Developer Supplemental Tools repository, and the subsequent CodeQL CLI version. For HLK/Windows Release compatability matrix, see [Windows Hardware Lab Kit](https://learn.microsoft.com/en-us/windows-hardware/test/hlk/) and for Windows Release/Windows Driver Developer Supplemental Tools repo branch/CodeQL CLI version, see the WHCP table in the [CodeQL Setup](#1-codeql-setup) section.

### Errors and Workarounds

For [database version](https://codeql.github.com/docs/codeql-cli/manual/version/) mismatches issues, the following tools may be helpful.

Use the codeql version command to display the version of the codeql exe.

```console
C:\codeql-home\codeql\>codeql version
CodeQL command-line toolchain release 2.4.0.
Copyright (C) 2019-2020 GitHub, Inc.
Unpacked in: C:\codeql-home\codeql\
   Analysis results depend critically on separately distributed query and
   extractor modules. To list modules that are visible to the toolchain,
   use 'codeql resolve qlpacks' and 'codeql resolve languages'.
```

The database upgrade command will update a database. Be aware that this is a one way upgrade and is not reversible. For more information, see [database upgrade](https://codeql.github.com/docs/codeql-cli/manual/database-upgrade/).

## Queries and Suites

As part of the [Microsoft CodeQL GitHub repository](https://github.com/microsoft/Windows-Driver-Developer-Supplemental-Tools), we provide two query suites to simplify the end-to-end driver developer workflow. The *windows_driver_recommended.qls* query suite contains a superset of [all of the queries](#queries) that Microsoft has deemed valuable for driver developers. The *windows_driver_mustfix.qls* query suite contains queries deemed **"Must-Fix"** for WHCP certification. Both the Mist-Fix and Recommended query suites are updated regularly.

### Recommended Fix Queries

These queries are part of the *windows_driver_recommended.qls* query suite in the [Microsoft GitHub CodeQL repository](https://github.com/microsoft/Windows-Driver-Developer-Supplemental-Tools). The "Common Weakness Enumeration" (CWE) column specifies what kinds of security issues the given query searches for. See [Mitre's page on CWE](https://cwe.mitre.org/) for more details around CWEs.

| ID                       | Location   | [Common Weakness Enumeration](https://cwe.mitre.org/)   |
| ------------------------ | ---------- | ----------------------------- |
| [cpp/too-few-arguments](https://codeql.github.com/codeql-query-help/cpp/cpp-too-few-arguments/)   | *cpp/ql/src/Likely Bugs/Underspecified Functions/TooFewArguments.ql* | N/A |
| [cpp/bad-addition-overflow-check](https://codeql.github.com/codeql-query-help/cpp/cpp-bad-addition-overflow-check/)   | *cpp/ql/src/Likely Bugs/Arithmetic/BadAdditionOverflowCheck.ql* | [CWE-190](https://cwe.mitre.org/data/definitions/190.html), [CWE-192](https://cwe.mitre.org/data/definitions/192.html) |
| [cpp/pointer-overflow-check](https://codeql.github.com/codeql-query-help/cpp/cpp-pointer-overflow-check/)   | *cpp/ql/src/Likely Bugs/Memory Management/PointerOverflow.ql* | N/A |
| [cpp/hresult-boolean-conversion](https://codeql.github.com/codeql-query-help/cpp/cpp-hresult-boolean-conversion/)   | *cpp/ql/src/Security/CWE/CWE-253/HResultBooleanConversion.ql* | [CWE-253](https://cwe.mitre.org/data/definitions/253.html) |
| [cpp/incorrect-string-type-conversion](https://codeql.github.com/codeql-query-help/cpp/cpp-incorrect-string-type-conversion/)   | *cpp/ql/src/Security/CWE/CWE-704/WcharCharConversion.ql* | [CWE-704](https://cwe.mitre.org/data/definitions/704.html) |
| [cpp/integer-multiplication-cast-to-long](https://codeql.github.com/codeql-query-help/cpp/cpp-integer-multiplication-cast-to-long/)   | *cpp/ql/src/Likely Bugs/Arithmetic/IntMultToLong.ql* | [CWE-190](https://cwe.mitre.org/data/definitions/190.html), [CWE-192](https://cwe.mitre.org/data/definitions/192.html), [CWE-197](https://cwe.mitre.org/data/definitions/197.html), [CWE-681](https://cwe.mitre.org/data/definitions/681.html) |
| [cpp/signed-overflow-check](https://codeql.github.com/codeql-query-help/cpp/cpp-signed-overflow-check/)   | *cpp/ql/src/Likely Bugs/Arithmetic/SignedOverflowCheck.ql* | N/A |
| [cpp/upcast-array-pointer-arithmetic](https://codeql.github.com/codeql-query-help/cpp/cpp-upcast-array-pointer-arithmetic/)   | *cpp/ql/src/Likely Bugs/Conversion/CastArrayPointerArithmetic.ql* | [CWE-119](https://cwe.mitre.org/data/definitions/119.html), [CWE-843](https://cwe.mitre.org/data/definitions/843.html) |
| [cpp/comparison-with-wider-type](https://codeql.github.com/codeql-query-help/cpp/cpp-comparison-with-wider-type/)   | *cpp/ql/src/Security/CWE/CWE-190/ComparisonWithWiderType.ql* | [CWE-190](https://cwe.mitre.org/data/definitions/190.html), [CWE-197](https://cwe.mitre.org/data/definitions/197.html), [CWE-835](https://cwe.mitre.org/data/definitions/835.html) |
| [cpp/suspicious-add-sizeof](https://codeql.github.com/codeql-query-help/cpp/cpp-suspicious-add-sizeof/)   | *cpp/ql/src/Security/CWE/CWE-468/SuspiciousAddWithSizeof.ql* | [CWE-468](https://cwe.mitre.org/data/definitions/468.html) |
| [cpp/potentially-dangerous-function](https://codeql.github.com/codeql-query-help/cpp/cpp-potentially-dangerous-function/)   | *cpp/ql/src/Security/CWE/CWE-676/PotentiallyDangerousFunction.ql* | [CWE-676](https://codeql.github.com/codeql-query-help/cpp/cpp-potentially-dangerous-function/)
| [cpp/incorrect-not-operator-usage](https://github.com/github/codeql/blob/main/cpp/ql/src/Likely%20Bugs/Likely%20Typos/IncorrectNotOperatorUsage.qhelp)   | *cpp/ql/src/Likely Bugs/Likely Typos/IncorrectNotOperatorUsage.ql* | [CWE-480](https://cwe.mitre.org/data/definitions/480.html) |
| [cpp/offset-use-before-range-check](https://github.com/github/codeql/blob/main/cpp/ql/src/Best%20Practices/Likely%20Errors/OffsetUseBeforeRangeCheck.qhelp)  | *cpp/ql/src/Best Practices/Likely Errors/OffsetUseBeforeRangeCheck.ql*   | N/A |
| [cpp/suspicious-add-sizeof](https://codeql.github.com/codeql-query-help/cpp/cpp-suspicious-add-sizeof/)   | *cpp/ql/src/Likely Bugs/Memory Management/SuspiciousSizeof.ql* | [CWE-468](https://codeql.github.com/codeql-query-help/cpp/cpp-suspicious-add-sizeof/) |
| [cpp/uninitialized-local](https://github.com/github/codeql/blob/main/cpp/ql/src/Likely%20Bugs/Memory%20Management/UninitializedLocal.qhelp)   | *cpp/ql/src/Likely Bugs/Memory Management/UninitializedLocal.ql* | [CWE-457](https://cwe.mitre.org/data/definitions/457.html), [CWE-665](https://cwe.mitre.org/data/definitions/665.html) |
| [cpp/unterminated-variadic-call](https://github.com/github/codeql/tree/main/cpp/ql/src/Security/CWE/CWE-121)   | *cpp/ql/src/Security/CWE/CWE-121/UnterminatedVarargsCall.ql* | [CWE-121](https://cwe.mitre.org/data/definitions/121.html) |
| [cpp/suspicious-pointer-scaling](https://github.com/github/codeql/blob/main/cpp/ql/src/Security/CWE/CWE-468/IncorrectPointerScalingChar.qhelp)   | *cpp/ql/src/Security/CWE/CWE-468/IncorrectPointerScaling.ql* | [CWE-468](https://cwe.mitre.org/data/definitions/468.html) |
| [cpp/suspicious-pointer-scaling-void](https://github.com/github/codeql/blob/main/cpp/ql/src/Security/CWE/CWE-468/IncorrectPointerScalingVoid.qhelp)   | *cpp/ql/src/Security/CWE/CWE-468/IncorrectPointerScalingVoid.ql* | [CWE-468](https://cwe.mitre.org/data/definitions/468.html) |
| [cpp/conditionally-uninitialized-variable](https://github.com/github/codeql/tree/main/cpp/ql/src/Security/CWE/CWE-457)   | *cpp/ql/src/Security/CWE/CWE-457/ConditionallyUninitializedVariable.ql.* | [CWE-457](https://cwe.mitre.org/data/definitions/457.html) |
| [cpp/use-after-free](./codeql-windows-driver-useafterfree.md)   | *Windows-Driver-Developer-Supplemental-Tools/codeql/windows-drivers/queries/Likely Bugs/Memory Management/UseAfterFree\UseAfterFree.ql* | N/A |
| [cpp/windows/wdk/deprecated-api](./codeql-windows-driver-wdkdeprecatedapi.md)   | *Windows-Driver-Developer-Supplemental-Tools/codeql/windows-drivers/queries/Windows/wdk/wdk-deprecated-api.ql* | N/A |
| [Likely Bugs/Boundary Violations/PaddingByteInformationDisclosure.ql](./codeql-windows-driver-padding-byte-information-disclosure.md)   | *Windows-Driver-Developer-Supplemental-Tools/codeql/windows-drivers/queries/Likely Bugs/Boundary Violations/PaddingByteInformationDisclosure.ql* | N/A |
| [Likely Bugs/Conversion/BadOverflowGuard.ql](./codeql-windows-driver-badoverflowguard.md)   | *Windows-Driver-Developer-Supplemental-Tools/codeql/windows-drivers/queries/Likely Bugs/Conversion/BadOverflowGuard.ql* | N/A |
| [Likely Bugs/Conversion/InfiniteLoop.ql](./codeql-windows-driver-infiniteloop.md)   | *Windows-Driver-Developer-Supplemental-Tools/codeql/windows-drivers/queries/Likely Bugs/Conversion/InfiniteLoop.ql* | N/A |
| [Likely Bugs/UninitializedPtrField.ql](./codeql-windows-driver-uninitializedptrfield.md)   | *Windows-Driver-Developer-Supplemental-Tools/codeql/windows-drivers/queries/Likely Bugs/UninitializedPtrField.ql* | N/A |
| [cpp/Security/Cryptography/HardcodedIVCNG.ql](./codeql-windows-driver-hardcodedivcng.md)   | *Windows-Driver-Developer-Supplemental-Tools/codeql/windows-drivers/queries/Security/Crytpography/HardcodedIVCNG.ql* | N/A |

### Must-Fix Queries

The subset of queries below are **Must-Fix** for WHCP certification and are also included in the **Recommended Fix** suite.

| ID            | Location | [Common Weakness Enumeration](https://cwe.mitre.org/)   |
| ------------------------ | ---------- | ----------------------------- |
| [cpp/too-few-arguments](https://codeql.github.com/codeql-query-help/cpp/cpp-too-few-arguments/)   | *cpp/ql/src/Likely Bugs/Underspecified Functions/TooFewArguments.ql* | N/A |
| [cpp/bad-addition-overflow-check](https://codeql.github.com/codeql-query-help/cpp/cpp-bad-addition-overflow-check/)   | *cpp/ql/src/Likely Bugs/Arithmetic/BadAdditionOverflowCheck.ql* | [CWE-190](https://cwe.mitre.org/data/definitions/190.html), [CWE-192](https://cwe.mitre.org/data/definitions/192.html) |
| [cpp/pointer-overflow-check](https://codeql.github.com/codeql-query-help/cpp/cpp-pointer-overflow-check/)   | *cpp/ql/src/Likely Bugs/Memory Management/PointerOverflow.ql*| N/A |
| [cpp/hresult-boolean-conversion](https://codeql.github.com/codeql-query-help/cpp/cpp-hresult-boolean-conversion/)   | *cpp/ql/src/Security/CWE/CWE-253/HResultBooleanConversion.ql* | [CWE-253](https://cwe.mitre.org/data/definitions/253.html) |
| [Security/incorrect-string-type-conversion-ignore-puchar-casts](https://github.com/microsoft/Windows-Driver-Developer-Supplemental-Tools/blob/main/src/microsoft/Security/CWE/CWE-704/WcharCharConversionLimited.ql)   | *Windows-Driver-Developer-Supplemental-Tools/blob/main/src/microsoft/Security/CWE/CWE-704/WcharCharConversionLimited.ql* | [CWE-704](https://cwe.mitre.org/data/definitions/704.html) |
| [cpp/comparison-with-wider-type](https://codeql.github.com/codeql-query-help/cpp/cpp-comparison-with-wider-type/)   | *cpp/ql/src/Security/CWE/CWE-190/ComparisonWithWiderType.ql*  | [CWE-190](https://cwe.mitre.org/data/definitions/190.html), [CWE-197](https://cwe.mitre.org/data/definitions/197.html), [CWE-835](https://cwe.mitre.org/data/definitions/835.html) |
| [cpp/windows/wdk/deprecated-api](./codeql-windows-driver-wdkdeprecatedapi.md)   | *Windows-Driver-Developer-Supplemental-Tools/codeql/windows-drivers/queries/Windows/wdk/wdk-deprecated-api.ql* | N/A |

## Frequently Asked Questions (FAQ's)

### When will this be required for device certification?

See the [Windows Hardware Compatibility Program Certification Process](https://learn.microsoft.com/en-us/windows-hardware/design/compatibility/whcp-certification-process) to for requirement details.

### What is the motivation behind requiring CodeQL be run on driver source code?

The motivation for requiring CodeQL to be run on driver source code can be summarized by two main reasons:

1. Security of Windows is paramount and requiring CodeQL to be run on driver source code is one step in helping improve the security of components which get certified by Microsoft.
1. CodeQL queries are actively developed by security engineers at Microsoft, as Microsoft is committed to ensuring that it's hardware ecosystem benefits from the same high-quality tooling that is used at Microsoft.

### Which license governs the usage of CodeQL for driver developers?

Usage of CodeQL for the purpose of WHCP testing is acceptable under the **[Hardware Lab Kit (HLK)](/windows-hardware/test/hlk/) End User License Agreement**. For WHCP participants, the HLK's EULA overwrites GitHub's CodeQL Terms and Conditions. The HLK EULA states that CodeQL **can be used** during automated analysis, CI or CD, as part of normal engineering processes for the purposes of analyzing drivers to be submitted and certified as part of the WHCP.

### Do I need to use Visual Studio or msbuild to run CodeQL?

CodeQL **does not require MSBuild or Visual Studio to be used**. See [supported languges and frameworks](https://codeql.github.com/docs/codeql-overview/supported-languages-and-frameworks/) for a list of which compilers are supported.

### How does the HLK verify that my driver was scanned by CodeQL?

The Static Tools Logo Test in the HLK is the test that enforces this requirement. Details on the Static Tools Logo Test can be found on its [MS Docs page](/windows-hardware/test/hlk/testref/6ab6df93-423c-4af6-ad48-8ea1049155ae).

### Are all defects reported by CodeQL true defects?

Every CodeQL query has varying levels of precision. Our goal is to minimize false positives, but occasionally they will occur. Our suite of "Must-Fix" queries have been developed and hand-picked for use with the WHCP program because our extensive testing results in nearly 0 false positives. If you are seeing false positives from a query in the set of "Must-Fix" queries, please **email stlogohelp@microsoft.com** immediately and we will work to get it resolved as soon as possible.

### Does a query's classification of either "warning" or "error" matter for the purposes of the Static Tools Logo Test?

Queries are classified using statuses such as "error" "warning" and "problem" in CodeQL but this classification is separate from how the Windows Hardware Compatibility Program and specifically the Static Tools Logo Test will grade the results. Any driver with defects from any query within the "Must-Fix" suite will **not pass** the Static Tools Logo Test and will **fail to be certified**, regardless of the query classification in the raw query file (ex. "warning").

### Can I generate a DVL on Visual Studio solutions?

No, DVL generation must be run at the project level and cannot be run on [Visual Studio solutions](/visualstudio/get-started/tutorial-projects-solutions). Instructions for how to generate a DVL can be found at: [Creating a Driver Verification Log](../develop/creating-a-driver-verification-log.md).

### Can I generate a Driver Verification Log (DVL) outside of the context of msbuild or Visual Studio?

As part of the Windows Driver Kit (WDK) and Enterprise WDK (eWDK), Microsoft ships a component called *dvl.exe* which can be used to generate Driver Verification Logs (DVLs). Starting in WDK/eWDK preview versions 21342 and above, it is possible to generate a DVL from the command line outside of the context of msbuild or Visual Studio by passing a driver name and architecture. See [Creating a Driver Verification Log](../develop/creating-a-driver-verification-log.md) for more details.

### I have comments or questions around how to use CodeQL on my driver, where do I send feedback?

Send feedback and questions to [stlogohelp@microsoft.com](mailto:stlogohelp@microsoft.com).
