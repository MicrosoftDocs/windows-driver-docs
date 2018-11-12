---
title: Examining the AnswerFile
description: Examining the AnswerFile
ms.assetid: 42d58786-e50c-43c2-b673-5f23c9930ee7
keywords:
- testing network component upgrades WDK
- AnswerFile WDK networking
- upgrade tests WDK networking
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Examining the AnswerFile





**Note**  Vendor-supplied network upgrades are not supported in Microsoft Windows XP (SP1 and later), Microsoft Windows Server 2003, and later operating systems.

 

Immediately before the "Setup is Copying Files" progress bar is displayed on a system being upgraded, the AnswerFile is created. NetSetup and vendor-supplied network migration DLLs create sections in the AnswerFile and then write entries to these sections during the Winnt32 upgrade phase.

You can examine the AnswerFile by copying c:\\$win\_nt$.~bt\\winnt.sif to %TEMP%. After the AnswerFile has been copied, you can click **Cancel** to cancel file copying. You do not have to wait until file copying is finished.

The following table lists the top-level sections in the AnswerFile and the corresponding entries that each section contains that pertain to network components:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Section</th>
<th align="left">Entries Contained</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><strong>NetAdapters</strong></p></td>
<td align="left"><p>Network adapters, including ISDN adapters</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>AsyncAdapters</strong></p></td>
<td align="left"><p>Async adapters</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>NetProtocols</strong></p></td>
<td align="left"><p>Network protocols</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>NetServices</strong></p></td>
<td align="left"><p>Network services</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>NetClients</strong></p></td>
<td align="left"><p>Network clients</p></td>
</tr>
</tbody>
</table>

 

**Note**  **NetClient** components are deprecated in Windows 8.1, Windows Server 2012 R2, and later.

 

For each network component that it finds during the Winnt32 phase, NetSetup writes an entry to the appropriate top-level section of the AnswerFile. Each entry has the following format:

params.*postupgrade-ID*

The *postupgrade-ID* entry is the Windows 2000 or later device ID that NetSetup obtained from the netmap.inf file for the component.

Each entry specifies the name of the parameters section for that component in the AnswerFile. For example, if a component's Windows 2000 or later device ID is netadapter2, its entry in the **NetAdapters** section is **params.netadapter2**. The top-level sections and the parameter sections in an AnswerFile are not visible to a network migration DLL.

To the parameters section name for a component, NetSetup adds the extension **OemSection** to create the *OEM-section* name for the component. For example, if the parameters section for a component is params.netadapter2, the *OEM-section* name for the component is params.netadapter2.OemSection. NetSetup passes the *OEM-section* name as the *szSectionName* parameter to the [**DoPreUpgradeProcessing**](https://msdn.microsoft.com/library/windows/hardware/ff545634) function supplied by the network migration DLL for the component. The **DoPreUpgradeProcessing** function calls the [**NetUpgradeAddSection**](https://msdn.microsoft.com/library/windows/hardware/ff559063) function to create the *OEM-section* for a component in the AnswerFile. The **DoPreUpgradeProcessing** function then calls the [**NetUpgradeAddLineToSection**](https://msdn.microsoft.com/library/windows/hardware/ff559059) to add component-specific information to the *OEM-section*.

The following portion of an AnswerFile shows the sections and entries for a network adapter whose Windows 2000 or later device ID is **adapter2**:

```INF
[NetAdapter]              ;top-level adapters section
adapter2=params.adapter2      ;entry for adapter2
[params.adapter2]          ;parameters section for adapter2
InfID=adapter2            ;Windows 2000 or later device ID
OemSection=params.adapter2.OemSection  ;Identifies the OemSection

[params.adapter2.OemSection]  ;OemSection created by migration DLL
InfToRunAfterInstall="", adapter2.SectionToRun ;Written by DLL

[adapter2.SectionToRun]      ;Section created by migration DLL
AddReg=adapter2.SectionToRun.AddReg ;AddReg directive

[adapter2.SectionToRun.AddReg] ;AddReg section created by DLL
HKR,0\0,IsdnPhoneNumber,0,"111-1111" ;AddReg entries written by DLL
HKR,0\1,IsdnPhoneNumber,0,"222-2222"
HKR,0\0,IsdnSpid,0,"111"
HKR,0\1,IsdnSpid,0,"222"
HKR,0,IsdnSwitchType,0x00010001,1
```

During the GUI mode phase, NetSetup detects the [**InfToRunAfterInstall**](https://msdn.microsoft.com/library/windows/hardware/ff559059) key written by the migration DLL to the **params.adapter2.OemSection** of the example AnswerFile. As directed by this key, NetSetup processes the **adapter2.SectionToRun.AddReg** section. The **adapter2.SectionToRun.AddReg** section directs NetSetup to add parameter values to adapater2's instance key in the Windows 2000 or later registry. These parameter values should match the preupgrade parameter values that the migration DLL read from adapter2's the registry during the Winnt32 phase of the upgrade.

If a network migration DLL is to be loaded during the GUI mode phase, its [**DoPreUpgradeProcessing**](https://msdn.microsoft.com/library/windows/hardware/ff545634) function sets the NUA\_LOAD\_POST\_UPGRADE flag. This flag causes NetSetup to write the **OemDllToLoad** entry to the component's parameters section in the AnswerFile. The **OemDllToLoad** entry causes NetSetup to load the migration DLL for the component during the GUI mode phase.

The following example shows the AnswerFile sections and entries for a component whose network migration DLL is loaded during the GUI mode phase:

```INF
[NetAdapter]              ;top-level adapters section
adapter2=params.adapter2      ;entry for adapter2
[params.adapter2]          ;parameters section for adapter2
InfID=adapter2            ;postupgrade device ID
OemSection=params.adapter2.OemSection;Identifies the OemSection
OemDllToLoad=c:\temp\oem0001\migration.dll
```

Note the **OemDllToLoad** entry in the **params.adapter2** section. Also note that the migration DLL did not create a **params.adapter2.OemSection**. When the migration DLL is to be loaded during the GUI mode phase, it typically does not write an **InfToRunAfterInstall** key to the AnswerFile. The DLL performs the postinstallation upgrade; therefore, it does not need to create an *Oem-Section* name that contains directives for NetSetup to perform during the GUI mode phase.

 

 





