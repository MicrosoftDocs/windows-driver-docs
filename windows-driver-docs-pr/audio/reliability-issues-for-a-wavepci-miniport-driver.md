---
Description: Reliability Issues for a WavePci Miniport Driver
MS-HAID: 'audio.reliability\_issues\_for\_a\_wavepci\_miniport\_driver'
MSHAttr: 'PreferredLib:/library/windows/hardware'
title: Reliability Issues for a WavePci Miniport Driver
---

# Reliability Issues for a WavePci Miniport Driver


## <span id="reliability_issues_for_a_wavepci_miniport_driver"></span><span id="RELIABILITY_ISSUES_FOR_A_WAVEPCI_MINIPORT_DRIVER"></span>


A WavePci miniport driver must keep track of the mappings that it receives from the port driver. A WavePci miniport driver maintains its list of mappings in a data structure that is shared between driver threads. The driver threads must also share access to the DMA channel in order to add new mappings to the hardware queue and remove completed mappings from the queue. To prevent data corruption, miniport drivers use spin locks to serialize accesses to shared data structures and peripherals. A spin lock protects the shared data and hardware queue from simultaneous access by two or more driver threads.

When developing the portion of the driver that manages mappings, vendors should pay particular attention to the following points.

### <span id="Spin_Locks"></span><span id="spin_locks"></span><span id="SPIN_LOCKS"></span>Spin Locks

To avoid potential deadlocks, the miniport driver must not hold its own spin lock when calling into Portcls.sys to acquire or release mappings. The Ac97 sample driver in the Microsoft Windows Driver Kit (WDK) illustrates this principle. Before calling either [**IPortWavePciStream::GetMapping**](audio.iportwavepcistream_getmapping) or [**IPortWavePciStream::ReleaseMapping**](audio.iportwavepcistream_releasemapping), the sample driver calls [**KeReleaseSpinLock**](kernel.kereleasespinlock) to release the spin lock. After the **GetMapping** or **ReleaseMapping** call returns, the driver calls [**KeAcquireSpinLock**](kernel.keacquirespinlock) to acquire the spin lock again. Between the calls to release and acquire the spin lock, a driver thread must not assume that it has exclusive access to the list of mappings. Accessing the shared data during this unprotected interval is dangerous. If the interval between releasing and acquiring the spin lock is small, the likelihood of the data being corrupted by a race condition between two driver threads is also small. This means that the resulting failures are intermittent and thus difficult to trace. After releasing and acquiring a spin lock, a well-written driver should assume that any temporary pointers or indices that it previously used to access the contents of the shared data structures are no longer valid.

### <span id="IRP_Cancellation"></span><span id="irp_cancellation"></span><span id="IRP_CANCELLATION"></span>IRP Cancellation

At any time during the processing of a playback or capture stream, cancellation of an IRP can cause the operating system to revoke one or more mappings that the miniport driver has acquired. When this occurs, the port driver calls the [**IMiniportWavePciStream::RevokeMappings**](audio.iminiportwavepcistream_revokemappings) method to notify the miniport driver. In order to avoid either playing data from or capturing data into the revoked mappings, the miniport driver has to remove the mappings from both its software list and the DMA controller's hardware queue. Because the software list and hardware queue are shared between driver threads, some care is required to perform these operations reliably.

For example, a set of mappings to be revoked might contain a mapping that has just been or is just about to be released. In this case, two driver threads might simultaneously attempt to remove the same mapping from the DMA queue. If the driver fails to prevent simultaneous access, the result can be corruption of the data in the registers or memory structures that manage the queue.

For a working code example, see the Ac97 sample driver in the Windows Driver Kit (WDK).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20Reliability%20Issues%20for%20a%20WavePci%20Miniport%20Driver%20%20RELEASE:%20%287/14/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")


