---
title: File Kernel Debug
description: File Kernel Debug
ms.assetid: a80b3572-87a0-4a9d-9b62-67e1ca65fff4
keywords: ["File Kernel Debug", "starting the debugger, File Kernel Debug"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# File | Kernel Debug


## <span id="ddk_file_kernel_debug_dbg"></span><span id="DDK_FILE_KERNEL_DEBUG_DBG"></span>


Click **Kernel Debug** on the **File** menu to debug a target computer in kernel mode.

This command is equivalent to pressing CTRL+K. You can use this command only when WinDbg is in dormant mode.

### <span id="dialog_box"></span><span id="DIALOG_BOX"></span>Dialog Box

When you click **Kernel Debug**, the **Kernel Debugging** dialog box appears with these tabs:

- The **COM** tab indicates that the connection will use a COM port. In the **Baud Rate** box, enter the baud rate. In the **Port** box, enter the name of the COM port. For more information, see [Setting Up a Serial Connection Manually](setting-up-a-null-modem-cable-connection.md).

  You can also use the COM tab to connect to virtual machine through a named pipe. In the **Port** box, enter **\\\\**<em>VMHost</em>**\\pipe\\**<em>PipeName</em>. *VMHost* specifies the name of the physical computer on which the virtual machine is running. If the virtual machine is running on the same computer as the kernel debugger itself, use a single period (.) for *VMHost*. For more information, see [Setting Up a Connection to a Virtual Machine](attaching-to-a-virtual-machine--kernel-mode-.md).

- The **1394** tab indicates that the connection will use 1394. In the **Channel** box, enter the 1394 channel number. 1394 debugging is supported only if both the host computer and target computer are running Windows XP or later versions of the Windows operating system. For more information, see [Setting Up a 1394 Connection Manually](setting-up-a-1394-cable-connection.md).

- The **USB** tab indicates that the connection will use USB 2.0 or USB 3.0. In the **Target Name** box, enter the target name that you created when you configured the target computer. For more information, see [Setting Up a USB 2.0 Connection Manually](setting-up-a-usb-2-0-debug-cable-connection.md) and [Setting Up a USB 3.0 Connection Manually](setting-up-a-usb-3-0-debug-cable-connection.md).

- The **NET** tab indicates that the connection will use Ethernet. In the **Port Number** box, enter the port number that you specified when you configured the target computer. In the **Key** box, enter the key that was generated for you (or that you created) when you configured the target computer. For more information, see [Setting Up a Network Connection Manually](setting-up-a-network-debugging-connection.md).

- The **Local** tab indicates that WinDbg will perform local kernel debugging. Local kernel debugging is supported only on Windows XP and later.

For more information and for other methods of beginning a kernel debugging session, see [Live Kernel-Mode Debugging Using WinDbg](performing-kernel-mode-debugging-using-windbg.md).

 

 





