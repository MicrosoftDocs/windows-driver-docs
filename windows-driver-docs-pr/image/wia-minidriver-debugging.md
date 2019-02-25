---
title: WIA Minidriver Debugging
description: WIA Minidriver Debugging
ms.assetid: 6466d0db-a2f9-4b3e-aa3e-8030b243f862
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# WIA Minidriver Debugging





WIA drivers execute inside the WIA service process. Therefore, in order to perform user-mode debugging of these drivers, you must connect the debugger to the WIA service. There are several different ways to do this; this topic presents two of them. (See Debugging Services in the Microsoft Windows SDK documentation for additional information).

Your debugger can be started in one of two ways:

-   By automatically starting the WIA service under a debugger.

-   By attaching the debugger to the appropriate process at run time.

Following are two points to keep in mind:

If you require network access to symbols and other files from within the debugger, these may not be visible if you automatically start the WIA service under the debugger. WIA runs as a LocalSystem service in Windows XP and as a LocalService for Microsoft Windows Server 2003 and later operating system versions and does not have the appropriate privileges to access the network. So, even though your machine can "see" everything on your network, the debugger running the service may not be able to. For more information about the WIA service's changed privilege level, see [Security Issues for WIA Drivers](security-issues-for-wia-drivers.md).

-   If a problem occurs during driver loading or initialization of the STI portion of the driver (for example, during [**IStiUSD::Initialize**](https://msdn.microsoft.com/library/windows/hardware/ff543824)), then by the time a debugger is attached, the error has already occurred and it is too late to get useful information. A common symptom of this problem is that the device does not show up in the **My Computer** folder, but *does* show up in the **Device Manager** folder.

### Starting the WIA Service Under a Debugger

When the WIA service is started, the service control manager (SCM) looks at the entry in the service control database and launches the executable file pointed to by that entry. A simple way to start the WIA service under a debugger is to replace that entry with one that includes your debugger. The entry can be found in the registry under:

**HKLM\\System\\CurrentControlSet\\Services\\StiSvc\\ImagePath**

Initially, the **ImagePath** key is set to the following string value:

"**%SystemRoot%\\System32\\svchost.exe -k imgsvc**"

To run the WIA service under NTSD, for example, modify the preceding value as follows:

"**ntsd -g -G %SystemRoot%\\System32\\svchost.exe -k imgsvc**"

With this change, the WIA service always starts under NTSD. Note that if the service is already running, it must be stopped and restarted before this change takes effect. See [Starting and Stopping the Still Image Service](starting-and-stopping-the-still-image-service.md) for details.

To make the debugger's window visible, you also need to change another registry key. The path to this registry key is:

**HKLM\\System\\CurrentControlSet\\Services\\StiSvc\\Type**

The initial value of the **Type** key, 0X20, prevents the debugger window from being displayed. Change the value of the **Type** key to the DWORD value 0X120.

### Attaching the Debugger at Run Time

Most debuggers require the PID of the running process in order to attach to it after the process has already started. Because WIA runs under a generic hosting process called *svchost.exe*, finding the correct instance of *svchost.exe* is essential.

If you downloaded the debugger package from the Microsoft site (www.microsoft.com), it includes a utility program named *tlist.exe*. *Tlist.exe* displays all running processes. If you execute *tlist.exe* using the s switch, this utility also shows which processes are hosting which services. For example, running *tlist.exe -s* produces output similar to the following:

```console
   0 System Process
   4 System
 160 smss.exe
 216 csrss.exe       Title:
 208 winlogon.exe    Title: NetDDE Agent
 268 services.exe    Svcs:  Eventlog,PlugPlay
 280 lsass.exe       Svcs:  Netlogon,PolicyAgent,ProtectedStorage,SamSs
 416 svchost.exe     Svcs:  RpcSs
 444 svchost.exe     Svcs:  AudioSrv,CryptSvc,Dhcp,EventSystem,FastUserSwitching,CompatibilityServices,helpsvc,Irmon,lanmanserver,lanmanworkstation,Netman,Nla,Schedule,SENS,ShellHWDetection,srservice,TapiSrv,TermService,ThemeService,uploadmgr,W32Time,winmgmt,WmdmPmSp
 504 svchost.exe     Svcs:  Dnscache
 372 svchost.exe     Svcs:  LmHosts,Messenger,RemoteRegistry,SSDPSRV,WebClient
 616 spoolsv.exe     Svcs:  Spooler
 680 inojobsv.exe    Svcs:  Cheyenne InocuLAN Anti-Virus Server
 700 emsvc.exe       Svcs:  EMSVC
 912 fxssvc.exe      Svcs:  Fax
 192 explorer.exe    Title: Program Manager
1076 svchost.exe     Svcs:  stisvc
22824 tlist.exe
```

In the preceding example, five instances of *svchost.exe* are running. The WIA service, **StiSvc** (Still Image service), is running under the *svchost.exe* instance whose PID is 1076. Attach the debugger to process 1076 to start debugging.

Instead of using a utility program such as *tlist.exe,* to identify a single instance of multiple *svchost.exe* instances, you can make a copy of *svchost.exe* and rename it (for example, *stisvc.exe*). Then, change the service control entry's **ImagePath** value to use this copy of *svchost.exe* (the one whose name is now *stisvc.exe*). For example, you can set the key whose path is

**HKLM\\System\\CurrentControlSet\\Control\\Services\\Stisvc\\ImagePath**

to the following string value:

"**%SystemRoot%\\System32\\stisvc.exe -k imgsvc**"

Now, when the WIA service starts, it runs under *stisvc.exe* instead of *svchost.exe*. Finding this process is simpler, because there is only a single instance of *stisvc.exe*. You do not have to look for the PID to find it. Thus, for example, if you are developing the driver using Microsoft Visual Studio, you can go to the **Start Debug** menu item under the **Build** menu, click **Attach to Process...**, and select *stisvc.exe* in the list.
