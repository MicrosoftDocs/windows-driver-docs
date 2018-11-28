---
title: Specifying a Callback Synchronization Mode
description: Specifying a Callback Synchronization Mode
ms.assetid: 3e041493-1095-47cb-b9a7-879a4cf1bd2e
keywords:
- callback synchronization WDK UMDF
- synchronization WDK UMDF
- queue callback functions WDK UMDF
- callback functions WDK UMDF
- I/O queues WDK UMDF
- locking WDK UMDF
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Specifying a Callback Synchronization Mode


[!include[UMDF 1 Deprecation](../umdf-1-deprecation.md)]

The driver can specify how its callback functions are called by the framework. The driver specifies a synchronization (or locking) mode for a device before it calls the [**IWDFDriver::CreateDevice**](https://msdn.microsoft.com/library/windows/hardware/ff558899) method to create a [device object](framework-device-object.md) for the device. To specify synchronization mode, the driver should call the [**IWDFDeviceInitialize::SetLockingConstraint**](https://msdn.microsoft.com/library/windows/hardware/ff556991) method. The driver receives a pointer to the [IWDFDeviceInitialize](https://msdn.microsoft.com/library/windows/hardware/ff556965) interface when its [**IDriverEntry::OnDeviceAdd**](https://msdn.microsoft.com/library/windows/hardware/ff554896) method is called to add the device to the system.

The driver can specify one of the following values from the WDF\_CALLBACK\_CONSTRAINT enumeration type in the *LockType* parameter of **IWDFDeviceInitialize::SetLockingConstraint** to identify the locking mode. The type of constraint (or locking) specified depends on how much parallelism the hardware device can exploit and how much the driver can handle.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Value</th>
<th align="left">Meaning</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><strong>None</strong> (0)</p></td>
<td align="left"><p>Indicates that no callback functions into the driver are synchronized.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>WdfDeviceLevel</strong> (1)</p></td>
<td align="left"><p>Indicates that all queue callback functions into the driver are synchronized.</p></td>
</tr>
</tbody>
</table>

 

**Note**   If the driver does not call **IWDFDeviceInitialize::SetLockingConstraint** to specify a value, the framework sets the default value of this property to **WdfDeviceLevel**.

 

Constraints apply only to queue callback functions and not to Plug and Play (PnP) and power management callback functions. Queue callback functions include the following:

-   Automatic dispatch callback functions, such as, [**IQueueCallbackRead::OnRead**](https://msdn.microsoft.com/library/windows/hardware/ff556875) and [**IQueueCallbackWrite::OnWrite**](https://msdn.microsoft.com/library/windows/hardware/ff556885). For more information, see [I/O Queue Event Callback Functions](i-o-queue-event-callback-functions.md).

-   Queue state change callback functions, such as, [**IQueueCallbackStateChange::OnStateChange**](https://msdn.microsoft.com/library/windows/hardware/ff556880).

-   Request cancellation callback functions, such as, [**IRequestCallbackCancel::OnCancel**](https://msdn.microsoft.com/library/windows/hardware/ff556903).

-   File cleanup and close callback functions, such as, [**IFileCallbackCleanup::OnCleanupFile**](https://msdn.microsoft.com/library/windows/hardware/ff554905) and [**IFileCallbackClose::OnCloseFile**](https://msdn.microsoft.com/library/windows/hardware/ff554910).

Request completion callback functions ([**IRequestCallbackRequestCompletion::OnCompletion**](https://msdn.microsoft.com/library/windows/hardware/ff556905)) are not queue callback functions. Therefore, they are not synchronized.

 

 





