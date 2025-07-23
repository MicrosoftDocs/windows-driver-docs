---
title: Application Verifier - Overview
description: Explore the Application Verifier (AppVerifier) runtime verification tool and look for programming errors, security issues, and user privilege problems in unmanaged code.
keywords:
- verifying drivers (Application Verifier)
- driver verification (Application Verifier)
- Application Verifier
- AppVerif.exe
- user-mode application testing
ms.date: 07/11/2025
ms.topic: concept-article
---

# Application Verifier

Application Verifier (AppVerifier) is a runtime verification tool for unmanaged code. The tool is helpful for finding issues that can be difficult to identify with standard application testing or driver testing techniques. AppVerifier can assist with locating subtle programming errors, security issues, and limited user account privilege problems.

## Overview of AppVerifier

One of the most significant challenges for programmers, software architects, testers, and security consultants, is understanding the variable execution paths of applications when they're deployed into production. Even with access to source code, it can be difficult to grasp everything that can occur during execution. Various dependencies like multiple groups contributing to code or exercising external components can increase the complexity for troubleshooting.

AppVerifier (_AppVerif.exe_) is a dynamic verification tool for user-mode applications. It can detect errors in any user-mode application that isn't based on managed code, including user-mode drivers. The tool monitors application actions while the application runs. It subjects the application to various stresses and tests, and generates a report about potential errors in application execution or design.

When used throughout the software development lifecycle, AppVerifier can bring cost benefits to development efforts. It facilitates identifying problems early on when they're easier and cheaper to fix. The tool also helps to detect errors that were previously unnoticed. It ensures the final application can be executed in restricted (for example, nonadmin) environments.

## AppVerifier installation and requirements

AppVerifier is included in the [Windows Software Development Kit (SDK)](https://developer.microsoft.com/windows/downloads/windows-sdk/). To install Application Verifier, select the checkbox for the tool during installation of the SDK.

:::image type="content" source="images/application-verifier-main-menu.png" alt-text="Screenshot of the Application Verifier main menu with a single test app selected and tests listed on the right side.":::

To use AppVerifier, review the following conditions and requirements:

- You can use AppVerifier alone or with a user-mode debugger.

- The current user must be a member of the Administrators group on the computer.

- AppVerifier doesn't support ARM64EC.

## Data you can check with AppVerifier

AppVerifier is a tool designed to detect and help debug memory corruptions, critical security vulnerabilities, and limited user account privilege issues. AppVerifier aids in the creation of reliable and secure applications by monitoring an application's interaction with the Microsoft Windows operating system. It profiles the operating system's use of objects, the registry, the file system, and Win32 APIs (including heaps, handles, and locks). AppVerifier also includes checks to predict how well the application can perform in nonadmin environments.

## Problems you can investigate with AppVerifier

AppVerifier helps determine when an application is using APIs correctly. The tool can check for the following issues in your application:

- Unsafe TerminateThread APIs
- Incorrect use of Thread Local Storage (TLS) APIs
- Incorrect use of virtual space manipulations (for example, VirtualAlloc, MapViewOfFile)
- Application hides access violations by using structured exception handling
- Application attempts to use invalid handles
- Memory corruptions or issues in the heap
- Application runs out of memory under low resources
- Incorrect use of critical sections
- Application running in an administrative environment can't run in an environment with reduced privileges
- Application running as a limited user might cause potential problems
- Uninitialized variables in future function calls in a thread's context

## Tests you can run with AppVerifier

AppVerifier consists of sets of tests called "verification layers." The layers can be turned on or off for each application you check.

- To view the specific tests, expand the verification layer within the set.

- To turn on a test for the application, select the checkbox for the test.

- To turn on all the tests in a verification layer, such as **Basics**, select the checkbox at the top level.

The following table lists the 13 test types AppVerifier can perform and provides links to articles for more information.

| Test type | Description | More information |
|-----------|-------------|------------------|
| **Basics** | At a minimum, you should run Application Verifier with the **Basics** setting selected. Each basic test checks an area that can cause crashes or other negative scenarios that have a direct and significant effect on the customer experience. | [Application Verifier - Tests within Application Verifier (Basics)](application-verifier-tests-within-application-verifier.md#basics) |
| **Compatibility** | Compatibility Verification Layer tests help to identify an application that might have problems with the Microsoft Windows operating system. Many of these checks can also be used to test for the logo requirements. | [Application Verifier - Tests within Application Verifier (Compatibility)](application-verifier-tests-within-application-verifier.md#compatibility) |
| **Cuzz** | The Concurrency Fuzzing (Cuzz) verification layer detects concurrency bugs and data race conditions. Cuzz adjusts thread scheduling by injecting random delays at key points in the application code. | [Application Verifier - Tests within Application Verifier (Cuzz)](application-verifier-tests-within-application-verifier.md#cuzz) |
| **Low Resource Simulation** | Low resource simulation tries to simulate an environment under low resources, such as out of memory. This simulation identifies bugs that occur in low memory conditions. This test is also referred to as _Fault Injection_. | [Application Verifier - Tests within Application Verifier (Low Resource Simulation)](application-verifier-tests-within-application-verifier.md#low-resource-simulation) |
| **LuaPriv** | Limited User Account Privilege Predictor (LuaPriv) tests are both predictive and diagnostic, and work to surface issues related to running an application with administrative privilege. The tests also reveal whether the application can work if you run the app with reduced privilege (generally, as a general user). | [Application Verifier - Tests within Application Verifier (LuaPriv)](application-verifier-tests-within-application-verifier.md#luapriv) |
| **Miscellaneous** | Miscellaneous tests check for an assortment of conditions, such as detecting dangerous APIs that execute unsafe actions. | [Application Verifier - Tests within Application Verifier (Miscellaneous)](application-verifier-tests-within-application-verifier.md#miscellaneous) |
| **Networking** | The networking tests look for improper use of WinSock APIs. For example, if a Networking API calls before a successful call to the `WSAStartup()` method, or after a balancing successful call to the `WSACleanup()` method. | [Application Verifier - Tests within Application Verifier (Networking)](application-verifier-tests-within-application-verifier.md#networking) |
| **NTLM** | Monitors the use of the authentication APIs `AcquireCredentialsHandle` and `InitializeSecurityContext` to detect uses of the NT LAN Manager (NTLM) protocol. The NTLM is an outdated authentication protocol with flaws that potentially compromise the security of applications and the operating system. | [Application Verifier - Tests within Application Verifier (NTLM)](application-verifier-tests-within-application-verifier.md#ntlm) |
| **Printing** | The Print Verifier helps find and troubleshoot issues that can result when an application calls the print subsystem. Print Verifier targets the two layers of the print subsystem, the PrintAPI layer and the PrintDriver layer. | [Application Verifier - Tests within Application Verifier (Printing)](application-verifier-tests-within-application-verifier.md#printing) |
| **Webservices** | The Windows Webservices API (WWSAPI) Verification Layer checks for proper use of WWSAPI, such as a WWSAPI call that references an invalid intrinsic WWSAPI object, or a WWSAPI call with references to a single-threaded object already in use. | [Application Verifier - Tests within Application Verifier (WebServices)](application-verifier-tests-within-application-verifier.md#webservices) |
| **Services** | The services tests check for the proper use of Windows Services. For example, the test verifies whether services start and stop properly. | [Application Verifier - Stop Codes - Services](application-verifier-stop-codes-services.md) |
| **Perf** | The Perf test checks for efficient use of APIs that affect system performance and energy consumption, such as calling a Windows function that uses an incorrect wait period. | [Application Verifier - Stop Codes - Perf](application-verifier-stop-codes-perf.md) |
| **Hangs** | The Hangs test checks for the use of APIs that cause the system to become unresponsive. For example, when the DllMain thread is waiting for another thread that is blocked. | [Application Verifier - Stop Codes - Hangs](application-verifier-stop-codes-hangs.md) |

## How AppVerifier works

AppVerifier works by modifying the unmanaged DLLs Method Tables so the required checks are performed before the real function is executed (this approach is also called "Function Hooking"). For example, the address of the Win32 API `CreateFileA` method is replaced with an internal AppVerifier method that triggers a series of tests that, when positive, are logged.

When new processes start, control of the AppVerifier Method Table Hooking techniques is accomplished with entries in specific registry keys. If the registry entry exists, the AppVerifier DLL is loaded in a newly created process that handles the Method Table replacements in existent DLLs and DLLs loaded later. Because the hooks are made when the DLL is loaded, it isn't possible to use AppVerifier on a currently running process.

The AppVerifier user interface (UI) is used to control the Registry Key settings and provide information about the existing logs. After the application and tests are set within the UI and you select **Save**, the Registry settings are configured. You then restart the application, which initiates the monitoring. Keep in mind that the settings persist until the application is removed from AppVerifier.

When AppVerifier identifies a problem, a verifier _stop_ occurs. The tool provides a number that identifies the exact nature and reason for the halt in execution.

## AppVerifier and the Software Development Lifecycle

It's a good practice to use Application Verifier throughout your software development lifecycle. Here are some suggestions:

- **Requirements Phase**: Plan to use AppVerifier to help determine app requirements. Allocate time for running the tool and following up on identified issues.

- **Design Phase**: Plan to use AppVerifier as you design your app. Define which components (modules, DLLs, or EXEs) to test.

- **Implementation Phase**: Run AppVerifier on stable builds (from Alpha to RTM) of the different components under development. Test the components individually and collectively.

- **Verification Phase**: Test engineers should run all tests (both manual and automatic) with AppVerifier for the initial verification. This phase in the cycle is the first time the app is pushed to the limits. Unexpected behavior and data are commonly discovered during initial verification. AppVerifier is also a powerful tool for security consultants running audits (black box and white box). The tool allows the quick enumeration of real (or potential) attack/exploit vectors. 

- **Release Phase**: Clients and security consultants can use AppVerifier on the released binaries to identify potential security vulnerabilities. 

- **Support and Servicing Phase**: Use AppVerifier to ensure code changes like updates and service packs don't introduce regressions.

## Related articles about AppVerifier

This section includes:

- [Application Verifier - Features](application-verifier-features.md)

- [Application Verifier - Testing applications](application-verifier-testing-applications.md)
 
- [Application Verifier - Tests within Application Verifier](application-verifier-tests-within-application-verifier.md)

- [Application Verifier - Stop codes and definitions](application-verifier-stop-codes-and-definitions.md)

- [Application Verifier - Debugging application verifier stops](application-verifier-debugging-application-verifier-stops.md)
  
- [Application Verifier - Frequently Asked Questions](application-verifier-faqs.md)