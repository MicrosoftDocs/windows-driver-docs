---
title: Debug Kernel Connection Cycle Baud Rate
description: Debug Kernel Connection Cycle Baud Rate
ms.assetid: 5d7f13ff-738d-498c-88cb-ad2d6fe596ac
keywords: ["Debug Kernel Connection Cycle Baud Rate"]
---

# Debug | Kernel Connection | Cycle Baud Rate


## <span id="ddk_debug_kernel_connection_cycle_baud_rate_dbg"></span><span id="DDK_DEBUG_KERNEL_CONNECTION_CYCLE_BAUD_RATE_DBG"></span>


Point to **Kernel Connection** and then click **Cycle Baud Rate** on the **Debug** menu to change the baud rate that is used in the kernel debugging connection.

This command is equivalent to pressing CTRL+ALT+A. (You can also press CTRL+A in KD.)

This command cycles through all available baud rates for the kernel debugging connection. Supported baud rates are 19200, 38400, 57600, and 115200. Every time that you use this command, the next baud rate is selected. If the baud rate is already at 115200, it is reduced to 19200.

You cannot use this command to change the baud rate at which you are debugging. The baud rate of the host computer and the target computer must match, and you cannot change the baud rate of the target computer without restarting the computer. Therefore, you must change the baud rate only if the two computers are trying to communicate at different rates. In this case, you must change the host computer's baud rate to match that of the target computer.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Debug%20|%20Kernel%20Connection%20|%20Cycle%20Baud%20Rate%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




