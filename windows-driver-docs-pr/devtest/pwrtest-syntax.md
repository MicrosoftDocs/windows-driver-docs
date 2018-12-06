---
title: PwrTest Syntax
description: You run PwrTest from a Command Prompt window. You can select and configure PwrTest Scenarios using command options.
ms.assetid: bcae1bb6-ce5b-4ece-a5ba-bae6fefd6408
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# PwrTest Syntax


You run PwrTest from a Command Prompt window. You can select and configure [PwrTest Scenarios](pwrtest-scenarios.md) using command options.

The syntax for the PwrTest tool is:

```
pwrtest /scenario [/scenario_options] [/common_options]
```

<span id="_scenario"></span><span id="_SCENARIO"></span>**/**<em>scenario</em>  

| Scenarios   | Description                                                                                                                                                        |
|-------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| sleep       | Cycles the computer through sleep/resume transitions. (Windows 7 and later)                                                                                        |
| battery     | Provides battery information and monitoring. (Windows 7 and later)                                                                                                 |
| info        | Provides system power information. (Windows 7 and later)                                                                                                           |
| es          | Monitors thread execution state. (Windows 7 and later)                                                                                                             |
| idle        | Monitors system idle events. (Windows 7 and later)                                                                                                                 |
| ppm         | Monitors processor power management. (Windows 7 and later)                                                                                                         |
| timer       | Monitors system timer resolution changes. (Windows 7 and later)                                                                                                    |
| disk        | Monitors disk idle statistics and spin-down events. (Windows 7 and later)                                                                                          |
| device      | Monitors device idle statistics and power-down events. (Windows 7 and later)                                                                                       |
| monitor     | Records user idle statistics related to monitor/display auto-dimming and blanking.(Windows 7 and later)                                                            |
| requests    | Displays outstanding and new power requests. (Windows 7 and later)                                                                                                 |
| thermal     | Monitors ACPI thermal zone information and statistics. This is only supported on systems that report thermal zones and temperature changes. (Windows 7 and later). |
| processidle | Forces background maintenance tasks to execute (now rather than at their scheduled time) and monitors their progress. (Windows 7 and later)                        |
| cs          | Cycles the computer through connected standby transitions if they are supported by the system. (Windows 8 and later)                                               |
| platidle    | Monitors and attempts to log platform idle transition counts if they are supported by the system. (Windows 8 and later)                                            |
 

 


<span id="_scenario_options"></span><span id="_SCENARIO_OPTIONS"></span>**/**<em>scenario\_options</em>  
To see the options available for each Pwrtest scenario, type: **pwrtest.exe /**<em>scenario</em> **/?**

For example: **pwrtest.exe /sleep /?**

<span id="_common_options"></span><span id="_COMMON_OPTIONS"></span>/*common\_options*  

|       *common\_options*       |                                                                                                                Description                                                                                                                 |
|-------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|    **/lf:**<em>folder</em>    |                                            Specifies the folder for the log files. For example, c:\\myfolder or \\\\server\\share. The default log location is the same folder as pwrtest.exe.                                             |
|     **/ln:**<em>name</em>     |                Specifies the name for the log files and the name for the Event Tracing for Windows (ETW) trace session. The log file extensions are added automatically (.wtl, .xml, etc.). The default name is pwrtestlog.                |
| **/etwbuffersize:**<em>n</em> |                                                  Specifies the ETW buffer size in KB if it is larger than default size. Default is the current page size or 256KB (whichever is greater).                                                  |
| **/etwminbuffers:**<em>n</em> |                                Specifies the minimum number of buffers allocated for the ETW session if larger than the minimum of 2 per logical processor. The default is 2 buffers per logical processor.                                |
| **/etwmaxbuffers:**<em>n</em> | Specifies the maximum number of buffers allocated for the ETW session if that number is larger than the minimum of 2 per logical processor and larger than the **etwminbuffers** setting. The default is the **etwminbuffers** value + 20. |
|        **/delaywrite**        |                                                           Specifies that log data is buffered in memory to reduce disk writes. This option affects all log types including ETL.                                                            |

**Examples**

```
pwrtest /?  
```

```
pwrtest /requests  /?
```

```
pwrtest /requests  /t:60
```

### <span id="Remarks"></span><span id="remarks"></span><span id="REMARKS"></span>Remarks

Execution Requirements to support ETW tracing:

-   Pwrtest must run from an administrator or elevated **Command Prompt** window (**Run as administrator**).

-   Pwrtest must run natively (WoW64 not supported).

The group policy settings put in place by your system administrator might interfere with some scenarios that need to temporarily modify power setting values (such as the sleep scenario).

PwrTest automatically generates multiple logs for each execution in .log (plaintext), .xml (format varies per scenario), .wtl (WTTLog), and .etl (ETW trace) log formats.

To be able to use all PwrTest Scenarios, you must first provision a test computer for testing using Visual Studio and the WDK. For more information, see [Provision a computer for driver deployment and testing (WDK 8.1)](https://msdn.microsoft.com/library/windows/hardware/dn745909), or [Provision a computer for driver deployment and testing (WDK 8)](https://msdn.microsoft.com/library/windows/hardware/hh698272). Some scenarios require the power button driver that is part of Windows Driver Testing Framework (WDTF). WDTF (and the included power button driver) is automatically installed when you provision a system for testing using Visual Studio and the WDK. For information about WDTF, see [**Windows Device Testing Framework (WDTF) (Windows Drivers)**](https://msdn.microsoft.com/library/windows/hardware/ff539547).

## <span id="related_topics"></span>Related topics


[PwrTest Scenarios](pwrtest-scenarios.md)

[PwrTest Log File](pwrtest-log-file.md)

 

 






