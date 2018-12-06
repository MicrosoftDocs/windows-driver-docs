---
title: Installing an Advanced Properties Page for a COM Port
description: Installing an Advanced Properties Page for a COM Port
ms.assetid: 056fd245-a9d2-4a10-9e92-fe75e51f6770
keywords:
- advanced COM port properties page WDK serial devices
- COM ports WDK serial devices
- default user dialog box for COM port
- overriding default dialog box WDK serial devices
- port numbers WDK serial devices
- FIFO control parameters WDK serial devices
- COM port numbers WDK serial devices
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Installing an Advanced Properties Page for a COM Port





The advanced property page displays a default user dialog box for setting FIFO control parameters and selecting a COM port number. However, you can override the default dialog box by supplying a custom dialog box.

To install the system-supplied property page and default dialog box for a COM port, do the following:

1.  Implement a Microsoft Win32 property page provider. For general information about installing property sheet dialogs, see [Providing Device Property Pages](https://msdn.microsoft.com/library/windows/hardware/ff549784).

    In the property page provider, call the system-supplied [**SerialDisplayAdvancedSettings**](https://msdn.microsoft.com/library/windows/hardware/ff547447) routine, which displays the system-supplied default dialog box.

2.  Install the property page provider by setting an **EnumPropPages32** value entry in an *add-registry-section* that is referenced by a device's [**DDInstall section**](https://msdn.microsoft.com/library/windows/hardware/ff547344). See the description of the **EnumPropPages32** value entry in [**INF AddReg Directive**](https://msdn.microsoft.com/library/windows/hardware/ff546320).

To override the default dialog box displayed by **SerialDisplayAdvancedSettings**, do the following:

1.  Implement a custom dialog [*DLL*](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-dll). The entry point for the dialog is a [**PPORT\_ADVANCED\_DIALOG**](https://msdn.microsoft.com/library/windows/hardware/ff546956)-typed routine.

2.  Install the custom dialog DLL by setting an **EnumAdvancedDialog** entry value in an *add-registry-section* that is referenced by a device's [**DDInstall section**](https://msdn.microsoft.com/library/windows/hardware/ff547344). The type and format of the value entry is the same as that used for a **EnumPropPages32** value entry.

 

 




