---
Description: 'Under certain circumstances, a device driver might need to cancel an idle request IRP that has been submitted to the bus driver.'
MS-HAID:
- 'usbpower\_91a4ce30-9738-4e05-837c-76ef645df02a.xml'
- 'buses.canceling\_a\_usb\_idle\_request'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
title: Canceling a USB Idle Request
---

# Canceling a USB Idle Request


Under certain circumstances, a device driver might need to cancel an idle request IRP that has been submitted to the bus driver. This might occur if the device is removed, becomes active after being idle and sending the idle request, or if the entire system is transitioning to a lower system power state.

The client driver cancels the idle IRP by calling [**IoCancelIrp**](https://msdn.microsoft.com/library/windows/hardware/ff548338). The following table describes three scenarios for canceling an idle IRP and specifies the action the driver must take:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Scenario</th>
<th>Idle Request Cancellation Mechanism</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>The client driver has canceled the idle IRP and the USB driver stack has not called the [USB Idle Notification Callback Routine](usb-idle-notification-callback-routine.md).</td>
<td><p>The USB driver stack completes the idle IRP. Because the device never left the <strong>D0</strong>, the driver does not change the device state.</p></td>
</tr>
<tr class="even">
<td>The client driver has canceled the idle IRP, the USB driver stack has called the USB idle notification callback routine, and it has not yet returned.</td>
<td><p>It is possible that the USB idle notification callback routine is invoked even though the client driver has invoked cancellation on the IRP. In this case, the client driver's callback routine must still power down the device by sending the device to a lower power state synchronously.</p>
<p>When the device is in the lower power state, the client driver can then send a <strong>D0</strong> request.</p>
<p>Alternatively, the driver can wait for the USB driver stack to complete the idle IRP and then send the <strong>D0</strong> IRP.</p>
<p>If the callback routine is unable to put the device into a low power state due to insufficient memory to allocate a power IRP, it should cancel the idle IRP and exit immediately. The idle IRP will not be completed until the callback routine has returned; therefore, the callback routine should not block waiting for the canceled idle IRP to complete.</p></td>
</tr>
<tr class="odd">
<td>The device is already in a low power state.</td>
<td><p>If the device is already in a low power state, the client driver can send a <strong>D0</strong> IRP. The USB driver stack completes the idle request IRP with STATUS_SUCCESS.</p>
<p>Alternatively, the driver can cancel the idle IRP, wait for the USB driver stack to complete the idle IRP, and then send a <strong>D0</strong> IRP.</p></td>
</tr>
</tbody>
</table>

 

## Related topics


[USB Selective Suspend](usb-selective-suspend.md)

[USB Power Management](usb-power-management.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Busbcon\buses%5D:%20Canceling%20a%20USB%20Idle%20Request%20%20RELEASE:%20%281/26/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




