---
title: Cross Architecture Execution
description: Cross Architecture Execution
ms.assetid: 6E7F53A0-7C6A-4063-8300-31E1853EDD04
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Cross Architecture Execution


TAEF supports the ability to run tests from different architectures with the same command-line - provided that the OS running the tests supports them. This means that - for example - x64 *and* x86 tests (on an x64 OS) can be executed with a single 'te.exe' command line.

## <span id="Prerequisites"></span><span id="prerequisites"></span><span id="PREREQUISITES"></span>Prerequisites


In order to run tests for a different architecture than 'te.exe' itself, the TAEF binaries for that architecture need to be available to 'te.exe'. The target architecture can be any of:

-   x86
-   x64
-   ia64

TAEF will look in a folder named for the target architecture relative to the original 'te.exe' for the TAEF binaries for that architecture.

## <span id="Executing_Tests_for_a_Different_Architecture"></span><span id="executing_tests_for_a_different_architecture"></span><span id="EXECUTING_TESTS_FOR_A_DIFFERENT_ARCHITECTURE"></span>Executing Tests for a Different Architecture


Executing tests for a different architecture requires no extra configuration - simply pass the given DLL as a parameter to 'te.exe'. TAEF will inspect the binary to identify it's target architecture, and instantiate the correct host process in order to load and run the tests. For example, an x86 'te.exe' can inspect an x64 test DLL, and will launch an x64 process to run the tests:

**c:\\taef\\x86&gt;te x64\\Scenario.Tests.dll**

Since the 'te.exe' command line can take multiple Test DLL's, you can mix architectures and TAEF will choose the correct host processes for the given Test DLL:

**c:\\taef\\x86&gt;te x64\\Scenario.Tests.dll x86\\Scenario.Tests.dll x64\\UI.Tests.dll**

This allows TAEF users to get more test coverage from a single command line, with all results rolled up into a single log. Without this functionality, the tests for each architecture would have to be pulled together into their own command line, executed individually and the results from each run combined.

If a given Test File is *not* architecture specific (for example, a C# binary that compiles to pure IL), then it will be run using the same architecture as the 'te.exe' it was passed to.

## <span id="Selecting_Tests_by_Architecture"></span><span id="selecting_tests_by_architecture"></span><span id="SELECTING_TESTS_BY_ARCHITECTURE"></span>Selecting Tests by Architecture


TAEF automatically applies the 'Architecture' metadata to Test Files that require a specific architecture. The value of the 'Architecture' metadata is the architecture that is required to run the tests, and will be one of:

-   x86
-   x64
-   ia64

In order to select tests for a specific architecture, you can use the selection language to match the 'Architecture' metadata. For example, if the 'Tests' folder contains a mix of x86 and x64 Test Files, then the following command line will run only the x64 tests:

**c:\\taef\\x86&gt;te Tests\\\*.Tests.dll /select:@Architecture='x64'**

## <span id="Errors"></span><span id="errors"></span><span id="ERRORS"></span>Errors


Passing a Test File that is compiled for a different architecture to TAEF without the required target architecture binaries present will result in an error message. The following example shows an x86 'te.exe' attempting to run x64 tests, without the 'x64' subfolder being populated with the required binaries:

``` syntax
c:\>te x64\Scenario.Tests.dll
Test Authoring and Execution Framework v2.2 Build 6.1.7689.0 (release.091218-1251) for x86
Error: Please copy all x64 TAEF binaries to the 'c:\taef\x86\x64' directory in order to run x64 tests from this process. 
Error: Failed to create the ProcessHostController. TE.ProcessHost.exe may be unavailable. Terminating execution...
Error: No test cases were executed.
```

 

 





