---
Description: Windows Vista Support for WDM Audio
MS-HAID: 'audio.windows\_vista\_support\_for\_wdm\_audio'
MSHAttr: 'PreferredLib:/library/windows/hardware'
title: Windows Vista Support for WDM Audio
---

# Windows Vista Support for WDM Audio


## <span id="windows_xp_support_for_wdm_audio"></span><span id="WINDOWS_XP_SUPPORT_FOR_WDM_AUDIO"></span>


Windows Vista supports the following WDM audio capabilities:

-   WDM version 1.40

-   All the features that Windows XP supports, with the following exceptions.
    -   Hardware peak meters are supported, except when the Windows Vista mixer API runs in per-application mode.
    -   Wave and MIDI NT4 drivers function normally, but they are not supported by the new audio user interface.
    -   AUX devices are not supported, and the [**auxGetNumDevs**](multimedia.auxgetnumdevs) function in Mmsystem.h will always return a count of zero.
    -   Windows NT4-style mixer drivers (DRIVERS32) are not supported.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20Windows%20Vista%20Support%20for%20WDM%20Audio%20%20RELEASE:%20%287/14/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")


