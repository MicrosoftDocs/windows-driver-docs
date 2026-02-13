---
title: Run CodeQL Analysis for Windows Driver Certification
description: Learn how to use CodeQL analysis on Windows driver source code to identify and fix Must-Fix issues for certification.
keywords:
- dynamic verification tools WDK
- static verification tools WDK
ms.date: 02/12/2026
ms.topic: how-to
---

# Run CodeQL Analysis on Windows Driver Code

CodeQL is a powerful static analysis engine that helps developers identify security vulnerabilities and code violations in Windows driver source code. This article explains how to use CodeQL analysis to create a Driver Verification File for Windows Hardware Compatibility Program (WHCP) certification.

In this article, you:  

- Install the appropriate CodeQL version.  
- Install the necessary CodeQL packages and query suites.  
- Run CodeQL to build a database and analyze your code.  
- Build a Driver Verification File.  

## Select the appropriate CodeQL version for your driver

> [!NOTE]
> Visual Studio (VS) 17.8 broke compatibility with older versions of CodeQL used in the WHCP_21H2 and WHCP_22H2 branches.
 CodeQL CLI version 2.15.4 is validated for use with WHCP 21H2 and WHCP 22H2 when using Visual Studio 17.8 or greater. When using Visual Studio 17.7 or earlier, use version 2.4.6 or version 2.6.3. For the WHCP Program, use the CodeQL CLI version and Windows release you're certifying for, per the following table. 

Select the tab for your scenario:

## [For Windows Hardware Compatibility Program Use](#tab/whcp)

Use this matrix to determine the versions to be downloaded.

| Windows Release          | CodeQL CLI version                                    | microsoft/windows-drivers CodeQL pack version | microsoft/cpp-queries CodeQL pack version | codeql/cpp-queries version | Associated branch |
|--------------------------|-------------------------------------------------------|-----------------------------------------------|-----------------------------------------|---------------|-----------|
| Windows Server 2022      | [2.4.6](https://github.com/github/codeql-cli-binaries/releases/tag/v2.4.6) or [2.15.4](https://github.com/github/codeql-cli-binaries/releases/tag/v2.15.4) | 1.0.13 (If using codeql 2.15.4)  | N/A   | 0.9.0 (If using codeql 2.15.4) | [WHCP_21H2](https://github.com/microsoft/Windows-Driver-Developer-Supplemental-Tools/tree/WHCP_21H2)     |
| Windows 11               | [2.4.6](https://github.com/github/codeql-cli-binaries/releases/tag/v2.4.6) or [2.15.4](https://github.com/github/codeql-cli-binaries/releases/tag/v2.15.4) | 1.0.13 (If using codeql 2.15.4)  | N/A   | 0.9.0 (If using codeql 2.15.4) | [WHCP_21H2](https://github.com/microsoft/Windows-Driver-Developer-Supplemental-Tools/tree/WHCP_21H2)     |
| Windows 11, version 22H2 | [2.6.3](https://github.com/github/codeql-cli-binaries/releases/tag/v2.6.3) or [2.15.4](https://github.com/github/codeql-cli-binaries/releases/tag/v2.15.4) | 1.0.13 (If using codeql 2.15.4)  | N/A   | 0.9.0 (If using codeql 2.15.4) | [WHCP_22H2](https://github.com/microsoft/Windows-Driver-Developer-Supplemental-Tools/tree/WHCP_22H2)     |
| Windows 11, version 23H2 | [2.6.3](https://github.com/github/codeql-cli-binaries/releases/tag/v2.6.3) or [2.15.4](https://github.com/github/codeql-cli-binaries/releases/tag/v2.15.4) | 1.0.13 (If using codeql 2.15.4)  | N/A   | 0.9.0 (If using codeql 2.15.4) | [WHCP_22H2](https://github.com/microsoft/Windows-Driver-Developer-Supplemental-Tools/tree/WHCP_22H2)     |
| Windows 11, version 24H2 | [2.15.4](https://github.com/github/codeql-cli-binaries/releases/tag/v2.15.4)                                                                               | 1.1.0                            | N/A   | 0.9.0                          | [WHCP_24H2](https://github.com/microsoft/Windows-Driver-Developer-Supplemental-Tools/tree/WHCP_24H2)      |
| Windows Server 2025      | [2.20.1](https://github.com/github/codeql-cli-binaries/releases/tag/v2.20.1)                                                                               | 1.8.0                            | 0.0.4 | N/A                            | [WHCP_25H2](https://github.com/microsoft/Windows-Driver-Developer-Supplemental-Tools/tree/WHCP_25H2)     |
| Windows 11, version 25H2 | [2.20.1](https://github.com/github/codeql-cli-binaries/releases/tag/v2.20.1)                                                                               | 1.8.0                            | 0.0.4 | N/A                            | [WHCP_25H2](https://github.com/microsoft/Windows-Driver-Developer-Supplemental-Tools/tree/WHCP_25H2)     |
| Windows 11, version 26H1 | [2.24.1](https://github.com/github/codeql-cli-binaries/releases/tag/v2.24.1)                                                                               | 1.8.2                            | 0.0.4 | N/A                            | [WHCP_26H1](https://github.com/microsoft/Windows-Driver-Developer-Supplemental-Tools/tree/WHCP_26H1)     |

> [!NOTE]
> A version of the CodeQL pack isn't specified for CodeQL CLI 2.4.6 and 2.6.3 because only versions of CodeQL later than v2.7.0 support CodeQL packs.

### CodeQL versions validated for use with WHCP

For the most recent version information, including testing the latest in development, see [Windows driver developer supplemental tools](https://github.com/microsoft/Windows-Driver-Developer-Supplemental-Tools/blob/main/README.md).


| CodeQL CLI version |
|--------------------|
| 2.24.1 |
| 2.23.3 |
| 2.21.4 |
| 2.21.2 |
| 2.20.1 |
| 2.15.4 |

## [For General Use](#tab/general)

For general use of CodeQL with other versions of Windows outside of the WHCP program, or for developing and testing queries, we currently recommend the following version and branch:

| CodeQL CLI version                                                           | microsoft/windows-drivers CodeQL pack version | microsoft/cpp-queries version | Branch to use |
|------------------------------------------------------------------------------|-----------------------------------------------|----------------------------|---------------|
| [2.24.1 or greater](https://github.com/github/codeql-cli-binaries/releases/tag/v2.24.1) | [Latest stable version](https://github.com/microsoft/Windows-Driver-Developer-Supplemental-Tools/pkgs/container/windows-drivers) | [0.0.4](https://github.com/orgs/microsoft/packages/container/package/cpp-queries)  | main          |

---

## Download and Install CodeQL

1. Create a directory to contain CodeQL. This example uses `C:\codeql-home\`

   ```console
   C:\> mkdir C:\codeql-home
   ```

1. Refer to the previous tables to select which version of CodeQL CLI to use in accordance with the desired branch of Microsoft's driver queries. If you're performing analysis as part of the WHCP program, refer to the table **For Windows Hardware Compatibility Program Use**, otherwise use Main branch and the version of the CLI listed in the GitHub README or the preceding "for general use" table. Using a different version may result in a database incompatible with the libraries.

1. Navigate to the CodeQL CLI binaries release associated with the previous tables, and download the zip file in accordance with your project's architecture. For example, for 64 bit Windows *codeql-win64.zip*.

1. Extract the Codeql CLI directory to the one you created, for example: *C:\codeql-home\codeql\*.

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

### Using CodeQL help

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

For help on a specific command, run *codeql \<command\> --help*. For example:  

`codeql create --help`  

To get help for subcommands, list them hierarchically, for example 

`codeql create language --help` 

## Install the CodeQL Packages

Select the tab for your build environment:

## [VS 17.8 or greater and CodeQL 2.15.4 or later](#tab/latest)

Use this procedure if you're using Visual Studio 2022 17.8 or greater for WHCP certification for 21H2 or later and CodeQL CLI version 2.15.4 or later.

> [!NOTE]
> If you ran CodeQL tests with an earlier version of CodeQL, make sure to remove the old CodeQL submodule if you still have an old version of the cloned repo. CodeQL might try to use the queries in the submodule by default, which may cause errors because of mismatched versions.

### Download the CodeQL query packages

CodeQL introduced CodeQL Packages (*CodeQL packs* or *query packs*) in version 2.7.0, eliminating the need to clone the *Windows-Driver-Developer-Supplemental-Tools* repo to use the queries for certification.

1. Download the correct version of the microsoft/windows-drivers pack from the [Windows Hardware Compatibility Program Use](#select-the-appropriate-codeql-version-for-your-driver) table. Specify the `@<version>` in the following command.

```console
C:\codeql-home\> codeql pack download microsoft/windows-drivers@<version>
```

For example, if you're certifying for WHCP 26H1, run the following command to download the 1.8.2 windows-drivers query pack:

```console
C:\codeql-home\> codeql pack download microsoft/windows-drivers@1.8.2
```

Use this command to download version 0.0.4 of the Microsoft cpp-queries query pack.

```console
C:\codeql-home\> codeql pack download microsoft/cpp-queries@0.0.4
```

CodeQL installs the query packs to the default directory:

`C:\Users\<current user>\.codeql\packages\microsoft\windows-drivers\<downloaded version>\`

> [!IMPORTANT]
> Don't change the install directory or move the installed query pack.

Microsoft provides three query suites to simplify the end-to-end driver developer workflow. These suites are included in the microsoft/windows-drivers CodeQL pack.

- *recommended.qls* contains queries recommended for driver developers to run and evaluate the results of. We recommend running this suite by default and reviewing results.
- *mustrun.qls* serves as a subset of *recommended.qls* and contains queries that **must be run** in order to pass WHCP certification. These queries may not necessarily need to be fixed due to potential false positives, but should have their results reviewed and any real bugs found fixed. A DVL generated without results for these checks fails the Static Tools Logo test.
- *mustfix.qls* serves as a further subset and contains queries that report issues that **must be fixed** in order to pass WHCP certification. A DVL generated with failures in these rules fails the Static Tools Logo test.

For details of the contents of the query suites, see [CodeQL Queries and Suites](../devtest/codeql-queries.md).

### Build the CodeQL Database

These examples assume use of a Windows development environment and that the installation location is C:\codeql-home, but you can use the setup that suits you. See [CodeQL supported languages and frameworks](https://codeql.github.com/docs/codeql-overview/supported-languages-and-frameworks/) for a list of which compilers are supported.

1. Create a directory for CodeQL to place the databases it creates. For example: C:\codeql-home\databases

    ```console
    mkdir C:\codeql-home\databases
    ```

1. Use the CodeQL command to create a database with these parameters:

    - The first parameter is a link to your database directory. For example, C:\codeql-home\databases\MyDriverDatabase. (This command fails if the directory already exists.)  
    - `--language` or `-l` specifies the language or languages your source code is in. This parameter can be a comma-separated list, such as [cpp, javascript].  
    - `--source-root` or `-s` specifies the path to your source code.  
    - `--command` or `-c` specifies your build command or the path to your build file.  

    ```console
    codeql database create <path to new database> --language=<cpp> --source-root=<driver parent directory> --command=<build command or path to build file>
    ```

#### Examples

Single driver example.

 ```console
C:\codeql-home\codeql> codeql database create D:\DriverDatabase --language=cpp --source-root=D:\Drivers\SingleDriver --command="msbuild /t:rebuild D:\Drivers\SingleDriver\SingleDriver.sln"
```

Multiple drivers example.

 ```console
C:\codeql-home\codeql> codeql database create D:\SampleDriversDatabase --language=cpp --source-root=D:\AllMyDrivers\SampleDrivers --command=D:\AllMyDrivers\SampleDrivers\BuildAllSampleDrivers.cmd
```

For more information or help using the `database create` command, see [Creating CodeQL Databases](https://codeql.github.com/docs/codeql-cli/creating-codeql-databases/) or [Using CodeQL help](#using-codeql-help).

### Perform Analysis

At this point, the database creation is complete and the next step is to perform the actual analysis on the driver source code.

1. Use the CodeQL command to analyze your database using the following parameters:

    - the first parameter is a link to your database directory. For example, *C:\codeql-home\databases\MyDriverDatabase*. (Note: this command fails if the directory doesn't exist.)
    - `--format` is the file type of the output file. Options include: SARIF and CSV. (**For WHCP Users** use SARIF format.)
    - `--output` is the path to where you want the output file, be sure to include the format in the file name. (This command fails if the directory doesn't already exist.)
    - the query specifiers parameter is a space separated list of arguments that can include:
        - a path to a query file
        - a path to a directory containing query files
        - a path to a query suite file
        - the name of a CodeQL query pack

    ```console
    codeql database analyze <path to database> <path to query suite .qls file> --format=sarifv2.1.0 --output=<outputname>.sarif
    ```

    Example:

    ```console
    codeql database analyze D:\DriverDatabase microsoft/windows-drivers:windows-driver-suites/recommended.qls --format=sarifv2.1.0 --output=D:\DriverAnalysis1.sarif
    ```

    For more information or help using the `database analyze` command, see [Analyzing Databases with the CodeQL CLI](https://codeql.github.com/docs/codeql-cli/analyzing-databases-with-the-codeql-cli/), [Using a CodeQL pack to analyze a CodeQL database](https://docs.github.com/en/code-security/codeql-cli/using-the-advanced-functionality-of-the-codeql-cli/publishing-and-using-codeql-packs#using-a-codeql-pack-to-analyze-a-codeql-database), or [Using CodeQL help](#using-codeql-help).

<!-- end tab 1 -->

## [VS 17.7 or earlier and CodeQL 2.4.6 or 2.6.3 ](#tab/earlier)

These instructions only apply when using both Visual Studio 17.7 or earlier, along with CodeQL 2.6.3 or 2.4.6.

2. Clone and install the Windows Driver Developer Supplemental Tools repository that contains the CodeQL queries specific for drivers:

    `git clone https://github.com/microsoft/Windows-Driver-Developer-Supplemental-Tools.git --recurse-submodules`

3. Refer to the [Windows Hardware Compatibility Program Use](#select-the-appropriate-codeql-version-for-your-driver) table to identify the correct branch for the version of Windows you wish to certify for.

4. Use the `git checkout` command to check out the identified branch.

5. Confirm that the submodules are present in the codeql-home directory.

   ```text
    D:/codeql-home
        |--- codeql
        |--- Windows-Driver-Developer-Supplemental-Tools
   ```

1. Build the CodeQL Database
    1.  Create a directory for CodeQL to place the databases it creates. For example: C:\codeql-home\databases
    
        ```console
        mkdir C:\codeql-home\databases
        ```
    1.  Use the CodeQL command to create a database using the following parameters:

        - The first parameter is a link to your database directory, for example: C:\codeql-home\databases\MyDriverDatabase. (This command fails if the directory already exists.)
        - `--language` or `-l` is the language or languages your source code is in (the parameters can be a comma separated list, for example [cpp, javascript]).
        - `-- source` or `-s` is the path to your source code.
        - `--command` or `-c` is your build command or the path to your build file.
    
        ```console
        codeql database create <database directory> --language=<language> --source=<path to source code> --command=<build command or path to build file>
        ```

        **Examples**
        
        Single driver example.
        
         ```console
        C:\codeql-home\codeql> codeql database create D:\DriverDatabase --language=cpp --source-root=D:\Drivers\SingleDriver --command="msbuild /t:rebuild D:\Drivers\SingleDriver\SingleDriver.sln"
        ```
        
        Multiple drivers example.
        
         ```console
        C:\codeql-home\codeql> codeql database create D:\SampleDriversDatabase --language=cpp --source-root=D:\AllMyDrivers\SampleDrivers --command=D:\AllMyDrivers\SampleDrivers\BuildAllSampleDrivers.cmd
        ```
        
        For more information or help using the `database create` command, see [Creating CodeQL Databases](https://codeql.github.com/docs/codeql-cli/creating-codeql-databases/) or [Using CodeQL help](#using-codeql-help).
        

6. Analyze your CodeQL database.

   Update this example command to match your environment. Set the parameters, path to new database, format, output sarif file, path to CodeQL query or query suite to use in analysis.

   `codeql database analyze <path to database> --format=sarifv2.1.0 --output=<"path to output file".sarif> <path to query/suite to run>`

    Example:

    `codeql database analyze D:\DriverDatabase --format=sarifv2.1.0 --output=D:\DriverAnalysis1.sarif D:\codeql-home\Windows-driver-developer-supplemental-tools\src\windows-driver-suites\mustfix.qls`

   Be sure to check the path to the suite or query you want to run, not every branch has the same file structure.

---

## View and Interpret Results

This section focuses on generating and interpreting results in SARIF format. Other results formats such as CSV are available, but are not supported by the Static Tools Logo test.

Static Analysis Results Interchange Format (SARIF) is a JSON type format used for sharing static analysis results. Read more about the standard at [OASIS Static Analysis Results Interchange Format (SARIF)](https://github.com/oasis-tcs/sarif-spec), how CodeQL uses [SARIF Output](https://codeql.github.com/docs/codeql-cli/sarif-output/#sarif-output), and [the schema json](https://github.com/oasis-tcs/sarif-spec/blob/main/sarif-2.1/schema/sarif-schema-2.1.0.json).

There are several methods for interpreting the analysis results, including manually sorting through the objects. Here are a few that we use:

- The [Microsoft Sarif Viewer (Web)](https://microsoft.github.io/sarif-web-component/) has functionality that allows you to drag and drop your SARIF file into the viewer, then displays results categorized by rule. This viewer is a quick and easy way to see the count of violations or which queries have violations, but only provides limited information on where in the source code the violation occurred. The page doesn't update if there are no violations.

- The [Microsoft SARIF Viewer for Visual Studio](https://marketplace.visualstudio.com/items?itemName=WDGIS.MicrosoftSarifViewer) is great for displaying the results within Visual Studio for seamless transition from results to source code.

- The [SARIF extension for Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=MS-SarifVSCode.sarif-viewer) opens a preview pane and displays any errors, warnings, or problems reported by CodeQL. To display the Sarif file in a readable format, open the file in Visual Studio Code and select *Shift-Alt-F*. 

The most important section of the SARIF file is the `Results` property within the `Run` object. Each query has a Results property with details about any detected violations and where it occurred. If no violations are found, the property value is empty.

Queries are classified using statuses such as *error*, *warning*, and *problem*. However, this classification is separate from how the Windows Hardware Compatibility Program and the Static Tools Logo Test grade the results. Any driver with defects from any query within the **Must-Fix** suite will **not pass** the Static Tools Logo Test and will **fail to be certified**, regardless of the query classification in the raw query file (for example, *warning*).

## Convert SARIF to Driver Verification Log Format (DVL)

The Static Tools Logo Test parses a [Driver Verification Log (DVL)](../develop/creating-a-driver-verification-log.md), which is the compiled result of the CodeQL static analysis you run on the driver source code. There are three ways to convert your SARIF file to DVL format: Visual Studio, MSBuild, or from the command line using the *dvl.exe* tool. For complete steps, see [Creating a Driver Verification Log](../develop/creating-a-driver-verification-log.md).

Further instructions for the Static Tools Logo Hardware Lab Kit (HLK) Test and guidance on where to place the DVL file can be found in [Running the Static Tools Logo test](/windows-hardware/test/hlk/testref/6ab6df93-423c-4af6-ad48-8ea1049155ae#running-the-test).

## Troubleshooting

If you're certifying with WHCP, first ensure you're using the HLK version associated with the Windows release you're targeting, the associated branch in the Windows Driver Developer Supplemental Tools repository, and the subsequent CodeQL CLI version. For HLK/Windows Release compatibility matrix, see [Windows Hardware Lab Kit](/windows-hardware/test/hlk/) and for Windows Release/Windows Driver Developer Supplemental Tools repo branch/CodeQL CLI version, see the WHCP table in the [Select the CodeQL version](#select-the-appropriate-codeql-version-for-your-driver) section.

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

The database upgrade command updates a database. This upgrade is one way and isn't reversible. For more information, see [database upgrade](https://codeql.github.com/docs/codeql-cli/manual/database-upgrade/).

## Optional procedures

Optionally, you can suppress CodeQL results or run the build and analyze procedures as a post build event in Visual Studio. 

### Suppressing CodeQL Results 

CodeQL for drivers supports suppressing results. Suppressions are currently provided as a convenience to help developers triage issues and reduce noise, not as a way to bypass the **Must-Fix**  checks. They have no impact on generating a Driver Verification Log or passing the Static Tools Logo test at this time. To use suppressions, you must run the DriverAlertSuppression.ql query at the same time as the other queries or suites you wish to run.

For checks ported from Code Analysis, existing Code Analysis suppressions are honored. For more information, see [C++ warning pragma](/cpp/preprocessor/warning).

- `Known limitation:` You can't combine a #pragma(disable) and #pragma(suppress) in the same line at this time.

For checks that are new to CodeQL, suppress them by doing one of two things:  

- Write a `#pragma(suppress:the-rule-id-here)` annotation (without quotes) on the line above the violation, as you do for Code Analysis. Replace "the-rule-id-here" with the `@id` value in the query's metadata, viewable at the top of the file.  

- Write a comment on the line above comprised of the text “lgtm[the-rule-id-here]” (minus quotes). You need to run the standard [C/C++ alert suppression query](https://github.com/github/codeql/blob/main/cpp/ql/src/AlertSuppression.ql) instead of the driver alert suppression query. 

Once a suppression is present and recognized, the resulting SARIF file includes data that a result is suppressed. Most result viewers don't show suppressed results by default.

### Visual Studio Post-Build Event 

If you're building the driver using Visual Studio, you can configure CodeQL queries to run as a post build event.

In this example, a small batch file is created in the target location and called as a post build event. For more information about Visual Studio C++ build events, see [Specifying build events](/cpp/build/specifying-build-events).

1. Create a small batch file that re-creates the CodeQL database then runs the desired queries on it. In this example, the batch file is named `RunCodeQLRebuildQuery.bat`. Modify the paths shown in the example batch file to match your directory locations.

   ```console
   ECHO ">>> Running CodeQL Security Rule V 1.0 <<<"
   ECHO ">>> Removing previously created rules database <<<"
   rmdir /s/q C:\codeql-home\databases\kmdf
   CALL C:\codeql-home\codeql\codeql\codeql.cmd database create -l=cpp -s="C:\codeql-home\drivers\kmdf" -c "msbuild /p:Configuration=Release /p:Platform=x64 C:\codeql-home\drivers\kmdf\kmdfecho.sln /t:rebuild /p:PostBuildEventUseInBuild=false " "C:\codeql-home\databases\kmdf" -j 0
   CALL C:\codeql-home\codeql\codeql\codeql database analyze "C:\codeql-home\databases\kmdf" "<path to query suite .qls file>" --format=sarifv2.1.0 --output=C:\codeql-home\databases\kmdf.sarif -j 0 --rerun
   ECHO ">>> Loading SARIF Results in Visual Studio <<<"
   CALL devenv /Edit C:\codeql-home\databases\kmdf.sarif
   SET ERRORLEVEL = 0
   ```

1. The [devenv.exe / Edit](/visualstudio/ide/reference/edit-devenv-exe) option is used in the batch file to open the SARIF results file in the existing instance of Visual Studio. To view the SARIF results, install the [Microsoft SARIF Viewer for Visual Studio](https://marketplace.visualstudio.com/items?itemName=WDGIS.MicrosoftSarifViewer) and refer to the instructions there for more information.

1. In the driver project, navigate to project properties. In the  **Configuration** pull down, select the build configuration that you wish to check with CodeQL - we recommend **Release**. Creating the CodeQL database and running the queries takes a few minutes, so we don't recommend you run CodeQL on the Debug configuration of your project.

1. Select **Build Events** and **Post-Build Event** in the driver project properties.

1. Provide a path to the batch file and a description of the post build event.

:::image type="content" source="images/codeql-visual-studio-post-build-event.png" alt-text="Visual Studio post build event configuration showing a batch file configured as a command line option.":::

1. The batch file results display at the end of the build output.

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

## Related content

- [CodeQL FAQ](./codeql-faq.md)
- [CodeQL overview](./codeql-overview.md)
- [CodeQL queries and suites](./codeql-queries.md)
