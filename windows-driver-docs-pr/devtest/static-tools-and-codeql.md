---
title: Static Tools and CodeQL
description: Using Static tools and CodeQL on Windows driver source code to discover and repair any issues that are deemed Must-Fix
keywords:
- dynamic verification tools WDK
- static verification tools WDK
ms.date: 12/10/2020
ms.localizationpriority: medium
---

# CodeQL and the Static Tools Logo Test

Microsoft is committed to mitigating the attack surface for the Windows operating system, and ensuring that third party drivers meet a strong security bar is critical to accomplishing that goal.  Microsoft will set this security bar by adding a new requirement to the [Windows Hardware Compatibility Program](/windows-hardware/design/compatibility).  This requirement states that all driver submissions must use the [CodeQL](https://securitylab.github.com/tools/codeql) engine on driver source code and fix any violations that are deemed **“Must-Fix”**.

[CodeQL](https://semmle.com/codeql) from Semmle, is a powerful static analysis technology for securing software. The combination of an extensive suite of high-value security queries and a robust platform make it an invaluable tool for securing third party driver code.

The requirement to analyze the driver source code and fix any **“Must-Fix”** violations will be enforced by the [Static Tools Logo Test](https://docs.microsoft.com/windows-hardware/test/hlk/testref/6ab6df93-423c-4af6-ad48-8ea1049155ae).

This topic describes how to:

- Use CodeQL to analyze your driver source code for known high impact security issues.
- Ensure the Static Tools Logo Test can consume the results of running CodeQL.
- Determine which **“Must-Fix”** [queries](#must-fix-queries) must be run without error for certification, as part of the Windows Hardware Compatibility Program.

> [!IMPORTANT]
> This information is preliminary and will be updated as the query rule set distribution is finalized.
>

## Concepts for CodeQL

**CodeQL** is the analysis engine used by developers to perform security analysis.  A **CodeQL database** is a directory containing:

- Queryable data, extracted from driver source code.
- A source reference, for displaying query results directly in source code.  A **query** can be thought of as a “check” or “rule”.  Each query represents a distinct security vulnerability that is being searched for. For more information, see [Writing queries](https://help.semmle.com/QL/learn-ql/writing-queries/writing-queries.html) in the CodeQL docs.
- Query results.
- Log files generated during database creation, query execution, and other operations.

This topic details how to perform analysis using CodeQL CLI with a focus on driver developers for Windows.  Supplementary documentation can be found at [CodeQL Getting Started](https://help.semmle.com/codeql/codeql-cli/procedures/get-started.html).

We will use the [CodeQL command line tools (CLI)](https://help.semmle.com/codeql/codeql-cli.html) to create a CodeQL database from a variety of compiled and interpreted languages, and then analyze that database with using individual queries and a driver specific query suite.

## CodeQL Windows Setup

### Download, install and test CodeQL

1. The first task will be to create a directory to contain CodeQL.  This example will use `C:\codeql-home\`

```command
C:\> mkdir C:\codeql-home
```

2. Navigate to the Github [CodeQL Download Page](https://github.com/github/codeql-cli-binaries/releases/)
3. Download the latest version of the zip file. For example for 64 bit Windows "codeql-win64.zip".
4. Unzip the downloaded zip file to a directory, for example,  `C:\codeql-home\codeql-win64`.
5. Confirm that the CodeCL command works by displaying the help.

```command
C:\codeql-home\codeql-win64\codeql>codeql --help
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

### Clone the repository to access the query rules

1. Navigate to the [CodeQL Github repository](https://github.com/github/codeql).

2. [Clone](https://github.com/git-guides/git-clone) the repository to download the necessary CodeQL queries.

```command
C:\codeql-home\>git clone https://github.com/github/codeql.git
```

> [!NOTE]
> Usage of CodeQL for the purpose of WHCP testing is acceptable under the **[Hardware Lab Kit (HLK)](/windows-hardware/test/hlk/) End User License Agreement**.
> Step 2 from the instructions above will be updated in the near future to specify a repository that contains a query suite with only driver-relevant queries.

This page assumes a Windows development environment and that the repository will be installed under *C:\codeql-home*.

## Building your CodeQL Database

The next steps create a CodeQL database that you can use for analysis.

Create a directory to keep CodeQL databases (the databases folder).  This example will use *C:\codeql-home\databases*

```command
mkdir C:\codeql-home\databases
```

In general, the command used to create a CodeQL database will look like the following:

```command
codeql database create -l=[cpp/csharp/python/java/javascript/go/xml] -s=<path to source code> -c=<command to build> <database folder>\<project name> -j 0
```

For help using the database create command, type:

```command
codeql database create --help
```

CodeQl uses the MSBuild compiler to process the C++ code to prepare it to be analyzed.

### Example

Using a command line environment that is used for building driver source code, such as the [Enterprise Windows Driver Kit (EWDK)](../develop/using-the-enterprise-wdk.md), navigate to the CodeQL tools folder where the repository was cloned.

This example will process the evaluate the kmdfecho.sln driver sample, which is available on github.

https://github.com/Microsoft/Windows-driver-samples/tree/master/general/echo/kmdf

The kmdf sample will be located in `C:\codeql-home\drivers\kmdf`.

Run the following commands to create a new CodeQL database under *C:\codeql-home\databases\kmdf*.

```command
C:\codeql-home>C:\codeql-home\codeql-win64\codeql\codeql database create -l=cpp -s=C:\codeql-home\drivers\kmdf -c "msbuild /t:rebuild "C:\codeql-home\drivers\kmdf\kmdfecho.sln" /p:UseSharedCompilation=false" "C:\codeql-home\databases\kmdf" -j 0
```

The *“-j 0”* flag indicates to use as many threads as there are CPU’s in the import step of creating the database.

This example uses this argument to find and build the driver project. The msbuild command must be available in the path.

```command
msbuild /t:rebuild "C:\codeql-home\drivers\kmdf\kmdfecho.sln"
```

## Summary of directory locations

At this point in our example setup, the following directories will be present.

| Description            | Location                           |
|------------------------|------------------------------------|
| Codeql.exe             | C:\codeql-home\codeql-win64\codeql |
| C++ Rules              | C:\codeql-home\codeql\cpp          |
| Databases              | C:\codeql-home\databases           |
| Driver code under test | C:\codeql-home\drivers\kmdf        |

## Perform Analysis

At this point, the set-up is complete and the next step is to perform the actual analysis on the driver source code.

CodeQL CLI tools can perform analysis of the database that has been created in the previous step and can run queries or suites of queries.  The findings are reported as output in *CSV* or *SARIF* format.

For the purposes of this example, it is assumed that the suite of queries to be run on driver source code is the suite that is included when the CodeQL Microsoft repository is cloned.

The database analyze command to execute analysis uses the following syntax.

```command
codeql database analyze <database> <path to query, suite or directory> 
--search-path=<path to search for packages> 
--format=[csv/sarif-latest/sarifv1/sarifv2/sarifv2.1.0/graphtext/dgml] 
--output=<output file directory>\output file name> 
-j 0
```
The *“-j 0”* flag indicates to use as many threads as there are CPU’s in the analysis portion.

Display help on the codeql database analyze command using the `--help` parameter.

```command
C:\codeql-home\codeql-win64\codeql>codeql database analyze --help
Usage: codeql database analyze [OPTIONS] <database> [<query|dir|suite>...]
Analyze a database, producing meaningful results in the context of the source code.

Run a query suite (or some individual queries) against a CodeQL database, producing results, styled as alerts or paths,
in SARIF or another interpreted format.

...

```

For example to evaluate the TooFewArguments query against the kmdf echo driver with the results returned in SARIF format use this command.

```command
C:\codeql-home>C:\codeql-home\codeql-win64\codeql\codeql database analyze "C:\codeql-home\databases\kmdf" "C:\codeql-home\codeql\cpp\ql\src\Likely Bugs\Underspecified Functions\TooFewArguments.ql" --format=sarifv2.1.0 --output=C:\codeql-home\databases\kmdfecho1.sarif -j 0
```

Output similar to the following should be displayed.

```command
Running queries.
Compiling query plan for C:\codeql-home\codeql\cpp\ql\src\Likely Bugs\Underspecified Functions\TooFewArguments.ql.
[1/1 comp 21.5s] Compiled C:\codeql-home\codeql\cpp\ql\src\Likely Bugs\Underspecified Functions\TooFewArguments.ql.
Starting evaluation of codeql-cpp\Likely Bugs\Underspecified Functions\TooFewArguments.ql.
[1/1 eval 4.6s] Evaluation done; writing results to codeql-cpp\Likely Bugs\Underspecified Functions\TooFewArguments.bqrs.
Shutting down query evaluator.
Interpreting results.
```

You can specify a timeout for the entire operation with the *"–timeout=[seconds]"* flag.  This can be useful for analysis on queries without being limited by a single, long-running query.  More options to tweak analysis optimizations are described in [database analyze](https://help.semmle.com/codeql/codeql-cli/commands/database-analyze.html).

Currently, the command above demonstrates how to run only one query, *"TooFewArguments.ql"*.  It is possible to run multiple queries at once by listing all queries sequentially in one command.  

In the near future, a driver specific *query suite* which contains all relevant driver queries will be provided. For more information, see [query suites](https://help.semmle.com/codeql/codeql-cli/procedures/query-suites.html).

## Troubleshooting

For database version mismatches issues, the following tools may be helpful.

Use the codeql version command to display the version of the codeql exe.

```command
C:\codeql-home\codeql-win64\codeql>codeql version
CodeQL command-line toolchain release 2.4.0.
Copyright (C) 2019-2020 GitHub, Inc.
Unpacked in: C:\codeql-home\codeql-win64\codeql
   Analysis results depend critically on separately distributed query and
   extractor modules. To list modules that are visible to the toolchain,
   use 'codeql resolve qlpacks' and 'codeql resolve languages'.
```

The database upgrade command will update a database. Be aware that this is a one way upgrade and is not reversible. For more information, see [database upgrade](https://help.semmle.com/codeql/codeql-cli/commands/database-upgrade.html).

## Queries

This page will be updated to indicate which queries are officially deemed **"Must-Fix"** for WHCP certification.

The queries that Microsoft recommends running on *all* driver source code are:

| ID                       | Location   |
| ------------------------ | ---------- |
| [cpp/too-few-arguments](https://help.semmle.com/wiki/display/CCPPOBJ/Call+to+function+with+fewer+arguments+than+declared+parameters)   | *cpp/ql/src/Likely Bugs/Underspecified Functions/TooFewArguments.ql* |
| [cpp/bad-additionoverflow-check](https://help.semmle.com/wiki/display/CCPPOBJ/Bad+check+for+overflow+of+integer+addition)   | *cpp/ql/src/Likely Bugs/Arithmetic/BadAdditionOverflowCheck.ql* |
| [cpp/pointer-overflowcheck](https://help.semmle.com/wiki/display/CCPPOBJ/Pointer+overflow+check)   | *cpp/ql/src/Likely Bugs/Memory Management/PointerOverflow.ql* | 
| [cpp/hresult-booleanconversion](https://help.semmle.com/wiki/display/CCPPOBJ/Cast+between+HRESULT+and+a+Boolean+type)   | *cpp/ql/src/Security/CWE/CWE-253/HResultBooleanConversion.ql* | 
| [cpp/incorrect-string-typeconversion](https://help.semmle.com/wiki/pages/viewpage.action?pageId=29392920)   | *cpp/ql/src/Security/CWE/CWE-704/WcharCharConversion.ql* |
| [cpp/integermultiplication-cast-to-long](https://help.semmle.com/wiki/display/CCPPOBJ/Multiplication+result+converted+to+larger+type)   | *cpp/ql/src/Likely Bugs/Arithmetic/IntMultToLong.ql* |
| [cpp/signed-overflowcheck](https://help.semmle.com/wiki/display/CCPPOBJ/Signed+overflow+check)   | *cpp/ql/src/Likely Bugs/Arithmetic/SignedOverflowCheck.ql* |
| [cpp/upcast-array-pointerarithmetic](https://help.semmle.com/wiki/display/CCPPOBJ/Upcast+array+used+in+pointer+arithmetic)   | *cpp/ql/src/Likely Bugs/Conversion/CastArrayPointerArithmetic.ql* |
| [cpp/comparison-withwider-type](https://help.semmle.com/wiki/display/CCPPOBJ/Comparison+of+narrow+type+with+wide+type+in+loop+condition)   | *cpp/ql/src/Security/CWE/CWE-190/ComparisonWithWiderType.ql* |
| [cpp/suspicious-add-sizeof](https://help.semmle.com/wiki/display/CCPPOBJ/Suspicious+add+with+sizeof)   | *cpp/ql/src/Security/CWE/CWE-468/SuspiciousAddWithSizeof.ql* |
| [cpp/potentiallydangerous-function](https://help.semmle.com/wiki/display/CCPPOBJ/Use+of+potentially+dangerous+function)   | *cpp/ql/src/Security/CWE/CWE-676/PotentiallyDangerousFunction.ql* |
| [cpp/incorrect-notoperator-usage](https://help.semmle.com/wiki/display/CCPPOBJ/Incorrect+%27not%27+operator+usage)   | *cpp/ql/src/Likely Bugs/Likely Typos/IncorrectNotOperatorUsage.ql* | 
| [cpp/offset-use-beforerange-check](https://help.semmle.com/wiki/display/CCPPOBJ/Array+offset+used+before+range+check)  | *cpp/ql/src/Best Practices/Likely Errors/OffsetUseBeforeRangeCheck.ql*   |
| [cpp/suspicious-sizeof](https://help.semmle.com/wiki/display/CCPPOBJ/Suspicious+add+with+sizeof)   | *cpp/ql/src/Likely Bugs/Memory Management/SuspiciousSizeof.ql* |
| [cpp/uninitialized-local](https://help.semmle.com/wiki/display/CCPPOBJ/Potentially+uninitialized+local+variable)   | *cpp/ql/src/Likely Bugs/Memory Management/UninitializedLocal.ql* |
| [cpp/unterminatedvariadic-call](https://help.semmle.com/wiki/display/CCPPOBJ/Call+to+function+with+fewer+arguments+than+declared+parameters)   | *cpp/ql/src/Security/CWE/CWE-121/UnterminatedVarargsCall.ql* |
| [cpp/suspicious-pointerscaling](https://help.semmle.com/wiki/display/CCPPOBJ/Suspicious+pointer+scaling)   | *cpp/ql/src/Security/CWE/CWE-468/IncorrectPointerScaling.ql* |
| [cpp/suspicious-pointerscaling-void](https://help.semmle.com/wiki/display/CCPPOBJ/Suspicious+pointer+scaling+to+void)   | *cpp/ql/src/Security/CWE/CWE-468/IncorrectPointerScalingVoid.ql* |
| [cpp/conditionally-uninitialized-variable](https://help.semmle.com/wiki/display/CCPPOBJ/Conditionally+uninitialized+variable)   | */cpp/ql/src/Security/CWE/CWE-457/ConditionallyUninitializedVariable.ql.* | 

### Must-Fix Queries

The subset of queries below are currently deemed as **"Must-Fix"** for WHCP certification.  **This list is subject to change**.  A final list will be posted to this page by April 1, 2021.  

| ID            | Location   |
| ------------- | ---------- |
| [cpp/too-few-arguments](https://help.semmle.com/wiki/display/CCPPOBJ/Call+to+function+with+fewer+arguments+than+declared+parameters)   | *cpp/ql/src/Likely Bugs/Underspecified Functions/TooFewArguments.ql* |
| [cpp/bad-additionoverflow-check](https://help.semmle.com/wiki/display/CCPPOBJ/Bad+check+for+overflow+of+integer+addition)   | *cpp/ql/src/Likely Bugs/Arithmetic/BadAdditionOverflowCheck.ql* |
| [cpp/pointer-overflowcheck](https://help.semmle.com/wiki/display/CCPPOBJ/Pointer+overflow+check)   | *cpp/ql/src/Likely Bugs/Memory Management/PointerOverflow.ql* |
| [cpp/hresult-booleanconversion](https://help.semmle.com/wiki/display/CCPPOBJ/Cast+between+HRESULT+and+a+Boolean+type)   | *cpp/ql/src/Security/CWE/CWE-253/HResultBooleanConversion.ql* | 
| [cpp/incorrect-string-typeconversion](https://help.semmle.com/wiki/pages/viewpage.action?pageId=29392920)   | *cpp/ql/src/Security/CWE/CWE-704/WcharCharConversion.ql* | 
| [cpp/conditionally-uninitialized-variable](https://help.semmle.com/wiki/display/CCPPOBJ/Conditionally+uninitialized+variable)   | */cpp/ql/src/Security/CWE/CWE-457/ConditionallyUninitializedVariable.ql.* | 
| [cpp/comparison-withwider-type](https://help.semmle.com/wiki/display/CCPPOBJ/Comparison+of+narrow+type+with+wide+type+in+loop+condition)   | *cpp/ql/src/Security/CWE/CWE-190/ComparisonWithWiderType.ql* |
| [cpp/uninitialized-local](https://help.semmle.com/wiki/display/CCPPOBJ/Potentially+uninitialized+local+variable)   | *cpp/ql/src/Likely Bugs/Memory Management/UninitializedLocal.ql* |

## View Analysis

The results of running the analysis command in the previous section can be viewed in a [SARIF](https://help.semmle.com/codeql/glossary.html#sarif-results-file) file format.  Details regarding SARIF output can be found at [SARIF Overview](https://help.semmle.com/codeql/codeql-cli/reference/sarif-overview.html).

The SARIF file contains a **result** section for each query that was run and includes details regarding the completed analysis.  For example, if the query found a vulnerability, the SARIF file will include details as to what the vulnerability is and where it found the defect. If no vulnerabilities are found, the results section will be blank.

```xml
    "results" : [ ],
```

In order to review the results, install the [Microsoft SARIF Viewer for Visual Studio](https://marketplace.visualstudio.com/items?itemName=WDGIS.MicrosoftSarifViewer) and follow the instructions on that page.  Alternatively, you can install the [SARIF extension for Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=MS-SarifVSCode.sarif-viewer).

## Driver Verification Log (DVL) Consumption of SARIF Output

Microsoft will enforce the requirement of running CodeQL queries with the Static Tools Logo Test.  The Static Tools Logo Test uses a [Driver Verification Log (DVL)](../develop/creating-a-driver-verification-log.md) to gather results from different static analyses run on driver source code.  This DVL is then parsed as part of the Static Tools Logo Test used in an HLK test.

CodeQL results follow the same model of using a DVL to show that the driver being certified ran the appropriate CodeQL queries in order to pass the HLK test for certification.

Place the .sarif file in the same directory as the .vcxproj file for which a DVL is being generated.  The exact name of the results file does not matter, as long as the file ends with *".sarif"*. The ability to submit a SARIF results file is available in the WDK, preview build 20190 and later.

Instructions for how to generate a DVL can be found on [Creating a Driver Verification Log](../develop/creating-a-driver-verification-log.md). Guidance for where to place the DVL for consumption by the Static Tools Logo HLK Test can be found in [Running the test](https://docs.microsoft.com/windows-hardware/test/hlk/testref/6ab6df93-423c-4af6-ad48-8ea1049155ae#running-the-test).
