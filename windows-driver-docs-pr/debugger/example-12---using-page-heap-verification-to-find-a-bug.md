---
title: Example 12 Using Page Heap Verification to Find a Bug
description: Example 12 Using Page Heap Verification to Find a Bug
ms.assetid: aa3f5c53-8522-48be-a3cd-49b740803fe3
ms.author: domars
ms.date: 10/12/2018
ms.localizationpriority: medium
---

# Example 12: Using Page Heap Verification to Find a Bug


## <span id="ddk_example_12___using_page_heap_verification_to_find_a_bug_dtools"></span><span id="DDK_EXAMPLE_12___USING_PAGE_HEAP_VERIFICATION_TO_FIND_A_BUG_DTOOLS"></span>


The following series of commands demonstrates how to use the page heap verification features of GFlags and the NTSD debugger to detect an error in heap memory use. In this example, the programmer suspects that a fictitious application, pheap-buggy.exe, has a heap error, and proceeds through a series of tests to identify the error.

For details on NTSD, see [Debugging Using CDB and NTSD](debugging-using-cdb-and-ntsd.md).

### <span id="Step_1__Enable_standard_page_heap_verification"></span><span id="step_1__enable_standard_page_heap_verification"></span><span id="STEP_1__ENABLE_STANDARD_PAGE_HEAP_VERIFICATION"></span>Step 1: Enable standard page heap verification

The following command enables standard page heap verification for pheap-buggy.exe:

```console
gflags /p /enable pheap-buggy.exe
```

### <span id="Step_2__Verify_that_page_heap_is_enabled"></span><span id="step_2__verify_that_page_heap_is_enabled"></span><span id="STEP_2__VERIFY_THAT_PAGE_HEAP_IS_ENABLED"></span>Step 2: Verify that page heap is enabled

The following command lists the image files for which page heap verification is enabled:

```console
gflags /p
```

In response, GFlags displays the following list of programs. In this display, **traces** indicates standard page heap verification, and **full traces** indicates full page heap verification. In this case, pheap-buggy.exe is listed with **traces**, indicating that standard page heap verification is enabled, as intended.

```console
pheap-buggy.exe: page heap enabled with flags (traces )
```

### <span id="Step_3__Run_the_debugger"></span><span id="step_3__run_the_debugger"></span><span id="STEP_3__RUN_THE_DEBUGGER"></span>Step 3: Run the debugger

The following command runs the **CorruptAfterEnd** function of pheap-buggy.exe in NTSD with the **-g** (ignore initial breakpoint) and **-x** (set second-chance break on access violation exceptions) parameters:

```console
ntsd -g -x pheap-buggy CorruptAfterEnd
```

When the application fails, NTSD generates the following display, which indicates that it detected an error in pheap-buggy.exe:

```dbgcmd
===========================================================
VERIFIER STOP 00000008: pid 0xAA0: corrupted suffix pattern

        00C81000 : Heap handle 
        00D81EB0 : Heap block 
        00000100 : Block size 
#         00000000 :
===========================================================

Break instruction exception - code 80000003 (first chance)
eax=00000000 ebx=00d81eb0 ecx=77f7e257 edx=0006fa18 esi=00000008 edi=00c81000
eip=77f7e098 esp=0006fc48 ebp=0006fc5c iopl=0         nv up ei pl zr na po nc
cs=001b  ss=0023  ds=0023  es=0023  fs=0038  gs=0000             efl=00000246
ntdll!DbgBreakPoint:
77f7e098 cc               int     3
```

The header information includes the address of the heap with the corrupted block (00C81000 : Heap handle), the address of the corrupted block (00D81EB0 : Heap block), and the size of the allocation (00000100 : Block size).

The "corrupted suffix pattern" message indicates that the application violated the data integrity pattern that GFlags inserted after the end of the pheap-buggy.exe heap allocation.

### <span id="Step_4__Display_the_call_stack"></span><span id="step_4__display_the_call_stack"></span><span id="STEP_4__DISPLAY_THE_CALL_STACK"></span>Step 4: Display the call stack

In the next step, use the addresses that NTSD reported to locate the function that caused the error. The next two commands turn on line number dumping in the debugger and display the call stack with line numbers.

```dbgcmd
C:\>.lines

Line number information will be loaded 

C:\>kb

ChildEBP RetAddr  Args to Child
WARNING: Stack unwind information not available. Following frames may be wrong.
0006fc5c 77f9e6dd 00000008 77f9e3e8 00c81000 ntdll!DbgBreakPoint
0006fcd8 77f9f3c8 00c81000 00000004 00d81eb0 ntdll!RtlpNtEnumerateSubKey+0x2879
0006fcfc 77f9f5bb 00c81000 01001002 00000010 ntdll!RtlpNtEnumerateSubKey+0x3564
0006fd4c 77fa261e 00c80000 01001002 00d81eb0 ntdll!RtlpNtEnumerateSubKey+0x3757
0006fdc0 77fc0dc2 00c80000 01001002 00d81eb0 ntdll!RtlpNtEnumerateSubKey+0x67ba
0006fe78 77fbd87b 00c80000 01001002 00d81eb0 ntdll!RtlSizeHeap+0x16a8
0006ff24 010013a4 00c80000 01001002 00d81eb0 ntdll!RtlFreeHeap+0x69
0006ff3c 01001450 00000000 00000001 0006ffc0 pheap-buggy!TestCorruptAfterEnd+0x2b [d:\nttest\base\testsrc\kernel\rtl\pageheap\pheap-buggy.cxx @ 185]
0006ff4c 0100157f 00000002 00c65a68 00c631d8 pheap-buggy!main+0xa9 [d:\nttest\base\testsrc\kernel\rtl\pageheap\pheap-buggy.cxx @ 69]
0006ffc0 77de43fe 00000000 00000001 7ffdf000 pheap-buggy!mainCRTStartup+0xe3 [crtexe.c @ 349]
0006fff0 00000000 0100149c 00000000 78746341 kernel32!DosPathToSessionPathA+0x204
```

As a result, the debugger displays the call stack for pheap-buggy.exe with line numbers. The call stack display shows that the error occurred when the **TestCorruptAfterEnd** function in pheap-buggy.exe tried to free an allocation at 0x00c80000 by calling **HeapFree**, a redirect to **RtlFreeHeap**.

The most likely cause of this error is that the program wrote past the end of the buffer that it allocated in this function.

### <span id="Step_5__Enable_full_page_heap_verification"></span><span id="step_5__enable_full_page_heap_verification"></span><span id="STEP_5__ENABLE_FULL_PAGE_HEAP_VERIFICATION"></span>Step 5: Enable full page heap verification

Unlike standard page heap verification, full page heap verification can catch the misuse of this heap buffer as soon as it occurs. The following command enables full page heap verification for pheap-buggy.exe:

```console
gflags /p /enable pheap-buggy.exe /full
```

### <span id="Step_6__Verify_that_full_page_heap_is_enabled"></span><span id="step_6__verify_that_full_page_heap_is_enabled"></span><span id="STEP_6__VERIFY_THAT_FULL_PAGE_HEAP_IS_ENABLED"></span>Step 6: Verify that full page heap is enabled

The following command lists the programs for which page heap verification is enabled:

```console
gflags /p
```

In response, GFlags displays the following list of programs. In this display, **traces** indicates standard page heap verification, and **full traces** indicates full page heap verification. In this case, pheap-buggy.exe is listed with **full traces**, indicating that full page heap verification is enabled, as intended.

```console
pheap-buggy.exe: page heap enabled with flags (full traces )
```

### <span id="Step_7__Run_the_debugger_again"></span><span id="step_7__run_the_debugger_again"></span><span id="STEP_7__RUN_THE_DEBUGGER_AGAIN"></span>Step 7: Run the debugger again

The following command runs the **CorruptAfterEnd** function of pheap-buggy.exe in the NTSD debugger with the **-g** (ignore initial breakpoint) and **-x** (set second-chance break on access violation exceptions) parameters:

```console
ntsd -g -x pheap-buggy CorruptAfterEnd
```

When the application fails, NTSD generates the following display, which indicates that it detected an error in pheap-buggy.exe:

```console
Page heap: process 0x5BC created heap @ 00880000 (00980000, flags 0x3)
ModLoad: 77db0000 77e8c000   kernel32.dll
ModLoad: 78000000 78046000   MSVCRT.dll
Page heap: process 0x5BC created heap @ 00B60000 (00C60000, flags 0x3)
Page heap: process 0x5BC created heap @ 00C80000 (00D80000, flags 0x3)
Access violation - code c0000005 (first chance)
Access violation - code c0000005 (!!! second chance !!!)
eax=00c86f00 ebx=00000000 ecx=77fbd80f edx=00c85000 esi=00c80000 edi=00c16fd0
eip=01001398 esp=0006ff2c ebp=0006ff4c iopl=0         nv up ei pl nz na po nc
cs=001b  ss=0023  ds=0023  es=0023  fs=0038  gs=0000             efl=00000206
pheap-buggy!TestCorruptAfterEnd+1f:
01001398 889801010000     mov     [eax+0x101],bl          ds:0023:00c87001=??
```

With full page heap verification enabled, the debugger breaks at an access violation. To find the precise location of the access violation, turn on line number dumping and display the call stack trace.

The numbered call stack trace appears as follows: The line displaying the problem appears in bold text.

```console
ChildEBP RetAddr  Args to Child
0006ff3c 01001450 00000000 00000001 0006ffc0 pheap-buggy!TestCorruptAfterEnd+0x1f [d:\nttest\base\testsrc\kernel\rtl\pageheap\pheap-buggy.cxx @ 184]
0006ff4c 0100157f 00000002 00c16fd0 00b70eb0 pheap-buggy!main+0xa9 [d:\nttest\base\testsrc\kernel\rtl\pageheap\pheap-buggy.cxx @ 69]
0006ffc0 77de43fe 00000000 00000001 7ffdf000 pheap-buggy!mainCRTStartup+0xe3 [crtexe.c @ 349]
WARNING: Stack unwind information not available. Following frames may be wrong.
0006fff0 00000000 0100149c 00000000 78746341 kernel32!DosPathToSessionPathA+0x204
```

The stack trace shows that the problem occurs in line 184 of pheap-buggy.exe. Because full page heap verification is enabled, the call stack starts in the program code, not in a system DLL. As a result, the violation was caught where it happened, instead of when the heap block was freed.

### <span id="Step_8__Locate_the_error_in_the_code"></span><span id="step_8__locate_the_error_in_the_code"></span><span id="STEP_8__LOCATE_THE_ERROR_IN_THE_CODE"></span>Step 8: Locate the error in the code

A quick inspection reveals the cause of the problem: The program tries to write to the 257th byte (0x101) of a 256-byte (0x100) buffer, a common off-by-one error.

```console
*((PCHAR)Block + 0x100) = 0;
```

 

 





