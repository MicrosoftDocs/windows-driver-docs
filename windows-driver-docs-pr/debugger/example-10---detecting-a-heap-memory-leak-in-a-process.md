---
title: Example 10 Detecting a Heap Memory Leak in a Process
description: Example 10 Detecting a Heap Memory Leak in a Process
ms.assetid: ec98dd96-b12b-4f83-85e8-2c5ee32fc17e
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Example 10: Detecting a Heap Memory Leak in a Process


## <span id="ddk_example_10___detecting_a_heap_memory_leak_in_a_process_dtools"></span><span id="DDK_EXAMPLE_10___DETECTING_A_HEAP_MEMORY_LEAK_IN_A_PROCESS_DTOOLS"></span>


This example uses GFlags and User Mode Dump Heap (UMDH, umdh.exe), a tool included in Microsoft Debugging Tools for Windows.

**To detect a leak in heap memory in notepad.exe**

1.  Set the [Create user mode stack trace database](create-user-mode-stack-trace-database.md) (**ust**) flag for the notepad.exe image file.

    The following command uses GFlags to set the **Create user mode stack trace database** flag. It uses the **/i** parameter to identify the image file and the **ust** abbreviation for the flag.

    ```
    gflags /i Notepad.exe +ust 
    ```

    As a result of this command, a user-mode stack trace is created for all new instances of the Notepad process.

2.  Set the symbol file path.

    The following command creates an environment variable that stores the path to the directory of symbol files:

    ```
    set _NT_SYMBOL_PATH=C:\Windows\symbols
    ```

3.  Start Notepad.

4.  Find the process identifier (PID) of the Notepad process.

    You can find the PID of any running process from Task Manager or Tasklist (tasklist.exe), a tool included in Windows XP Professional and Windows Server 2003 operating systems. In this example, the Notepad PID is 1228.

5.  Run UMDH.

    The following command runs UMDH (umdh.exe). It uses the **-p:** parameter to specify the PID that, in this example, is 1228. It uses the **/f:** parameter to specify the name and location of the output file for the heap dump, notepad.dmp.

    ```
    umdh -p:1228 -f:notepad.dmp 
    ```

    In response, UMDH writes a complete dump of all active heaps to the notepad.dmp file.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Example%2010:%20%20Detecting%20a%20Heap%20Memory%20Leak%20in%20a%20Process%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




