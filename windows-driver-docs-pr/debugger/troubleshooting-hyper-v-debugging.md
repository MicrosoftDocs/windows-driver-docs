---
title: Troubleshooting Hyper-V Debugging
description: Troubleshooting Hyper-V Debugging
ms.assetid: e1062300-0855-476c-9375-fdc6bc774949
---

# Troubleshooting Hyper-V Debugging


## <span id="ddk_opening_a_crash_dump_dbg"></span><span id="DDK_OPENING_A_CRASH_DUMP_DBG"></span>


This section discusses some problems that can arise during Hyper-V debugging.

### <span id="cabling_and_configuration_problems"></span><span id="CABLING_AND_CONFIGURATION_PROBLEMS"></span>Cabling and Configuration Problems

If there is no connection string when the root partition starts up, this is usually caused by a cabling or configutation issue. For example, output such as the following might be displayed:

```
Waiting to reconnect...
Connected to Windows 6001 x64 target, ptr64 TRUE
Kernel Debugger connection established.
Symbol search path is: c:\mysymbols\
Executable search path is:
Loading symbols for fffff800`01602000     ntkrnlmp.exe ->   ntkrnlmp.exe
ModLoad: fffff800`01602000 fffff800`01b17000   ntkrnlmp.exe
Windows Kernel Version 6001 MP (1 procs) Free x64
```

To address this problem, check the configuration of the root partition by typing **bcdedit** at a command prompt, and verify that the values are correct.

### <span id="vmdemux_problems"></span><span id="VMDEMUX_PROBLEMS"></span>Vmdemux Problems

If you restart vmdemux (virtual machine demultiplexer) after you have begun debugging Windows hypervisor, you must add -channel 0 to its command-line options in order to have the hypervisor channel re-created. This is typically done automatically by Windows hypervisor, but in this case it is not possible, because Windows hypervisor is already being debugged.

For a full list of the VMDemux command-line options, type vmdemux -? at the command prompt.

### <span id="problems_with_unmodified_partitions"></span><span id="PROBLEMS_WITH_UNMODIFIED_PARTITIONS"></span>Problems with Unmodified Partitions

If you have already set up Hyper-V debugging across a null-modem cable, and have copied the Kdhvcom.dll file to the root partition, and then you later restart the target computer in another partition that does not have this file installed, the debugger may freeze. In this case, restart vmdemux. This problem arises because unmodified partitions cannot handle multiplexed traffic. Typically, vmdemux closes down all the pipes on a clean shutdown. However, a non-clean shutdown, such as doing a hard restart, is not detectable.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Troubleshooting%20Hyper-V%20Debugging%20%20RELEASE:%20%284/24/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




