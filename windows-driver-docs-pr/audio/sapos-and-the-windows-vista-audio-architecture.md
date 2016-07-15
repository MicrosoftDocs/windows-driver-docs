---
Description: sAPOs and the Windows Vista Audio Architecture
MS-HAID: 'audio.sapos\_and\_the\_windows\_vista\_audio\_architecture'
MSHAttr: 'PreferredLib:/library/windows/hardware'
title: sAPOs and the Windows Vista Audio Architecture
---

# sAPOs and the Windows Vista Audio Architecture


The 32-bit versions of Windows Server 2003 and Windows XP process digital audio data for system effects by using global effects filters (GFX filters).

The operating system does not support the Windows XP-style GFX filters. Instead, Windows Vista includes several user-mode in-process COM objects that are installed by default. These objects, called system effects audio processing objects (sAPOs), provide digital signal processing for Windows Vista audio streams. An sAPO is basically a host object that contains an algorithm that is written to provide a specific Digital Signal Processing (DSP) effect.

The following diagram is a simplified representation of the Windows Vista audio architecture. The arrows show the path of a stream of audio data.

![diagram illustrating the basic windows vista audio architecture](images/sysfxapo-ms-components.png)

As the diagram shows, the Windows Vista audio architecture consists of user-mode and kernel-mode components. The audio engine consists of stream and device pipes, which are built from system-supplied audio processing objects (APOs) and sAPOs.

The kernel-mode components have well-defined functionality that is isolated in each component.

Audio endpoint refers to components such as headphones and loudspeakers collectively. As shown in the diagram, an application communicates with an audio endpoint via the endpoint buffer, stream and device pipes and a stack of kernel-mode drivers.

The concepts of pipes, APOs, and sAPOs are explained in more detail in the [Exploring the Windows Vista Audio Engine](exploring-the-windows-vista-audio-engine.md) topic. For more information about the system-supplied sAPOs, see the [Windows Vista Default sAPOs](windows-vista-default-sapos.md) topic.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20sAPOs%20and%20the%20Windows%20Vista%20Audio%20Architecture%20%20RELEASE:%20%287/14/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")


