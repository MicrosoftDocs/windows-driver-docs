---
ms.assetid: D4B7FC2A-259F-4B72-A52B-03CBF712D5C5
title: Validating Universal Windows drivers
description: You can use the ApiValidator.exe tool to verify that the APIs that your driver calls are valid for a Universal Windows driver.
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Validating Universal Windows drivers

You can use the ApiValidator.exe tool to verify that the APIs that your driver calls are valid for a Universal Windows driver. The tool returns an error if your driver calls an API that is outside the set of valid APIs for Universal Windows drivers. This tool is part of the Windows Driver Kit (WDK) for Windows 10.

## <span id="Running_ApiValidator_in_Visual_Studio"></span><span id="running_apivalidator_in_visual_studio"></span><span id="RUNNING_APIVALIDATOR_IN_VISUAL_STUDIO"></span>Running ApiValidator in Visual Studio


If the **Target Platform** property of your driver project is set to **Universal**, Visual Studio runs ApiValidator automatically as a post-build step.

To view all the messages displayed by ApiValidator, navigate to **Tools &gt; Options &gt; Projects and Solutions &gt; Build and Run**, and set **MSBuild project build output verbosity** to **Detailed**. When building from the command line, add the switch **/v:detailed** or **/v:diag** to your build command to increase the verbosity.

For the umdf2\_fx2 driver sample, API validation errors look this:

``` syntax
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

**Fixing validation errors**

1.  If you switched a legacy desktop driver to universal, verify that you are including the correct libraries. Right click the project and choose properties. Navigate to **Linker-&gt;Input**. The **Additional Dependencies** should contain:

    ```
    %AdditionalDependencies);$(SDK_LIB_PATH)\OneCoreUAP.lib
    ```

2.  Remove or replace the non-universal API calls one at a time and rerun the tool until there are no errors.

## <span id="Running_ApiValidator_from_the_Command_Prompt"></span><span id="running_apivalidator_from_the_command_prompt"></span><span id="RUNNING_APIVALIDATOR_FROM_THE_COMMAND_PROMPT"></span>Running ApiValidator from the Command Prompt


You can also run Apivalidator.exe from the command prompt. In your WDK installation, navigate to C:\\Program Files (x86)\\Windows Kits\\10\\bin\\*&lt;arch&gt;*.

Use the following syntax:

**Apivalidator.exe** **-DriverPackagePath:***&lt;driver folder path&gt;* **-SupportedApiXmlFiles:***&lt;path to XML files containing supported APIs for universal drivers&gt;*

For example, to verify the APIs called by the Activity sample in the WDK, first build the sample in Visual Studio. Then open a command prompt and navigate to the directory containing the tool, for example C:\\Program Files (x86)\\Windows Kits\\10\\bin\\x64. Enter the following command:

**apivalidator.exe -DriverPackagePath:"C:\\Program Files (x86)\\Windows Kits\\10\\src\\usb\\umdf2\_fx2\\Debug\\\\" -SupportedApiXmlFiles:"c:\\Program Files (x86)\\Windows Kits\\10\\build\\universalDDIs\\x64\\UniversalDDIs.xml"**

The command produces the following output:

``` syntax
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

``` syntax
Error      1              error : AitStatic output file has incorrect format or analysis run on incorrect file types.     C:\Program Files (x86)\Windows Kits\10\src\usb\umdf2_fx2\driver\ApiValidator.exe            osrusbfx2um
```

Use this workaround:

1.  Open Project properties, navigate to **General**, and rename **Output Directory** to the following:

    ``` syntax
    $(SolutionDir)$(Platform)\$(ConfigurationName)\
    ```

2.  Rebuild the solution.

 

 





