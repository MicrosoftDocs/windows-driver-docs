---
title: Controlling Processes and Threads
description: Controlling Processes and Threads
ms.assetid: f5a50b54-443e-425e-98cb-cff8d31ac897
keywords: ["process", "process, choosing", "thread", "thread, choosing", "thread, freezing", "thread, unfreezing (thawing)", "thread, suspending", "suspend count of threads", "freezing threads"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Controlling Processes and Threads


## <span id="ddk_controlling_processes_and_threads_dbg"></span><span id="DDK_CONTROLLING_PROCESSES_AND_THREADS_DBG"></span>


When you are performing user-mode debugging, you activate, display, freeze, unfreeze, suspend, and unsuspend processes and threads.

The *current* or *active* process is the process that is currently being debugged. Similarly, the *current* or *active* thread is the thread that the debugger is currently controlling. The actions of many debugger commands are determined by the identity of the current process and thread. The current process also determines the virtual address mappings that the debugger uses.

When debugging begins, the current process is the one that the debugger is attached to or that caused the exception that broke into the debugger. Similarly, the current thread is the one that was active when the debugger attached to the process or that caused the exception. However, you can use the debugger to change the current process and thread and to freeze or unfreeze individual threads.

In kernel-mode debugging, processes and threads are not controlled by the methods that are described in this section. For more information about how processes and threads are manipulated in kernel mode, see [Changing Contexts](changing-contexts.md).

### <span id="displaying_processes_and_threads"></span><span id="DISPLAYING_PROCESSES_AND_THREADS"></span>Displaying Processes and Threads

To display process and thread information, you can use the following methods:

-   The [**| (Process Status)**](---process-status-.md) command

-   The [**~ (Thread Status)**](---thread-status-.md) command

-   (WinDbg only) The [Processes and Threads window](processes-and-threads-window.md)

### <span id="setting_the_current_process_and_thread"></span><span id="SETTING_THE_CURRENT_PROCESS_AND_THREAD"></span>Setting the Current Process and Thread

To change the current process or thread, you can use the following methods:

-   The [**|s (Set Current Process)**](-s--set-current-process-.md) command

-   The [**~s (Set Current Thread)**](-s--set-current-thread-.md) command

-   (WinDbg only) The [Processes and Threads window](processes-and-threads-window.md)

### <span id="freezing_and_suspending_threads"></span><span id="FREEZING_AND_SUSPENDING_THREADS"></span>Freezing and Suspending Threads

The debugger can change the execution of a thread by *suspending* the thread or by *freezing* the thread. These two actions have somewhat different effects.

Each thread has a *suspend count* that is associated with it. If this count is one or larger, the system does not run the thread. If the count is zero or lower, the system runs the thread when appropriate.

Typically, each thread has a suspend count of zero. When the debugger attaches to a process, it increments the suspend counts of all threads in that process by one. If the debugger detaches from the process, it decrements all suspend counts by one. When the debugger executes the process, it temporarily decrements all suspend counts by one.

You can control the suspend count of any thread from the debugger by using the following methods:

-   The [**~n (Suspend Thread)**](-n--suspend-thread-.md) command increments the specified thread's suspend count by one.

-   The [**~m (Resume Thread)**](-m--resume-thread-.md) command decrements the specified thread's suspend count by one.

The most common use for these commands is to raise a specific thread's suspend count from one to two. When the debugger executes or detaches from the process, the thread then has a suspend count of one and remains suspended, even if other threads in the process are executing.

You can suspend threads even when you are performing [noninvasive debugging](noninvasive-debugging--user-mode-.md).

The debugger can also *freeze* a thread. This action is similar to suspending the thread in some ways. However, "frozen" is only a debugger setting. Nothing in the Windows operating system recognizes that anything is different about this thread.

By default, all threads are unfrozen. When the debugger causes a process to execute, threads that are frozen do not execute. However, if the debugger detaches from the process, all threads unfreeze.

To freeze and unfreeze individual threads, you can use the following methods:

-   The [**~f (Freeze Thread)**](-f--freeze-thread-.md) command freezes the specified thread.

-   The [**~u (Unfreeze Thread)**](-u--unfreeze-thread-.md) command unfreezes the specified thread.

In any event, threads that belong to the target process never execute when the debugger has broken into the target. The suspend count of a thread affects the thread's behavior only when the debugger executes the process or detaches. The frozen status affects the thread's behavior only when the debugger executes the process.

### <span id="threads_and_processes_in_other_commands"></span><span id="THREADS_AND_PROCESSES_IN_OTHER_COMMANDS"></span>Threads and Processes in Other Commands

You can add thread specifiers or process specifiers before many other commands. For more information, see the individual command topics.

You can add the [**~e (Thread-Specific Command)**](-e--thread-specific-command-.md) qualifier before many commands and extension commands. This qualifier causes the command to be executed with respect to the specified thread. This qualifier is especially useful if you want to apply a command to more than one thread. For example, the following command repeats the [**!gle**](-gle.md) extension command for every thread that is being debugged.

```dbgcmd
~*e !gle 
```

### <span id="multiple_systems"></span><span id="MULTIPLE_SYSTEMS"></span>Multiple Systems

The debugger can attach to multiple targets at the same time. When these processes include dump files or include live targets on more than one computer, the debugger references a system, process, and thread for each action. For more information about this kind of debugging, see [Debugging Multiple Targets](debugging-multiple-targets.md).

 

 





