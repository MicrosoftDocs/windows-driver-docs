---
title: GUI Mode Phase of the Network Upgrade Process
description: GUI Mode Phase of the Network Upgrade Process
ms.assetid: 35c382aa-5905-4a22-b9fa-b876d1373b94
keywords:
- network component upgrades WDK , phases
- upgrading network components WDK , phases
- GUI mode phase WDK networking
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# GUI Mode Phase of the Network Upgrade Process





**Note**  Vendor-supplied network upgrades are not supported in Microsoft Windows XP (SP1 and later), Microsoft Windows Server 2003, and later operating systems.

 

Before the Windows 2000 or later operating system is installed on the system, NetSetup reads the network-specific information that was written to the AnswerFile during the Winnt32 phase.

If a network migration DLL wrote the [**InfToRunBeforeInstall**](https://msdn.microsoft.com/library/windows/hardware/ff559059) key to a component's *OEM section* in the AnswerFile, NetSetup finds the INF file and section specified by the key and processes the INF directives in this section. This section usually contains the **AddReg**, **DelReg**, **AddService**, or **DelService** directives.

After the Windows 2000 or later operating system is installed, NetSetup installs each network component detected in the system, using the default parameter values specified for the component in the component's Windows 2000 or later INF file. NetSetup then installs network components listed in the AnswerFile.

If a network component's *OEM section* in the AnswerFile contains an [OemDllToLoad](examining-the-answerfile.md) key, NetSetup loads the network migration DLL if the DLL is not already loaded and then calls the DLL's [**PostUpgradeInitialize**](https://msdn.microsoft.com/library/windows/hardware/ff562410) function. The **PostUpgradeInitialize** function supplies the DLL with information that the DLL uses to initialize itself. NetSetup then calls the DLL's [**DoPostUpgradeProcessing**](https://msdn.microsoft.com/library/windows/hardware/ff545629) function once for each network component to be upgraded by the DLL. **DoPostUpgradeProcessing** can display a user interface that allows a user to specify parameter values for a component. **DoPostUpgradeProcessing** writes any user-specified parameter values to the registry.

If the miniport driver for a network adapter required the adapter's instance ID before the upgrade, it will probably require the adapter's instance ID after the upgrade. A network migration DLL can call [**HrGetInstanceGuidOfPreNT5NetCardInstance**](https://msdn.microsoft.com/library/windows/hardware/ff546613) from its **DoPostUpgradeProcessing** function to obtain the Windows 2000 or later instance GUID for a network adapter.

NetSetup starts the installed network protocols, clients, and services.

NetSetup processes the entries in the **Identification** section of the AnswerFile and tries to connect the system to the workgroup or domain specified in that section.

If the system being upgraded contains any Async adapters, Setup calls the Async class installer, which upgrades each Async adapter as follows:

-   The Async class installer locates the OEM section for the Async adapter in the AnswerFile.

-   From the Async adapter's OEM section, the Async class installer reads the preupgrade parameter values for the adapter. These parameter values were written by the network migration DLL for the adapter during the Winnt32 phase of the upgrade.

-   The Async class installer writes the adapter's preupgrade parameter values to the Windows 2000 or later registry.

 

 





