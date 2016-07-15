---
Description: Avoiding Data Copying
MS-HAID: 'audio.avoiding\_data\_copying'
MSHAttr: 'PreferredLib:/library/windows/hardware'
title: Avoiding Data Copying
---

# Avoiding Data Copying


## <span id="avoiding_data_copying"></span><span id="AVOIDING_DATA_COPYING"></span>


You can improve driver performance by designing your audio hardware to avoid unnecessary data copying.

You can achieve the best results by implementing your hardware to perform true scatter/gather DMA and by writing a WavePci miniport driver to manage the hardware. Your device can then directly access playback data buffers or empty record buffers wherever they are located in system memory. This eliminates a lot of unnecessary software intervention and time-consuming data copying.

If you are designing a WaveCyclic device, however, you can improve its performance by making its hardware buffer directly accessible as system memory. This eliminates the overhead of copying data from an intermediate buffer in system memory.

Also, if your device requires an audio format with a channel ordering that is incompatible with the standard WDM audio formats, the driver might have to perform in-place conversion of each audio frame in an intermediate buffer before the hardware can process it. This can degrade performance. For additional information, see the white paper titled Multiple Channel Audio Data and WAVE Files at the [audio technology](http://go.microsoft.com/fwlink/p/?linkid=8751) website.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20Avoiding%20Data%20Copying%20%20RELEASE:%20%287/14/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")


