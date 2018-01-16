---
title: Specific Exceptions
description: Specific Exceptions
ms.assetid: e9fec81f-7e93-47cd-b496-a5e2a58f3b19
keywords: ["Specific Exceptions Windows Debugging"]
topic_type:
- apiref
api_name:
- Specific Exceptions
api_type:
- NA
ms.author: domars
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Specific Exceptions


The following table lists the exception codes for the specific exception filters.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Exception Code</th>
<th align="left">Exception</th>
<th align="left">Header file or value</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>STATUS_ACCESS_VIOLATION</p></td>
<td align="left"><p>Access violation</p></td>
<td align="left"><p>NtStatus.h</p></td>
</tr>
<tr class="even">
<td align="left"><p>STATUS_ASSERTION_FAILURE</p></td>
<td align="left"><p>Assertion failure</p></td>
<td align="left"><p>NtStatus.h</p></td>
</tr>
<tr class="odd">
<td align="left"><p>STATUS_APPLICATION_HANG</p></td>
<td align="left"><p>Application hang</p></td>
<td align="left"><p>0xCFFFFFFF</p></td>
</tr>
<tr class="even">
<td align="left"><p>STATUS_BREAKPOINT</p></td>
<td align="left"><p>Break instruction exception</p></td>
<td align="left"><p>NtStatus.h</p></td>
</tr>
<tr class="odd">
<td align="left"><p>STATUS_CPP_EH_EXCEPTION</p></td>
<td align="left"><p>C++ exception handling exception</p></td>
<td align="left"><p>0xE06D7363</p></td>
</tr>
<tr class="even">
<td align="left"><p>STATUS_CLR_EXCEPTION</p></td>
<td align="left"><p>Common language runtime (CLR) exception</p></td>
<td align="left"><p>0xE0434f4D</p></td>
</tr>
<tr class="odd">
<td align="left"><p>DBG_CONTROL_BREAK</p></td>
<td align="left"><p>CTRL+Break exception</p></td>
<td align="left"><p>NtStatus.h</p></td>
</tr>
<tr class="even">
<td align="left"><p>DBG_CONTROL_C</p></td>
<td align="left"><p>CTRL+C exception</p></td>
<td align="left"><p>NtStatus.h</p></td>
</tr>
<tr class="odd">
<td align="left"><p>STATUS_DATATYPE_MISALIGNMENT</p></td>
<td align="left"><p>Data misaligned</p></td>
<td align="left"><p>NtStatus.h</p></td>
</tr>
<tr class="even">
<td align="left"><p>DBG_COMMAND_EXCEPTION</p></td>
<td align="left"><p>Debugger command exception</p></td>
<td align="left"><p>NtStatus.h</p></td>
</tr>
<tr class="odd">
<td align="left"><p>STATUS_GUARD_PAGE_VIOLATION</p></td>
<td align="left"><p>Guard page violation</p></td>
<td align="left"><p>NtStatus.h</p></td>
</tr>
<tr class="even">
<td align="left"><p>STATUS_ILLEGAL_INSTRUCTION</p></td>
<td align="left"><p>Illegal instruction</p></td>
<td align="left"><p>NtStatus.h</p></td>
</tr>
<tr class="odd">
<td align="left"><p>STATUS_IN_PAGE_ERROR</p></td>
<td align="left"><p>In-page I/O error</p></td>
<td align="left"><p>NtStatus.h</p></td>
</tr>
<tr class="even">
<td align="left"><p>STATUS_INTEGER_DIVIDE_BY_ZERO</p></td>
<td align="left"><p>Integer divide-by-zero</p></td>
<td align="left"><p>NtStatus.h</p></td>
</tr>
<tr class="odd">
<td align="left"><p>STATUS_INTEGER_OVERFLOW</p></td>
<td align="left"><p>Integer overflow</p></td>
<td align="left"><p>NtStatus.h</p></td>
</tr>
<tr class="even">
<td align="left"><p>STATUS_INVALID_HANDLE</p></td>
<td align="left"><p>Invalid handle</p></td>
<td align="left"><p>NtStatus.h</p></td>
</tr>
<tr class="odd">
<td align="left"><p>STATUS_INVALID_LOCK_SEQUENCE</p></td>
<td align="left"><p>Invalid lock sequence</p></td>
<td align="left"><p>NtStatus.h</p></td>
</tr>
<tr class="even">
<td align="left"><p>STATUS_INVALID_SYSTEM_SERVICE</p></td>
<td align="left"><p>Invalid system call</p></td>
<td align="left"><p>NtStatus.h</p></td>
</tr>
<tr class="odd">
<td align="left"><p>STATUS_PORT_DISCONNECTED</p></td>
<td align="left"><p>Port disconnected</p></td>
<td align="left"><p>NtStatus.h</p></td>
</tr>
<tr class="even">
<td align="left"><p>STATUS_SINGLE_STEP</p></td>
<td align="left"><p>Single-step exception</p></td>
<td align="left"><p>NtStatus.h</p></td>
</tr>
<tr class="odd">
<td align="left"><p>STATUS_STACK_BUFFER_OVERRUN</p></td>
<td align="left"><p>Stack buffer overflow</p></td>
<td align="left"><p>NtStatus.h</p></td>
</tr>
<tr class="even">
<td align="left"><p>STATUS_STACK_OVERFLOW</p></td>
<td align="left"><p>Stack overflow</p></td>
<td align="left"><p>NtStatus.h</p></td>
</tr>
<tr class="odd">
<td align="left"><p>STATUS_VERIFIER_STOP</p></td>
<td align="left"><p>Application Verifier stop</p></td>
<td align="left"><p>NtStatus.h</p></td>
</tr>
<tr class="even">
<td align="left"><p>STATUS_WAKE_SYSTEM_DEBUGGER</p></td>
<td align="left"><p>Wake debugger</p></td>
<td align="left"><p>NtStatus.h</p></td>
</tr>
</tbody>
</table>

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Specific%20Exceptions%20%20RELEASE:%20%2811/27/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




