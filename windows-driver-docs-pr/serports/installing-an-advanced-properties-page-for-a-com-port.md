---
title: Installing an Advanced Properties Page for a COM Port
description: Installing an Advanced Properties Page for a COM Port
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

1. Implement a Microsoft Win32 property page provider. For general information about installing property sheet dialogs, see [Providing Device Property Pages](../install/overview-of-device-property-pages.md).

    In the property page provider, call the system-supplied [**SerialDisplayAdvancedSettings**](/windows/win32/api/msports/nf-msports-serialdisplayadvancedsettings) routine, which displays the system-supplied default dialog box.

2. Install the property page provider by setting an **EnumPropPages32** value entry in an *add-registry-section* that is referenced by a device's [**DDInstall section**](../install/inf-ddinstall-section.md). See the description of the **EnumPropPages32** value entry in [**INF AddReg Directive**](../install/inf-addreg-directive.md).

To override the default dialog box displayed by **SerialDisplayAdvancedSettings**, do the following:

1. Implement a custom dialog *DLL*. The entry point for the dialog is a [**PPORT\_ADVANCED\_DIALOG**](/previous-versions/windows/hardware/drivers/ff546956(v=vs.85))-typed routine.

2. Install the custom dialog DLL by setting an **EnumAdvancedDialog** entry value in an *add-registry-section* that is referenced by a device's [**DDInstall section**](../install/inf-ddinstall-section.md). The type and format of the value entry is the same as that used for a **EnumPropPages32** value entry.
