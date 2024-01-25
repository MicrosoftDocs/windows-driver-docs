---
title: Combine Custom and Windows APOs
description: Combine Windows and Custom Audio processing objects (APOs) to provide customizable software based digital signal processing for Windows audio streams.
ms.date: 06/23/2022
---

# Combine custom and Windows APOs

Audio processing objects (APOs), provide customizable software based digital signal processing for Windows audio streams. It is possible to combine Microsoft provided APOs, with partner developed code, wrapping and customizing the existing functionality.

Refer to these topics for general information about APOs.

- [Audio Processing Object Architecture](audio-processing-object-architecture.md)
- [Implementing Audio Processing Objects](implementing-audio-processing-objects.md)
- [Implementing Hardware Offloaded APO Effects](implementing-hardware-offloaded-apo-effects.md)

APOs were first introduced in Windows Vista and you may see references to the earlier system APOs - sAPOs. For more information, see the [Custom Audio Effects in Windows Vista](https://download.microsoft.com/download/9/c/5/9c5b2167-8017-4bae-9fde-d599bac8184a/sysfx.doc) white paper. This white paper may reference older [COM](/windows/win32/com/component-object-model--com--portal) and [UI development](/windows/win32/controls/property-sheets) topics.

## How to combine custom and Windows APOs

This section contains guidelines for implementing custom audio system effects APOs, by creating a thin wrapper around the corresponding APO. *Custom* APO refers to the IHV’s implementation of the APO.

There are two type of APOs, SFX (Stream) and MFX (Mode). In Windows 8.1, SFX were referred to as LFX (local) and MFX was refereed to as GFX (global) APOs.

IHVs can implement custom audio system effects APOs to replace either or both of the Windows SFX and MFX custom audio system effects APOs. Broadly speaking, IHVs or OEMs have two basic strategies for combining custom audio system effects APOs with the APOs that Windows provides. These strategies give the IHVs flexibility on how they integrate their custom effects with those of Windows. 

**Replace**

Develop a detailed understanding of the Windows APO that you want to replace and its features. Use that understanding to implement a custom APO that calls the Windows APO in a way that makes the most sense to the IHV from the perspective of their target user experience. This strategy is best suited to IHVs or OEMs who want to:
- Seamlessly integrate their custom effects with the Windows effects.
- Implement their own UI to control their effects and the effects implemented by the Windows APOs.

For more information on writing an APO see [Windows Audio Processing Objects](windows-audio-processing-objects.md). 

**Thin wrapper** 

Write the custom APO as a thin wrapper around the Windows APO. This strategy is best suited to IHVs or OEMs who want to:
- Add their custom effects in the simplest way possible.
- Have the Windows UI continue to control the effects.

IHV or OEMs who choose Strategy the thin wrapper option, should still review [Windows Audio Processing Objects](windows-audio-processing-objects.md) to obtain a thorough understanding of Windows custom audio system effects.

Note: With the thin wrapper strategy IHVs cannot add UI to control their added custom audio system effects to the Windows Enhancements tab. There is only one Enhancements tab, and it must remain associated with the property page for the Windows APOs. The IHV's UI must be implemented in some other way, such as a separate Control Panel application.

## Programming information

This section covers the general programming issues that must be addressed implement a custom APOs.


Both SFX(Stream) and MFX(Mode) custom audio system effects APOs have the following general characteristics:

- They must be registered as COM in-process server objects that can be instantiated by using CoCreateInstance.
- The CLSIDs are `CLSID_CWMAudioLFXAPO` and `CLSID_CWMAudioGFXAPO`for the SFX and MFX APOs, respectively. The CLSIDs are declared in wmcodecdsp.h and defined in wmcodecdspuuid.lib.
- They must support COM aggregation. However, aggregation is not expected to be used in custom audio system effects scenario, so it should pose no significant problems.

### Initialization

A custom APO must initialize the Window APO by calling its [IAudioSystemEffects::Initialize](/windows/win32/api/audioenginebaseapo/nn-audioenginebaseapo-iaudiosystemeffects) method. This is typically done from the custom APO’s Initialize method. Any arguments that are passed to the custom APO's Initialize method should be passed directly to the Windows APO’s Initialize. This allows the  APO to fetch its settings from the endpoint and Fx property stores in the APOInitSystemEffects structure. It is possible to have the custom APO fetch the settings and selectively pass them to the  APO, but that is essentially Strategy A.

If the custom APO replaces a feature, it is generally advisable to turn off the corresponding feature on the APO. However, turning off the  feature might not be strictly necessary, depending on how the feature works. To turn off a feature, query the APO for its IPropertyStore interface and call [IPropertyStore::SetValue](/windows/win32/api/propsys/nf-propsys-ipropertystore-setvalue). The properties that are supported by the APO's property store are described in "Supported IPropertyStore Properties." later in this topic.

For examples of how to communicate with the Windows custom audio system effects APO property store, see the samples on Github at: 
https://github.com/Microsoft/Windows-driver-samples/tree/main/audio/sysvad/APO

### Query APO's feature state

If a custom APO merely replaces a Windows audio effects feature and does not have its own configuration UI or settings store, it might have to determine what features are enabled on the corresponding  APO. 

There are at least two ways to get this information:

- Option A: By directly querying the Fx property store.

- Option B: Indirectly, by instantiating the APO and using its IPropertyStore interface to query the property store.

### Option A

This option has the advantage that it can be done without instantiating a APO. Also, if a custom APO wants to monitor the Fx property store, Option A is the only way to receive on-the-fly property change notifications. For an example of Option A, see the "compress" sample.

With Option A, the custom APO queries the main endpoint property store—not Fx—for PKEY_AudioEngine_DeviceFormat. It then uses the channel mask from that format as the PID for the property key that is used to query the Fx property store. The GUID (fmtid) for the property key that is used to query the Fx property store is one of the XXX_XXX_KEY_GUID values from wmcodecdsp.h. The _KEY_GUID names correspond in obvious ways to the MFPKEY_ names that were discussed earlier in this topic. 

### Option B

This option has the advantage that it can correctly handle the possibility that the Windows APO could eventually have some of its features enabled by default if the corresponding property in the Fx property store does not exist.

With Option B, the custom APO simply queries the APO for its IPropertyStore interface and calls [IPropertyStore::GetValue](/windows/win32/api/propsys/nf-propsys-ipropertystore-getvalue) by using one of the MFPKEY_XXX keys that were discussed earlier in this topic.

### Format negotiation

When implementing a custom SFX APO that wraps the SFX APO, do not specify `APO_FLAG_FRAMESPERSECOND_MUST_MATCH` in the custom APO's registration properties. This rule should be followed whether or not the custom APO can change the channel format. If the custom SFX APO were to specify this flag, it would prevent the corresponding SFX from doing speaker filling, headphone virtualization, or virtual surround.

A custom SFX APO implementation must implement or override [IAudioProcessingObject::IsInputFormatSupported](/windows/win32/api/audioenginebaseapo/nf-audioenginebaseapo-iaudioprocessingobject-isinputformatsupported). The base class IsInputFormatSupported implementation is unlikely to accurately reflect the set of possible channel conversions that were implemented by the custom SFX APO and the SFX APO.

The custom SFX APO's IsInputFormatSupported method should call the corresponding APO's IsInputFormatSupported. This ensures that the SFX APO handles any channel conversions that are not handled by the custom SFX APO. Note that the SFX APO might be updated to support more conversions in future Windows releases. Calling the APO's IsInputFormatSupported method is one way to ensure that the set of channel conversions that are supported by the custom APO completely contains the set of channel conversions that are supported by the SFX APO.

What the custom APO should do with the return value from the SFX APO's IsInputFormatSupported method depends on what channel conversions, if any, the custom SFX APO supports.

If the custom SFX APO does not support any of its own channel conversions, its IsInputFormatSupported method can return the value that was returned by the SFX APO's IsInputFormatSupported method directly to the caller. For an example, see the "swap" and "compress" samples.

If the custom SFX APO supports its own channel conversions, then a negative return value—including S_FALSE—from the SFX APO's IsInputFormatSupported method does not necessarily translate into a negative return value to the caller. The custom SFX APO could, for example, support channel conversions that are not supported by the corresponding APO. In that case, the custom SFX APO must combine the return value from the SFX APO's IsInputFormatSupported method with its own logic for determining supported inputs. Note that the optimal meaning of "combine" depends on which type of channel conversion should take precedence. The best approach depends on the exact design of the custom implementation.

The IsOutputFormatSupported method on an SFX APO is uninteresting because a SFX APO's output format is the device's mix format. This format is based on external considerations and cannot be affected by an SFX APO or its input format. For that reason, the samples do not attempt to implement correct logic for IsOutputFormatSupported.

The above considerations do not apply to MFX APOs because the MFX APO does not implement any features that require or imply changing the channel format. For that reason, the MFX sample does nothing special for either IsInputFormatSupported or IsOutputFormatSupported. The format negotiation logic of a custom MFX APO is not affected by the fact that it is wrapping the MFX APO.

### LockForProcess/UnlockForProcess

The custom APO's [IAudioProcessingObjectConfiguration::LockForProcess](/windows/win32/api/audioenginebaseapo/nf-audioenginebaseapo-iaudioprocessingobjectconfiguration-lockforprocess) method should call the corresponding method on the APO. LockForProcess() is a good place to make decisions as to the order in which the various processing stages should happen. For example, it can decide whether to apply custom APO processing or the APO's processing first. All three samples provide examples of such decision logic, and the comments in the samples provide some background. However, it is impossible to provide completely general guidance on that subject in this document because it would require knowledge of the specific features of the custom APO and how they might interact with the  APOs features.

### GetLatency

The custom APO’s [IAudioProcessingObject::GetLatency](/windows/win32/api/audioenginebaseapo/nf-audioenginebaseapo-iaudioprocessingobject-getlatency) implementation should call GetLatency on the APO that is being wrapped. If the custom APO processing incurs latency, it should add it to the result that was returned by the APO before returning the value to the caller.

### APOProcess

The custom APO's [IAudioProcessingObjectRT::APOProcess](/windows/win32/api/audioenginebaseapo/nf-audioenginebaseapo-iaudioprocessingobjectrt-apoprocess) method should call the APO's APOProcess method before, after, or even during processing. The decision on when to call APOProcess should be made in LockForProcess, so that any necessary intermediate buffers can be allocated. The  APOs support in-place processing whenever their input and output formats are identical. In that case, the custom APO can pass the same APO_CONNECTION_PROPERTY as both the input and output connection property for the Windows APO. The custom APO should not, however, use the custom APO's input connection property as the output connection property for the APO. In general, APOs should not modify their input buffer.

### Handling APO errors

If a APO returns an error to the corresponding custom APO, the custom APO should act from that point on as if there is no APO. The samples treat all APO errors as equivalent to CoCreateInstance failing to create the APO. Optionally, the custom APO can limit the effect of errors from the APO's LockForProcess method to the current session. In other words, the custom APO does not use the APO during subsequent calls to its APOProcess method. However, the custom APO could try using the APO again if there is another LockForProcess call later, with different formats.

### Compilation and linking

To use the APO CLSID and property key definitions, include wmcodecdsp.h and link with wmcodecdspuuid.lib. For more information, see [wmcodecdsp.h header](/windows/win32/api/wmcodecdsp/).

### APO samples

There are four sample audio system effects samples. The APO samples are available on Github at: 
https://github.com/Microsoft/Windows-driver-samples/tree/main/audio/sysvad/APO 

## General guidelines for custom audio system effects

The following are some guidelines that IHVs should follow when implementing custom audio system effects APOs.

- All audio system effects should provide on/off options. Users should not be forced to use an audio system effect.
- Interactions between features in the SFX and MFX APO should be mediated by the APOs and their related UI.
- Features that are specified as SFX or MFX here can be moved between SFX and MFX in custom implementations. However, this should be done with the understanding that the on/off options should exist and that the accessibility and appropriateness of the options should not be compromised.
- Implementers should remember that the SFX can have different input and output channel masks. The MFX APO must have the same input and output channel masks.

## Windows provided APOs

For information about the other Windows provided APOs, see these topics.

[Bass Boost](bass-boost.md)

[Bass Management](bass-management.md)

[Enhanced Sound for Laptop Computers](enhanced-sound-for-laptop-computers.md)

[Loudness Equalization DSP](loudness-equalization-dsp.md)

[Low Frequency Protection](low-frequency-protection.md)

[Room Correction](room-correction.md)

[Speaker Fill](speaker-fill.md)

[Speaker Phantoming](speaker-phantoming.md)

[Virtual Surround](virtual-surround.md)

[Virtualized Surround Sound over Headphones](virtualized-surround-sound-over-headphones.md)

## Specific APO customization information

### Loudness Equalization (SFX APO)

Loudness equalization is a compressed (dynamics) processing that is driven by a perceptual loudness metric.
Room Correction (MFX APO)

Room correction uses a profile that the Room Calibration Wizard generated. This profile is stored as a binary blob. The format of the blob is not currently published.

### Channel Conversion (SFX APO)

The Channel Conversion APO handles several tasks.

#### Headphone Virtualization

This effect is enabled if the channel format of the content being played back (N.x) is 2.0 or larger, where x can be 0 or 1. The output mask must be stereo (0x3). The input mask is limited to a few supported combinations, which are listed in the table below

**Headphone Virtualization Channel Masks**

Name                     | Value
-------------------------|------
MASK_STEREO MASK_FRONTLR | 0x3
MASK_3_FRONT (SPEAKER_FRONT_CENTER \| MASK_FRONTLR) | 0x7
MASK_4_SQUARE (MASK_FRONTLR \| MASK_BACKLR) | 0x33
MASK_4_DIAMOND (MASK_FRONTLR \| MASK_FBCENTERS) | 0x107
MASK_5_BACK (MASK_FRONTLR \| MASK_BACKLR \| SPEAKER_FRONT_CENTER) | 0x3F
MASK_5_SIDE (MASK_FRONTLR \| MASK_SIDELR \| SPEAKER_FRONT_CENTER) | 0x60F

#### Virtual Surround

This effect is also referred as left /right (LTRT) folddown or left/right matrix encoding. It is used if the channel format of the content that is being played back (N.x) is 2.0 or larger, where x can be 0 or 1. LTRT folddown is normally 4.0 to 2.0. Any other input format is usually handled by first applying N.x to 4.0 generic folddown. However, in our implementation, LTRT folddown is natively 5.1 to 2.0. Any other input is handled by first applying N.x to 5.1 generic folddown first.

The output channel mask must be 0x3 (stereo) and the number of input channels—including the subwoofer if present—must be no more than eight.

#### Speaker Fill

This effect is used when the number of input channels (N) is less than the number of output channels (M). The effect fills N.x channel to M.x channels, where x can be either 0 or 1.

The channel masks in Table 4—ignoring the LFE channel—are supported for speaker fill. Speaker fill supports any combination of input or output subwoofer channel presence, so the numbers on the left are only examples. The actual configurations might or might not have a subwoofer.

**Speaker Fill Channel Masks**

 Name                                           | Value
------------------------------------------------|-------
MASK_STEREO MASK_FRONTLR                        | 0x3
MASK_3_FRONT  (SPEAKER_FRONT_CENTER \| MASK_FRONTLR) | 0x7
MASK_4_SQUARE (MASK_FRONTLR \| MASK_BACKLR) \ | 0x33
MASK_4_DIAMOND (MASK_FRONTLR \| MASK_FBCENTERS) | 0x107
MASK_5_BACK (MASK_FRONTLR \| MASK_BACKLR \| SPEAKER_FRONT_CENTER) | 0x3F
MASK_5_SIDE (MASK_FRONTLR \| MASK_SIDELR \| SPEAKER_FRONT_CENTER) | 0x60F
MASK_7_SIDE_BACK (MASK_FRONTLR \| MASK_BACKLR \| SPEAKER_FRONT_CENTER \| MASK_SIDELR) | 0x63F
MASK_7_FRONT_SIDE (MASK_FRONTLR \| MASK_SIDELR \| SPEAKER_FRONT_CENTER \| MASK_CENTERLR)  | 0x6CF
MASK_7_FRONT_BACK (MASK_FRONTLR \| MASK_BACKLR \| SPEAKER_FRONT_CENTER \| MASK_CENTERLR)| 0xFF

Speaker fill is not supported if any of the following is true:
- The input mask equals the output mask.
- The only difference between input and output is that one has side left/right channels; the other has back left/right channels.
- Input has more main channels than output has.
- The output mask includes the center left/right speakers, but the input mask does not.
- The set of channels in the output but not in the input does not include at least one of: front center, back left/right, or side left/right.

There is one exception to the second item on the list. If the only difference between input and output is that one has side left/right channels and the other has back left/right channels, speaker fill is supported if either format contains channels that would fall between sideLR and backLR in the channel mask bit order. There are three such channels:
- SPEAKER_FRONT_LEFT_OF_CENTER
- SPEAKER_FRONT_RIGHT_OF_CENTER
- SPEAKER_BACK_CENTER

If the input or output mask contains any of these three channels, speaker fill might be supported even though it does not meet the second condition on the list, but only if the other conditions are satisfied. For example, speaker fill from  MASK_7_FRONT_BACK to or from MASK_7_FRONT_SIDE is supported by speaker fill for this reason.

The following table has the full list of channel values.

| Name                          | Value |
|-------------------------------|-------|
| SPEAKER_FRONT_LEFT            | 0x1   |
| SPEAKER_FRONT_RIGHT           | 0x2   |
| SPEAKER_FRONT_CENTER          | 0x4   |
| SPEAKER_LOW_FREQUENCY         | 0x8   |
| SPEAKER_BACK_LEFT             | 0x10  |
| SPEAKER_BACK_RIGHT            | 0x20  |
| SPEAKER_FRONT_LEFT_OF_CENTER  | 0x40  |
| SPEAKER_FRONT_RIGHT_OF_CENTER | 0x80  |
| SPEAKER_BACK_CENTER           | 0x100 |
| SPEAKER_SIDE_LEFT             | 0x200 |
| SPEAKER_SIDE_RIGHT            | 0x400 |

Delays are used for channels in the output configurations that are "outside" the front-back range in the input configuration. Conversely, if a speaker in the output configuration is "between" some speakers in the input configuration in the front-back sense, the output for that speaker is generated by mixing some of the input channels on either side of the output channel.

## Run-Time Considerations when reusing Windows APOs

This section contains some additional information that IHVs and OEMs may find useful when implementing their custom audio system effects.

A custom APO implementation:
- Uses CoCreateInstance to instantiate one or more instances of the Windows custom audio system effects APOs.
- Configures each instance to enable the desired set of features.
- Inserts each instance into an appropriate place within the custom APO’s internal pipeline.

### Why one or more instances?

To avoid undesirable interactions, most features require a certain relative ordering. Because Windows APOs implement multiple features inside a single APO, multiple instances of that APO might be required to ensure correct ordering. For example, assume that three enabled features—A, B, and C—must be ordered ABC. The custom implementation handles B but delegates A and C to the Windows APO. A and C must then be in separate instances of the Microsoft APO so that the custom implementation of B can happen between them.

Windows implements room correction in the MFX APO, which means it is a separate COM object from the SFX APO. A custom implementation could choose to delegate room correction to the Windows implementation but place it in a custom SFX APO. The custom SFX implementation might then need to delegate some processing to the Windows SFX APO implementation and other processing to the Windows MFX APO implementation.

### Handling the limitations of different input-output format combination

Many features—especially bass management—do not work in certain cases. For example, forward bass management is undefined if the bass speaker configuration property is "AllSmall" or "AllLarge" and the output format does not include a subwoofer channel or the NoSub flag is set. It is not always possible to detect the failure during the [IPropertyStore::SetValue](/windows/win32/api/propsys/nf-propsys-ipropertystore-setvalue) call. The method attempts to enable the feature, but the input and output formats are not known at that time because LockForProcess must happen after all property manipulations. This means that it is possible to enable a feature, see it apparently succeed, but not have the corresponding processing take place. 

Two strategies are available for dealing with such situations:
- Carefully study the feature-specific sections of this document to be able to predict exactly when a given feature will or will not succeed.
- Call IPropertyStore::GetValue after LockForProcess is called to check the state of important properties. 

When LockForProcess determines that a particular feature cannot be enabled—because of the input and output formats or the value of some other property—LockForProcess updates the value of the corresponding property in the property store.

### Interaction between Speaker Fill and Bass Management

When speaker fill is on and a subwoofer is connected, forward bass management must occur before speaker fill to avoid comb filtering of the low-frequency signal by the speaker fill's surround delay.

When speaker fill is enabled and no subwoofer is connected, two types of forward bass management are possible:

- If the front left/right speakers are big, forward bass management routes the low-frequency portion of the surround and center channels into the front left/right speakers. Forward bass management must come after speaker fill in this case.
- If all speakers are small, forward bass management becomes low-frequency protection for all main speakers. 

This can occur either before or after speaker fill. However, for performance reasons, it is better to have forward bass management before speaker fill.

The Windows APO implements certain common speaker fill configurations, such as 2.0 => 5.1, with special optimized code that handles reverse bass management in the same step as speaker fill.

### Interaction between Folddown and Bass Management

Headphone virtualization supports only reverse bass management:
- Forward bass management does not make sense with headphone virtualization.
- For implementation simplicity, low-frequency protection and bass boost are not supported.

When any of the headphone virtualization, virtual surround encoding, or speaker fill effects are on, reverse bass management is handled during that step. Reverse bass management is still controlled via the APOs reverse bass management property as if it were a separate feature. In these cases, reverse bass management simply controls the folddown coefficients for the .1 input channel. One open issue is that reverse bass management cannot be disabled when LTRT is on. In that case, reverse bass management uses an unconventional subwoofer channel gain.

The Windows audio system effects APOs apply some minor processing—gain and delay—even when no features are enabled. The goal of such processing is to ensure that the gain and delay parameters do not change when a feature is enabled on the fly. The reason is that delay is inherent in the implementation of some features, and a gain <1 is applied by some features to avoid excessively high output in certain situations. The set of available features depends on the input-output formats and certain properties, and so does the cumulative normalization gain and delay.

If features will not be turned on or off on the fly, normalization gain can be disabled by setting the `MFPKEY_CORR_NORMALIZATION_GAIN` property to FALSE by calling [IPropertyStore::SetValue](/windows/win32/api/propsys/nf-propsys-ipropertystore-setvalue). The property might be TRUE by default.

There is no mechanism to disable the normalization delay because it is presumed less likely to be objectionable than normalization gain. If normalization delay is objectionable, simply bypass the APO in question.

## See also

- [Audio Processing Object Architecture](audio-processing-object-architecture.md)
- [Implementing Audio Processing Objects](implementing-audio-processing-objects.md)

