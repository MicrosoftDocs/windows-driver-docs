---
title: Custom Rendering in User Mode
description: Custom Rendering in User Mode
ms.assetid: a30c9eae-c3a9-4ff8-8e6c-d98c83f8596e
keywords:
- DirectMusic custom rendering WDK audio
- DirectMusic custom rendering WDK audio , about user-mode custom rendering
- Microsoft Software Synthesizer WDK audio
- custom synths WDK audio
- user-mode synths WDK audio , custom
- customizing user mode rendering WDK audio
- wave sinks WDK audio , user-mode custom rendering
- DirectMusic WDK audio , custom synths
- custom rendering in user mode WDK audio
- custom rendering in user mode WDK audio , about custom rendering
- DirectMusic WDK audio , user mode
- default synthesizers
- synthesizers WDK audio , user-mode custom rendering
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Custom Rendering in User Mode


## <span id="custom_rendering_in_user_mode"></span><span id="CUSTOM_RENDERING_IN_USER_MODE"></span>


The Microsoft Software Synthesizer is a user-mode component of the DirectMusic installation and should be adequate for most synthesizer purposes. DirectMusic uses this component as its default synthesizer.

In addition, DirectMusic allows you to implement your own user-mode software synthesizer. The synthesizer accepts an input stream consisting of MIDI events, and it generates an output stream containing wave data. Typically, a custom synthesizer feeds its generated wave stream to DirectMusic's built-in wave sink, which plays the stream through Microsoft DirectSound. However, in Microsoft DirectX 6.1 and 7, DirectMusic allows you to use a custom, user-mode wave sink to redirect rendered wave output to a device other than DirectSound. However, custom wave sinks are seldom necessary. In DirectX 8 and later, DirectMusic provides no support for custom wave sinks.

The most important header files for DirectMusic synths are dmusics.h (user mode only), dmusicks.h (kernel mode only), dmusbuff.h, and dmusprop.h.

The remainder of this section discusses various aspects of customizing the rendering process. The examples in this section assume a user-mode implementation, although the concepts that they present apply to both user and kernel mode, except where noted otherwise. The following topics are discussed:

[Synthesizers and Wave Sinks](synthesizers-and-wave-sinks.md)

[IDirectMusicSynth and IDirectMusicSynthSink](idirectmusicsynth-and-idirectmusicsynthsink.md)

[MIDI to Wave](midi-to-wave.md)

[Synthesizer Timing](synthesizer-timing.md)

[DLS Download Support](dls-download-support.md)

[Registering Your Synthesizer](registering-your-synthesizer.md)

 

 




