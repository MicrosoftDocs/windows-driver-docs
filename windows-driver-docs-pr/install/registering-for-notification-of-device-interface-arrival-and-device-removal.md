---
title: Registering for Notification of Device Interface Arrival and Device Removal
description: This topic describes how a user-mode application or driver registers for notification of device interface arrival and device removal.
ms.assetid: 665E7881-F49C-4FC1-971C-1762B7D0C26E
---

# Registering for Notification of Device Interface Arrival and Device Removal


This topic describes how a user-mode application or driver registers for notification of device interface arrival and device removal.

Typically, a user-mode component calls [**CM\_Register\_Notification**](https://msdn.microsoft.com/library/windows/hardware/hh780224) to find a device interface, and then sends I/O requests to the interface. To do so, the component registers for both **CM\_NOTIFY\_FILTER\_TYPE\_DEVICEINTERFACE** and **CM\_NOTIFY\_FILTER\_TYPE\_DEVICEHANDLE**, for notification of device interface arrivals and device removals respectively. The calling sequence might look like the following.

**Registering for Notification of Device Interface Arrival and Device Removal**

1.  Call [**CM\_Register\_Notification**](https://msdn.microsoft.com/library/windows/hardware/hh780224) with **CM\_NOTIFY\_FILTER\_TYPE\_DEVICEINTERFACE** to register for device interface arrival notifications. When future interfaces in the specified class arrive, the system notifies your component.
2.  Because the interface you want to send I/O to might already be present on the system, call [**CM\_Get\_Device\_Interface\_List**](https://msdn.microsoft.com/library/windows/hardware/ff538463) or [**SetupDiGetClassDevs**](https://msdn.microsoft.com/library/windows/hardware/ff551069) to retrieve a list of existing interfaces.
    **Note**  If an interface arrives between step 1 and step 2, the interface is listed twice, from the registration in step 1 and the list of interfaces in step 2.

     

3.  Once you find your desired interface, call [**CreateFile**](https://msdn.microsoft.com/library/windows/desktop/aa363858) to open a handle for the device.
4.  After successfully creating a device handle in step 3, call [**CM\_Register\_Notification**](https://msdn.microsoft.com/library/windows/hardware/hh780224) a second time. This time, register for notifications of type **CM\_NOTIFY\_FILTER\_TYPE\_DEVICEHANDLE**, and provide the new device handle as the handle for which to receive notifications. When the device represented by the interface receives a query remove request, the system notifies your component.

5.  Use this table as you implement your device handle notification callback.

    <table>
    <colgroup>
    <col width="50%" />
    <col width="50%" />
    </colgroup>
    <thead>
    <tr class="header">
    <th align="left">Action value the callback receives</th>
    <th align="left">What your component should do</th>
    </tr>
    </thead>
    <tbody>
    <tr class="odd">
    <td align="left"><strong>CM_NOTIFY_ACTION_DEVICEQUERYREMOVE</strong></td>
    <td align="left"><p>Call [CloseHandle](http://msdn.microsoft.com/library/windows/desktop/ms724211.aspx) to close the device handle. If you do not do this, your open handle prevents the query remove of this device from succeeding.</p></td>
    </tr>
    <tr class="even">
    <td align="left"><strong>CM_NOTIFY_ACTION_DEVICEQUERYREMOVEFAILED</strong></td>
    <td align="left"><p>The query remove failed, so the device and its interface are still valid. To continue sending I/O to the interface, open a new handle to it.</p>
    <p>First, unregister the notifications for your old handle by calling [<strong>CM_Unregister_Notification</strong>](https://msdn.microsoft.com/library/windows/hardware/hh780228). You must do this from a deferred routine because you cannot call <strong>CM_Unregister_Notification</strong> from a notification callback for the notification handle you are unregistering. You can use methods such as [<strong>TrySubmitThreadpoolCallback</strong>](https://msdn.microsoft.com/library/windows/desktop/ms686862) to defer this processing to another thread.</p>
    <p>Then, either continuing in the deferred routine, or back in your notification callback, call [<strong>CreateFile</strong>](https://msdn.microsoft.com/library/windows/desktop/aa363858) to create a new handle. Then call [<strong>CM_Register_Notification</strong>](https://msdn.microsoft.com/library/windows/hardware/hh780224) with the new handle and <strong>CM_NOTIFY_FILTER_TYPE_DEVICEHANDLE</strong>.</p></td>
    </tr>
    <tr class="odd">
    <td align="left"><strong>CM_NOTIFY_ACTION_DEVICEREMOVEPENDING</strong></td>
    <td align="left"><p>Call [<strong>CM_Unregister_Notification</strong>](https://msdn.microsoft.com/library/windows/hardware/hh780228) to unregister the notifications for your handle. You must do this from a deferred routine. You can use methods such as [<strong>TrySubmitThreadpoolCallback</strong>](https://msdn.microsoft.com/library/windows/desktop/ms686862) to defer this processing to another thread. If you still have an open handle to the device, call [<strong>CloseHandle</strong>](https://msdn.microsoft.com/library/windows/desktop/ms724211) to close the device handle.</p></td>
    </tr>
    <tr class="even">
    <td align="left"><strong>CM_NOTIFY_ACTION_DEVICEREMOVECOMPLETE</strong></td>
    <td align="left"><p>Call [<strong>CM_Unregister_Notification</strong>](https://msdn.microsoft.com/library/windows/hardware/hh780228) to unregister the notifications for your handle. You must do this from a deferred routine. You can use methods such as [<strong>TrySubmitThreadpoolCallback</strong>](https://msdn.microsoft.com/library/windows/desktop/ms686862) to defer this processing to another thread. If you still have an open handle to the device, call [<strong>CloseHandle</strong>](https://msdn.microsoft.com/library/windows/desktop/ms724211) to close the device handle.</p></td>
    </tr>
    </tbody>
    </table>

     

6.  Once you are finished with the device, call [**CM\_Unregister\_Notification**](https://msdn.microsoft.com/library/windows/hardware/hh780228) to unregister the interface notification callback that you registered in step 1.

If you are following this procedure in a UMDF 2 driver, see [Using Device Interfaces](https://msdn.microsoft.com/windows/hardware/drivers/wdf/using-device-interfaces) for a code example. A UMDF 2 driver might perform steps 1-4 in the driver's [*EvtDevicePrepareHardware*](https://msdn.microsoft.com/library/windows/hardware/ff540880) callback routine, and step 6 in one of the driver's device removal callback routines.

## Related topics


[**CM\_Register\_Notification**](https://msdn.microsoft.com/library/windows/hardware/hh780224)

[**CM\_Unregister\_Notification**](https://msdn.microsoft.com/library/windows/hardware/hh780228)

[Using Device Interfaces](https://msdn.microsoft.com/library/windows/hardware/ff545432)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Registering%20for%20Notification%20of%20Device%20Interface%20Arrival%20and%20Device%20Removal%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





