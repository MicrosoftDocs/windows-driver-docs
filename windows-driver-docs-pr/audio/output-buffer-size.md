---
title: Output Buffer Size
description: Output Buffer Size
ms.assetid: 386cc6f7-2fab-474a-b997-9ba2457ada0c
keywords: ["data-intersection handlers WDK audio , output buffer size", "output buffers WDK audio", "buffer size WDK audio"]
---

# Output Buffer Size


## <span id="output_buffer_size"></span><span id="OUTPUT_BUFFER_SIZE"></span>


The miniport driver's [**IMiniport::DataRangeIntersection**](https://msdn.microsoft.com/library/windows/hardware/ff536764) method copies the structure that specifies the negotiated data format into a buffer that is allocated by the caller. The method's *OutputBufferLength* parameter specifies the buffer's size in bytes. Note that the size of the format structure varies with the selected format. In order to avoid writing past the end of the buffer, the **DataRangeIntersection** method should first verify that the allocated buffer is big enough to contain the format.

For a mono or stereo format, the minimum size for the output buffer is either **sizeof**([**KSDATAFORMAT\_WAVEFORMATEX**](https://msdn.microsoft.com/library/windows/hardware/ff537095)) or **sizeof**([**KSDATAFORMAT\_DSOUND**](https://msdn.microsoft.com/library/windows/hardware/ff537094)), depending on whether a WAVEFORMATEX or DirectSound format has been selected.

If the wave format supports more than two channels, the [**WAVEFORMATEX**](https://msdn.microsoft.com/library/windows/hardware/ff538799) structure that is embedded at the end of the[**KSDATAFORMAT\_WAVEFORMATEX**](https://msdn.microsoft.com/library/windows/hardware/ff537095) structure expands to occupy an additional number of bytes that is equal to the difference

**sizeof**([**WAVEFORMATEXTENSIBLE**](https://msdn.microsoft.com/library/windows/hardware/ff538802)) - **sizeof**([**WAVEFORMATEX**](https://msdn.microsoft.com/library/windows/hardware/ff538799))

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20Output%20Buffer%20Size%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




