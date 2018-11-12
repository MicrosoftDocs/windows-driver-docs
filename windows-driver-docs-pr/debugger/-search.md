---
title: search
description: The search extension searches pages in physical memory for pointer-sized data that matches the specified criteria.
ms.assetid: 5f9d4e50-c389-4309-8851-0f5069b1b66e
keywords: ["search Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- search
api_type:
- NA
ms.localizationpriority: medium
---

# !search


The **!search** extension searches pages in physical memory for pointer-sized data that matches the specified criteria.

Syntax

```dbgcmd
!search [-s] [-p] Data [ Delta [ StartPFN [ EndPFN ]]] 
!search -?
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______-s______"></span><span id="_______-S______"></span> **-s**   
Causes symbol check errors to be ignored during the search. This is useful if you are getting too many "incorrect symbols for kernel" errors.

<span id="_______-p______"></span><span id="_______-P______"></span> **-p**   
Causes the value of *Data* to be interpreted as a 32-bit value, preventing any sign extension.

<span id="_______Data______"></span><span id="_______data______"></span><span id="_______DATA______"></span> *Data*   
Specifies the data to search for. *Data* must be the size of a pointer on the target system (32 bits or 64 bits). An exact match for the value of *Data* is always displayed. Other matches are displayed as well, depending on the value of *Delta*; see the Remarks section below for details.

<span id="_______Delta______"></span><span id="_______delta______"></span><span id="_______DELTA______"></span> *Delta*   
Specifies the allowable difference between a value in memory and the value of *Data*. See the Remarks section below for details.

<span id="_______StartPFN______"></span><span id="_______startpfn______"></span><span id="_______STARTPFN______"></span> *StartPFN*   
Specifies the page frame number (PFN) of the beginning of the range to be searched. If this is omitted, the search begins at the lowest physical page.

<span id="_______EndPFN______"></span><span id="_______endpfn______"></span><span id="_______ENDPFN______"></span> *EndPFN*   
Specifies the page frame number (PFN) of the end of the range to be searched. If this is omitted, the search ends at the highest physical page.

<span id="_______-_______"></span> **-?**   
Displays help for this extension in the Debugger Command window.

### <span id="DLL"></span><span id="dll"></span>DLL

Kdexts.dll

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For more ways to display and search physical memory, see [Reading and Writing Memory](reading-and-writing-memory.md).

Remarks
-------

If *StartPFN* and *EndPFN* are specified, these are taken as the page frame numbers of the beginning and end of the range in physical memory to be searched. For an explanation of page frame numbers, see [Converting Virtual Addresses to Physical Addresses](converting-virtual-addresses-to-physical-addresses.md). If *StartPFN* and *EndPFN* are omitted, all physical memory is searched.

All hits are displayed.

The **!search** extension will search through all memory for in the specified page range and examine each ULONG\_PTR-aligned value. Values that satisfy at least one of the following criteria are displayed:

-   The value matches *Data* exactly.

-   If Delta is 0 or omitted: The value differs from *Data* by a single bit.

-   If Delta is nonzero: The value differs from *Data* by at most *Delta*. In other words, the value lies in the range \[Data - Delta, Data + Delta\].

-   If Delta is nonzero: The value differs from the lowest number in the range (Data - Delta) by a single bit.

In most cases, *Data* will specify an address you are interested in, but any ULONG\_PTR sized data can be specified.

Because the debugger's search engine structures reside in memory on the target computer, if you search all of memory (or any range containing these structures) you will see matches in the area where the structures themselves are located. If you need to eliminate these matches, do a search for a random value; this will indicate where the debugger's search structures are located.

Here are some examples. The following will search the memory page with PFN 0x237D for values between 0x80001230 and 0x80001238, inclusive:

```dbgcmd
kd> !search 80001234 4 237d 237d 
```

The following will search the memory pages ranging from PFN 0x2370 to 0x237F for values that are within one bit of 0x0F100F0F. The exact matches are indicated in bold; the others are off by one bit:

```dbgcmd
kd> !search 0f100f0f 0 2370 237f
Searching PFNs in range 00002370 - 0000237F for [0F100F0F - 0F100F0F]

Pfn      Offset   Hit      Va       Pte      
- - - - - - - - - - - - - - - - - - -
0000237B 00000368 0F000F0F 01003368 C0004014 
0000237C 00000100 0F100F0F 01004100 C0004014 
0000237D 000003A8 0F100F0F 010053A8 C0004014 
0000237D 000003C8 0F100F8F 010053C8 C0004014 
0000237D 000003E8 0F100F0F 010053E8 C0004014 
0000237D 00000408 0F100F0F 01005408 C0004014 
0000237D 00000428 0F100F8F 01005428 C0004014 
Search done.
```

The columns in the display are as follows: **Pfn** is the page frame number (PFN) of the page; **Offset** is the offset on that page; **Hit** is the value at that address; **Va** is the virtual address mapped to this physical address (if this exists and can be determined); **Pte** is the page table entry (PTE).

To calculate the physical address, shift the PFN left three hexadecimal digits (12 bits) and add the offset. For example, the last line in the table is virtual address 0x0237D000 + 0x428 = 0x02347D428.

 

 





