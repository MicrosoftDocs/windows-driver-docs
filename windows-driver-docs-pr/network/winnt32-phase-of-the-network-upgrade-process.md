---
title: Winnt32 Phase of the Network Upgrade Process
description: Winnt32 Phase of the Network Upgrade Process
ms.assetid: a83edcfb-e075-4763-8a6a-33879ccf2357
keywords:
- network component upgrades WDK , phases
- upgrading network components WDK , phases
- Winnt32 phase WDK networking
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Winnt32 Phase of the Network Upgrade Process





**Note**  Vendor-supplied network upgrades are not supported in Microsoft Windows XP (SP1 and later), Microsoft Windows Server 2003, and later operating systems.

 

The user or system administrator starts the upgrade process by taking either of the following actions:

-   Selecting the component upgrade in the user interface that is displayed after the Windows 2000 or later CD-ROM spins up

-   Selecting and running \\i386\\winnt32.exe on the CD-ROM

If the user or system administrator has set the NETUPGRD\_INIT\_FILE\_DIR environment variable on the system being upgraded, NetSetup searches for a [netupg.inf](creating-a-netupg-inf-file.md) file in the directory specified by that variable. The netupg.inf file contains only one section: **OemNetUpgradeDirs**. Each entry in this section specifies the complete path to a directory that contains the vendor-supplied upgrade files, including a [netmap.inf](creating-a-netmap-inf-file.md) file, for a network component. If the NETUPGRD\_INIT\_FILE\_DIR environment variable is not set, NetSetup (netupgrd.dll) looks for netmap.inf files in its own directory.

NetSetup reads the netmap.inf files to identify the network components that do not have built-in upgrade support. If NetSetup is running in unattended mode, it displays a wizard; however, the user or system administrator cannot use the wizard. If NetSetup is not running in unattended mode, the wizard displays a list of the network components that do not have built-in upgrade support.

Using the wizard, a user or system administrator can:

-   Click **Cancel** to abort the installation of the operating system.

-   Click **Next** to install the operating system without upgrading the listed network components.

-   Specify the drive and directory location of vendor-supplied upgrade files for listed network components.

    NetSetup reads the netmap.inf file at the specified location and copies the vendor-supplied upgrade files at that location to a temporary directory on the system's hard disk. This temporary directory becomes the working directory for the vendor-supplied network migration DLL. NetSetup also removes any component that has a netmap.inf file from the component list in the wizard.

NetSetup generates the winnt.sif file (also known as the AnswerFile) in the $Win\_nt$.~bt directory, which is usually located on the C: drive.

NetSetup generates the AnswerFile as follows:

1.  NetSetup reads the registry of the preupgraded system to enumerate each network component. For each network component that has built-in upgrade support, NetSetup writes the information that is read from the registry to the AnswerFile.

2.  For each network component that does not have built-in upgrade support, NetSetup reads the component's netmap.inf file. The netmap.inf file maps the preupgrade device, hardware, or compatible ID of a network component to the corresponding ID in the upgraded operating system. If NetSetup matches the preupgrade ID of the network component that it read from the registry with a preupgrade ID in the **OemNetAdapters**, **OemNetProtocols**, **OemNetServices**, or **OemAsyncAdapters** section of the netmap.inf file, NetSetup writes vendor-provided information for the component to the AnswerFile.

3.  Using the component's operating system device, hardware, or compatible ID, NetSetup reads the **OemUpgradeSupport** section of the netmap.inf file to determine which network migration DLL to load. NetSetup then loads the network migration DLL, and calls the DLL's [**PreUpgradeInitialize**](https://msdn.microsoft.com/library/windows/hardware/ff562439) function. The **PreUpgradeInitialize** function supplies information that the DLL uses to initialize itself.

4.  NetSetup calls the DLL's [**DoPreUpgradeProcessing**](https://msdn.microsoft.com/library/windows/hardware/ff545634) function once for each network component supported by the network migration DLL. **DoPreUpgradeProcessing** reads a network component's preupgrade parameter values from the registry and calls the [**NetUpgradeAddSection**](https://msdn.microsoft.com/library/windows/hardware/ff559063) and [**NetUpgradeAddLineToSection**](https://msdn.microsoft.com/library/windows/hardware/ff559059) functions to write these parameters, along with other component-specific information, to the AnswerFile. **DoPreUpgradeProcessing** can also migrate binary data associated with the preupgraded component by making appropriate entries in the AnswerFile.

5.  After the AnswerFile is completely generated, NetSetup copies the vendor-supplied upgrade files to the appropriate directories and then boots into the text mode phase of the upgrade process.

 

 





