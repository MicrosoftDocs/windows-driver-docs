---
title: HKLM\SYSTEM\CurrentControlSet\Enum Registry Tree
description: The HKLM\SYSTEM\CurrentControlSet\Enum registry tree contains information about the devices on the system.
ms.date: 05/20/2022
---

# HKLM\\SYSTEM\\CurrentControlSet\\Enum Registry Tree

The **Enum** tree is reserved for use by operating system components, and its layout is subject to change. Drivers and user-mode device installation components must use system-supplied functions, such as [**IoGetDeviceProperty**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iogetdeviceproperty), [**CM_Get_DevNode_Registry_Property**](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_get_devnode_registry_propertyw), and [**SetupDiGetDeviceRegistryProperty**](/windows/win32/api/setupapi/nf-setupapi-setupdigetdeviceregistrypropertya) to extract information from this tree. 

> [!NOTE]
> Drivers and Windows applications must not access the ***Enum*** tree directly.

 

