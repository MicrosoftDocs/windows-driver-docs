---
title: /pae
description: The /pae parameter enables Physical Address Extension (PAE).
ms.assetid: 15ddeb45-9a18-45fc-82ab-97e7c311e178
keywords: ["/pae Driver Development Tools"]
topic_type:
- apiref
api_name:
- /pae
api_type:
- NA
---

/pae
====

The **/pae** parameter enables Physical Address Extension (PAE). This parameter directs the system to load the PAE version of the Windows kernel.

For more information about using the **/pae** parameter and the other parameters that affect PAE configuration, see [Boot Parameters to Configure DEP and PAE](https://msdn.microsoft.com/library/windows/hardware/ff542275).

``` syntax
    /pae 

   
```

### Comments

The **/pae** parameter is supported only on Windows Server 2003, Windows XP, and Windows 2000. On Windows Vista and later versions of Windows, use the **PAE** element with the [**BCDEdit /set**](bcdedit--set.md) command.

PAE is an addressing strategy that uses a page-translation hierarchy to enable systems with 32-bit addressing to address more than 4 GB of physical memory. PAE also supports several advanced system and processor features, such as Data Execution Prevention (DEP; "No execute"), Non-Uniform Memory Architecture (NUMA), and hot-add memory, so it is also used on computers with less than 4 GB of memory. PAE must be supported by the processor and by the operating system.

PAE is supported beginning with the Windows 2000 operating system.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Operating system</th>
<th align="left">Maximum memory support with PAE</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Windows 2000 Advanced Server</p></td>
<td align="left"><p>8 GB of physical RAM</p></td>
</tr>
<tr class="even">
<td align="left"><p>Windows 2000 Datacenter Server</p></td>
<td align="left"><p>32 GB of physical RAM</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Windows XP (all versions)</p></td>
<td align="left"><p>4 GB of physical RAM*</p></td>
</tr>
<tr class="even">
<td align="left"><p>Windows Server 2003 (and SP1), Standard Edition</p></td>
<td align="left"><p>4 GB of physical RAM*</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Windows Server 2003, Enterprise Edition</p></td>
<td align="left"><p>64 GB of physical RAM</p></td>
</tr>
<tr class="even">
<td align="left"><p>Windows Server 2003, Datacenter Edition</p></td>
<td align="left"><p>64 GB of physical RAM</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Windows Server 2003 SP1, Enterprise Edition</p></td>
<td align="left"><p>64 GB of physical RAM</p></td>
</tr>
<tr class="even">
<td align="left"><p>Windows Server 2003 SP1, Datacenter Edition</p></td>
<td align="left"><p>128 GB of physical RAM</p></td>
</tr>
</tbody>
</table>

 

\* Total physical address space is limited to 4 GB on these versions of Windows. When 4 GB of memory is installed and PAE is enabled, the amount of available memory could be less than what you would expect. For more information about memory usage, see article Q888137, ["The amount of RAM reported by the System Properties dialog box and the System Information tool is less than you expect after you install Windows XP Service Pack 2"](http://go.microsoft.com/fwlink/p/?linkid=3100&amp;ID=888137) in the Microsoft Knowledge Base.

The **/pae** parameter is valid only on boot entries for 32-bit versions of Windows that run on computers with x86 and x64-based processors. On 32-bit versions of Windows, PAE is disabled by default. You must use the **/pae** boot parameter to enable PAE.

However, Windows automatically enables PAE when the computer is configured for hot-add memory devices in memory ranges beyond the 4 GB region, as defined by the Static Resource Affinity Table (SRAT). *Hot-add memory* supports memory devices that you can add without rebooting or turning off the computer. In this case, because PAE must be enabled when the system starts, it is enabled automatically so that the system can immediately address extended memory that is added between restarts. Hot-add memory is supported only on Windows Server 2003, Datacenter Edition; Windows Server 2003, Enterprise Edition; Windows Server 2008, Datacenter Edition; Windows Server 2008 for Itanium-Based Systems; and on the datacenter and enterprise editions of all later versions of Windows Server. Moreover, for versions of Windows prior to Windows Server 2008, hot-add memory is supported only on computers with an ACPI BIOS, an x86 processor, and specialized hardware. For Windows Server 2008 and later versions of Windows Server, it is supported for all processor architectures.

On a computer that supports hardware-enabled Data Execution Prevention (DEP) and is running a 32-bit version of the Windows operating system that supports DEP, PAE is automatically enabled when DEP is enabled and, on all 32-bit versions of the Windows operating system, except Windows Server 2003 with SP1, PAE is disabled when you disable DEP. To enable PAE when DEP is disabled, you must enable PAE explicitly, by using **/noexecute=alwaysoff /pae**. For more information about DEP, see [**/noexecute**](-noexecute.md) and [**/execute**](-execute.md).

PAE is required to support Cache Coherent Non-Uniform Memory Architecture (known as ccNUMA or NUMA) on computers with x86 processors, although Windows can run in non-NUMA mode on NUMA-capable computers without PAE. Even when it is required, PAE is not enabled automatically. NUMA is supported in all editions of Windows XP and Windows Vista, and in the Enterprise and Datacenter editions of Windows Server 2003.

### Example

```
multi(0)disk(0)rdisk(0)partition(1)\WINDOWS="Windows Server 2003, Enterprise" /fastdetect /pae
```

### Bootcfg command

```
bootcfg /raw "/pae" /A /ID 1
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevtest\devtest%5D:%20/pae%20%20RELEASE:%20%281/17/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




