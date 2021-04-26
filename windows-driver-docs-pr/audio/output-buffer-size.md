---
title: Output Buffer Size
description: Output Buffer Size
keywords:
- data-intersection handlers WDK audio , output buffer size
- output buffers WDK audio
- buffer size WDK audio
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Output Buffer Size


## <span id="output_buffer_size"></span><span id="OUTPUT_BUFFER_SIZE"></span>


The miniport driver's [**IMiniport::DataRangeIntersection**](/windows-hardware/drivers/ddi/portcls/nf-portcls-iminiport-datarangeintersection) method copies the structure that specifies the negotiated data format into a buffer that is allocated by the caller. The method's *OutputBufferLength* parameter specifies the buffer's size in bytes. Note that the size of the format structure varies with the selected format. In order to avoid writing past the end of the buffer, the **DataRangeIntersection** method should first verify that the allocated buffer is big enough to contain the format.

For a mono or stereo format, the minimum size for the output buffer is either **sizeof**([**KSDATAFORMAT\_WAVEFORMATEX**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksdataformat_waveformatex)) or **sizeof**([**KSDATAFORMAT\_DSOUND**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksdataformat_dsound)), depending on whether a WAVEFORMATEX or DirectSound format has been selected.

If the wave format supports more than two channels, the [**WAVEFORMATEX**](/windows/win32/api/mmreg/ns-mmreg-waveformatex) structure that is embedded at the end of the[**KSDATAFORMAT\_WAVEFORMATEX**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksdataformat_waveformatex) structure expands to occupy an additional number of bytes that is equal to the difference

**sizeof**([**WAVEFORMATEXTENSIBLE**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-waveformatextensible)) - **sizeof**([**WAVEFORMATEX**](/windows/win32/api/mmreg/ns-mmreg-waveformatex))

 

