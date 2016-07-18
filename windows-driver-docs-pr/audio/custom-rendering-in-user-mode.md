---
title: Custom Rendering in User Mode
description: Custom Rendering in User Mode
ms.assetid: a30c9eae-c3a9-4ff8-8e6c-d98c83f8596e
keywords: ["DirectMusic custom rendering WDK audio", "DirectMusic custom rendering WDK audio , about user-mode custom rendering", "Microsoft Software Synthesizer WDK audio", "custom synths WDK audio", "user-mode synths WDK audio , custom", "customizing user mode rendering WDK audio", "wave sinks WDK audio , user-mode custom rendering", "DirectMusic WDK audio , custom synths", "custom rendering in user mode WDK audio", "custom rendering in user mode WDK audio , about custom rendering", "DirectMusic WDK audio , user mode", "default synthesizers", "synthesizers WDK audio , user-mode custom rendering"]
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20Custom%20Rendering%20in%20User%20Mode%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




