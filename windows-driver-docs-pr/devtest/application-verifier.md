---
title: Application Verifier - Overview
description: Application Verifier - Overview
keywords:
- verifying drivers (Application Verifier)
- driver verification (Application Verifier)
- Application Verifier
- AppVerif.exe
- user-mode application testing
ms.date: 03/25/2022
---

# Application Verifier - Overview

## Summary

Application Verifier (AppVerifier) is a runtime verification tool for unmanaged code that assists in finding subtle programming errors, security issues and limited user account privilege problems that can be difficult to identify with normal application testing techniques.

## Overview

One of the biggest challenges faced by programmers, software architects, testers, and security consultants is to understand the variable execution paths of their applications when deployed into production. Even with access to source code, it is difficult to grasp everything that will occur during execution due to a variety of dependencies (for example. multiple groups contributing to code or leveraging external components). The Microsoft AppVerifier can play a useful role in helping to manage this complexity and the potential side effects of bugs. The AppVerifier assists in finding programming errors, security issues, and user account privilege problems that can be difficult to identify during a typical test pass.

Application Verifier (AppVerif.exe) is a *dynamic verification* tool for user-mode applications. This tool monitors application actions while the application runs, subjects the application to a variety of stresses and tests, and generates a report about potential errors in application execution or design.

Application Verifier can detect errors in any user-mode applications that are not based on managed code, including user-mode drivers. It finds subtle programming errors that might be difficult to detect during standard application testing or driver testing.

You can use Application Verifier alone or in conjunction with a user-mode debugger. The current user must be a member of the Administrators group on the computer.

## Installing AppVerifier

Application Verifier is included in the [Windows Software Development Kit](https://developer.microsoft.com/windows/downloads/windows-sdk/) (SDK). To install Application Verifier, check the box for it, during installation of the SDK.

:::image type="content" source="images/application-verifier-main-menu.png" alt-text="Screenshot of Application Verifier main menu with a single test app selected and tests listed on the right side.":::

## What Is AppVerifier?

AppVerifier is a tool designed to detect and help debug memory corruptions, critical security vulnerabilities, and limited user account privilege issues. AppVerifier aids in the creation of reliable and secure applications by monitoring an application's interaction with the Microsoft Windows operating system, and profiling its use of objects, the registry, the file system, and Win32 APIs (including heaps, handles, and locks). AppVerifier also includes checks to predict how well the application will perform in non-admin environments.

When used throughout the software development lifecycle, AppVerifier can bring cost benefits to development efforts because it facilitates identifying problems early on when they are easier and cheaper to fix. It also helps to detect errors that may have gone unnoticed and ensures that the final application can be executed in restricted (for example, non-admin) environments.

### Problems That AppVerifier Identifies

AppVerifier helps to determine:

When the application is using APIs correctly:
- Unsafe TerminateThread APIs.
- Correct use of Thread Local Storage (TLS) APIs.
- Correct use of virtual space manipulations (for example, VirtualAlloc, MapViewOfFile).
- Whether the application is hiding access violations using structured exception handling.
- Whether the application is attempting to use invalid handles.
- Whether there are memory corruptions or issues in the heap.
- Whether the application runs out of memory under low resources.
- Whether the correct usage of critical sections is occurring.
- Whether an application running in an administrative environment will run well in an environment with less privilege.
- Whether there are potential problems when the application is running as a limited user.
- Whether there are uninitialized variables in future function calls in a thread's context.

### AppVerifier Tests

AppVerifier consists of sets of tests called "verification layers." These can be turned on or off for each application being tested. By expanding the verification layer within the tests area, the specific tests are displayed. To turn on a test for the application, select the check box next to it. To turn on an entire verification layer, such as Basics, select the check box at the top level.

There are thirteen different types of tests that AppVerifier can perform.

**Basics** - At a minimum, you should run Application Verifier with the Basics setting selected. Each of these will test for an area that will cause crashes or other negative scenarios, that have a direct and significant impact of the customer experience. For more details, see [Application Verifier- Tests within Application Verifier](application-verifier-tests-within-application-verifier.md#basics)

**Compatibility** - Compatibility Verification Layer tests help to identify an application that may have problems with Microsoft Windows operating system. Many of these checks can also be used to test for the logo requirements. For more details, see [Application Verifier- Tests within Application Verifier](application-verifier-tests-within-application-verifier.md#compatibility)

**Cuzz** - The Concurrency Fuzzing (Cuzz) verification layer detects concurrency bugs and data race conditions. Cuzz adjusts thread scheduling by injecting random delays at key points in an application's code. For more details, see [Application Verifier- Tests within Application Verifier](application-verifier-tests-within-application-verifier.md#cuzz)

**Low Resource Simulation** - Low resource simulation tries to simulate an environment under low resources, such as out of memory. This simulation will identify bugs that occur in low memory conditions. This is also referred to as Fault Injection.For more details, see [Application Verifier- Tests within Application Verifier](application-verifier-tests-within-application-verifier.md#low-resource-simulation)

**LuaPriv** - Limited User Account Privilege Predictor (LuaPriv) tests are both Predictive and diagnostic an work to surface issues related to running an application with administrative privilege, and whether that application would work as well if run with less privilege (generally, as a normal user).For more details, see [Application Verifier- Tests within Application Verifier](application-verifier-tests-within-application-verifier.md#luapriv)

**Miscellaneous** - Miscellaneous consists of tests for an assortment of tests such as for dangerous APIs that take unsafe actions.
For more details, see [Application Verifier- Tests within Application Verifier](application-verifier-tests-within-application-verifier.md#miscellaneous)

**Networking** - The networking tests look for improper use of WinSock APIs. For example, if a Networking API called before a successful WSAStartup() or after a balancing successful WSACleanup() call was made. For more details, see [Application Verifier- Tests within Application Verifier](application-verifier-tests-within-application-verifier.md#networking)

**NTLM** - Monitors the use of the authentication APIs AcquireCredentialsHandle and InitializeSecurityContext in order to detect uses of the NTLM protocol. The NTLM is an outdated authentication protocol with flaws that potentially compromise the security of applications and the operating system. For more details, see [Application Verifier- Tests within Application Verifier](application-verifier-tests-within-application-verifier.md#ntlm)

**Printing** - The Print Verifier helps find and troubleshoot issues that may result when an application calls the print subsystem. Print Verifier targets the two layers of the print subsystem, the PrintAPI layer and the PrintDriver layer.
For more details, see [Application Verifier- Tests within Application Verifier](application-verifier-tests-within-application-verifier.md#printing)

**Webservices** - The Windows Webservices API (WWSAPI) Verification Layer works to check for proper use of WWSAPI, such as a WWSAPI being called which references an invalid intrinsic WWSAPI object or WWSAPI being called with references to a single threaded object already in use. For more details, see [Application Verifier- Tests within Application Verifier](application-verifier-tests-within-application-verifier.md#webservices)

**Services** - The services tests, check for the proper use of Windows Services. For example that services are being started and stopped properly. For information on the stop code exceptions generated by these tests, see [Application Verifier - Stop Codes and Definitions](application-verifier-stop-codes-and-definitions.md#services).

**Perf** - The Perf test check for efficient use of APIs that impact system performance and energy consumption, such as calling a Windows function that uses an incorrect wait period. For information on the stop code exceptions generated by these tests, see [Application Verifier - Stop Codes and Definitions](application-verifier-stop-codes-and-definitions.md#perf).

**Hangs** - The Hangs tests for the use of APIs that cause the system to become unresponsive, for example when the DllMain thread is waiting for another thread that was blocked. For information on the stop code exceptions generated by these tests, see [Application Verifier - Stop Codes and Definitions](application-verifier-stop-codes-and-definitions.md#hangs).


## How Does AppVerifier Work?

AppVerifier works by modifying the unmanaged DLLs Method Tables so that the required checks are performed before the real function is executed (this is also called "Function Hooking"). For example, the address of the Win32 API CreateFileA method is replaced with an internal AppVerifier method that will trigger a series of tests that, when positive, will be logged.

When new processes are started, the use of AppVerifier's Method Table Hooking techniques is controlled by entries made in specific registry keys. If the registry entry exists, then the AppVerifier DLL will be loaded in a newly created process that will handle the Method Table replacements in the existent and subsequently loaded DLLs. Because these hooks are made when the DLL is loaded, it is not possible to use AppVerifier on a process that is already running.

The AppVerifier user interface (UI) is used to control the Registry Key settings and to provide information about the existing logs. After the application and tests are set within the UI and the "Save" button is clicked, the Registry settings are made. The application will then need to be restarted, which will start the monitoring. It is important to note that the settings will persist until the application is removed from AppVerifier.

When a problem is identified, a verifier stop will occur. The number provided is used to identify the exact nature and reason for its occurrence.

## Use of Application Verifier in the Software Development Lifecycle

You should use Application Verifier throughout your software development lifecycle. 

*Requirements Phase* - AppVerifier should be planned and time allocated for its execution and follow up.

*Design Phase* - Plan for the use of Application Verifier and define which components (modules, DLLs or EXEs) will be tested.

*Implementation Phase* - Run Application Verifier on stable builds (from Alpha to RTM) of the different components under development (it is important to test the components individually and collectively).

*Verification Phase* - Testers should execute all of their tests (both manual and automatic) with Application Verifier since this will be the first time that the application will be pushed to the limits and unexpected behavior and data will be submitted. AppVerifier is also a powerful tool for security consultants doing audits (black box and white box) since it will allow the quick enumeration of real (or potential) attack/exploit vectors. 

*Release Phase* - Clients and security consultants can use AppVerifier on the released binaries to identify potential security vulnerabilities. 

*Support and Servicing Phase* - Use Application Verifier to ensure that code changes (e.g. updates, service packs) do not introduce regressions.

## Section topics

This section contains the following topics.

[Application Verifier - Features](application-verifier-features.md)

[Application Verifier - Testing Applications](application-verifier-testing-applications.md)
 
[Application Verifier - Tests within Application Verifier](application-verifier-tests-within-application-verifier.md)

[Application Verifier - Stop Codes and Definitions](application-verifier-stop-codes-and-definitions.md)

[Application Verifier - Debugging Application Verifier Stops](application-verifier-debugging-application-verifier-stops.md)
  
[Application Verifier - Frequently Asked Questions](application-verifier-faqs.md)


