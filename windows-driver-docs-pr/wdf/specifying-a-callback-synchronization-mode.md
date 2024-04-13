---
title: Specifying a Callback Synchronization Mode
description: Specifying a Callback Synchronization Mode
keywords:
- callback synchronization WDK UMDF
- synchronization WDK UMDF
- queue callback functions WDK UMDF
- callback functions WDK UMDF
- I/O queues WDK UMDF
- locking WDK UMDF
ms.date: 04/20/2017
---

# Specifying a Callback Synchronization Mode


[!include[UMDF 1 Deprecation](../includes/umdf-1-deprecation.md)]

The driver can specify how its callback functions are called by the framework. The driver specifies a synchronization (or locking) mode for a device before it calls the [**IWDFDriver::CreateDevice**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfdriver-createdevice) method to create a [device object](framework-device-object.md) for the device. To specify synchronization mode, the driver should call the [**IWDFDeviceInitialize::SetLockingConstraint**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfdeviceinitialize-setlockingconstraint) method. The driver receives a pointer to the [IWDFDeviceInitialize](/windows-hardware/drivers/ddi/wudfddi/nn-wudfddi-iwdfdeviceinitialize) interface when its [**IDriverEntry::OnDeviceAdd**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-idriverentry-ondeviceadd) method is called to add the device to the system.

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

-   Automatic dispatch callback functions, such as, [**IQueueCallbackRead::OnRead**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iqueuecallbackread-onread) and [**IQueueCallbackWrite::OnWrite**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iqueuecallbackwrite-onwrite). For more information, see [I/O Queue Event Callback Functions](i-o-queue-event-callback-functions.md).

-   Queue state change callback functions, such as, [**IQueueCallbackStateChange::OnStateChange**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iqueuecallbackstatechange-onstatechange).

-   Request cancellation callback functions, such as, [**IRequestCallbackCancel::OnCancel**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-irequestcallbackcancel-oncancel).

-   File cleanup and close callback functions, such as, [**IFileCallbackCleanup::OnCleanupFile**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-ifilecallbackcleanup-oncleanupfile) and [**IFileCallbackClose::OnCloseFile**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-ifilecallbackclose-onclosefile).

Request completion callback functions ([**IRequestCallbackRequestCompletion::OnCompletion**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-irequestcallbackrequestcompletion-oncompletion)) are not queue callback functions. Therefore, they are not synchronized.

 

