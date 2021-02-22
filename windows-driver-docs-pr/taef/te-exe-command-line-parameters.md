---
title: Te.exe Command Options
description: Te.exe Command Options
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Te.exe Command Options

## Usage

**te.exe** \<[test\_binaries](#test_binaries)> \[[/appendWttLogging](#appendwttlogging)\] \[[/breakOnCreate](#breakoncreate)\] \[[/breakOnError](#breakonerror)\] \[[/breakOnInvoke](#breakoninvoke)\] \[[/coloredConsoleOutput](#coloredconsoleoutputtruefalse)\] \[ [/console:flushWrites](#consoleflushwrites)\] \[[/console:position=\[x,y | current\]](#consolepositionxy--current-) \[[/console:size=&lt;x,y&gt;\]](#consolesize-xy--current-) \[ [/console:topmost \]](#consoletopmost) [\[/defaultAppDomain\]](#defaultappdomain) \[[/disableConsoleLogging](#disableconsolelogging)\] \[[/disableTimeouts](#disabletimeouts)\] \[[/dpiaware](#dpiaware) \] \[[/enableWttLogging](#enablewttlogging)\] \[[/inproc](#inproc)\] \[[/isolationLevel](#isolationlevellevel)\] \[[/labMode](#labmode)\] \[[/list](#list)\] \[[/listProperties](#listproperties)\] \[[/logFile:&lt;name&gt;](#logfilename)\] \[[/logOutput:&lt;mode&gt;](#logoutputmode)\] \[[/miniDumpOnCrash](#minidumponcrash)\] \[[/miniDumpOnError](#minidumponerror)\] \[[/name:&lt;testname&gt;](#nametestname)\] \[[/outputFolder:&lt;folderName&gt;](#outputfolderfoldername)\] \[[/p:&lt;ParamName&gt;=&lt;ParamValue&gt;](#pparamnameparamvalue)\] \[[/parallel](#parallel)\] \[[/persistPictResults](#persistpictresults)\] \[[/pict:&lt;OptionName&gt;=&lt;OptionValue&gt;](#pictoptionnameoptionvalue)\] [\[/rebootStateFile\]](#rebootstatefile) \[[/reportLoadingIssue](#reportloadingissue)\] \[[/runas:&lt;RunAsType&gt;](#runasrunastype)\] \[[/runIgnoredTests](#runignoredtests)\] \[[/runon:&lt;MachineName&gt;](#runonmachinename)\] \[[/screenCaptureOnError](#screencaptureonerror)\] \[[/select:&lt;query&gt;](#selectquery)\] \[[/sessionTimeout:&lt;value&gt;](#sessiontimeoutvalue)\] \[[/stackFrameCount:&lt;value&gt;](#stackframecountvalue)\] \[[/stackTraceOnError](#stacktraceonerror)\] \[[/terminateOnFirstFailure](#terminateonfirstfailure)\] \[[/testDependencies:&lt;files&gt;](#testdependenciesfiles)\] \[[/testmode:Loop](#testmodeloop)\] \[[/testmode:Stress](#testmodestress)\] \[[/testTimeout:&lt;value&gt;](#testtimeoutvalue)\] \[[/unicodeOutput:&lt;true/false&gt;](#unicodeoutputtruefalse)\] [\[/version\]](#version) \[[/wttDeviceString:&lt;value&gt;](#wttdevicestringvalue)\] \[[/wttDeviceStringSuffix:&lt;value&gt;](#wttdevicestringsuffixvalue)\]

## Selection/Execution Commands

### test_binaries

Specify one or more test files to execute (separated by spaces). Wildcard characters are supported.

#### te.exe test1.dll

**Interpretation:** Run all tests in test1.dll.

#### te.exe test1.dll test2.dll test3.dll

**Interpretation:** Run all tests in test1.dll, test2.dll and test3.dll.

#### te.exe \*.dll

**Interpretation:** Run all tests in all dlls in the current directory.

### /coloredConsoleOutput:\<true/false>

Specifies whether or not TAEF should output colored console text. The default is true. If set to false, TAEF will output all text with the default console color.

`te.exe test1.dll /coloredConsoleOutput:false`

### /console:\<optionName>=\<value>

Provides options for configuring TE's use of the console. The following options are available:

#### /console:flushWrites

Causes console output to be flushed after every line is written - useful when TE.exe's output has been redirected.

#### /console:position=\[x,y | current \]

Sets the position (in pixels) of the console window relative to the corner of the primary monitor. Use a value of **current** to specify that the current console position should be stored and used when resuming from reboot.

#### /console:size=\[ \<x,y\> | current \]

Sets the size of the console window (in character dimensions). The screen buffer size will be increased to match the size of the window if necessary. Use a value of **current** to specify that the current console size should be stored and used when resuming from reboot.

#### /console:topmost

Keeps the console running te.exe 'topmost' in the desktop z-order for the duration of execution.

### /dpiaware

Executes tests in a process marked as DPI-aware, see [High DPI](/windows/desktop/hidpi/high-dpi-desktop-application-development-on-windows). This can also be set via metadata ("DpiAware").

### /inproc

Execute all tests within the TE.exe process itself rather than within TE.ProcessHost.exe.

te.exe test1.dll /inproc

> [!NOTE]
> TE only supports executing one test dll at a time when using the */inproc* setting.

### /isolationLevel:\<Level>

Specifies the minimum level of isolation to be used when executing TAEF tests. If this value conflicts with the IsolationLevel specified as metadata, the value becomes the isolation level with the tightest scope. See [Test Isolation](test-isolation.md) for more details.

`te.exe test1.dll /isolationLevel:Class`

### /labMode

Executes tests and removes potential blocking UI (for example, Windows Error Reporting dialogs on crashing tests).

### /list

Lists the names of all the [test\_binaries](#test_binaries) and the classes and methods within them. If selection criteria is specified, lists only the names of those which meet the criteria.

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
 te.exe test1.dll test2.dll /select:@name='*Example2*' /list

 WEX::UnitTests::Test1
  WEX::UnitTests::Test1::Example2

 WEX: :UnitTests::Test2
  WEX::UnitTests::Test2::Example2
```

### /listProperties

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
 te.exe test1.dll test2.dll /select:@name='*Example2*' /listProperties

 WEX::UnitTests::Test1
  WEX::UnitTests::Test1::Example2
   Setup: Test1Setup
   Teardown: Test1Teardown
   Property[ThreadingModel] = STA

 WEX::UnitTests::Test2
  WEX::UnitTests::Test2::Example2
   Property[ThreadingModel] = STA
```

### /name:\<testname>

Test name based selection is an easy alternative to "/select:@Name='&lt;testname&gt;'". The &lt;testname&gt; can still contain wildcard characters ("\*" and "?"), but should not be contained within single quotes. If /select and /name both are specified at the command prompt, then /select query takes precedence and /name is ignored.

te.exe test1.dll /name:\*TestToLower  

**Interpretation:** Run all tests in test1.dll where method names end with 'TestToLower'. The same can be represented using selection criteria as /select:@Name='\*TestToLower'.

te.exe test1.dll /name:\*StringTest\*  

**Interpretation:** Run all tests in test1.dll which contain the phrase 'StringTest' in their namespace, class or method name.

### /outputFolder:\<folderName>

Specifies a folder to place all generated files. The default is the current directory. You can use environment variables, for example:

`te.exe test1.dll /outputFolder:%TEMP%\\MyOutput`

### /p:\<ParamName>=\<ParamValue>

Defines a runtime parameter with parameter name=ParamName and parameter value=ParamValue. These parameters are accessible from a test method or setup/cleanup methods.

`te.exe test1.dll /p:x=5 /p:myParm=cool`

You can grab x as one of several supported types in your test code. For example, here you can see us retrieving it as both an int and a WEX::Common::String:

```cpp
                int x = 0;
                String xString;
                RuntimeParameters::TryGetValue(L"x", x);
                RuntimeParameters::TryGetValue(L"x", xString);
```

For more information, please visit the [TAEF.Runtime Parameters](runtime-parameters.md) help page.

### /parallel

Executes tests in parallel across multiple processors. Tests must opt-in to parallel execution by being marked with the 'Parallel' metadata.

`te.exe test1.dll /parallel`

For more information, please visit the [Parallel](parallel.md) help page.

### /persistPictResults

Caches results generated by PICT.exe for tests using [PICT DataSource](pict-data-source.md) in the current execution. The subsequent test execution will try to utilize the cached results as against running PICT.exe against the same model and seed files.

### /pict:\<OptionName>=\<OptionValue>

Provides options for controlling PICT.exe when it is called for tests using a [PICT DataSource](pict-data-source.md). Setting one of these options currently overrides all associated metadata in the code. The following options are available:

/Pict:Order=3  
Sets the order of combinations by passing the value via the /o command option for PICT.exe.

/Pict:ValueSeparator=;  
Sets the value separator by passing the value via the /d command option for PICT.exe.

/Pict:AliasSeparator=+  
Sets the alias separator by passing the value via the /a command option for PICT.exe.

Pict:NegativeValuePrefix=!  
Sets the negative value prefix by passing the value via the /n command option for PICT.exe.

/Pict:SeedingFile=test.seed  
Sets the path to the seeding file by passing the value via the /e command option for PICT.exe.

/Pict:Random=true  
Turns on or off randomness in the PICT results and makes the PICT data source log the random seed that was used.

/Pict:RandomSeed=33  
Sets the random seed by passing the value via the /r command option for PICT.exe. Setting this will turn on Pict:Random unless Pict:Random is explicitly set to false.

/Pict:CaseSensitive=true  
When set to true, turns on case sensitivity by passing the /c command option to PICT.exe.

/Pict:Timeout=00:01:30  
Sets the time to wait for PICT.exe to finish before killing its process. The value is in the format \[Day.\]Hour\[:Minute\[:Second\[.FractionalSeconds\]\]\].

### /runas:\<RunAsType>

Executes tests in specified environment. Please refer to the [RunAs](runas.md) documentation for detailed usage information.

te.exe \*.dll /runas:System  

**Interpretation:** Run all tests as System.

te.exe \*.dll /runas:Elevated  

**Interpretation:** Run all tests as an elevated user.

te.exe \*.dll /runas:Restricted  

**Interpretation:** Run all tests as a non-elevated user.

te.exe \*.dll /runas:LowIL  

**Interpretation:** Run all tests in a Low Integrity process.

### /runIgnoredTests

Executes or lists (if in conjunction with [/list](#list) or [/listProperties](#listproperties)) all tests, including test classes and test methods with "Ignore" metadata set to "true". By default test classes and test methods with "Ignore" metadata set to "true" are skipped during execution and while listing.

### /runon:\<MachineName>

Executes tests remotely, on the specified machine. TAEF authenticates, authorizes and deploys the necessary binaries to execute the tests, and logs all information back to the originating console. Please refer to the [Cross Machine Test Execution](cross-machine-execution.md) documentation for detailed usage information.

te.exe \*.dll /runon:TestMachine1

**Interpretation:** Run all tests remotely on "TestMachine1".

### /select:\<query>

The selection criteria to be used when selecting tests from each test binary. Selection criteria is composed of one or more of the following:

@\[property name\] = \[value as string\]

@\[property name\] &gt;= \[value as float or integer\]

@\[property name\] &gt; \[value as float or integer\]

@\[property name\] &lt;= \[value as float or integer\]

@\[property name\] &lt; \[value as float or integer\]

* *Property values as strings must be within single quotes.*
* *You can specify a composite selection criteria using "and", "or" and "not" (case insensitive).*
* *Property string values support wildcard characters via "\*" and "?" characters.*
* *For float and integer values, the "\*" character may also be used as 'exists', but may not be used for partial matching.* For example: **/select:"@Priority=\*"** is valid, but **/select:"@Priority=4\*"** is not.

te.exe test1.dll /select:"(@Name='\*TestToLower' or @Owner='C2') and not(@Priority &lt; 3)"

**Interpretation:** Run all tests in test1.dll where method names end with 'TestToLower' or where owner is 'C2'; and where Priority is not less than 3.

te.exe test1.dll test2.dll /select:@Priority=\*

**Interpretation:** Run all tests in test1.dll and test2.dll where the Priority has been specified in their test metadata.

te.exe test1.dll /select:@Name='\*StringTest\*'  

**Interpretation:** Run all tests in test1.dll which contain the phrase 'StringTest' in their namespace, class or method name.

### /sessionTimeout:\<value>

Sets a session time-out for the entire execution of Te.exe. If the time-out expires, the test session will be gracefully aborted, and the process exit code will signify that a time-out occurred.

> [!NOTE]
> The time-out value must be specified in the following format:

```cpp
[Day.]Hour[:Minute[:Second[.FractionalSeconds]]]
```

> [!NOTE]
> If running under WTT, this value can be used to ensure that the Wtt log file remains intact even if the TAEF session times out.

te.exe test1.dll /sessionTimeout:0:0:0.5  

The entire test session will time out after .5 seconds.

te.exe test1.dll /sessionTimeout:0:0:45  

The entire test session will time out after 45 seconds.

te.exe test1.dll /sessionTimeout:0:20  

The entire test session will time out after 20 minutes.

te.exe test1.dll /sessionTimeout:5  

The entire test session will time out after 5 hours.

te.exe test1.dll /sessionTimeout:1.2  

The entire test session will time out after 1 day and 2 hours.

### /terminateOnFirstFailure

Terminates the test run the first time a test failure is encountered. All teardown operations for that test are invoked, but all subsequent tests are marked as ignored. Due to a known issue, tests might continue to run when using a test mode.

`te.exe test1.dll /terminateOnFirstFailure`

### /testDependencies:\<files>

Specifies additional test dependencies to deploy when using [cross machine test execution](cross-machine-execution.md). Unless a full path is provided, TAEF will search relative to the current directory, not the test directory.

te.exe \*.dll /runon:TestMachine1 /TestDependencies:test\*.jpg;file1.doc  

**Interpretation:** Run all tests remotely on "TestMachine1", and copy 'test\*.jpg' and 'file1.doc' over to the remote machine before executing any tests. Each file specification can contain wildcard characters (test.txt; test\*.dll; etc.) to match one or more files.

### /testTimeout:\<value>

Sets a global test time-out for the entire execution of Te.exe. This value overrides any [test time-out](standard-test-metadata.md) metadata that may have been set for a given test being executed.

> [!NOTE]
> The time-out value must be specified in the following format:

```cpp
[Day.]Hour[:Minute[:Second[.FractionalSeconds]]]
```

> [!NOTE]
> Will be ignored when used in conjunction with [/inproc](#inproc).

te.exe test1.dll /testTimeout:0:0:0.5  

Every test and setup/cleanup method will time out after .5 seconds.

te.exe test1.dll /testTimeout:0:0:45  

Every test and setup/cleanup method will time out after 45 seconds.

te.exe test1.dll /testTimeout:0:20  

Every test and setup/cleanup method will time out after 20 minutes.

te.exe test1.dll /testTimeout:5  

Every test and setup/cleanup method will time out after 5 hours.

te.exe test1.dll /testTimeout:1.2  

Every test and setup/cleanup method will time out after 1 day and 2 hours.

### /unicodeOutput:\<true/false>

When TE is piped to a text file, it outputs unicode by default. The one exception to this is if you have requested to append to an existing ANSII file (via '&gt;&gt;').

In order to override this behavior, you may specify /unicodeOutput:false. This will force TE to always output ANSII to the file.

`te.exe test1.dll /unicodeOutput:false > output.txt`

## Logger Settings

### /appendWttLogging

When WTT logging is enabled, appends to the log file rather than overwriting it. Must be used in conjunction with [/enableWttLogging](#enablewttlogging).

te.exe test1.dll /enableWttLogging /appendWttLogging  

Will create, or append to a log file called *TE.wtl* upon test execution completion.

### /enableWttLogging

Enables WTT logging; Wttlog.dll must be available in your path.

te.exe test1.dll /enableWttLogging

Will produce a log file called *TE.wtl* upon test execution completion.

### /defaultAppDomain

Executes managed tests in the default application domain.

te.exe managed.test1.dll /defaultAppDomain  

### /disableConsoleLogging

Disables console log output; must be used in conjunction with [/enableWttLogging](#enablewttlogging).

`te.exe test1.dll /disableConsoleLogging /enableWttLogging`

### /logFile:\<name>

Specify a name to use as the wtt log file; must be used in conjunction with [/enableWttLogging](#enablewttlogging).

te.exe test1.dll /logFile:myCustomLogFile.xml /enableWttLogging  

Will produce a log file called *myCustomeLogFile.xml* upon test execution completion.

### /logOutput:\<mode>

Sets the output level of the logger. Valid values are:

* *High*: Enables some additional console output such as printing a time stamp next to every trace.
* *Low*: Emits only core events (start, end group, etc) and errors. The log file includes lower priority details preceeding any errors to provide context for failures.
* *LowWithConsoleBuffering*: Same as *Low*, but includes the context of failures in both the log file and console output.
* *Lowest*: Same as *Low*, but console output includes only errors, test failures, and the summary of execution.

### /version

Outputs detailed version information.

### /wttDeviceString:\<value>

Completely overrides the WttDeviceString used by WexLogger when it initializes WttLogger.

`te.exe test1.dll /wttDeviceString:$Console`

### /wttDeviceStringSuffix:\<value>

Appends the specified value to the default WttDeviceString used by WexLogger when it initializes WttLogger. Ignored if [wttDeviceString](#wttdevicestringvalue) is also specified.

`te.exe test1.dll /wttDeviceStringSuffix:$Console`

## Debug Settings

### /breakOnCreate

Breaks into the debugger prior to instantiating each test class.

`te.exe test1.dll /breakOnCreate`

### /breakOnError

Breaks into the debugger if an error or test failure is logged.

`te.exe test1.dll /breakOnError`

### /breakOnInvoke

Breaks into the debugger prior to invoking each test method.

`te.exe test1.dll /breakOnInvoke`

### /disableTimeouts

Disables all time-outs during execution. This can be useful while debugging to prevent a timeout when TAEF is waiting on the part of the program that is being debugged.

`te.exe test1.dll /disableTimeouts`

### /miniDumpOnError

Takes and logs a mini dump if a test error or failure occurs.

`te.exe test1.dll /miniDumpOnError`

### /miniDumpOnCrash

Takes and logs a mini dump if a test crash occurs.

`te.exe test1.dll /miniDumpOnCrash`

### /rebootStateFile

Explicitly enables execution of [Reboot](reboot.md) tests.

`te.exe test1.dll /rebootStateFile:myFile.xml`

### /reportLoadingIssue

Displays an error description dialog when TAEF fails to load a test dll. Must only be used for investigation of native test dll loading issues.

`te.exe test1.dll /reportLoadingIssue`

### /screenCaptureOnError

Takes and logs a screen capture if a test error or failure occurs.

`te.exe test1.dll /screenCaptureOnError`

### /stackFrameCount:\<value>

Specifies the number of stack frames to display when getting call stacks. The default value is 50.

`te.exe test1.dll /stackFrameCount:100`

### /stackTraceOnError

Takes and logs a stack trace if a test error or failure occurs.

`te.exe test1.dll /stackTraceOnError`

## Test Modes

### /testmode:Loop

Allows controlling the execution using two variables *Loop* and *LoopTest*.

* *Loop*: Controls how many times the whole run is executed. Default 1.
* *LoopTest*: Controls how many times an individual test is executed. Default 10.

te.exe test1.dll /testmode:Loop  

**Interpretation:** Run every test in test1.dll 10 times (default value for *LoopTest*). The whole execution is run once (default value for *Loop*).

te.exe test1.dll test2.dll /testmode:Loop /Loop:3 /LoopTest:1  

**Interpretation:** Run every test in test1.dll and test2.dll once (determined by *LoopTest*). The whole execution (all combined tests in test1.dll and test2.dll) is run 3 times - as determined by *Loop*.

### /testmode:Stress

In 'stress' test mode, TAEF will run tests indefinitely, until Ctrl+C is entered or until a WM\_CLOSE message is sent to TAEF's hidden window. /testmode:stress must be run in conjunction with [/inproc](#inproc).

`te.exe test1.dll /testmode:Stress /inproc`

For detailed information and other parameters supported in this mode, see [Test Modes](test-modes.md).
