---
title: memusage (WinDbg)
description: The memusage extension displays summary statistics about physical memory use.
keywords: ["memusage Windows Debugging"]
ms.date: 12/11/2023
topic_type:
- apiref
ms.topic: reference
api_name:
- memusage
api_type:
- NA
---

# !memusage

The **!memusage** extension displays summary statistics about physical memory use.

Syntax

`!memusage [Flags]`

## <span id="ddk__memusage_dbg"></span><span id="DDK__MEMUSAGE_DBG"></span>Parameters


<span id="_______Flags______"></span><span id="_______flags______"></span><span id="_______FLAGS______"></span> *Flags*   
Can be any one of the following values. The default is 0x0.

<span id="0x0"></span><span id="0X0"></span>0x0  
Displays general summary information, along with a more detailed description of the pages in the PFN database. See the Remarks section for an example of this type of output.

<span id="0x1"></span><span id="0X1"></span>0x1  
Displays only summary information about the modified no-write pages in the PFN database.

<span id="0x2"></span><span id="0X2"></span>0x2  
Displays only detailed information about the modified no-write pages in the PFN database.

<span id="0x8"></span><span id="0X8"></span>0x8  
Displays only general summary information about memory use.

### Environment

**Modes**: kernel mode only

## DLL

Kdexts.dll

### Additional Information

Physical memory statistics are collected from the Memory Manager's page frame number (PFN) database table.

This command takes a long time to run, especially if the target computer is running in 64-bit mode, due to the greater amount of data to obtain. While it is loading the PFN database, a counter shows its progress. To speed up this loading, use a network connection, or increase the COM port speed with the [**CTRL+A (Toggle Baud Rate)**](../debugger/ctrl-a--toggle-baud-rate-.md) key, or use the [**.cache (Set Cache Size)**](-cache--set-cache-size-.md) command to increase the cache size (perhaps to around 10 MB).

The **!memusage** command can also be used while performing [local kernel debugging](../debugger/performing-local-kernel-debugging.md).

Here is an example of the output from this extension:

```dbgcmd
kd> !memusage
loading PFN database
loading (100% complete)
Compiling memory usage data (99% Complete).
             Zeroed:      218 (     872 kb)
               Free:      831 (    3324 kb)
            Standby:   124049 (  496196 kb)
           Modified:    55101 (  220404 kb)
    ModifiedNoWrite:       58 (     232 kb)
       Active/Valid:   321846 ( 1287384 kb)
         Transition:        8 (      32 kb)
         SLIST/Temp:     1533 (    6132 kb)
                Bad:        0 (       0 kb)
            Unknown:        0 (       0 kb)
              TOTAL:   503644 ( 2014576 kb)

Dangling Yes Commit:      184 (     736 kb)
 Dangling No Commit:    81706 (  326824 kb)
  Building kernel map
  Finished building kernel map
Scanning PFN database - (100% complete) 

...

```

Also included in the report is detailed information about the usage of memory that is visible to the debugger.

```dbgcmd
  Usage Summary (in Kb):
Control       Valid Standby Dirty Shared Locked PageTables  name
ffffaf0fb369f010   204    956     0    32   204     0  mapped_file( shell32.dll )
ffffaf0fb369f270   492     60     0   252   492     0  mapped_file( KernelBase.dll )
ffffaf0fb36ad050    20     36     0     0    20     0  mapped_file( WMIsvc.dll )
ffffaf0fb36adad0    88    144     0    40    88     0  mapped_file( Can't read file name buffer at ffffc10e0497e170 )
ffffaf0fb36b5670   780   1012     0   560   780     0  mapped_file( KernelBase.dll )
ffffaf0fb36b5910    44    144     0    28    44     0  mapped_file( cfgmgr32.dll )
ffffaf0fb36bc270     8      0     0     0     8     0  mapped_file( Can't read file name buffer at ffffc10e061a17d0 )
ffffaf0fb36bc520    24     56     0     4    24     0  mapped_file( ShareHost.dll )

...

```

The first column displays the address of the control area structure that describes each mapped structure. Use the [**!ca**](-ca.md) extension command to display these control areas.

## Remarks

You can use the [**!vm**](-vm.md) extension command to analyze virtual memory use. This extension is typically more useful than **!memusage**. For more information about memory management, see *Microsoft Windows Internals*, by Pavel Yosifovich, Andrea Allievi, Alex Ionescu, Mark Russinovich and David Solomon.

The [**!pfn**](-pfn.md) extension command can be used to display a particular page frame entry in the PFN database.

The [**!pool**](-pool.md) extension displays information about a specific pool allocation or about the entire system-wide pool.
