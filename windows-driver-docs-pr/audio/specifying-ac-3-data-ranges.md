---
title: Specifying AC-3 Data Ranges
description: Specifying AC-3 Data Ranges
ms.assetid: 87d59554-43fa-4d61-9829-c38691d0a525
keywords:
- S/PDIF pass-through WDK audio
- AC-3-over-S/PDIF format WDK audio
- audio non-PCM formats WDK
- non-PCM audio formats WDK , S/PDIF
- WMA Pro WDK audio
- AC-3 WDK audio
- Sony/Philips digital interface
- data ranges WDK audio , AC-3
- non-PCM audio formats WDK , AC-3
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Specifying AC-3 Data Ranges


## <span id="specifying_ac_3_data_ranges"></span><span id="SPECIFYING_AC_3_DATA_RANGES"></span>


The header file Mmreg.h defines the value 0x0092 to be the wave-format tag for AC-3-over-S/PDIF:

```cpp
    #define WAVE_FORMAT_DOLBY_AC3_SPDIF  0x0092
```

Wave-format tags 0x0240 and 0x0241 are synonymous with 0x0092 and many DVD applications treat the three tags as identical. However, to eliminate redundancy, drivers and applications should support only tag 0x0092 (and not support tags 0x0240 and 0x0241).

The corresponding format-subtype GUID can be specified in terms of the wave-format tag by using the DEFINE\_WAVEFORMATEX\_GUID macro from the header file Ksmedia.h as follows:

```cpp
  #define KSDATAFORMAT_SUBTYPE_AC3_SPDIF    \
                      DEFINE_WAVEFORMATEX_GUID(WAVE_FORMAT_DOLBY_AC3_SPDIF)
```

The following code example shows how a WaveCyclic or WavePci miniport driver can specify the [**KSDATARANGE\_AUDIO**](https://msdn.microsoft.com/library/windows/hardware/ff537096) table entries for a pin that supports the AC-3-over-S/PDIF format:

```cpp
static KSDATARANGE_AUDIO PinDataRangesAC3Stream[] =
{
  // 48-kHz AC-3 over S/PDIF
  {
    {
      sizeof(KSDATARANGE_AUDIO),
      0,
      0,
      0,
      STATICGUIDOF(KSDATAFORMAT_TYPE_AUDIO),
      STATICGUIDOF(KSDATAFORMAT_SUBTYPE_DOLBY_AC3_SPDIF),
      STATICGUIDOF(KSDATAFORMAT_SPECIFIER_WAVEFORMATEX)
    },
    2,     // Max number of channels
    16,    // Minimum number of bits per sample
    16,    // Maximum number of bits per channel
    48000, // Minimum rate
    48000  // Maximum rate
  },

  // If you do not include this second data range (which is identical
  // to the first except for the value KSDATAFORMAT_SPECIFIER_DSOUND),
  // then your non-PCM pin is not seen by DirectSound on Windows 98 SE
  // or Windows 2000, regardless of the DirectX version or whether a
  // hotfix or service pack is installed.
  {
    {
      sizeof(KSDATARANGE_AUDIO),
      0,
      0,
      0,
      STATICGUIDOF(KSDATAFORMAT_TYPE_AUDIO),
      STATICGUIDOF(KSDATAFORMAT_SUBTYPE_DOLBY_AC3_SPDIF),
      STATICGUIDOF(KSDATAFORMAT_SPECIFIER_DSOUND)
    },
    2,     // Max number of channels
    16,    // Minimum number of bits per sample
    16,    // Maximum number of bits per channel
    48000, // Minimum rate
    48000  // Maximum rate
  }
};
```

The second data-range entry in the preceding table is necessary to enable DirectSound to handle the non-PCM AC-3-over-S/PDIF format in Windows 2000 SP2 and in Microsoft Windows 98 SE + hotfix.

For each data range that the miniport driver specifies with KSDATAFORMAT\_SPECIFIER\_WAVEFORMATEX, the port driver automatically adds a second data range that is specified with KSDATAFORMAT\_SPECIFIER\_DSOUND but is otherwise identical to the first. (You can verify this by using the [KsStudio utility](ksstudio-utility.md) to view the list of data ranges.) In Windows 2000 and Windows 98, the port driver creates KSDATAFORMAT\_SPECIFIER\_DSOUND versions of data ranges only for KSDATAFORMAT\_SUBTYPE\_PCM formats because DirectSound versions before DirectSound 8 support only PCM. This limitation is removed in Windows XP and later and in Windows Me. However, it is not removed in Windows 2000 SP2 or in the hot-fix package for Windows 98 SE, and to support non-PCM on DirectSound on these Windows versions, a driver should explicitly list two data ranges for each non-PCM data format--one with KSDATAFORMAT\_SPECIFIER\_WAVEFORMATEX, and another with KSDATAFORMAT\_SPECIFIER\_DSOUND.

As explained in [S/PDIF Pass-Through Transmission of Non-PCM Streams](s-pdif-pass-through-transmission-of-non-pcm-streams.md), the two AC-3-over-S/PDIF data ranges both use the following PCM parameters: two channels and 16 bits per channel.

 

 




