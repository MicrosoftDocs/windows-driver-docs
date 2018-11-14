---
title: memusage
description: The memusage extension displays summary statistics about physical memory use.
ms.assetid: 32796ada-53ee-465f-b284-db6ee5481878
keywords: ["memusage Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- memusage
api_type:
- NA
ms.localizationpriority: medium
---

# !memusage


The **!memusage** extension displays summary statistics about physical memory use.

Syntax

```dbgcmd
!memusage [Flags]
```

## <span id="ddk__memusage_dbg"></span><span id="DDK__MEMUSAGE_DBG"></span>Parameters


<span id="_______Flags______"></span><span id="_______flags______"></span><span id="_______FLAGS______"></span> *Flags*   
Can be any one of the following values. The default is 0x0.

<span id="0x0"></span><span id="0X0"></span>0x0  
Displays general summary information, along with a more detailed description of the pages in the PFN database. See the Remarks section for an example of this type of output.

<span id="0x1"></span><span id="0X1"></span>0x1  
Displays only summary information about the modified no-write pages in the PFN database..

<span id="0x2"></span><span id="0X2"></span>0x2  
Displays only detailed information about the modified no-write pages in the PFN database.

<span id="0x8"></span><span id="0X8"></span>0x8  
Displays only general summary information about memory use.

### <span id="Environment"></span><span id="environment"></span><span id="ENVIRONMENT"></span>Environment

|       |                  |
|-------|------------------|
| Modes | kernel mode only |

 

### <span id="DLL"></span><span id="dll"></span>DLL

Kdexts.dll

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

Physical memory statistics are collected from the Memory Manager's page frame number (PFN) database table.

This command takes a long time to run, especially if the target computer is running in 64-bit mode, due to the greater amount of data to obtain. While it is loading the PFN database, a counter shows its progress. To speed up this loading, increase the COM port speed with the [**CTRL+A (Toggle Baud Rate)**](ctrl-a--toggle-baud-rate-.md) key, or use the [**.cache (Set Cache Size)**](-cache--set-cache-size-.md) command to increase the cache size (perhaps to around 10 MB).

The **!memusage** command can also be used while performing [local kernel debugging](performing-local-kernel-debugging.md).

Here is an example of the output from this extension:

```dbgcmd
kd> !memusage
 loading PFN database
loading (98% complete)

Compiling memory usage data (100% Complete).
             Zeroed:     49 (   196 kb)
               Free:      5 (    20 kb)
            Standby:   5489 ( 21956 kb)
           Modified:    714 (  2856 kb)
    ModifiedNoWrite:      1 (     4 kb)
       Active/Valid:  10119 ( 40476 kb)
         Transition:      6 (    24 kb)
            Unknown:      0 (     0 kb)
              TOTAL:  16383 ( 65532 kb)

  Building kernel map
  Finished building kernel map
Scanning PFN database - (99% complete) 

  Usage Summary (in Kb):


Control Valid Standby Dirty Shared Locked PageTables  name

8251a258    12    108     0     0     0     0  mapped_file( cscui.dll )
827ab1b8     8   1708     0     0     0     0  mapped_file( $Mft )
8263c408   908     48     0     0     0     0  mapped_file( win32k.sys )
8252dda8     0    324     0     0     0     0  mapped_file( ShellIconCache )
8272f638   128    112     0   116     0     0  mapped_file( advapi32.dll )
......
82755958     0      4     0     0     0     0  mapped_file( $Directory )
8250b518     0      4     0     0     0     0    No Name for File
8254d8d8     0      4     0     0     0     0  mapped_file( $Directory )
82537be8     0      4     0     0     0     0  mapped_file( Windows Explorer.lnk )

--------  1348      0     0 ----- -----   904  process ( System )
--------   492      0     0 ----- -----    72  process ( winmine.exe )
--------  3364   1384  1396 ----- -----   188  process ( explorer.exe )
--------   972      0     0 ----- -----    88  process ( services.exe )
--------   496   1456   384 ----- -----   164  process ( winmgmt.exe )
--------  1144      0     0 ----- -----   120  process ( svchost.exe )
--------   944      0     0 ----- -----   156  process ( winlogon.exe )
--------   412      0     0 ----- -----    64  process ( csrss.exe )
......
--------    12      0     0 ----- -----     8  process ( wmiadap.exe )

--------   316      0     0 ----- -----     0  pagefile section (346e)
--------  4096      0     0 ----- -----     0  pagefile section (9ad)

--------   884    280    36 -----     0 -----  driver ( ntoskrnl.exe )
--------    88      8     0 -----     0 -----  driver ( hal.dll )
--------     8      0     0 -----     0 -----  driver ( kdcom.dll )
--------    12      0     0 -----     0 -----  driver ( BOOTVID.dll )
......
--------     8      0     0 -----     0 -----  driver ( ndisuio.sys )
--------    16      0     0 -----     0 -----  driver ( dump_scsiport.sys )
--------    56      0     0 -----     0 -----  driver ( dump_aic78xx.sys )
--------  2756   1060   876 -----     0 -----  driver ( Paged Pool )
--------  1936    128   148 -----     0 -----  driver ( Kernel Stacks )
--------     0      0     0 -----     0 -----  driver ( NonPaged Pool )
```

The first column displays the address of the control area structure that describes each mapped structure. Use the [**!ca**](-ca.md) extension command to display these control areas.

Remarks
-------

You can use the [**!vm**](-vm.md) extension command to analyze virtual memory use. This extension is typically more useful than **!memusage**. For more information about memory management, see *Microsoft Windows Internals*, by Mark Russinovich and David Solomon. (This book may not be available in some languages and countries.)

The [**!pfn**](-pfn.md) extension command can be used to display a particular page frame entry in the PFN database.

 

 





