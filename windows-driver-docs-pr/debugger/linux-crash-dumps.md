---
title: Linux crash dumps
description: Linux crash dumps
keywords: ["remote debugging, linux, process"]
ms.date: 04/04/2025
ms.topic: concept-article
---

# Linux crash dumps

This article describes how to create and view different types of Linux crash dump files. Viewing Linux crash dumps requires WinDbg version 1.2402.24001.0 or above.

When opening a Linux (non-Windows) core dump in WinDbg, basic debugger commands should all work properly, but extensions and Windows-specific commands that reference Windows structures, will not work.

## Crash dump files supported

### Linux kernel dumps

Opening Linux Kernel compressed KDUMPs and doing post-mortem debugging and analysis with full private DWARF symbols is available in the Windows debugger.

WinDbg only supports ZLIB compressed KDUMP files. LZO and Snappy compressed KDUMPs are unsupported.

For general information about Linux KDUMPs, see [KDump (Linux)](https://en.wikipedia.org/wiki/Kdump_(Linux)) Wikipedia page, and [Core dump](https://wiki.archlinux.org/title/Core_dump).

### ELF core dumps

As part of supporting Open Enclave, WinDbg can open ELF core dumps and binaries as well as DWARF symbols (DWARF 5 isn't supported) from both Enclaves and Linux applications. For more information about Open Enclave, see [Open Enclave debugging](open-enclave-debugging.md).

### Process dumps

Single process dumps are supported. There are a number of ways to gather a process dump, including the Linux [Sysinternals ProcDump for Linux](https://github.com/Sysinternals/ProcDump-for-Linux) utility. Another option is to use the GNU Debugger - GDBServer, to generate a core dump. For more information about GDBServer, see [https://en.wikipedia.org/wiki/Gdbserver](https://en.wikipedia.org/wiki/Gdbserver). Documentation for remote gdb debugging is available on the Sourceware web site - [Debugging Remote Programs](https://sourceware.org/gdb/current/onlinedocs/gdb#Remote-Debugging).

## Enable Linux NATVIS visualization and DML link traversal

The  Standard Template Library (STL) extensibility in the Windows Debuggers is provided by a NatVis file, `stl.natvis` that understands many versions of the STL that ship with Visual Studio and Windows. For general information about NATVIS, see 
[Native Debugger Objects in NatVis](native-debugger-objects-in-natvis.md). The versions of the STL which are used for Linux components (GCC's or LLDB's) are very different.

To enable NATVIS visualization and DML link traversal optimized for Linux first unload the default natvis file, [.scriptunload](../debuggercmds/-scriptunload--unload-script-.md) `stl.natvis`.

Then [.scriptload](../debuggercmds/-scriptload--load-script-.md) the `gstl.natvis` file. Use [.scriptlist](../debuggercmds/-scriptlist--list-loaded-scripts-.md) to confirm that `gstl.natvis` is active.

```dbgcmd
0: kd> .scriptlist
Command Loaded Scripts:
...
    NatVis script from 'C:\Users\Bob\AppData\Local\dbg\UI\2402.24001.0\amd64\Visualizers\gstl.natvis'
```

For more information about working with DML, see [Customizing Debugger Output Using DML](customizing-debugger-output-using-dml.md).

## Single process core dump of the DisplayGreeting app

This example shows how to create a single process core dump using gdb. For more information on using GDBServer with WinDbg, and a code walkthrough, see [Linux live remote process debugging](linux-live-remote-process-debugging.md). For the example code for DisplayGreeting, see [C++ app walkthrough](linux-live-remote-process-debugging.md#c-app-walkthrough).

### Locate the desired process

We can either list all of the processes in Linux using the `ps -A` command, or use the -f option with pgrep, as we know that we are looking for the DisplayGreeting app.

```dbgcmd
$ pgrep -f DisplayGreeting
9382
```

In this example walkthrough, it shows a process ID of 9382.

### Attach to process with gdb and generate a core dump

Use gdb to attach to the process.

```dbgcmd
$ gdb -p 9382
```

Display help for the `generate-core-file` gdb command.

```dbgcmd
(gdb) help generate-core-file
Save a core file with the current state of the debugged process.
Argument is optional filename.  Default filename is 'core.<process_id>'.
```

Then at the (gdb) prompt, generate a process core dump file with the default filename.

```dbgcmd
(gdb) generate-core-file
Saved corefile core.9382
(gdb) quit
```

### Load and examine the Linux process core dump

Use the **Open dump file** menu option in WinDbg to load the generated core dump.

### Add the source and symbol paths to the debugger session

To view the source code and variables, set the symbols and source path. For general information on setting the symbols path, see [Using Symbols](using-symbols.md). For more detailed information on Linux symbols, see [Linux symbols and sources](linux-dwarf-symbols.md).

Use `.sympath` to add the symbol path to the debugger session. In this WSL Linux Ubuntu example, the DisplayGreetings code and symbols are available this location, for a user named Bob.

`\\wsl$\Ubuntu\mnt\c\Users\Bob\`

In WSL this directory maps to the Windows OS location of: `C:\Users\Bob\` So these two commands are used.

`.sympath C:\Users\Bob\`

`.srcpath C:\Users\Bob\`

For more information about accessing the WSL file system in Windows, see [File Permissions for WSL](/windows/wsl/file-permissions).

To benefit from additional Linux OS symbols, add the DebugInfoD symbols using the .sympath location.

`.sympath+ DebugInfoD*https://debuginfod.elfutils.org`

Use the `.reload` command to reload the symbols.

Also supported is the automatic download of sources from DebugInfoD servers, which support returning that artifact type. To take advantage of this capability, add the elfutils server using .srcpath.

`.srcpath+ DebugInfoD*https://debuginfod.elfutils.org`

### Examining the process dump

Use the `lm` command to confirm that the dump file contains the DisplayGreeting app.

```dbgcmd
0:000> lm
start             end                 module name
00005555`55554000 00005555`55558140   DisplayGreeting T (service symbols: DWARF Private Symbols)        c:\users\bob\DisplayGreeting
00007fff`f7a54000 00007fff`f7a732e8   libgcc_s_so   (deferred)    
00007fff`f7a74000 00007fff`f7b5a108   libm_so    (deferred)    
00007fff`f7b5b000 00007fff`f7d82e50   libc_so  T (service symbols: DWARF Private Symbols)        C:\ProgramData\Dbg\sym\_.debug\elf-buildid-sym-a43bfc8428df6623cd498c9c0caeb91aec9be4f9\_.debug
00007fff`f7d83000 00007fff`f7fae8c0   libstdc___so   (deferred)    
00007fff`f7fc1000 00007fff`f7fc1000   linux_vdso_so   (deferred)    
00007fff`f7fc3000 00007fff`f7ffe2d8   ld_linux_x86_64_so T (service symbols: DWARF Private Symbols)        C:\ProgramData\Dbg\sym\_.debug\elf-buildid-sym-9718d3757f00d2366056830aae09698dbd35e32c\_.debug
```

Note that the first command execution may take a bit of time, as debug symbols are loaded into cache. In addition to looking for symbols and binaries via the symbol server or your local search path, because of the GDBServer integration, it may load these files from a remote filesystem if they cannot be found locally. This operation is typically slower than acquiring symbols from symsrv or a local search path.

Use the `x` command to display the functions available in DisplayGreeting.

```dbgcmd
0:000> x /D /f DisplayGreeting!*
 A B C D E F G H I J K L M N O P Q R S T U V W X Y Z

*** WARNING: Unable to verify timestamp for DisplayGreeting
00005651`7935b331 DisplayGreeting!_GLOBAL__sub_I__Z17GetCppConGreetingPwm (void)
00005651`7935b2db DisplayGreeting!__static_initialization_and_destruction_0 (int, int)
00005651`7935b37b DisplayGreeting!std::__array_traits<wchar_t, 50>::_S_ptr (wchar_t (*)[50])
00005651`7935b368 DisplayGreeting!std::array<wchar_t, 50>::size (std::array<wchar_t, 50> *)
00005651`7935b34a DisplayGreeting!std::array<wchar_t, 50>::data (std::array<wchar_t, 50> *)
00005651`7935b225 DisplayGreeting!main (void)
00005651`7935b1e9 DisplayGreeting!GetCppConGreeting (wchar_t *, size_t)
```

Use the `dx` command to view the local variable *greeting*.

```dbgcmd
0:000> dx greeting
...
Error: Unable to bind name 'greeting'
```

As the parameter greeting was not yet used when the dump was taken, it isn't available in the dump file.

Use the `dx` command to examine the processes that are available in the dump file.

```dbgcmd
:000> dx @$cursession.Processes.Take(30)
@$cursession.Processes.Take(30)                
    [0x24a6]         : DisplayGreeting [Switch To]

Click on the `[Switch To]` DML link to switch to the 9382 process.

```dbgcmd
0:000> dx -s @$cursession.Processes.Take(30)[9382].SwitchTo()
0:000> dx -r1 @$cursession.Processes.Take(30)[9382]
@$cursession.Processes.Take(30)[9382]                 : DisplayGreeting [Switch To]
    Name             : DisplayGreeting
    Id               : 0x24a6
    Index            : 0x0
    Handle           : 0x24a6
    Threads         
    Modules         
    Environment     
    Direct3D        
    Attributes      
    Devices         
    Io              
    Memory          
    TTD    
    GroupedStacks   
```

To view information about the threads and modules, click on the generated DML link in the output, or type in commands similar to this one for your crash dump.

```dbgcmd
0:000> dx -r1 @$cursession.Processes.Take(30)[9382].Threads
@$cursession.Processes.Take(30)[9382].Threads       
    [0x24a6]         [Switch To]
0:000> dx -r1 @$cursession.Processes.Take(30)[9382].Modules
@$cursession.Processes.Take(30)[9382].Modules       
    [0x0]            : /mnt/c/Users/Bob/DisplayGreeting
    [0x1]            : /usr/lib/x86_64-linux-gnu/libgcc_s.so.1
    [0x2]            : /usr/lib/x86_64-linux-gnu/libm.so.6
    [0x3]            : /usr/lib/x86_64-linux-gnu/libc.so.6
    [0x4]            : /usr/lib/x86_64-linux-gnu/libstdc++.so.6.0.30
    [0x5]            : /usr/lib/x86_64-linux-gnu/ld-linux-x86-64.so.2
    [0x6]            : linux-vdso.so.1
```

### Use the ELF/CORE diagnostic extensions to display dump file information

Use the [Linux diagnostic extensions - ELFBinComposition.dll](#linux-diagnostic-extensions---elfbincompositiondll) to display dump file information. For example, use `!dumpdebug` to confirm that this is an ELF user core dump, and display other information.

```dbgcmd
0:000> !dumpdebug
Dump Diagnostics: Format = ELF User Core
********************************************************************************
File Mapping Size:           0x151d78 (1 Mb)
Highest Memory Offset:       0x14e5f0 (1 Mb)
...
```

Use `!ntprpsinfo` to display the NT_PRPSINFO data.

```dbgcmd
0:000> !ntprpsinfo
NT_PRPSINFO (process info):
    state: 0, sname: t, zomb: 0, nice: 0, flag: 0x4040000019999999
    uid: 1000, gid: 1000, pid: 9382, ppid: 388, pgrp: 9382, sid: 388
    fname: DisplayGreeting
    psargs: ./DisplayGreeting
```

## Kernel KDump crash dumps

There are many ways to create a crash dump file in Linux. For example, one option with Ubuntu Linux is described in [Kernel crash dump](https://ubuntu.com/server/docs/kernel-crash-dump).

Other options include the use of kexectools to enable Kdump. For more information, see [KDump (Linux)](https://en.wikipedia.org/wiki/Kdump_(Linux)). If kdump is enabled, you can verify that kdump is active and running using `systemctl status kdump`.

Once the OS crash is triggered on a test system, the crash dump file is created.

### Load and examine the Linux OS crash dump

Use the **Open dump file** menu option to load the generated kdump.

As described in the previous section, enable NATVIS visualization and DML link traversal optimized for Linux, by loading the `gstl.natvis` file.

## Use the ELF Bin composition commands to analyze a Linux kernel dump

To be able to use additional ELF Bin composition commands, use the [.chain](../debuggercmds/-chain--list-debugger-extensions-.md) command for confirm that the ELFBinComposition.dll is loaded.

```dbgcmd
0: kd> .chain
Extension DLL chain:
    ELFBinComposition: image 10.0.27606.1000, API 0.0.0, 
        [path: C:\Users\Bob\AppData\Local\dbg\UI\Fast.20240423.1\amd64\winext\ELFBinComposition.dll]
...
```

If ELFBinComposition isn't loaded, use .load to load it.  For more information, see [.load, .loadby (Load Extension DLL)](../debuggercmds/-load---loadby--load-extension-dll-.md)

Use the `!ELFBinComposition.dumpdebug` command to display information about the loaded dump file. In this example, an ELF user core dump file has been loaded.

```dbgcmd
0: kd> !ELFBinComposition.dumpdebug
Dump Diagnostics: Format = Kernel KDump
********************************************************************************
File Mapping Size:           0x3b34090 (59 Mb)
Highest Memory Offset:       0x3b34090 (59 Mb)
```

Use ELFBinComposition `!vmcoreinfo` to display the VMCOREINFO table from the Linux kernel core dump (KDUMP) being debugged.

```dbgcmd
0: kd> !vmcoreinfo
VMCOREINFO:
    OSRELEASE=6.5.0-25-generic
    BUILD-ID=8567ad7c7c2f78f3654f6cc90a9e1b3f9c3a4b32
    PAGESIZE=4096
    SYMBOL(init_uts_ns)=ffffded86e11b388
    OFFSET(uts_namespace.name)=0
    SYMBOL(node_online_map)=ffffded86dcceb40
    SYMBOL(swapper_pg_dir)=ffffded86d143000
    SYMBOL(_stext)=ffffded86ace0000
    SYMBOL(vmap_area_list)=ffffded86de48140
    SYMBOL(mem_section)=ffff0f2e1efe4600
    LENGTH(mem_section)=8192
...
```

Use the `!kdumppagerange` to dump the first part of the dump file, starting at zero.

```dbgcmd
0: kd> !kdumppagerange 0
    PFNs [0x540e0, 0x55643) -> Descs [0x0, 0x1563): File Offsets [0x307430, 0xeeb37a) 0xbe3f4a bytes across 5475 pages as ZLIB
    PFNs [0x55643, 0x55650) -> Descs [0x1563, 0x1570): File Offsets [0x306430, 0x307430) 0x1000 bytes across 13 duplicate pages as Uncompressed
    PFNs [0x55650, 0x556d6) -> Descs [0x1570, 0x15f6): File Offsets [0xeeb37a, 0xf0c405) 0x2108b bytes across 134 pages as ZLIB
    PFNs [0x556d6, 0x556dc) -> Descs [0x15f6, 0x15fc): File Offsets [0xf0c405, 0xf12405) 0x6000 bytes across 6 pages as Uncompressed
    PFNs [0x556dc, 0x55e98) -> Descs [0x15fc, 0x1db8): File Offsets [0xf12405, 0x1216d1b) 0x304916 bytes across 1980 pages as ZLIB
    PFNs [0x55e98, 0x55ea4) -> Descs [0x1db8, 0x1dc4): File Offsets [0x1216d1b, 0x1222d1b) 0xc000 bytes across 12 pages as Uncompressed
    PFNs [0x55ea4, 0x56542) -> Descs [0x1dc4, 0x2462): File Offsets [0x1222d1b, 0x14ba138) 0x29741d bytes across 1694 pages as ZLIB
    PFNs [0x56542, 0x56543) -> Descs [0x2462, 0x2463): File Offsets [0x306430, 0x307430) 0x1000 bytes across 1 pages as Uncompressed
    PFNs [0x56543, 0x56544) -> Descs [0x2463, 0x2464): File Offsets [0x14ba138, 0x14ba194) 0x5c bytes across 1 pages as ZLIB
    PFNs [0x56544, 0x5654f) -> Descs [0x2464, 0x246f): File Offsets [0x306430, 0x307430) 0x1000 bytes across 11 duplicate pages as Uncompressed
```

The output of !kdumppagerange displays various page frame (PFN) values. We can select one of interest and use the `!kdumppfn <PFN>` to display information about the PFN and where its data is within the KDUMP.

```dbgcmd
0: kd> !kdumppfn 0x540e0
    Page frame 0x540e0 = File offset [0x307430, 0x307b9f) 0x76f bytes as ZLIB...
```

### Examine the dump file

Use the `k` command to display the call stack to investigate what code was running when the crash occurred.

```dbgcmd
6: kd> k
 # Child-SP          RetAddr               Call Site
00 ffff0000`0bc3bc90 ffff0000`085161f8     vmlinux!sysrq_handle_crash+0x24 [/usr/src/kernel/drivers/tty\sysrq.c @ 147] 
01 ffff0000`0bc3bca0 ffff0000`08516824     vmlinux!__handle_sysrq+0x88 [/usr/src/kernel/drivers/tty\sysrq.c @ 583] 
02 ffff0000`0bc3bcb0 ffff0000`08308990     vmlinux!write_sysrq_trigger+0xb4 [/usr/src/kernel/drivers/tty\sysrq.c @ 1110] 
03 ffff0000`0bc3bcf0 ffff0000`08290070     vmlinux!proc_reg_write+0x80 [/usr/src/kernel/fs/proc\inode.c @ 245] 
04 ffff0000`0bc3bd10 ffff0000`0829039c     vmlinux!__vfs_write+0x60 [/usr/src/kernel/fs\read_write.c @ 490] 
05 ffff0000`0bc3bd50 ffff0000`08290704     vmlinux!vfs_write+0xac [/usr/src/kernel/fs\read_write.c @ 550] 
06 ffff0000`0bc3be00 ffff0000`082907a4     vmlinux!ksys_write+0x74 [/usr/src/kernel/fs\read_write.c @ 599] 
07 (Inline Function) --------`--------     vmlinux!__do_sys_write+0xc [/usr/src/kernel/fs\read_write.c @ 608] 
08 (Inline Function) --------`--------     vmlinux!__se_sys_write+0xc [/usr/src/kernel/fs\read_write.c @ 608] 
09 ffff0000`0bc3be40 ffff0000`08095904     vmlinux!__arm64_sys_write+0x24 [/usr/src/kernel/fs\read_write.c @ 608] 
0a ffff0000`0bc3be90 ffff0000`080834c8     vmlinux!el0_svc_handler+0x94
0b ffff0000`0bc3beb0 00000000`00000000     vmlinux!el0_svc+0x8
```

Use the `dx` command to examine the dump file. For example, look at the first 30 processes using this command.

```dbgcmd
6: kd> dx @$cursession.Processes.Take(30)
@$cursession.Processes.Take(30)                
    [0x0]            : swapper/0 [Switch To]
    [0x1]            : systemd [Switch To]
    [0x2]            : kthreadd [Switch To]
    [0x3]            : rcu_gp [Switch To]
    [0x4]            : rcu_par_gp [Switch To]
    [0x5]            : kworker/0:0 [Switch To]
    [0x6]            : kworker/0:0H [Switch To]
    [0x7]            : kworker/u16:0 [Switch To]
    [0x8]            : mm_percpu_wq [Switch To]
    [0x9]            : ksoftirqd/0 [Switch To]
    [0xa]            : rcu_sched [Switch To]
    [0xb]            : rcu_bh [Switch To]
    [0xc]            : migration/0 [Switch To]
...
```

Click on the DML links, or use commands similar to this one, to look at threads on a process of interest.

```dbgcmd
6: kd> dx @$cursession.Processes[0x1a].Threads
@$cursession.Processes[0x1a].Threads                
    [0x1a]           [Switch To]
6: kd> dx @$cursession.Processes[0x1a].Threads[0x1a]
@$cursession.Processes[0x1a].Threads[0x1a]                 [Switch To]
    KernelObject     [Type: thread_struct]
    Id               : 0x1a
    Stack           
    Registers       
    Environment     
    Analysis        
    WaitChain       
    Scheduling      
    IRPs            
...
```

Additional information for each thread is available, as shown below.

```dbgcmd
6: kd> dx @$cursession.Processes[0x1a].Threads[0x1a].KernelObject
@$cursession.Processes[0x1a].Threads[0x1a].KernelObject                 [Type: thread_struct]
    [+0x000] cpu_context      [Type: cpu_context]
    [+0x070] uw               [Type: <unnamed-tag>]
    [+0x290] fpsimd_cpu       : 0x100 [Type: unsigned int]
    [+0x298] sve_state        : 0x0 [Type: void *]
    [+0x2a0] sve_vl           : 0x0 [Type: unsigned int]
    [+0x2a4] sve_vl_onexec    : 0x0 [Type: unsigned int]
    [+0x2a8] fault_address    : 0x0 [Type: long unsigned int]
    [+0x2b0] fault_code       : 0x0 [Type: long unsigned int]
    [+0x2b8] debug            [Type: debug_info]
6: kd> dx -s @$cursession.Processes[0x1a].Threads[0x1a].SwitchTo()
Process ffff8008`0f894380 has invalid page directories
```

### Use the LinuxKernel.js script to analyze a Linux kernel dump

The LinuxKernel.js debugger extension contains a set of commands designed to function similarly to those found in the Linux crash utility that is used to open and analyze Linux Kernel mode crashes.

To use the script, first load the script.

```dbgcmd
0: kd> .scriptload LinuxKernel.js
JavaScript script successfully loaded from 'C:\Users\Bob\AppData\Local\dbg\UI\Fast.20240423.1\amd64\winext\LinuxKernel.js'
```

For more information about working with loading scripts, see [JavaScript Debugger Scripting](javascript-debugger-scripting.md).

#### !files

Use the `!files` to display information about the Linux file structure in the dump file. It is similar to the crash files command.

```dbgcmd
6: kd> !files
@$files()                 : Files for process 'sh' (pid 545) root dir = '/' working dir = '/home/root'
    [0x0]            : /dev/ttyS0 [Type: file]
    [0x1]            : /proc/sysrq-trigger [Type: file]
    [0x2]            : /dev/ttyS0 [Type: file]
    [0xa]            : /dev/ttyS0 [Type: file]
    [0xff]           : /dev/ttyS0 [Type: file]
```

`!files` syntax:

`!files [<arg>]`

Without `[<arg>]`- Equivalent to 'files' - gives current process file list

`[<arg>]`:

`pid` - Gives the file list for the given process id

`64-bit num` - Gives the file list for the task at the given address

`<task struct [*]>` - Gives the file list for the given task struct by object

`<process object>` - Gives the file list for the task represented by the process object

#### !mount

Use the `!mount` to display information about the Linux file structure in the dump file.

```dbgcmd
6: kd> !mount
@$mount()                
    [0x0]            : (rootfs) rootfs at / [Type: mount]
    [0x1]            : (squashfs) /dev/mapper/nested_rootfs at / [Type: mount]
    [0x2]            : (sysfs) sysfs at /sys [Type: mount]
    [0x3]            : (proc) proc at /proc [Type: mount]
    [0x4]            : (devtmpfs) devtmpfs at /dev [Type: mount]
    [0x5]            : (securityfs) securityfs at /kernel/security [Type: mount]
```

`!mount` syntax:

Without `[<arg>]`- Equivalent to 'mount' command - shows mounted file systems

`[<arg>]`:

`pid` - Gives the mounted file systems for namespace of the process with the given pid

`64-bit num` - Gives the mounted file systems for the namespace of the task_struct given by address

`<task struct [*]>` - Gives the mounted file systems for the namespace of the given task_struct

`<process object>` - Gives the mounted file systems for the namespace of the task represented by the process

#### !net

Use the `!net` to display the system network list.

```dbgcmd
6: kd> !net
@$net()                
    [0x0]            : lo (127.0.0.1) [Type: net_device]
    [0x1]            : enP8p1s0f0np0 (192.168.3.19) [Type: net_device]
    [0x2]            : enP8p1s0f1np0 [Type: net_device]
```

`!net` syntax:

`!net [<arg>]`

 Without `[<arg>]`- Equivalent to 'net' - gives system network list

`[<arg>]`:

`pid` - Gives the net list for namespace of the process with the given pid

`64-bit num` - Gives the net list for the namespace of the task_struct given by address

`<task struct [*]>` - Gives the net list for the namespace of the given task_struct

`<process object>` - Gives the net list for the namespace of the task represented by the process

#### !runq

Use the `!runq` to display information about the tasks on the run queue.

```dbgcmd
0: kd> !runq
@$runq()                
    [0x0]            : CPU 0 run queue [current = 'bash' (17ca)]
        Cpu              : 0x0
        RunQueue         [Type: rq]
        CurrentTask      : bash [Type: task_struct]
        RTTasks         
        CfsTasks        
            [0x16b3]         : kworker/0:7 [Type: task_struct]
    [0x1]            : CPU 1 run queue [current = 'swapper/1' (0)]
        Cpu              : 0x1
        RunQueue         [Type: rq]
        CurrentTask      : swapper/1 [Type: task_struct]
        RTTasks         
        CfsTasks   
```

`!runq` syntax:

`!runq`

!runq does not have any command parameters.

### Additional kernel dump commands

`!dev` - Displays device data concerning the character and block device,  assignments, I/O port usage, I/O memory usage.

`!log` - Displays the kernel log_buf contents.

`!vm` -   Displays a summary of virtual memory usage.

`!timer` - Displays the timer queue entries.

#### dx command and Linux objects

The dx command can be used to investigate kdumps. Display the Sessions object to see the various child objects that are available.  

```dbgcmd
0: kd> dx -r3 Debugger.Sessions[0]
Debugger.Sessions[0]                 : Target Composition Target
    Processes       
        [0x0]            : swapper/0 [Switch To]
            KernelObject     : swapper/0 [Type: task_struct]
            Name             : swapper/0
            Id               : 0x0
            Index            : 0x0
            Threads         
            Modules         
            Environment     
            Direct3D        
            Attributes      
            Devices         
            Io              
            Memory          
            GroupedStacks   
...
```

The cursession Kernel object contains the PrintKLog object that can be used to view the kernel log.

```dbgcmd
6: kd> dx @$cursession.Kernel.PrintKLog.Take(4)
@$cursession.Kernel.PrintKLog.Take(4)                
    [0x0]            : [     0.000000] Booting Linux on physical CPU 0x0000000000 [0x410fd083]
    [0x1]            : [     0.000000] Linux version 4.19.90-microsoft-standard (oe-user@oe-host) (gcc version 8.2.0 (GCC)) #1 SMP Fri Mar 27 14:25:24 UTC 2020..
    [0x2]            : [     0.000002] sched_clock: 64 bits at 125MHz, resolution 8ns, wraps every 4398046511100ns
    [0x3]            : [     0.000003]         17.250901928 MSFT: kernel boot start
```

This dx command shows the use of `.Contains()` to look for specific strings in the log.

```dbgcmd
6: kd> dx @$cursession.Kernel.PrintKLog.Where(le => le.ToLower().Contains("oops") || le.ToLower().Contains("crash"))
@$cursession.Kernel.PrintKLog.Where(le => le.ToLower().Contains("oops") || le.ToLower().Contains("crash"))                
    [0x0]            : [     0.000493] crashkernel reserved: 0x00000000dc600000 - 0x00000000fc600000 (512 MB)
    [0x1]            : [     0.078790] Kernel command line: console=ttyS0,115200n8 earlycon=uart8250,mmio32,0x68A10000 crashkernel=512M enforcing=0 ipe.enforce=0
    [0x2]            : [    26.621228] sysrq: SysRq : Trigger a crash
    [0x3]            : [    26.621254] Internal error: Oops: 96000044 [#1] SMP
    [0x4]            : [    26.656655] pc : sysrq_handle_crash+0x24/0x30
    [0x5]            : [    26.753494]  sysrq_handle_crash+0x24/0x30
    [0x6]            : [    26.801441] Starting crashdump kernel...8J»=.
```

Use `.Reverse()` to show the last events logged.

```dbgcmd
2: kd> dx @$cursession.Kernel.PrintKLog.Reverse().Take(5).Reverse()
@$cursession.Kernel.PrintKLog.Reverse().Take(5).Reverse()
   [0x0]           : [3147944.378367]  kthread+0x118/0x2a4
   [0x1]           : [3147944.381876]  ret_from_fork+0x10/0x18
   [0x2]           : [3147944.385747] Code: 78002507 36000042 39000107 d65f03c0 (cb0803e4)
   [0x3]           : [3147944.392221] SMP: stopping secondary CPUs
   [0x4]           : [3147944.397539] Starting crashdump kernel...
```

For more information about using LINQ queries with the dx command, see [Using LINQ With the debugger objects](using-linq-with-the-debugger-objects.md).

## Linux diagnostic extensions - ELFBinComposition.dll

The following Linux dump file diagnostic extensions are available in the ELFBinComposition.dll.

### Dump file commands

These commands can be used on most dump files.

`!dumpdebug` - Display diagnostics for the core dump being debugged. This includes the output of various other commands.

`!ntprstatus` - Display the NT_PRSTATUS records from the core dump being debugged.

`!vmcoreinfo` - Display the VMCOREINFO table from the kernel core dump (KDUMP) being debugged.

### ELF dump commands

These commands can only be used on an ELF core dump files.

`!corephdrs` - Display the program header table for the core dump being debugged.

`!ntprpsinfo` - Display the NT_PRPSINFO data from the core dump being debugged.

`!ntfile` - Display the NT_FILE data from the core dump being debugged.

`!ntauxv` - Display the NT_AUXV data from the core dump being debugged.

### Kernel crash dump file commands

These commands can be used only on kernel core dump (KDUMP) files.

`!kdumpdescs` - Display the list of page ranges & page descriptors in a KDUMP.

`!kdumppagerange <n>` - Display information about the n-th grouping of pages in the KDUMP.

`!kdumppfn <pfn>` - Display information about the page frame `<pfn>` and where its data is within the KDUMP.

### Other diagnostic commands

`!cppex` - Displays information about the current in-flight (uncaught and "just" caught) C++ exceptions for the current thread, using libstdc++'s internal structures and DWARF symbols.

`!cppfilt [-n] <mangled name>`  -  Demangles a C++ mangled name as if it were run through the c++filt tool. For more information about  C==filtr tool, see [c++filt(1) — Linux manual page](https://www.man7.org/linux/man-pages/index.html).

`!rustdemangle <mangled name>` - Demangles a Rust mangled name. For more information about rust symbol name mangling, see [Rust Symbol Mangling - RFC 2603](https://rust-lang.github.io/rfcs/2603-rust-symbol-name-mangling-v0.html).  

## See also

[Linux symbols and sources](linux-dwarf-symbols.md)

[Linux live remote process debugging](linux-live-remote-process-debugging.md)
