---
title: Te.exe Command Options
description: Te.exe Command Options
ms.assetid: E9A9292D-FA30-410d-9322-BD0F321314F9
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Te.exe Command Options


-   [Usage](#usage)
-   [Selection/Execution Commands](#selectionexecutioncommands)
-   [Logger Settings](#loggersettings)
-   [Debug Settings](#debugsettings)
-   [Test Modes](#testmodes)

## <span id="Usage"></span><span id="usage"></span><span id="USAGE"></span>Usage


**te.exe** &lt;[test\_binaries](#testbinaries)&gt; \[[/appendWttLogging](#appendwttlogging)\] \[[/breakOnCreate](#breakoncreate)\] \[[/breakOnError](#breakonerror)\] \[[/breakOnInvoke](#breakoninvoke)\] \[[/coloredConsoleOutput](#coloredconsoleoutput)\] \[ [/console:flushWrites](#console-option) \] \[ /console:position=&lt;x,y&gt; \] \[ /console:size=&lt;x,y&gt; \] \[ /console:topmost \][\[/defaultAppDomain\]](#defaultappdomain) \[[/disableConsoleLogging](#disableconsolelogging)\] \[[/disableTimeouts](#disabletimeouts)\] \[[/dpiaware](#dpiaware) \] \[[/enableWttLogging](#enablewttlogging)\] \[[/inproc](#inproc)\] \[[/isolationLevel](#isolationlevel)\] \[[/labMode](#labmode)\] \[[/list](#list)\] \[[/listProperties](#listproperties)\] \[[/logFile:&lt;name&gt;](#logfile)\] \[[/logOutput:&lt;mode&gt;](#logoutput)\] \[[/miniDumpOnCrash](#minidumponcrash)\] \[[/miniDumpOnError](#minidumponerror)\] \[[/name:&lt;testname&gt;](#name)\] \[[/outputFolder:&lt;folderName&gt;](#outputfolder)\] \[[/p:&lt;ParamName&gt;=&lt;ParamValue&gt;](#p)\] \[[/parallel](#parallel)\] \[[/persistPictResults](#persistpictresults)\] \[[/pict:&lt;OptionName&gt;=&lt;OptionValue&gt;](#pict)\] [\[/rebootStateFile\]](#rebootstatefile) \[[/reportLoadingIssue](#reportloadingissue)\] \[[/runas:&lt;RunAsType&gt;](#runas)\] \[[/runIgnoredTests](#runignoredtests)\] \[[/runon:&lt;MachineName&gt;](#runon)\] \[[/screenCaptureOnError](#screencaptureonerror)\] \[[/select:&lt;query&gt;](#select)\] \[[/sessionTimeout:&lt;value&gt;](#sessiontimeout)\] \[[/stackFrameCount:&lt;value&gt;](#stackframecount)\] \[[/stackTraceOnError](#stacktraceonerror)\] \[[/terminateOnFirstFailure](#terminateonfirstfailure)\] \[[/testDependencies:&lt;files&gt;](#testdependencies)\] \[[/testmode:Loop](#looptestmode)\] \[[/testmode:Stress](#stress)\] \[[/testTimeout:&lt;value&gt;](#testtimeout)\] \[[/unicodeOutput:&lt;true/false&gt;](#unicodeoutput)\] [\[/version\]](#version) \[[/wttDeviceString:&lt;value&gt;](#wttdevicestring)\] \[[/wttDeviceStringSuffix:&lt;value&gt;](#wttdevicestringsuffix)\]

## <span id="SelectionExecutionCommands"></span><span id="selectionexecutioncommands"></span><span id="SELECTIONEXECUTIONCOMMANDS"></span>Selection/Execution Commands


### test\_binaries

Specify one or more test files to execute (separated by spaces). Wildcard characters are supported.

<span id="te.exe_test1.dll"></span><span id="TE.EXE_TEST1.DLL"></span>te.exe test1.dll  
**Interpretation:** Run all tests in test1.dll.

<span id="te.exe_test1.dll_test2.dll_test3.dll"></span><span id="TE.EXE_TEST1.DLL_TEST2.DLL_TEST3.DLL"></span>te.exe test1.dll test2.dll test3.dll  
**Interpretation:** Run all tests in test1.dll, test2.dll and test3.dll.

<span id="te.exe__.dll"></span><span id="TE.EXE__.DLL"></span>te.exe \*.dll  
**Interpretation:** Run all tests in all dlls in the current directory.

### <span id="coloredConsoleOutput"></span><span id="coloredconsoleoutput"></span><span id="COLOREDCONSOLEOUTPUT"></span>/coloredConsoleOutput:&lt;true/false&gt;

Specifies whether or not TAEF should output colored console text. The default is true. If set to false, TAEF will output all text with the default console color.

**te.exe test1.dll /coloredConsoleOutput:false**

### <span id="console_option"></span><span id="CONSOLE_OPTION"></span>/console:&lt;optionName&gt;=&lt;value&gt;

Provides options for configuring TE's use of the console. The following options are available:

<span id="console-option"></span>**/console:flushWrites**  
Causes console output to be flushed after every line is written - useful when TE.exe's output has been redirected.

<span id="_console_position__x_y___current__"></span><span id="_CONSOLE_POSITION__X_Y___CURRENT__"></span>**/console:position=\[x,y | current \]**  
Sets the position (in pixels) of the console window relative to the corner of the primary monitor. Use a value of **current** to specify that the current console position should be stored and used when resuming from reboot.

<span id="_console_size____x_y____current__"></span><span id="_CONSOLE_SIZE____X_Y____CURRENT__"></span>**/console:size=\[ &lt;x,y&gt; | current \]**  
Sets the size of the console window (in character dimensions). The screen buffer size will be increased to match the size of the window if necessary. Use a value of **current** to specify that the current console size should be stored and used when resuming from reboot.

<span id="_console_topmost"></span><span id="_CONSOLE_TOPMOST"></span>**/console:topmost**  
Keeps the console running te.exe 'topmost' in the desktop z-order for the duration of execution.

### <span id="dpiaware"></span><span id="DPIAWARE"></span>/dpiaware

Executes tests in a process marked as DPI-aware, see [High DPI](https://msdn.microsoft.com/library/windows/desktop/dd464646). This can also be set via metadata ("DpiAware").

### <span id="inproc"></span><span id="INPROC"></span>/inproc

Execute all tests within the TE.exe process itself rather than within TE.ProcessHost.exe.

<span id="te.exe_test1.dll__inproc"></span><span id="TE.EXE_TEST1.DLL__INPROC"></span>te.exe test1.dll /inproc  
**Note:** TE only supports executing one test dll at a time when using the */inproc* setting.

### <span id="isolationLevel"></span><span id="isolationlevel"></span><span id="ISOLATIONLEVEL"></span>/isolationLevel:&lt;Level&gt;

Specifies the minimum level of isolation to be used when executing TAEF tests. If this value conflicts with the IsolationLevel specified as metadata, the value becomes the isolation level with the tightest scope. See [Test Isolation](test-isolation.md) for more details.

**te.exe test1.dll /isolationLevel:Class**

### <span id="labMode"></span><span id="labmode"></span><span id="LABMODE"></span>/labMode

Executes tests and removes potential blocking UI (for example, Windows Error Reporting dialogs on crashing tests).

### <span id="list"></span><span id="LIST"></span>/list

Lists the names of all the [test\_binaries](#testbinaries) and the classes and methods within them. If selection criteria is specified, lists only the names of those which meet the criteria.

```cpp
 te.exe test1.dll test2.dll /list

 WEX::UnitTests::Test1
  WEX::UnitTests::Test1::Example1
  WEX::UnitTests::Test1::Example2
  WEX::UnitTests::Test1::Example3

 WEX::UnitTests::Test2
  WEX::UnitTests::Test2::Example1
  WEX::UnitTests::Test2::Example2
  WEX::UnitTests::Test2::Example3
```

```cpp
 te.exe test1.dll test2.dll /select:@name=&#39;*Example2*&#39; /list

 WEX::UnitTests::Test1
  WEX::UnitTests::Test1::Example2

 WEX: :UnitTests::Test2
  WEX::UnitTests::Test2::Example2
```

### <span id="listProperties"></span><span id="listproperties"></span><span id="LISTPROPERTIES"></span>/listProperties

Lists the names and properties of all the test\_binaries and the classes and methods in them along with Setup and Teardown function names, if available. If selection criteria is specified, lists only the names of those which meet the criteria.

```cpp
 te.exe test1.dll test2.dll /listProperties

 WEX::UnitTests::Test1
  WEX::UnitTests::Test1::Example1
   Setup: Test1Setup
   Teardown: Test1Teardown
   Property[ThreadingModel] = MTA
  WEX::UnitTests::Test1::Example2
   Setup: Test1Setup
   Teardown: Test1Teardown
   Property[ThreadingModel] = STA
  WEX::UnitTests::Test1::Example3
   Setup: Test1Setup
   Teardown: Test1Teardown
   Property[ThreadingModel] = STA

 WEX::UnitTests::Test2
  WEX::UnitTests::Test2::Example1
   Property[ThreadingModel] = MTA
  WEX::UnitTests::Test2::Example2
   Property[ThreadingModel] = STA
  WEX::UnitTests::Test2::Example3
   Property[ThreadingModel] = MTA
```

```cpp
 te.exe test1.dll test2.dll /select:@name=&#39;*Example2*&#39; /listProperties

 WEX::UnitTests::Test1
  WEX::UnitTests::Test1::Example2
   Setup: Test1Setup
   Teardown: Test1Teardown
   Property[ThreadingModel] = STA

 WEX::UnitTests::Test2
  WEX::UnitTests::Test2::Example2
   Property[ThreadingModel] = STA
```

### <span id="name"></span><span id="NAME"></span>/name:&lt;testname&gt;

Test name based selection is an easy alternative to "/select:@Name='&lt;testname&gt;'". The &lt;testname&gt; can still contain wildcard characters ("\*" and "?"), but should not be contained within single quotes. If /select and /name both are specified at the command prompt, then /select query takes precedence and /name is ignored.

<span id="te.exe_test1.dll__name__TestToLower"></span><span id="te.exe_test1.dll__name__testtolower"></span><span id="TE.EXE_TEST1.DLL__NAME__TESTTOLOWER"></span>te.exe test1.dll /name:\*TestToLower  
**Interpretation:** Run all tests in test1.dll where method names end with 'TestToLower'. The same can be represented using selection criteria as /select:@Name='\*TestToLower'.

<span id="te.exe_test1.dll__name__StringTest_"></span><span id="te.exe_test1.dll__name__stringtest_"></span><span id="TE.EXE_TEST1.DLL__NAME__STRINGTEST_"></span>te.exe test1.dll /name:\*StringTest\*  
**Interpretation:** Run all tests in test1.dll which contain the phrase 'StringTest' in their namespace, class or method name.

### <span id="outputFolder"></span><span id="outputfolder"></span><span id="OUTPUTFOLDER"></span>/outputFolder:&lt;folderName&gt;

Specifies a folder to place all generated files. The default is the current directory. You can use environment variables, for example:

**te.exe test1.dll /outputFolder:%TEMP%\\MyOutput**

### <span id="p"></span><span id="P"></span>/p:&lt;ParamName&gt;=&lt;ParamValue&gt;

Defines a runtime parameter with parameter name=ParamName and parameter value=ParamValue. These parameters are accessible from a test method or setup/cleanup methods.

**te.exe test1.dll /p:x=5 /p:myParm=cool**

You can grab x as one of several supported types in your test code. For example, here you can see us retrieving it as both an int and a WEX::Common::String:

```cpp
                int x = 0;
                String xString;
                RuntimeParameters::TryGetValue(L"x", x);
                RuntimeParameters::TryGetValue(L"x", xString);
```

For more information, please visit the [TAEF.Runtime Parameters](runtime-parameters.md) help page.

### <span id="parallel"></span><span id="PARALLEL"></span>/parallel

Executes tests in parallel across multiple processors. Tests must opt-in to parallel execution by being marked with the 'Parallel' metadata.

**te.exe test1.dll /parallel**

For more information, please visit the [Parallel](parallel.md) help page.

### <span id="persistPictResults"></span><span id="persistpictresults"></span><span id="PERSISTPICTRESULTS"></span>/persistPictResults

Caches results generated by PICT.exe for tests using [PICT DataSource](pict-data-source.md) in the current execution. The subsequent test execution will try to utilize the cached results as against running PICT.exe against the same model and seed files.

### <span id="pict"></span><span id="PICT"></span>/pict:&lt;OptionName&gt;=&lt;OptionValue&gt;

Provides options for controlling PICT.exe when it is called for tests using a [PICT DataSource](pict-data-source.md). Setting one of these options currently overrides all associated metadata in the code. The following options are available:

<span id="_Pict_Order_3"></span><span id="_pict_order_3"></span><span id="_PICT_ORDER_3"></span>/Pict:Order=3  
Sets the order of combinations by passing the value via the /o command option for PICT.exe.

<span id="_Pict_ValueSeparator__"></span><span id="_pict_valueseparator__"></span><span id="_PICT_VALUESEPARATOR__"></span>/Pict:ValueSeparator=;  
Sets the value separator by passing the value via the /d command option for PICT.exe.

<span id="_Pict_AliasSeparator__"></span><span id="_pict_aliasseparator__"></span><span id="_PICT_ALIASSEPARATOR__"></span>/Pict:AliasSeparator=+  
Sets the alias separator by passing the value via the /a command option for PICT.exe.

<span id="_Pict_NegativeValuePrefix__"></span><span id="_pict_negativevalueprefix__"></span><span id="_PICT_NEGATIVEVALUEPREFIX__"></span>/Pict:NegativeValuePrefix=!  
Sets the negative value prefix by passing the value via the /n command option for PICT.exe.

<span id="_pict_seedingfile_test.seed"></span><span id="_PICT_SEEDINGFILE_TEST.SEED"></span>/Pict:SeedingFile=test.seed  
Sets the path to the seeding file by passing the value via the /e command option for PICT.exe.

<span id="_Pict_Random_true"></span><span id="_pict_random_true"></span><span id="_PICT_RANDOM_TRUE"></span>/Pict:Random=true  
Turns on or off randomness in the PICT results and makes the PICT data source log the random seed that was used.

<span id="_Pict_RandomSeed_33"></span><span id="_pict_randomseed_33"></span><span id="_PICT_RANDOMSEED_33"></span>/Pict:RandomSeed=33  
Sets the random seed by passing the value via the /r command option for PICT.exe. Setting this will turn on Pict:Random unless Pict:Random is explicitly set to false.

<span id="_Pict_CaseSensitive_true"></span><span id="_pict_casesensitive_true"></span><span id="_PICT_CASESENSITIVE_TRUE"></span>/Pict:CaseSensitive=true  
When set to true, turns on case sensitivity by passing the /c command option to PICT.exe.

<span id="_Pict_Timeout_00_01_30"></span><span id="_pict_timeout_00_01_30"></span><span id="_PICT_TIMEOUT_00_01_30"></span>/Pict:Timeout=00:01:30  
Sets the time to wait for PICT.exe to finish before killing its process. The value is in the format \[Day.\]Hour\[:Minute\[:Second\[.FractionalSeconds\]\]\].

### <span id="runas"></span><span id="RUNAS"></span>/runas:&lt;RunAsType&gt;

Executes tests in specified environment. Please refer to the [RunAs](runas.md) documentation for detailed usage information.

<span id="te.exe__.dll__runas_System"></span><span id="te.exe__.dll__runas_system"></span><span id="TE.EXE__.DLL__RUNAS_SYSTEM"></span>te.exe \*.dll /runas:System  
**Interpretation:** Run all tests as System.

<span id="te.exe__.dll__runas_Elevated"></span><span id="te.exe__.dll__runas_elevated"></span><span id="TE.EXE__.DLL__RUNAS_ELEVATED"></span>te.exe \*.dll /runas:Elevated  
**Interpretation:** Run all tests as an elevated user.

<span id="te.exe__.dll__runas_Restricted"></span><span id="te.exe__.dll__runas_restricted"></span><span id="TE.EXE__.DLL__RUNAS_RESTRICTED"></span>te.exe \*.dll /runas:Restricted  
**Interpretation:** Run all tests as a non-elevated user.

<span id="te.exe__.dll__runas_LowIL"></span><span id="te.exe__.dll__runas_lowil"></span><span id="TE.EXE__.DLL__RUNAS_LOWIL"></span>te.exe \*.dll /runas:LowIL  
**Interpretation:** Run all tests in a Low Integrity process.

### <span id="runIgnoredTests"></span><span id="runignoredtests"></span><span id="RUNIGNOREDTESTS"></span>/runIgnoredTests

Executes or lists (if in conjunction with [/list](#list) or [/listProperties](#listproperties)) all tests, including test classes and test methods with "Ignore" metadata set to "true". By default test classes and test methods with "Ignore" metadata set to "true" are skipped during execution and while listing.

### <span id="runon"></span><span id="RUNON"></span>/runon:&lt;MachineName&gt;

Executes tests remotely, on the specified machine. TAEF authenticates, authorizes and deploys the necessary binaries to execute the tests, and logs all information back to the originating console. Please refer to the [Cross Machine Test Execution](cross-machine-execution.md) documentation for detailed usage information.

<span id="te.exe__.dll__runon_TestMachine1"></span><span id="te.exe__.dll__runon_testmachine1"></span><span id="TE.EXE__.DLL__RUNON_TESTMACHINE1"></span>te.exe \*.dll /runon:TestMachine1  
**Interpretation:** Run all tests remotely on "TestMachine1".

### <span id="select"></span><span id="SELECT"></span>/select:&lt;query&gt;

The selection criteria to be used when selecting tests from each test binary. Selection criteria is composed of one or more of the following:

@\[property name\] = \[value as string\]
@\[property name\] &gt;= \[value as float or integer\]
@\[property name\] &gt; \[value as float or integer\]
@\[property name\] &lt;= \[value as float or integer\]
@\[property name\] &lt; \[value as float or integer\]
-   *Property values as strings must be within single quotes.*
-   *You can specify a composite selection criteria using "and", "or" and "not" (case insensitive).*
-   *Property string values support wildcard characters via "\*" and "?" characters.*
-   *For float and integer values, the "\*" character may also be used as 'exists', but may not be used for partial matching.* For example: **/select:"@Priority=\*"** is valid, but **/select:"@Priority=4\*"** is not.

<span id="te.exe_test1.dll__select____Name___TestToLower__or__Owner__C2___and_not__Priority___3__"></span><span id="te.exe_test1.dll__select____name___testtolower__or__owner__c2___and_not__priority___3__"></span><span id="TE.EXE_TEST1.DLL__SELECT____NAME___TESTTOLOWER__OR__OWNER__C2___AND_NOT__PRIORITY___3__"></span>te.exe test1.dll /select:"(@Name='\*TestToLower' or @Owner='C2') and not(@Priority &lt; 3)"  
**Interpretation:** Run all tests in test1.dll where method names end with 'TestToLower' or where owner is 'C2'; and where Priority is not less than 3.

<span id="te.exe_test1.dll_test2.dll__select__Priority__"></span><span id="te.exe_test1.dll_test2.dll__select__priority__"></span><span id="TE.EXE_TEST1.DLL_TEST2.DLL__SELECT__PRIORITY__"></span>te.exe test1.dll test2.dll /select:@Priority=\*  
**Interpretation:** Run all tests in test1.dll and test2.dll where the Priority has been specified in their test metadata.

<span id="te.exe_test1.dll__select__Name___StringTest__"></span><span id="te.exe_test1.dll__select__name___stringtest__"></span><span id="TE.EXE_TEST1.DLL__SELECT__NAME___STRINGTEST__"></span>te.exe test1.dll /select:@Name='\*StringTest\*'  
**Interpretation:** Run all tests in test1.dll which contain the phrase 'StringTest' in their namespace, class or method name.

### <span id="sessionTimeout"></span><span id="sessiontimeout"></span><span id="SESSIONTIMEOUT"></span>/sessionTimeout:&lt;value&gt;

Sets a session time-out for the entire execution of Te.exe. If the time-out expires, the test session will be gracefully aborted, and the process exit code will signify that a time-out occurred.

**Note:** The time-out value must be specified in the following format:

```cpp
[Day.]Hour[:Minute[:Second[.FractionalSeconds]]] 
```

**Note:** If running under WTT, this value can be used to ensure that the Wtt log file remains intact even if the TAEF session times out.

<span id="te.exe_test1.dll__sessionTimeout_0_0_0.5"></span><span id="te.exe_test1.dll__sessiontimeout_0_0_0.5"></span><span id="TE.EXE_TEST1.DLL__SESSIONTIMEOUT_0_0_0.5"></span>te.exe test1.dll /sessionTimeout:0:0:0.5  
The entire test session will time out after .5 seconds.

<span id="te.exe_test1.dll__sessionTimeout_0_0_45"></span><span id="te.exe_test1.dll__sessiontimeout_0_0_45"></span><span id="TE.EXE_TEST1.DLL__SESSIONTIMEOUT_0_0_45"></span>te.exe test1.dll /sessionTimeout:0:0:45  
The entire test session will time out after 45 seconds.

<span id="te.exe_test1.dll__sessionTimeout_0_20"></span><span id="te.exe_test1.dll__sessiontimeout_0_20"></span><span id="TE.EXE_TEST1.DLL__SESSIONTIMEOUT_0_20"></span>te.exe test1.dll /sessionTimeout:0:20  
The entire test session will time out after 20 minutes.

<span id="te.exe_test1.dll__sessionTimeout_5"></span><span id="te.exe_test1.dll__sessiontimeout_5"></span><span id="TE.EXE_TEST1.DLL__SESSIONTIMEOUT_5"></span>te.exe test1.dll /sessionTimeout:5  
The entire test session will time out after 5 hours.

<span id="te.exe_test1.dll__sessionTimeout_1.2"></span><span id="te.exe_test1.dll__sessiontimeout_1.2"></span><span id="TE.EXE_TEST1.DLL__SESSIONTIMEOUT_1.2"></span>te.exe test1.dll /sessionTimeout:1.2  
The entire test session will time out after 1 day and 2 hours.

### <span id="terminateOnFirstFailure"></span><span id="terminateonfirstfailure"></span><span id="TERMINATEONFIRSTFAILURE"></span>/terminateOnFirstFailure

Terminates the test run the first time a test failure is encountered. All teardown operations for that test are invoked, but all subsequent tests are marked as ignored. Due to a known issue, tests might continue to run when using a test mode.

**te.exe test1.dll /terminateOnFirstFailure**

### <span id="testDependencies"></span><span id="testdependencies"></span><span id="TESTDEPENDENCIES"></span>/testDependencies:&lt;files&gt;

Specifies additional test dependencies to deploy when using [cross machine test execution](cross-machine-execution.md). Unless a full path is provided, TAEF will search relative to the current directory, not the test directory.

<span id="te.exe__.dll__runon_TestMachine1__TestDependencies_test_.jpg_file1.doc"></span><span id="te.exe__.dll__runon_testmachine1__testdependencies_test_.jpg_file1.doc"></span><span id="TE.EXE__.DLL__RUNON_TESTMACHINE1__TESTDEPENDENCIES_TEST_.JPG_FILE1.DOC"></span>te.exe \*.dll /runon:TestMachine1 /TestDependencies:test\*.jpg;file1.doc  
**Interpretation:** Run all tests remotely on "TestMachine1", and copy 'test\*.jpg' and 'file1.doc' over to the remote machine before executing any tests. Each file specification can contain wildcard characters (test.txt; test\*.dll; etc.) to match one or more files.

### <span id="testTimeout"></span><span id="testtimeout"></span><span id="TESTTIMEOUT"></span>/testTimeout:&lt;value&gt;

Sets a global test time-out for the entire execution of Te.exe. This value overrides any [test time-out](standard-test-metadata.md) metadata that may have been set for a given test being executed.

**Note:** The time-out value must be specified in the following format:

```cpp
[Day.]Hour[:Minute[:Second[.FractionalSeconds]]] 
```

**Note:** Will be ignored when used in conjunction with [/inproc](#inproc).

<span id="te.exe_test1.dll__testTimeout_0_0_0.5"></span><span id="te.exe_test1.dll__testtimeout_0_0_0.5"></span><span id="TE.EXE_TEST1.DLL__TESTTIMEOUT_0_0_0.5"></span>te.exe test1.dll /testTimeout:0:0:0.5  
Every test and setup/cleanup method will time out after .5 seconds.

<span id="te.exe_test1.dll__testTimeout_0_0_45"></span><span id="te.exe_test1.dll__testtimeout_0_0_45"></span><span id="TE.EXE_TEST1.DLL__TESTTIMEOUT_0_0_45"></span>te.exe test1.dll /testTimeout:0:0:45  
Every test and setup/cleanup method will time out after 45 seconds.

<span id="te.exe_test1.dll__testTimeout_0_20"></span><span id="te.exe_test1.dll__testtimeout_0_20"></span><span id="TE.EXE_TEST1.DLL__TESTTIMEOUT_0_20"></span>te.exe test1.dll /testTimeout:0:20  
Every test and setup/cleanup method will time out after 20 minutes.

<span id="te.exe_test1.dll__testTimeout_5"></span><span id="te.exe_test1.dll__testtimeout_5"></span><span id="TE.EXE_TEST1.DLL__TESTTIMEOUT_5"></span>te.exe test1.dll /testTimeout:5  
Every test and setup/cleanup method will time out after 5 hours.

<span id="te.exe_test1.dll__testTimeout_1.2"></span><span id="te.exe_test1.dll__testtimeout_1.2"></span><span id="TE.EXE_TEST1.DLL__TESTTIMEOUT_1.2"></span>te.exe test1.dll /testTimeout:1.2  
Every test and setup/cleanup method will time out after 1 day and 2 hours.

### <span id="unicodeOutput"></span><span id="unicodeoutput"></span><span id="UNICODEOUTPUT"></span>/unicodeOutput:&lt;true/false&gt;

When TE is piped to a text file, it outputs unicode by default. The one exception to this is if you have requested to append to an existing ANSII file (via '&gt;&gt;').

In order to override this behavior, you may specify /unicodeOutput:false. This will force TE to always output ANSII to the file.

**te.exe test1.dll /unicodeOutput:false &gt; output.txt**

## <span id="LoggerSettings"></span><span id="loggersettings"></span><span id="LOGGERSETTINGS"></span>Logger Settings


### <span id="appendWttLogging"></span><span id="appendwttlogging"></span><span id="APPENDWTTLOGGING"></span>/appendWttLogging

When WTT logging is enabled, appends to the log file rather than overwriting it. Must be used in conjunction with [/enableWttLogging](#enablewttlogging).

<span id="te.exe_test1.dll__enableWttLogging__appendWttLogging"></span><span id="te.exe_test1.dll__enablewttlogging__appendwttlogging"></span><span id="TE.EXE_TEST1.DLL__ENABLEWTTLOGGING__APPENDWTTLOGGING"></span>te.exe test1.dll /enableWttLogging /appendWttLogging  
Will create, or append to a log file called *TE.wtl* upon test execution completion.

### <span id="enableWttLogging"></span><span id="enablewttlogging"></span><span id="ENABLEWTTLOGGING"></span>/enableWttLogging

Enables WTT logging; Wttlog.dll must be available in your path.

<span id="te.exe_test1.dll__enableWttLogging"></span><span id="te.exe_test1.dll__enablewttlogging"></span><span id="TE.EXE_TEST1.DLL__ENABLEWTTLOGGING"></span>te.exe test1.dll /enableWttLogging  
Will produce a log file called *TE.wtl* upon test execution completion.

### <span id="defaultAppDomain"></span><span id="defaultappdomain"></span><span id="DEFAULTAPPDOMAIN"></span>/defaultAppDomain

Executes managed tests in the default application domain.

<span id="te.exe_managed.test1.dll__defaultAppDomain"></span><span id="te.exe_managed.test1.dll__defaultappdomain"></span><span id="TE.EXE_MANAGED.TEST1.DLL__DEFAULTAPPDOMAIN"></span>te.exe managed.test1.dll /defaultAppDomain  

### <span id="disableConsoleLogging"></span><span id="disableconsolelogging"></span><span id="DISABLECONSOLELOGGING"></span>/disableConsoleLogging

Disables console log output; must be used in conjunction with [/enableWttLogging](#enablewttlogging).

**te.exe test1.dll /disableConsoleLogging /enableWttLogging**

### <span id="logFile"></span><span id="logfile"></span><span id="LOGFILE"></span>/logFile:&lt;name&gt;

Specify a name to use as the wtt log file; must be used in conjunction with [/enableWttLogging](#enablewttlogging).

<span id="te.exe_test1.dll__logFile_myCustomLogFile.xml__enableWttLogging"></span><span id="te.exe_test1.dll__logfile_mycustomlogfile.xml__enablewttlogging"></span><span id="TE.EXE_TEST1.DLL__LOGFILE_MYCUSTOMLOGFILE.XML__ENABLEWTTLOGGING"></span>te.exe test1.dll /logFile:myCustomLogFile.xml /enableWttLogging  
Will produce a log file called *myCustomeLogFile.xml* upon test execution completion.

### <span id="logOutput"></span><span id="logoutput"></span><span id="LOGOUTPUT"></span>/logOutput:&lt;mode&gt;

Sets the output level of the logger. Valid values are:

-   *High*: Enables some additional console output such as printing a time stamp next to every trace.
-   *Low*: Emits only core events (start, end group, etc) and errors. The log file includes lower priority details preceeding any errors to provide context for failures.
-   *LowWithConsoleBuffering*: Same as *Low*, but includes the context of failures in both the log file and console output.
-   *Lowest*: Same as *Low*, but console output includes only errors, test failures, and the summary of execution.

### <span id="version"></span><span id="VERSION"></span>/version

Outputs detailed version information.

### <span id="wttDeviceString"></span><span id="wttdevicestring"></span><span id="WTTDEVICESTRING"></span>/wttDeviceString:&lt;value&gt;

Completely overrides the WttDeviceString used by WexLogger when it initializes WttLogger.

**te.exe test1.dll /wttDeviceString:$Console**

### <span id="wttDeviceStringSuffix"></span><span id="wttdevicestringsuffix"></span><span id="WTTDEVICESTRINGSUFFIX"></span>/wttDeviceStringSuffix:&lt;value&gt;

Appends the specified value to the default WttDeviceString used by WexLogger when it initializes WttLogger. Ignored if [wttDeviceString](#wttdevicestringsuffix) is also specified.

**te.exe test1.dll /wttDeviceStringSuffix:$Console**

## <span id="DebugSettings"></span><span id="debugsettings"></span><span id="DEBUGSETTINGS"></span>Debug Settings


### <span id="breakOnCreate"></span><span id="breakoncreate"></span><span id="BREAKONCREATE"></span>/breakOnCreate

Breaks into the debugger prior to instantiating each test class.

**te.exe test1.dll /breakOnCreate**

### <span id="breakOnError"></span><span id="breakonerror"></span><span id="BREAKONERROR"></span>/breakOnError

Breaks into the debugger if an error or test failure is logged.

**te.exe test1.dll /breakOnError**

### <span id="breakOnInvoke"></span><span id="breakoninvoke"></span><span id="BREAKONINVOKE"></span>/breakOnInvoke

Breaks into the debugger prior to invoking each test method.

**te.exe test1.dll /breakOnInvoke**

### <span id="disableTimeouts"></span><span id="disabletimeouts"></span><span id="DISABLETIMEOUTS"></span>/disableTimeouts

Disables all time-outs during execution. This can be useful while debugging to prevent a timeout when TAEF is waiting on the part of the program that is being debugged.

**te.exe test1.dll /disableTimeouts**

### <span id="miniDumpOnError"></span><span id="minidumponerror"></span><span id="MINIDUMPONERROR"></span>/miniDumpOnError

Takes and logs a mini dump if a test error or failure occurs.

**te.exe test1.dll /miniDumpOnError**

### <span id="miniDumpOnCrash"></span><span id="minidumponcrash"></span><span id="MINIDUMPONCRASH"></span>/miniDumpOnCrash

Takes and logs a mini dump if a test crash occurs.

**te.exe test1.dll /miniDumpOnCrash**

### <span id="rebootStateFile"></span><span id="rebootstatefile"></span><span id="REBOOTSTATEFILE"></span>/rebootStateFile

Explicitly enables execution of [Reboot](reboot.md) tests.

**te.exe test1.dll /rebootStateFile:myFile.xml**

### <span id="reportLoadingIssue"></span><span id="reportloadingissue"></span><span id="REPORTLOADINGISSUE"></span>/reportLoadingIssue

Displays an error description dialog when TAEF fails to load a test dll. Must only be used for investigation of native test dll loading issues.

**te.exe test1.dll /reportLoadingIssue**

### <span id="screenCaptureOnError"></span><span id="screencaptureonerror"></span><span id="SCREENCAPTUREONERROR"></span>/screenCaptureOnError

Takes and logs a screen capture if a test error or failure occurs.

**te.exe test1.dll /screenCaptureOnError**

### <span id="stackFrameCount"></span><span id="stackframecount"></span><span id="STACKFRAMECOUNT"></span>/stackFrameCount:&lt;value&gt;

Specifies the number of stack frames to display when getting call stacks. The default value is 50.

**te.exe test1.dll /stackFrameCount:100**

### <span id="stackTraceOnError"></span><span id="stacktraceonerror"></span><span id="STACKTRACEONERROR"></span>/stackTraceOnError

Takes and logs a stack trace if a test error or failure occurs.

**te.exe test1.dll /stackTraceOnError**

## <span id="TestModes"></span><span id="testmodes"></span><span id="TESTMODES"></span>Test Modes


### <span id="loopTestMode"></span><span id="looptestmode"></span><span id="LOOPTESTMODE"></span>/testmode:Loop

Allows controlling the execution using two variables *Loop* and *LoopTest*.

-   *Loop*: Controls how many times the whole run is executed. Default 1.
-   *LoopTest*: Controls how many times an individual test is executed. Default 10.

<span id="te.exe_test1.dll__testmode_Loop"></span><span id="te.exe_test1.dll__testmode_loop"></span><span id="TE.EXE_TEST1.DLL__TESTMODE_LOOP"></span>te.exe test1.dll /testmode:Loop  
**Interpretation:** Run every test in test1.dll 10 times (default value for *LoopTest*). The whole execution is run once (default value for *Loop*).

<span id="te.exe_test1.dll_test2.dll__testmode_Loop__Loop_3__LoopTest_1"></span><span id="te.exe_test1.dll_test2.dll__testmode_loop__loop_3__looptest_1"></span><span id="TE.EXE_TEST1.DLL_TEST2.DLL__TESTMODE_LOOP__LOOP_3__LOOPTEST_1"></span>te.exe test1.dll test2.dll /testmode:Loop /Loop:3 /LoopTest:1  
**Interpretation:** Run every test in test1.dll and test2.dll once (determined by *LoopTest*). The whole execution (all combined tests in test1.dll and test2.dll) is run 3 times - as determined by *Loop*.

### <span id="stress"></span><span id="STRESS"></span>/testmode:Stress

In 'stress' test mode, TAEF will run tests indefinitely, until Ctrl+C is entered or until a WM\_CLOSE message is sent to TAEF's hidden window. /testmode:stress must be run in conjunction with [/inproc](#inproc).

**te.exe test1.dll /testmode:Stress /inproc**

For detailed information and other parameters supported in this mode, see the documentation [here](test-modes.md).









