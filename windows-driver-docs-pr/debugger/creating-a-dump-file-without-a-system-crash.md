---
title: Creating a Dump File Without a System Crash
description: Creating a Dump File Without a System Crash
ms.assetid: 747194d0-0aac-487a-acdc-ff27721606d4
keywords: ["dump file, creating without a system crash"]
---

# Creating a Dump File Without a System Crash


## <span id="ddk_creating_a_dump_file_without_a_system_crash_dbg"></span><span id="DDK_CREATING_A_DUMP_FILE_WITHOUT_A_SYSTEM_CRASH_DBG"></span>


If KD or WinDbg is performing kernel-mode debugging, it can cause a kernel-mode dump file to be written without crashing the target computer.

This dump file can be either a Complete Memory Dump or a Small Memory Dump. The Control Panel settings are not relevant to this action.

Whereas dump files caused by a system crash are written to the computer that has crashed, this dump file will be written to the host computer.

For details, see the [**.dump (Create Dump File)**](https://msdn.microsoft.com/library/windows/hardware/ff562428) command.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Creating%20a%20Dump%20File%20Without%20a%20System%20Crash%20%20RELEASE:%20%284/24/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




