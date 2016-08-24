---
title: Hardware-Assisted Scanning Algorithm
author: windows-driver-content
description: Hardware-Assisted Scanning Algorithm
MS-HAID:
- 'vidcapds\_fb8f5306-bcf5-489b-9063-96ae0797ce4b.xml'
- 'stream.hardware\_assisted\_scanning\_algorithm'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 9a24b985-9667-4424-84e5-b1c728b3c558
keywords: ["hardware-assisted scanning WDK video capture"]
---

# Hardware-Assisted Scanning Algorithm


**This section applies only to operating systems starting with Microsoft Windows Vista.**

A driver sets the **fSupportsHardwareAssistedScanning** member of the [**KSPROPERTY\_TUNER\_SCAN\_CAPS\_S**](https://msdn.microsoft.com/library/windows/hardware/ff565892) structure in a call to its [**KSPROPERTY\_TUNER\_SCAN\_CAPS**](https://msdn.microsoft.com/library/windows/hardware/ff565887) property to indicate that it and its associated hardware support event-based scanning operations. The tuner filter (*KsTvTune.ax*) calls the driver's KSPROPERTY\_TUNER\_SCAN\_CAPS property to determine whether the driver supports hardware-assisted scanning. The tuner filter also calls the KSPROPERTY\_TUNER\_SCAN\_CAPS to determine the broadcast network types that the driver supports scanning on. If the driver supports hardware-assisted scanning, it can return scanning capabilities of each supported broadcast network type through its [**KSPROPERTY\_TUNER\_NETWORKTYPE\_SCAN\_CAPS**](https://msdn.microsoft.com/library/windows/hardware/ff565881) property. Scanning capabilities include, for example, providing the amount of time that the tuning device requires for a frequency setting to become stable (settling time) and providing the frequency ranges that the tuning filter can use to sense the presence of a tunable signal (sensing ranges). For information about scanning capabilities of an analog broadcast network, see the [**TUNER\_ANALOG\_CAPS\_S**](https://msdn.microsoft.com/library/windows/hardware/ff568547) structure.

*KsTvTune.ax* uses the settling-time value as an approximation. *KsTvTune.ax* can provide an application with a close estimate for how long the scan process might take based on the scanning frequency range and the sensing range. After the driver's [**KSEVENT\_TUNER\_INITIATE\_SCAN**](https://msdn.microsoft.com/library/windows/hardware/ff561898) event is called to start the scanning process, the application can wait for the event notification for the stipulated time.

For hardware-assisted scanning, depending on whether the tuning device has locked onto a signal, the driver returns either Tuner\_LockType\_None or Tuner\_LockType\_Locked status from a call to its [**KSPROPERTY\_TUNER\_SCAN\_STATUS**](https://msdn.microsoft.com/library/windows/hardware/ff565893) property. If the driver has locked onto a signal, the driver also returns the frequency of the locked signal.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20Hardware-Assisted%20Scanning%20Algorithm%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


