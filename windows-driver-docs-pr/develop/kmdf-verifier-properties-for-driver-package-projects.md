---
ms.assetid: 40D39F8E-3CD3-434B-A161-45D5BD4FBA09
title: KMDF Verifier Properties for Driver Package Projects
description: Sets properties for KMDF Verifier on a remote computer.  Use these settings to build and deploy a KMDF driver to a test computer.
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# KMDF Verifier Properties for Driver Package Projects

Sets the properties for the KMDF Verifier (or framework verifier) on a remote computer. You can use these settings when you build and deploy a KMDF driver to a test computer. For information about KMDF drivers, see [Kernel-Mode Driver Framework](https://docs.microsoft.com/windows-hardware/drivers/wdf/).

For more information about the framework verifier, see [Using the Framework's Verifier](https://msdn.microsoft.com/Library/Windows/Hardware/Ff545540) and [WDF Verifier Control Application](https://msdn.microsoft.com/Library/Windows/Hardware/Ff556129).

## <span id="Setting_KMDF_Verifier_properties_for_driver_package_projects"></span><span id="setting_kmdf_verifier_properties_for_driver_package_projects"></span><span id="SETTING_KMDF_VERIFIER_PROPERTIES_FOR_DRIVER_PACKAGE_PROJECTS"></span>Setting KMDF Verifier properties for driver package projects


1.  Open the property pages for your driver package. Right-click the driver package project in Solution Explorer and select **Properties**.
2.  In the property pages for the driver package, click **Configuration Properties**, click **Driver Install**, and then click **KMDF Verifier**.
3.  Click the **Enable KMDF Verifier** option and select **KMDF verifier is always on**. When this option is selected, you can configure the framework verification options for KMDF drivers.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Option</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><span id="Enable_KMDF_Verifier"></span><span id="enable_kmdf_verifier"></span><span id="ENABLE_KMDF_VERIFIER"></span><strong>Enable KMDF Verifier</strong></p></td>
<td align="left"><p>Enables the KMDF verifier on the test computer. The choices are <strong>KMDF verifier is always on</strong> or <strong>KMDF verifer is off</strong>. If the KMDF verifier is not enabled, basic framework verification is enabled as part of <a href="https://msdn.microsoft.com/Library/Windows/Hardware/Ff545448" data-raw-source="[Driver Verifier](https://msdn.microsoft.com/Library/Windows/Hardware/Ff545448)">Driver Verifier</a> if KMDF version is 1.9 or higher.</p></td>
</tr>
<tr class="even">
<td align="left"><p><span id="KMDF_Service_Names"></span><span id="kmdf_service_names"></span><span id="KMDF_SERVICE_NAMES"></span><strong>KMDF Service Names</strong></p></td>
<td align="left"><p>Specifies the service names of the KDMF drivers to monitor.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><span id="IRQL_checks"></span><span id="irql_checks"></span><span id="IRQL_CHECKS"></span><strong>IRQL checks</strong></p></td>
<td align="left"><p>Enables IRQL checks and critical memory leak checks.</p></td>
</tr>
<tr class="even">
<td align="left"><p><span id="Forward_Compatible_Checks"></span><span id="forward_compatible_checks"></span><span id="FORWARD_COMPATIBLE_CHECKS"></span><strong>Forward Compatible Checks</strong></p></td>
<td align="left"><p>Enables checks created after the current driver version.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><span id="Forward_Progress_Handler_Testing"></span><span id="forward_progress_handler_testing"></span><span id="FORWARD_PROGRESS_HANDLER_TESTING"></span><strong>Forward Progress Handler Testing</strong></p></td>
<td align="left"><p>Specifies options for testing forward progress handling of your driver.</p>
<p><strong>No Allocation Failures</strong> No faults will be simulated to test the forward progress handling of your driver.</p>
<p><strong>Fail All Allocations</strong> All I/O requests destined for a forward progress queue will appear to fail, relying on your driver&#39;s forward progress handling.</p>
<p><strong>Randomly Fail Allocations</strong> Randomly fail I/O requests destined for a forward progress queue.</p></td>
</tr>
<tr class="even">
<td align="left"><p><span id="Track_KMDF_Object_Handles"></span><span id="track_kmdf_object_handles"></span><span id="TRACK_KMDF_OBJECT_HANDLES"></span><strong>Track KMDF Object Handles</strong></p></td>
<td align="left"><p>Specifies the list of object handle types to track.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><span id="Enable_KMDF_Loader_Messages"></span><span id="enable_kmdf_loader_messages"></span><span id="ENABLE_KMDF_LOADER_MESSAGES"></span><strong>Enable KMDF Loader Messages</strong></p></td>
<td align="left"><p>Enables KMDF loader messages through the debugger. A reboot of the target computer is required to enable this.</p>
<p>Starting with Windows Vista, the operating system suppresses DbgPrint output by default, which makes the WDF Loader diagnostic messages unusable until the suppression is overridden. KDMF Verifier can manage this for you so that KMDF loader diagnostics are available in the kernel debugger for these systems.</p></td>
</tr>
<tr class="even">
<td align="left"><p><span id="Verbose_logging"></span><span id="verbose_logging"></span><span id="VERBOSE_LOGGING"></span><strong>Verbose logging</strong></p></td>
<td align="left"><p>Enables verbose logging.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><span id="Memory_Pages_for_Logs"></span><span id="memory_pages_for_logs"></span><span id="MEMORY_PAGES_FOR_LOGS"></span><strong>Memory Pages for Logs</strong></p></td>
<td align="left"><p>Specifies the number of non-paged pool pages (1-10) to allocate for kernel event trace logs. The options are <strong>Runtime Choice</strong> or [<strong>1</strong>-<strong>10</strong>]. If <strong>Runtime Choice</strong>, the number of pages depends on the KMDF runtime. Starting with KMDF 1.9, the runtime uses more pages when verification is enabled with verbose logging.</p></td>
</tr>
<tr class="even">
<td align="left"><p><span id="Fail_Memory_Allocations"></span><span id="fail_memory_allocations"></span><span id="FAIL_MEMORY_ALLOCATIONS"></span><strong>Fail Memory Allocations</strong></p></td>
<td align="left"><p>Specifies the number of successful memory allocations allowed before the KMDF verifier starts to fail all memory allocations.</p></td>
</tr>
</tbody>
</table>

 

## <span id="related_topics"></span>Related topics


* [Kernel-Mode Driver Framework](https://docs.microsoft.com/windows-hardware/drivers/wdf/)
* [Driver Verifier](https://msdn.microsoft.com/Library/Windows/Hardware/Ff545448)
* [Deploying a Driver to a Test Computer](deploying-a-driver-to-a-test-computer.md)
 

 






