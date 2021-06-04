---
title: Bug Check 0x18C HYPERGUARD_VIOLATION
description: The HYPERGUARD_VIOLATION bug check has a value of 0x0000018C. It indicates that the kernel has detected that critical kernel code or data have been corrupted.
keywords: ["Bug Check 0x18C HYPERGUARD_VIOLATION", "HYPERGUARD_VIOLATION"]
ms.date: 01/04/2019
topic_type:
- apiref
api_name:
- HYPERGUARD_VIOLATION
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0x18C: HYPERGUARD\_VIOLATION 

The HYPERGUARD\_VIOLATION bug check has a value of 0x0000018C. This indicates that the kernel has detected that critical kernel code or data have been corrupted.

> [!IMPORTANT]
> This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://www.windows.com/stopcode).


> [!NOTE] 
> This bug code is reserved for use by Hyperguard only.  
> It is  not a general purpose bug code intended for use by other components in data corruption scenarios.  
> Instead, define a unique bug code for your component.   
> Do not use this bug code in your component.
>

 ## HYPERGUARD\_VIOLATION Parameters

| Parameter | Description |
|-----------|-------------|
| 1    | Type of corrupted region - values listed below. |
| 2    | Failure type dependent information. |
| 3    | Reserved.  |
| 4    | Reserved.  |


**Type of corrupted region**

1001 : A generic data region

1002 : A page hash mismatch

1004 : A processor IDT

1005 : A processor GDT

1007 : Debug routine modification

1008 : A dynamic code region

1009 : A generic shareable data region

100a : A hypervisor overlay region

100b : A processor mode misconfiguration

100c : An extended processor control register

100d : A secure memory region

100e : A loaded module

100f : A processor state region

1010 : The kernel CFG bitmap

1011 : The virtual address 0 page

1012 : The alternate inverted function table

1013 : An on-demand page verification failed

1016 : A secure image region

1017 : Kernel virtual address protection inconsistency

1101 : Internal context corruption

1102 : IDTR modification

1103 : GDTR modification

## ## Cause

This bugcheck is generated when the kernel detects that critical kernel code or data have been corrupted. There are generally three causes for a corruption:

1) A driver has inadvertently or deliberately modified critical kernel code or data. 

2) A developer attempted to set a normal kernel breakpoint using a kernel debugger that was not attached when the system was booted. Normal breakpoints,
 "bp", can only be set if the debugger is attached at boot time. Hardware breakpoints, "ba", can be set at any time.

3) A hardware corruption occurred, e.g. failing RAM holding kernel code or data.


## ## See Also-

[Bug Check Code Reference](bug-check-code-reference2.md)





