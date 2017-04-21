---
title: Cross Architecture Execution
description: Cross Architecture Execution
ms.assetid: 6E7F53A0-7C6A-4063-8300-31E1853EDD04
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[taef\taef]:%20Cross%20Architecture%20Execution%20%20RELEASE:%20%289/12/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




