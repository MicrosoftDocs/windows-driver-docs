---
title: Overview of Executing Tests
description: Overview of Executing Tests
ms.date: 04/20/2017
---

# Overview of Executing Tests

To execute tests using TAEF, you specify the Test Files with the command **TE.EXE**, found in %:\Program Files (x86)\Windows Kits\10\Testing\Runtimes\TAEF. For example, in order to run all tests within the **CPP.Basic.Examples.dll** Test File, run:

``` syntax
TE.exe CPP.Basic.Examples.dll
```

You can specify multiple test files, even if they contain tests marked up in a different manner. For example, the following command runs all tests in the **CPP.Basic.Examples.dll** and **CSharp.Basic.Examples.dll** files, even though they are written in different languages:

``` syntax
TE.exe CPP.Basic.Examples.dll CSharp.Basic.Examples.dll
```

You can also use wildcards for selecting files to execute:

``` syntax
TE.exe *.Examples.dll
```

And you can also specify relative paths:

``` syntax
TE.exe Examples\*
```

If a file is specified at the command prompt that doesn't contain any tests, then TE.exe reports an error message.

## Order of Execution

The Test Files specified at the command prompt will be processed in the order that they are specified.

## Out of Process Execution

By default TAEF executes tests out-of-process. TAEF uses the **TE.ProcessHost.exe** process to run tests. This allows tests to be isolated from one another, preventing tests from being affected by prior tests. To execute tests in the **TE.exe** process, specify the **"/inproc"** option for **TE.exe**.

## Selecting Tests

You can select specific tests by using the **"/select"** option and specifying a 'selection query'. If you want to select based on only the test's name, use the **"/name"** option instead. For more info about how to use the selection query to select specific tests to execute, see [Selection](selection.md).

## Specifying part of command as environment variable: **te\_cmd**

If some of your command options for te.exe will always be the same, you can leverage the environment variable **te\_cmd**. Whatever te\_cmd is set to will get appended to the command for te.exe execution. With "*set te\_cmd=/list*", you will always see listing of tests as against execution for the binaries specified at the command prompt.

## Listing Tests

Specifying the **"/list"** command option along with the test files will list the names of the classes and test methods in the test files on the console. Note that this will only list the binary, class, and test methods names for each binary specified and not execute them. If you want to list more details, like the setup and cleanup methods, the metadata or properties specified at each level, and in case of data driven tests, the data provided, use the **"/listproperties"** command option instead.

## Test Results

For any generic test case, the test result depends on whether the Verify calls made succeeded or failed. You can find the APIs available and other details on ['Verify'](verify.md). If no Verify call is made during the test, the test result will default to "Passed" for the log subscribers provided with TAEF. You could choose to specify a **"DefaultTestResult"** explictly while authoring the test. See [Authoring Tests](authoring-tests.md) for more details.

## Help - Command Options

Find explantions for all command options available by specifying the **"/?"** option for TE.exe. For extended explanations, see [Te.exe Command Options](te-exe-command-line-parameters.md).
