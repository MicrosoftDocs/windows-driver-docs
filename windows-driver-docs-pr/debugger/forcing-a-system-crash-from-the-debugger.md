---
title: Forcing a System Crash from the Debugger
description: Forcing a System Crash from the Debugger
ms.assetid: 7d7d9b07-00a3-4f87-8eb9-01b3f2fa312f
keywords: ["system crash, causing from debugger", "bug check, causing from debugger", "forcing system crash from debugger"]
---

# Forcing a System Crash from the Debugger


## <span id="ddk_forcing_a_system_crash_from_the_debugger_dbg"></span><span id="DDK_FORCING_A_SYSTEM_CRASH_FROM_THE_DEBUGGER_DBG"></span>


If KD or WinDbg is performing kernel-mode debugging, it can force a system crash to occur. This is done by entering the [**.crash (Force System Crash)**](https://msdn.microsoft.com/library/windows/hardware/ff562277) command at the command prompt. (If the target computer does not crash immediately, follow this with the [**g (Go)**](https://msdn.microsoft.com/library/windows/hardware/ff549693) command.)

When this command is issued, the system will call **KeBugCheck** and issue [**bug check 0xE2**](bug-check-0xe2--manually-initiated-crash.md) (MANUALLY\_INITIATED\_CRASH). Unless crash dumps have been disabled, a crash dump file is written at this point.

After the crash dump file has been written, the kernel debugger on the host computer will be alerted and can be used to actively debug the crashed target.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Forcing%20a%20System%20Crash%20from%20the%20Debugger%20%20RELEASE:%20%284/24/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




