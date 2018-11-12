---
title: Debug Kernel Connection Cycle Baud Rate
description: Debug Kernel Connection Cycle Baud Rate
ms.assetid: 5d7f13ff-738d-498c-88cb-ad2d6fe596ac
keywords: ["Debug Kernel Connection Cycle Baud Rate"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Debug | Kernel Connection | Cycle Baud Rate


## <span id="ddk_debug_kernel_connection_cycle_baud_rate_dbg"></span><span id="DDK_DEBUG_KERNEL_CONNECTION_CYCLE_BAUD_RATE_DBG"></span>


Point to **Kernel Connection** and then click **Cycle Baud Rate** on the **Debug** menu to change the baud rate that is used in the kernel debugging connection.

This command is equivalent to pressing CTRL+ALT+A. (You can also press CTRL+A in KD.)

This command cycles through all available baud rates for the kernel debugging connection. Supported baud rates are 19200, 38400, 57600, and 115200. Every time that you use this command, the next baud rate is selected. If the baud rate is already at 115200, it is reduced to 19200.

You cannot use this command to change the baud rate at which you are debugging. The baud rate of the host computer and the target computer must match, and you cannot change the baud rate of the target computer without restarting the computer. Therefore, you must change the baud rate only if the two computers are trying to communicate at different rates. In this case, you must change the host computer's baud rate to match that of the target computer.

 

 





