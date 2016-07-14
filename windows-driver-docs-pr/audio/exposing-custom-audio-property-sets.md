---
Description: Exposing Custom Audio Property Sets
MS-HAID: 'audio.exposing\_custom\_audio\_property\_sets'
MSHAttr: 'PreferredLib:/library/windows/hardware'
title: Exposing Custom Audio Property Sets
---

# Exposing Custom Audio Property Sets


## <span id="exposing_custom_audio_property_sets"></span><span id="EXPOSING_CUSTOM_AUDIO_PROPERTY_SETS"></span>


DirectSound supports the use of custom properties on sound cards and provides an **IKsPropertySet** interface for this purpose.

**Note**   Header files Dsound.h and Ksproxy.h define similar but incompatible versions of the **IKsPropertySet** interface. DirectSound applications should use the version defined in Dsound.h. The DirectSound version of **IKsPropertySet** is defined in the DirectSound reference pages in the Microsoft Windows SDK documentation. For the KSProxy version, see [IKsPropertySet](stream.ikspropertyset).

 

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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20Exposing%20Custom%20Audio%20Property%20Sets%20%20RELEASE:%20%287/14/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")



