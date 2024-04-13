---
title: Writing a Network Migration DLL
description: Writing a Network Migration DLL
keywords:
- network migration DLL WDK
- network component upgrades WDK , network migration DLL
- upgrading network components WDK , network migration DLL
- migration DLL WDK networking
- writing network migration DLL
- DLLs WDK network migration
ms.date: 04/20/2017
---

# Writing a Network Migration DLL





**Note**  Vendor-supplied network upgrades are not supported in Microsoft Windows XP (SP1 and later), Microsoft Windows Server 2003, and later operating systems.

 

A network migration DLL migrates the parameter values for one or more network components from Microsoft Windows NT 3.51 or Windows NT 4.0 to Windows 2000 or later.

A network migration DLL must:

-   **Load under the preupgrade operating system (Windows NT 3.51 or Windows 4.0)**

    The DLL cannot call any functions specific to Windows 2000 or later or use any features specific to Windows 2000 or later. If the DLL runs in the postupgrade (GUI mode) phase, it must also load under Windows 2000 and later operating systems.

-   **Export the** [**PreUpgradeInitialize**](/previous-versions/windows/hardware/network/ff562439(v=vs.85))**and**[**DoPreUpgradeProcessing**](/previous-versions/windows/hardware/network/ff545634(v=vs.85))**functions**

    If the DLL runs in the GUI mode phase, it must export the [**PostUpgradeInitialize**](/previous-versions/windows/hardware/network/ff562410(v=vs.85)) and [**DoPostUpgradeProcessing**](/previous-versions/windows/hardware/network/ff545629(v=vs.85)) functions, as well.

-   **Make no irreversible changes during the Winnt32 phase**

    The DLL must not make any irreversible changes, such as deleting files or modifying registry keys, during this phase because a user can cancel the upgrade of a network component or the operating system. The DLL can, however, modify files in its temporary working directory, which is specified by NetSetup in the call to **PreUpgradeInitialize**.

 

