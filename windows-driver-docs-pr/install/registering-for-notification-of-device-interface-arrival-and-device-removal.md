---
title: Register for Notification of Device Interface Arrival and Removal
description: This topic describes how a user-mode application or driver registers for notification of device interface arrival and device removal.
ms.date: 04/20/2017
---

# Registering for Notification of Device Interface Arrival and Device Removal


This topic describes how a user-mode application or driver registers for notification of device interface arrival and device removal.

Typically, a user-mode component calls [**CM_Register_Notification**](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_register_notification) to find a device interface, and then sends I/O requests to the interface. To do so, the component registers for both **CM_NOTIFY_FILTER_TYPE_DEVICEINTERFACE** and **CM_NOTIFY_FILTER_TYPE_DEVICEHANDLE**, for notification of device interface arrivals and device removals respectively. The calling sequence might look like the following.

**Registering for Notification of Device Interface Arrival and Device Removal**

1. Call [**CM_Register_Notification**](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_register_notification) with **CM_NOTIFY_FILTER_TYPE_DEVICEINTERFACE** to register for device interface arrival notifications. When future interfaces in the specified class arrive, the system notifies your component.
2. Because the interface you want to send I/O to might already be present on the system, call [**CM_Get_Device_Interface_List**](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_get_device_interface_lista) or [**SetupDiGetClassDevs**](/windows/win32/api/setupapi/nf-setupapi-setupdigetclassdevsw) to retrieve a list of existing interfaces.
   **Note**  If an interface arrives between step 1 and step 2, the interface is listed twice, from the registration in step 1 and the list of interfaces in step 2.

     

3. Once you find your desired interface, call [**CreateFile**](/windows/win32/api/fileapi/nf-fileapi-createfilea) to open a handle for the device.
4. After successfully creating a device handle in step 3, call [**CM_Register_Notification**](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_register_notification) a second time. This time, register for notifications of type **CM_NOTIFY_FILTER_TYPE_DEVICEHANDLE**, and provide the new device handle as the handle for which to receive notifications. When the device represented by the interface receives a query remove request, the system notifies your component.

5. Use this table as you implement your device handle notification callback.

   <div class="mx-tableFixed">
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
   <td align="left"><p>Call <a href="/windows/win32/api/handleapi/nf-handleapi-closehandle" data-raw-source="[CloseHandle](/windows/win32/api/handleapi/nf-handleapi-closehandle)">CloseHandle</a> to close the device handle. If you do not do this, your open handle prevents the query remove of this device from succeeding.</p></td>
   </tr>
   <tr class="even">
   <td align="left"><strong>CM_NOTIFY_ACTION_DEVICEQUERYREMOVEFAILED</strong></td>
   <td align="left"><p>The query remove failed, so the device and its interface are still valid. To continue sending I/O to the interface, open a new handle to it.</p>
   <p>First, unregister the notifications for your old handle by calling <a href="/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_unregister_notification" data-raw-source="[&lt;strong&gt;CM_Unregister_Notification&lt;/strong&gt;](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_unregister_notification)"><strong>CM_Unregister_Notification</strong></a>. You must do this from a deferred routine because you cannot call <strong>CM_Unregister_Notification</strong> from a notification callback for the notification handle you are unregistering.  See the <strong>Remarks</strong> section of <a href="/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_unregister_notification" data-raw-source="[&lt;strong&gt;CM_Unregister_Notification&lt;/strong&gt;](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_unregister_notification)"><strong>CM_Unregister_Notification</strong></a> for more information.</p>
   <p>Then, either continuing in the deferred routine, or back in your notification callback, call <a href="/windows/win32/api/fileapi/nf-fileapi-createfilea" data-raw-source="[&lt;strong&gt;CreateFile&lt;/strong&gt;](/windows/win32/api/fileapi/nf-fileapi-createfilea)"><strong>CreateFile</strong></a> to create a new handle. Then call <a href="/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_register_notification" data-raw-source="[&lt;strong&gt;CM_Register_Notification&lt;/strong&gt;](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_register_notification)"><strong>CM_Register_Notification</strong></a> with the new handle and <strong>CM_NOTIFY_FILTER_TYPE_DEVICEHANDLE</strong>.</p>
   <p>Note that if you register for notifications on a device that is in the process of being query removed after the <strong>CM_NOTIFY_ACTION_DEVICEQUERYREMOVE</strong> notifications have been sent, you may receive a <strong>CM_NOTIFY_ACTION_DEVICEQUERYREMOVEFAILED</strong> notification without first receiving a <strong>CM_NOTIFY_ACTION_DEVICEQUERYREMOVE</strong> notification.</p></td>
   </tr>
   <tr class="odd">
   <td align="left"><strong>CM_NOTIFY_ACTION_DEVICEREMOVEPENDING</strong></td>
   <td align="left"><p>Call <a href="/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_unregister_notification" data-raw-source="[&lt;strong&gt;CM_Unregister_Notification&lt;/strong&gt;](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_unregister_notification)"><strong>CM_Unregister_Notification</strong></a> to unregister the notifications for your handle. You must do this from a deferred routine.  See the <strong>Remarks</strong> section of <a href="/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_unregister_notification" data-raw-source="[&lt;strong&gt;CM_Unregister_Notification&lt;/strong&gt;](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_unregister_notification)"><strong>CM_Unregister_Notification</strong></a> for more information.  If you still have an open handle to the device, call <a href="/windows/win32/api/handleapi/nf-handleapi-closehandle" data-raw-source="[&lt;strong&gt;CloseHandle&lt;/strong&gt;](/windows/win32/api/handleapi/nf-handleapi-closehandle)"><strong>CloseHandle</strong></a> to close the device handle.</p></td>
   </tr>
   <tr class="even">
   <td align="left"><strong>CM_NOTIFY_ACTION_DEVICEREMOVECOMPLETE</strong></td>
   <td align="left"><p>Call <a href="/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_unregister_notification" data-raw-source="[&lt;strong&gt;CM_Unregister_Notification&lt;/strong&gt;](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_unregister_notification)"><strong>CM_Unregister_Notification</strong></a> to unregister the notifications for your handle. You must do this from a deferred routine.  See the <strong>Remarks</strong> section of <a href="/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_unregister_notification" data-raw-source="[&lt;strong&gt;CM_Unregister_Notification&lt;/strong&gt;](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_unregister_notification)"><strong>CM_Unregister_Notification</strong></a> for more information.  If you still have an open handle to the device, call <a href="/windows/win32/api/handleapi/nf-handleapi-closehandle" data-raw-source="[&lt;strong&gt;CloseHandle&lt;/strong&gt;](/windows/win32/api/handleapi/nf-handleapi-closehandle)"><strong>CloseHandle</strong></a> to close the device handle.</p></td>
   </tr>
   </tbody>
   </table>
   </div>
     

6. Once you are finished with the device, call [**CM_Unregister_Notification**](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_unregister_notification) to unregister the interface notification callback that you registered in step 1.

If you are following this procedure in a UMDF 2 driver, see [Using Device Interfaces](../wdf/using-device-interfaces.md) for a code example. A UMDF 2 driver might perform steps 1-4 in the driver's [*EvtDevicePrepareHardware*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_prepare_hardware) callback routine, and step 6 in one of the driver's device removal callback routines.

## Related topics


[**CM_Register_Notification**](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_register_notification)

[**CM_Unregister_Notification**](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_unregister_notification)

[Using Device Interfaces](../wdf/using-device-interfaces.md)

