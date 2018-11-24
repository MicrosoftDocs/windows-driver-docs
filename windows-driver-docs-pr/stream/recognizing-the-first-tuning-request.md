---
title: Recognizing the First Tuning Request
description: Recognizing the First Tuning Request
ms.assetid: dc18a056-16f8-4b99-97e3-52c92464a2b2
keywords:
- first tuning requests WDK video capture
- recognizing first tuning requests WDK video capture
- radio tuners WDK video capture
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Recognizing the First Tuning Request


Some tuners require slewing around a frequency to get valid signal strength/PLL information, so a minidriver may need to recognize when *KsTvTune.ax* is making an initial tuning request.

Each tuning request is actually a pair of requests to the minidriver. The minidriver first receives a set [**KSPROPERTY\_TUNER\_FREQUENCY**](https://msdn.microsoft.com/library/windows/hardware/ff565833) request followed by one or more get [**KSPROPERTY\_TUNER\_STATUS**](https://msdn.microsoft.com/library/windows/hardware/ff565921) requests.

On the first tuning request, there is a delay between the set request and the first get request. The minidriver sets the delay length in milliseconds in the **SettlingTime** member of the [**KSPROPERTY\_TUNER\_MODE\_CAPS\_S**](https://msdn.microsoft.com/library/windows/hardware/ff565872) structure. The get request is repeated every five milliseconds while the **Busy** member of the [**KSPROPERTY\_TUNER\_STATUS\_S**](https://msdn.microsoft.com/library/windows/hardware/ff565925) structure is nonzero, up to five tries.

*KsTvTune.ax* does not consider a tune request complete until it receives a nonbusy status from the device, or if the device is still busy 20 milliseconds after the interval specified by the **SettlingTime** member of the [**KSPROPERTY\_TUNER\_MODE\_CAPS\_S**](https://msdn.microsoft.com/library/windows/hardware/ff565872) structure, whichever comes first.

Thereafter, for each tuning request during fine-tuning mode, there will be a five millisecond interval between the set request and the first get request.

If you want *KsTvTune.ax* to retry at least once after an initial request, always return a **PLLOffset** value of 1 on the first tuning request. *KsTvTune.ax* immediately tries the next step higher, as specified by the **TuningGranularity** member of the [**KSPROPERTY\_TUNER\_MODE\_CAPS\_S**](https://msdn.microsoft.com/library/windows/hardware/ff565872) structure. At that point, you could return a **PLLOffset** value greater than 1 or less than -1 if your minidriver determines that there is no signal, or a **PLLOffset** value of -1 or 0 if your minidriver determines that the signal is good.

 

 




