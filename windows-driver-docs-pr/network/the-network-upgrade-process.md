---
title: The Network Upgrade Process
description: The Network Upgrade Process
ms.assetid: f89cb7c2-8375-4326-94c8-70e2a5e3a1f7
keywords:
- network component upgrades WDK , phases
- upgrading network components WDK , phases
- AnswerFile WDK networking
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# The Network Upgrade Process





**Note**  Vendor-supplied network upgrades are not supported in Microsoft Windows XP (SP1 and later), Microsoft Windows Server 2003, and later operating systems.

 

The network upgrade process is divided into three distinct phases, which can be briefly summarized as follows:

-   **Winnt32 phase**

    Winnt32.exe calls NetSetup. NetSetup writes network component-specific information to the AnswerFile and calls any vendor-supplied network migration DLLs. The DLLs write component-specific information to the AnswerFile. Winnt32.exe copies the Microsoft Windows 2000 or later files to the system being upgraded and prepares the boot sector on the system. The system then boots into text mode.

-   **Text mode phase**

    Installation messages are displayed on a blue, text-based screen. Setup performs the basic Windows 2000 or later installation. The system then boots into GUI mode.

-   **GUI mode phase**

    NetSetup processes the winnt.sif file, which is also known as the AnswerFile, and installs the network components. Network migration DLLs can display a user interface in which a user or system administrator can specify parameter values for network components. Either NetSetup or a network migration DLL writes a network component's preupgrade parameter values to the Windows 2000 or later registry.

The phases of the network upgrade process are described in more detail in the following topics:

[Winnt32 Phase of the Network Upgrade Process](winnt32-phase-of-the-network-upgrade-process.md)

[Text Mode Phase of the Network Upgrade Process](text-mode-phase-of-the-network-upgrade-process.md)

[GUI Mode Phase of the Network Upgrade Process](gui-mode-phase-of-the-network-upgrade-process.md)

 

 





