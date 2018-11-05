---
title: Specifying WMA Pro Data Ranges
description: Specifying WMA Pro Data Ranges
ms.assetid: c7e9bc68-cec2-4a34-9ef0-ce3c9a4cc987
keywords:
- S/PDIF pass-through WDK audio
- WMA Pro-over-S/PDIF format WDK audio
- audio non-PCM formats WDK
- non-PCM audio formats WDK , S/PDIF
- WMA Pro WDK audio
- Sony/Philips digital interface
- data ranges WDK audio , WMA Pro
- non-PCM audio formats WDK , WMA Pro
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Specifying WMA Pro Data Ranges


## <span id="specifying_wma_pro_data_ranges"></span><span id="SPECIFYING_WMA_PRO_DATA_RANGES"></span>


The header file Mmreg.h defines the value 0x0164 to be the wave-format tag for WMA Pro-over-S/PDIF:

```cpp
  #define WAVE_FORMAT_WMASPDIF  0x0164
```

The corresponding format-subtype GUID can be specified in terms of the wave-format tag by using the DEFINE\_WAVEFORMATEX\_GUID macro from the header file Ksmedia.h as follows:

```cpp
  #define KSDATAFORMAT_SUBTYPE_WMA_SPDIF    \
                      DEFINE_WAVEFORMATEX_GUID(WAVE_FORMAT_WMASPDIF)
```

The following code example shows how a WaveCyclic or WavePci miniport driver can specify the [**KSDATARANGE\_AUDIO**](https://msdn.microsoft.com/library/windows/hardware/ff537096) table entries for a pin that supports the WMA Pro-over-S/PDIF and AC-3-over-S/PDIF formats:

```cpp
static KSDATARANGE_AUDIO PinDataRangesSpdifOut[] =
{
  // 48-kHz WMA Pro over S/PDIF
  {
    {
      sizeof(KSDATARANGE_AUDIO),
      0,
      0,
      0,
      STATICGUIDOF(KSDATAFORMAT_TYPE_AUDIO),
      STATICGUIDOF(KSDATAFORMAT_SUBTYPE_WMA_SPDIF),
      STATICGUIDOF(KSDATAFORMAT_SPECIFIER_WAVEFORMATEX)
    },
    2,       // Max number of channels
    16,      // Minimum number of bits per sample
    16,      // Maximum number of bits per channel
    48000,   // Minimum rate
    48000    // Maximum rate
  },

  // 44.1-kHz WMA Pro over S/PDIF
  {
    {
      sizeof(KSDATARANGE_AUDIO),
      0,
      0,
      0,
      STATICGUIDOF(KSDATAFORMAT_TYPE_AUDIO),
      STATICGUIDOF(KSDATAFORMAT_SUBTYPE_WMA_SPDIF),
      STATICGUIDOF(KSDATAFORMAT_SPECIFIER_WAVEFORMATEX)
    },
    2,       // Max number of channels
    16,      // Minimum number of bits per sample
    16,      // Maximum number of bits per channel
    44100,   // Minimum rate
    44100    // Maximum rate
  },

  // 48-kHz AC-3 over S/PDIF
  {
    {
      sizeof(KSDATARANGE_AUDIO),
      0,
      0,
      0,
      STATICGUIDOF(KSDATAFORMAT_TYPE_AUDIO),
      STATICGUIDOF(KSDATAFORMAT_SUBTYPE_AC3_SPDIF),
      STATICGUIDOF(KSDATAFORMAT_SPECIFIER_WAVEFORMATEX)
    },
    2,       // Max number of channels
    16,      // Minimum number of bits per sample
    16,      // Maximum number of bits per channel
    48000,   // Minimum rate
    48000    // Maximum rate
  },
};
```

In this code example, the first and second data ranges specify WMA Pro-over-S/PDIF data formats at sample rates of 48 kHz and 44.1 kHz. With these two options, an audio application can play a WMA Pro audio stream recorded at either of these two sample rates, assuming that the external decoder can also handle the sample rate.

The WMA Pro sync frame size is the same at both 48 kHz and 44.1 kHz, and both data ranges use the same PCM parameter values--two channels and 16 bits per channel. For information about the use of PCM parameters to specify data ranges for WMA Pro-over-S/PDIF and AC-3-over-S/PDIF formats, see [S/PDIF Pass-Through Transmission of Non-PCM Streams](s-pdif-pass-through-transmission-of-non-pcm-streams.md).

The third data range specifies an AC-3-over-S/PDIF data format. For more information, see [Specifying AC-3 Data Ranges](specifying-ac-3-data-ranges.md).

The preceding example does not enable DirectSound to handle the non-PCM WMA Pro-over-S/PDIF and AC-3-over-S/PDIF formats on Microsoft Windows 2000 SP2 and Windows 98 SE + hotfix. To enable this capability, the sample code would need to be modified so that for each of the three data ranges that uses the specifier KSDATAFORMAT\_SPECIFIER\_WAVEFORMATEX, a second data range must be included that is identical except that it uses the specifier KSDATAFORMAT\_SPECIFIER\_DSOUND instead. For an example, see [Specifying AC-3 Data Ranges](specifying-ac-3-data-ranges.md).

 

 




