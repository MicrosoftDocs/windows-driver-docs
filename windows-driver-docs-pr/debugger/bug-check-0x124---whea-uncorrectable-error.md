---
title: Bug Check 0x124 WHEA_UNCORRECTABLE_ERROR
description: The WHEA_UNCORRECTABLE_ERROR bug check has a value of 0x00000124. This bug check indicates that a fatal hardware error has occurred. 
ms.assetid: b3b7c6dd-3891-4ccb-96d1-49e8a2de34c8
keywords: ["Bug Check 0x124 WHEA_UNCORRECTABLE_ERROR", "WHEA_UNCORRECTABLE_ERROR"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- WHEA_UNCORRECTABLE_ERROR
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0x124: WHEA\_UNCORRECTABLE\_ERROR


The WHEA\_UNCORRECTABLE\_ERROR bug check has a value of 0x00000124. This bug check indicates that a fatal hardware error has occurred. This bug check uses the error data that is provided by the Windows Hardware Error Architecture (WHEA).

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## WHEA\_UNCORRECTABLE\_ERROR Parameters


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
<th align="left">Cause of error</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>0x0</p></td>
<td align="left"><p>Address of WHEA_ERROR_RECORD structure.</p></td>
<td align="left"><p>High 32 bits of MCi_STATUS MSR for the MCA bank that had the error.</p></td>
<td align="left"><p>Low 32 bits of MCi_STATUS MSR for the MCA bank that had the error.</p></td>
<td align="left"><p>A machine check exception occurred.</p>
<p>These parameter descriptions apply if the processor is based on the x64 architecture, or the x86 architecture that has the MCA feature available (for example, Intel Pentium Pro, Pentium IV, or Xeon).</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x1</p></td>
<td align="left"><p>Address of WHEA_ERROR_RECORD structure.</p></td>
<td align="left"><p>Reserved.</p></td>
<td align="left"><p>Reserved.</p></td>
<td align="left"><p>A corrected machine check exception occurred.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x2</p></td>
<td align="left"><p>Address of WHEA_ERROR_RECORD structure.</p></td>
<td align="left"><p>Reserved.</p></td>
<td align="left"><p>Reserved.</p></td>
<td align="left"><p>A corrected platform error occurred.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x3</p></td>
<td align="left"><p>Address of WHEA_ERROR_RECORD structure.</p></td>
<td align="left"><p>Reserved.</p></td>
<td align="left"><p>Reserved.</p></td>
<td align="left"><p>A nonmaskable Interrupt (NMI) error occurred.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x4</p></td>
<td align="left"><p>Address of WHEA_ERROR_RECORD structure.</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>Reserved.</p></td>
<td align="left"><p>An uncorrectable PCI Express error occurred.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x5</p></td>
<td align="left"><p>Address of WHEA_ERROR_RECORD structure.</p></td>
<td align="left"><p>Reserved.</p></td>
<td align="left"><p>Reserved.</p></td>
<td align="left"><p>A generic hardware error occurred.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x6</p></td>
<td align="left"><p>Address of WHEA_ERROR_RECORD structure</p></td>
<td align="left"><p>Reserved.</p></td>
<td align="left"><p>Reserved.</p></td>
<td align="left"><p>An initialization error occurred.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x7</p></td>
<td align="left"><p>Address of WHEA_ERROR_RECORD structure.</p></td>
<td align="left"><p>Reserved.</p></td>
<td align="left"><p>Reserved.</p></td>
<td align="left"><p>A BOOT error occurred.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x8</p></td>
<td align="left"><p>Address of WHEA_ERROR_RECORD structure</p></td>
<td align="left"><p>Reserved.</p></td>
<td align="left"><p>Reserved.</p></td>
<td align="left"><p>A Scalable Coherent Interface (SCI) generic error occurred.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x9</p></td>
<td align="left"><p>Address of WHEA_ERROR_RECORD structure.</p></td>
<td align="left"><p>Length, in bytes, of the SAL log.</p></td>
<td align="left"><p>Address of the SAL log.</p></td>
<td align="left"><p>An uncorrectable Itanium-based machine check abort error occurred.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0xA</p></td>
<td align="left"><p>Address of WHEA_ERROR_RECORD structure</p></td>
<td align="left"><p>Reserved.</p></td>
<td align="left"><p>Reserved.</p></td>
<td align="left"><p>A corrected Itanium-based machine check error occurred.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0xB</p></td>
<td align="left"><p>Address of WHEA_ERROR_RECORD structure.</p></td>
<td align="left"><p>Reserved.</p></td>
<td align="left"><p>Reserved.</p></td>
<td align="left"><p>A corrected Itanium platform error occurred.</p></td>
</tr>
</tbody>
</table>

 

Cause
-----

This bug check is typically related to physical hardware failures. It can be heat related, defective hardware, memory or even a processor that is beginning to fail or has failed. If over-clocking has been enabled, try disabling it. Confirm that any cooling systems such as fans are functional. Run system diagnostics to confirm that the system memory is not defective. It is less likely, but possible that a driver is causing the hardware to fail with this bug check.

For additional general bug check troubleshooting information, see [**Blue Screen Data**](blue-screen-data.md).

Remarks
-------

The [**!analyze**](-analyze.md) debug extension displays information about the bug check and can be very helpful in determining the root cause.

Parameter 1 identifies the type of error source that reported the error. Parameter 2 holds the address of the WHEA\_ERROR\_RECORD structure that describes the error condition.

When a hardware error occurs, WHEA creates an error record to store the error information associated with the hardware error condition. Each error record is described by a WHEA\_ERROR\_RECORD structure. The Windows kernel includes the error record with the Event Tracing for Windows (ETW) hardware error event that it raises in response to the error so that the error record is saved in the system event log. The format of the error records that are used by WHEA are based on the Common Platform Error Record as described in Appendix N of version 2.2 of the Unified Extensible Firmware Interface (UEFI) Specification. For more information, see [WHEA\_ERROR\_RECORD](https://msdn.microsoft.com/library/windows/hardware/ff560483) and [Windows Hardware Error Architecture (WHEA)](https://msdn.microsoft.com/library/windows/hardware/ff559509).

You can use [**!errrec**](-errrec.md) &lt;addr&gt; to display the WHEA\_ERROR\_RECORD structure using the address provided in Parameter 2. The [**!whea**](-whea.md) and [**!errpkt**](-errpkt.md) extensions can be used to display additional WHEA information.

For more information see the following topics:

[Crash dump analysis using the Windows debuggers (WinDbg)](crash-dump-files.md)

[Analyzing a Kernel-Mode Dump File with WinDbg](analyzing-a-kernel-mode-dump-file-with-windbg.md)

[Using the !analyze Extension](using-the--analyze-extension.md) and [!analyze](-analyze.md)

This bug check is not supported in Windows versions prior to Windows Vista. Instead, machine check exceptions are reported through [**bug check 0x9C**](bug-check-0x9c--machine-check-exception.md).

 

 




