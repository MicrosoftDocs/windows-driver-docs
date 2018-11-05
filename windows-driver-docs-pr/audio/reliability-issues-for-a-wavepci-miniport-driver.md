---
title: Reliability Issues for a WavePci Miniport Driver
description: Reliability Issues for a WavePci Miniport Driver
ms.assetid: 329f28a8-5e99-4c25-8a88-1e634f7eeec8
keywords:
- WavePci reliability issues WDK audio
- spin locks WDK audio
- canceling IRPs
- deadlocks WDK audio
- interrupt service routines WDK audio
- ISRs WDK audio
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Reliability Issues for a WavePci Miniport Driver


## <span id="reliability_issues_for_a_wavepci_miniport_driver"></span><span id="RELIABILITY_ISSUES_FOR_A_WAVEPCI_MINIPORT_DRIVER"></span>


A WavePci miniport driver must keep track of the mappings that it receives from the port driver. A WavePci miniport driver maintains its list of mappings in a data structure that is shared between driver threads. The driver threads must also share access to the DMA channel in order to add new mappings to the hardware queue and remove completed mappings from the queue. To prevent data corruption, miniport drivers use spin locks to serialize accesses to shared data structures and peripherals. A spin lock protects the shared data and hardware queue from simultaneous access by two or more driver threads.

When developing the portion of the driver that manages mappings, vendors should pay particular attention to the following points.

### <span id="Spin_Locks"></span><span id="spin_locks"></span><span id="SPIN_LOCKS"></span>Spin Locks

To avoid potential deadlocks, the miniport driver must not hold its own spin lock when calling into Portcls.sys to acquire or release mappings. The Ac97 sample driver in the Microsoft Windows Driver Kit (WDK) illustrates this principle. Before calling either [**IPortWavePciStream::GetMapping**](https://msdn.microsoft.com/library/windows/hardware/ff536909) or [**IPortWavePciStream::ReleaseMapping**](https://msdn.microsoft.com/library/windows/hardware/ff536911), the sample driver calls [**KeReleaseSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff553145) to release the spin lock. After the **GetMapping** or **ReleaseMapping** call returns, the driver calls [**KeAcquireSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff551917) to acquire the spin lock again. Between the calls to release and acquire the spin lock, a driver thread must not assume that it has exclusive access to the list of mappings. Accessing the shared data during this unprotected interval is dangerous. If the interval between releasing and acquiring the spin lock is small, the likelihood of the data being corrupted by a race condition between two driver threads is also small. This means that the resulting failures are intermittent and thus difficult to trace. After releasing and acquiring a spin lock, a well-written driver should assume that any temporary pointers or indices that it previously used to access the contents of the shared data structures are no longer valid.

### <span id="IRP_Cancellation"></span><span id="irp_cancellation"></span><span id="IRP_CANCELLATION"></span>IRP Cancellation

At any time during the processing of a playback or capture stream, cancellation of an IRP can cause the operating system to revoke one or more mappings that the miniport driver has acquired. When this occurs, the port driver calls the [**IMiniportWavePciStream::RevokeMappings**](https://msdn.microsoft.com/library/windows/hardware/ff536730) method to notify the miniport driver. In order to avoid either playing data from or capturing data into the revoked mappings, the miniport driver has to remove the mappings from both its software list and the DMA controller's hardware queue. Because the software list and hardware queue are shared between driver threads, some care is required to perform these operations reliably.

For example, a set of mappings to be revoked might contain a mapping that has just been or is just about to be released. In this case, two driver threads might simultaneously attempt to remove the same mapping from the DMA queue. If the driver fails to prevent simultaneous access, the result can be corruption of the data in the registers or memory structures that manage the queue.

For a working code example, see the Ac97 sample driver in the Windows Driver Kit (WDK).

 

 




