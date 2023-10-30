---
title: poolused (WinDbg)
description: The poolused extension displays memory use summaries, based on the tag used for each pool allocation.
keywords: ["poolused Windows Debugging"]
ms.date: 08/29/2023
topic_type:
- apiref
ms.topic: reference
api_name:
- poolused
api_type:
- NA
---

# !poolused

The **!poolused** extension displays memory use summaries, based on the tag used for each pool allocation.

```dbgcmd
!poolused [Flags [TagString]] 
```

## Parameters

*Flags* 

Specifies the amount of output to be displayed and the method of sorting the output. This can be any combination of the following bit values, except that bits 1 (0x2) and 2 (0x4) cannot be used together. The default is 0x0, which produces summary information, sorted by pool tag.

Bit 0 (0x1)  

Displays more detailed (verbose) information.

Bit 1 (0x2)  

Sorts the display by the amount of nonpaged memory use.

Bit 2 (0x4)  

Sorts the display by the amount of paged memory use.

Bit 3 (0x8)  

Displays the session pool instead of the standard pool. You can use the [**!session**](-session.md) command to switch between sessions.


*TagString*

Specifies the pool tag. *TagString* is a case-sensitive ASCII string. The asterisk (\*) can be used to represent any number of characters; the question mark (?) can be used to represent exactly one character. Unless an asterisk is used, *TagString* must be exactly four characters in length.

### DLL

Kdexts.dll


### Additional Information

For information about memory pools and pool tags, see *Microsoft Windows Internals*, by Mark Russinovich and David Solomon.

## Remarks

The **!poolused** extension gathers data from the pool tagging feature of Windows. Pool tagging is permanently enabled on Windows Server 2003 and later versions of Windows.

If you stop executing the extension before it completes, the debugger displays partial results.

The display for this command shows the memory use for each tag in paged pool and nonpaged pool. In both cases, the display includes the number of currently outstanding allocations for the given tag and the number of bytes being consumed by those allocations.

Here is a partial example of the output from this extension:

```dbgcmd
0: kd> !poolused
   Sorting by  Tag

  Pool Used:
            NonPaged            Paged
 Tag    Allocs     Used    Allocs     Used
 1394        1      520         0        0UNKNOWN pooltag '1394', please update pooltag.txt
 1MEM        1     3368         0        0UNKNOWN pooltag '1MEM', please update pooltag.txt
 2MEM        1     3944         0        0UNKNOWN pooltag '2MEM', please update pooltag.txt
 3MEM        3      248         0        0UNKNOWN pooltag '3MEM', please update pooltag.txt
 8042        4     3944         0        0PS/2 kb and mouse , Binary: i8042prt.sys
 AGP         1      344         2      384UNKNOWN pooltag 'AGP ', please update pooltag.txt
 AcdN        2     1072         0        0TDI AcdObjectInfoG 
 AcpA        3      192         1      504ACPI Pooltags , Binary: acpi.sys
 AcpB        0        0         4      576ACPI Pooltags , Binary: acpi.sys
 AcpD       40    13280         0        0ACPI Pooltags , Binary: acpi.sys
 AcpF        6      240         0        0ACPI Pooltags , Binary: acpi.sys
 AcpM        0        0         1      128ACPI Pooltags , Binary: acpi.sys
 AcpO        4      208         0        0ACPI Pooltags , Binary: acpi.sys

...

 WmiG       30     6960         0        0Allocation of WMIGUID 
 WmiR       63     4032         0        0Wmi Registration info blocks 
 Wmip      146     3504       182    18600Wmi General purpose allocation 
 Wmit        1     4096         7    49480Wmi Trace 
 Wrpa        2      720         0        0WAN_ADAPTER_TAG 
 Wrpc        1       72         0        0WAN_CONN_TAG 
 Wrpi        1      120         0        0WAN_INTERFACE_TAG 
 Wrps        2      128         0        0WAN_STRING_TAG 
 aEoP        1      672         0        0UNKNOWN pooltag 'aEoP', please update pooltag.txt
 fEoP        1       16         0        0UNKNOWN pooltag 'fEoP', please update pooltag.txt
 hSVD        0        0         1       40Shared Heap Tag , Binary: mrxdav.sys
 hibr        0        0         1    24576UNKNOWN pooltag 'hibr', please update pooltag.txt
 iEoP        1       24         0        0UNKNOWN pooltag 'iEoP', please update pooltag.txt
 idle        2      208         0        0Power Manager idle handler 
 jEoP        1       24         0        0UNKNOWN pooltag 'jEoP', please update pooltag.txt
 mEoP        1       88         0        0UNKNOWN pooltag 'mEoP', please update pooltag.txt
 ohci        1      136         0        01394 OHCI host controller driver 
 rx..       3     1248         0        0UNKNOWN pooltag '  rx', please update pooltag.txt
 sidg        2       48         0        0GDI spooler events 
 thdd        0        0         1    20480DirectDraw/3D handle manager table 
 usbp       18    77056         2       96UNKNOWN pooltag 'usbp', please update pooltag.txt
 vPrt        0        0        18    68160UNKNOWN pooltag 'vPrt', please update pooltag.txt
 TOTAL     3570214 209120008     38769 13066104
```
