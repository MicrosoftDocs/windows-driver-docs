---
title: Setting Up and Using Device Queues
author: windows-driver-content
description: Setting Up and Using Device Queues
MS-HAID:
- 'IRPs\_bbdc3d33-9e3e-4619-ba22-c9307ae26cc9.xml'
- 'kernel.setting\_up\_and\_using\_device\_queues'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 5221ffc0-0cb4-498b-9be2-4d240b5f2744
keywords: ["device queues WDK IRPs , setting up", "device queues WDK IRPs , objects", "inserting IRPs in queue", "storing device queue objects", "supplemental IRP queues WDK kernel"]
---

# Setting Up and Using Device Queues


## <a href="" id="ddk-setting-up-and-using-device-queues-kg"></a>


A driver sets up a device queue object by calling [**KeInitializeDeviceQueue**](https://msdn.microsoft.com/library/windows/hardware/ff552126) at driver or device initialization. After starting its device(s), the driver inserts IRPs into this queue by calling [**KeInsertDeviceQueue**](https://msdn.microsoft.com/library/windows/hardware/ff552180) or [**KeInsertByKeyDeviceQueue**](https://msdn.microsoft.com/library/windows/hardware/ff552178). The following figure illustrates these calls.

![diagram illustrating using a device queue object](images/3devqobj.png)

As this figure shows, the driver must provide the storage for a device queue object, which must be resident. Drivers that set up a device queue object usually provide the necessary storage in the [device extension](device-extensions.md) of a driver-created device object, but the storage can be in a controller extension if the driver uses a [controller object](using-controller-objects.md) or in nonpaged pool allocated by the driver.

If the driver provides storage for the device queue object in a device extension, it calls **KeInitializeDeviceQueue** after creating the device object and before starting the device. In other words, the driver can initialize the queue from its [*AddDevice*](https://msdn.microsoft.com/library/windows/hardware/ff540521) routine or when it handles a PnP [**IRP\_MN\_START\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff551749) request. In the call to **KeInitializeDeviceQueue**, the driver passes a pointer to the storage it provides for the device queue object.

After starting its device(s), the driver can insert an IRP into its device queue by calling **KeInsertDeviceQueue**, which places the IRP at the tail of the queue, or **KeInsertByKeyDeviceQueue**, which places the IRP into the queue according to a driver-determined *SortKey* value, as shown in the previous figure.

Each of these support routines returns a Boolean value indicating whether the IRP was inserted into the queue. Each of these calls also sets the state of the device queue object to Busy if the queue is currently empty (Not-Busy). However, if the queue is empty (Not-Busy), neither **KeInsert*Xxx*DeviceQueue** routine inserts the IRP into the queue. Instead, it sets the state of the device queue object to Busy and returns **FALSE**. Because the IRP has not been queued, the driver must pass it on to another driver routine for further processing.

**When setting up supplemental device queues, follow this implementation guideline:**

When a call to **KeInsert*Xxx*DeviceQueue** returns **FALSE**, the caller must pass the IRP it attempted to queue on for further processing to another driver routine.
However, the call to **KeInsert*Xxx*DeviceQueue** changes the state of the device queue object to Busy, so the next IRP to come in is inserted in the queue unless the driver calls **KeRemove*Xxx*DeviceQueue** first.

When the device queue object's state is set to Busy, the driver can dequeue an IRP for further processing or reset the state to Not-Busy by calling one of the following support routines:

-   [**KeRemoveDeviceQueue**](https://msdn.microsoft.com/library/windows/hardware/ff553156) to remove the IRP at the head of the queue

-   [**KeRemoveByKeyDeviceQueue**](https://msdn.microsoft.com/library/windows/hardware/ff553152) to remove an IRP chosen according to a driver-determined *SortKey* value

-   [**KeRemoveEntryDeviceQueue**](https://msdn.microsoft.com/library/windows/hardware/ff553163) to remove a particular IRP in the queue or to determine whether a particular IRP is in the queue

    **KeRemoveEntryDeviceQueue** returns a Boolean indicating whether the IRP was in the device queue.

Calling any of these routines to remove an entry from a device queue that is empty but Busy changes the queue state to Not-Busy.

Each device queue object is protected by a built-in executive spin lock (not shown in the [Using a Device Queue Object](#ddk-setting-up-and-using-device-queues-kg) figure). As a result, a driver can insert IRPs into the queue and remove them in a multiprocessor-safe manner from any driver routine running at less than or equal to IRQL = DISPATCH\_LEVEL. Because of this IRQL restriction, a driver cannot call any **Ke*Xxx*DeviceQueue** routine from its ISR or [*SynchCritSection*](https://msdn.microsoft.com/library/windows/hardware/ff563928) routines, which run at DIRQL.

See [Managing Hardware Priorities](managing-hardware-priorities.md) and [Spin Locks](spin-locks.md) for more information. For IRQL requirements for a specific support routine, see the routine's reference page.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Setting%20Up%20and%20Using%20Device%20Queues%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


