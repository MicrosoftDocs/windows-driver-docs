---
title: HKLM\SYSTEM\CurrentControlSet\Enum Registry Tree
description: The HKLM\SYSTEM\CurrentControlSet\Enum registry tree contains information about the devices on the system.
ms.assetid: 9de3ca54-d23f-4ee6-a638-27e52a60dfdd
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# HKLM\\SYSTEM\\CurrentControlSet\\Enum Registry Tree





The **HKLM\\SYSTEM\\CurrentControlSet\\Enum** registry tree contains information about the devices on the system. The PnP manager creates a subkey for each device, with a name in the form of **HKLM\\SYSTEM\\CurrentControlSet\\Enum\\**<em>Enumerator</em>**\\**<em>deviceID</em>. Under each of these keys is a subkey for each device instance present on the system. This subkey has information such as the device description, hardware IDs, compatible IDs, and resource requirements.

The **Enum** tree is reserved for use by operating system components, and its layout is subject to change. Drivers and user-mode [Device Installation Components](https://msdn.microsoft.com/library/windows/hardware/ff541277) must use system-supplied functions, such as [**IoGetDeviceProperty**](https://msdn.microsoft.com/library/windows/hardware/ff549203) and [**SetupDiGetDeviceRegistryProperty**](https://msdn.microsoft.com/library/windows/hardware/ff551967), to extract information from this tree. *Drivers and Windows applications must not access the* ***Enum*** *tree directly.* You can view the **Enum** tree directly by using Registry Editor when you debug drivers.

 

 





