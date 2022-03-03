---
title: Application Verifier - Testing Applications
description: Application Verifier- Testing Applications
keywords:
- verifying drivers (Application Verifier)
- driver verification (Application Verifier)
- Application Verifier
- AppVerif.exe
- user-mode application testing
ms.date: 01/12/2022
---

# Application Verifier - Testing Applications

Application Verifier (AppVerifier) is a runtime verification tool for unmanaged code that assists in finding subtle programming errors, security issues and limited user account privilege problems that can be difficult to identify with normal application testing techniques.

To deliver reliable Windows applications:

1.  Test applications written in unmanaged (native) code with Application Verifier under the debugger and with full-page heap before releasing it to customers.
2.  Follow the steps provided by Application Verifier to resolve errant conditions.
3.  Once your application is released, regularly monitor the application failure reports collected, for example by Windows Error Reporting if available.

Thread-pool checks are enabled by default under the "Basics" check heading. As this is included in the default setting, users need only to run Application Verifier on their code with the default settings to leverage these and other important checks.

## Installing and configuring Application Verifier

### Debugger setup 

The application being verified should run under a user-mode debugger or the system should run under a kernel debugger since it will break into a debugger when an error occurs. See [Application Verifier - Debugging Application Verifier Stops](application-verifier-debugging-application-verifier-stops.md) for more debugger details. 

### Settings 

Application Verifier cannot be enabled for a running process. As a result, you need to make settings as described below and then start the application. The settings are persistent until explicitly deleted. Therefore, no matter how many times you launch an application it will start with AppVerifier enabled until the settings are deleted.

## Using Application Verifier Basics Test

The scenarios below illustrate the recommended command line and user interface options. These should be run during all tests that exercise the code to ensure complete coverage. The expectation for these scenarios is that application does not break into debugger and all tests pass with the same pass rate as when run without AppVerifier enabled.

Enable verifier for the application(s) you wish to test using. From the command line: `appverif /verify MyApp.exe`. 

From the user interface: Add your application by right clicking within the Applications area and selecting Add Application. Select the Basics from the Tests area. Click the Save button. 

Notes: 

/verify will enable the basics tests

If you are testing a DLL, Application Verifier has to be enabled for the test executable that is exercising the DLL.

Run the verification layers separately. For example, in one session enable all Basics and on another one enable all LuaPriv checks.

Run ALL your tests exercising the application.

Analyze any debugger break(s) encountered. If a break occurs you will need to understand it and fix it. NOTE: The help contents provide details on the breaks and how to investigate them.

When finished, delete all settings. From the command line: `appverif /n MyApp.exe`. 

From the user interface, remove your application by right clicking within the Applications area and selecting Delete Application. Then click the Save button.

## Heap Corruption

Nearly 10% of application crashes on Windows systems are due to heap corruption. These crashes are nearly impossible to debug after the fact. The best way to avoid these issues is to test with the Page Heap features found in Application Verifier. There are two flavors of Page Heap: "Full" and "Light." Full is the default; it will force a debugger stop instantly upon detecting corruption. This feature MUST be run while under the debugger. However, it is also the most resource demanding. If a user is having timing issues and has already run a scenario under "Full" Page Heap, setting it to "Light" will likely address these issues. Additionally, Light Page Heap does not crash until the process exits. It does provide a stack trace to the allocation, but can take considerably longer to diagnose than leveraging its Full counterpart.

## Using AppVerifier Low Resource Simulation (fault injection)

The expectation for this scenario is that the application does not break into debugger. By not breaking into the debugger means that you have no errors that need to be addressed.

The pass rate for the tests may decrease significantly since random fault injections are introduced into the normal operation.

Enable Application Verifier Low Resource Simulation (fault injection) for the application(s). From the command line: `Appverif /verify MyApp.exe /faults`. From the user interface: Add your application by right clicking within the Applications area and selecting Add Application . Select the Low Resource Simulation from the Tests area. Click the Save button.

Note: If you are testing a DLL, you can apply low resource simulation (fault injection) on a certain DLL instead of the whole process. The command line format would be: 

`appverif /verify TARGET [/faults [PROBABILITY [TIMEOUT [DLL …]]]]`

Example: 

`appverif /verify mytest.exe /faults 50000 1000 d3d9.dll`

Run ALL your tests exercising the application

Analyze any debugger break(s) encountered. If a break occurs you will need to understand it and fix it.

When finished, delete all settings. From the command line: appverif /n MyApp.exe. From the user interface: remove your application by right clicking within the Applications area and selecting Delete Application , clicking the Save button.

Note: Running with and without fault injection exercises largely different code paths in an application and therefore both scenarios must be run in order to get the full benefit of AppVerifier.

### Using Application Verifier with WOW64

You can use either the 32-bit or the 64-bit version of Application Verifier to verify a 32-bit application running under WOW64.

## Analyzing AppVerifier Data

All data created during AppVerifier analysis is stored in the %USERPROFILE%\AppVerifierLogs folder in a binary format. These logs can then be converted to XML via the user interface or command line for further analysis. 

To view the XML files, you can use any tool to view the XML, for example importing into Microsoft Excel - Import the XML file into Excel and use filters or Pivot Tables to reorganize and analyze the collected data.

## Using the Command Line 
 
Application Verifier can be used via the UI or by using command line options. 

Following are examples of how to use the command line (below are the details): 

```dbgcmd
appverif /verify TARGET [/faults [PROBABILITY [TIMEOUT [DLL …]]]]

appverif /verify notepad

appverif -enable LAYER … -for TARGET ... [-with [LAYER].PROPERTY=[VALUE] …] 

appverif -disable LAYER ... -for TARGET ...

appverif -query LAYER ... -for TARGET ...

appverif –configure STOP ... -for TARGET ... [-with STOPPROPERTY=[VALUE] …]

appverif –logtofile {enable|disable}
```

To enable Application Verifier for a specific verification layer for two applications: 

`appverif –enable Heaps Locks –for notepad.exe iexplore.exe` 
 
To enable two layers named X and Y for target test.exe with properties X.DebugLevel and Y.DebugLevel: 

`appverif –enable X Y –for test.exe –with X.DebugLevel=1 Y.DebugLevel=2` 

To disable all checks run on an application: 

`appverif -disable * -for notepad.exe`

OR 

`appverif -delete settings -for notepad.exe` 


To globally enable or disable Application Verifier logging for all processes:

`appverif –logtofile enable`

`appverif –logtofile disable`
 
Logging is enabled by default for all processes.

## Application Verifier Command Line Syntax

Application Verifier Command Line Usage:

```dbgcmd
-enable TEST ... -for TARGET ... [-with [TEST.]PROPERTY=VALUE ...]
-disable TEST ... -for TARGET ...
-query TEST ... -for TARGET ...
-configure STOP ... -for TARGET ... -with PROPERTY=VALUE...
-verify TARGET [-faults [PROBABILITY [TIMEOUT [DLL ...]]]]
-export log -for TARGET -with To=XML_FILE [Symbols=SYMBOL_PATH] [StampFrom=LOG_STAMP] [StampTo=LOG_STAMP] [Log=RELATIVE_TO_LAST_INDEX]
-delete {logs|settings} -for TARGET ...
-stamp log -for TARGET -with Stamp=LOG_STAMP [Log=RELATIVE_TO_LAST_INDEX]
-logtoxml LOGFILE XMLFILE
-installprovider PROVIDERBINARY
-sppath [PROTECTED_PROCESS_LOG_PATH]
-cppath
-logtofile [enable | disable]
```

The command line syntax accepts one or more layers and applies them to one or more targets with optional property specifiers for layers. 

`appverif -enable LAYER ... -for TARGET ... [-with [LAYER].PROPERTY=[VALUE] …]` 
`appverif -disable LAYER ... -for TARGET ...`
`appverif -query LAYER ... -for TARGET ...`
`appverif –configure STOP ... -for TARGET ... [-with STOPPROPERTY=[VALUE] …]`

where: 

LAYER is a standard name for a verification layer. If a new verifier provider is installed then this will expose a new verification layer name to be used in the command line. Example layers are Heap, Handles or Locks.

You can set LAYER to * to specify that the command applies to all layers.

TARGET is a binary name (e.g. notepad.exe). This is a static setting that is persisted in the registry and will be taken into consideration whenever the application is started. For the appverif –disable command, you can set TARGET to * to specify that all targets should be disabled.

PROPERTY is property name specific to the LAYER mentioned in the command line. For example, the Handles layer has traces as property.

VALUE is a value for the property. The type of the value depends on the type associated with the property and it will be enforced. The supported types for now are: boolean (true/false), integer (decimal/octal/hex in C notation), string and multi-string (containing `\0’ between strings and being terminated by `\0\0’). If VALUE is not specified it means the user wants to delete that property and revert behavior to the default value for the property. 

STOP is the number (decimal or hex in C notation) of the verifier stop issue to be configured. The stop codes must be unique (no two layers can use the same stop code therefore the tool itself will determine to what layer the stop belongs to) 


STOPPROPERTY is a property name that is acceptable for verifier stops. If the value is not specified it is assumed the property must be deleted. The allowed properties for stops are (See Configuring Verifier Stops below for more details): 

- ErrorReport 
- Severity 
- Flavor 

The properties can be optionally qualified by the layer they belong to. However, this is not needed if command line enables just one layer. For example, to enable two layers named X and Y for target test.exe with properties X.DebugLevel and Y.DebugLevel the command is: 

`appverif –enable X Y –for test.exe –with X.DebugLevel=1 Y.DebugLevel=2` 

However if layer X is enabled, then an unqualified property name can be used: 

`appverif –enable X –for test.exe –with DebugLevel=1` 
 
The separator character between property name and value can be `=` (equal sign) or `:` (colon). 

### Miscellaneous commands

`appverif –query providers` 

`appverif –delete logs –for TARGET ...`

`appverif –delete settings –for TARGET ...` 

Wipe out completely TARGET from registry. 

`appverif –stamp log –for Target –with Stamp=”LOG_STAMP”[Log= RELATIVE_TO_LAST_INDEX]` 
 
This command will stamp the log with LOG_STAMP. This stamp is useful to identify only a section of a log as relevant when viewing the log in XML form. 

`appverif –export log –for TARGET –with To=XML_FILE[Symbols=SYMBOL_PATH][Stamp=LOG_STAMP][StampTo=LOG_STAMP][Log=RELATIVE_TO_LAST_INDEX]` 

The command above will export a binary log to an xml file. The optional Stamp property is used to identify which part of the log should be exported to XML. If not specified then the entire log will be converted. The Log property has a negative integer as possible value and signifies what log file should be converted starting from last one (assumed if property is not present). For example, launch notepad.exe three times in a row. To access the first log created, specify Log=-2 in the command line.

### Shortcuts for Command Line

Following are shortcuts:

`appverif /verify TARGET [/faults [PROBABILITY [TIMEOUT [DLL …]]]]` 


where: 

TARGET has the same meaning as described above. 

PROBABILITY is the probability to inject faults. Must be a value in the range 0..1000000. If not specified the default value is 5%. 

TIMEOUT is the time interval in milliseconds during process startup when fault injection does not happen. This is done to allow the process to properly startup before faults happen. If not specified the value is 500 msecs.

DLL is the name of module that gets loaded in the process. Typically this is the name of a dynamic library (extension .dll) but can be an ActiveX (extension .ocx) or some other loadable module. 

Examples:

`appverif /verify notepad.exe /faults 100000 1000 msvcrt.dll` 

Enable fault injection for notepad.exe (whenever it will be launched). Faults should happen with probability 10%, only 1000 msecs after process got launched and only for operations initiated from msvcrt.dll.

#### Enabling Fault Injection details

Using the /faults command line will enable fault injection just for OLE_ALLOC and HEAP_ALLOC. However, you can use the command line to configure which type of fault injection you want to turn on. For example, if you want to inject fault into a registry or file API as 2%, use the command line:

`appverif -enable lowres -for hello.exe -with registry=20000 file=20000`

Another example:

```dbgcmd
appverif -query lowres -for hello.exe

Settings for hello.exe:
Test [lowres] enabled.

Include = *
Exclude =
TimeOut = 2000 (0x7D0)
WAIT = 0 (0x0)
HEAP_ALLOC = 20000 (0x4E20)
VIRTUAL_ALLOC = 0 (0x0)
REGISTRY = 20000 (0x4E20)
FILE = 20000 (0x4E20)
EVENT = 0 (0x0)
MAP_VIEW = 0 (0x0)
OLE_ALLOC = 20000 (0x4E20)
STACKS = false
``` 

### Configuring Verifier Stops

Using the command line (or user interface) you can configure verifier stops. Following are examples to leverage: 

`Appverif -configure STOP ... -for TARGET ... -with PROPERTY=VALUE ...`
 
STOP is stop code such as 0x200 0x201

TARGET is application name such as foo.exe

PROPERTY can be one of the “ErrorReport”, “Severity”, and “Flavor”

For the ErrorReport , VALUE can be the combination of the following values.

0x00000001 means the stop is active. (If this bit is zero, it means the stop is disabled)

0x00000020 means the stop will break into debugger using a breakpoint.

0x00000040 means the stop break into debugger by generating a Verifier Exception.

0x00000080 means the stop will be logged in the log file.

0x00000100 means the stack trace for this stop will be logged in the log file.

For the Severity , VALUE can be one of followings.

0x00000003 Informative stop.

0x0000000F Warning.

0x0000003F Error.

For the Flavor , Value can be the combination of the following values.

0x00000002 Non-continuable stop.

0x00000010 This stop will only appear one time. It will be ignored the following time within the test run.

For example, disable stops 0x2700, 0x2701 for foo.exe

`Appverif –configure 0x2700 0x2701 –for foo.exe –with ErrorReport=0`
 

Configure stop code 0x2700 as breaking into debugger (it’s off by default), saving a log without stack trace, and make it non-continuable

`Appverif –configure 0x2700 –for foo.exe –with ErrorReport=0xA1 Flavor=0x2`
 

## Verifier Stop Options - Advanced Settings 
 
Application Verifier has advanced settings, such as Inactivate, that you may alter per verifier stop.

Access Verifier Stop Options - Verifier stop options are changed on a dialog that lists the available options.
To access the verifier stop options: 

1. Select the name of a test in the Tests pane. 
2. On the Edit menu, select Verifier Stop Options or Right-click the test and select Verifier Stop Options.

### Verifier Stop Options

You may alter the following elements per verifier stop listed by clicking the stop code (note that a description of the stop will appear when clicked).

Inactive is a checkbox that when selected will deactivate the verifier stop code from being run.  

Severity determines how the verifier stop should be flagged: 

- Ignore 
- Information 
- Warning 
- Error 

Error Reporting determines how you would like the specific verifier stop to be reported/logged: 

Log to File - a checkbox that when selected will log to the designated file. 

Log Stack Trace - a checkbox that when selected will log the stack traces when they are available. 

No Break - an option not to break in the debugger. 

Exception - an option along with no break and breakpoint 

Breakpoint - an option along with no break or exception. 

Miscellaneous provides two options 

Stop Once - a checkbox that when selected will only stop on that error once when testing an application. 

Not Continuable - a checkbox that when selected will not allow you to continue without investigating. 

## See Also

[Application Verifier - Overview](application-verifier.md)

[Application Verifier - Features](application-verifier-features.md)

[Application Verifier - Tests within Application Verifier](application-verifier-tests-within-application-verifier.md)

[Application Verifier - Stop Codes and Definitions](application-verifier-stop-codes-and-definitions.md)

[Application Verifier - Debugging Application Verifier Stops](application-verifier-debugging-application-verifier-stops.md)
  
[Application Verifier - Frequently Asked Questions](application-verifier-faqs.md)


 





