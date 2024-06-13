---
title: CodeQL and the Static Tools Logo Test
description: Using Static tools and CodeQL on Windows driver source code to discover and repair any issues that are deemed Must-Fix
keywords:
- dynamic verification tools WDK
- static verification tools WDK
ms.date: 04/03/2024
---

# CodeQL and the Static Tools Logo Test

## CodeQL and Driver Security

Microsoft is committed to mitigating the attack surface for the Windows operating system, and ensuring that third party drivers meet a strong security bar is critical to accomplishing that goal. One step in setting this security bar is the requirement to the [Windows Hardware Compatibility Program](/windows-hardware/design/compatibility) (WHCP) which states that all driver submissions must use the [CodeQL](https://codeql.github.com/) engine on driver source code and fix any violations that are deemed **"Must-Fix"**.

[CodeQL](https://codeql.github.com/), by GitHub, is a powerful semantic code analysis engine, and the combination of an extensive suite of high-value security queries along with a robust platform make it an invaluable tool for securing driver code.

Usage of CodeQL for the purpose of WHCP testing is acceptable under the **[Hardware Lab Kit (HLK)](/windows-hardware/test/hlk/) End User License Agreement**. For WHCP participants, the HLK's EULA overwrites GitHub's CodeQL Terms and Conditions by stating that CodeQL **can be used** during automated analysis, CI or CD, as part of normal engineering processes for the purposes of analyzing drivers to be submitted and certified as part of the WHCP.

The requirement to analyze driver source code and fix any **"Must-Fix"** violations will be enforced by the [Static Tools Logo Test](/windows-hardware/test/hlk/testref/6ab6df93-423c-4af6-ad48-8ea1049155ae).

This topic describes how to:

- Use CodeQL to analyze your driver source code for known high impact security issues.
- Ensure the Static Tools Logo Test can consume the results of running CodeQL.
- Determine which **"Must-Fix"** [queries](#must-fix-queries) must be run for WHCP certification.

> [!IMPORTANT]
> Windows Hardware Compatibility Program requires CodeQL for Static Tool Logo (STL) Tests on our Client and Server Operating Systems. We will continue to maintain support for SDV and CA on older products. Partners are highly encouraged to review the CodeQL requirements for the [Static Tool Logo Test](/windows-hardware/test/hlk/testref/6ab6df93-423c-4af6-ad48-8ea1049155ae).

### HLK EULA and CodeQL

Usage of CodeQL for the purpose of certifying for the Windows Hardware Compatibility Program testing is acceptable under the [Hardware Lab Kit (HLK)](/windows-hardware/test/hlk/) End User License Agreement. For WHCP participants, the HLK's EULA overwrites GitHub's CodeQL Terms and Conditions. The HLK EULA states that CodeQL can be used during automated analysis, CI or CD, as part of normal engineering processes for the purposes of analyzing drivers to be submitted and certified as part of the Windows Hardware Compatibility Program. For those following along for general use, read the [GitHub CodeQL Terms and Conditions](https://github.com/github/codeql-cli-binaries/blob/main/LICENSE.md) and/or [contact CodeQL](https://support.github.com/contact).

## CodeQL Concepts

CodeQL is a static analysis engine used by developers to perform security analysis on code outside of a live environment. CodeQL ingests code while it is compiling, and builds a database from it. The database becomes a directory containing queryable data, a source reference, and log files. Once the database is built, one can run analysis on it by utilizing CodeQL queries (also called checks or rules) which will determine if the source code contains violations or security vulnerabilities. CodeQL provides a library of standard queries which check for language correctness, semantics, and provides great value to developers who wish to ensure their code is free of bugs and vulnerabilities.

CodeQL also provides the option to build custom queries. For more information on writing custom queries, see [Writing queries](https://codeql.github.com/docs/writing-codeql-queries/codeql-queries/) in the CodeQL docs.

CodeQL also provides a [CodeQL command line tool (CLI)](https://codeql.github.com/docs/codeql-cli/) to easily perform CodeQL actions and/or perform large scale analysis.

Supplementary CodeQL CLI documentation can be found at [CodeQL Getting Started](https://codeql.github.com/docs/codeql-cli/getting-started-with-the-codeql-cli/).

## 1. CodeQL Setup

### For Windows Hardware Compatibility Program Use

#### Windows Hardware Compatibility Program Release Version Matrix

Use this matrix to determine the versions to be downloaded.

| Windows Release          | CodeQL CLI version                                    | microsoft/windows-drivers QL pack version| codeql/cpp-queries QL pack version  | Branch to use|
|--------------------------|-------------------------------------------------------|-----------------------------------------|-----------------------------|--------------|
| Windows Server 2022      | [2.4.6](https://github.com/github/codeql-cli-binaries/releases/tag/v2.4.6) or [2.15.4](https://github.com/github/codeql-cli-binaries/releases/tag/v2.15.4)|  1.0.13 (If using codeql 2.15.4) | 0.9.0 (If using codeql 2.15.4) | WHCP_21H2 |
| Windows 11               | [2.4.6](https://github.com/github/codeql-cli-binaries/releases/tag/v2.4.6) or [2.15.4](https://github.com/github/codeql-cli-binaries/releases/tag/v2.15.4)|  1.0.13 (If using codeql 2.15.4) | 0.9.0 (If using codeql 2.15.4) | WHCP_21H2 |
| Windows 11, version 22H2 | [2.6.3](https://github.com/github/codeql-cli-binaries/releases/tag/v2.6.3) or [2.15.4](https://github.com/github/codeql-cli-binaries/releases/tag/v2.15.4)|  1.0.13 (If using codeql 2.15.4) | 0.9.0 (If using codeql 2.15.4) | WHCP_22H2 |
| Windows 11, version 23H2 | [2.6.3](https://github.com/github/codeql-cli-binaries/releases/tag/v2.6.3) or [2.15.4](https://github.com/github/codeql-cli-binaries/releases/tag/v2.15.4)|  1.0.13 (If using codeql 2.15.4) | 0.9.0 (If using codeql 2.15.4) | WHCP_22H2 |
| Windows 11, version 24H2 | [2.15.4](https://github.com/github/codeql-cli-binaries/releases/tag/v2.15.4)  |  1.1.0          |        0.9.0                 |  WHCP_24H2  |

A version of the QL pack is not specified for CodeQL CLI 2.4.6 and 2.6.3 because only newer versions of CodeQL support QL packs.

### For General Use

For general use of CodeQL with other versions of Windows outside of the WHCP program, or for developing and testing queries, we currently recommend the following version and branch:

| CodeQL CLI version                                                           | microsoft/windows-drivers qlpack version | codeql/cpp-queries version | Branch to use |
|------------------------------------------------------------------------------|------------------------------------------|----------------------------|---------------|
| [2.15.4](https://github.com/github/codeql-cli-binaries/releases/tag/v2.15.4) | latest                                   | latest                     | main          |

### Download and Install CodeQL

> [!NOTE]
> Visual Studio 17.8 broke compatibility with the older versions of CodeQL used in the WHCP_21H2 and WHCP_22H2 branches. CodeQL CLI version 2.15.4 has been validated for use with WHCP 21H2 and WHCP 22H2 when using Visual Studio 17.8 or greater.
> For the WHCP Program, use the CodeQL CLI version in accordance with the table above and Windows release you are certifying for - version 2.4.6, version 2.6.3, or version 2.15.4.
> For general use with the main branch, use CodeQL CLI version 2.15.4.

1. Create a directory to contain CodeQL. This example uses `C:\codeql-home\`

   ```console
   C:\> mkdir C:\codeql-home
   ```

1. Refer to the tables above to select which version of CodeQL CLI to use in accordance with the desired branch of Microsoft's driver queries. If you are performing analysis as part of the WHCP program, refer to the table **For Windows Hardware Compatibility Program Use** otherwise use Main branch and [2.15.4](https://github.com/github/codeql-cli-binaries/releases/tag/v2.15.4). Using a different version may result in a database incompatible with the libraries.

1. Navigate to the CodeQL CLI binaries release associated with the tables above, and download the zip file in accordance with your project's architecture. For example, for 64 bit Windows "codeql-win64.zip".

1. Extract Codeql CLI directory to the one you just created, for example: C:\codeql-home\codeql\.

1. Verify CodeQL is installed correctly by checking the version:

   ```console
    C:\codeql-home\codeql>codeql --version
    CodeQL command-line toolchain release 2.15.4.
    Copyright (C) 2019-2023 GitHub, Inc.
    Unpacked in: C:\codeql-home\codeql
        Analysis results depend critically on separately distributed query and
        extractor modules. To list modules that are visible to the toolchain,
        use 'codeql resolve qlpacks' and 'codeql resolve languages'.
   ```

1. The help command displays command line usage information.

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

#### Install CodeQL Packages

#### For WHCP_21H2 and WHCP_22H2 branches

If using Visual Studio 2022 17.8 or greater with WHCP_21H2 or WHCP_22H2 and CodeQL CLI version 2.15.4:

- Follow the steps for "ALL OTHER BRANCHES."
- **Make sure to remove the CodeQL submodule if you still have an old version of the repo cloned.** CodeQL might try to use the queries in the submodule by default, which will cause errors because of mismatched versions.

If using Visual Studio version 17.7 or below **AND** either WHCP_21H2 or WHCP_22H2 AND CodeQL CLI version 2.4.6 or 2.6.3:

- Follow *Special instructions for WHCP_21H2 and WHCP_22H2 using VS17.7 or earlier* below.

#### ALL OTHER BRANCHES

##### Download the CodeQL query packages

It is no longer necessary to clone the Windows-Driver-Developer-Supplemental-Tools repo to use the queries for certification. CodeQL packages ("QL packs" or "query packs") are now used.

1. Download the correct version of the microsoft/windows-drivers pack from the *Windows Hardware Compatibility Program Release Version Matrix*. Specify the `@<version>` in the command below.

```console
C:\codeql-home\> codeql pack download microsoft/windows-drivers@<version>
```

For examples, if using WHCP_24H2, run the following command to download the 1.1.0 windows-drivers query pack:

```console
C:\codeql-home\> codeql pack download microsoft/windows-drivers@1.1.0
```

Use this command to download version 0.9.0 of the CodeQL cpp-queries query pack.

```console
C:\codeql-home\> codeql pack download codeql/cpp-queries@0.9.0
```

(It is possible to skip the above step, as the `--download` option will download needed queries later in the analysis process.)

CodeQL installs the downloaded query packs to the default directory:

`C:\Users\<current user>\.codeql\packages\microsoft\windows-drivers\<downloaded version>\`

Do not change this directory or move the installed pack.

##### Download the Windows driver query suites

Locate and copy to the local PC the two primary query suite files.

- *windows-driver-recommended.qls*
- *windows-driver-mustfix.qls*

Their contents are shown below in [Queries and Suites](#queries-and-suites); the two files are located at [https://github.com/microsoft/Windows-Driver-Developer-Supplemental-Tools/tree/main/suites](https://github.com/microsoft/Windows-Driver-Developer-Supplemental-Tools/tree/main/suites)

## 2. Build the CodeQL Database

These examples assume use of a Windows development environment and that the installation location is C:\codeql-home, but you can use the setup that suits you. See [CodeQL supported languages and frameworks](https://codeql.github.com/docs/codeql-overview/supported-languages-and-frameworks/) for a list of which compilers are supported.

1. Create a directory for CodeQL to place the databases it creates. For example: C:\codeql-home\databases

    ```console
    mkdir C:\codeql-home\databases
    ```

1. Use the CodeQL command to create a database using the following parameters:

    - the first parameter is a link to your database directory. For example: C:\codeql-home\databases\MyDriverDatabase (this command will fail if the directory already exists).
    - `--language` or `-l` is the language or languages your source code is in (this can be a comma separated list; ex: [cpp, javascript]).
    - `-- source` or `-s` is the path to your source code.
    - `--command` or `-c` is your build command or the path to your build file.

    ```console
    codeql database create <database directory> --language=<language> --source=<path to source code> --command=<build command or path to build file>
    ```

### Examples

Single driver example.

 ```console
C:\codeql-home\codeql> codeql database create D:\DriverDatabase --language=cpp --source-root=D:\Drivers\SingleDriver --command="msbuild /t:rebuild D:\Drivers\SingleDriver\SingleDriver.sln"
```

Multiple drivers example.

 ```console
C:\codeql-home\codeql> codeql database create D:\SampleDriversDatabase --language=cpp --source-root=D:\AllMyDrivers\SampleDrivers --command=D:\AllMyDrivers\SampleDrivers\BuildAllSampleDrivers.cmd
```

For more information or help using the `database create` command, go to [Creating CodeQL Databases](https://codeql.github.com/docs/codeql-cli/creating-codeql-databases/) or use the following command:

```console
C:\codeql-home\codeql> codeql database create --help
```

## 3. Perform Analysis

> [!NOTE]
> If using Visual Studio version 17.7 or below **AND** either WHCP_21H2 or WHCP_22H2 AND CodeQL VLI version 2.4.6 or 2.6.3, follow *Special instructions for WHCP_21H2 and WHCP_22H2 using VS17.7 or earlier* below.

At this point, the set-up is complete and the next step is to perform the actual analysis on the driver source code.

1. Use the CodeQL command to analyze your database using the following parameters:

    - the first parameter is a link to your database directory. For example: C:\codeql-home\databases\MyDriverDatabase. (This command will fail if the directory doesn't exist.)
    - `--download` flag tells CodeQL to download dependencies before running the queries.
    - `--format` is the file type of the output file. Options include: SARIF and CSV. (**For WHCP Users** use SARIF format.)
    - `--output` is the path to where you want the output file, be sure to include the format in the file name. (This command will fail if the directory doesn't already exist.)
    - the query specifiers parameter is a space separated list of arguments which can include:
        - a path to a query file
        - a path to a directory containing query files
        - a path to a query suite file
        - the name of a CodeQL query pack

    ```console
    codeql database analyze --download <path to database> <path to query suite .qls file> --format=sarifv2.1.0 --output=<outputname>.sarif
    ```

    Example:

    ```console
    codeql database analyze --download D:\DriverDatabase suites/windows-driver-recommended.qls --format=sarifv2.1.0 --output=D:\DriverAnalysis1.sarif 
    ```

    For more information or help using the `database analyze` command, go to [Analyzing Databases with the CodeQL CLI](https://codeql.github.com/docs/codeql-cli/analyzing-databases-with-the-codeql-cli/) and [Using a CodeQL pack to analyze a CodeQL database](https://docs.github.com/en/code-security/codeql-cli/using-the-advanced-functionality-of-the-codeql-cli/publishing-and-using-codeql-packs#using-a-codeql-pack-to-analyze-a-codeql-database).

    For command line help use the following command:

    ```console
    C:\codeql-home\codeql> codeql database analyze --help
    ```

## Special instructions for WHCP_21H2 and WHCP_22H2 using VS17.7 or earlier

These instructions only apply when using both Visual Studio 17.7 or earlier, along with CodeQL 2.6.3 or 2.4.6

1. Install CodeQL version as indicated in above steps.

2. Clone and install the Windows Driver Developer Supplemental Tools repository which contains the CodeQL queries specific for drivers:

    `git clone https://github.com/microsoft/Windows-Driver-Developer-Supplemental-Tools.git --recurse-submodules`

3. Refer to the *Windows Hardware Compatibility Program Release Version Matrix* to identify the correct branch for the version of Windows you wish to certify for.

4. Use the `git checkout` command to checkout the identified branch.

5. Confirm that the submodules are present in the codeql-home directory.

   ```text
    D:/codeql-home
        |--- codeql
        |--- Windows-Driver-Developer-Supplemental-Tools
   ```

6. Analyze your CodeQL database.

   Update this example command to match your environment. Set the parameters, path to new database, format, output sarif file, path to CodeQL query or query suite to use in analysis.

   `codeql database analyze <path to database> --format=sarifv2.1.0 --output=<"path to output file".sarif> <path to query/suite to run>`

    Example:

    `codeql database analyze D:\DriverDatabase --format=sarifv2.1.0 --output=D:\DriverAnalysis1.sarif D:\codeql-home\Windows-driver-developer-supplemental-tools\src\suites\windows_driver_mustfix.qls`

   Be sure to check the path to the suite or query you want to run, not every branch has the same file structure.

7. Refer to other guidance in this document for next steps, such as reviewing and submitting test results.

## 4. View and Interpret Results

We will be focusing on SARIF format for this section as it is what is required for the following steps, though you are welcome to use CSV format if it suits your needs better.

Static Analysis Results Interchange Format (SARIF) is a JSON type format used for sharing static analysis results. Read more about the standard at [OASIS Static Analysis Results Interchange Format (SARIF)](https://github.com/oasis-tcs/sarif-spec), how CodeQL uses [SARIF Output](https://codeql.github.com/docs/codeql-cli/sarif-output/#sarif-output), and [the schema json](https://github.com/oasis-tcs/sarif-spec/blob/main/sarif-2.1/schema/sarif-schema-2.1.0.json).

There are several methods for interpreting the analysis results, including manually sorting through the objects. Here are a few that we use:

- The [Microsoft Sarif Viewer (Web)](https://microsoft.github.io/sarif-web-component/) has functionality which allows you to drag and drop your SARIF file into the viewer, then displays results categorized by rule. This is a very quick and easy way to see the count of violations or which queries have violations, but less easy to find source code information aside from the line number. Note that the page will not update if there are no violations.

- The [Microsoft SARIF Viewer for Visual Studio](https://marketplace.visualstudio.com/items?itemName=WDGIS.MicrosoftSarifViewer) is great for displaying the results within Visual Studio for seamless transition from results to source code.

- The [SARIF extension for Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=MS-SarifVSCode.sarif-viewer)

The most important section of the SARIF file is the "Results" property within the "Run" object. Each query will have a Results property with details about any detected violations and where it occurred. If no violations are found, the property value will be empty.

Queries are classified using statuses such as "error" "warning" and "problem" but this classification is separate from how the Windows Hardware Compatibility Program and specifically the Static Tools Logo Test will grade the results. Any driver with defects from any query within the "Must-Fix" suite will **not pass** the Static Tools Logo Test and will **fail to be certified**, regardless of the query classification in the raw query file (ex. "warning").

## 5. Suppressing CodeQL Results (Optional)

CodeQL for drivers supports suppressing results. Suppressions are currently provided as a convenience to help developers triage issues and reduce noise, not as a way to bypass the must-fix checks. They have no impact on generating a Driver Verification Log or passing the Static Tools Logo test at this time. To use suppressions, you must run the DriverAlertSuppression.ql query at the same time as the other queries or suites you wish to run. By default, this query is enabled when running our suites from our githubs main/development branch.

For checks that have been ported from Code Analysis, existing Code Analysis suppressions will be honored. For more information, see [C++ warning pragma](/cpp/preprocessor/warning).

- `Known limitation:` You cannot combine a #pragma(disable) and #pragma(suppress) in the same line at this time.

For checks that are new to CodeQL, you can suppress them by doing one of two things:

- Write a “#pragma(suppress:the-rule-id-here)” annotation (minus quotes) on the line above the violation, as you would for Code Analysis. “the-rule-id-here” can be replaced by the @id value in a given query’s metadata, viewable at the top of the file.

- Write a comment on the line above comprised of the text “lgtm[the-rule-id-here]” (minus quotes). You will need to run the standard [C/C++ alert suppression query](https://github.com/github/codeql/blob/main/cpp/ql/src/AlertSuppression.ql) instead of the driver alert suppression query. 

Once a suppression is present and recognized, the resulting SARIF file will include data that a result was suppressed, and most result viewers will not show the result by default.

## 6. Convert SARIF to Driver Verification Log Format (DVL)

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

    `msbuild.exe <vcxprojectfile> /target:dvl /p:Configuration="Release" /P:Platform=<platform>`

### Using CMD

1. Locate the dvl.exe from the WDK or a mounted eWDK.
2. Use the exe with the following parameters:
    - `/manualCreate`
    - `driver name` (Do not include the .sys file format)
    - `driver architecture` (Use one of the following strings only: x86, x64, arm, arm64)

    `"C:\Program Files (x86)\Windows Kits\10\Tools\dvl\dvl.exe" /manualCreate <driver name> <driver architecture>`

Further instructions for the Static Tools Logo HLK Test and guidance on where to place the DVL file can be found in [Running the test](/windows-hardware/test/hlk/testref/6ab6df93-423c-4af6-ad48-8ea1049155ae#running-the-test).

## 7. Visual Studio Post-Build Event (Optional)

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

:::image type="content" source="images/codeql-visual-studio-post-build-event.png" alt-text="Visual Studio post build event configuration showing a batch file configured as a command line option.":::

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

If you are certifying with WHCP, first ensure you are using the HLK version associated with the Windows release you are targeting, the associated branch in the Windows Driver Developer Supplemental Tools repository, and the subsequent CodeQL CLI version. For HLK/Windows Release compatibility matrix, see [Windows Hardware Lab Kit](/windows-hardware/test/hlk/) and for Windows Release/Windows Driver Developer Supplemental Tools repo branch/CodeQL CLI version, see the WHCP table in the [CodeQL Setup](#1-codeql-setup) section.

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

As part of the [Microsoft CodeQL GitHub repository](https://github.com/microsoft/Windows-Driver-Developer-Supplemental-Tools), we provide two query suites to simplify the end-to-end driver developer workflow. The *windows_driver_recommended.qls* query suite is a superset of all the queries Microsoft has deemed valuable for driver developers. The *windows_driver_mustfix.qls* query suite contains queries deemed **"Must-Fix"** for WHCP certification, which must be run and passed in order to pass the Static Tools Logo Test. Both the Must-Fix and Recommended query suites are updated regularly.

### Must-Fix Queries

The subset of queries below are **Must-Fix** for WHCP certification and are also included in the **Recommended Fix** suite.

This set of rules is included in *windows_driver_mustfix.qls*.

| ID                       | Location   | [Common Weakness Enumeration](https://cwe.mitre.org/)   |
| ------------------------ | ---------- | ------------------------------------------------------- |
| [cpp/bad-addition-overflow-check](https://codeql.github.com/codeql-query-help/cpp/cpp-bad-addition-overflow-check/)   | *codeql/cpp-queries/`<Version>`/Likely Bugs/Arithmetic/BadAdditionOverflowCheck.ql* | [CWE-190](https://cwe.mitre.org/data/definitions/190.html), [CWE-192](https://cwe.mitre.org/data/definitions/192.html) |
| [cpp/pointer-overflow-check](https://codeql.github.com/codeql-query-help/cpp/cpp-pointer-overflow-check/)   | *codeql/cpp-queries/`<Version>`/Likely Bugs/Memory Management/PointerOverflow.ql*| N/A |
| [cpp/too-few-arguments](https://codeql.github.com/codeql-query-help/cpp/cpp-too-few-arguments/)   | *codeql/cpp-queries/`<Version>`/Likely Bugs/Underspecified Functions/TooFewArguments.ql* | N/A |
| [cpp/comparison-with-wider-type](https://codeql.github.com/codeql-query-help/cpp/cpp-comparison-with-wider-type/)   | *codeql/cpp-queries/`<Version>`/Security/CWE/CWE-190/ComparisonWithWiderType.ql*  | [CWE-190](https://cwe.mitre.org/data/definitions/190.html), [CWE-197](https://cwe.mitre.org/data/definitions/197.html), [CWE-835](https://cwe.mitre.org/data/definitions/835.html) |
| [cpp/hresult-boolean-conversion](https://codeql.github.com/codeql-query-help/cpp/cpp-hresult-boolean-conversion/)   | *codeql/cpp-queries/`<Version>`/Security/CWE/CWE-253/HResultBooleanConversion.ql* | [CWE-253](https://cwe.mitre.org/data/definitions/253.html) |

The *windows_driver_mustfix.qls* file contains these must fix code queries.

```text
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT license.

- description: Security queries required to fix when certifying Windows Drivers
- queries: . 
  from: codeql/cpp-queries
  version: 0.9.0
- include:
    query path: 
      - Likely Bugs/Arithmetic/BadAdditionOverflowCheck.ql
      - Likely Bugs/Memory Management/PointerOverflow.ql
      - Likely Bugs/Underspecified Functions/TooFewArguments.ql
      - Security/CWE/CWE-190/ComparisonWithWiderType.ql
      - Security/CWE/CWE-253/HResultBooleanConversion.ql
- import: windows-driver-suites/windows_mustfix_partial.qls
  from: microsoft/windows-drivers
```

This set of rules is included in *windows-driver-suites/windows_mustfix_partial.qls*.

| ID                       | Location   | [Common Weakness Enumeration](https://cwe.mitre.org/)   |
| ------------------------ | ---------- | ------------------------------------------------------- |
| [cpp/windows/wdk/deprecated-api](./codeql-windows-driver-wdkdeprecatedapi.md)   | */microsoft/windows-drivers/`<Version>`/drivers/general/queries/WdkDeprecatedApis/wdk-deprecated-api.ql* | N/A |
| [microsoft/Security/CWE/CWE-704/WcharCharConversionLimited](https://github.com/microsoft/Windows-Driver-Developer-Supplemental-Tools/blob/main/src/microsoft/Security/CWE/CWE-704/WcharCharConversionLimited.ql)  |*/microsoft/windows-drivers/`<Version>`/microsoft/Security/CWE/CWE-704/WcharCharConversionLimited.ql* | [CWE-704](https://cwe.mitre.org/data/definitions/704.html) |

The *windows_mustfix_partial.qls* file contains these must fix code queries.

```text
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT license.

- description: Security queries required to fix when certifying Windows Drivers
- queries: .
  from: microsoft/windows-drivers
- include:
    query path: 
      - drivers/general/queries/WdkDeprecatedApis/wdk-deprecated-api.ql
      - microsoft/Security/CWE/CWE-704/WcharCharConversionLimited.ql
```

### Recommended Fix Queries

These queries are part of the *windows_driver_recommended.qls* query suite in the [Microsoft GitHub CodeQL repository](https://github.com/microsoft/Windows-Driver-Developer-Supplemental-Tools). The "Common Weakness Enumeration" (CWE) column specifies what kinds of security issues the given query searches for. See [Mitre's page on CWE](https://cwe.mitre.org/) for more details around CWEs.

#### Best Practices

| ID                       | Location   | [Common Weakness Enumeration](https://cwe.mitre.org/)   |
| ------------------------ | ---------- | ------------------------------------------------------- |
| [cpp/offset-use-before-range-check](https://github.com/github/codeql/blob/main/cpp/ql/src/Best%20Practices/Likely%20Errors/OffsetUseBeforeRangeCheck.qhelp)  | *codeql/cpp-queries/`<Version>`/Best Practices/Likely Errors/OffsetUseBeforeRangeCheck.ql*   | N/A |

#### Likely Bugs

| ID                       | Location   | [Common Weakness Enumeration](https://cwe.mitre.org/)   |
| ------------------------ | ---------- | ------------------------------------------------------- |
| [cpp/bad-addition-overflow-check](https://codeql.github.com/codeql-query-help/cpp/cpp-bad-addition-overflow-check/)   | *codeql/cpp-queries/`<Version>`/Likely Bugs/Arithmetic/BadAdditionOverflowCheck.ql* | [CWE-190](https://cwe.mitre.org/data/definitions/190.html), [CWE-192](https://cwe.mitre.org/data/definitions/192.html) |
| [cpp/integer-multiplication-cast-to-long](https://codeql.github.com/codeql-query-help/cpp/cpp-integer-multiplication-cast-to-long/)   | *codeql/cpp-queries/`<Version>`/Likely Bugs/Arithmetic/IntMultToLong.ql* | [CWE-190](https://cwe.mitre.org/data/definitions/190.html), [CWE-192](https://cwe.mitre.org/data/definitions/192.html), [CWE-197](https://cwe.mitre.org/data/definitions/197.html), [CWE-681](https://cwe.mitre.org/data/definitions/681.html) |
| [cpp/signed-overflow-check](https://codeql.github.com/codeql-query-help/cpp/cpp-signed-overflow-check/)   | *codeql/cpp-queries/`<Version>`/Likely Bugs/Arithmetic/SignedOverflowCheck.ql* | N/A |
| [cpp/upcast-array-pointer-arithmetic](https://codeql.github.com/codeql-query-help/cpp/cpp-upcast-array-pointer-arithmetic/)   | *codeql/cpp-queries/`<Version>`/Likely Bugs/Conversion/CastArrayPointerArithmetic.ql* | [CWE-119](https://cwe.mitre.org/data/definitions/119.html), [CWE-843](https://cwe.mitre.org/data/definitions/843.html) |
| [cpp/pointer-overflow-check](https://codeql.github.com/codeql-query-help/cpp/cpp-pointer-overflow-check/)   | *codeql/cpp-queries/`<Version>`/Likely Bugs/Memory Management/PointerOverflow.ql* | N/A |
| [cpp/too-few-arguments](https://codeql.github.com/codeql-query-help/cpp/cpp-too-few-arguments/)   | *codeql/cpp-queries/`<Version>`/Likely Bugs/Underspecified Functions/TooFewArguments.ql* | N/A |
| [cpp/incorrect-not-operator-usage](https://github.com/github/codeql/blob/main/cpp/ql/src/Likely%20Bugs/Likely%20Typos/IncorrectNotOperatorUsage.qhelp)   | *codeql/cpp-queries/`<Version>`/Likely Bugs/Likely Typos/IncorrectNotOperatorUsage.ql* | [CWE-480](https://cwe.mitre.org/data/definitions/480.html) |
| [cpp/suspicious-add-sizeof](https://codeql.github.com/codeql-query-help/cpp/cpp-suspicious-add-sizeof/)   | *codeql/cpp-queries/`<Version>`/Likely Bugs/Memory Management/SuspiciousSizeof.ql* | [CWE-468](https://codeql.github.com/codeql-query-help/cpp/cpp-suspicious-add-sizeof/) |
| [cpp/uninitialized-local](https://github.com/github/codeql/blob/main/cpp/ql/src/Likely%20Bugs/Memory%20Management/UninitializedLocal.qhelp)   | *codeql/cpp-queries/`<Version>`/Likely Bugs/Memory Management/UninitializedLocal.ql* | [CWE-457](https://cwe.mitre.org/data/definitions/457.html), [CWE-665](https://cwe.mitre.org/data/definitions/665.html) |

#### Security

| ID                       | Location   | [Common Weakness Enumeration](https://cwe.mitre.org/)   |
| ------------------------ | ---------- | ------------------------------------------------------- |
| [cpp/conditionally-uninitialized-variable](https://github.com/github/codeql/tree/main/cpp/ql/src/Security/CWE/CWE-457)   | *codeql/cpp-queries/`<Version>`/Security/CWE/CWE-457/ConditionallyUninitializedVariable.ql.* | [CWE-457](https://cwe.mitre.org/data/definitions/457.html) |
| [cpp/unterminated-variadic-call](https://github.com/github/codeql/tree/main/cpp/ql/src/Security/CWE/CWE-121)   | *codeql/cpp-queries/`<Version>`/Security/CWE/CWE-121/UnterminatedVarargsCall.ql* | [CWE-121](https://cwe.mitre.org/data/definitions/121.html) |
| [cpp/suspicious-pointer-scaling](https://github.com/github/codeql/blob/main/cpp/ql/src/Security/CWE/CWE-468/IncorrectPointerScalingChar.qhelp)   | *codeql/cpp-queries/`<Version>`/Security/CWE/CWE-468/IncorrectPointerScaling.ql* | [CWE-468](https://cwe.mitre.org/data/definitions/468.html) |
| [cpp/suspicious-pointer-scaling-void](https://github.com/github/codeql/blob/main/cpp/ql/src/Security/CWE/CWE-468/IncorrectPointerScalingVoid.qhelp)   | *codeql/cpp-queries/`<Version>`/Security/CWE/CWE-468/IncorrectPointerScalingVoid.ql* | [CWE-468](https://cwe.mitre.org/data/definitions/468.html) |
| [cpp/potentially-dangerous-function](https://codeql.github.com/codeql-query-help/cpp/cpp-potentially-dangerous-function/)   | *codeql/cpp-queries/`<Version>`/Security/CWE/CWE-676/PotentiallyDangerousFunction.ql* | [CWE-676](https://codeql.github.com/codeql-query-help/cpp/cpp-potentially-dangerous-function/)|
| [cpp/incorrect-string-type-conversion](https://codeql.github.com/codeql-query-help/cpp/cpp-incorrect-string-type-conversion/)   | *codeql/cpp-queries/`<Version>`/Security/CWE/CWE-704/WcharCharConversion.ql* | [CWE-704](https://cwe.mitre.org/data/definitions/704.html) |
| [cpp/comparison-with-wider-type](https://codeql.github.com/codeql-query-help/cpp/cpp-comparison-with-wider-type/)   | *codeql/cpp-queries/`<Version>`/Security/CWE/CWE-190/ComparisonWithWiderType.ql* | [CWE-190](https://cwe.mitre.org/data/definitions/190.html), [CWE-197](https://cwe.mitre.org/data/definitions/197.html), [CWE-835](https://cwe.mitre.org/data/definitions/835.html) |
| [cpp/hresult-boolean-conversion](https://codeql.github.com/codeql-query-help/cpp/cpp-hresult-boolean-conversion/)   | *codeql/cpp-queries/`<Version>`/Security/CWE/CWE-253/HResultBooleanConversion.ql* | [CWE-253](https://cwe.mitre.org/data/definitions/253.html) |
| [cpp/suspicious-add-sizeof](https://codeql.github.com/codeql-query-help/cpp/cpp-suspicious-add-sizeof/) | *codeql/cpp-queries/`<Version>`/Security/CWE/CWE-468/CWE-468/SuspiciousAddWithSizeof.ql*|[CWE-468](https://cwe.mitre.org/data/definitions/468.html)|

The *windows_driver_recommended.qls* file contains these recommended code queries.

```text
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT license.

- description: Recommended and required queries for Windows Drivers.
- import: windows-driver-suites/windows_mustfix_partial.qls
  from: microsoft/windows-drivers
- import: windows-driver-suites/windows_recommended_partial.qls
  from: microsoft/windows-drivers
- queries: . 
  from: codeql/cpp-queries
  version: 0.9.0
- include:
    query path: 
      - Best Practices/Likely Errors/OffsetUseBeforeRangeCheck.ql
      - Likely Bugs/Arithmetic/IntMultToLong.ql
      - Likely Bugs/Arithmetic/SignedOverflowCheck.ql
      - Likely Bugs/Conversion/CastArrayPointerArithmetic.ql
      - Likely Bugs/Likely Typos/IncorrectNotOperatorUsage.ql
      - Likely Bugs/Memory Management/SuspiciousSizeof.ql
      - Likely Bugs/Memory Management/UninitializedLocal.ql
      - Security/CWE/CWE-121/UnterminatedVarargsCall.ql
      - Security/CWE/CWE-457/ConditionallyUninitializedVariable.ql
      - Security/CWE/CWE-468/IncorrectPointerScaling.ql
      - Security/CWE/CWE-468/IncorrectPointerScalingVoid.ql
      - Security/CWE/CWE-468/SuspiciousAddWithSizeof.ql
      - Security/CWE/CWE-676/PotentiallyDangerousFunction.ql
      - Security/CWE/CWE-704/WcharCharConversion.ql
      - Likely Bugs/Arithmetic/BadAdditionOverflowCheck.ql
      - Likely Bugs/Memory Management/PointerOverflow.ql
      - Likely Bugs/Underspecified Functions/TooFewArguments.ql
      - Security/CWE/CWE-190/ComparisonWithWiderType.ql
      - Security/CWE/CWE-253/HResultBooleanConversion.ql
```

These queries are part of *windows_recommended_partial.qls*.

#### Likely Bugs - windows_recommended_partial.qls

| ID                       | Location   | [Common Weakness Enumeration](https://cwe.mitre.org/)   |
| ------------------------ | ---------- | ------------------------------------------------------- |
| [cpp/paddingbyteinformationdisclosure](./codeql-windows-driver-padding-byte-information-disclosure.md)   | *microsoft/windows-drivers/`<Version>`/microsoft/Likely Bugs/Boundary Violations/PaddingByteInformationDisclosure.ql* | N/A |
| [cpp/badoverflowguard](./codeql-windows-driver-badoverflowguard.md)   | *microsoft/windows-drivers/`<Version>`/microsoft/Likely Bugs/Conversion/BadOverflowGuard.ql* | N/A |
| [cpp/infiniteloop](./codeql-windows-driver-infiniteloop.md)   | *microsoft/windows-drivers/`<Version>`/microsoft/Likely Bugs/Conversion/InfiniteLoop.ql* | N/A |
| [cpp/uninitializedptrfield](./codeql-windows-driver-uninitializedptrfield.md)   | *microsoft/windows-drivers/`<Version>`/microsoft/Likely Bugs/UninitializedPtrField.ql* | N/A |
| [cpp/use-after-free](./codeql-windows-driver-useafterfree.md)   | *microsoft/windows-drivers/`<Version>`/microsoft/Likely Bugs/Memory Management/UseAfterFree/UseAfterFree.ql* | N/A |

#### Security - windows_recommended_partial.qls

| ID                       | Location   | [Code Analysis Warning](prefast-for-drivers-warnings.md)   |
| ------------------------ | ---------- | ---------------------------------------------------------- |
| [cpp/weak-crypto/cng/hardcoded-iv](./codeql-windows-driver-hardcodedivcng.md)   | */microsoft/windows-drivers/`<Version>`/microsoft/Security/Crytpography/HardcodedIVCNG.ql* | N/A |

#### Drivers - General

| ID                       | Location   | [Code Analysis Warning](prefast-for-drivers-warnings.md)   |
| ------------------------ | ---------- | ---------------------------------------------------------- |
| [cpp/drivers/ke-set-event-pageable](./codeql-windows-driver-keseteventpageable.md) | */microsoft/windows-drivers/`<Version>`/drivers/general/queries/KeSetEventPageable/KeSetEventPageable.ql*  | No associated CA check  |
| [cpp/drivers/role-type-correctly-used](./codeql-windows-driver-roletypecorrectlyused.md) | */microsoft/windows-drivers/`<Version>`/drivers/general/queries/RoleTypeCorrectlyUsed/RoleTypeCorrectlyUsed.ql* | No associated CA check|
| [cpp/drivers/extended-deprecated-apis](https://github.com/microsoft/Windows-Driver-Developer-Supplemental-Tools/blob/main/src/drivers/general/queries/ExtendedDeprecatedApis/ExtendedDeprecatedApis.ql) | */microsoft/windows-drivers/`<Version>`/drivers/general/queries/ExtendedDeprecatedApis.ql* | [C28719 Warning](28719-banned-api-usage-use-updated-function-replacement.md), [C28726 Warning](28726-banned-api-usage-use-updated-function-replacement.md), [C28735 Warning](28735-banned-crimson-api-usage.md), [C28750 Warning](28750-banned-istrlen-usage.md) |
| [cpp/drivers/irql-not-saved](https://github.com/microsoft/Windows-Driver-Developer-Supplemental-Tools/blob/main/src/drivers/general/queries/IrqlNotSaved/) | */microsoft/windows-drivers/`<Version>`/drivers/general/queries/IrqlNotSaved/IrqlNotSaved.ql* | [C28158 Warning](28158-no-irql-was-saved.md) |
| [cpp/drivers/irql-not-used](https://github.com/microsoft/Windows-Driver-Developer-Supplemental-Tools/blob/main/src/drivers/general/queries/IrqlNotUsed/) | */microsoft/windows-drivers/`<Version>`/drivers/general/queries/IrqlNotUsed/IrqlNotUsed.ql* | [C28157 Warning](28157-function-irql-never-restored.md) |
| [cpp/drivers/irql-set-too-high](https://github.com/microsoft/Windows-Driver-Developer-Supplemental-Tools/blob/main/src/drivers/general/queries/IrqlSetTooHigh) | */microsoft/windows-drivers/`<Version>`/drivers/general/queries/IrqlTooHigh/IrqlTooHigh.ql* | [C28150 Warning](28150-function-causes-irq-level-to-be-set-above-max.md) |
| [cpp/drivers/irql-too-low](https://github.com/microsoft/Windows-Driver-Developer-Supplemental-Tools/blob/main/src/drivers/general/queries//IrqlTooLow) | */microsoft/windows-drivers/`<Version>`/drivers/general/queries/IrqlTooLow/IrqlTooLow.ql* | [C28120 Warning](28120-irql-execution-too-low.md) |
| [cpp/drivers/irql-set-too-high](https://github.com/microsoft/Windows-Driver-Developer-Supplemental-Tools/blob/main/src/drivers/general/queries/IrqlTooHigh) | */microsoft/windows-drivers/`<Version>`/drivers/general/queries/IrqlSetTooHigh/IrqlTooHigh.ql* | [C28121 Warning](28121-irq-execution-too-high.md) |
| [cpp/drivers/irql-set-too-low](https://github.com/microsoft/Windows-Driver-Developer-Supplemental-Tools/blob/main/src/drivers/general/queries/IrqlSetTooLow) | */microsoft/windows-drivers/`<Version>`/drivers/general/queries/IrqlSetTooLow/IrqlSetTooLow.ql* | [C28124 Warning](28124-call-below-minimum-irq-level.md) |
| [cpp/drivers/pool-tag-integral](https://github.com/microsoft/Windows-Driver-Developer-Supplemental-Tools/blob/main/src/drivers/general/queries/PoolTagIntegral) | */microsoft/windows-drivers/`<Version>`/drivers/general/queries/PoolTagIntegral/PoolTagIntegral.ql* | [C28134 Warning](28134-pool-tag-type-should-be-integral.md) |
| [cpp/drivers/str-safe](https://github.com/microsoft/Windows-Driver-Developer-Supplemental-Tools/blob/main/src/drivers/general/queries/StrSafe) | */microsoft/windows-drivers/`<Version>`/drivers/general/queries/StrSafe/StrSafe.ql* | [C28146 Warning](28146-kernel-mode-drivers-should-use-ntstrsafe.md) |

#### Drivers - WDM

| ID                       | Location   | [Code Analysis Warning](prefast-for-drivers-warnings.md)   |
| ------------------------ | ---------- | ---------------------------------------------------------- |
| [cpp/drivers/illegal-field-access](https://github.com/microsoft/Windows-Driver-Developer-Supplemental-Tools/blob/main/src/drivers/wdm/queries/IllegalFieldAccess)| */microsoft/windows-drivers/`<Version>`/drivers/wdm/queries/IllegalFieldAccess/IllegalFieldAccess.ql* | [C28128 Warning](28128-structure-member-directly-accessed.md) |
| [cpp/drivers/illegal-field-access2](https://github.com/microsoft/Windows-Driver-Developer-Supplemental-Tools/blob/main/src/drivers/wdm/queries//IllegalFieldAccess2) | */microsoft/windows-drivers/`<Version>`/drivers/wdm/queries/IllegalFieldAccess2/IllegalFieldAccess2.ql* | [C28175 Warning](28175struct-member-should-not-be-accessed-by-driver.md) |
| [cpp/drivers/illegal-field-write](https://github.com/microsoft/Windows-Driver-Developer-Supplemental-Tools/blob/main/src/drivers/wdm/queries/IllegalFieldWrite) | */microsoft/windows-drivers/`<Version>`/drivers/wdm/queries/IllegalFieldWrite/IllegalFieldWrite.ql* | [C28176 Warning](28176-struct-member-should-not-be-modified-by-driver.md) |
| [cpp/drivers/opaque-mdl-use](https://github.com/microsoft/Windows-Driver-Developer-Supplemental-Tools/blob/main/src/drivers/wdm/queries/OpaqueMdlUse)| */microsoft/windows-drivers/`<Version>`/drivers/wdm/queries/OpaqueMdlUse/OpaqueMdlUse.ql* | (No associated CA check) |
| [cpp/drivers/opaque-mdl-write](https://github.com/microsoft/Windows-Driver-Developer-Supplemental-Tools/blob/main/src/drivers/wdm/queries/OpaqueMdlWrite)| */microsoft/windows-drivers/`<Version>`/drivers/wdm/queries/OpaqueMdlUse/OpaqueMdlWrite.ql* | [C28145 Warning](28145-opaque-mdl-structure-should-not-be-modified.md) |
| [cpp/drivers/pending-status-error](https://github.com/microsoft/Windows-Driver-Developer-Supplemental-Tools/blob/main/src/drivers/wdm/queries/PendingStatusError)| */microsoft/windows-drivers/`<Version>`/drivers/wdm/queries/PendingStatusError/PendingStatusError.ql* | [C28143 Warning](28143-iomarkirppending-must-return-statuspending.md) |
| [cpp/drivers/wrong-dispatch-table-assignment](https://github.com/microsoft/Windows-Driver-Developer-Supplemental-Tools/blob/main/src/drivers/wdm/queries/WrongDispatchTableAssignment)| */microsoft/windows-drivers/`<Version>`/drivers/wdm/queries/WrongDispatchTableAssignment/WrongDispatchTableAssignment.ql* | [C28169 Warning](28169-dispatch-function-does-not-have-proper-annotation.md) |

The *windows-driver-suites/windows_recommended_partial.qls* file contains these recommended code queries.

```text
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT license.

- description: Recommended and required queries for Windows Drivers.
- import: windows-driver-suites/windows_mustfix_partial.qls
- queries: .
  from: microsoft/windows-drivers
- include:
    query path: 
      - microsoft/Likely Bugs/Boundary Violations/PaddingByteInformationDisclosure.ql
      - microsoft/Likely Bugs/Conversion/BadOverflowGuard.ql
      - microsoft/Likely Bugs/Conversion/InfiniteLoop.ql
      - microsoft/Likely Bugs/Memory Management/UseAfterFree/UseAfterFree.ql
      - microsoft/Likely Bugs/UninitializedPtrField.ql
      - microsoft/Security/Crytpography/HardcodedIVCNG.ql
      - drivers/general/queries/KeSetEventPageable/KeSetEventPageable.ql
      - drivers/general/queries/RoleTypeCorrectlyUsed/RoleTypeCorrectlyUsed.ql
      - drivers/general/queries/DefaultPoolTag/DefaultPoolTag.ql
      - drivers/general/queries/ExaminedValue/ExaminedValue.ql
      - drivers/general/queries/ExtendedDeprecatedApis/ExtendedDeprecatedApis.ql
      - drivers/general/queries/IrqlNotSaved/IrqlNotSaved.ql
      - drivers/general/queries/IrqlNotUsed/IrqlNotUsed.ql
      - drivers/general/queries/IrqlTooHigh/IrqlTooHigh.ql
      - drivers/general/queries/IrqlTooLow/IrqlTooLow.ql
      - drivers/general/queries/IrqlSetTooHigh/IrqlTooHigh.ql
      - drivers/general/queries/IrqlSetTooLow/IrqlSetTooLow.ql
      - drivers/general/queries/PoolTagIntegral/PoolTagIntegral.ql
      - drivers/general/queries/StrSafe/StrSafe.ql
      - drivers/wdm/queries/IllegalFieldAccess/IllegalFieldAccess.ql
      - drivers/wdm/queries/IllegalFieldAccess2/IllegalFieldAccess2.ql
      - drivers/wdm/queries/IllegalFieldWrite/IllegalFieldWrite.ql
      - drivers/wdm/queries/OpaqueMdlUse/OpaqueMdlUse.ql
      - drivers/wdm/queries/OpaqueMdlUse/OpaqueMdlWrite.ql
      - drivers/wdm/queries/PendingStatusError/PendingStatusError.ql
      - drivers/wdm/queries/WrongDispatchTableAssignment/WrongDispatchTableAssignment.ql
```

## Frequently Asked Questions (FAQ's)

### When will this be required for device certification?

See the [Windows Hardware Compatibility Program Certification Process](/windows-hardware/design/compatibility/whcp-certification-process) to for requirement details.

### What is the motivation behind requiring CodeQL be run on driver source code?

The motivation for requiring CodeQL to be run on driver source code can be summarized by two main reasons:

1. Security of Windows is paramount and requiring CodeQL to be run on driver source code is one step in helping improve the security of components which get certified by Microsoft.
1. CodeQL queries are actively developed by security engineers at Microsoft, as Microsoft is committed to ensuring that its hardware ecosystem benefits from the same high-quality tooling that is used at Microsoft.

### What types of drivers do CodeQL and the Static Tools Logo test apply to?

At present, the Static Tools Logo test requires that CodeQL be run and the "Must-Fix" set of queries passed for all kernel-mode drivers excluding graphics drivers. Note that running CodeQL on graphics drivers is **highly recommended** even though it is not currently required. Some queries may also find useful defects in user-mode components.

We anticipate extending the test and its queries to require results for graphics drivers, user-mode drivers and driver components, and other driver package components in the future. If you encounter unexpected behavior or false positives running CodeQL on graphics drivers or user-mode drivers, please file an issue on the [Windows-Driver-Developer-Supplemental-Tools repo](https://github.com/microsoft/Windows-Driver-Developer-Supplemental-Tools).

### Which license governs the usage of CodeQL for driver developers?

Usage of CodeQL for the purpose of WHCP testing is acceptable under the **[Hardware Lab Kit (HLK)](/windows-hardware/test/hlk/) End User License Agreement**. For WHCP participants, the HLK's EULA overwrites GitHub's CodeQL Terms and Conditions. The HLK EULA states that CodeQL **can be used** during automated analysis, CI or CD, as part of normal engineering processes for the purposes of analyzing drivers to be submitted and certified as part of the WHCP.

### Do I need to use Visual Studio or msbuild to run CodeQL?

CodeQL **does not require MSBuild or Visual Studio to be used**. See [supported languages and frameworks](https://codeql.github.com/docs/codeql-overview/supported-languages-and-frameworks/) for a list of which compilers are supported.

### How does the HLK verify that my driver was scanned by CodeQL?

The Static Tools Logo Test in the HLK is the test that enforces this requirement. Details on the Static Tools Logo Test can be found on its [MS Docs page](/windows-hardware/test/hlk/testref/6ab6df93-423c-4af6-ad48-8ea1049155ae).

### Are all defects reported by CodeQL true defects?

Every CodeQL query has varying levels of precision. Our goal is to minimize false positives, but occasionally they will occur. Our suite of "Must-Fix" queries have been developed and hand-picked for use with the WHCP program because our extensive testing results in nearly zero false positives. If you are seeing false positives from a query in the set of "Must-Fix" queries, email `stlogohelp@microsoft.com` immediately or file an issue on the [Windows-Driver-Developer-Supplemental-Tools repo](https://github.com/microsoft/Windows-Driver-Developer-Supplemental-Tools/issues), and we will work to get it resolved as soon as possible.

### Does a query's classification of either "warning" or "error" matter for the purposes of the Static Tools Logo Test?

Queries are classified using statuses such as "error" "warning" and "problem" in CodeQL but this classification is separate from how the Windows Hardware Compatibility Program and specifically the Static Tools Logo Test will grade the results. Any driver with defects from any query within the "Must-Fix" suite will **not pass** the Static Tools Logo Test and will **fail to be certified**, regardless of the query classification in the raw query file (ex. "warning").

### Can I generate a DVL on Visual Studio solutions?

No, DVL generation must be run at the project level and cannot be run on [Visual Studio solutions](/visualstudio/get-started/tutorial-projects-solutions). Instructions for how to generate a DVL can be found at: [Creating a Driver Verification Log](../develop/creating-a-driver-verification-log.md).

### Can I generate a Driver Verification Log (DVL) outside of the context of msbuild or Visual Studio?

As part of the Windows Driver Kit (WDK) and Enterprise WDK (eWDK), Microsoft ships a component called *dvl.exe* which can be used to generate Driver Verification Logs (DVLs). Starting in WDK/eWDK preview versions 21342 and above, it is possible to generate a DVL from the command line outside of the context of msbuild or Visual Studio by passing a driver name and architecture. See [Creating a Driver Verification Log](../develop/creating-a-driver-verification-log.md) for more details.

### I have comments or questions around how to use CodeQL on my driver, where do I send feedback?

Send feedback and questions to [stlogohelp@microsoft.com](mailto:stlogohelp@microsoft.com). 
