---
title: Synchronizing with the Target Computer
description: Synchronizing with the Target Computer
ms.assetid: bc9bbe35-6665-49ee-ba95-16ff03e25e96
keywords: ["synchronizing with the target computer", "synchronizing with the target computer, overview"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Synchronizing with the Target Computer


## <span id="ddk_synchronizing_with_the_target_computer_dbg"></span><span id="DDK_SYNCHRONIZING_WITH_THE_TARGET_COMPUTER_DBG"></span>


Sometimes during kernel-mode debugging, the target computer stops responding to the debugger.

In KD, you can press [**CTRL+R (Re-synchronize)**](ctrl-r--re-synchronize-.md) and then press ENTER to synchronize with the target computer. In WinDbg, use [CTRL+ALT+R](debug---kernel-connection---resynchronize.md) or Debug | Kernel Connection | Resynchronize.

These commands frequently restore communication between the host and the target. However, resynchronization might not always be successful, especially if you are using a 1394 kernel connection.

The [**.restart (Restart Kernel Connection)**](-restart--restart-kernel-connection-.md) command provides a more powerful method of resynchronization. This command is equivalent to exiting the debugger and then attaching a new debugger to the existing session. This command is available only in KD, not in WinDbg.

The **.restart** command is most useful when you are performing [remote debugging through remote.exe](remote-debugging-through-remote-exe.md). (In this kind of debugging, it might be difficult to end and restart the debugger.) However, you cannot use **.restart** from a debugging client if you are performing remote debugging through the debugger.

 

 





