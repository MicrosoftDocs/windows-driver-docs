---
title: Output Buffer Size
description: Output Buffer Size
ms.assetid: 386cc6f7-2fab-474a-b997-9ba2457ada0c
keywords:
- data-intersection handlers WDK audio , output buffer size
- output buffers WDK audio
- buffer size WDK audio
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Output Buffer Size


## <span id="output_buffer_size"></span><span id="OUTPUT_BUFFER_SIZE"></span>


The miniport driver's [**IMiniport::DataRangeIntersection**](https://msdn.microsoft.com/library/windows/hardware/ff536764) method copies the structure that specifies the negotiated data format into a buffer that is allocated by the caller. The method's *OutputBufferLength* parameter specifies the buffer's size in bytes. Note that the size of the format structure varies with the selected format. In order to avoid writing past the end of the buffer, the **DataRangeIntersection** method should first verify that the allocated buffer is big enough to contain the format.

For a mono or stereo format, the minimum size for the output buffer is either **sizeof**([**KSDATAFORMAT\_WAVEFORMATEX**](https://msdn.microsoft.com/library/windows/hardware/ff537095)) or **sizeof**([**KSDATAFORMAT\_DSOUND**](https://msdn.microsoft.com/library/windows/hardware/ff537094)), depending on whether a WAVEFORMATEX or DirectSound format has been selected.

If the wave format supports more than two channels, the [**WAVEFORMATEX**](https://msdn.microsoft.com/library/windows/hardware/ff538799) structure that is embedded at the end of the[**KSDATAFORMAT\_WAVEFORMATEX**](https://msdn.microsoft.com/library/windows/hardware/ff537095) structure expands to occupy an additional number of bytes that is equal to the difference

**sizeof**([**WAVEFORMATEXTENSIBLE**](https://msdn.microsoft.com/library/windows/hardware/ff538802)) - **sizeof**([**WAVEFORMATEX**](https://msdn.microsoft.com/library/windows/hardware/ff538799))

 

 




