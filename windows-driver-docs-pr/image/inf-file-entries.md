---
title: INF File Entries
description: INF File Entries
ms.assetid: 8af2cbe7-f249-4e2f-940f-b50bc451cabe
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# INF File Entries





Using a microdriver for your device requires additional entries in the setup information (INF) file. First, there must be an entry called "MicroDriver" in the **DeviceData** section of the INF file. (See [INF Files for WIA Devices](inf-files-for-wia-devices.md) for more information.) This entry should be set to the name of the DLL that implements the microdriver.

### Windows Me INF File Entries

The following applies to Microsoft Windows Millennium Edition (Me), Windows XP, and later operating systems.

In the space in the [**INF AddReg Directive**](https://msdn.microsoft.com/library/windows/hardware/ff546320) where your WIA minidriver normally would be referenced, the INF should list *wiafbdrv.dll* as the driver. This is the component that implements the WIA flatbed driver.

Be sure that the [**INF CopyFiles Directive**](https://msdn.microsoft.com/library/windows/hardware/ff546346) includes both your microdriver and *wiafbdrv.dll*, which is copied from the Windows CAB files. The rest of the INF file is the same as for other WIA devices.

### Windows XP INF File Entries

The following information applies to Windows XP and later. Windows Me INF files do not use **Include** and **Needs** directives, and so cannot use this style of INF.

The [**INF DDInstall Section**](https://msdn.microsoft.com/library/windows/hardware/ff547344) should contain the directive **Include**=sti.inf. Additionally, the **Needs** directive should reference **STI.MICRODRIVERSection**, as well as the appropriate device type section. This will supply the necessary USDClass and CLSID **AddReg** directives, so these do not need to be explicitly included in the INF.

**Note**  It is not necessary to include *wiafbdrv.dll* in your **CopyFiles** directive.

 

The INF included with the WIA microdriver on the Windows Driver Kit (WDK) CD uses this new method to reference the microdriver.

 

 




