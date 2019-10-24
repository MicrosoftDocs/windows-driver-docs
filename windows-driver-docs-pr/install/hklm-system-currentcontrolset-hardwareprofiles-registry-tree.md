---
title: HKLM\SYSTEM\CurrentControlSet\HardwareProfiles Registry Tree
description: HKLM\SYSTEM\CurrentControlSet\HardwareProfiles registry tree contains information about the hardware profiles on the system.
ms.assetid: 548d7a50-b3b1-4413-8898-9ed13bcbdcfc
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# HKLM\\SYSTEM\\CurrentControlSet\\HardwareProfiles Registry Tree





The **HKLM\\SYSTEM\\CurrentControlSet\\HardwareProfiles** registry tree contains information about the hardware profiles on the system. Hardware profiles are deprecated and state should not be stored relative to a hardware profile.

Instead, store information globally using **PLUGPLAY_REGKEY_DEVICE** and **PLUGPLAY_REGKEY_DRIVER** without also using **PLUGPLAY_REGKEY_CURRENT_HWPROFILE**. For more info, see [**IoOpenDeviceRegistryKey**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdm/nf-wdm-ioopendeviceregistrykey).




