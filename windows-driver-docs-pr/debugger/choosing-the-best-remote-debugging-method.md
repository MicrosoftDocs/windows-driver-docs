---
title: Choosing the Best Remote Debugging Method
description: Choosing the Best Remote Debugging Method
ms.assetid: af048b78-cb80-44d2-854f-11e0991e3353
keywords: ["remote debugging, choosing the best method"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Choosing the Best Remote Debugging Method


## <span id="ddk_choosing_the_best_remote_debugging_method_dbg"></span><span id="DDK_CHOOSING_THE_BEST_REMOTE_DEBUGGING_METHOD_DBG"></span>


There are two primary methods of performing remote debugging, as well as several additional methods and a huge number of combination methods.

Here are some tips to help you choose the best technique.

-   [Remote debugging through the debugger](remote-debugging-through-the-debugger.md) is usually the best method. If you simply have one server and one client and they can freely connect to each other, the same debugger binaries are installed on both the client and the server, and the debugging technician who will be operating the client will be able to talk to someone in the room with the server, this is the recommended method.

    The client and the server can be running any version of Windows. They do not have to be running the same version as each other.

    If the client is unable to send a connection request to the server, but the server is able to send a request to the client, you can use remote debugging through the debugger with a *reverse connection* by using the **clicon** parameter.

-   [Remote debugging through remote.exe](remote-debugging-through-remote-exe.md) is used to remotely control a Command Prompt window. It can be used to remotely control KD, CDB, or NTSD. It cannot be used with WinDbg.

    If your client does not have copies of the debugger binaries, you must use the remote.exe method.

-   **A process server** or a **KD connection server** can be used if the debugging technician will not be able to talk to someone in the room with the server. All the actual debugging work is done by the client (called the *smart client*); this removes the need to have a second person present at the server itself.

    Process servers are used for user-mode debugging; KD connection servers are used for kernel-mode debugging. Other than this distinction, they behave in similar ways.

    This method is also useful if the computer where the server will be running cannot handle heavy process loads, or if the technician running the client has access to symbol files or source files that are confidential and cannot be accessed by the server. However, this method is not as fast or efficient as remote debugging through the debugger. This method cannot be used for dump-file debugging.

    See [Process Servers (User Mode)](process-servers--user-mode-.md) and [KD Connection Servers (Kernel Mode)](kd-connection-servers--kernel-mode-.md) for details.

-   **A repeater** is a lightweight proxy server that relays data between two computers. You can add a repeater between the client and the server if you are performing remote debugging through the debugger or if you are using a process server.

    Using a repeater may be necessary if your client and your server are unable to talk directly to each other, but can each access an outside computer. You can use reverse-connections with repeaters as well. It is even possible to use two repeaters in a row, but this is rarely necessary.

    See [Repeaters](repeaters.md) for details.

-   It is also possible to control CDB (or NTSD) from the kernel debugger. This is yet another form of remote debugging. See [Controlling the User-Mode Debugger from the Kernel Debugger](controlling-the-user-mode-debugger-from-the-kernel-debugger.md) for details.

Variations on all of these methods are possible.

It is possible to chain several computers together to take advantage of more than one transport method. You can create complicated transport sequences that take into account where the technician is, where the symbols are located, and whether there are firewalls preventing connections in certain directions. See [Advanced Remote Debugging Scenarios](advanced-remote-debugging-scenarios.md) for some examples.

You can even perform remote debugging on a single computer. For example, it might be useful to start a low-privilege process server and then connect to it with a high-privilege smart client. And on a Windows 2000 terminal server computer you can debug one session from another.

 

 





