---
title: Setting Up the Test System
description: Setting Up the Test System
ms.assetid: 99c591e0-fe01-4db9-af95-4ce458625bfb
keywords:
- testing network component upgrades WDK
- upgrade tests WDK networking
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Setting Up the Test System





**Note**  Vendor-supplied network upgrades are not supported in Microsoft Windows XP (SP1 and later), Microsoft Windows Server 2003, and later operating systems.

 

Before you upgrade network components, make sure that the network components to be upgraded are correctly installed and configured.

**To set up the test system**

1.  Create one partition for the preupgrade operating system and another partition for the Microsoft Windows 2000 or later operating system.
    **Note**  Do not install the preupgrade operating system and the upgrade operating system in the same partition. If the preupgrade operating system and Windows 2000 or later are installed in the same partition, they will share the same Program Files directory.

     

2.  On the test system, boot an operating system build other than the one to be upgraded. Then copy the entire partition to be upgraded, except for the pagefile.sys file, into a back-up directory. There is no need to copy the pagefile.sys file, since it is created on the start-up of Windows 2000 or later.

    This method of creating a back-up installation is preferable to creating a disk-image program, because it allows you to use **xcopy**, which takes less time to copy files than a disk-image program. You can repeat an upgrade test by simply copying the contents of the back-up partition into a new partition to be upgraded; it is not necessary to reinstall the preupgrade operating system.

3.  Create a test directory for storing the network migration DLL and the netmap.inf file, and then copy these files to the test directory.

4.  Create another directory for storing the Windows 2000 or later files required for the Winnt32 upgrade phase.

5.  Insert the Windows 2000 or later Driver Development Kit (DDK) CD-ROM that contains the checked build of Windows 2000 or later. From the \\i386 directory on the CD-ROM, copy the following files to the back-up directory (Step 2):
    -   winnt32.exe
    -   winnt32u.dll
    -   pidgen.dll
    -   wetuplog.\*

6.  Create an upgrade directory named winntupg. Copy the files in the \\i386\\winntupg directory on the CD-ROM to the winntupg directory on the test system.

7.  Enable the debugger on the text system or start debugmon.exe, which is included with the Resource Kit for Windows 2000 or later operating systems. Then copy a netcfg.ini file to %windir%. The netcfg.ini file enables debug tracing.

    The following is a sample netcfg.ini file:

    ```INI
    [DebugFlags]
    BreakOnAddLegacy=0
    BreakOnAlloc=0
    BreakonDoUnattend=0
    BreakonDwrefProblem=0
    BreakOnError=0
    BreakOnHr=0
    BreakOnHrInteraction=0
    BreakOnIteration=0
    BreakOnNetInstall=0
    BreakOnWizard=0
    DisableTray=0
    DumpLeaks=0
    DumpNetCfgTree=0
    NetShellBreakOnInit=0
    ShowIngnoreErrors=0
    ShowProcessAndThreadIds=0
    SkipLanEnum=0
    TracingTimeStamps=0

    [Default]
    OutputToDebug=1

    [EsLocks]
    OutputToDebug=0

    [ShellViewMsgs]
    OutputToDebug=0

    [OptErrors]
    OutputToDebug=0
    ```

 

 





