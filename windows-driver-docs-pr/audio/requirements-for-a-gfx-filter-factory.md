---
Description: Requirements for a GFX Filter Factory
MS-HAID: 'audio.requirements\_for\_a\_gfx\_filter\_factory'
MSHAttr: 'PreferredLib:/library/windows/hardware'
title: Requirements for a GFX Filter Factory
---

# Requirements for a GFX Filter Factory


## <span id="requirements_for_a_gfx_filter_factory"></span><span id="REQUIREMENTS_FOR_A_GFX_FILTER_FACTORY"></span>


For the operating system to treat an [AVStream](stream.avstream_overview) filter factory as a factory for GFX filters, the [filter factories](filter-factories.md) should do the following:

-   Register its device interface in both the KSCATEGORY\_AUDIO and KSCATEGORY\_DATATRANSFORM device classes.

-   Have only one input pin and one output pin.

-   Add a **Gfx** subkey to the filter's KSCATEGORY\_AUDIO device interface registry key. The device setup information file for the filter factory typically uses an [**INF AddReg directive**](devinst.inf_addreg_directive) to add the **Gfx** subkey to the registry path during driver installation.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20Requirements%20for%20a%20GFX%20Filter%20Factory%20%20RELEASE:%20%287/14/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")


