---
title: User Mode Monitor
description: User Mode Monitor
ms.assetid: CE6CEC2C-5E8E-40aa-A5D3-0062D6F82EFE
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# User Mode Monitor


The User Mode Monitor allows tests to obtain more context about the execution of the 'process under test' in order to obtain more context for investigating test failures, or for enabling better verification from existing tests. The current User Mode Monitor implementation provides a basic implementation, with more customization and configuration coming in subsequent releases.

## <span id="Introduction"></span><span id="introduction"></span><span id="INTRODUCTION"></span>Introduction


The User Mode Monitor (UMM) uses low-level Windows API's to be notified of all 'debugger' events that originate from a given process - thread start and stop, module load, crashes, and handled exceptions to name just a few. Upon receiving a debugger event the UMM code can take one of several actions, including logging comments, logging errors (in order to fail a test), or even taking a minidump of the Process Under Test.

## <span id="Enabling_the_User_Mode_Monitor"></span><span id="enabling_the_user_mode_monitor"></span><span id="ENABLING_THE_USER_MODE_MONITOR"></span>Enabling the User Mode Monitor


To enable the UMM for a given test case, you need to provide two pieces of configuration:

1.  The test must be marked with the 'ProcessUnderTest' metadata value. This allows the UMM to identify the process that is being tested.
2.  The Te.exe command line should include '/userModeMonitor' to turn on the UMM functionality.

The following points should be taken into account when using the UMM code;

1.  If there are multiple instances of the named Process Under Test running, then the instance that is discovered first will be used.
2.  The user that is executing the test automation must have sufficient permission to receive debugger events from the Process Under Test.
3.  The UMM code will 'attach' to the Process Under Test after the all setup fixtures have executed, and 'detach' before cleanup fixtures are executed. This allows a test's setup fixtures to start the Process Under Test, and perform any necessary initialization to prepare for the test.

## <span id="Supported_User_Mode_Monitor__Actions_"></span><span id="supported_user_mode_monitor__actions_"></span><span id="SUPPORTED_USER_MODE_MONITOR__ACTIONS_"></span>Supported User Mode Monitor 'Actions'


The User Mode Monitor has a set of 'Actions' that it can take when a given debugger event occurs in the monitored process. In the current implementation, a given event will only invoke it's default action; there is currently no configuration support.

| Action     | Description                                                            |
|------------|------------------------------------------------------------------------|
| LogComment | Adds a comment to the log, with contextual information from the event. |
| LogError   | Logs an error to the log, which will fail the current test.            |
| Minidump   | Writes out a minidump and saves it to the Log.                         |
| Ignore     | Does nothing.                                                          |

 

## <span id="Supported_User_Mode_Monitor__Events_"></span><span id="supported_user_mode_monitor__events_"></span><span id="SUPPORTED_USER_MODE_MONITOR__EVENTS_"></span>Supported User Mode Monitor 'Events'


The User Mode Monitor surfaces 'events' that can apply one of the 'actions' that are listed, above. The following table shows the current list of reported events, along with the default Action that will be performed when the event is received.

| Event                                | Default Action (second chance default action) |
|--------------------------------------|-----------------------------------------------|
| Create thread                        | Ignore                                        |
| Exit thread                          | Ignore                                        |
| Create process                       | Ignore                                        |
| Exit process                         | LogError                                      |
| Load module                          | LogComment                                    |
| Unload module                        | Ignore                                        |
| System error                         | Ignore                                        |
| Initial breakpoint                   | LogError                                      |
| Initial module load                  | Ignore                                        |
| Debuggee output                      | LogComment                                    |
| Access violation                     | LogError (LogError)                           |
| Assertion failure                    | LogError (LogError)                           |
| Application hang                     | LogError (LogError)                           |
| Break instruction exception          | LogError                                      |
| Break instruction exception continue | Ignore                                        |
| C++ EH exception                     | LogError (LogError)                           |
| CLR exception                        | LogError (LogError)                           |
| CLR notification exception           | LogError (Ignore)                             |
| Control-LogError exception           | LogError                                      |
| Control-LogError exception continue  | Ignore                                        |
| Control-C exception                  | LogError                                      |
| Control-C exception continue         | Ignore                                        |
| Data misaligned                      | LogError (LogError)                           |
| Debugger command exception           | Ignore                                        |
| Guard page violation                 | LogError (LogError)                           |
| Illegal instruction                  | LogError (LogError)                           |
| In-page I/O error                    | LogError (LogError)                           |
| Integer divide-by-zero               | LogError (LogError)                           |
| Integer overflow                     | LogError (LogError)                           |
| Invalid handle                       | LogError                                      |
| Invalid handle continue              | LogError                                      |
| Invalid lock sequence                | LogError (LogError)                           |
| Invalid system call                  | LogError (LogError)                           |
| Port disconnected                    | LogError (LogError)                           |
| Service hang                         | LogError (LogError)                           |
| Single step exception                | LogError                                      |
| Single step exception continue       | Ignore                                        |
| Stack buffer overflow                | LogError (LogError)                           |
| Stack overflow                       | LogError (LogError)                           |
| Verifier stop                        | LogError (LogError)                           |
| Visual C++ exception                 | Ignore (Ignore)                               |
| Wake debugger                        | LogError (LogError)                           |
| WOW64 breakpoint                     | LogError (Ignore)                             |
| WOW64 single step exception          | LogError (Ignore)                             |
| Other exception                      | LogError (LogError)                           |

 

## <span id="Example"></span><span id="example"></span><span id="EXAMPLE"></span>Example


In order to illustrate the use of the UMM functionality, let's take a look at a (slightly contrived) example of a test that automates 'MSPaint':

```cpp
namespace UserModeMonitorExample
{
    using System;
    using System.Diagnostics;
    using System.Threading;
    using Microsoft.VisualStudio.TestTools.UnitTesting;
    using WEX.Logging.Interop;
    using WEX.TestExecution;

    [TestClass]
    public class BasicExample
    {
        [TestInitialize]
        public void TestInitialize()
        {
            Process[] runningPaintInstances = Process.GetProcessesByName("mspaint.exe");

            Verify.IsTrue(runningPaintInstances.Length == 0, "There are no running instances of mspaint.exe");

            this.mspaintUnderTest = Process.Start("mspaint.exe");
        }

        [TestCleanup]
        public void TestCleanup()
        {
            // Close the &#39;mspaint under test&#39; - if it&#39;s already gone, this will throw, but that&#39;s no big deal.
            this.mspaintUnderTest.CloseMainWindow();
        }

        [TestMethod]
        [TestProperty("ProcessUnderTest", "mspaint.exe")]
        [TestProperty("Description", "Shows how a test can be failed if the UI is closed from underneath the test.")]
        public void SimpleInteraction()
        {
            Log.Comment("If the &#39;user mode monitor&#39; is enabled and mspaint.exe is closed,&quot;);
            Log.Comment(&quot;then this test will be failed.&quot;);
            Log.Comment("Sleeping for 5 seconds");

            Thread.Sleep(TimeSpan.FromSeconds(5));
        }

        private Process mspaintUnderTest;
    }
}
```

Here's a quick breakdown of the structure of the test:

-   The 'SimpleInteraction' test represents a test that interacts with a UI based application - in this case it's "MSPaint.exe". Notice, that the "ProcessUnderTest" metadata has been applied to call out that this test is testing the "mspaint.exe" process.
-   The test has a setup fixture that makes sure that there's no pre-existing instances running, and launches a single instance to test.
-   The test also has a cleanup fixture that closes the instance that was launched in the setup fixture.

The 'test' is very straight forward, let's look at possible outcomes:

1.  The test runs without problems. This is the best possible outcome.
2.  Without UMM enabled, a user closes the MSPaint instance during execution. In this case, the test will pass, but the cleanup will fail with an 'InvalidOperationException'.
3.  With UMM enabled, a user closes the MSPaint instance during execution. In this case, the UMM code will log an error showing that the process closed failing the test. The cleanup fails as in case (2).

With UMM enabled, the errant behavior is reported immediately, and directly affects the test result. This is a much better testing pattern since errors are reported as early as possible and extra context is provided to help with debugging or understanding test failures.

 

 





