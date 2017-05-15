---
title: Debug Break
description: Debug Break
ms.assetid: fc17d0b2-3ef5-4e10-a6a3-51f7011fddcf
keywords: ["Debug Break", "controlling the target, Debug Break"]
---

# Debug | Break


## <span id="ddk_debug_break_dbg"></span><span id="DDK_DEBUG_BREAK_DBG"></span>


Click **Break** on the **Debug** menu to stop the target's execution and return control to the debugger.

In user mode, this command stops the process and its threads, enabling you to regain control of the debugger. In kernel mode, this command breaks into the target computer.

You can also use this command while the debugger is active. In this situation, the command will truncate long [Debugger Command window](debugger-command-window.md) displays.

The **Break** command is equivalent to pressing CTRL+BREAK or clicking the **Break (Ctrl+Break)** button (![screen shot of the break button](images/tbbreak.png)) on the toolbar.

### <span id="ALT_DEL"></span><span id="alt_del"></span>ALT+DEL

You can use **ALT+DEL** to send a **Break**. **ALT+DEL** works the same as **Break (Ctrl+Break).**

### <span id="user_mode_effects"></span><span id="USER_MODE_EFFECTS"></span>User-Mode Effects

In user mode, the **Break** command causes the target application to break into the debugger. The target application stops, the debugger becomes active, and you can enter debugger commands.

If the debugger is already active, **Break** does not affect the target application. However, you can use this command to terminate a debugger command. For example, if you have requested a long display and do not want to see any more of it, **Break** will end the display and return you to the debugger command prompt.

When you are performing remote debugging with WinDbg, you can press the Break key on the host computer's keyboard. If you want to issue a break from the target computer's keyboard, use CTRL+C on an x86-based computer.

You can press the F12 key to open a command prompt when the application that is being debugged is busy. Click one of the target application's windows and press F12 on the target computer.

### <span id="kernel_mode_effects"></span><span id="KERNEL_MODE_EFFECTS"></span>Kernel-Mode Effects

In kernel mode, the **Break** command causes the target computer to break into the debugger. This command locks the target computer and wakes up the debugger.

When you are debugging a system that is still running, you must press the Break key on the host keyboard to open an initial command prompt.

If the debugger is already active, **Break** does not affect the target computer. However, you can use this command to terminate a debugger command. For example, if you have requested a long display and do not want to see any more of it, **Break** will end the display and return you to the debugger command prompt.

You can also use **Break** to open a command prompt when a debugger command is generating a long display or when the target computer is busy. When you are debugging an x86-based computer, you can also press CTRL+C on the target keyboard to have the same effect.

The SYSRQ key (or pressing ALT+SYSRQ on an enhanced keyboard) is similar. This key works from the host or target keyboard on any processor. However, this key works only if you have opened the prompt by pressing CTRL+C at least one time before.

You can disable the SYSRQ key by editing the registry. In the HKEY\_LOCAL\_MACHINE\\System\\CurrentControlSet\\Services\\i8042prt\\Parameters registry key, create a value named **BreakOnSysRq** and set it equal to DWORD 0x0. Then, restart the computer. After you have restarted the computer, you can press the SYSRQ key on the target computer's keyboard and it will not break into the kernel debugger.

### <span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

The corresponding key in KD and CDB is [**CTRL+C**](ctrl-c--break-.md). For more information about other ways to control program execution, see [Controlling the Target](controlling-the-target.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Debug%20|%20Break%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




