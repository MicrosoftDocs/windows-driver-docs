---
title: INF GeneralConfigData Section
description: INF GeneralConfigData Section
ms.assetid: 49b00396-479f-471a-8c79-bb8ef33ebcaa
keywords:
- GeneralConfigData section
- INF files WDK Windows 2000 display
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# INF GeneralConfigData Section


## <span id="ddk_inf_generalconfigdata_section_gg"></span><span id="DDK_INF_GENERALCONFIGDATA_SECTION_GG"></span>


If your miniport driver maps more than 8 MB of device memory, include a **GeneralConfigData** section in your INF file.

```inf
[GeneralConfigData]

[MaximumDeviceMemoryConfiguration = n]
[MaximumNumberOfDevices = n]
```

The following are **GeneralConfigData** entries and values:

<span id="MaximumDeviceMemoryConfiguration_n"></span><span id="maximumdevicememoryconfiguration_n"></span><span id="MAXIMUMDEVICEMEMORYCONFIGURATION_N"></span>**MaximumDeviceMemoryConfiguration**=*n*  
Specifies the maximum number of megabytes of device memory that the miniport driver will attempt to map into the system address space for one video device enumerated by PCI. Windows uses this value as a hint to determine how many system page table entries (PTEs) it should allocate for the mapping. For this entry to take effect, a reboot may be needed. You can determine whether a reboot is necessary by checking the status of your device in the Device Manager.

<span id="MaximumNumberOfDevices_n"></span><span id="maximumnumberofdevices_n"></span><span id="MAXIMUMNUMBEROFDEVICES_N"></span>**MaximumNumberOfDevices**=*n*  
Specifies how many video devices (as enumerated by PCI and driven by your miniport driver) are expected to be present in the system. If you specify this entry, you must also specify the **MaximumDeviceMemoryConfiguration** entry. For this entry to take effect, a reboot may be needed. You can determine whether a reboot is necessary by checking the status of your device in the Device Manager.

For information about supporting more than one monitor, see [Supporting DualView (Windows 2000 Model)](supporting-dualview--windows-2000-model-.md) and [Multiple-Monitor Support in the Display Driver](multiple-monitor-support-in-the-display-driver.md).









