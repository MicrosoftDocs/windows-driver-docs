---
title: Event Mechanism and Flow
author: windows-driver-content
description: Event Mechanism and Flow
ms.assetid: 13a6c6fb-3615-44ef-bf01-5003520b3e26
keywords:
- event operation flow WDK video capture
- terminating scanning WDK video capture
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Event Mechanism and Flow


**This section applies only to operating systems starting with Microsoft Windows Vista.**

When a scan operation completes, the driver notifies an application through an event handle that the **EventData** member of the [**KSEVENT\_TUNER\_INITIATE\_SCAN\_S**](https://msdn.microsoft.com/library/windows/hardware/ff561901) structure specifies. However, to determine the actual lock status of the scan operation, the driver's [**KSPROPERTY\_TUNER\_SCAN\_STATUS**](https://msdn.microsoft.com/library/windows/hardware/ff565893) property must be called.

Like all kernel-streaming event requests, the application can cancel a [**KSEVENT\_TUNER\_INITIATE\_SCAN**](https://msdn.microsoft.com/library/windows/hardware/ff561898) event request before the event completes. When the application requires the cancellation of the current scan operation, the tuner filter (*KsTvTune.ax*) sets the **StartFrequency** and **EndFrequency** members of KSEVENT\_TUNER\_INITIATE\_SCAN\_S to zero in a call to the driver's KSEVENT\_TUNER\_INITIATE\_SCAN. The driver might perform an entire cleanup. However, because *KsTvTune.ax* might request another entire scan operation, the driver might not perform an entire cleanup. The call to cancel a scan operation is a synchronous operation.

When the application requires the termination of scanning, *KsTvTune.ax* calls KSEVENT\_TUNER\_INITIATE\_SCAN with **StartFrequency** and **EndFrequency** set to zero to unregister the event. The driver then must perform the entire cleanup of its worker threads and other internal data structures.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20Event%20Mechanism%20and%20Flow%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


