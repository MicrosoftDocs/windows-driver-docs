---
title: INF GeneralConfigData Section
description: INF GeneralConfigData Section
ms.assetid: 49b00396-479f-471a-8c79-bb8ef33ebcaa
keywords:
- GeneralConfigData section
- INF files WDK Windows 2000 display
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# INF GeneralConfigData Section


## <span id="ddk_inf_generalconfigdata_section_gg"></span><span id="DDK_INF_GENERALCONFIGDATA_SECTION_GG"></span>


If your miniport driver maps more than 8 MB of device memory, include a **GeneralConfigData** section in your INF file.

```
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20INF%20GeneralConfigData%20Section%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




