---
title: Debugging User-Mode Processes Without Symbols
description: Debugging User-Mode Processes Without Symbols
ms.assetid: ac742239-ed6b-4813-80d6-7b8eb84a0cb4
keywords: ["symbols, debugging without symbols"]
---

# Debugging User-Mode Processes Without Symbols


## <span id="ddk_debugging_user_mode_processes_without_symbols_dbg"></span><span id="DDK_DEBUGGING_USER_MODE_PROCESSES_WITHOUT_SYMBOLS_DBG"></span>


It is important to have symbols on the faulting machine before starting the debugger for a user-mode failure. However, sometimes the debugger is started without symbols. If the problem is easily reproducible, you can just copy symbols and rerun. If, however, the problem may not occur again, some information can still be gleaned from the failure:

1.  To figure out what the addresses mean, you'll need a computer which matches the one with the error. It should have the same platform (x86 or x64) and be loaded with the same version of Windows.

2.  When you have the computer configured, copy the user-mode symbols and the binaries you want to debug onto the new machine.

3.  Start CDB or WinDbg on the symbol-less machine.

4.  If you don't know which application failed on the symbol-less machine, issue an [**| (Process Status)**](---process-status-.md) command. If that doesn't give you a name, break into KD on the symbol-less machine and do a [**!process 0 0**](-process.md), looking for the process ID given by the CDB command.

5.  When you have the two debuggers set up -- one with symbols which hasn't hit the error, and one which has hit the error but is without symbols -- issue a [**k (Display Stack Backtrace)**](k--kb--kc--kd--kp--kp--kv--display-stack-backtrace-.md) command on the symbol-less machine.

6.  On the machine with symbols, issue a [**u (Unassemble)**](u--unassemble-.md) command for each address given on the symbol-less stack. This will give you the stack trace for the error on the symbol-less machine.

7.  By looking at a stack trace you can see the module and function names involved in the call.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Debugging%20User-Mode%20Processes%20Without%20Symbols%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




