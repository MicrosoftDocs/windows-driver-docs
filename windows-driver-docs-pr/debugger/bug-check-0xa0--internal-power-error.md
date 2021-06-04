---
title: Bug Check 0xA0 INTERNAL_POWER_ERROR
description: The INTERNAL_POWER_ERROR bug check has a value of 0x000000A0. This bug check indicates that the power policy manager experienced a fatal error.
keywords: ["Bug Check 0xA0 INTERNAL_POWER_ERROR", "INTERNAL_POWER_ERROR"]
ms.date: 12/09/2020
topic_type:
- apiref
api_name:
- INTERNAL_POWER_ERROR
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0xA0: INTERNAL\_POWER\_ERROR

The INTERNAL\_POWER\_ERROR bug check has a value of 0x000000A0. This bug check indicates that the power policy manager experienced a fatal error.

> [!IMPORTANT]
> This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://www.windows.com/stopcode).

## INTERNAL\_POWER\_ERROR Parameters


Parameter 1 indicates the type of violation. The meaning of the other parameters depends on the value of Parameter 1.

<table>
<colgroup>
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Parameter 1</th>
<th align="left">Parameter 2</th>
<th align="left">Parameter 3</th>
<th align="left">Parameter 4</th>
<th align="left">Cause</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>0x1</p></td>
<td align="left"><p><strong>1:</strong> A device has overrun its maximum number of reference counts.</p>
<p><strong>2, 3, or 4:</strong>  Too many inrush power IRPs have been queued.</p>
<p><strong>5:</strong>  The power IRP has been sent to a passive level device object.</p>
<p><strong>6:</strong> The system has failed to allocate a necessary power IRP.</p></td>
<td align="left"><p>If Parameter 2 has a value of 1, the maximum number of references allowed.</p>
<p>If Parameter 2 has a value of 2, 3, or 4, the maximum number of pending IRPs allowed.</p>
<p>If Parameter 2 has a value of 6, the target device object.</p></td>
<td align="left">If Parameter 2 has value of 6, indicates whether this is a system (0x0) or device (0x1) power IRP.</td>
<td align="left"><p>An error occurred during the handling of the power I/O request packet (IRP).</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x2</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>An internal failure has occurred while attempting to process a power event. For more information, see <a href="#parameter-1-equals-0x2" data-raw-source="[Debugging bug check 0xA0 when parameter 1 equals 0x2](#parameter-1-equals-0x2)">Debugging bug check 0xA0 when parameter 1 equals 0x2</a>.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x3</p></td>
<td align="left"><p>The expected checksum</p></td>
<td align="left"><p>The actual checksum</p></td>
<td align="left"><p>The line number of the failure</p></td>
<td align="left"><p>The checksum for a hibernation context page does not match its expected checksum.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x4</p></td>
<td align="left"><p>The expected checksum</p></td>
<td align="left"><p>The actual checksum</p></td>
<td align="left"><p>The line number of the failure</p></td>
<td align="left"><p>The checksum for a page about to be written to the hibernation file does not match its expected checksum.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x5</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>An unknown shutdown code has been sent to the system shutdown handler.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x7</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>An unhandled exception has occurred. For more information, see <a href="#parameter-1-equals-0x7" data-raw-source="[Debugging bug check 0xA0 when parameter 1 equals 0x7](#parameter-1-equals-0x7)">Debugging bug check 0xA0 when parameter 1 equals 0x7</a>.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x8</p></td>
<td align="left"><p>This parameter is always set to 0x100.</p></td>
<td align="left"><p>The device object</p></td>
<td align="left"><p>POWER_CHANNEL_SUMMARY</p>
<p></p></td>
<td align="left"><p>A fatal error occurred while processing a system power event.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x9</p></td>
<td align="left"><p>Status code</p></td>
<td align="left"><p>Mirroring phase</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>A fatal error occured while preparing the hibernate file.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0xA</p></td>
<td align="left"><p><strong>0:</strong> A bug check was requested immediately upon resuming.</p>
<p><strong>1:</strong> A bug check was requested during resume after all non-pageable devices had been powered on.</p>
<p><strong>2:</strong> A bug check was requested during resume after all devices had been powered on.</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>A bug check was requested when waking for debugging purposes.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0xB</p></td>
<td align="left"><p>Size of the hibernation file.</p></td>
<td align="left"><p>Hibernation progress before running out of space</p>
<p><strong>0:</strong> HIBERFILE_PROGRESS_FREE_MAP</p>
<p><strong>1:</strong> HIBERFILE_PROGRESS_RESUME_CONTEXT</p>
<p><strong>2:</strong> HIBERFILE_PROGRESS_PROCESSOR_STATE</p>
<p><strong>3:</strong> HIBERFILE_PROGRESS_SECURE_RANGES</p>
<p><strong>4:</strong> HIBERFILE_PROGRESS_MEMORY_RANGES</p>
<p><strong>5:</strong> HIBERFILE_PROGRESS_TABLE_PAGES</p>
<p><strong>6:</strong> HIBERFILE_PROGRESS_MEMORY_IMAGE</p></td>
<td align="left"><p>When param 2 is 4, Size of the remaining memory ranges.</p></td>
<td align="left"><p>The hibernation file is too small.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0xC</p></td>
<td align="left"><p>Status code</p></td>
<td align="left"><p>Dump stack context</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>The dump stack failed to initialize.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0xD</p></td>
<td align="left"><p>The system power state in transition.</p></td>
<td align="left"><p>The sleep checkpoint most recently reached.</p></td>
<td align="left"><p>A pointer to the POP_POWER_ACTION structure.</p></td>
<td align="left"><p>The system failed to complete a power transition in a timely manner.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0xF</p></td>
<td align="left"><p>The system power state in transition. </p></td>
<td align="left"><p>The sleep checkpoint most recently reached.</p></td>
<td align="left"><p>A pointer to the thread currently processing the request.</p></td>
<td align="left"><p>The system failed to complete a power transition in a timely manner.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0xF0</p></td>
<td align="left"><p>The system power state in transition.</p></td>
<td align="left"><p>The sleep checkpoint most recently reached.</p></td>
<td align="left"><p>A pointer to the thread currently processing the request.</p></td>
<td align="left"><p>The system failed to complete(suspend) a power transition in a timely manner. </p></td>
</tr>
<tr class="odd">
<td align="left"><p>0xF1</p></td>
<td align="left"><p>The system power state in transition.</p></td>
<td align="left"><p>The sleep checkpoint most recently reached.</p></td>
<td align="left"><p>A pointer to the thread currently processing the request.</p></td>
<td align="left"><p>The system failed to complete(resume) a power transition in a timely manner.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x101</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>Exception pointer.</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>An unhandled exception occured while processing a system power event. For more information, see <a href="#parameter-1-equals-0x101" data-raw-source="[Debugging bug check 0xA0 when parameter 1 equals 0x101](#parameter-1-equals-0x101)">Debugging bug check 0xA0 when parameter 1 equals 0x101</a>.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x102</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>DUMP_INITIALIZATION_CONTEXT</p></td>
<td align="left"><p>POP_HIBER_CONTEXT</p></td>
<td align="left"><p>The hibernation working buffer size is not page aligned.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x103</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>POP_HIBER_CONTEXT</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>All working pages have failed to be accounted for during the hibernation process.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x104</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>POP_HIBER_CONTEXT</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>An attempt was made to map internal hibernation memory while the internal memory structures were locked.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x105</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>POP_HIBER_CONTEXT</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>An attempt was made to map internal hibernation memory with an unsupported memory type flag.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x106</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>The memory descriptor list (MDL)</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>A memory descriptor list was created during the hibernation process which describes memory that is not paged-aligned.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x107</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>POP_HIBER_CONTEXT</p></td>
<td align="left"><p>PO_MEMORY_RANGE_ARRAY</p></td>
<td align="left"><p>A data mismatch has occurred in the internal hibernation data structures.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x108</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>POP_HIBER_CONTEXT</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>The disk subsystem failed to properly write part of the hibernation file.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x109</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>Expected checksum</p></td>
<td align="left"><p>Actual checksum</p></td>
<td align="left"><p>The checksum for the processor state data does not match its expected checksum.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x10A</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>POP_HIBER_CONTEXT</p></td>
<td align="left"><p>NTSTATUS failure code</p></td>
<td align="left"><p>The disk subsystem failed to properly read or write part of the hibernation file.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x10B</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>Current hibernation progress</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>An attempt was made to mark pages for the boot phase of hibernation at the wrong time using the PoSetHiberRange API.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x10C</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>Flags provided to the API</p></td>
<td align="left"><p>Length to mark</p></td>
<td align="left"><p>The PoSetHiberRange API was called with invalid parameters.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x10D</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>POP_HIBER_CONTEXT</p></td>
<td align="left"><p>NTSTATUS failure code</p></td>
<td align="left"><p>The secure kernel subsystem failed while providing data for resume.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x10E</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>Incorrect checksum</p></td>
<td align="left"><p>Previous disk read's checksum</p></td>
<td align="left"><p>The disk subsystem returned corrupt data while reading from the hibernation file.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x10F</p></td>
<td align="left"><p>The current system sleep checkpoint.</p></td>
<td align="left"><p>The type of internal error.</p>
<p>0 : A checkpoint was written while paging was disabled but before Po disabled interrupts on all processors.</p>
<p>1 : A CPU other than 0 tried to write a checkpoint during the interrupts disabled phase of system sleep.</p>
<p>2 : Another piece of code in the system is executing an EFI runtime service.</p>
</td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>An internal error occured while checkpointing system sleep progress.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x110</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>The system failed to disable system sleep states, but must do so to ensure data integrity.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x111</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>A driver has indicated that the user is present, and the user has enabled a debugging option to capture the call stack.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x200</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>DEVICE_OBJECT</p></td>
<td align="left"><p>DEVICE_OBJECT_POWER_EXTENSION</p></td>
<td align="left"><p>An unknown device type is being checked for an idle state.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x300</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>DEVICE_OBJECT</p></td>
<td align="left"><p>IRP</p></td>
<td align="left"><p>An unknown status was returned from a battery power IRP.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x301</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>DEVICE_OBJECT</p></td>
<td align="left"><p>IRP</p></td>
<td align="left"><p>The battery has entered an unknown state.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x400</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>IO_STACK_LOCATION</p></td>
<td align="left"><p>DEVICE_OBJECT</p></td>
<td align="left"><p>A device has overrun its maximum number of reference counts.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x401</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>Pending IRP list</p></td>
<td align="left"><p>DEVICE_OBJECT</p></td>
<td align="left"><p>Too many inrush power IRPs have been queued.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x402</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>Pending IRP list</p></td>
<td align="left"><p>DEVICE_OBJECT</p></td>
<td align="left"><p>Too many inrush power IRPs have been queued.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x403</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>Pending IRP list</p></td>
<td align="left"><p>DEVICE_OBJECT</p></td>
<td align="left"><p>Too many inrush power IRPs have been queued.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x404</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>IO_STACK_LOCATION</p></td>
<td align="left"><p>DEVICE_OBJECT</p></td>
<td align="left"><p>A power IRP has been sent to a passive-level device object.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x500</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>IRP</p></td>
<td align="left"><p>DEVICE_OBJECT</p></td>
<td align="left"><p>An unknown status was returned from a thermal power IRP.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x600</p></td>
<td align="left"><p>DEVICE_OBJECT PDO</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>A driver has attempted a duplicate registration with the Power Runtime Framework.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x601</p></td>
<td align="left"><p>POP_FX_DEVICE device</p></td>
<td align="left"><p>PEP_DEVICE_REGISTER PEP</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>No Power Engine Plugins accepted device registration.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x602</p></td>
<td align="left"><p>DEVICE_NODE device node</p></td>
<td align="left"><p>Sleep count</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>Device node sleep count does not match its activation count.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x603</p></td>
<td align="left"><p>POP_FX_PLUGIN</p></td>
<td align="left"><p>Work request type</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>A Power Engine Plugin made an invalid work request.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x605</p></td>
<td align="left"><p>Notification ID</p></td>
<td align="left"><p>POP_FX_PLUGIN</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>A Power Engine Plugin failed to accept mandatory device power management notification.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x606</p></td>
<td align="left"><p>POP_FX_COMPONENT</p></td>
<td align="left"><p>POP_FX_COMPONENT_FLAGS</p></td>
<td align="left"><p>New condition for the component</p></td>
<td align="left"><p>A Power Engine Plugin attempted to transition a critical system resource component to an Active (or Idle) condition when the resource was already Active (or Idle).</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x607</p></td>
<td align="left"><p>POP_FX_DEVICE</p></td>
<td align="left"><p>NTSTATUS</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>The acquisition of a runtime power management framework device-removal lock failed when it was required to succeed.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x608</p></td>
<td align="left"><p>POP_FX_COMPONENT</p></td>
<td align="left"><p>POP_FX_COMPONENT_FLAGS</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>A driver has attempted to transition a component to idle without a preceding active request.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x609</p></td>
<td align="left"><p>POP_FX_PLUGIN</p></td>
<td align="left"><p>POP_FX_DEVICE</p></td>
<td align="left"><p>Duplicate Request Type</p>
<p><strong>0:</strong> DevicePowerRequired</p>
<p><strong>1:</strong> DevicePowerNotRequired</p></td>
<td align="left"><p>A Power Engine Plugin has requested either device power required or device power not required without an intervening request of the opposite type.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x610</p></td>
<td align="left"><p>POP_FX_PLUGIN</p></td>
<td align="left"><p>POP_FX_DEVICE</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>A Power Engine Plugin has requested device power not required while a previous device power required request is outstanding.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x611</p></td>
<td align="left"><p>POP_FX_PLUGIN</p></td>
<td align="left"><p>POP_FX_DEVICE</p></td>
<td align="left"><p>Invalid component index</p></td>
<td align="left"><p>A Power Engine Plugin has requested an operation on an invalid component.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x612</p></td>
<td align="left"><p>POP_FX_PLUGIN PowerEnginePlugin</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>A Power Engine Plugin has requested additional work to be done in the context of a device notification where no buffer was supplied by PO for the request.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x613</p></td>
<td align="left"><p>POP_FX_DEVICE</p></td>
<td align="left"><p>Component index</p></td>
<td align="left"><p>Operation</p>
<p><strong>0:</strong> Complete device power not required</p>
<p><strong>1:</strong> Report device powered on</p>
<p><strong>2:</strong> Complete idle condition</p></td>
<td align="left"><p>A driver has attempted to complete a request when no such outstanding request is pending.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x614</p></td>
<td align="left"><p>POP_FX_DEVICE</p></td>
<td align="left"><p>Component index</p></td>
<td align="left"><p>Illegal parameter</p>
<p><strong>0:</strong> PO_FX_FLAG_BLOCKING used at IRQL &gt;= DISPATCH_LEVEL</p>
<p><strong>1:</strong> PO_FX_FLAG_BLOCKING and PO_FX_FLAG_ASYNC_ONLY both specified</p>
<p><strong>2:</strong> Invalid component index</p></td>
<td align="left"><p>A driver has requested an active/idle transition on a component with an illegal parameter.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x615</p></td>
<td align="left"><p>POP_FX_PLUGIN</p></td>
<td align="left"><p>POP_FX_COMPONENT</p></td>
<td align="left"><p>Illegal Action</p>
<p><strong>0:</strong> Component not in idle state 0</p>
<p><strong>1:</strong>Component is already active</p>
<p><strong>2:</strong> No outstanding activation request</p>
<p><strong>3:</strong> Outstanding idle state transition</p></td>
<td align="left"><p>A Power Engine Plugin has illegally indicated the completion of a component activation.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x616</p></td>
<td align="left"><p>POP_FX_PLUGIN</p></td>
<td align="left"><p>POP_FX_COMPONENT</p></td>
<td align="left"><p>Illegal Action</p>
<p><strong>0:</strong> Invalid idle state</p>
<p><strong>1:</strong> Component is already in the requested state</p>
<p><strong>2:</strong> Requested a non-zero idle state without passing through idle state 0</p></td>
<td align="left"><p>A Power Engine Plugin has illegally requested a component idle state transition.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x617</p></td>
<td align="left"><p>POP_FX_PLUGIN PowerEnginePlugin</p></td>
<td align="left"><p>UNICODE_STRING DeviceId</p></td>
<td align="left"><p>PEP_DEVICE_REGISTER PEP Registration</p></td>
<td align="left"><p>A Power Engine Plugin has returned an invalid acceptance type when processing a device registration notification.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x618</p></td>
<td align="left"><p>POP_FX_WORK_ORDER_WATCHDOG_INFO WorkOrder</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>A runtime power worker thread has been blocked for too long.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x619</p></td>
<td align="left"><p>POP_FX_DEVICE Device</p></td>
<td align="left"><p>Component index</p></td>
<td align="left"><p>NULL or DEVICE_NODE of the child device actually responsible</p></td>
<td align="left"><p>A device has blocked entry into the deepest runtime idle power state for too long.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x61A</p></td>
<td align="left"><p>POP_FX_PLUGIN Power Engine Plugin</p></td>
<td align="left"><p>POP_FX_DEVICE device</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>A Power Engine Plugin has supplied invalid information about a component's performance state information.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x61B</p></td>
<td align="left"><p>POP_FX_DEVICE device</p></td>
<td align="left"><p>Component index</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>A driver has issued a perf state request before registering for device perf states. </p></td>
</tr>
<tr class="even">
<td align="left"><p>0x61C</p></td>
<td align="left"><p>POP_FX_DEVICE device</p></td>
<td align="left"><p>Component index</p></td>
<td align="left"><p>Invalid Parameter</p>
<p>VALUES:</p>
<p>  0 : PerfChangesCount exceeds the number of perf state sets registered for this component</p></td>
<td align="left"><p> A driver has issued a perf state request with invalid parameters.
</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x61D</p></td>
<td align="left"><p>POP_FX_DEVICE device</p></td>
<td align="left"><p>Component index</p></td>
<td align="left"><p>Outstanding request context</p></td>
<td align="left"><p>A driver has issued a perf state request while a previous request is outstanding.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x61E</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p> A Power Engine Plugin has attempted to perform a critical transition on a debugger device while automatic transitions are enabled.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x61F</p></td>
<td align="left"><p>POP_FX_DEVICE device</p></td>
<td align="left"><p>Coordinated idle state index</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>A Power Engine Plugin has attempted to enable automatic debugger transitions for a coordinated idle state that is not a platform-wide state.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x620</p></td>
<td align="left"><p>POP_FX_DEVICE device</p></td>
<td align="left"><p> Coordinated idle state index</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p> A Power Engine Plugin has attempted to register a D-state dependency for a coordinated idle state that is not a platform-wide state.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x621</p></td>
<td align="left"><p>POP_FX_DEVICE device</p></td>
<td align="left"><p>Component index</p></td>
<td align="left"><p>Coordinated idle state index</p></td>
<td align="left"><p> A Power Engine Plugin has attempted to register an F-state dependency for a coordinated idle state that is not a platform-wide state.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x622</p></td>
<td align="left"><p>The parent POP_FX_COMPONENT</p></td>
<td align="left"><p>The child POP_FX_COMPONENT</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>A driver has attempted to unregister from PoFx with outstanding dependents.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x666</p></td>
<td align="left"><p>PPOP_PEP_ACTIVITY</p></td>
<td align="left"><p>New activity type</p>
<p><strong>0:</strong> DevicePowerOn</p>
<p><strong>1:</strong> ComponentIdleStateChange</p>
<p><strong>2:</strong> ComponentActivating</p>
<p><strong>3:</strong> ComponentActive</p>
<p><strong>4:</strong> DevicePowerOff</p>
<p><strong>5:</strong> DeviceSuspend</p></td>
<td align="left"><p>Conflicting activity type</p>
<p><strong>0:</strong> DevicePowerOn</p>
<p><strong>1:</strong> ComponentIdleStateChange</p>
<p><strong>2:</strong> ComponentActivating</p>
<p><strong>3:</strong> ComponentActive</p>
<p><strong>4:</strong> DevicePowerOff</p>
<p><strong>5:</strong> DeviceSuspend</p></td>
<td align="left"><p>The default Power Engine Plugin has attempted to trigger a new activity that conflicts with another activity.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x667</p></td>
<td align="left"><p>POP_PEP_ACTIVITY</p></td>
<td align="left"><p>Activity type</p>
<p><strong>0:</strong> DevicePowerOn</p>
<p><strong>1:</strong> ComponentIdleStateChange</p>
<p><strong>2:</strong> ComponentActivating</p>
<p><strong>3:</strong> ComponentActive</p>
<p><strong>4:</strong> DevicePowerOff</p>
<p><strong>5:</strong> DeviceSuspend</p></td>
<td align="left"><p>POP_PEP_ACTIVITY_STATUS</p></td>
<td align="left"><p>Default Power Engine Plugin has attempted to complete an activity that is not running.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x668</p></td>
<td align="left"><p>PPPM_COORDINATED_STATE whose reference count is being updated.</p></td>
<td align="left"><p>The invalid reference count value observed by this function.</p></td>
<td align="left"><p>The mask of platform idle states being updated.</p></td>
<td align="left"><p> Default Power Engine Plugin has attempted to remove a platform idle state constraint that was not previously constrained.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x669</p></td>
<td align="left"><p>PPPM_COORDINATED_STATE whose reference count is being updated.</p></td>
<td align="left"><p>The invalid reference count value observed by this function.</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>Default Power Engine Plugin has encountered an internal consistency error while attempting to exclusively notify PoFx about the availability of a platform idle state.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x680</p></td>
<td align="left"><p>NTSTATUS failure code.</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>The runtime power framework could not parse a required ACPI table due to it either being missing or malformed. This is usually due to a BIOS error.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x700</p></td>
<td align="left"><p>PEPHANDLE</p></td>
<td align="left"><p>PEP_PPM_IDLE_SELECT</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>A Power Engine Plugin has specified invalid processor idle dependencies.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x701</p></td>
<td align="left"><p>The index of the selected idle state of the hung processor</p></td>
<td align="left"><p>The PRCB address of the hung processor</p></td>
<td align="left"><p>The index of the hung processor</p></td>
<td align="left"><p>A processor was not able to complete an idle transition within the allocated interval. This indicates the specified processor is hung.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x702</p></td>
<td align="left"><p>The index of the selected idle state of the processor</p></td>
<td align="left"><p>The idle synchronization state of the processor</p></td>
<td align="left"><p>The PRCB address of the hung processor</p></td>
<td align="left"><p>A processor woke up from a non-interruptible state without the OS initiating an explicit wake through the PEP (using the necessary PPM idle synchronization).</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x703</p></td>
<td align="left"><p>PEPHANDLE</p></td>
<td align="left"><p>PEP_PPM_QUERY_PLATFORM_STATE</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>A Power Engine Plugin has specified invalid processor idle dependencies during a query platform state notification.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x704</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>A coordinated idle state transition did not complete in a timely manner.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x705</p></td>
<td align="left"><p>PEPHANDLE</p></td>
<td align="left"><p>Notification</p></td>
<td align="left"><p>Four-character tag identifying the illegally altered field. Decode tag in a kernel debugger with: .formats tag, with tag enclosed in < >. </p></td>
<td align="left"><p>A Power Engine Plugin has altered a read only field in the buffer passed into a notification. </p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x706</p></td>
<td align="left"><p>Notification</p></td>
<td align="left"><p>Four-character tag identifying the field containing the illegal value. Decode tag in a kernel debugger with: .formats tag, with tag enclosed in < >. </p></td>
<td align="left"><p>Illegal value or index into an array where an illegal value exists</p></td>
<td align="left"><p>A Power Engine Plugin has returned an illegal value in one of the fields of the buffer passed into a notification.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x800</p></td>
<td align="left"><p>Current CS state</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>The monitor unexpectedly turned on while the system was in connected standby.
</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x801</p></td>
<td align="left"><p>The display state change reason</p></td>
<td align="left"><p>The ID of the session that updated the display state</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>An invalid display state transition has occurred.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x802</p></td>
<td align="left"><p>POWER_MONITOR_REQUEST_REASON that caused the display to turn off</p></td>
<td align="left"><p>1 if the Power Event Processor is enabled, 0 otherwise.</p></td>
<td align="left"><p>Pointer to a POP_PDC_IDLE_PHASE_WATCHDOG_CONTEXT global.</p></td>
<td align="left"><p>PDC System Idle Phase (NoCsPhase) has been blocking transition to Modern Standby for a longer time than expected.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x900</p></td>
<td align="left"><p>Pointer to the responsible power-setting callback</p></td>
<td align="left"><p>IRQL before calling the power-setting callback</p></td>
<td align="left"><p>IRQL after returning from the power-setting callback</p></td>
<td align="left"><p> A registered power-setting callback returned with modified IRQL. This indicates that the callback changed the IRQL but did not restore the original IRQL before returning.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x901</p></td>
<td align="left"><p>DEVICE_OBJECT</p></td>
<td align="left"><p>IRP</p></td>
<td align="left"><p>The thread's APC disable count</p></td>
<td align="left"><p>A driver has enabled/disabled kernel APCs while handling a power IRP.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x4001</p></td>
<td align="left"><p>KE error subcode.</p>
<p>VALUES:</p>
<p>0x100 : (INTERNAL_POWER_ERROR_KE_PROCESSOR_ON_TIMED_OUT) The firmware took too long to power on a processor.</p>
<p>0x101 : (INTERNAL_POWER_ERROR_KE_INVALID_INTERRUPT_TARGET) An invalid interrupt target was specified.</p>
<p>0x102 : (INTERNAL_POWER_ERROR_KE_SETDESTINATION_FAILED) Failed to change the target destination of an
interrupt line.</p>
<p>0x103 : (INTERNAL_POWER_ERROR_KE_IPI_REQUEST_FAILED) Failed to issue an IPI while an interrupt is being redirected.</p>
<p>0x104 : (INTERNAL_POWER_ERROR_KE_ARCH_NOT_SUPPORTED) Unsupported processor architecture.</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>(INTERNAL_POWER_ERROR_KE_SUBCODE) An internal failure has occured in kernel executive during a power operation.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0xAA64</p></td>
<td align="left"><p>Error Code</p></td>
<td align="left"><p>PSCI Function ID in progress</p></td>
<td align="left"><p>Optional internal context dependent data</p></td>
<td align="left"><p>AArm64 Power State Coordination Interface (PSCI) function encountered an unrecoverable critical error.</p></td>
</tr>
</tbody>
</table>

## Resolution

**General Notes**

In the preceding table, several of the parameters are pointers to structures. For example, if Parameter 2 is listed as DEVICE\_OBJECT, then Parameter 2 is a pointer to a DEVICE\_OBJECT structure. Some of the structures are defined in wdm.h, which is included in the Windows Driver Kit. For example, the following structures are defined in wdm.h.

-   EXCEPTION\_POINTERS
-   DEVICE\_OBJECT
-   IO\_STACK\_LOCATION
-   PEP\_DEVICE\_REGISTER

Some of the structures that appear in the preceding table are not defined in any public header file. You can see the definitions of those structures by using the [**dt**](dt--display-type-.md) debugger command. The following example shows how to use the **dt** command to see the **DEVICE\_OBJECT\_POWER\_EXTENSION** structure.

```dbgcmd
3: kd> dt nt!DEVICE_OBJECT_POWER_EXTENSION
   +0x000 IdleCount        : Uint4B
   +0x004 BusyCount        : Uint4B
   +0x008 BusyReference    : Uint4B
   +0x00c TotalBusyCount   : Uint4B
   +0x010 ConservationIdleTime : Uint4B
   +0x014 PerformanceIdleTime : Uint4B
   +0x018 DeviceObject     : Ptr64 _DEVICE_OBJECT
   +0x020 IdleList         : _LIST_ENTRY
   +0x030 IdleType         : _POP_DEVICE_IDLE_TYPE
   +0x034 IdleState        : _DEVICE_POWER_STATE
   +0x038 CurrentState     : _DEVICE_POWER_STATE
   +0x040 Volume           : _LIST_ENTRY
   +0x050 Specific         : <unnamed-tag>
```

The following procedures will help you debug certain instances of this bug check.

<span id="parameter-1-equals-0x2"></span><span id="PARAMETER-1-EQUALS-0X2"></span>
**Debugging bug check 0xA0 when Parameter 1 equals 0x2**

1.  Examine the stack. Look for the **ntoskrnl!PopExceptionFilter** function. This function contains the following code as its first argument.

    ```cpp
     (error_code << 16) | _LINE_
    ```

    If the caller is **PopExceptionFilter**, the first argument to this function is of type PEXCEPTION\_POINTERS. Note the value of this argument.

2.  Use the [**dt (Display Type)**](dt--display-type-.md) command and specify the value that you found in the previous step as *argument*.

    ```dbgcmd
    dt nt!_EXCEPTION_POINTERS argument 
    ```

    This command displays the structure. Note the address of the context record.

3.  Use the [**.cxr (Display Context Record)**](-cxr--display-context-record-.md) command and specify the context record that you found in the previous step as *record*.

    ```dbgcmd
    .cxr record 
    ```

    This command sets the register context to the proper value.

4.  Use a variety of commands to analyze the source of the error. Start with [**kb (Display Stack Backtrace)**](k--kb--kc--kd--kp--kp--kv--display-stack-backtrace-.md) .

<span id="parameter-1-equals-0x7"></span><span id="PARAMETER-1-EQUALS-0X7"></span>
**Debugging bug check 0xA0 when Parameter 1 equals 0x7**

1.  Examine the stack. Look for the **ntoskrnl!PopExceptionFilter** function. The first argument to this function is of type PEXCEPTION\_POINTERS. Note the value of this argument.

2.  Use the [**dt (Display Type)**](dt--display-type-.md) command and specify the value that you found in the previous step as *argument*.

    ```dbgcmd
    dt nt!_EXCEPTION_POINTERS argument 
    ```

    This command displays the structure. Note the address of the context record.

3.  Use the [**.cxr (Display Context Record)**](-cxr--display-context-record-.md) command and specify the context record that you found in the previous step as *record*.

    ```dbgcmd
    .cxr record 
    ```

    This command sets the register context to the proper value.

4.  Use a variety of commands to analyze the source of the error. Start with [**kb (Display Stack Backtrace)**](k--kb--kc--kd--kp--kp--kv--display-stack-backtrace-.md) .

<span id="parameter-1-equals-0x101"></span><span id="PARAMETER-1-EQUALS-0X101"></span>
**Debugging bug check 0xA0 when Parameter 1 equals 0x101**

1.  Use the [**dt (Display Type)**](dt--display-type-.md) command and specify the value of Parameter 3 as *argument*.

    ```dbgcmd
    dt nt!_EXCEPTION_POINTERS argument 
    ```

    This command displays the structure. Note the address of the context record.

2.  Use the [**.cxr (Display Context Record)**](-cxr--display-context-record-.md) command and specify the context record that you found the previous step as *record*.

    ```dbgcmd
    .cxr record 
    ```

    This command sets the register context to the proper value.

3.  Use a variety of commands to analyze the source of the error. Start with [**kb (Display Stack Backtrace)**](k--kb--kc--kd--kp--kp--kv--display-stack-backtrace-.md) .

 

 




