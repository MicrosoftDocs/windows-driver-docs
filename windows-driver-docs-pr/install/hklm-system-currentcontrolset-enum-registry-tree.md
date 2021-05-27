---
title: HKLM\SYSTEM\CurrentControlSet\Enum Registry Tree
description: The HKLM\SYSTEM\CurrentControlSet\Enum registry tree contains information about the devices on the system.
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# HKLM\\SYSTEM\\CurrentControlSet\\Enum Registry Tree





The **Enum** tree is reserved for use by operating system components, and its layout is subject to change. Drivers and user-mode [Device Installation Components](/previous-versions/ff541277(v=vs.85)) must use system-supplied functions, such as [**IoGetDeviceProperty**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iogetdeviceproperty) and [**SetupDiGetDeviceRegistryProperty**](/windows/win32/api/setupapi/nf-setupapi-setupdigetdeviceregistrypropertya), to extract information from this tree. *Drivers and Windows applications must not access the* ***Enum*** *tree directly.*

 

