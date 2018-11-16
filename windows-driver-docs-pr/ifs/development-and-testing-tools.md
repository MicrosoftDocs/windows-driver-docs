---
title: Development and Testing Tools
description: Development and Testing Tools
ms.assetid: 6cc81509-27e1-4d5b-996c-6a7bbfd0ddcf
keywords:
- filter manager WDK file system minifilter , tools
- Fltmc.exe WDK file system minifilter
- fltkd debugger extension WDK file system minifilter
- Filter Verifier WDK file system minifilter
- Verifier utility
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Development and Testing Tools


The filter manager tools described in this section are provided in the IFS Kit for Windows Server 2003 SP1 and in the Windows Driver Kit (WDK) for Windows Vista and later.

Minifilter driver developers are also encouraged to use general-purpose kernel-mode development and testing tools, such as PREfast with driver-specific rules.

### <span id="Fltmc.exe_Control_Program"></span><span id="fltmc.exe_control_program"></span><span id="FLTMC.EXE_CONTROL_PROGRAM"></span>Fltmc.exe Control Program

The Fltmc.exe control program is a command-line utility for common minifilter driver management operations. Developers can use Fltmc.exe to load and unload minifilter drivers, attach minifilter drivers to volumes or detach them from volumes, and enumerate minifilter drivers, instances, and volumes.

### <span id="_fltkd_Debugger_Extension"></span><span id="_fltkd_debugger_extension"></span><span id="_FLTKD_DEBUGGER_EXTENSION"></span>!fltkd Debugger Extension

The !fltkd debugger extension is provided in the [Windows Debugging](https://msdn.microsoft.com/library/windows/hardware/ff551063) tools. Commonly used commands include the following:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Command</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><strong>!cbd</strong></p></td>
<td align="left"><p>The filter manager equivalent of !irp</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>!filter</strong></p></td>
<td align="left"><p>Lists detailed information about the specified filter</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>!filters</strong></p></td>
<td align="left"><p>Lists all attached minifilter drivers</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>!frames</strong></p></td>
<td align="left"><p>Lists all filter manager frames and attached minifilter drivers</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>!instance</strong></p></td>
<td align="left"><p>Lists detailed information about the specified instance</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>!volume</strong></p></td>
<td align="left"><p>Lists detailed information about the specified volume</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>!volumes</strong></p></td>
<td align="left"><p>Lists all volumes and attached minifilter driver instances</p></td>
</tr>
</tbody>
</table>

 

For additional debugging help, test the minifilter driver with the debug version of Fltmgr.sys, which contains numerous ASSERT statements to catch common errors.

### <span id="Filter_Verifier"></span><span id="filter_verifier"></span><span id="FILTER_VERIFIER"></span>Filter Verifier

Filter Verifier is an [I/O Verification](https://msdn.microsoft.com/library/windows/hardware/ff548045) option in [Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff545448) that validates minifilter driver usage of filter manager functions. Filter Verifier is installed with the filter manager. Developers should always develop minifilter drivers with Driver Verifier and Filter Verifier enabled.

To use Filter Verifier, specify the minifilter driver's name and enable the I/O Verification option in Driver Verifier (Verifier.exe). Verification starts when the minifilter driver registers with the filter manager.

Filter Verifier validates the following usage in a minifilter driver:

-   Correct use of parameters and calling context

-   Correct return values from preoperation and postoperation callback routines

-   Consistent and coherent changes to parameters in callback data

Filter Verifier tracks the following filter manager objects:

-   Contexts

-   Callback Data structures

-   Queued Work Items

-   NameInformation structures

-   File Objects

-   Filter Objects

-   Instance Objects

-   Volume Objects

 

 




