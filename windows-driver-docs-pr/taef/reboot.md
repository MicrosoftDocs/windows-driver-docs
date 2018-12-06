---
title: Reboot
description: Reboot
ms.assetid: 8AB66CAB-9BAA-4911-A143-618627226B78
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Reboot


TAEF allows a test to specify that it can cause or require the computer to restart. The feature consists of two to three components: metadata to flag the test as possibly causing or requiring a restart, an API to request that TAEF perform a restart or notify TAEF of an impending test-initiated restart, and a command option to opt in to running these tests when executing locally.

## <span id="behavior_reboot"></span><span id="BEHAVIOR_REBOOT"></span>Behavior


The particular semantics of restarting the computer necessitate some changes to the TAEF execution model, the guarantees of setup and cleanup operations, and the success and failure behavior.

-   The restart behavior is only available to a test (with the appropriate metadata), not to fixtures (setup and cleanup).
-   If the Reboot API is used from anywhere other than a test with the appropriate markup, the function will not return. Instead, TAEF kills the test process. This represents a bug in the way the test was written and the test code should be fixed.
-   Test fixtures will not be run on the restart boundary. This means teardown operations are not run before the restart (no matter whether the test initiates the restart or requests that TAEF cause the restart itself) and setup operations will not be run after the restart.
-   Logging (and consequently log failures) will be ignored from the time you notify or request a restart until the test finishes.

## <span id="metadata_reboot"></span><span id="METADATA_REBOOT"></span>Metadata


To enable use of the Reboot APIs, a test should be flagged by setting the **RebootPossible** metadata to **"true"**. This metadata obeys the usual rules of metadata inheritance, so it can be specified at the class level if any test in your class might restart (though given the rather heavyweight nature of restarting, it would be advisable to make explicit decisions about which test can and cannot initiate restarts). Refer to the documentation on [Authoring Tests in C++](authoring-tests-in-c--.md) and [Authoring Tests in C#](authoring-tests-in-c-.md) for examples of metadata specification.

## <span id="api_reboot"></span><span id="API_REBOOT"></span>API


There are two main functions for handling machine restarts:

-   **Reboot(Option)** requests that TAEF initiate a restart of the test machine.
-   **RebootCustom(Option)** notifies TAEF that the test will be causing a restart of the test machine. This API also supports system crash. TAEF will ensure that the applicable data are flushed after the API returns.

The **Option** parameter specifies the resume behavior, one of:

-   **Rerun**, causing TAEF to execute the same test again after the restart has occurred
-   **Continue**, causing TAEF to execute the next test after the restart has occurred

### <span id="native_reboot"></span><span id="NATIVE_REBOOT"></span>Native

Access the Reboot APIs by including the Interruption.h header and calling the functions in the **WEX::TestExecution::Interruption** namespace. The four possible calls are:

```cpp
using namespace WEX::TestExecution;
Interruption::Reboot(RebootOption::Rerun);
Interruption::Reboot(RebootOption::Continue);
Interruption::RebootCustom(RebootOption::Rerun);
Interruption::RebootCustom(RebootOption::Continue);
```

### <span id="managed_reboot"></span><span id="MANAGED_REBOOT"></span>Managed

Call either of the two methods in the **Interruption** static class in the **WEX.TestExecution** namespace, which is located within **Te.Managed.dll**:

```cpp
using WEX.TestExecution;
Interruption.Reboot(RebootOption.Rerun);
Interruption.Reboot(RebootOption.Continue);
Interruption.RebootCustom(RebootOption.Rerun);
Interruption.RebootCustom(RebootOption.Continue);
```

## <span id="prompt_reboot"></span><span id="PROMPT_REBOOT"></span>Command Prompt Usage


The ideal usage for this feature is to run TAEF tests that will potentially restart with [Cross Machine Execution](cross-machine-execution.md) or through WTT. In these cases TAEF enables restart execution implicitly\* because it should not disrupt your work flow. If you are executing restarting tests manually on the local machine or need to override the default path that TAEF uses to cache its state, you will have to explicitly opt in to restarting tests. If you do not, then any restarting test will be marked as blocked. To enable restart tests when executing locally, use the following command argument:

``` syntax
Te.exe /rebootStateFile:MyRestartFile.xml
```

TAEF will create the file specified to store its state (which tests have already been executed, any TAEF command or environment options, etc.) and resume from where it left off when it resumes after the restart. TAEF handles re-executing itself once the machine comes up again after the restart.

Note that this option does not work on ARM machines due to the removal of a feature that TAEF depends on to resume the tests after reboot (RunOnce key).

\* So long as you are not using any incompatible execution features (currently [Parallel](parallel.md) and [Test Modes](test-modes.md)).

## <span id="faqs_reboot"></span><span id="FAQS_REBOOT"></span>Frequently Asked Questions


### <span id="rerun_faq"></span><span id="RERUN_FAQ"></span>If I choose Rerun, is there any way I can tell whether the test is being invoked for the first time or after a restart?

TAEF does not provide any functionality for you to achieve this. The intent of the rerun option is to enable you to write tests that may require an indeterminate number of restarts based on the state of the machine (such as running Windows Update to completion). Consider using an [ExecutionGroup](execution-groups.md) and the continue option to break down the tasks into separate test operations that occur in sequence before/after the restart.

### <span id="othertests_faq"></span><span id="OTHERTESTS_FAQ"></span>Which TAEF test types are supported?

This feature is available to native, managed, and script tests.

 

 





