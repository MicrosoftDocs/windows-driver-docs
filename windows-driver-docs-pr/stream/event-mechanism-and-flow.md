---
title: Event Mechanism and Flow
description: Event Mechanism and Flow
keywords:
- event operation flow WDK video capture
- terminating scanning WDK video capture
ms.date: 04/20/2017
---

# Event Mechanism and Flow


**This section applies only to operating systems starting with Microsoft Windows Vista.**

When a scan operation completes, the driver notifies an application through an event handle that the **EventData** member of the [**KSEVENT\_TUNER\_INITIATE\_SCAN\_S**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksevent_tuner_initiate_scan_s) structure specifies. However, to determine the actual lock status of the scan operation, the driver's [**KSPROPERTY\_TUNER\_SCAN\_STATUS**](./ksproperty-tuner-scan-status.md) property must be called.

Like all kernel-streaming event requests, the application can cancel a [**KSEVENT\_TUNER\_INITIATE\_SCAN**](./ksevent-tuner-initiate-scan.md) event request before the event completes. When the application requires the cancellation of the current scan operation, the tuner filter (*KsTvTune.ax*) sets the **StartFrequency** and **EndFrequency** members of KSEVENT\_TUNER\_INITIATE\_SCAN\_S to zero in a call to the driver's KSEVENT\_TUNER\_INITIATE\_SCAN. The driver might perform an entire cleanup. However, because *KsTvTune.ax* might request another entire scan operation, the driver might not perform an entire cleanup. The call to cancel a scan operation is a synchronous operation.

When the application requires the termination of scanning, *KsTvTune.ax* calls KSEVENT\_TUNER\_INITIATE\_SCAN with **StartFrequency** and **EndFrequency** set to zero to unregister the event. The driver then must perform the entire cleanup of its worker threads and other internal data structures.

 

