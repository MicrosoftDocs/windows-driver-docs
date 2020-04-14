---
ms.assetid: D4B7FC2A-259F-4B72-A52B-03CBF712D5C5
title: Validating Universal Windows drivers
description: You can use the ApiValidator.exe tool to verify that the APIs that your driver calls are valid for a Universal Windows driver.
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Validating Windows Drivers

## InfVerif

[InfVerif](https://docs.microsoft.com/windows-hardware/drivers/devtest/infverif) is a tool for statically analyzing INF files that ships with the Windows Driver Kit (WDK).  It performs syntax valiation on the INF file and checks that the INF conforms to certain requirements and restrictions.

InfVerif can run in multiple modes with different levels of validation strictness.

If you are developing a *Windows Driver*:

Use **infverif /w** to determine compatability with the **declarative (D)** requirement for Windows Drivers.  Additionally, this flag will determine if your driver's INF file is properly isolated according to [driver package isolation](https://docs.microsoft.com/windows-hardware/drivers/develop/driver-isolation) requirements. This switch is present in all kits for Windows 10 Version 1809 and later.

The **“/v”** argument will run InfVerif in verbose mode. An example of using InfVerif is:

```infverif.exe /v /w test.inf
Running in Verbose
Running Windows Core INF check

Validating test.inf
INF is VALID
Checked 1 INF(s) in 0 m 0 s 2 ms
```

InfVerif also supports parsing multiple INF files at a time by passing multiple filenames on the command line or using a wildcard:

```infverif.exe /w test1.inf test2.inf
infverif.exe /w test*.inf
```

## ApiValidator

[ApiValidator](https://docs.microsoft.com/windows-hardware/test/hlk/testref/df4a9671-c2aa-4c81-b964-7247fb4799df) is a tool to verify that the APIs that your binaries call are valid for a Windows Driver. The tool returns an error if your binaries call an API that is outside the set of valid APIs for Windows Drivers. This tool is part of the WDK for Windows 10.

ApiValidator is critical while developing Windows Drivers as it helps validate that your driver is following the proper [API Layering](https://review.docs.microsoft.com/en-us/windows-hardware/drivers/develop/api-layering) requirements for Windows Drivers.

### <span id="Running_ApiValidator_in_Visual_Studio"></span><span id="running_apivalidator_in_visual_studio"></span><span id="RUNNING_APIVALIDATOR_IN_VISUAL_STUDIO"></span>Running ApiValidator in Visual Studio

If the **Target Platform** property of your driver project is set to **Windows Driver**, Visual Studio runs ApiValidator automatically as a post-build step.

To view all the messages displayed by ApiValidator, navigate to **Tools &gt; Options &gt; Projects and Solutions &gt; Build and Run**, and set **MSBuild project build output verbosity** to **Detailed**. When building from the command line, add the switch **/v:detailed** or **/v:diag** to your build command to increase the verbosity.

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

1.  If you switched a legacy desktop UMDF driver project to Windows Driver, verify that you are including the correct libraries when building your binaries. Right click the project and choose properties. Navigate to **Linker-&gt;Input**. The **Additional Dependencies** should contain:

    ```cpp
    %AdditionalDependencies);$(SDK_LIB_PATH)\OneCoreUAP.lib
    ```

    To review other linker options for targeting OneCore SKUs, see [Building for OneCore](building-for-onecore.md).

2.  Remove or replace API calls that are not permitted one at a time and rerun the tool until there are no errors.

3.  In some cases, you can replace these calls with alternate DDIs that are listed on the reference pages for the desktop-only DDI. If you cannot find a suitable replacement, please [submit feedback](https://go.microsoft.com/fwlink/p/?linkid=529549).  You may have to code a workaround if there is not a suitable replacement.  If you need to, write a new Windows Driver starting from the driver templates in the WDK.

If you see errors like the following, please refer to the guidance in [Building for OneCore](building-for-onecore.md).

```cpp
ApiValidation: Error: FlexLinkTest.exe has a dependency on 'wtsapi32.dll!WTSEnumerateSessionsW' but is missing: IsApiSetImplemented("ext-ms-win-session-wtsapi32-l1-1-0")
ApiValidation: Error: FlexLinkTest.exe has a dependency on 'wtsapi32.dll!WTSFreeMemory' but is missing: IsApiSetImplemented("ext-ms-win-session-wtsapi32-l1-1-0")
ApiValidation: NOT all binaries are Universal
```

### Running ApiValidator from the Command Prompt

Running ApiValidator from the Command Prompt
You can also run Apivalidator.exe from the command prompt. In your WDK installation, navigate to **C:\Program Files (x86)\Windows Kits\10\bin\<arch>** and **C:\Program Files (x86)\Windows Kits\10\build\universalDDIs\<arch>**. 

**Important Notes:**
* ApiValidator requires the following binaries in order to run successfully: ApiValidator.exe, Aitstatic.exe, Microsoft.Kits.Drivers.ApiValidator.dll, and UniversalDDIs.xml. 
* The UniversalDDIs.xml must match binary architecture being validated, example: x64 drivers use the x64 UniversalDDI.xml
* ApiValidator only tests one architecture at a time
* See Known ApiValidator issues below for additional info

Use the following syntax:

**Apivalidator.exe** **-DriverPackagePath:**_&lt;driver folder path&gt;_  
 **-SupportedApiXmlFiles:**_&lt;path to XML files containing supported APIs for Windows drivers&gt;_

For example, to verify the APIs called by the Activity sample in the WDK, first build the sample in Visual Studio. Then open a command prompt and navigate to the directory containing the tool, for example C:\\Program Files (x86)\\Windows Kits\\10\\bin\\x64. Enter the following command:

**apivalidator.exe -DriverPackagePath:"C:\\Program Files (x86)\\Windows Kits\\10\\src\\usb\\umdf2\_fx2\\Debug\\\\" -SupportedApiXmlFiles:"c:\\Program Files (x86)\\Windows Kits\\10\\build\\universalDDIs\\x64\\UniversalDDIs.xml"**

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

The XML files that enumerate the valid APIs for Windows Drivers are located in C:\\Program Files (x86)\\Windows Kits\\10\\build\\universalDDIs\\*&lt;arch&gt;*.

### <span id="Troubleshooting ApiValidator"></span><span id="troubleshooting"></span><span id="TROUBLESHOOTING"></span>Troubleshooting ApiValidator


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



