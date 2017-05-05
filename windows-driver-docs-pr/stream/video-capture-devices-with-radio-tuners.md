---
title: Video Capture Devices with Radio Tuners
author: windows-driver-content
description: Video Capture Devices with Radio Tuners
ms.assetid: 36e3ca98-cb1b-46cc-809a-8c9ad08a53c8
keywords:
- radio tuners WDK video capture
- PLL offsets WDK video capture
- signal strength WDK video capture
- manual radio tuning WDK video capture
- FM tuners WDK video capture
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Video Capture Devices with Radio Tuners


Microsoft Windows XP and later, and Microsoft DirectX 8.1 and later provide support for video capture devices that include FM radio tuners.

A video capture minidriver for a device with an FM tuner should support the [**KSPROPERTY\_TUNER\_STATUS**](https://msdn.microsoft.com/library/windows/hardware/ff565921) property. This will allow user-mode clients to retrieve a [**KSPROPERTY\_TUNER\_STATUS\_S**](https://msdn.microsoft.com/library/windows/hardware/ff565925) structure that describes the progress of tuning operations.

Minidrivers can support one of three tuning strategies:

1.  **Tuning by PLL offset.**

    If your FM tuner hardware supports tuning through PLL offset, your minidriver should set the **Strategy** member of the [**KSPROPERTY\_TUNER\_MODE\_CAPS\_S**](https://msdn.microsoft.com/library/windows/hardware/ff565872) structure to KS\_TUNER\_STRATEGY\_PLL.

    If your FM tuner hardware does not provide PLL support, the minidriver should emulate PLL support by using the native signal strength indicator. The system-supplied FM tuning logic in *KsTvTune.ax* is enabled only if the minidriver specifies that it supports the **KS\_TUNER\_STRATEGY\_PLL** strategy.

2.  **Tuning by Signal Strength.**

    If the minidriver sets the **Strategy** member of the KSPROPERTY\_TUNER\_MODE\_CAPS\_S structure to KS\_TUNER\_STRATEGY\_SIGNAL\_STRENGTH, *KsTvTune.ax* still attempts to use the **PLLOffset** member of the KSPROPERTY\_TUNER\_STATUS\_S structure. Consequently, this is not a valid option for future compatibility.

    In addition, the minidriver should set the **SignalStrength** member of the [**KSPROPERTY\_TUNER\_STATUS\_S**](https://msdn.microsoft.com/library/windows/hardware/ff565925) structure to -1, 0, or 1, depending on whether an acceptable frequency is currently selected. Vendors decide what Receiver Signal Strength Indicator (RSSI) or decibel millivolt (dBmV) level above or below the baseline voltage constitutes an acceptable signal for FM reception.

3.  **Tuning performed manually by the minidriver.**

    Set the **Strategy** member of the [**KSPROPERTY\_TUNER\_MODE\_CAPS\_S**](https://msdn.microsoft.com/library/windows/hardware/ff565872) structure to **KS\_TUNER\_STRATEGY\_DRIVER\_TUNES** to control tuning logic in the minidriver.

In FM mode, *KsTvTune.ax* steps through the 200-kHz band around a frequency (100 kHz on either side), using the minidriver-specified **TuningGranularity** member of the [**KSPROPERTY\_TUNER\_MODE\_CAPS\_S**](https://msdn.microsoft.com/library/windows/hardware/ff565872) structure as a step size. The search stops when *KsTvTune.ax* has searched the entire 200 kHz band, or when the minidriver determines that a good signal has been found, whichever occurs first.

Tuning takes much longer if the minidriver always specifies a **PLLOffset** value of -1 or 1. In this case, the tuning logic in *KsTvTune.ax* retries overlapping frequency ranges. The minidriver should specify a **PLLOffset** of -1 or 1 only on the first tuning request, or when the tuner is within eight steps of the best signal. For more information about tuning requests see [Recognizing the First Tuning Request](recognizing-the-first-tuning-request.md).

The tuning process always starts at the center frequency, as requested by an application, and steps up no higher than 100 kHz above the center. However, if the **PLLOffset** becomes 1 near the upper 100-kHz limit, the tuning logic steps beyond the 100-kHz band.

If the tuning process does not find an acceptable signal in the upper range, it tries below the center frequency, stepping up from no lower than 100 kHz below the center and ending at the center frequency if it still has found no acceptable signal. Again, if the **PLLOffset** becomes 1 near the center frequency, tuning steps beyond the center frequency before finally returning to it.

A **PLLOffset** member value of -1 or 1 on the first tuning request causes *KsTvTune.ax* to enter fine-tuning mode. Fine-tuning mode consists of tuning requests in rapid succession at step intervals specified by the **TuningGranularity** member of the [**KSPROPERTY\_TUNER\_MODE\_CAPS\_S**](https://msdn.microsoft.com/library/windows/hardware/ff565872) structure in the direction indicated by **PLLOffset**.

*KsTvTune.ax* stops its tuning attempt if it is unsuccessful after eight fine-tuning steps in either increasing or decreasing frequencies. After *KsTvTune.ax* is in fine-tuning mode, if **PLLOffset** changes direction from -1 to 1, or 1 to -1, or becomes 0, the tuning request is considered successful. Both the fine-tuning and the search through the 200 kHz band stop at that point.

However, if **PLLOffset** is greater than 1 or less than -1, fine-tuning either does not start, or is abandoned. Fine-tuning mode is independent of the search through the 200 kHz band around the center frequency, although both use the step size specified in **TuningGranularity** (thus the caution against always returning a **PLLOffset** of -1..1).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20Video%20Capture%20Devices%20with%20Radio%20Tuners%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


