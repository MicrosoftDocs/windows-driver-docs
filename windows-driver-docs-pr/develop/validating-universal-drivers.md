---
ms.assetid: D4B7FC2A-259F-4B72-A52B-03CBF712D5C5
title: Validating Universal Windows drivers
description: You can use the ApiValidator.exe tool to verify that the APIs that your driver calls are valid for a Universal Windows driver.
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Validating Universal Windows drivers

You can use the ApiValidator.exe tool to verify that the APIs that your binaries call are valid for a Universal Windows driver. The tool returns an error if your binaries call an API that is outside the set of valid APIs for Universal Windows drivers. This tool is part of the Windows Driver Kit (WDK) for Windows 10.

## <span id="Running_ApiValidator_in_Visual_Studio"></span><span id="running_apivalidator_in_visual_studio"></span><span id="RUNNING_APIVALIDATOR_IN_VISUAL_STUDIO"></span>Running ApiValidator in Visual Studio


If the **Target Platform** property of your driver project is set to **Universal**, Visual Studio runs ApiValidator automatically as a post-build step.

To view all the messages displayed by ApiValidator, navigate to **Tools &gt; Options &gt; Projects and Solutions &gt; Build and Run**, and set **MSBuild project build output verbosity** to **Detailed**. When building from the command line, add the switch **/v:detailed** or **/v:diag** to your build command to increase the verbosity.

For the umdf2\_fx2 driver sample, API validation errors look this:

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

## Fixing validation errors

1.  If you switched a legacy desktop UMDF driver project to universal, verify that you are including the correct libraries when building your binaries. Right click the project and choose properties. Navigate to **Linker-&gt;Input**. The **Additional Dependencies** should contain:

    ```cpp
    %AdditionalDependencies);$(SDK_LIB_PATH)\OneCoreUAP.lib
    ```

    To review other linker options for targeting OneCore SKUs, see [Building for OneCore](building-for-onecore.md).

2.  Remove or replace the non-universal API calls one at a time and rerun the tool until there are no errors.

3.  In some cases, you can replace these calls with alternate DDIs that are listed on the reference pages for the desktop-only DDI. If you cannot find a suitable replacement, please [submit feedback](http://go.microsoft.com/fwlink/p/?linkid=529549).  You may have to code a workaround if there is not a suitable replacement.  If you need to, write a new Universal Windows driver starting from the driver templates in the WDK.

If you see errors like the following, please refer to the guidance in [Building for OneCore](building-for-onecore.md).

```cpp
ApiValidation: Error: FlexLinkTest.exe has a dependency on 'wtsapi32.dll!WTSEnumerateSessionsW' but is missing: IsApiSetImplemented("ext-ms-win-session-wtsapi32-l1-1-0")
ApiValidation: Error: FlexLinkTest.exe has a dependency on 'wtsapi32.dll!WTSFreeMemory' but is missing: IsApiSetImplemented("ext-ms-win-session-wtsapi32-l1-1-0")
ApiValidation: NOT all binaries are Universal
```

## Running ApiValidator from the Command Prompt

You can also run Apivalidator.exe from the command prompt. In your WDK installation, navigate to C:\\Program Files (x86)\\Windows Kits\\10\\bin\\*&lt;arch&gt;*.

Use the following syntax:

**Apivalidator.exe** **-DriverPackagePath:***&lt;driver folder path&gt;* **-SupportedApiXmlFiles:***&lt;path to XML files containing supported APIs for universal drivers&gt;*

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

The XML files that enumerate the valid APIs for Universal Windows drivers are located in C:\\Program Files (x86)\\Windows Kits\\10\\build\\universalDDIs\\*&lt;arch&gt;*.

## <span id="Troubleshooting"></span><span id="troubleshooting"></span><span id="TROUBLESHOOTING"></span>Troubleshooting


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

 

 





