---
title: Scanning to Tunable Signals
author: windows-driver-content
description: Scanning to Tunable Signals
ms.assetid: cc934079-5d00-42e0-a024-1b7548bb88e4
keywords:
- signal scanning WDK video capture
- scanning tunable signals WDK video capture
- tunable signals WDK video capture
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Scanning to Tunable Signals


**This section applies only to operating systems starting with Microsoft Windows Vista.**

Signal scanning is the process of locking to the next tunable signal (up or down) that is broadcast along a range of frequency values on a cable or antenna system. For operating systems earlier than Windows Vista, signal scanning is driven largely by software (the *KsTvTune.ax* module) and is based on scanning a known map of channels as opposed to a frequency-based scan of the broadcast spectrum. If an AVStream minidriver that runs on Windows Vista reports back signal-scanning capabilities through a new-for-Windows Vista property in the [PROPSETID\_TUNER](https://msdn.microsoft.com/library/windows/hardware/ff567800) property set, the tuner filter (*KsTvTune.ax*) and the applications above can use those capabilities for scanning. If the driver does not support the new frequency-based scanning functionality, *KsTvTune.ax* falls back to the former channel-based scanning functionality.

The tuner filter and an AVStream minidriver can handle the new frequency-based scanning functionality by using a [hardware-assisted scanning algorithm](hardware-assisted-scanning-algorithm.md).

When scanning completes, the minidriver must signal an event handle. For information about the event operation flow, see [Event Mechanism and Flow](event-mechanism-and-flow.md).

To support the new frequency-based scanning functionality, the minidriver must implement the required property in the following list and optionally implement the remaining properties and the event:

[**KSPROPERTY\_TUNER\_SCAN\_CAPS**](https://msdn.microsoft.com/library/windows/hardware/ff565887) (Required)

[**KSPROPERTY\_TUNER\_SCAN\_STATUS**](https://msdn.microsoft.com/library/windows/hardware/ff565893) (Optional)

[**KSPROPERTY\_TUNER\_NETWORKTYPE\_SCAN\_CAPS**](https://msdn.microsoft.com/library/windows/hardware/ff565881) (Optional)

[**KSEVENT\_TUNER\_INITIATE\_SCAN**](https://msdn.microsoft.com/library/windows/hardware/ff561898) (Optional)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20Scanning%20to%20Tunable%20Signals%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


