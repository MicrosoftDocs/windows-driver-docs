---
title: Synchronizing with the Target Computer
description: Synchronizing with the Target Computer
ms.assetid: bc9bbe35-6665-49ee-ba95-16ff03e25e96
keywords: ["synchronizing with the target computer", "synchronizing with the target computer, overview"]
---

# Synchronizing with the Target Computer


## <span id="ddk_synchronizing_with_the_target_computer_dbg"></span><span id="DDK_SYNCHRONIZING_WITH_THE_TARGET_COMPUTER_DBG"></span>


Sometimes during kernel-mode debugging, the target computer stops responding to the debugger.

In KD, you can press [**CTRL+R (Re-synchronize)**](https://msdn.microsoft.com/library/windows/hardware/ff540337) and then press ENTER to synchronize with the target computer. In WinDbg, use [CTRL+ALT+R](https://msdn.microsoft.com/library/windows/hardware/ff541792) or Debug | Kernel Connection | Resynchronize.

These commands frequently restore communication between the host and the target. However, resynchronization might not always be successful, especially if you are using a 1394 kernel connection.

The [**.restart (Restart Kernel Connection)**](https://msdn.microsoft.com/library/windows/hardware/ff564821) command provides a more powerful method of resynchronization. This command is equivalent to exiting the debugger and then attaching a new debugger to the existing session. This command is available only in KD, not in WinDbg.

The **.restart** command is most useful when you are performing [remote debugging through remote.exe](remote-debugging-through-remote-exe.md). (In this kind of debugging, it might be difficult to end and restart the debugger.) However, you cannot use **.restart** from a debugging client if you are performing remote debugging through the debugger.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Synchronizing%20with%20the%20Target%20Computer%20%20RELEASE:%20%284/24/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




