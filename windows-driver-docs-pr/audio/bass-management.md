---
title: Bass Management
description: Bass Management
ms.date: 06/15/2022
---

# Bass Management

Bass Management users can adjust the movie or music playback experience to maximize the bass effects on the loudspeakers.

In many audio systems, some or all of the loudspeakers have a limited frequency range. In such systems, a single subwoofer is often used for frequencies below the capabilities of the main loudspeakers. Although a system with one subwoofer might not maintain all of the auditory cues in the original source material, such systems are very common. Often they must prefilter the signals to all channels to maximize the bass response.

## Forward bass and reverse management

There are two bass management modes: forward bass management and reverse bass management.

- Forward bass management filters out the low frequency content of the audio data stream. The forward bass management algorithm redirects the filtered output to the subwoofer or to the front-left and front-right loudspeaker channels, depending on the channels that can handle deep bass frequencies. This decision is based on the setting of the LRBig flag.

To set the LRBig flag, the user uses the Sound applet in Control Panel to access the Bass Management Settings dialog box. The user selects a check box to indicate, for example, that the front-right and front-left speakers are full range and this action sets the LRBig flag. To clear this flag, click the check box to clear it.

- Reverse bass management distributes the signal from the subwoofer channel to the other output channels. The signal is directed either to all channels or to the front-left and front-right channels, depending on the setting of the LRBig flag. This process uses a substantial gain reduction when mixing the subwoofer signal into the other channels.

As long as reverse bass management is possible for the current output format, the APO that handles it should always scale gain on the main channels down by a factor of (1.0 + the subwoofer gain) to avoid overloading the channel. This should be done regardless of whether reverse bass management is currently enabled and whether the content that is currently playing has a subwoofer channel.

The bass management mode that is used depends on the availability of a subwoofer and the bass-handling capability of the main speakers. In Windows, the user provides this information via the Sound applet in Control Panel.

The following table summarizes which bass management mode applies in various scenarios. 

The six scenarios are numbered for later reference. FBM and RBM refer to forward and reverse bass management, respectively.

Main speakers |	Subwoofer is present (inverted or noninverted) |	No subwoofer
--------------|-----------------------------------------------|-----------------
All speakers are small|	FBM (Scenario 1)|	Low-frequency protection or bass boost (Scenario 4)
The front left/right speakers are large	FBM (Scenario 2)|	RBM and FBM (Scenario 5)
All speakers are large	N/A (Scenario 3) |	RBM (Scenario 6)

In all six scenarios, the user has at least the following choices:
- Turn off bass management completely.
- Turn on bass management, which causes the sAPO to automatically decide the appropriate bass management mode.

The following list is a case-by-case description of the six scenarios:

**Scenario 1**: Forward bass management. The low-frequency portion of the signal for the speaker channels is redirected to the subwoofer.

**Scenario 2**: Forward bass management. The low-frequency portion of the signal for the speaker channels is redirected as follows:
- If the original channel is off center, the low-frequency signal is redirected to the front-left or front-right channel, depending on which of those two channels is on the same side as the original channel.
- If the original channel is on the center axis, the low-frequency signal is redirected to the subwoofer channel.

**Scenario 3**: No bass management.

**Scenario 4**: Low-frequency protection. The low-frequency portion of each of the main channels is removed. The user can choose to turn on bass boost instead of low-frequency protection.

**Scenario 5**: Both bass management modes applied. There is no way to enable them separately.
- Forward bass management. The low-frequency portion of each of the surround channels is redirected to the front-left or front-right channels, depending on which of those two channels is on the same side as the original channel. If the incoming channel is on the center axis, the low-frequency part of its signal is divided equally between the front-left and front-right channels.
- Reverse bass management The subwoofer signal is sent with equal gain to the front-left and front-right channels, with equal gain.

**Scenario 6**: The subwoofer signal sent with equal gain to each of the main output channels.

Note: In this context, the term surround refers to all main channels other than front-left and front-right channels. It includes the front-center channel. The low-frequency portion refers to frequencies below a user-adjustable crossover frequency.

When a user turns on bass management, the programming logic that the sAPO uses to decide which bass management mode to enable is to:
- Enable reverse bass management if the content has a .1 channel and there is no subwoofer channel. The lack of a subwoofer channel is indicated by either of the following:
- The GFX sAPO does have a .1 channel.
- The NoSub flag is set.
- Enable forward bass management if the subwoofer is present or either of the following are true:
- The LRBig flag is set, indicating that the front and right speakers are large.
- The content has main channels other than the front-left and front-right channels.

When the NoSub and LRBig flags are both set, the content has both surround and subwoofer channels, which calls for both bass management modes.

### Bass Management Settings

The following settings are used to define the speaker configuration programmatically.
- Crossover frequency. Only some speakers, such as the subwoofer, can support frequencies below the crossover frequency. The setting is used for forward bass management, low-frequency protection, and bass boost. Multiple crossover frequencies—such as different values for front and surround speakers—are not supported.
- Speaker size for speakers other than the subwoofer has three settings:
- All big: All speakers can handle unlimited deep bass.
- All small: No speakers can go below the crossover frequency.
- Front LR big: The front left and right speakers are big, and the rest are small. This is referred to subsequently as LRBig.

LRBig allows, for example, forward bass management to work without an output subwoofer channel by redirecting deep bass signals from the surround/rear channels into the front channels. Otherwise, forward bass management requires an output subwoofer channel. Other modes of bass management also must know which main speakers are big.

A flag that is named NoSub is set to indicate that no subwoofer is connected even though the output format advertised by the audio device or GFX input may include a .1 channel. The NoSub flag indicates that the output configuration is effectively N.0 as far as bass management is concerned.

Note that "NoSub" is an explicit setting, separate from the presence of a low-frequency effects (LFE) flag in the output channel mask that indicates a subwoofer. The output channel mask cannot be used to convey the presence or absence of a subwoofer because most drivers do not support N.0 channel masks for N > 4.

### Bass Management Channel Mask Dependencies

Usually, at least some form of bass management is supported. This is true only if all of the following conditions are met:
- NoSub is set to FALSE.
- The output channel mask includes an LFE flag.
- There are no small output speakers. This includes when the speaker setup is LRBig, but stereo content is being played.
