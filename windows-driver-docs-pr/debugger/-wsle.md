---
title: wsle
description: The wsle extension displays all working set list entries (WSLEs).
ms.assetid: 9540ac44-a44b-4af6-acdd-baa275e8d004
keywords: ["wsle Windows Debugging"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- wsle
api_type:
- NA
---

# !wsle


The **!wsle** extension displays all working set list entries (WSLEs).

Syntax

``` syntax
    !wsle [Flags [Address]] 
```

## <span id="ddk__wsle_dbg"></span><span id="DDK__WSLE_DBG"></span>Parameters


<span id="_______Flags______"></span><span id="_______flags______"></span><span id="_______FLAGS______"></span> *Flags*   
Specifies the information to include in the display. This can be any combination of the following bits. The default is zero. If this is used, only basic information about the working set is displayed.

<span id="Bit_0__0x1_"></span><span id="bit_0__0x1_"></span><span id="BIT_0__0X1_"></span>Bit 0 (0x1)  
Causes the display to include information about each WSLE's address, age, lock status, and reference count. If a WSLE has an invalid page table entry (PTE) or page directory entry (PDE) associated with it, this is also displayed.

<span id="Bit_1__0x2_"></span><span id="bit_1__0x2_"></span><span id="BIT_1__0X2_"></span>Bit 1 (0x2)  
Causes the display to include the total number of valid WSLEs, the index of the last WSLE, and the index of the first free WSLE.

<span id="Bit_2__0x4_"></span><span id="bit_2__0x4_"></span><span id="BIT_2__0X4_"></span>Bit 2 (0x4)  
Causes the display to include the total number of free WSLEs, as well as the index of each free WSLE. If bit 1 is also set, then a check is done to make sure that the number of free WSLEs plus the number of valid WSLEs is actually equal to the total number of WSLEs.

<span id="_______Address______"></span><span id="_______address______"></span><span id="_______ADDRESS______"></span> *Address*   
Specifies the address of the working set list. If this is omitted, the default working set list is used. Specifying zero for *Address* is the same as omitting it.

### <span id="DLL"></span><span id="dll"></span>DLL

Kdexts.dll

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For information about working sets, see the Windows Driver Kit (WDK) documentation and *Microsoft Windows Internals*, by Mark Russinovich and David Solomon. (These resources may not be available in some languages and countries.)

Remarks
-------

This extension can take a significant amount of time to execute.

Here is an example from an x86 target computer running Windows Server 2003:

``` syntax
kd> !wsle 3

Working Set @ c0503000
    FirstFree:       a7  FirstDynamic:          4
    LastEntry      23d  NextSlot:         4  LastInitialized      259
    NonDirect       65  HashTable:        0  HashTableSize:         0

Reading the WSLE data...

Virtual Address           Age  Locked  ReferenceCount
        c0300203          0        1        1
        c0301203          0        1        1
        c0502203          0        1        1
        c0503203          0        1        1
        c01ff201          0        0        1
        77f74d19          3        0        1
        7ffdfa01          2        0        1
        c0001201          0        0        1

.....

Reading the WSLE data...
Valid WSLE entries = 0xa7
found end @ wsle index 0x259

.....
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20!wsle%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




