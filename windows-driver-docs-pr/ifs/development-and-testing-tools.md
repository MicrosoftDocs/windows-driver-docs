---
title: Development and Testing Tools
author: windows-driver-content
description: Development and Testing Tools
ms.assetid: 6cc81509-27e1-4d5b-996c-6a7bbfd0ddcf
keywords: ["filter manager WDK file system minifilter , tools", "Fltmc.exe WDK file system minifilter", "fltkd debugger extension WDK file system minifilter", "Filter Verifier WDK file system minifilter", "Verifier utility"]
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[ifsk\ifsk]:%20Development%20and%20Testing%20Tools%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


