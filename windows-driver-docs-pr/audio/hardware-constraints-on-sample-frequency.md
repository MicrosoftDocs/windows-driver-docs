---
title: Hardware Constraints on Sample Frequency
description: Hardware Constraints on Sample Frequency
ms.assetid: e0041fd9-073c-4779-a3cf-6d0527ba847b
keywords:
- sample frequency constraints WDK audio
- constraining sample frequency WDK audio
- hardware constraints WDK audio
- frequency constraints WDK audio
- data-intersection handlers WDK audio , sample frequency constraints
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Hardware Constraints on Sample Frequency


## <span id="hardware_constraints_on_sample_frequency"></span><span id="HARDWARE_CONSTRAINTS_ON_SAMPLE_FREQUENCY"></span>


Some audio devices require that the sample frequency at the adapter filter's sink pin match the frequency of a digital output port or the input stream from a microphone. For example, Sound Blaster 16-compatible hardware typically has a single crystal, which constrains its input and output streams to run at the same clock rate. An adapter that can support more than one clock rate for its various on-board audio streams might still need to restrict the number of different clock rates to some small number.

For these reasons, an adapter driver might need to constrain the sample frequency on one on-board stream to match that of another on-board stream. For example, a Sound Blaster 16-compatible adapter might require that the sample frequency at the adapter's sink pin match the rate at which the latches are clocked at the output DACs.

As explained previously, KMixer is the system mixer in Windows Server 2003, Windows XP, Windows 2000, and Windows Me/98. When KMixer's source pin is connected to an adapter's sink pin, KMixer might need to call the adapter's **SetFormat** method (for example, see [**IMiniportWavePciStream::SetFormat**](https://msdn.microsoft.com/library/windows/hardware/ff536732)) to adjust the sample frequency at the connection to match the highest sample frequency of the audio streams at its inputs. If the adapter is unable to change the frequency--perhaps because it is constrained by the clock rates of other on-board streams--it can fail the **SetFormat** call. In this case, KMixer will respond by making more **SetFormat** calls with successively lower sample frequencies until the call succeeds. Once KMixer has settled on a reduced sample frequency, it will sample-down its higher frequency input streams accordingly.

 

 




