---
title: TList Examples
description: TList Examples
ms.assetid: 9c9a1e81-03c2-4b7c-b0da-b25942548aa9
keywords: ["TList, TList examples"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# TList Examples


## <span id="ddk_tlist_examples_dtools"></span><span id="DDK_TLIST_EXAMPLES_DTOOLS"></span>


The following examples demonstrate how to use TList.

### <span id="simplest_tlist_command__tlist_"></span><span id="SIMPLEST_TLIST_COMMAND__TLIST_"></span>Simplest TList Command (tlist)

Typing **tlist** without additional parameters displays a list of running processes, their process IDs (PIDs), and the title of the window in which they are running, if any.

```console
c:\>tlist

   0 System Process  
   4 System          
 308 smss.exe        
 356 csrss.exe         
 380 winlogon.exe      NetDDE Agent
 424 services.exe    
 436 lsass.exe       
 604 svchost.exe     
 776 svchost.exe     
 852 spoolsv.exe     
1000 clisvcl.exe     
1036 InoRpc.exe      
1064 InoRT.exe       
1076 InoTask.exe     
1244 WTTSvc.exe        
1492 Sysparse_com.exe  OleMainThreadWndName
1980 explorer.exe      Program Manager
1764 launch32.exe      SMS Client User Application Launcher 
1832 msmsgs.exe        MSBLNetConn
2076 ctfmon.exe        
2128 ISATRAY.EXE       IsaTray
4068 tlist.exe   
```

### <span id="find_a_process_id___p_"></span><span id="FIND_A_PROCESS_ID___P_"></span>Find a process ID (-p)

The following command uses the **-p** parameter and process name to find the process ID of the Explorer.exe (Explorer) process.

In response, TList displays the process ID of the Explorer process, 328.

```console
c:\>tlist -p explorer
328
```

### <span id="find_process_details_using_pid"></span><span id="FIND_PROCESS_DETAILS_USING_PID"></span>Find process details using PID

The following command uses the process ID of the process in which Explorer is running to find detailed information about the Explorer process.

```console
c:\>tlist 328
```

In response, TList displays details of the Explorer process including the following elements:

-   Process ID, executable name, program friendly name.

-   Current working directory (CWD).

-   The command line that started the process (CmdLine).

-   Current virtual address space values.

-   Number of threads.

-   A list of threads running in the process. For each thread, TList displays the thread ID (TID), the function that the thread is running, the address of the entry point, the address of the last reported error (if any), and the thread state.

-   A list of the modules loaded for the process. For each module, TList displays the version number, attributes, virtual address of the module, and the module name.

The following is an excerpt of the output resulting from this command.

```console
 328 explorer.exe      Program Manager
   CWD:     C:\Documents and Settings\user01\
   CmdLine: C:\WINDOWS\Explorer.EXE
   VirtualSize:    90120 KB   PeakVirtualSize:   104844 KB
   WorkingSetSize: 19676 KB   PeakWorkingSetSize: 35716 KB
   NumberOfThreads: 17
    332 Win32StartAddr:0x010160cc LastErr:0x00000008 State:Waiting
   1232 Win32StartAddr:0x70a7def2 LastErr:0x00000000 State:Waiting
   1400 Win32StartAddr:0x77f883de LastErr:0x00000000 State:Waiting
   1452 Win32StartAddr:0x77f91e38 LastErr:0x00000000 State:Waiting
   1484 Win32StartAddr:0x70a7def2 LastErr:0x00000006 State:Waiting
   1904 Win32StartAddr:0x74b02ed6 LastErr:0x00000000 State:Ready
   1948 Win32StartAddr:0x72d22ecc LastErr:0x00000000 State:Waiting
   ....  (thread data deleted here)

  6.0.2800.1106 shp  0x01000000  Explorer.EXE
  5.1.2600.1217 shp  0x77F50000  ntdll.dll
  5.1.2600.1106 shp  0x77E60000  kernel32.dll
  7.0.2600.1106 shp  0x77C10000  msvcrt.dll
  5.1.2600.1106 shp  0x77DD0000  ADVAPI32.dll
  5.1.2600.1254 shp  0x78000000  RPCRT4.dll
  5.1.2600.1106 shp  0x77C70000  GDI32.dll
  5.1.2600.1255 shp  0x77D40000  USER32.dll
  ....  (module data deleted here)
```

### <span id="find_multiple_processes__pattern_"></span><span id="FIND_MULTIPLE_PROCESSES__PATTERN_"></span>Find multiple processes (Pattern)

The following command searches for processes by a regular expression that represents the process name or window name of one or more processes. In this example, the command searches for a process whose process name or window name begins with "ino."

```console
c:\>tlist ino*
```

In response, TList displays process details for Inorpc.exe, Inort.exe, and Inotask.exe. For a description of the output, see the "Find process details using PID" subsection above.

### <span id="display_a_process_tree___t_"></span><span id="DISPLAY_A_PROCESS_TREE___T_"></span>Display a process tree (/t)

The following command displays a tree that represents the processes running on the computer. Processes appear as the children of the process that created them.

```console
c:\>tlist /t
```

The resulting process tree follows. This tree shows, among other things, that the System (4) process created the Smss.exe process, which created Csrss.exe, Winlogon.exe, Lsass.exe and Rundll32.exe. Also, Winlogon.exe created Services.exe, which created all of the service-related processes.

```console
System Process (0)
System (4)
  smss.exe (404)
    csrss.exe (452)
    winlogon.exe (476) NetDDE Agent
      services.exe (520)
        svchost.exe (700)
        svchost.exe (724)
        svchost.exe (864)
        svchost.exe (888)
        spoolsv.exe (996)
        scardsvr.exe (1040)
        alg.exe (1172)
        atievxx.exe (1200) ATI video bios poller
        InoRpc.exe (1248)
        InoRT.exe (1264)
        InoTask.exe (1308)
        mdm.exe (1392)
        dllhost.exe (2780)
      lsass.exe (532)
      rundll32.exe (500)
explorer.exe (328) Program Manager
  WLANMON.exe (1728) TI Wireless LAN Monitor
  ISATRAY.EXE (1712) IsaTray
  cmmon32.exe (456)
  WINWORD.EXE (844) Tlist.doc - Microsoft Word
  dexplore.exe (2096) Platform SDK - CreateThread
```

### <span id="find_process_by_module___m_"></span><span id="FIND_PROCESS_BY_MODULE___M_"></span>Find process by module (/m)

The following command finds all of the processes running on the computer that load a particular DLL.

```console
c:\>tlist /m 
```

In response, TList displays process details for Inorpc.exe, Inort.exe, and Inotask.exe. For a description of the output, see the "Find process details using PID" subsection above.

 

 





