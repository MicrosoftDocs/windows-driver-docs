---
title: Test Modes
description: Test Modes
ms.assetid: 1E9C0198-8C74-4966-A401-329723B5A933
---

# Test Modes


TAEF provides several test modes which modify test execution behavior in various ways. Make sure that you are familiar with basic execution of TAEF, see [Authoring Tests](authoring-tests.md) and [Executing Tests](executing-tests.md), before proceeding with this section.

**Note:** Test modes are not compatible with each other; only one test mode may be enabled during a given test run.

The following test modes are currently provided by TAEF:

-   [Loop](#loop)
-   [Stress](#stress)

## <span id="loop"></span><span id="LOOP"></span>Loop Test Mode


The "Loop Test Mode" provides simple functionality for iterating individual tests, or entire test runs. Loop Test Mode is great for verifying the robustness of test automation, or getting easy stress or long haul automation.

Loop Test Mode is enabled by specifying the /testmode:loop command option. There are two other - optional - parameters that control the specific behavior:

<span id="_Loop__loopNum_"></span><span id="_loop__loopnum_"></span><span id="_LOOP__LOOPNUM_"></span>/Loop:&lt;loopNum&gt;  
Controls how many times the whole run is executed (default:1).

<span id="_LoopTest__loopTestNum_"></span><span id="_looptest__looptestnum_"></span><span id="_LOOPTEST__LOOPTESTNUM_"></span>/LoopTest:&lt;loopTestNum&gt;  
Controls how many times the each test in the run gets executed (default:10).

The diagram, below, shows how TAEF represents a test run comprising of a single Test File, containing a single Test Class, that contains two Test Methods:

![the 'looptest' parameter](images/looptestmode-looptest.png)

The arrows on the diagram show the flow of execution under TAEF; showing how TAEF executes setup fixtures, then the tests themselves, and the appropriate cleanup fixtures are executed after the tests are complete. The 'looptest' value causes TAEF to iterate around the test methods themselves - the *smallest possible scope*. Notice that the setup and cleanup for the test **aren't** executed. The same behavior occurs for data-driven tests, too: the 'looptest' value controls the looping at the 'Test Method' level.

There are times when it's not possible to loop around just the Test Method, and that's where the 'loop' parameter can be used. The diagram, below, shows how TAEF represents a test run comprising of a two test files, each file containing a single test class and each test class containing a single test method:

![the 'loop' parameter](images/looptestmode-loop.png)

The 'loop' parameter controls looping at the *largest possible scope*; the entire run. If you specify a single test file to Te.exe, or if you have multiple test files, the entire run will be looped the specified number of times.

## <span id="stress"></span><span id="STRESS"></span>Stress Test Mode


'Stress' Test Mode for TAEF helps users run tests in a 'stress' environment. By enabling Stress Test Mode via the "/testmode:stress" command option, the following behavior is enabled:

1.  *Te.exe runs indefinitely* - Te.exe requires Ctrl+C to be sent to the command prompt, or a WM\_CLOSE message to be sent to its hidden window to stop.
2.  *Te.exe iterates on the first 'group' of tests that it runs* - To avoid loading subsequent files during a run, Te.exe will iterate on the first 'group' of tests that it runs. Note that:
    1.  If you specify multiple Test Files at the command prompt, without any selection, only the first Test File will be executed.
    2.  If multiple Test Files along with a selection query are specified at the command prompt, only the tests within the first Test File where the selection criteria is satisfied will be executed.
    3.  If a Test File is specified that is data-driven at a module level, the first combination of data-driven parameters that is executed will be looped.

3.  *A 'stress logger' is enabled* - In order to minimize the amount of resources that logging would consume, Te.exe switches to a minimal output logger:
    -   Only errors are written to the console - no other Log entries are written out.
    -   Every 60 seconds, the Logger will output the current pass/fail counts to the console.
    -   Every second the Logger will output a single '.' to show that Te.exe is still working.

When running in stress test mode, you also need to specify the "/inproc" switch - which means that all stress execution runs in the Te.exe process. This restriction removes the need for TAEF to launch and maintain the separate sandbox process for execution, thereby minimizing test failures due to failed memory allocations.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[taef\taef]:%20Test%20Modes%20%20RELEASE:%20%289/12/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




