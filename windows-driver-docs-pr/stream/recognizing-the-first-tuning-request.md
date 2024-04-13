---
title: Recognizing the First Tuning Request
description: Recognizing the First Tuning Request
keywords:
- first tuning requests WDK video capture
- recognizing first tuning requests WDK video capture
- radio tuners WDK video capture
ms.date: 04/20/2017
---

# Recognizing the First Tuning Request


Some tuners require slewing around a frequency to get valid signal strength/PLL information, so a minidriver may need to recognize when *KsTvTune.ax* is making an initial tuning request.

Each tuning request is actually a pair of requests to the minidriver. The minidriver first receives a set [**KSPROPERTY\_TUNER\_FREQUENCY**](./ksproperty-tuner-frequency.md) request followed by one or more get [**KSPROPERTY\_TUNER\_STATUS**](./ksproperty-tuner-status.md) requests.

On the first tuning request, there is a delay between the set request and the first get request. The minidriver sets the delay length in milliseconds in the **SettlingTime** member of the [**KSPROPERTY\_TUNER\_MODE\_CAPS\_S**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_tuner_mode_caps_s) structure. The get request is repeated every five milliseconds while the **Busy** member of the [**KSPROPERTY\_TUNER\_STATUS\_S**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_tuner_status_s) structure is nonzero, up to five tries.

*KsTvTune.ax* does not consider a tune request complete until it receives a nonbusy status from the device, or if the device is still busy 20 milliseconds after the interval specified by the **SettlingTime** member of the [**KSPROPERTY\_TUNER\_MODE\_CAPS\_S**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_tuner_mode_caps_s) structure, whichever comes first.

Thereafter, for each tuning request during fine-tuning mode, there will be a five millisecond interval between the set request and the first get request.

If you want *KsTvTune.ax* to retry at least once after an initial request, always return a **PLLOffset** value of 1 on the first tuning request. *KsTvTune.ax* immediately tries the next step higher, as specified by the **TuningGranularity** member of the [**KSPROPERTY\_TUNER\_MODE\_CAPS\_S**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_tuner_mode_caps_s) structure. At that point, you could return a **PLLOffset** value greater than 1 or less than -1 if your minidriver determines that there is no signal, or a **PLLOffset** value of -1 or 0 if your minidriver determines that the signal is good.

 

