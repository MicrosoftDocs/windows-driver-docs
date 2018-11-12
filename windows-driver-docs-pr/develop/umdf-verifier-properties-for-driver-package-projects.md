---
ms.assetid: 5BF7AB90-FF2E-4679-8C84-2E8091917F5D
title: UMDF Verifier Properties for Driver Package Projects
description: Sets the properties for the UMDF Verifier on a test computer. You can use these settings when you build and deploy a driver to a test computer.
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# UMDF Verifier Properties for Driver Package Projects

Sets the properties for the UMDF Verifier on a test computer. You can use these settings when you build and deploy a driver to a test computer.

For information about deployment, see [Provision a computer for driver deployment and testing (WDK 8.1)](https://msdn.microsoft.com/Library/Windows/Hardware/Dn745909) and [Deploying a Driver to a Test Computer](deploying-a-driver-to-a-test-computer.md)

For information about debugging UMDF drivers, see [How to Enable Debugging of a UMDF Driver](https://msdn.microsoft.com/Library/Windows/Hardware/Ff554716) and [WDF Verifier Control Application](https://msdn.microsoft.com/Library/Windows/Hardware/Ff556129).

## <span id="Setting_UMDF_Verifier_properties_for_driver_projects"></span><span id="setting_umdf_verifier_properties_for_driver_projects"></span><span id="SETTING_UMDF_VERIFIER_PROPERTIES_FOR_DRIVER_PROJECTS"></span>Setting UMDF Verifier properties for driver projects


1.  Open the property pages for your driver package. Right-click the driver package project in Solution Explorer and select **Properties**.
2.  In the property pages for the driver package, click **Configuration Properties**, click **Driver Install**, and then click **UMDF Verifier**.
3.  Select the **Deploy UMDF Verifier** option. When this option is enabled (**Yes**), you can select the UMDF Verifier options to use on the test computer to verify a UMDF driver.

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
<td align="left"><p><span id="_Deploy_UMDF_Verifier"></span><span id="_deploy_umdf_verifier"></span><span id="_DEPLOY_UMDF_VERIFIER"></span> <strong>Deploy UMDF Verifier</strong></p></td>
<td align="left"><p>Enables the UMDF verifier settings on the test computer.</p></td>
</tr>
<tr class="even">
<td align="left"><p><span id="UMDF_Service_Names"></span><span id="umdf_service_names"></span><span id="UMDF_SERVICE_NAMES"></span><strong>UMDF Service Names</strong></p></td>
<td align="left"><p>Specifies the service names of the UMDF drivers to monitor.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><span id="Enable_Object_Tracking"></span><span id="enable_object_tracking"></span><span id="ENABLE_OBJECT_TRACKING"></span><strong>Enable Object Tracking</strong></p></td>
<td align="left"><p>Tracks all created UMDF objects.</p></td>
</tr>
<tr class="even">
<td align="left"><p><span id="Enable_Reference_Count_Tracking"></span><span id="enable_reference_count_tracking"></span><span id="ENABLE_REFERENCE_COUNT_TRACKING"></span><strong>Enable Reference Count Tracking</strong></p></td>
<td align="left"><p>Tracks all UMDF object references.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><span id="Maximum_Restart_Attempts"></span><span id="maximum_restart_attempts"></span><span id="MAXIMUM_RESTART_ATTEMPTS"></span><strong>Maximum Restart Attempts</strong></p></td>
<td align="left"><p>Maximum number of times UMDF will restart a failed host process.</p></td>
</tr>
<tr class="even">
<td align="left"><p><span id="UMDF_Logging_level"></span><span id="umdf_logging_level"></span><span id="UMDF_LOGGING_LEVEL"></span><strong>UMDF Logging level</strong></p></td>
<td align="left"><p>Specifies the amount of information logged by the UMDF verifier for the drivers it is hosting.</p>
<p><strong>Only Critical and Fatal Errors</strong> - Logs only critical and fatal errors.</p>
<p><strong>All Errors</strong> - Logs all errors.</p>
<p><strong>Warnings and all Errors</strong> - Logs warnings and all errors.</p>
<p><strong>Informational events, Warnings and all Errors</strong> - Logs informational events, warnings, and all errors.</p>
<p><strong>Verbose Output (All Events of any Sort)</strong> - Logs all events.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><span id="Log_to_Kernel_Debugger"></span><span id="log_to_kernel_debugger"></span><span id="LOG_TO_KERNEL_DEBUGGER"></span><strong>Log to Kernel Debugger</strong></p></td>
<td align="left"><p>Logs verifier output to the kernel debugger.</p></td>
</tr>
<tr class="even">
<td align="left"><p><span id="Break_into_Kernel_Debugger"></span><span id="break_into_kernel_debugger"></span><span id="BREAK_INTO_KERNEL_DEBUGGER"></span><strong>Break into Kernel Debugger</strong></p></td>
<td align="left"><p>Break into kernel debugger when the UMDF host process fails.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><span id="Attach_to_Kernel_Debugger"></span><span id="attach_to_kernel_debugger"></span><span id="ATTACH_TO_KERNEL_DEBUGGER"></span><strong>Attach to Kernel Debugger</strong></p></td>
<td align="left"><p>Attaches to the kernel debugger if no user-mode debugger is attached.</p></td>
</tr>
<tr class="even">
<td align="left"><p><span id="Timeout_on_Driver_Load__sec_"></span><span id="timeout_on_driver_load__sec_"></span><span id="TIMEOUT_ON_DRIVER_LOAD__SEC_"></span><strong>Timeout on Driver Load (sec)</strong></p></td>
<td align="left"><p>Specifies the time to wait (in seconds) before attaching the debugger after the driver loads.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><span id="Timeout_on_Driver_Start__sec_"></span><span id="timeout_on_driver_start__sec_"></span><span id="TIMEOUT_ON_DRIVER_START__SEC_"></span><strong>Timeout on Driver Start (sec)</strong></p></td>
<td align="left"><p>Specifies the time to wait (in seconds) before attaching the debugger after the driver starts.</p></td>
</tr>
<tr class="even">
<td align="left"><p><span id="Verify_at_Current_Level"></span><span id="verify_at_current_level"></span><span id="VERIFY_AT_CURRENT_LEVEL"></span><strong>Verify at Current Level</strong></p></td>
<td align="left"><p>Verifies drivers built using earlier versions of the framework against current framework versions rules.</p></td>
</tr>
</tbody>
</table>

 

## <span id="related_topics"></span>Related topics


* [User-Mode Driver Framework](https://docs.microsoft.com/windows-hardware/drivers/wdf/)
* [Driver Verifier](https://msdn.microsoft.com/Library/Windows/Hardware/Ff545448)
* [Deploying a Driver to a Test Computer](deploying-a-driver-to-a-test-computer.md)
 

 






