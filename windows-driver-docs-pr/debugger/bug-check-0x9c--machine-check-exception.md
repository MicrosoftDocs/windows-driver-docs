---
title: Bug Check 0x9C MACHINE_CHECK_EXCEPTION
description: The MACHINE_CHECK_EXCEPTION bug check has a value of 0x0000009C. This bug check indicates that a fatal machine check exception has occurred.
ms.assetid: b8945dba-c515-4a30-a36c-ef4feaadabbe
keywords: ["Bug Check 0x9C MACHINE_CHECK_EXCEPTION", "MACHINE_CHECK_EXCEPTION"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- MACHINE_CHECK_EXCEPTION
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0x9C: MACHINE\_CHECK\_EXCEPTION


The MACHINE\_CHECK\_EXCEPTION bug check has a value of 0x0000009C. This bug check indicates that a fatal machine check exception has occurred.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## MACHINE\_CHECK\_EXCEPTION Parameters


The four parameters that are listed in the message have different meanings, depending on the processor type.

If the processor is based on an older x86-based architecture and has the Machine Check Exception (MCE) feature but not the Machine Check Architecture (MCA) feature (for example, the Intel Pentium processor), the parameters have the following meaning.

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
<td align="left"><p>The low 32 bits of P5_MC_TYPE Machine Service Report (MSR)</p></td>
</tr>
<tr class="even">
<td align="left"><p>2</p></td>
<td align="left"><p>The address of the MCA_EXCEPTION structure</p></td>
</tr>
<tr class="odd">
<td align="left"><p>3</p></td>
<td align="left"><p>The high 32 bits of P5_MC_ADDR MSR</p></td>
</tr>
<tr class="even">
<td align="left"><p>4</p></td>
<td align="left"><p>The low 32 bits of P5_MC_ADDR MSR</p></td>
</tr>
</tbody>
</table>

 

If the processor is based on a newer x86-based architecture and has the MCA feature and the MCE feature (for example, any Intel Processor of family 6 or higher, such as Pentium Pro, Pentium IV, or Xeon), or if the processor is an x64-based processor, the parameters have the following meaning.

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
<td align="left"><p>The bank number</p></td>
</tr>
<tr class="even">
<td align="left"><p>2</p></td>
<td align="left"><p>The address of the MCA_EXCEPTION structure</p></td>
</tr>
<tr class="odd">
<td align="left"><p>3</p></td>
<td align="left"><p>The high 32 bits of MCi_STATUS MSR for the MCA bank that had the error</p></td>
</tr>
<tr class="even">
<td align="left"><p>4</p></td>
<td align="left"><p>The low 32 bits of MCi_STATUS MSR for the MCA bank that had the error</p></td>
</tr>
</tbody>
</table>

 

On an Itanium-based processor, the parameters have the following meaning.

**Note**  Parameter 1 indicates the type of violation.

 

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
<td align="left"><p>The address of the log</p></td>
<td align="left"><p>The size of the log</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p></p></td>
</tr>
<tr class="even">
<td align="left"><p>0x2</p></td>
<td align="left"><p>The address of the log</p></td>
<td align="left"><p>The size of the log</p></td>
<td align="left"><p>The error code</p></td>
<td align="left"><p>The system abstraction layer (SAL) returned an error for SAL_GET_STATEINFO while processing MCA.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x3</p></td>
<td align="left"><p>The address of the log</p></td>
<td align="left"><p>The size of the log</p></td>
<td align="left"><p>The error code</p></td>
<td align="left"><p>SAL returned an error for SAL_CLEAR_STATEINFO while it processed MCA.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x4</p></td>
<td align="left"><p>The address of the log</p></td>
<td align="left"><p>The size of the log</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>Firmware (FW) reported a fatal MCA.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x5</p></td>
<td align="left"><p>The address of the log</p></td>
<td align="left"><p>The size of the log</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>There are two possible causes:</p>
<ul>
<li><p>SAL reported a recoverable MCA, but this recovery is not currently supported.</p></li>
<li><p>SAL generated an MCA but could not produce an error record.</p></li>
</ul></td>
</tr>
<tr class="even">
<td align="left"><p>0xB</p></td>
<td align="left"><p>The address of the log</p></td>
<td align="left"><p>The size of the log</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p></p></td>
</tr>
<tr class="odd">
<td align="left"><p>0xC</p></td>
<td align="left"><p>The address of the log</p></td>
<td align="left"><p>The size of the log</p></td>
<td align="left"><p>The error code</p></td>
<td align="left"><p>SAL returned an error for SAL_GET_STATEINFO while processing an INIT event.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0xD</p></td>
<td align="left"><p>The address of the log</p></td>
<td align="left"><p>The size of the log</p></td>
<td align="left"><p>The error code</p></td>
<td align="left"><p>SAL returned an error for SAL_CLEAR_STATEINFO while it processed an INIT event.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0xE</p></td>
<td align="left"><p>The address of the log</p></td>
<td align="left"><p>The size of the log</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p></p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

In Windows Vista and later operating systems, this bug check occurs only in the following circumstances.

-   WHEA is not fully initialized.
-   All processors that rendezvous have no errors in their registers.

For other circumstances, this bug check has been replaced with [**bug Check 0x124: WHEA\_UNCORRECTABLE\_ERROR**](bug-check-0x124---whea-uncorrectable-error.md) in Windows Vista and later operating systems.

For more information about Machine Check Architecture (MCA), see the Intel or AMD Web sites.

 

 




