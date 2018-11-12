---
title: sysinfo
description: The sysinfo extension reads and displays specified SMBIOS, Advanced Configuration and Power Interface (ACPI), and CPU information from a dump file or live system.
ms.assetid: 1637fcc8-54ff-46a4-94f4-0b2df38507d1
keywords: ["sysinfo Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- sysinfo
api_type:
- NA
ms.localizationpriority: medium
---

# !sysinfo


The **!sysinfo** extension reads and displays specified SMBIOS, Advanced Configuration and Power Interface (ACPI), and CPU information from a dump file or live system.

```dbgcmd
!sysinfo cpuinfo [-csv [-noheaders]]
!sysinfo cpumicrocode [-csv [-noheaders]]
!sysinfo cpuspeed [-csv [-noheaders]]
!sysinfo gbl [-csv [-noheaders]]
!sysinfo machineid [-csv [-noheaders]]
!sysinfo registers
!sysinfo smbios [-csv [-noheaders]] {-debug | -devices | -memory | -power | -processor | -system | -v} 
!sysinfo -?
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______cpuinfo______"></span><span id="_______CPUINFO______"></span> **cpuinfo**   
Displays information about the processor.

<span id="_______cpumicrocode______"></span><span id="_______CPUMICROCODE______"></span> **cpumicrocode**   
(GenuineIntel processors only) Displays the initial and cached microcode processor versions.

<span id="_______cpuspeed______"></span><span id="_______CPUSPEED______"></span> **cpuspeed**   
Displays the maximum and current processor speeds.

<span id="_______gbl______"></span><span id="_______GBL______"></span> **gbl**   
Displays the BIOS list of ACPI tables.

<span id="_______machineid______"></span><span id="_______MACHINEID______"></span> **machineid**   
Displays machine ID information for the SMBIOS, BIOS, firmware, system, and baseboard.

<span id="_______registers______"></span><span id="_______REGISTERS______"></span> **registers**   
Displays machine-specific registers (MSRs).

<span id="_______smbios______"></span><span id="_______SMBIOS______"></span> **smbios**   
Displays the SMBIOS table.

<span id="_______-csv______"></span><span id="_______-CSV______"></span> **-csv**   
Displays all data in comma-separated, variable-length (CSV) format.

<span id="_______-noheaders______"></span><span id="_______-NOHEADERS______"></span> **-noheaders**   
Suppresses the header for the CSV format.

<span id="_______-debug______"></span><span id="_______-DEBUG______"></span> **-debug**   
Displays output in standard format and CSV format.

<span id="_______-devices______"></span><span id="_______-DEVICES______"></span> **-devices**   
Displays the device entries in the SMBIOS table.

<span id="_______-memory______"></span><span id="_______-MEMORY______"></span> **-memory**   
Displays the memory entries in the SMBIOS table.

<span id="_______-power______"></span><span id="_______-POWER______"></span> **-power**   
Displays the power entries in the SMBIOS table.

<span id="_______-processor______"></span><span id="_______-PROCESSOR______"></span> **-processor**   
Displays the processor entries in the SMBIOS table.

<span id="_______-system______"></span><span id="_______-SYSTEM______"></span> **-system**   
Displays the system entries in the SMBIOS table.

<span id="_______-v______"></span><span id="_______-V______"></span> **-v**   
Verbose. Displays the details of entries in the SMBIOS table.

<span id="_______-_______"></span> **-?**   
Displays help for this extension in the Debugger Command window.

### <span id="DLL"></span><span id="dll"></span>DLL

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Windows 2000</strong></p></td>
<td align="left"><p>Unavailable</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Windows XP base system</strong></p>
<p><strong>Windows 2003 base system</strong></p></td>
<td align="left"><p>Unavailable</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Windows XP, Service Pack 2 and later</strong></p>
<p><strong>Windows 2003, Service Pack 1 and later</strong></p></td>
<td align="left"><p>Kdexts.dll</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

This extension is useful only when the dump file is a System Crash File (.dmp) that has not been converted to a minidump file from a kernel or full dump file, or the live system has finished starting and is online (for example, at the log-in prompt).

You can use any combination of the **-debug**, **-devices**, **-memory**, **-power**, **-processor**, **-system**, and **-v** parameters in a single extension command.

The following parameters are supported only on particular systems:

-   The **gbl** parameter works only when the target computer supports ACPI.

-   The **smbios** parameter works only when the target computer supports SMBIOS.

-   The **registers** parameter does not work on Itanium-based target computers, because they do not collect MSRs.

Microsoft makes every effort to remove personally identifiable information (PII) from these records. All PII is removed from dump files. However, on a live system, some PII may not yet be removed. As a result, PII fields will be reported as 0 or blank, even if they actually contain information.

To stop execution of commands that include the **cpuinfo**, **gbl**, **registers**, or **smbios** parameters at any time, press CTRL+BREAK (in WinDbg) or CTRL+C (in KD).

 

 





