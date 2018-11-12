---
title: Example 10 Detecting a Heap Memory Leak in a Process
description: Example 10 Detecting a Heap Memory Leak in a Process
ms.assetid: ec98dd96-b12b-4f83-85e8-2c5ee32fc17e
ms.author: domars
ms.date: 10/12/2018
ms.localizationpriority: medium
---

# Example 10: Detecting a Heap Memory Leak in a Process


## <span id="ddk_example_10___detecting_a_heap_memory_leak_in_a_process_dtools"></span><span id="DDK_EXAMPLE_10___DETECTING_A_HEAP_MEMORY_LEAK_IN_A_PROCESS_DTOOLS"></span>


This example uses GFlags and User Mode Dump Heap (UMDH, umdh.exe), a tool included in Microsoft Debugging Tools for Windows.

**To detect a leak in heap memory in notepad.exe**

1.  Set the [Create user mode stack trace database](create-user-mode-stack-trace-database.md) (**ust**) flag for the notepad.exe image file.

    The following command uses GFlags to set the **Create user mode stack trace database** flag. It uses the **/i** parameter to identify the image file and the **ust** abbreviation for the flag.

    ```console
    gflags /i Notepad.exe +ust 
    ```

    As a result of this command, a user-mode stack trace is created for all new instances of the Notepad process.

2.  Set the symbol file path.

    The following command creates an environment variable that stores the path to the directory of symbol files:

    ```console
    set _NT_SYMBOL_PATH=C:\Windows\symbols
    ```

3.  Start Notepad.

4.  Find the process identifier (PID) of the Notepad process.

    You can find the PID of any running process from Task Manager or Tasklist (tasklist.exe), a tool included in Windows XP Professional and Windows Server 2003 operating systems. In this example, the Notepad PID is 1228.

5.  Run UMDH.

    The following command runs UMDH (umdh.exe). It uses the **-p:** parameter to specify the PID that, in this example, is 1228. It uses the **/f:** parameter to specify the name and location of the output file for the heap dump, notepad.dmp.

    ```console
    umdh -p:1228 -f:notepad.dmp 
    ```

    In response, UMDH writes a complete dump of all active heaps to the notepad.dmp file.

 

 





