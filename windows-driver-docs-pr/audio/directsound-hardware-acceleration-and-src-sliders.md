---
title: DirectSound Hardware-Acceleration and SRC Sliders
description: DirectSound Hardware-Acceleration and SRC Sliders
ms.assetid: 40329177-b8d5-49a2-a1d3-6730a26b6e78
keywords: ["hardware acceleration WDK DirectSound , SRC sliders", "sliders WDK audio"]
---

# DirectSound Hardware-Acceleration and SRC Sliders


## <span id="directsound_hardware_acceleration_and_src_sliders"></span><span id="DIRECTSOUND_HARDWARE_ACCELERATION_AND_SRC_SLIDERS"></span>


Windows Me/98, and Windows 2000 and later, provide global slider controls for altering DirectSound performance on a system-wide basis. The sliders control the level of hardware acceleration and quality of sample-rate conversion (SRC) that are made available to DirectSound applications. Changes made to the hardware-acceleration and SRC sliders are persistent across boot-ups.

The hardware-acceleration and SRC settings can be changed only by direct end-user action. No API is available for changing the hardware-acceleration or SRC setting from an application program. This behavior improves stability and prevents software from placing the audio system in a state from which it cannot be removed without rebooting.

These settings affect only DirectSound applications. Note that the waveOut API always uses the best SRC quality regardless of the setting of the DirectSound SRC slider. Also, in all current versions of Windows, waveOut applications are unable to use hardware-accelerated pins on audio devices and are unaffected by the setting of the DirectSound hardware-acceleration slider. For more information about the Windows multimedia waveOut API, see the Microsoft Windows SDK documentation.

To locate the DirectSound hardware-acceleration and SRC sliders in Windows XP, for example, follow these steps:

1.  In Control Panel, double-click the **Sounds and Audio Devices** icon (or just run mmsys.cpl).

2.  On the **Audio** tab, select a device from the **Sound Playback** list.

3.  Click the **Advanced** button.

4.  Click the **Performance** tab.

At this point, you should see two sliders that are labeled **Hardware acceleration** and **Sample rate conversion quality**.

The hardware-acceleration slider has four settings that range from **None** (level 0) on the left to **Full** (level three) on the right. The following table shows the meaning of these settings.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Acceleration Level</th>
<th align="left">Setting Name</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>0</p></td>
<td align="left"><p>Emulation</p></td>
<td align="left"><p>Forces emulation.</p></td>
</tr>
<tr class="even">
<td align="left"><p>1</p></td>
<td align="left"><p>Basic</p></td>
<td align="left"><p>Disables hardware acceleration of DirectSound secondary buffers.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>2</p></td>
<td align="left"><p>Standard</p></td>
<td align="left"><p>Enables hardware acceleration of DirectSound secondary buffers but disables vendor-specific property-set extensions.</p></td>
</tr>
<tr class="even">
<td align="left"><p>3</p></td>
<td align="left"><p>Full</p></td>
<td align="left"><p>Enables hardware acceleration of DirectSound secondary buffers and enables vendor-specific property-set extensions.</p></td>
</tr>
</tbody>
</table>

 

<span id="Emulation_Setting"></span><span id="emulation_setting"></span><span id="EMULATION_SETTING"></span>**Emulation Setting**  
The **Emulation** setting above forces DirectSound into emulation mode. In this mode, DirectSound applications run as though no DirectSound driver is present. All mixing is done by DirectSound in user mode, and the resulting audio data is played back through the waveOut API. The result is typically a large increase in latency. Note that after you select this setting, you might need to reboot if you are running a Windows version that is earlier than Windows XP and you want to change to one of the other three settings: **Basic**, **Standard**, or **Full**. This problem has been fixed in the version of DirectSound that ships with Windows XP and later.

<span id="Basic_Setting"></span><span id="basic_setting"></span><span id="BASIC_SETTING"></span>**Basic Setting**  
The **Basic** setting disables hardware acceleration of DirectSound secondary buffers. Under this setting, all DirectSound applications run as though no hardware acceleration is available, regardless of the capabilities of the sound card that is being used. You can use this setting during testing to emulate a sound card that has no DirectSound acceleration. With an adapter such as the OPL, which has no acceleration of DirectSound secondary buffers, this setting has the same effect as the **Standard** setting. In Windows Server 2003, **Basic** is the default setting.

<span id="Standard_Setting"></span><span id="standard_setting"></span><span id="STANDARD_SETTING"></span>**Standard Setting**  
The **Standard** setting enables hardware acceleration of DirectSound secondary buffers but disables vendor-specific extensions such as EAX (Creative Technologies' environmental audio extensions) that are exposed as property sets through the **IKsPropertySet** interface (see [Exposing Custom Audio Property Sets](exposing-custom-audio-property-sets.md)). In Windows 2000, the **Standard** setting is selected by default.

<span id="Full_Setting"></span><span id="full_setting"></span><span id="FULL_SETTING"></span>**Full Setting**  
The **Full** setting enables full acceleration of DirectSound secondary buffers. This setting also enables property sets for vendor-specific extensions that are exposed through the **IKsPropertySet** interface (see [Exposing Custom Audio Property Sets](exposing-custom-audio-property-sets.md)). **IKsPropertySet** extensions include vendor-specific hardware enhancements such as EAX. This is the default setting in Windows Me/98 and Windows XP.

The following table summarizes the default settings for the hardware-acceleration and SRC sliders for the various Windows releases.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Windows Release</th>
<th align="left">Default Hardware-Acceleration Setting</th>
<th align="left">Default SRC Setting</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Windows 98</p></td>
<td align="left"><p><strong>Full</strong></p></td>
<td align="left"><p><strong>Good</strong></p></td>
</tr>
<tr class="even">
<td align="left"><p>Windows 2000</p></td>
<td align="left"><p><strong>Standard</strong></p></td>
<td align="left"><p><strong>Good</strong></p></td>
</tr>
<tr class="odd">
<td align="left"><p>Windows Me</p></td>
<td align="left"><p><strong>Full</strong></p></td>
<td align="left"><p><strong>Good</strong></p></td>
</tr>
<tr class="even">
<td align="left"><p>Windows XP</p></td>
<td align="left"><p><strong>Full</strong></p></td>
<td align="left"><p><strong>Best</strong></p></td>
</tr>
<tr class="odd">
<td align="left"><p>Windows Server 2003</p></td>
<td align="left"><p><strong>Basic</strong></p></td>
<td align="left"><p><strong>Best</strong></p></td>
</tr>
</tbody>
</table>

 

If the user adjusts either the hardware-acceleration or SRC setting to a value other than the default, DirectSound uses the new setting instead of the default.

In Windows XP, the [KMixer system driver](kernel-mode-wdm-audio-components.md#kmixer_system_driver) uses an SRC algorithm that provides a signal-to-noise ratio of up to 85 decibels when the SRC slider is set to **Best**. For more information about KMixer's SRC algorithms, see [KMixer Driver Sample Rate Conversion and Mixing Policy](kmixer-driver-sample-rate-conversion-and-mixing-policy.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20DirectSound%20Hardware-Acceleration%20and%20SRC%20Sliders%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


