---
title: Bug Check 0x14B SOC_SUBSYSTEM_FAILURE
description: The SOC_SUBSYSTEM_FAILURE bug check has a value of 0x0000014B. This indicates that an unrecoverable error was encountered in a System on a Chip (SoC) subsystem.
ms.assetid: CC42D634-90CE-43F1-8552-E5DE711D2117
keywords: ["Bug Check 0x14B SOC_SUBSYSTEM_FAILURE", "Bug Check 0x14B SOC_SUBSYSTEM_FAILURE"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- Bug Check 0x14B SOC_SUBSYSTEM_FAILURE
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0x14B: SOC\_SUBSYSTEM\_FAILURE


The SOC\_SUBSYSTEM\_FAILURE bug check has a value of 0x0000014B. This indicates that an unrecoverable error was encountered in a System on a Chip (SoC) subsystem.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## Bug Check 0x14B SOC\_SUBSYSTEM\_FAILURE Parameters


<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Parameter</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>1</p></td>
<td align="left"><p>Address of an <strong><a href="https://msdn.microsoft.com/library/windows/hardware/dn376404" data-raw-source="[SOC_SUBSYSTEM_FAILURE_DETAILS](https://msdn.microsoft.com/library/windows/hardware/dn376404)">SOC_SUBSYSTEM_FAILURE_DETAILS</a></strong> structure.</p></td>
</tr>
<tr class="even">
<td align="left"><p>2</p></td>
<td align="left"><p>Reserved.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>3</p></td>
<td align="left"><p>Reserved.</p></td>
</tr>
<tr class="even">
<td align="left"><p>4</p></td>
<td align="left"><p>Optional. Address of a vendor-supplied data block.</p></td>
</tr>
</tbody>
</table>

 

Resolution
----------

The [**!analyze**](-analyze.md) debug extension displays information about the bug check and can be very helpful in determining the root cause.

```dbgcmd
2: kd> !analyze -v
*******************************************************************************
*                                                                             *
*                        Bugcheck Analysis                                    *
*                                                                             *
*******************************************************************************

SOC_SUBSYSTEM_FAILURE (14b)
A SOC subsystem has experienced an unrecoverable critical fault.
Arguments:
Arg1: 9aa8d630, nt!SOC_SUBSYSTEM_FAILURE_DETAILS
Arg2: 00000000, Reserved
Arg3: 00000000, Reserved
Arg4: a126c000, (Optional) address to vendor supplied general purpose data block.
```

Use the provided nt!SOC\_SUBSYSTEM\_FAILURE\_DETAILS structure to dump the failure data using the dt command and the address provided by Arg1.

```dbgcmd
2: kd> dt nt!SOC_SUBSYSTEM_FAILURE_DETAILS 9aa8d630
   +0x000 SubsysType       : 1 ( SOC_SUBSYS_AUDIO_DSP )
   +0x008 FirmwareVersion  : 0
   +0x010 HardwareVersion  : 0
   +0x018 UnifiedFailureRegionSize : 0x24
   +0x01c UnifiedFailureRegion : [1]  "F"
```

Work with SoC vendor to further parse the data, including the optional vendor supplied general purpose data block.

You may want to examine the stack trace using the [**k, kb, kc, kd, kp, kP, kv (Display Stack Backtrace)**](k--kb--kc--kd--kp--kp--kv--display-stack-backtrace-.md) command. You can specify the processor number to examine the stacks on all processors.

You can also set a breakpoint in the code leading up to this stop code and attempt to single step forward into the faulting code.

For more information see the following topics:

[Crash dump analysis using the Windows debuggers (WinDbg)](crash-dump-files.md)

If you are not equipped to use the Windows debugger to work on this problem, you can use some basic troubleshooting techniques.

-   Check the System Log in Event Viewer for additional error messages that might help identify the device or driver that is causing this bug check.

-   If a driver is identified in the bug check message, disable the driver or check with the manufacturer for driver updates.

-   You can try running the hardware diagnostics supplied by the system manufacturer.

-   For additional general troubleshooting information, see [**Blue Screen Data**](blue-screen-data.md).

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Minimum supported client</p></td>
<td align="left"><p>Windows 8</p></td>
</tr>
<tr class="even">
<td align="left"><p>Minimum supported server</p></td>
<td align="left"><p>Windows Server 2012</p></td>
</tr>
</tbody>
</table>

 

 




