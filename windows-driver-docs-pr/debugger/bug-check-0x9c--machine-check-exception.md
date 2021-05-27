---
title: Bug Check 0x9C MACHINE_CHECK_EXCEPTION
description: The MACHINE_CHECK_EXCEPTION bug check has a value of 0x0000009C. This bug check indicates that a fatal machine check exception has occurred.
keywords: ["Bug Check 0x9C MACHINE_CHECK_EXCEPTION", "MACHINE_CHECK_EXCEPTION"]
ms.date: 05/13/2020
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

> [!IMPORTANT]
> This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://www.windows.com/stopcode).


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


## Remarks

This bug check occurs only in the following circumstances.

-   WHEA is not fully initialized.
-   All processors that rendezvous have no errors in their registers.

For other circumstances, this bug check has been replaced with [**bug Check 0x124: WHEA\_UNCORRECTABLE\_ERROR**](bug-check-0x124---whea-uncorrectable-error.md) in Windows Vista and later operating systems.

For more information about Machine Check Architecture (MCA), see the Intel or AMD Web sites.

 

 




