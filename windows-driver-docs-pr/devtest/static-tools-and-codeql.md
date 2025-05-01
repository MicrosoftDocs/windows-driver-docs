---
title: CodeQL and the Static Tools Logo Test
description: Using Static tools and CodeQL on Windows driver source code to discover and repair any issues that are deemed Must-Fix
keywords:
- dynamic verification tools WDK
- static verification tools WDK
ms.date: 04/03/2024
---

# CodeQL and the Static Tools Logo Test

Microsoft is committed to mitigating the attack surface for the Windows operating system, and ensuring that third party drivers meet a strong security bar is critical to accomplishing that goal. One step in setting this security bar is the requirement to the [Windows Hardware Compatibility Program](/windows-hardware/design/compatibility) (WHCP) which states that all driver submissions must use the [CodeQL](https://codeql.github.com/) engine on driver source code and fix any violations that are deemed *Must-Fix* .

## CodeQL and Driver Security

[CodeQL](https://codeql.github.com/), by GitHub, is a powerful semantic code analysis engine, and the combination of an extensive suite of high-value security queries along with a robust platform make it an invaluable tool for securing driver code.

Usage of CodeQL for the purpose of WHCP testing is acceptable under the **[Hardware Lab Kit (HLK)](/windows-hardware/test/hlk/) End User License Agreement**. For WHCP participants, the HLK's EULA overwrites GitHub's CodeQL Terms and Conditions by stating that CodeQL **can be used** during automated analysis, CI or CD, as part of normal engineering processes for the purposes of analyzing drivers to be submitted and certified as part of the WHCP.

This requirement to analyze driver source code and fix any *Must-Fix* violations will be enforced by the [Static Tools Logo Test](/windows-hardware/test/hlk/testref/6ab6df93-423c-4af6-ad48-8ea1049155ae).

This topic describes how to:

- Determine which *Must-Fix* [queries](#must-fix-queries) must be run for WHCP certification.
- Use CodeQL to analyze your driver source code for known high impact security issues.
- Create a [Driver Verification Log](#6-convert-sarif-to-driver-verification-log-format-dvl) that the [Static Tools Logo Test](/windows-hardware/test/hlk/testref/6ab6df93-423c-4af6-ad48-8ea1049155ae) can consume to certify your driver code.

> [!IMPORTANT]
> Windows Hardware Compatibility Program requires CodeQL for Static Tool Logo (STL) Tests on our Client and Server Operating Systems. We will continue to maintain support for SDV and CA on older products. Partners are highly encouraged to review the CodeQL requirements for the [Static Tool Logo Test](/windows-hardware/test/hlk/testref/6ab6df93-423c-4af6-ad48-8ea1049155ae).

### HLK EULA and CodeQL

Usage of CodeQL for the purpose of certifying for the Windows Hardware Compatibility Program testing is acceptable under the [Hardware Lab Kit (HLK)](/windows-hardware/test/hlk/) End User License Agreement. For WHCP participants, the HLK's EULA overwrites GitHub's CodeQL Terms and Conditions. The HLK EULA states that CodeQL can be used during automated analysis, CI or CD, as part of normal engineering processes for the purposes of analyzing drivers to be submitted and certified as part of the Windows Hardware Compatibility Program. For those following along for general use, read the [GitHub CodeQL Terms and Conditions](https://github.com/github/codeql-cli-binaries/blob/main/LICENSE.md) and/or [contact CodeQL](https://support.github.com/contact).

## CodeQL Concepts

CodeQL is a static analysis engine used by developers to perform security analysis on code outside of a live environment. CodeQL ingests code while it is compiling, and builds a database from it. The database becomes a directory containing queryable data, a source reference, and log files. Once the database is built, one can run analysis on it by utilizing CodeQL queries (also called checks or rules) which will determine if the source code contains violations or security vulnerabilities. CodeQL provides a library of standard queries which check for language correctness, semantics, and provides great value to developers who wish to ensure their code is free of bugs and vulnerabilities.

CodeQL also provides the option to build custom queries. For more information on writing custom queries, see [Writing queries](https://codeql.github.com/docs/writing-codeql-queries/codeql-queries/) in the CodeQL docs.

CodeQL also provides a [CodeQL command line tool (CLI)](https://codeql.github.com/docs/codeql-cli/) to easily perform CodeQL actions and/or perform large scale analysis.

Supplementary CodeQL CLI documentation can be found at [CodeQL Getting Started](https://codeql.github.com/docs/codeql-cli/getting-started-with-the-codeql-cli/).

## 1. Select the CodeQL version

Select the tab for your scenario.

## [For Windows Hardware Compatibility Program Use](#tab/whcp)

Use this matrix to determine the versions to be downloaded.

| Windows Release          | CodeQL CLI version                                    | microsoft/windows-drivers CodeQL pack version| codeql/cpp-queries CodeQL pack version  | Branch to use|
|--------------------------|-------------------------------------------------------|-----------------------------------------|-----------------------------|--------------|
| Windows Server 2022      | [2.4.6](https://github.com/github/codeql-cli-binaries/releases/tag/v2.4.6) or [2.21.2](https://github.com/github/codeql-cli-binaries/releases/tag/v2.21.2)|  1.0.13 (If using codeql 2.21.2) | 0.9.0 (If using codeql 2.21.2) | WHCP_21H2 |
| Windows 11               | [2.4.6](https://github.com/github/codeql-cli-binaries/releases/tag/v2.4.6) or [2.21.2](https://github.com/github/codeql-cli-binaries/releases/tag/v2.21.2)|  1.0.13 (If using codeql 2.21.2) | 0.9.0 (If using codeql 2.21.2) | WHCP_21H2 |
| Windows 11, version 22H2 | [2.6.3](https://github.com/github/codeql-cli-binaries/releases/tag/v2.6.3) or [2.21.2](https://github.com/github/codeql-cli-binaries/releases/tag/v2.21.2)|  1.0.13 (If using codeql 2.21.2) | 0.9.0 (If using codeql 2.21.2) | WHCP_22H2 |
| Windows 11, version 23H2 | [2.6.3](https://github.com/github/codeql-cli-binaries/releases/tag/v2.6.3) or [2.21.2](https://github.com/github/codeql-cli-binaries/releases/tag/v2.21.2)|  1.0.13 (If using codeql 2.21.2) | 0.9.0 (If using codeql 2.21.2) | WHCP_22H2 |
| Windows 11, version 24H2 | [2.21.2](https://github.com/github/codeql-cli-binaries/releases/tag/v2.21.2)  |  1.1.0          |        0.9.0                 |  WHCP_24H2  |

A version of the CodeQL pack is not specified for CodeQL CLI 2.4.6 and 2.6.3 because only newer versions of CodeQL support CodeQL packs.

## [For General Use](#tab/general)

For general use of CodeQL with other versions of Windows outside of the WHCP program, or for developing and testing queries, we currently recommend the following version and branch:

| CodeQL CLI version                                                           | microsoft/windows-drivers CodeQL pack version | codeql/cpp-queries version | Branch to use |
|------------------------------------------------------------------------------|------------------------------------------|----------------------------|---------------|
| [2.21.2](https://github.com/github/codeql-cli-binaries/releases/tag/v2.21.2) | latest                                   | latest                     | main          |

---


## 2. Download and Install CodeQL

> [!NOTE]
> Visual Studio 17.8 broke compatibility with the older versions of CodeQL used in the WHCP_21H2 and WHCP_22H2 branches. CodeQL CLI version 2.21.2 has been validated for use with WHCP 21H2 and WHCP 22H2 when using Visual Studio 17.8 or greater.
> For the WHCP Program, use the CodeQL CLI version in accordance with the previous table and Windows release you are certifying for - version 2.4.6, version 2.6.3, or version 2.21.2.
> For general use with the main branch, use CodeQL CLI version 2.21.2.

1. Create a directory to contain CodeQL. This example uses `C:\codeql-home\`

   ```console
   C:\> mkdir C:\codeql-home
   ```

1. Refer to the previous tables to select which version of CodeQL CLI to use in accordance with the desired branch of Microsoft's driver queries. If you are performing analysis as part of the WHCP program, refer to the table **For Windows Hardware Compatibility Program Use** otherwise use Main branch and [2.21.2](https://github.com/github/codeql-cli-binaries/releases/tag/v2.21.2). Using a different version may result in a database incompatible with the libraries.

1. Navigate to the CodeQL CLI binaries release associated with the previous tables, and download the zip file in accordance with your project's architecture. For example, for 64 bit Windows *codeql-win64.zip*.

1. Extract Codeql CLI directory to the one you just created, for example: C:\codeql-home\codeql\.

1. Verify CodeQL is installed correctly by checking the version:

   ```console
    C:\codeql-home\codeql>codeql --version
    CodeQL command-line toolchain release 2.21.2.
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
<!-- Make this a tab section  -->

#### Install CodeQL Packages

#### For WHCP_21H2 and WHCP_22H2 branches

If using Visual Studio 2022 17.8 or greater with WHCP_21H2 or WHCP_22H2 and CodeQL CLI version 2.21.2:

- Follow the steps for [ALL OTHER BRANCHES](#all-other-branches).
- **Make sure to remove the CodeQL submodule if you still have an old version of the repo cloned.** CodeQL might try to use the queries in the submodule by default, which will cause errors because of mismatched versions.

If using Visual Studio version 17.7 or earlier **AND** either WHCP_21H2 or WHCP_22H2 AND CodeQL CLI version 2.4.6 or 2.6.3:

- Follow [Special instructions for WHCP_21H2 and WHCP_22H2 using VS17.7 or earlier](#special-instructions-for-whcp_21h2-and-whcp_22h2-using-vs177-or-earlier) in this article.

#### ALL OTHER BRANCHES

##### Download the CodeQL query packages

It is no longer necessary to clone the Windows-Driver-Developer-Supplemental-Tools repo to use the queries for certification. CodeQL packs are now used.

1. Download the correct version of the microsoft/windows-drivers pack from the [Windows Hardware Compatibility Program Use](#1-select-the-codeql-version) table. Specify the `@<version>` in the following command.

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

> [!IMPORTANT]
> Do not change this directory or move the installed pack.

##### Download the Windows driver query suites

Locate and copy the two primary query suite files to the local PC.

- *windows_driver_recommended.qls*
- *windows_driver_mustfix.qls*

Details of the queries are shown in [Queries and Suites](../devtest/codeql-queries.md); the two query files are located at [https://github.com/microsoft/Windows-Driver-Developer-Supplemental-Tools/tree/main/suites](https://github.com/microsoft/Windows-Driver-Developer-Supplemental-Tools/tree/main/suites).

## 2. Build the CodeQL Database

These examples assume use of a Windows development environment and that the installation location is C:\codeql-home, but you can use the setup that suits you. See [CodeQL supported languages and frameworks](https://codeql.github.com/docs/codeql-overview/supported-languages-and-frameworks/) for a list of which compilers are supported.

1. Create a directory for CodeQL to place the databases it creates. For example: C:\codeql-home\databases

    ```console
    mkdir C:\codeql-home\databases
    ```

1. Use the CodeQL command to create a database using the following parameters:

    - the first parameter is a link to your database directory. For example: C:\codeql-home\databases\MyDriverDatabase (Note: this command will fail if the directory already exists).
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

For more information or help using the `database create` command, see [Creating CodeQL Databases](https://codeql.github.com/docs/codeql-cli/creating-codeql-databases/) or use the following command:

```console
C:\codeql-home\codeql> codeql database create --help
```

## 3. Perform Analysis

> [!NOTE]
> If using Visual Studio version 17.7 or earlier **AND** either WHCP_21H2 or WHCP_22H2 AND CodeQL VLI version 2.4.6 or 2.6.3, follow the step0s in [Special instructions for WHCP_21H2 and WHCP_22H2 using VS17.7 or earlier](#special-instructions-for-whcp_21h2-and-whcp_22h2-using-vs177-or-earlier).

At this point, the database creation is complete and the next step is to perform the actual analysis on the driver source code.

1. Use the CodeQL command to analyze your database using the following parameters:

    - the first parameter is a link to your database directory. For example, *C:\codeql-home\databases\MyDriverDatabase*. (Note: this command will fail if the directory doesn't exist.)
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
    codeql database analyze --download D:\DriverDatabase suites/windows\_driver_recommended.qls --format=sarifv2.1.0 --output=D:\DriverAnalysis1.sarif 
    ```

    For more information or help using the `database analyze` command, see [Analyzing Databases with the CodeQL CLI](https://codeql.github.com/docs/codeql-cli/analyzing-databases-with-the-codeql-cli/) and [Using a CodeQL pack to analyze a CodeQL database](https://docs.github.com/en/code-security/codeql-cli/using-the-advanced-functionality-of-the-codeql-cli/publishing-and-using-codeql-packs#using-a-codeql-pack-to-analyze-a-codeql-database).

    For command line help use the following command:

    ```console
    C:\codeql-home\codeql> codeql database analyze --help
    ```

## Special instructions for WHCP_21H2 and WHCP_22H2 using VS17.7 or earlier

These instructions only apply when using both Visual Studio 17.7 or earlier, along with CodeQL 2.6.3 or 2.4.6

1. Install CodeQL version as indicated in above steps.

2. Clone and install the Windows Driver Developer Supplemental Tools repository which contains the CodeQL queries specific for drivers:

    `git clone https://github.com/microsoft/Windows-Driver-Developer-Supplemental-Tools.git --recurse-submodules`

3. Refer to the [Windows Hardware Compatibility Program Use](#1-select-the-codeql-version) table to identify the correct branch for the version of Windows you wish to certify for.

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

7. Refer to other guidance in this document for next steps, such as viewing the test results and creating a Driver Verification Log. 

## 4. View and Interpret Results

We will be focusing on SARIF format for this section as it is what is required for the following steps, though you are welcome to use CSV format if it suits your needs better.

Static Analysis Results Interchange Format (SARIF) is a JSON type format used for sharing static analysis results. Read more about the standard at [OASIS Static Analysis Results Interchange Format (SARIF)](https://github.com/oasis-tcs/sarif-spec), how CodeQL uses [SARIF Output](https://codeql.github.com/docs/codeql-cli/sarif-output/#sarif-output), and [the schema json](https://github.com/oasis-tcs/sarif-spec/blob/main/sarif-2.1/schema/sarif-schema-2.1.0.json).

There are several methods for interpreting the analysis results, including manually sorting through the objects. Here are a few that we use:

- The [Microsoft Sarif Viewer (Web)](https://microsoft.github.io/sarif-web-component/) has functionality which allows you to drag and drop your SARIF file into the viewer, then displays results categorized by rule. This is a very quick and easy way to see the count of violations or which queries have violations, but less easy to find source code information aside from the line number. Note that the page will not update if there are no violations.

- The [Microsoft SARIF Viewer for Visual Studio](https://marketplace.visualstudio.com/items?itemName=WDGIS.MicrosoftSarifViewer) is great for displaying the results within Visual Studio for seamless transition from results to source code.

- The [SARIF extension for Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=MS-SarifVSCode.sarif-viewer) opens a preview pane and displays any errors, warnings, or problems reported by CodeQL. To display the Sarif file in a readable format, open the file in Visual Studio Code and select *Shift-Alt-F*. 

The most important section of the SARIF file is the `Results` property within the `Run` object. Each query will have a Results property with details about any detected violations and where it occurred. If no violations are found, the property value will be empty.

Queries are classified using statuses such as *error*, *warning*, and *problem* but this classification is separate from how the Windows Hardware Compatibility Program and specifically the Static Tools Logo Test will grade the results. Any driver with defects from any query within the *Must-Fix* suite will **not pass** the Static Tools Logo Test and will **fail to be certified**, regardless of the query classification in the raw query file (for example, *warning*).

## 5. Suppressing CodeQL Results (Optional)

CodeQL for drivers supports suppressing results. Suppressions are currently provided as a convenience to help developers triage issues and reduce noise, not as a way to bypass the *Must-Fix*  checks. They have no impact on generating a Driver Verification Log or passing the Static Tools Logo test at this time. To use suppressions, you must run the DriverAlertSuppression.ql query at the same time as the other queries or suites you wish to run. By default, this query is enabled when running our suites from our githubs main/development branch.

For checks that have been ported from Code Analysis, existing Code Analysis suppressions will be honored. For more information, see [C++ warning pragma](/cpp/preprocessor/warning).

- `Known limitation:` You cannot combine a #pragma(disable) and #pragma(suppress) in the same line at this time.

For checks that are new to CodeQL, you can suppress them by doing one of two things:

- Write a “#pragma(suppress:the-rule-id-here)” annotation (minus quotes) on the line above the violation, as you would for Code Analysis. “the-rule-id-here” can be replaced by the @id value in a given query’s metadata, viewable at the top of the file.

- Write a comment on the line above comprised of the text “lgtm[the-rule-id-here]” (minus quotes). You will need to run the standard [C/C++ alert suppression query](https://github.com/github/codeql/blob/main/cpp/ql/src/AlertSuppression.ql) instead of the driver alert suppression query. 

Once a suppression is present and recognized, the resulting SARIF file will include data that a result was suppressed, and most result viewers will not show the result by default.

## 6. Convert SARIF to Driver Verification Log Format (DVL)

The Static Tools Logo Test parses a [Driver Verification Log (DVL)](../develop/creating-a-driver-verification-log.md), which is the compiled results from the CodeQL static analysis you ran on the driver source code. There are three ways to convert your SARIF file to DVL format: Visual Studio, MSBuild, or from the command line using the *dvl.exe* tool. For complete steps, see [Creating a Driver Verification Log](../develop/creating-a-driver-verification-log.md).
<!-->

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

-->

Further instructions for the Static Tools Logo HLK Test and guidance on where to place the DVL file can be found in [Running the Static Tools Logo test](/windows-hardware/test/hlk/testref/6ab6df93-423c-4af6-ad48-8ea1049155ae#running-the-test).

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

1. In the driver project, navigate to project properties. In the  **Configuration** pull down, select the build configuration that you wish to check with CodeQL - we recommend **Release**. Creating the CodeQL database and running the queries takes a few minutes, so we don't recommend you run CodeQL on the Debug configuration of your project.

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

If you are certifying with WHCP, first ensure you are using the HLK version associated with the Windows release you are targeting, the associated branch in the Windows Driver Developer Supplemental Tools repository, and the subsequent CodeQL CLI version. For HLK/Windows Release compatibility matrix, see [Windows Hardware Lab Kit](/windows-hardware/test/hlk/) and for Windows Release/Windows Driver Developer Supplemental Tools repo branch/CodeQL CLI version, see the WHCP table in the [Select the CodeQL version](#1-select-the-codeql-version) section.

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

## Frequently Asked Questions (FAQ's)

### When will this be required for device certification?

See the [Windows Hardware Compatibility Program Certification Process](/windows-hardware/design/compatibility/whcp-certification-process) to for requirement details.

### What is the motivation behind requiring CodeQL be run on driver source code?

The motivation for requiring CodeQL to be run on driver source code can be summarized by two main reasons:

1. Security of Windows is paramount and requiring CodeQL to be run on driver source code is one step in helping improve the security of components which get certified by Microsoft.
1. CodeQL queries are actively developed by security engineers at Microsoft, as Microsoft is committed to ensuring that its hardware ecosystem benefits from the same high-quality tooling that is used at Microsoft.

### What types of drivers do CodeQL and the Static Tools Logo test apply to?

At present, the Static Tools Logo test requires that CodeQL be run and the *Must-Fix* set of queries passed for all kernel-mode drivers excluding graphics drivers. Note that running CodeQL on graphics drivers is **highly recommended** even though it is not currently required. Some queries may also find useful defects in user-mode components.

We anticipate extending the test and its queries to require results for graphics drivers, user-mode drivers and driver components, and other driver package components in the future. If you encounter unexpected behavior or false positives running CodeQL on graphics drivers or user-mode drivers, please file an issue on the [Windows-Driver-Developer-Supplemental-Tools repo](https://github.com/microsoft/Windows-Driver-Developer-Supplemental-Tools).

### Which license governs the usage of CodeQL for driver developers?

Usage of CodeQL for the purpose of WHCP testing is acceptable under the **[Hardware Lab Kit (HLK)](/windows-hardware/test/hlk/) End User License Agreement**. For WHCP participants, the HLK's EULA overwrites GitHub's CodeQL Terms and Conditions. The HLK EULA states that CodeQL **can be used** during automated analysis, CI or CD, as part of normal engineering processes for the purposes of analyzing drivers to be submitted and certified as part of the WHCP.

### Do I need to use Visual Studio or msbuild to run CodeQL?

CodeQL **does not require MSBuild or Visual Studio to be used**. See [supported languages and frameworks](https://codeql.github.com/docs/codeql-overview/supported-languages-and-frameworks/) for a list of which compilers are supported.

### How does the HLK verify that my driver was scanned by CodeQL?

The Static Tools Logo Test in the HLK is the test that enforces this requirement. Details on the Static Tools Logo Test can be found on its [MS Docs page](/windows-hardware/test/hlk/testref/6ab6df93-423c-4af6-ad48-8ea1049155ae).

### Are all defects reported by CodeQL true defects?

Every CodeQL query has varying levels of precision. Our goal is to minimize false positives, but occasionally they will occur. Our suite of *Must-Fix*  queries have been developed and hand-picked for use with the WHCP program because our extensive testing results in nearly zero false positives. If you are seeing false positives from a query in the set of *Must-Fix*  queries, email `stlogohelp@microsoft.com` immediately or file an issue on the [Windows-Driver-Developer-Supplemental-Tools repo](https://github.com/microsoft/Windows-Driver-Developer-Supplemental-Tools/issues), and we will work to get it resolved as soon as possible.

### Does a query's classification of either "warning" or "error" matter for the purposes of the Static Tools Logo Test?

Queries are classified using statuses such as *error*, *warning*, or *proble* in CodeQL but this classification is separate from how the Windows Hardware Compatibility Program and specifically the Static Tools Logo Test will grade the results. Any driver with defects from any query within the *Must-Fix*  suite will **not pass** the Static Tools Logo Test and will **fail to be certified**, regardless of the query classification in the raw query file (for example, *warning*).

### Can I generate a DVL on Visual Studio solutions?

No, DVL generation must be run at the project level and cannot be run on [Visual Studio solutions](/visualstudio/get-started/tutorial-projects-solutions). Instructions for how to generate a DVL can be found at: [Creating a Driver Verification Log](../develop/creating-a-driver-verification-log.md).

### Can I generate a Driver Verification Log (DVL) outside of the context of msbuild or Visual Studio?

As part of the Windows Driver Kit (WDK) and Enterprise WDK (eWDK), Microsoft ships a component called *dvl.exe* which can be used to generate Driver Verification Logs (DVLs). Starting in WDK/eWDK preview versions 21342 and later, it is possible to generate a DVL from the command line outside of the context of msbuild or Visual Studio by passing a driver name and architecture. See [Creating a Driver Verification Log](../develop/creating-a-driver-verification-log.md) for more details.

### I have comments or questions around how to use CodeQL on my driver, where do I send feedback?

Send feedback and questions to [stlogohelp@microsoft.com](mailto:stlogohelp@microsoft.com). 
