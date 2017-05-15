---
title: Debug Kernel Connection Cycle Initial Break
description: Debug Kernel Connection Cycle Initial Break
ms.assetid: e4dbb810-d9b3-4721-89ec-af4b5e244cc0
keywords: ["Debug Kernel Connection Cycle Initial Break"]
---

# Debug | Kernel Connection | Cycle Initial Break


## <span id="ddk_debug_kernel_connection_cycle_initial_break_dbg"></span><span id="DDK_DEBUG_KERNEL_CONNECTION_CYCLE_INITIAL_BREAK_DBG"></span>


Point to **Kernel Conection** and then click **Cycle Initial Break** on the **Debug** menu to change the conditions on which the debugger automatically breaks into the target computer.

This command is equivalent to pressing CTRL+ALT+K. (You can also press CTRL+K in KD.)

This command causes the kernel debugger to cycle through the following three states:

<span id="No_break"></span><span id="no_break"></span><span id="NO_BREAK"></span>**No break**  
The debugger does not break into the target computer unless you press [CTRL+BREAK](debug---break.md) or Debug | Break.

<span id="Break_on_reboot"></span><span id="break_on_reboot"></span><span id="BREAK_ON_REBOOT"></span>**Break on reboot**  
The debugger breaks into a restarted target computer after the kernel initializes. This command is equivalent to starting WinDbg with the -b [**command-line option**](windbg-command-line-options.md).

<span id="Break_on_first_module_load"></span><span id="break_on_first_module_load"></span><span id="BREAK_ON_FIRST_MODULE_LOAD"></span>**Break on first module load**  
The debugger breaks into a restarted target computer after the first kernel module is loaded. (This action causes the break to occur earlier than in the **Break on reboot** state.) This command is equivalent to starting WinDbg with the -d [**command-line option**](windbg-command-line-options.md).

When you use the **Cycle Initial Break** command, the new break state is displayed.

### <span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For more information about related commands and an explanation of how the restart process affects the debugger, see [Crashing and Rebooting the Target Computer](crashing-and-rebooting-the-target-computer.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Debug%20|%20Kernel%20Connection%20|%20Cycle%20Initial%20Break%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




