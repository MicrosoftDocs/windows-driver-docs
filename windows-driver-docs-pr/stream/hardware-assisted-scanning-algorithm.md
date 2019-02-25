---
title: Hardware-Assisted Scanning Algorithm
description: Hardware-Assisted Scanning Algorithm
ms.assetid: 9a24b985-9667-4424-84e5-b1c728b3c558
keywords:
- hardware-assisted scanning WDK video capture
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Hardware-Assisted Scanning Algorithm


**This section applies only to operating systems starting with Microsoft Windows Vista.**

A driver sets the **fSupportsHardwareAssistedScanning** member of the [**KSPROPERTY\_TUNER\_SCAN\_CAPS\_S**](https://msdn.microsoft.com/library/windows/hardware/ff565892) structure in a call to its [**KSPROPERTY\_TUNER\_SCAN\_CAPS**](https://msdn.microsoft.com/library/windows/hardware/ff565887) property to indicate that it and its associated hardware support event-based scanning operations. The tuner filter (*KsTvTune.ax*) calls the driver's KSPROPERTY\_TUNER\_SCAN\_CAPS property to determine whether the driver supports hardware-assisted scanning. The tuner filter also calls the KSPROPERTY\_TUNER\_SCAN\_CAPS to determine the broadcast network types that the driver supports scanning on. If the driver supports hardware-assisted scanning, it can return scanning capabilities of each supported broadcast network type through its [**KSPROPERTY\_TUNER\_NETWORKTYPE\_SCAN\_CAPS**](https://msdn.microsoft.com/library/windows/hardware/ff565881) property. Scanning capabilities include, for example, providing the amount of time that the tuning device requires for a frequency setting to become stable (settling time) and providing the frequency ranges that the tuning filter can use to sense the presence of a tunable signal (sensing ranges). For information about scanning capabilities of an analog broadcast network, see the [**TUNER\_ANALOG\_CAPS\_S**](https://msdn.microsoft.com/library/windows/hardware/ff568547) structure.

*KsTvTune.ax* uses the settling-time value as an approximation. *KsTvTune.ax* can provide an application with a close estimate for how long the scan process might take based on the scanning frequency range and the sensing range. After the driver's [**KSEVENT\_TUNER\_INITIATE\_SCAN**](https://msdn.microsoft.com/library/windows/hardware/ff561898) event is called to start the scanning process, the application can wait for the event notification for the stipulated time.

For hardware-assisted scanning, depending on whether the tuning device has locked onto a signal, the driver returns either Tuner\_LockType\_None or Tuner\_LockType\_Locked status from a call to its [**KSPROPERTY\_TUNER\_SCAN\_STATUS**](https://msdn.microsoft.com/library/windows/hardware/ff565893) property. If the driver has locked onto a signal, the driver also returns the frequency of the locked signal.

 

 




