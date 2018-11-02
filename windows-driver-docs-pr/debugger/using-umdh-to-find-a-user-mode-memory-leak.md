---
title: Using UMDH to Find a User-Mode Memory Leak
description: Using UMDH to Find a User-Mode Memory Leak
ms.assetid: b15ed695-3f35-4a72-93ab-3cbfd2e33980
keywords: ["memory leak, user-mode, UMDH", "UMDH, memory leak detection"]
ms.author: domars
ms.date: 08/16/2018
ms.localizationpriority: medium
---

# Using UMDH to Find a User-Mode Memory Leak


The user-mode dump heap (UMDH) utility works with the operating system to analyze Windows heap allocations for a specific process. UMDH locates which routine in a specific process is leaking memory.

UMDH is included in Debugging Tools for Windows. For full details, see [UMDH](umdh.md).

### <span id="preparing_to_use_umdh"></span><span id="PREPARING_TO_USE_UMDH"></span>Preparing to Use UMDH

If you have not already determined which process is leaking memory, do that first. For details, see [Using Performance Monitor to Find User-Mode Memory Leaks](using-performance-monitor-to-find-a-user-mode-memory-leak.md).

The most important data in the UMDH logs are the stack traces of the heap allocations. To determine whether a process is leaking heap memory, analyze these stack traces.

Before using UMDH to display the stack trace data, you must use [GFlags](gflags.md) to configure your system properly. GFlags is included in Debugging Tools for Windows.

The following GFlags settings enable UMDH stack traces:

-   In the GFlags graphical interface, choose the Image File tab, type the process name (including the file name extension), press the TAB key, select **Create user mode stack trace database**, and then click **Apply**.

    Or, equivalently, use the following GFlags command line, where *ImageName* is the process name (including the file name extension):

    ```dbgcmd
    gflags /i ImageName +ust 
    ```
    Use this command to clear the GFlag settings once you are done. For more information, see [GFlags Commands](gflags-commands.md).

    ```dbgcmd
    gflags /i ImageName -ust 
    ```
    

-   By default, the amount of stack trace data that Windows gathers is limited to 32 MB on an x86 processor, and 64 MB on an x64 processor. If you must increase the size of this database, choose the **Image File** tab in the GFlags graphical interface, type the process name, press the TAB key, check the **Stack Backtrace (Megs)** check box, type a value (in MB) in the associated text box, and then click **Apply**. Increase this database only when necessary, because it may deplete limited Windows resources. When you no longer need the larger size, return this setting to its original value.

-   If you changed any flags on the **System Registry** tab, you must restart Windows to make these changes effective. If you changed any flags on the **Image File** tab, you must restart the process to make the changes effective. Changes to the **Kernel Flags** tab are effective immediately, but they are lost the next time Windows restarts.

Before using UMDH, you must have access to the proper symbols for your application. UMDH uses the symbol path specified by the environment variable \_NT\_SYMBOL\_PATH. Set this variable equal to a path containing the symbols for your application. If you also include a path to Windows symbols, the analysis may be more complete. The syntax for this symbol path is the same as that used by the debugger; for details, see [Symbol Path](symbol-path.md).

For example, if the symbols for your application are located at C:\\MySymbols, and you want to use the public Microsoft symbol store for your Windows symbols, using C:\\MyCache as your downstream store, you would use the following command to set your symbol path:

```console
set _NT_SYMBOL_PATH=c:\mysymbols;srv*c:\mycache*https://msdl.microsoft.com/download/symbols 
```

In addition, to assure accurate results, you must disable BSTR caching. To do this, set the OANOCACHE environment variable equal to one (1). Make this setting before you launch the application whose allocations are to be traced.

If you need to trace the allocations made by a service, you must set OANOCACHE as a system environment variable and then restart Windows for this setting to take effect.

On Windows 2000, in addition to setting OANOCACHE equal to 1, you must also install the hotfix available with [Microsoft Support Article 139071](https://go.microsoft.com/fwlink/p/?LinkId=241583). This hotfix is not needed on Windows XP and later versions of Windows.

### <span id="detecting_increases_in_heap_allocations_with_umdh"></span><span id="DETECTING_INCREASES_IN_HEAP_ALLOCATIONS_WITH_UMDH"></span>Detecting Increases in Heap Allocations with UMDH

After making these preparations, you can use UMDH to capture information about the heap allocations of a process. To do so, follow this procedure:

1.  Determine the [process ID (PID)](finding-the-process-id.md) for the process you want to investigate.

2.  Use UMDH to analyze the heap memory allocations for this process, and save it to a log file. Use the -p switch with the PID, and the -f switch with the name of the log file. For example, if the PID is 124, and you want to name the log file Log1.txt, use the following command:

    ```console
    umdh -p:124 -f:log1.txt 
    ```dbgcmd

3.  Use Notepad or another program to open the log file. This file contains the call stack for each heap allocation, the number of allocations made through that call stack, and the number of bytes consumed through that call stack.

4.  Because you are looking for a memory leak, the contents of a single log file are not sufficient. You must compare log files recorded at different times to determine which allocations are growing.

    UMDH can compare two different log files and display the change in their respective allocation sizes. You can use the greater-than symbol (**&gt;**) to redirect the results into a third text file. You may also want to include the -d option, which converts the byte and allocation counts from hexadecimal to decimal. For example, to compare Log1.txt and Log2.txt, saving the results of the comparison to the file LogCompare.txt, use the following command:

    ```console
    umdh log1.txt log2.txt > logcompare.txt 
    ```

5.  Open the LogCompare.txt file. Its contents resemble the following:

    ```text
    + 5320 ( f110 - 9df0) 3a allocs BackTrace00B53 
    Total increase == 5320 
    ```

    For each call stack (labeled "BackTrace") in the UMDH log files, there is a comparison made between the two log files. In this example, the first log file (Log1.txt) recorded 0x9DF0 bytes allocated for BackTrace00B53, while the second log file recorded 0xF110 bytes, which means that there were 0x5320 additional bytes allocated between the time the two logs were captured. The bytes came from the call stack identified by BackTrace00B53.

6.  To determine what is in that backtrace, open one of the original log files (for example, Log2.txt) and search for "BackTrace00B53." The results are similar to this data:

    ```text
    00005320 bytes in 0x14 allocations (@ 0x00000428) by: BackTrace00B53
    ntdll!RtlDebugAllocateHeap+0x000000FD
    ntdll!RtlAllocateHeapSlowly+0x0000005A
    ntdll!RtlAllocateHeap+0x00000808
    MyApp!_heap_alloc_base+0x00000069
    MyApp!_heap_alloc_dbg+0x000001A2
    MyApp!_nh_malloc_dbg+0x00000023
    MyApp!_nh_malloc+0x00000016
    MyApp!operator new+0x0000000E
    MyApp!DisplayMyGraphics+0x0000001E
    MyApp!main+0x0000002C
    MyApp!mainCRTStartup+0x000000FC
    KERNEL32!BaseProcessStart+0x0000003D 
    ```

    This UMDH output shows that there were 0x5320 (decimal 21280) total bytes allocated from the call stack. These bytes were allocated from 0x14 (decimal 20) separate allocations of 0x428 (decimal 1064) bytes each.

    The call stack is given an identifier of "BackTrace00B53," and the calls in this stack are displayed. In reviewing the call stack, you see that the **DisplayMyGraphics** routine is allocating memory through the **new** operator, which calls the routine *malloc*, which uses the Visual C++ run-time library to obtain memory from the heap.

    Determine which of these calls is the last one to explicitly appear in your source code. In this case, it is probably the **new** operator because the call to *malloc* occurred as part of the implementation of **new** rather than as a separate allocation. So this instance of the **new** operator in the **DisplayMyGraphics** routine is repeatedly allocating memory that is not being freed.

 

 





