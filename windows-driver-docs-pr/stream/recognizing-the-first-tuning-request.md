---
title: Recognizing the First Tuning Request
author: windows-driver-content
description: Recognizing the First Tuning Request
MS-HAID:
- 'vidcapds\_a4fc0d80-6805-4f72-8af4-467e0b796680.xml'
- 'stream.recognizing\_the\_first\_tuning\_request'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: dc18a056-16f8-4b99-97e3-52c92464a2b2
keywords: ["first tuning requests WDK video capture", "recognizing first tuning requests WDK video capture", "radio tuners WDK video capture"]
---

# Recognizing the First Tuning Request


Some tuners require slewing around a frequency to get valid signal strength/PLL information, so a minidriver may need to recognize when *KsTvTune.ax* is making an initial tuning request.

Each tuning request is actually a pair of requests to the minidriver. The minidriver first receives a set [**KSPROPERTY\_TUNER\_FREQUENCY**](https://msdn.microsoft.com/library/windows/hardware/ff565833) request followed by one or more get [**KSPROPERTY\_TUNER\_STATUS**](https://msdn.microsoft.com/library/windows/hardware/ff565921) requests.

On the first tuning request, there is a delay between the set request and the first get request. The minidriver sets the delay length in milliseconds in the **SettlingTime** member of the [**KSPROPERTY\_TUNER\_MODE\_CAPS\_S**](https://msdn.microsoft.com/library/windows/hardware/ff565872) structure. The get request is repeated every five milliseconds while the **Busy** member of the [**KSPROPERTY\_TUNER\_STATUS\_S**](https://msdn.microsoft.com/library/windows/hardware/ff565925) structure is nonzero, up to five tries.

*KsTvTune.ax* does not consider a tune request complete until it receives a nonbusy status from the device, or if the device is still busy 20 milliseconds after the interval specified by the **SettlingTime** member of the [**KSPROPERTY\_TUNER\_MODE\_CAPS\_S**](https://msdn.microsoft.com/library/windows/hardware/ff565872) structure, whichever comes first.

Thereafter, for each tuning request during fine-tuning mode, there will be a five millisecond interval between the set request and the first get request.

If you want *KsTvTune.ax* to retry at least once after an initial request, always return a **PLLOffset** value of 1 on the first tuning request. *KsTvTune.ax* immediately tries the next step higher, as specified by the **TuningGranularity** member of the [**KSPROPERTY\_TUNER\_MODE\_CAPS\_S**](https://msdn.microsoft.com/library/windows/hardware/ff565872) structure. At that point, you could return a **PLLOffset** value greater than 1 or less than -1 if your minidriver determines that there is no signal, or a **PLLOffset** value of -1 or 0 if your minidriver determines that the signal is good.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20Recognizing%20the%20First%20Tuning%20Request%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


