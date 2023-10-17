---
title: DumpChk
description: Learn about DumpChk (the Microsoft Crash Dump File Checker tool), which is a program that performs a quick analysis of a crash dump file.
keywords: ["DumpChk"]
ms.date: 03/07/2023
---

# DumpChk

**DumpChk** (the Microsoft Crash Dump File Checker tool) is a program that performs a quick analysis of a crash dump file. This tool enables you to see summary information about what the dump file contains. You can use **DumpChk** to find dump files that are corrupt and can't be opened by a debugger.

## Where to get DumpChk

DumpChk.exe is included in [Debugging Tools for Windows](index.md).

## DumpChk command-line options

```dbgcmd
DumpChk [-y SymbolPath] DumpFile
```

### Parameters

**-y SymbolPath**  
*SymbolPath* specifies where **DumpChk** is to search for symbols. Symbol information might be necessary for some dump files. It can also help to improve the information shown in the dump file by allowing symbol names to be resolved.

**DumpFile**  
*DumpFile* specifies the crash dump file that's to be analyzed. It might include an absolute or relative directory path or a universal naming convention (UNC) path. If *DumpFile* contains spaces, it must be enclosed in quotation marks.

## How to use DumpChk

The following example shows a corrupt dump file. The error shown at the end, `DebugClient cannot open DumpFile`, indicates that some kind of corruption must have occurred.

```console
C:\Debuggers> dumpchk C:\mydir\dumpfile2.dmp 

Loading dump file C:\mydir\dumpfile2.dmp

Microsoft (R) Windows Debugger Version 6.9.0003.113 X86
Copyright (C) Microsoft. All rights reserved.


Loading Dump File [C:\mydir\dumpfile2.dmp]
Could not match Dump File signature - invalid file format
Could not open dump file [C:\mydir\dumpfile2.dmp], HRESULT 0x80004002
    "No such interface supported"
**** DebugClient cannot open DumpFile - error 80004002   
```

 The `DebugClient cannot open DumpFile` error message at the end shows that the dump file couldn't be opened. If the dump file wasn't corrupt, this display would end with the words `Finished dump check`.

Other errors might be listed, some of which are benign. For example, the following error message doesn't represent a problem:

```dbgcmd
error 3 InitTypeRead( nt!_PEB at 7ffd5000) 
```

The following example shows DumpChk run on a healthy user-mode minidump. The display begins with an overall summary of the dump file and then gives detailed information about what data is contained in the dump file:

```console
C:\Debuggers> dumpchk C:\mydir\dumpfile1.dmp 

Loading dump file C:\mydir\dumpfile1.dmp

Microsoft (R) Windows Debugger Version 6.9.0003.113 X86
Copyright (C) Microsoft. All rights reserved.


Loading Dump File [C:\mydir\dumpfile1.dmp]
User Mini Dump File with Full Memory: Only application data is available

Symbol search path is: srv*C:\CODE\LocalStore*\\symbols\symbols
Executable search path is: 
Windows Vista Version 6000 MP (2 procs) Free x86 compatible
Product: WinNt, suite: SingleUserTS
Debug session time: Tue Jun 17 02:28:23.000 2008 (GMT-7)
System Uptime: 0 days 15:43:52.861
Process Uptime: 0 days 0:00:26.000
...
This dump file has an exception of interest stored in it.
The stored exception information can be accessed via .ecxr.

----- User Mini Dump Analysis

MINIDUMP_HEADER:
Version         A793 (6903)
NumberOfStreams 12
Flags           1826
                0002 MiniDumpWithFullMemory
                0004 MiniDumpWithHandleData
                0020 MiniDumpWithUnloadedModules
                0800 MiniDumpWithFullMemoryInfo
                1000 MiniDumpWithThreadInfo

Streams:
Stream 0: type ThreadListStream (3), size 00000064, RVA 000001BC
  2 threads
  RVA 000001C0, ID 1738, Teb:000000007FFDF000
  RVA 000001F0, ID 1340, Teb:000000007FFDE000
Stream 1: type ThreadInfoListStream (17), size 0000008C, RVA 00000220
  RVA 0000022C, ID 1738
  RVA 0000026C, ID 1340
Stream 2: type ModuleListStream (4), size 00000148, RVA 000002AC
  3 modules
  RVA 000002B0, 00400000 - 00438000: 'C:\CODE\TimeTest\Debug\TimeTest.exe'
  RVA 0000031C, 779c0000 - 77ade000: 'C:\Windows\System32\ntdll.dll'
  RVA 00000388, 76830000 - 76908000: 'C:\Windows\System32\kernel32.dll'
Stream 3: type Memory64ListStream (9), size 00000290, RVA 00001D89
  40 memory ranges
  RVA 0x2019 BaseRva
  range#    RVA      Address      Size
       0 00002019    00010000   00010000
       1 00012019    00020000   00005000
       2 00017019    0012e000   00002000

 (additional stream data deleted)   

Stream 9: type UnusedStream (0), size 00000000, RVA 00000000
Stream 10: type UnusedStream (0), size 00000000, RVA 00000000
Stream 11: type UnusedStream (0), size 00000000, RVA 00000000


Windows Vista Version 6000 MP (2 procs) Free x86 compatible
Product: WinNT, suite: SingleUserTS
kernel32.dll version: 6.0.6000.16386 (vista_rtm.061101-2205)
Debug session time: Tue Jun 17 02:28:23.000 2008 (GMT-7)
System Uptime: 0 days 15:43:52.861
Process Uptime: 0 days 0:00:26.000
  Kernel time: 0 days 0:00:00.000
  User time: 0 days 0:00:00.000
PEB at 7ffd9000
    InheritedAddressSpace:    No
    ReadImageFileExecOptions: No
    BeingDebugged:            Yes
    ImageBaseAddress:         00400000
    Ldr                       77a85d00
    Ldr.Initialized:          Yes
    Ldr.InInitializationOrderModuleList: 002c1e30 . 002c2148
    Ldr.InLoadOrderModuleList:           002c1da0 . 002c2138
    Ldr.InMemoryOrderModuleList:         002c1da8 . 002c2140
            Base TimeStamp                     Module
          400000 47959d85 Jan 21 23:38:45 2008 C:\CODE\TimeTest\Debug\TimeTest.exe
        779c0000 4549bdc9 Nov 02 02:43:37 2006 C:\Windows\system32\ntdll.dll
        76830000 4549bd80 Nov 02 02:42:24 2006 C:\Windows\system32\kernel32.dll
    SubSystemData:     00000000
    ProcessHeap:       002c0000
    ProcessParameters: 002c14c0
    WindowTitle:  'C:\CODE\TimeTest\Debug\TimeTest.exe'
    ImageFile:    'C:\CODE\TimeTest\Debug\TimeTest.exe'
    CommandLine:  '\CODE\TimeTest\Debug\TimeTest.exe'
    DllPath:      'C:\CODE\TimeTest\Debug;C:\Windows\system32;C:\Windows\system;
    Environment:  002c0808
        =C:=C:\CODE
        =ExitCode=00000000
        ALLUSERSPROFILE=C:\ProgramData
        AVENGINE=C:\PROGRA~1\CA\SHARED~1\SCANEN~1
        CommonProgramFiles=C:\Program Files\Common Files
        COMPUTERNAME=EMNET
        ComSpec=C:\Windows\system32\cmd.exe
        configsetroot=C:\Windows\ConfigSetRoot
        FP_NO_HOST_CHECK=NO
        HOMEDRIVE=C:
        NUMBER_OF_PROCESSORS=2
        OS=Windows_NT
        Path=C:\DTFW\200804~2.113\winext\arcade;C:\Windows\system32
        PATHEXT=.COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC
        PROCESSOR_ARCHITECTURE=x86
        PROCESSOR_IDENTIFIER=x86 Family 6 Model 15 Stepping 13, GenuineIntel
        PROCESSOR_LEVEL=6
        PROCESSOR_REVISION=0f0d
        ProgramData=C:\ProgramData
        ProgramFiles=C:\Program Files
        PROMPT=$P$G
        PUBLIC=C:\Users\Public
        RoxioCentral=C:\Program Files\Common Files\Roxio Shared\9.0\Roxio Central33\
        SESSIONNAME=Console
        SystemDrive=C:
        SystemRoot=C:\Windows
        USERDNSDOMAIN=NORTHSIDE.COMPANY.COM
        USERDOMAIN=NORTHSIDE
        USERNAME=myname
        USERPROFILE=C:\Users\myname
        WINDBG_DIR=C:\DTFW\200804~2.113
        windir=C:\Windows
        WINLAYTEST=200804~2.113
        _NT_SOURCE_PATH=C:\mysources
        _NT_SYMBOL_PATH=C:\mysymbols
Finished dump check
```

The output begins by identifying the characteristics of the dump file. In this case, a user-mode minidump with full memory information, including application data but not operating-system data. The symbol path that's being used by DumpChk follows, and then a summary of the dump file contents.

Because this display ends with the words `Finished dump check`, the dump file is probably not corrupt and can be opened by a debugger. However, more subtle forms of corruption might still be present in the file.

## See also

[Tools included in Debugging Tools for Windows](extra-tools.md)
