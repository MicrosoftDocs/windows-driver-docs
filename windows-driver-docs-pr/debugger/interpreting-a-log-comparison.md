---
title: Interpreting a Log Comparison
description: Interpreting a Log Comparison
ms.assetid: fe2acdd5-00aa-4414-a59e-e6203ad48363
keywords: ["UMDH, interpreting a log comparison"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Interpreting a Log Comparison


## <span id="ddk_interpreting_a_log_comparison_dtools"></span><span id="DDK_INTERPRETING_A_LOG_COMPARISON_DTOOLS"></span>


You can generate multiple User-Mode Dump Heap (UMDH) logs of the same process over time. Then, you can use UMDH to compare the logs and determine which call stack allocations have grown the most between trials.

For example, the following command directs UMDH to compare two UMDH logs, Log1.txt and Log2.txt, and redirects the output to a third file, Compare.txt.

```console
umdh -v Log1.txt Log2.txt > Compare.txt
```

The resulting Compare.txt file lists the call stacks recorded in each log and, for each stack, displays the change in heap allocations between the log files.

For example, the following line from the file shows the change in allocation size for the functions in the call stack labeled "Backtrace00053."

In Log1.txt, the calls in the stack accounts for 40,432 (0x9DF0) bytes, but in Log2.txt, the same call stack accounts for 61,712 (0xF110) bytes, a difference of 21,280 (0x5320) bytes.

```console
+ 5320 (f110 - 9df0) 3a allocs BackTrace00053 
Total increase == 5320
```

Following is the stack for the allocation:

```console
ntdll!RtlDebugAllocateHeap+0x000000FD
ntdll!RtlAllocateHeapSlowly+0x0000005A
ntdll!RtlAllocateHeap+0x00000808
MyApp!_heap_alloc_base+0x00000069
MyApp!_heap_alloc_dbg+0x000001A2
MyApp!_nh_malloc_dbg+0x00000023
MyApp!_nh_malloc+0x00000016
MyApp!operator new+0x0000000E
MyApp!LeakyFunc+0x0000001E
MyApp!main+0x0000002C
MyApp!mainCRTStartup+0x000000FC
KERNEL32!BaseProcessStart+0x0000003D
```

An examination of the call stack shows that the **LeakyFunc** function is allocating memory by using the Visual C++ run-time library. If examination of the other log files shows that the allocation grows over time, you might be able to conclude that memory allocated from the heap is not being freed.

### <span id="Symbol_Files_for_Analyzing_a_Log_File"></span><span id="symbol_files_for_analyzing_a_log_file"></span><span id="SYMBOL_FILES_FOR_ANALYZING_A_LOG_FILE"></span>Symbol Files for Analyzing a Log File

Suppose you have two computers: a *logging computer* where you create a UMDH log and an *analysis computer* where you analyze the UMDH log. The symbol path on your analysis computer must point to the symbols for the version of Windows that was loaded on the logging computer at the time the log was made. Do not point the symbol path on the analysis computer to a symbol server. If you do, UMDH will retrieve symbols for the version of Windows that is running on the analysis computer, and UMDH will not display meaningful results.

### <span id="see_also"></span><span id="SEE_ALSO"></span>See Also

[Using UMDH to Find a User-Mode Memory Leak](using-umdh-to-find-a-user-mode-memory-leak.md)

 

 





