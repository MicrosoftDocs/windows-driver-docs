---
title: Exposing Custom Audio Property Sets
description: Exposing Custom Audio Property Sets
ms.assetid: dc45f0fb-f462-4d20-967a-0665e18019e4
keywords:
- hardware acceleration WDK DirectSound , custom audio property sets
- custom audio property sets WDK
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Exposing Custom Audio Property Sets


## <span id="exposing_custom_audio_property_sets"></span><span id="EXPOSING_CUSTOM_AUDIO_PROPERTY_SETS"></span>


DirectSound supports the use of custom properties on sound cards and provides an **IKsPropertySet** interface for this purpose.

**Note**   Header files Dsound.h and Ksproxy.h define similar but incompatible versions of the **IKsPropertySet** interface. DirectSound applications should use the version defined in Dsound.h. The DirectSound version of **IKsPropertySet** is defined in the DirectSound reference pages in the Microsoft Windows SDK documentation. For the KSProxy version, see [IKsPropertySet](https://msdn.microsoft.com/library/windows/hardware/ff560718).

 

Custom audio property sets are enabled by default in Windows 98 Second Edition and Windows Me, and in Windows XP and later. By default, DirectSound ignores custom property sets in Windows 2000, and in Windows Server 2003 and later server versions of Windows. For DirectSound to recognize a custom property set in one of these operating systems, users must first enable custom property sets on their systems.

For example, to enable custom audio property sets in Windows 2000:

1.  In Control Panel, double-click the **Sounds and Multimedia** icon (or just run mmsys.cpl).

2.  On the **Audio** tab, select the appropriate preferred device in the **Sound Playback** list.

3.  Click the **Advanced** button.

4.  On the **Performance** tab, slide the **Hardware Acceleration** slider to **Full**.

5.  Click **Apply**.

DirectSound is now enabled to pass custom property sets to the driver.

Four settings are available on the **Hardware Acceleration** slider:

-   **None**

-   **Basic**

-   **Standard**

-   **Full**

Custom property sets are enabled only when the slider is set to **Full**. For more information, see [DirectSound Hardware-Acceleration and SRC Sliders](directsound-hardware-acceleration-and-src-sliders.md).

 

 




