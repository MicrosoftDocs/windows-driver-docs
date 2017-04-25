---
title: Overview of Executing Tests
description: Overview of Executing Tests
ms.assetid: 3D58D074-DC06-4b01-9EB5-7A17E69D6935
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Overview of Executing Tests


Executing tests using TAEF is straight-forward; you simply specify the Test Files with the command "TE.EXE". For example, in order to run all tests within the "CPP.Basic.Examples.dll" Test File, you can run;

``` syntax
TE.exe CPP.Basic.Examples.dll
```

You can specify multiple test files, even if they contain tests marked up in a different manner. For example, the following command will run all tests in the "CPP.Basic.Examples.dll" and "CSharp.Basic.Examples.dll" files, even though they are written in different languages;

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

If a file is specified at the command prompt that doesn't contain any tests, then TE will report an error message.

## <span id="Order_of_Execution"></span><span id="order_of_execution"></span><span id="ORDER_OF_EXECUTION"></span>Order of Execution


The Test Files specified at the command prompt will be processed in the order that they are specified.

## <span id="OutOfProcessExecution"></span><span id="outofprocessexecution"></span><span id="OUTOFPROCESSEXECUTION"></span>Out of Process Execution


By default TAEF executes tests out-of-process - it uses the "TE.ProcessHost.exe" process to run tests. This allows tests to be isolated from one another - preventing tests from being affected by prior tests. If you want to execute tests in the "TE.exe" process then you can specify the **"/inproc"** option for TE.exe.

## <span id="Selecting_Tests"></span><span id="selecting_tests"></span><span id="SELECTING_TESTS"></span>Selecting Tests


Specific tests can be selected using the **"/select"** option, and specifying a 'selection query'. The [Selection](selection.md) page explains how to use the selection query to select specific tests to execute. If you want to select based on only the test's name, you could use **"/name"** option instead. See the Selection page for details.

## <span id="Specifying_part_of_command_as_environment_variable__te_cmd"></span><span id="specifying_part_of_command_as_environment_variable__te_cmd"></span><span id="SPECIFYING_PART_OF_COMMAND_AS_ENVIRONMENT_VARIABLE__TE_CMD"></span>Specifying part of command as environment variable: **te\_cmd**


If some of your command options for te.exe will always be the same, you can leverage the environment variable **te\_cmd**. Whatever te\_cmd is set to will get appended to the command for te.exe execution. With "*set te\_cmd=/list*", you will always see listing of tests as against execution for the binaries specified at the command prompt.

## <span id="Listing_Tests"></span><span id="listing_tests"></span><span id="LISTING_TESTS"></span>Listing Tests


Specifying the **"/list"** command option along with the test files will list the names of the classes and test methods in the test files on the console. Note that this will only list the binary, class and test methods names for each binary specified and not execute them. If you want to list more details, like the setup and cleanup methods, the metadata or properties specified at each level, and in case of data driven tests, the data provided, use the **"/listproperties"** command option instead.

## <span id="Test_Results"></span><span id="test_results"></span><span id="TEST_RESULTS"></span>Test Results


For any generic test case, the test result depends on whether the Verify calls made succeeded or failed. You can find the APIs available and other details on ['Verify'](verify.md). If no Verify call is made during the test, the test result will default to "Passed" for the log subscribers provided with TAEF. You could choose to specify a **"DefaultTestResult"** explictly while authoring the test. See [Authoring Tests](authoring-tests.md) for more details.

## <span id="Help_-_Command_Options"></span><span id="help_-_command_options"></span><span id="HELP_-_COMMAND_OPTIONS"></span>Help - Command Options


You can find explantions for all command options available by specifying the **"/?"** option for TE.exe. For extended explanations, see [Te.exe Command Options](te-exe-command-line-parameters.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[taef\taef]:%20Overview%20of%20Executing%20Tests%20%20RELEASE:%20%289/12/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




