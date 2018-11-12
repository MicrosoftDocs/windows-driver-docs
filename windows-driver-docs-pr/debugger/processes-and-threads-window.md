---
title: Controlling Processes and Threads in WinDbg
description: Controlling Processes and Threads in WinDbg
ms.assetid: d4755889-9a65-4e81-b3a3-e0bbc6324d3e
keywords: ["debugging information windows, Processes and Threads window", "Processes and Threads window", "process, Processes and Threads window", "thread, Processes and Threads window"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Controlling Processes and Threads in WinDbg


## <span id="ddk_processes_and_threads_window_dbg"></span><span id="DDK_PROCESSES_AND_THREADS_WINDOW_DBG"></span>


In WinDbg, the Processes and Threads window displays information about the systems, processes, and threads that are being debugged. This window also enables you to select a new system, process, and thread to be active.

### <span id="opening_the_processes_and_threads_window"></span><span id="OPENING_THE_PROCESSES_AND_THREADS_WINDOW"></span>Opening the Processes and Threads Window

To open the Processes and Threads window, choose **Processes and Threads** from the **View** menu. (You can also press ALT+9 or click the **Processes and Threads** button (![screen shot of the processes and threads button](images/window-processes-threads.png)) on the toolbar. ALT+SHIFT+9 closes the Processes and Threads window.)

The following screen shot shows an example of a Processes and Threads window.

![screen shot of the processes and threads window](images/window-prth.png)

The Processes and Threads window displays a list of all processes that are currently being debugged. The threads in the process appear under each process. If the debugger is attached to multiple systems, the systems are shown at the top level of the tree, with the processes subordinate to them, and the threads subordinate to the processes.

Each system listing includes the server name and the protocol details. The system that the debugger is running on is identified as **&lt;Local&gt;**.

Each process listing includes the internal decimal process index that the debugger uses, the hexadecimal process ID, and the name of the application that is associated with the process.

Each thread listing includes the internal decimal thread index that the debugger uses and the hexadecimal thread ID.

### <span id="using_the_processes_and_threads_window"></span><span id="USING_THE_PROCESSES_AND_THREADS_WINDOW"></span>Using the Processes and Threads Window

In the Processes and Threads window, the current or active system, process, and thread appear in bold type. To make a new system, process, or thread active, click its line in the window.

The Processes and Threads window has a shortcut menu with additional commands. To access the menu, right-click the title bar or click the icon near the upper-right corner of the window (![screen shot of the button that displays the scratch pad window toolbar shortcut menu](images/window-processes-threads.png)). The following list describes some of the menu commands:

-   **Move to new dock** closes the Processes and Threads window and opens it in a new dock.

-   **Always floating** causes the window to remain undocked even if it is dragged to a docking location.

-   **Move with frame** causes the window to move when the WinDbg frame is moved, even if the window is undocked.

### <span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For other methods of displaying or controlling systems, see [Debugging Multiple Targets](debugging-multiple-targets.md). For other methods of displaying or controlling processes and threads, see [Controlling Processes and Threads](controlling-processes-and-threads.md).

 

 





