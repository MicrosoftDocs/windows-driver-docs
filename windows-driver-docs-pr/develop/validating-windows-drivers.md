---
title: Validating Universal Windows drivers
description: You can use the ApiValidator.exe tool to verify that the APIs that your driver calls are valid for a Universal Windows driver.
ms.date: 04/28/2020
---

# Validating Windows Drivers

Use the InfVerif, Driver Verifier Driver Isolation Checks, and ApiValidator tools to test your Windows Driver for compliance with the requirements described in [Getting Started with Windows Drivers](getting-started-with-windows-drivers.md).

## InfVerif

[InfVerif](../devtest/infverif.md) is a tool that validates INF syntax and checks that the INF conforms to requirements and restrictions.

Use InfVerif with `/w` and `/v` to verify that a Windows Driver:

* Meets the **declarative (D)** principle of [DCH Design Principles](dch-principles-best-practices.md)
* Complies with the [driver package isolation](driver-isolation.md) requirement of [Getting Started with Windows Drivers](getting-started-with-windows-drivers.md)

For more details, see [Running InfVerif from the command line](../devtest/running-infverif-from-the-command-line.md).

### Targeting current and earlier versions of Windows

Each run of InfVerif tests a single ruleset, for example `/w` (Windows driver compatibility) or `/k` (Hardware Dev Center submission).  If your INF contains syntax introduced in a more recent version of Windows and you also want to target previous Windows versions, use [INF decorations](../install/inf-manufacturer-section.md) to mark version-specific INF entries and then run InfVerif multiple times, for example:

```inf
infverif /k <INF file>
infverif /w NTAMD64.10.0.0.<build number where w is a requirement> <INF file>
```

If there are no errors, the INF meets the [Driver Package Isolation](driver-isolation.md) requirement of Windows Drivers.

For example, the [INF AddEventProvider Directive](../install/inf-addeventprovider-directive.md) is available starting in Windows 10, version 1809. To use this directive in an INF targeting an OS version before Windows 10, version 1809, decorate both the install section using legacy INF syntax for registering ETW event providers as well as the install section using the updated syntax.

For sample code showing how to use OS decorations, see [Combining Platform Extensions with Operating System Versions](../install/combining-platform-extensions-with-operating-system-versions.md).

## Driver Verifier Driver Isolation Checks

To qualify as a Windows Driver, a driver must meet [Driver Package Isolation](driver-isolation.md) requirements. Starting in Windows 10 Preview Build 19568, [Driver Verifier](../devtest/driver-verifier.md) (DV) monitors registry reads and writes that are not allowed for isolated driver packages.

You can either view violations as they happen in a kernel debugger, or you can configure DV to halt the system and generates a memory dump with details when a violation occurs. You might start driver development with the first method, then switch to the second as your driver nears completion.

To view violations as they occur, first connect a kernel debugger and then use the following commands. After a reboot has enabled the DV settings, you can monitor violations in kernel debugger output.

To enable driver isolation checks on a single driver:

```command
verifier /rc 33 36 /driver myDriver.sys
```

To check more than one driver, separate each driver name with a space:

```command
verifier /rc 33 36 /driver myDriver1.sys myDriver2.sys
```

To configure DV to bugcheck when a violation occurs, use the following syntax:

```
verifier /onecheck /rc 33 36 /driver myDriver1.sys
```

You'll need to reboot to enable the verification settings. To do this from the command line, specify:

```command
shutdown /r /t 0
```

Here are a few examples of error messages:

Example: **ZwCreateKey** provides full absolute path:

`DRIVER_ISOLATION_VIOLATION: <driver name>: Registry operations should not use absolute paths. Detected creation of unisolated registry key \Registry\Machine\SYSTEM`

Example: **ZwCreateKey** provides path relative to a handle that is not from an approved API:

`DRIVER_ISOLATION_VIOLATION: <driver name>: Registry operations should only use key handles returned from WDF or WDM APIs. Detected creation of unisolated registry key \REGISTRY\MACHINE\SYSTEM\SomeKeyThatShouldNotExist`

Consider enabling [Device Fundamentals tests](../devtest/run-devfund-tests-via-the-command-line.md) with DV driver isolation checks to help catch driver isolation violations early.

## ApiValidator

The ApiValidator tool verifies that the APIs that your binaries call are valid for a Windows Driver. The tool returns an error if your binaries call an API that is outside the set of valid APIs for Windows Drivers. This tool is part of the WDK for Windows 10.

ApiValidator validates that a driver supports [API Layering](api-layering.md), one of the requirements for Windows Drivers. For a full list of requirements, see [Getting Started with Windows Drivers](getting-started-with-windows-drivers.md).

### Running ApiValidator in Visual Studio

If the **Target Platform** property of your driver project is set to **Windows Driver**, Visual Studio runs ApiValidator automatically as a post-build step.

To view all the messages displayed by ApiValidator, navigate to **Tools->Options->Projects and Solutions->Build and Run**, and set **MSBuild project build output verbosity** to **Detailed**. When building from the command line, add the switch **/v:detailed** or **/v:diag** to your build command to increase the verbosity.

For the umdf2_fx2 driver sample, API validation errors look this:

```cpp
Warning  1   warning : API DecodePointer in kernel32.dll is not supported. osrusbfx2um.dll calls this API.   C:\Program Files (x86)\Windows Kits\10\src\usb\umdf2_fx2\driver\ApiValidator.exe    osrusbfx2um
Warning 2   warning : API DisableThreadLibraryCalls in kernel32.dll is not supported. osrusbfx2um.dll calls this API.   C:\Program Files (x86)\Windows Kits\10\src\usb\umdf2_fx2\driver\ApiValidator.exe    osrusbfx2um
Warning 3   warning : API EncodePointer in kernel32.dll is not supported. osrusbfx2um.dll calls this API.   C:\Program Files (x86)\Windows Kits\10\src\usb\umdf2_fx2\driver\ApiValidator.exe    osrusbfx2um
Warning 4   warning : API GetCurrentProcessId in kernel32.dll is not supported. osrusbfx2um.dll calls this API. C:\Program Files (x86)\Windows Kits\10\src\usb\umdf2_fx2\driver\ApiValidator.exe    osrusbfx2um
Warning 5   warning : API GetCurrentThreadId in kernel32.dll is not supported. osrusbfx2um.dll calls this API.  C:\Program Files (x86)\Windows Kits\10\src\usb\umdf2_fx2\driver\ApiValidator.exe    osrusbfx2um
Warning 6   warning : API GetSystemTimeAsFileTime in kernel32.dll is not supported. osrusbfx2um.dll calls this API. C:\Program Files (x86)\Windows Kits\10\src\usb\umdf2_fx2\driver\ApiValidator.exe    osrusbfx2um
Warning 7   warning : API IsDebuggerPresent in kernel32.dll is not supported. osrusbfx2um.dll calls this API.   C:\Program Files (x86)\Windows Kits\10\src\usb\umdf2_fx2\driver\ApiValidator.exe    osrusbfx2um
Warning 8   warning : API IsProcessorFeaturePresent in kernel32.dll is not supported. osrusbfx2um.dll calls this API.   C:\Program Files (x86)\Windows Kits\10\src\usb\umdf2_fx2\driver\ApiValidator.exe    osrusbfx2um
Warning 9   warning : API QueryPerformanceCounter in kernel32.dll is not supported. osrusbfx2um.dll calls this API. C:\Program Files (x86)\Windows Kits\10\src\usb\umdf2_fx2\driver\ApiValidator.exe    osrusbfx2um
Error   10  error MSB3721: The command ""C:\Program Files (x86)\Windows Kits\10\bin\x64\ApiValidator.exe" -DriverPackagePath:"C:\Program Files (x86)\Windows Kits\10\src\usb\umdf2_fx2\Debug\\" -SupportedApiXmlFiles:"C:\Program Files (x86)\Windows Kits\10\build\universalDDIs\x86\UniversalDDIs.xml" -ApiExtractorExePath:"C:\Program Files (x86)\Windows Kits\10\bin\x64"" exited with code -1.    C:\Program Files (x86)\Windows Kits\10\build\WindowsDriver.common.targets   1531    5   osrusbfx2um
```

### Fixing validation errors

1.  If you switched a legacy desktop UMDF driver project to Windows Driver, verify that you are including the correct libraries when building your binaries. Select and hold (or right-click) the project and choose properties. Navigate to **Linker->Input**. The **Additional Dependencies** should contain:

    ```cpp
    %AdditionalDependencies);$(SDK_LIB_PATH)\OneCoreUAP.lib
    ```

    To review other linker options for targeting OneCore SKUs, see [Building for OneCore](building-for-onecore.md).

2.  Remove or replace API calls that are not permitted one at a time and rerun the tool until there are no errors.

3.  In some cases, you can replace these calls with alternate DDIs that are listed on the reference pages for the desktop-only DDI. You may have to code a workaround if there is not a suitable replacement.  If you need to, write a new Windows Driver starting from the driver templates in the WDK.

If you see errors like the following, please refer to the guidance in [Building for OneCore](building-for-onecore.md).

```cpp
ApiValidation: Error: FlexLinkTest.exe has a dependency on 'wtsapi32.dll!WTSEnumerateSessionsW' but is missing: IsApiSetImplemented("ext-ms-win-session-wtsapi32-l1-1-0")
ApiValidation: Error: FlexLinkTest.exe has a dependency on 'wtsapi32.dll!WTSFreeMemory' but is missing: IsApiSetImplemented("ext-ms-win-session-wtsapi32-l1-1-0")
ApiValidation: NOT all binaries are Universal
```

### Running ApiValidator from the Command Prompt

You can also run Apivalidator.exe from the command prompt. In your WDK installation, navigate to **C:\Program Files (x86)\Windows Kits\10\bin\<arch>** and **C:\Program Files (x86)\Windows Kits\10\build\universalDDIs\<arch>**.

**Important Notes:**
* ApiValidator requires the following files: ApiValidator.exe, Aitstatic.exe, Microsoft.Kits.Drivers.ApiValidator.dll, and UniversalDDIs.xml.
* The UniversalDDIs.xml must match the binary architecture being validated, for example for an x64 driver use the x64 UniversalDDI.xml
* ApiValidator only tests one architecture at a time
* See Known ApiValidator issues below for additional info

Use the following syntax:

`Apivalidator.exe -DriverPackagePath: <driver folder path> -SupportedApiXmlFiles: (path to XML files containing supported APIs for Windows drivers)`

For example, to verify the APIs called by the Activity sample in the WDK, first build the sample in Visual Studio. Then open a command prompt and navigate to the directory containing the tool, for example `C:\Program Files (x86\Windows Kits\10\bin\x64`. Enter the following command:

`apivalidator.exe -DriverPackagePath:"C:\Program Files (x86)\Windows Kits\10\src\usb\umdf2\_fx2\Debug" -SupportedApiXmlFiles:"c:\Program Files (x86)\Windows Kits\10\build\universalDDIs\x64\UniversalDDIs.xml"`

The command produces the following output:

```cpp
ApiValidator.exe: Warning: API DecodePointer in kernel32.dll is not supported. osrusbfx2um.dll calls this API.
ApiValidator.exe: Warning: API DisableThreadLibraryCalls in kernel32.dll is not supported. osrusbfx2um.dll calls this API.
ApiValidator.exe: Warning: API EncodePointer in kernel32.dll is not supported. osrusbfx2um.dll calls this API.
ApiValidator.exe: Warning: API GetCurrentProcessId in kernel32.dll is not supported. osrusbfx2um.dll calls this API.
ApiValidator.exe: Warning: API GetCurrentThreadId in kernel32.dll is not supported. osrusbfx2um.dll calls this API.
ApiValidator.exe: Warning: API GetSystemTimeAsFileTime in kernel32.dll is not supported. osrusbfx2um.dll calls this API.
ApiValidator.exe: Warning: API IsDebuggerPresent in kernel32.dll is not supported. osrusbfx2um.dll calls this API.
ApiValidator.exe: Warning: API IsProcessorFeaturePresent in kernel32.dll is not supported. osrusbfx2um.dll calls this API.
ApiValidator.exe: Warning: API QueryPerformanceCounter in kernel32.dll is not supported. osrusbfx2um.dll calls this API.

ApiValidator.exe Driver located at C:\Program Files (x86)\Windows Kits\10\src\usb\umdf2_fx2\Debug is NOT a Universal Driver
```

### Troubleshooting ApiValidator


If ApiValidator.exe outputs an incorrect format error such as the following:

```cpp
Error      1              error : AitStatic output file has incorrect format or analysis run on incorrect file types.     C:\Program Files (x86)\Windows Kits\10\src\usb\umdf2_fx2\driver\ApiValidator.exe            osrusbfx2um
```

Use this workaround:

1.  Open Project properties, navigate to **General**, and rename **Output Directory** to the following:

    ```cpp
    $(SolutionDir)$(Platform)\$(ConfigurationName)\
    ```

2.  Rebuild the solution.

### Known ApiValidator Issues

* ApiValidator does not run on ARM64 because AitStatic does not work on ARM64.
* ARM64 binaries can be tested on x64 machines but not on an x86 machine.
* ApiValidator can run on x86 to test x86 binaries and ARM binaries.
* ApiValidator can run on x64 to test x86, x64, ARM, and ARM64 binaries.



