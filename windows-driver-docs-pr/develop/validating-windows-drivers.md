---
title: Validating Windows Drivers
description: Various tools to use to validate that your driver package is compliant with the Windows Drivers rules.
ms.date: 08/12/2024
---

# Validating Windows Drivers

Use the InfVerif, Driver Verifier Driver Isolation Checks, and ApiValidator tools to test your [driver package](../install/driver-packages.md) for compliance with the Windows Drivers requirements described in [Get started developing Windows drivers](get-started-developing-windows-drivers.md).

## InfVerif

[InfVerif](../devtest/infverif.md) is a tool that validates INF syntax and checks that the INF conforms to requirements and restrictions.

Use InfVerif with `/w` to verify that a Windows Driver:

* Meets the **declarative (D)** principle of [DCH Design Principles](dch-principles-best-practices.md)
* Complies with the [driver package isolation](driver-isolation.md) requirement of [Get started developing Windows drivers](get-started-developing-windows-drivers.md)

For more details, see [Running InfVerif from the command line](../devtest/running-infverif-from-the-command-line.md).

InfVerif validates Driver Isolation requirements with the '/w' argument, as shown here:

```inf
infverif.exe /w <INF file> [<INF file>]
```

If InfVerif reports no errors when validating with /w, the INF meets the [Driver Package Isolation](driver-isolation.md) requirement of Windows Drivers.

### Targeting current and earlier versions of Windows

If your INF contains syntax introduced in a recent version of Windows, such as the [INF AddEventProvider Directive](../install/inf-addeventprovider-directive.md) which is available starting in Windows 10 version 1809 and you also want to target previous Windows versions, use [INF decorations](../install/inf-manufacturer-section.md) to mark version-specific INF entries. For sample code showing how to use OS version decorations, see [Combining Platform Extensions with Operating System Versions](../install/combining-platform-extensions-with-operating-system-versions.md).

INF files using OS version decorations may fail InfVerif because Driver Isolation requirements may not be supported on the previous Windows versions. To validate such an INF, you may specify the minimum Windows version where Driver Isolation checks should be applied, using the '/wbuild' argument. For example, an INF file that uses the AddEventProvider directive might use the following to only apply Driver Isolation checks to Windows 10 version 1809 and later:

```inf
infverif.exe /w /wbuild NTAMD64.10.0.0.17763 <INF file> [<INF file>]
```

## Driver Verifier Driver Isolation Checks

To qualify as a Windows Driver, a driver package must meet [Driver Package Isolation](driver-isolation.md) requirements. Starting in Windows 11, [Driver Verifier](../devtest/driver-verifier.md) (DV) can monitor kernel binaries for registry and file system reads and writes that are not allowed for isolated driver packages.

You can either view violations as they happen in a kernel debugger, you can review the violations as reported in the System event log, or you can configure DV to halt the system and generate a memory dump with details when a violation occurs. You might start driver development with the first and second methods, then switch to the second as your driver nears completion.

To enable driver isolation checks so they will be reported via kernel debugger and System event log but not bugcheck the system:

```command
verifier /rc 33 36 /driver myDriver.sys [myDriver2.sys ...]
```

To configure DV to bugcheck when a driver isolation violation occurs, use the following syntax:

```command
verifier /onecheck /rc 33 36 /driver myDriver1.sys [myDriver2.sys ...]
```

Regardless of which monitoring method you choose, you'll need to reboot to enable the verification settings. To do this from the command line, specify:

```command
shutdown /r /t 0
```

Here are a few examples of error messages as seen in the kernel debugger:

Example: **ZwCreateKey** provides full absolute path:

```
DRIVER_ISOLATION_VIOLATION: <driver name>: Registry operations should not use absolute paths. Detected creation of unisolated registry key \Registry\Machine\SYSTEM
```

Example: **ZwCreateKey** provides path relative to a handle that is not from an approved API:

```
DRIVER_ISOLATION_VIOLATION: <driver name>: Registry operations should only use key handles returned from WDF or WDM APIs. Detected creation of unisolated registry key \REGISTRY\MACHINE\SYSTEM\SomeKeyThatShouldNotExist
```

Consider running [Device Fundamentals tests](../devtest/run-devfund-tests-via-the-command-line.md) with DV driver isolation checks enabled on your driver to help catch driver isolation violations early.

> [!NOTE]
> DV does not want to flood users with a deluge of reports of the same violation, so it has a throttling mechanism where it may throttle the reporting of each unique error.  Starting with Windows 11 24H2, in order to make sure you see the full set of Driver Isolation violations for any given run of a test or series of tests, you can request to have the throttling for Driver Isolation violations to be reset using:
>
> verifier /dif 33 /action 1
> 
> If you do not do this before you run a test, then you may not see certain violations during the running of your tests if those violations already occurred before the test was started.

### WHCP compliance

Currently, the [Windows Hardware Compatibility Program (WHCP) program](/windows-hardware/design/compatibility/whcp-specifications-policies) does not mandate full driver package isolation.  However, starting with Windows 11 24H2, the WHCP program starts including driver isolation related requirements. To enable the same level of driver package isolation validation as the [Hardware Lab Kit (HLK)](/windows-hardware/test/hlk/) does as part of enforcing the WHCP requirements, you would use the following syntax:

```command
Verifier /dif 33 /33 whcp /driver myDriver.sys [myDriver2.sys ...]
```

When using this syntax, all driver isolation violations will still be reported, but the ones not currently being enforced for the HLK will be reported as warnings instead of errors.  Ones listed as warnings will not cause HLK failures and will not cause the system to bugcheck if you enable the driver isolation checks with /onecheck to have it generate a bugcheck when a violation occurs.

When viewing events with a kernel debugger, the ones that are considered errors will be prefixed with `DRIVER_ISOLATION_VIOLATION` while the ones that are warnings will be prefixed with `DRIVER_ISOLATION_WARNING`.

When viewing events in the System event log, the events with an `ErrorLevel` attribute of 0 are considered errors and events with another `ErrorLevel` value are not considered errors.  Please see the "Viewing violations in the System event log" section below for more information.

### Viewing violations in the System event log

Driver verifier violations are reported in the System event log from the provider `Microsoft-Windows-Kernel-XDV` and with an event ID of '4'.  On Windows 11 24H2 and later, the events will contain an `ErrorLevel` value.  Events with an `ErrorLevel` value of 0 are considered errors according to the driver isolation mode active (full driver isolation compliance vs WHCP isolation compliance) when the violation was generated. Events with other `ErrorLevel` values are not considered errors.  For example, an event with these attributes would be considered an error:

```
EventData
	RuleId	0x210001
	ErrorMessage	Registry operations should not use absolute paths. Detected opening of unisolated registry key \Registry\Machine\System\CurrentControlSet\Services\ExampleDriver\Parameters
	Module	\SystemRoot\System32\drivers\ExampleDriver.sys
	Irql	0
	ErrorLevel	0x0
```

While an event with these attributes would not be considered an error:

```
EventData
	RuleId	0x210001
	ErrorMessage	Registry operations should only use key handles returned from WDF or WDM APIs. Detected querying of value under unisolated registry key \REGISTRY\MACHINE\SYSTEM\ControlSet001\Control
	Module	\SystemRoot\System32\drivers\ExampleDriver.sys
	Irql	0
	ErrorLevel	0xf4240
```

If you are using the Event Viewer application to view the System event log, you can filter the view of the log using the menu on the right side of the application by clicking "Filter Current Log".  On the dialog that pops up, if you go to the XML tab and edit the query manually, you can use this query to filter the System event log to just DV violations that should be considered an error:

```xml
<QueryList>
  <Query Id="0" Path="System">
    <Select Path="System">*[System/Provider[@Name='Microsoft-Windows-Kernel-XDV'] and System[(EventID='4')] and (EventData/Data[@Name='ErrorLevel']='0')]</Select>
  </Query>
</QueryList>
```

If you want to filter the view of the event log to all DV violations that should be considered an error after a certain time (e.g. after the time that a test pass started), you can do:

```xml
<QueryList>
  <Query Id="0" Path="System">
    <Select Path="System">*[System/Provider[@Name='Microsoft-Windows-Kernel-XDV'] and System[(EventID='4')] and System/TimeCreated[@SystemTime&gt;='2024-01-24T23:00:00.0Z'] and (EventData/Data[@Name='ErrorLevel']='0')]</Select>
  </Query>
</QueryList>
```

Or if you prefer an XML file that you can load up to view, you can use wevtutil to generate such an XML based on the same queries:

```command
wevtutil qe System /q:"*[System/Provider[@Name='Microsoft-Windows-Kernel-XDV'] and System[(EventID='4')] and (EventData/Data[@Name='ErrorLevel']='0')]" /e:Events > DriverVerifierErrors.xml

wevtutil qe System /q:"*[System/Provider[@Name='Microsoft-Windows-Kernel-XDV'] and System[(EventID='4')] and System/TimeCreated[@SystemTime>='2024-01-24T23:00:00.0Z'] and (EventData/Data[@Name='ErrorLevel']='0')]" /e:Events > DriverVerifierErrors.xml
```

### KMDF drivers

When KMDF drivers use WDF APIs to access the registry, such as [WdfRegistryCreateKey](/windows-hardware/drivers/ddi/wdfregistry/nf-wdfregistry-wdfregistrycreatekey), [WdfRegistryOpenKey](/windows-hardware/drivers/ddi/wdfregistry/nf-wdfregistry-wdfregistryopenkey), or [WdfRegistryQueryValue](/windows-hardware/drivers/ddi/wdfregistry/nf-wdfregistry-wdfregistryqueryvalue), the registry access happens via wdf01000.sys instead of the KMDF driver binary directly.  In order to view violations caused by your KMDF driver binary, please enable driver isolation checks on wdf01000.sys in addition to your KMDF driver binary.  Note that when you do this, you will see violations from all KMDF drivers on the system that are using WDF for their registry accesses.

## ApiValidator

The ApiValidator tool verifies that the APIs that your binaries call are valid for a Windows Driver. The tool returns an error if your binaries call an API that is outside the set of valid APIs for Windows Drivers. This tool is part of the WDK for Windows 10.

ApiValidator validates that a driver supports [API Layering](api-layering.md), one of the requirements for Windows Drivers. For a full list of requirements, see [Get started developing Windows drivers](get-started-developing-windows-drivers.md).

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

```command
Apivalidator.exe -DriverPackagePath: <driver folder path> -SupportedApiXmlFiles: (path to XML files containing supported APIs for Windows drivers)
```

For example, to verify the APIs called by the Activity sample in the WDK, first build the sample in Visual Studio. Then open a command prompt and navigate to the directory containing the tool, for example `C:\Program Files (x86\Windows Kits\10\bin\x64`. Enter the following command:

```command
apivalidator.exe -DriverPackagePath:"C:\Program Files (x86)\Windows Kits\10\src\usb\umdf2\_fx2\Debug" -SupportedApiXmlFiles:"c:\Program Files (x86)\Windows Kits\10\build\universalDDIs\x64\UniversalDDIs.xml"
```

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

* ApiValidator does not run on Arm64 because AitStatic does not work on Arm64.
* Arm64 binaries can be tested on x64 machines but not on an x86 machine.
* ApiValidator can run on x86 to test x86 binaries and Arm binaries.
* ApiValidator can run on x64 to test x86, x64, Arm, and Arm64 binaries.
