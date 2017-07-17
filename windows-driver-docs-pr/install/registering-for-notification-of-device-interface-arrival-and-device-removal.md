---
title: Register for Notification of Device Interface Arrival and Removal
description: This topic describes how a user-mode application or driver registers for notification of device interface arrival and device removal.
ms.assetid: 665E7881-F49C-4FC1-971C-1762B7D0C26E
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

    [!div class="mx-tableFixed"]

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
    <p>Then, either continuing in the deferred routine, or back in your notification callback, call [<strong>CreateFile</strong>](https://msdn.microsoft.com/library/windows/desktop/aa363858) to create a new handle. Then call [<strong>CM_Register_Notification</strong>](https://msdn.microsoft.com/library/windows/hardware/hh780224) with the new handle and <strong>CM_NOTIFY_FILTER_TYPE_DEVICEHANDLE</strong>.</p>
    <p>Note that if you register for notifications on a device that is in the process of being query removed after the <strong>CM_NOTIFY_ACTION_DEVICEQUERYREMOVE</strong> notifications have been sent, you may receive a <strong>CM_NOTIFY_ACTION_DEVICEQUERYREMOVEFAILED</strong> notification without first receiving a <strong>CM_NOTIFY_ACTION_DEVICEQUERYREMOVE</strong> notification.</p></td>
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

 

 






