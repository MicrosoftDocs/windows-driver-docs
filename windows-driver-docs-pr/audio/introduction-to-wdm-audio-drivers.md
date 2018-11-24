---
title: Introduction to WDM Audio Drivers
description: Introduction to WDM Audio Drivers
ms.assetid: 376392a8-b3ae-40c3-8bfa-55df6165cefb
keywords:
- audio filters WDK audio , subset of KS filters
- WDM audio drivers WDK , about WDM audio drivers
- audio drivers WDK , about audio drivers
- KS filters WDK audio , about KS filters
- filters WDK audio , KS
- KS pins WDK audio
- KS pins WDK audio , about KS pins
- pins WDK audio , KS
- audio jacks WDK
- output pins WDK audio
- input pins WDK audio
- filter factories WDK audio
- pin factories WDK audio
- kernel streaming WDK audio
- filter graphs WDK audio
- speakers WDK audio
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Introduction to WDM Audio Drivers


## <span id="introduction_to_wdm_audio_drivers"></span><span id="INTRODUCTION_TO_WDM_AUDIO_DRIVERS"></span>


Kernel streaming (KS) services support kernel-mode processing of data streams for audio and for other types of continuous media. Conceptually, a stream undergoes processing as it flows along a data path containing some number of processing nodes. A set of related nodes is grouped together to form a *KS filter*, which represents a more-or-less independent block of stream-processing functionality. More complex functions can be constructed in a modular way by cascading several filters together to form a *filter graph*.

A typical audio adapter card might contain audio devices for playing a wave stream through a set of speakers, converting the audio signal from a microphone to a wave stream, and synthesizing sound from a MIDI stream. The adapter driver can wrap each of these audio devices in a KS filter that it exposes to the operating system. The operating system connects the filters to other filters to form filter graphs that process audio streams on behalf of application programs.

KS filters are connected together through their *pins*. A pin on an audio filter can be thought of as an audio jack. A client instantiates an input or output pin on a filter when the client needs to route a data stream into or out of that filter. In some contexts, the terms *pin* and *stream* can be used interchangeably.

The output pin of the upstream filter is connected to the input pin of the downstream filter. The data stream from the output pin must have a data format that the input pin can accept. Data buffering is typically required to smooth out momentary mismatches in the rates at which an output pin produces data and an input pin consumes it.

A KS filter is implemented as a kernel-mode driver object that encapsulates some number of related stream-processing functions. The functionality can be implemented in software or in hardware. In this model, an audio adapter can be viewed as a collection of hardware devices, and the adapter driver exposes each of these devices to the audio system as an individual filter.

An adapter driver exposes a collection of *filter factories* to the audio system. Each filter factory is capable of instantiating filters of a particular type:

-   If the adapter contains one or more devices that are similar or identical in function, the driver groups the filters for those devices together into the same filter factory.

-   If the adapter contains several different types of devices, those devices are presented through several different filter factories.

A KS filter exposes a collection of *pin factories* to the audio system. Each pin factory is capable of instantiating pins of a particular type. If the filter can provide one or more pins that are similar or identical in function, the filter groups those pins together into the same pin factory. For example, a filter that performs audio mixing might have one pin factory that can instantiate a single output pin and a second pin factory that can instantiate several input pins.

KS services are built upon the Windows Driver Model. Note that the term *KS filter* must be distinguished from the term *filter driver*, which is another WDM concept. A filter driver resides in a WDM driver stack and can intercept and modify the I/O request packets (IRPs) that propagate through the stack. Upper- and lower-level filter drivers reside above and below the function driver, respectively. In this section, the term *filter* refers to a KS filter rather than a filter driver unless noted otherwise. For more information about filter drivers, see [Types of WDM Drivers](https://msdn.microsoft.com/library/windows/hardware/ff564862).

This section contains the following topics:

[Basic Functions of a WDM Audio Driver](basic-functions-of-a-wdm-audio-driver.md)

[Vendor Audio Driver Options](vendor-audio-driver-options.md)

[WDM Audio Terminology](wdm-audio-terminology.md)

[Sample Audio Drivers](sample-audio-drivers.md)

[KsStudio Utility](ksstudio-utility.md)

For updates and information about new features of the WDM audio architecture, see the [audio technology](https://go.microsoft.com/fwlink/p/?linkid=8751) website.

 

 




