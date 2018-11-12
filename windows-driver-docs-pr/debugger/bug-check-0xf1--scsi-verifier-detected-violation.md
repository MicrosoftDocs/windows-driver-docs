---
title: Bug Check 0xF1 SCSI_VERIFIER_DETECTED_VIOLATION
description: The SCSI_VERIFIER_DETECTED_VIOLATION bug check has a value of 0x000000F1. This is the bug check code for all Driver Verifier SCSI Verification violations.
ms.assetid: babc33f9-a467-4b19-b1a2-1898d0224d4d
keywords: ["Bug Check 0xF1 SCSI_VERIFIER_DETECTED_VIOLATION", "SCSI_VERIFIER_DETECTED_VIOLATION"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- SCSI_VERIFIER_DETECTED_VIOLATION
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0xF1: SCSI\_VERIFIER\_DETECTED\_VIOLATION


The SCSI\_VERIFIER\_DETECTED\_VIOLATION bug check has a value of 0x000000F1. This is the bug check code for all Driver Verifier **SCSI Verification** violations.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## SCSI\_VERIFIER\_DETECTED\_VIOLATION Parameters


Parameter 1 identifies the type of violation.

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
<th align="left">Cause of Error</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>0x1000</p></td>
<td align="left"><p>First argument passed</p></td>
<td align="left"><p>Second argument passed</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>The miniport driver passed bad arguments to <strong>ScsiPortInitialize</strong>.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x1001</p></td>
<td align="left"><p>Delay, in microseconds</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>The miniport driver called <strong>ScsiPortStallExecution</strong> and specified a delay greater than 0.1 second, stalling the processor too long.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x1002</p></td>
<td align="left"><p>Address of routine that took too long</p></td>
<td align="left"><p>Address of miniport&#39;s HW_DEVICE_EXTENSION</p></td>
<td align="left"><p>Duration of the routine, in microseconds</p></td>
<td align="left"><p>A miniport routine called by the port driver took longer than 0.5 second to execute.</p>
<p>(0.5 seconds is the limit for most routines. However, the <strong>HwInitialize</strong> routine is allowed 5 seconds, and the <strong>FindAdapter</strong> routine is exempt.)</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x1003</p></td>
<td align="left"><p>Address of miniport&#39;s HW_DEVICE_EXTENSION</p></td>
<td align="left"><p>Address of the SRB</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>The miniport driver completed a request more than once.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x1004</p></td>
<td align="left"><p>Address of the SRB</p></td>
<td align="left"><p>Address of miniport&#39;s HW_DEVICE_EXTENSION</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>The miniport driver completed a request with an invalid SRB status.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x1005</p></td>
<td align="left"><p>Address of miniport&#39;s HW_DEVICE_EXTENSION</p></td>
<td align="left"><p>Address of LOGICAL_UNIT_EXTENSION</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>The miniport driver called <strong>ScsiPortNotification</strong> to ask for <strong>NextLuRequest</strong>, but an untagged request is still active.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x1006</p></td>
<td align="left"><p>Address of miniport&#39;s HW_DEVICE_EXTENSION</p></td>
<td align="left"><p>Invalid virtual address</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>The miniport driver passed an invalid virtual address to <strong>ScsiPortGetPhysicalAddress</strong>.</p>
<p>(This usually means the address supplied doesn&#39;t map to the common buffer area.)</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x1007</p></td>
<td align="left"><p>Address of ADAPTER_EXTENSION</p></td>
<td align="left"><p>Address of miniport&#39;s HW_DEVICE_EXTENSION</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>The reset hold period for the bus ended, but the miniport driver still has outstanding requests.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x2001</p></td>
<td align="left"><p>Delay, in microseconds</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>The Storport miniport driver called <strong><a href="https://msdn.microsoft.com/library/windows/hardware/ff567508" data-raw-source="[StorPortStallExecution](https://msdn.microsoft.com/library/windows/hardware/ff567508)">StorPortStallExecution</a></strong> and specified a delay longer than 0.1 second, stalling the processor for an excessive length of time.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x2002</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p><strong><a href="https://msdn.microsoft.com/library/windows/hardware/ff567103" data-raw-source="[StorPortGetUncachedExtension](https://msdn.microsoft.com/library/windows/hardware/ff567103)">StorPortGetUncachedExtension</a></strong> was not called from the miniport driver&#39;s <strong><a href="https://msdn.microsoft.com/library/windows/hardware/ff557390" data-raw-source="[HwStorFindAdapter](https://msdn.microsoft.com/library/windows/hardware/ff557390)">HwStorFindAdapter</a></strong> routine. The <strong>StorPortGetUncachedExtension</strong> routine can only be called from the miniport driver&#39;s <strong>HwStorFindAdapter</strong> routine and only for a bus-master adapter. A Storport miniport driver must set the <strong>SrbExtensionSize</strong> of the <strong><a href="https://msdn.microsoft.com/library/windows/hardware/ff557459" data-raw-source="[HW_INITIALIZATION_DATA](https://msdn.microsoft.com/library/windows/hardware/ff557459)">HW_INITIALIZATION_DATA</a></strong> (Storport) structure before calling <strong>StorPortGetUncachedExtension</strong>.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x2003</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>An invalid address was passed to the <strong><a href="https://msdn.microsoft.com/library/windows/hardware/ff567080" data-raw-source="[StorPortGetDeviceBase](https://msdn.microsoft.com/library/windows/hardware/ff567080)">StorPortGetDeviceBase</a></strong> routine. The <strong>StorPortGetDeviceBase</strong> routine supports only those addresses that were assigned to the driver by the system Plug and Play (PnP) manager.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x2004</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>The Storport miniport driver completed the same I/O request more than once.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x2005</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>The Storport miniport driver passed an invalid virtual address to one of the <strong>StorPortRead</strong><em>xxx</em> or <strong>StorPortWrite</strong><em>xxx</em> routines. This usually means the address supplied doesn&#39;t map to the common buffer area. The specified <em>Register</em> or <em>Port</em> must be in mapped memory-space range returned by <strong><a href="https://msdn.microsoft.com/library/windows/hardware/ff567080" data-raw-source="[StorPortGetDeviceBase](https://msdn.microsoft.com/library/windows/hardware/ff567080)">StorPortGetDeviceBase</a></strong> routine.</p></td>
</tr>
</tbody>
</table>

 

Cause
-----

See the description of each code in the Parameters section for an explanation of the cause.

Resolution
----------

This bug check can only occur when Driver Verifier has been instructed to monitor one or more drivers. If you did not intend to use Driver Verifier, you should deactivate it. You might consider removing the driver which caused this problem as well.

If you are the driver writer, use the information obtained through this bug check to fix the bugs in your code.

The Driver Verifier **SCSI Verification** option is available only in Windows XP and later. The Driver Verifier **Storport Verification** option is available only in Windows 7 and later. For full details on Driver Verifier, see the Windows Driver Kit.

 

 




