---
title: File Kernel Debug
description: File Kernel Debug
ms.assetid: a80b3572-87a0-4a9d-9b62-67e1ca65fff4
keywords: ["File Kernel Debug", "starting the debugger, File Kernel Debug"]
ms.author: domars
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# File | Kernel Debug


## <span id="ddk_file_kernel_debug_dbg"></span><span id="DDK_FILE_KERNEL_DEBUG_DBG"></span>


Click **Kernel Debug** on the **File** menu to debug a target computer in kernel mode.

This command is equivalent to pressing CTRL+K. You can use this command only when WinDbg is in dormant mode.

### <span id="dialog_box"></span><span id="DIALOG_BOX"></span>Dialog Box

When you click **Kernel Debug**, the **Kernel Debugging** dialog box appears with these tabs:

-   The **COM** tab indicates that the connection will use a COM port. In the **Baud Rate** box, enter the baud rate. In the **Port** box, enter the name of the COM port. For more information, see [Setting Up a Serial Connection Manually](setting-up-a-null-modem-cable-connection.md).

    You can also use the COM tab to connect to virtual machine through a named pipe. In the **Port** box, enter **\\\\***VMHost***\\pipe\\***PipeName*. *VMHost* specifies the name of the physical computer on which the virtual machine is running. If the virtual machine is running on the same computer as the kernel debugger itself, use a single period (.) for *VMHost*. For more information, see [Setting Up a Connection to a Virtual Machine](attaching-to-a-virtual-machine--kernel-mode-.md).

-   The **1394** tab indicates that the connection will use 1394. In the **Channel** box, enter the 1394 channel number. 1394 debugging is supported only if both the host computer and target computer are running Windows XP or later versions of the Windows operating system. For more information, see [Setting Up a 1394 Connection Manually](setting-up-a-1394-cable-connection.md).

-   The **USB** tab indicates that the connection will use USB 2.0 or USB 3.0. In the **Target Name** box, enter the target name that you created when you configured the target computer. For more information, see [Setting Up a USB 2.0 Connection Manually](setting-up-a-usb-2-0-debug-cable-connection.md) and [Setting Up a USB 3.0 Connection Manually](setting-up-a-usb-3-0-debug-cable-connection.md).

-   The **NET** tab indicates that the connection will use Ethernet. In the **Port Number** box, enter the port number that you specified when you configured the target computer. In the **Key** box, enter the key that was generated for you (or that you created) when you configured the target computer. For more information, see [Setting Up a Network Connection Manually](setting-up-a-network-debugging-connection.md).

-   The **Local** tab indicates that WinDbg will perform local kernel debugging. Local kernel debugging is supported only on Windows XP and later.

For more information and for other methods of beginning a kernel debugging session, see [Live Kernel-Mode Debugging Using WinDbg](performing-kernel-mode-debugging-using-windbg.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20File%20|%20Kernel%20Debug%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




