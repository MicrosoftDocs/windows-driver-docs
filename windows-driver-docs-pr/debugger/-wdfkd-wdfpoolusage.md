---
title: wdfkd.wdfpoolusage
description: The wdfkd.wdfpoolusage extension displays pool usage information for a specified driver, if the Kernel-Mode Driver Framework (KMDF) verifier is enabled for the driver.
ms.assetid: 6a77b76b-c970-447c-a8dd-e1ceb7add611
keywords: ["wdfkd.wdfpoolusage Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- wdfkd.wdfpoolusage
api_type:
- NA
ms.localizationpriority: medium
---

# !wdfkd.wdfpoolusage


The **!wdfkd.wdfpoolusage** extension displays pool usage information for a specified driver, if the Kernel-Mode Driver Framework (KMDF) verifier is enabled for the driver.

```dbgcmd
!wdfkd.wdfpoolusage [DriverName [SearchAddress] [Flags]]]
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______DriverName______"></span><span id="_______drivername______"></span><span id="_______DRIVERNAME______"></span> *DriverName*   
Optional. The name of a driver. *DriverName* must not include the .sys file name extension.

<span id="_______SearchAddress______"></span><span id="_______searchaddress______"></span><span id="_______SEARCHADDRESS______"></span> *SearchAddress*   
Optional. A string that represents a memory address. The pool entry that contains *SearchAddress* is displayed. If *SearchAddress* is 0 or omitted, all of the driver's pool entries are displayed.

<span id="_______Flags______"></span><span id="_______flags______"></span><span id="_______FLAGS______"></span> *Flags*   
Optional. The kind of information to display. This parameter is valid only if *SearchAddress* is nonzero. *Flags* can be any combination of the following bits. The default value is 0x0.

<span id="Bit_0__0x1_"></span><span id="bit_0__0x1_"></span><span id="BIT_0__0X1_"></span>Bit 0 (0x1)  
Displays verbose output. Multiple lines are displayed for each. If this flag is not set, the information about an allocation is displayed on one line.

<span id="Bit_1__0x2_"></span><span id="bit_1__0x2_"></span><span id="BIT_1__0X2_"></span>Bit 1 (0x2)  
Displays internal type information for each handle.

<span id="Bit_2__0x4_"></span><span id="bit_2__0x4_"></span><span id="BIT_2__0X4_"></span>Bit 2 (0x4)  
Displays the caller of each pool entry.

### <span id="DLL"></span><span id="dll"></span>DLL

Wdfkd.dll

### <span id="Frameworks"></span><span id="frameworks"></span><span id="FRAMEWORKS"></span>Frameworks

KMDF 1, UMDF 2

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For more information, see [Kernel-Mode Driver Framework Debugging](kernel-mode-driver-framework-debugging.md).

Remarks
-------

If you omit the *DriverName* parameter, the default driver is used. You can display the default driver by using the [**!wdfkd.wdfgetdriver**](-wdfkd-wdfgetdriver.md) extension; you can set the default driver by using the [**!wdfkd.wdfsetdriver**](-wdfkd-wdfsetdriver.md) extension.

The following example shows the output from the **!wdfpoolusage** extension when no pool allocation is marked and the *Flags* value is set to 0.

```dbgcmd
## kd> !wdfpoolusage wdfrawbusenumtest 0 0 
-----------------------------------
## FxDriverGlobals 83b7af18 pool stats
-----------------------------------
Driver Tag: 'RawB'
15126 NonPaged Bytes, 548 Paged Bytes
94 NonPaged Allocations, 10 Paged Allocations
15610 PeakNonPaged Bytes, 752 PeakPaged Bytes
100 PeakNonPaged Allocations, 14 PeakPaged Allocations

pool 82dbae00, Size  512 Tag 'RawB', NonPaged, Caller:  Wdf01000!FxVerifierLock::AllocateThreadTable+5d
```

The following example shows the output from **!wdfpoolusage** that appears when the value of *Flags* is 1. (Note that the ellipsis (...) on the second line indicates the omission of some output that is the same as that shown in the preceding example.)

```dbgcmd
kd> !wdfpoolusage wdfrawbusenumtest 0 1 
. . . 
100 PeakNonPaged Allocations, 14 PeakPaged Allocations

Client alloc starts at 82dbae00
Size  512 Tag 'RawB'
NonPaged (0x0)
Caller:  Wdf01000!FxVerifierLock::AllocateThreadTable+5d
```

 

 





