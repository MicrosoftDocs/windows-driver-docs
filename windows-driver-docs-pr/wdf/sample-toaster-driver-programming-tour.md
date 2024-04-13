---
title: Sample Toaster Driver Programming Tour
description: This topic provides a code walkthrough of the Toaster sample, which contains Kernel-Mode Driver Framework (KMDF) and User-Mode Driver Framework (UMDF) drivers designed for learning purposes.
ms.date: 03/20/2023
---

# Sample Toaster Driver Programming Tour


This topic provides a code walkthrough of the [Toaster](https://github.com/microsoft/Windows-driver-samples/tree/main/general/toaster) sample, which contains Kernel-Mode Driver Framework (KMDF) and User-Mode Driver Framework (UMDF) drivers designed for learning purposes.

## Applications


The sample includes applications that interact with the toaster bus driver and function driver. These applications work with both KMDF and UMDF toaster versions.

-   Enum.exe is a user-mode enumerator, a simple console application. Because the toaster bus is not a physical bus, you can use this application to cause the bus driver to plug in, unplug, and eject devices from the system. Type Enum.exe for usage tips.
-   Toast.exe: This is a user-mode console application to control the toaster. This application enumerates toaster devices, opens the last enumerated device, and sends a read request to it.
-   Notify.exe: This GUI application combines the functionality of Enum.exe and toast.exe and also shows how to handle PnP notifications in user mode. You can also use Notify.exe to specify a different hardware ID (other than the default toaster device ID) to cause a different driver to be loaded as a function driver.

## KMDF Bus Driver


The KMDF bus driver services the toaster bus controller, enumerates devices that are plugged in, and performs bus-level power management. The bus driver supports D0 and D3 power states. It also has a WMI interface. This directory contains two subdirectories that show two different implementation of the Toaster bus driver.

- **Static**

  The static version of the bus driver shows how to enumerate child devices using a static child list, one per device, provided by the framework.

  *Static enumeration* enables a driver to detect and report the existence of devices during initialization, with a limited ability to report subsequent changes to the system's configuration.

  Bus drivers can use static enumeration if the number and type of devices or functional subunits is predetermined and permanent, and does not depend on the configuration of the system on which the driver is running.

  For example, a sound card's driver might act as a bus driver and create separate physical device objects (PDOs) for each of the card's capabilities, such as MIDI, audio, and joystick.

  To enumerate a child, the bus driver:

  1.  Calls [**WdfPdoInitAllocate**](/windows-hardware/drivers/ddi/wdfpdo/nf-wdfpdo-wdfpdoinitallocate) to obtain a [WDFDEVICE\_INIT](./wdfdevice_init.md) structure.

  2.  Initializes the [WDFDEVICE\_INIT](./wdfdevice_init.md) structure.

  3.  Call [**WdfDeviceCreate**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicecreate) to create a framework device object that represents a PDO.

  After calling [**WdfDeviceCreate**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicecreate), the driver calls [**WdfFdoAddStaticChild**](/windows-hardware/drivers/ddi/wdffdo/nf-wdffdo-wdffdoaddstaticchild) to add the child device to the child list.

  Because drivers should only use static child lists for device configurations that are predetermined and permanent, a driver does not typically modify a static child list after creating it. If the driver determines that a child device has become inaccessible, the driver can call [**WdfPdoMarkMissing**](/windows-hardware/drivers/ddi/wdfpdo/nf-wdfpdo-wdfpdomarkmissing). (If a child device is accessible but unresponsive, the driver should set the **Failed** member of the [**WDF\_DEVICE\_STATE**](/windows-hardware/drivers/ddi/wdfdevice/ns-wdfdevice-_wdf_device_state) structure to **WdfTrue** and then call [**WdfDeviceSetDeviceState**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicesetdevicestate).)

  In order to statically enumerate child devices every time the bus driver starts, configure this value through the Toaster Bus Inf file. The maximum number of child devices that can be enumerated using this registry setting is 10.

  ```inf
  [ToasterStatBus_Device.NT.HW]
  AddReg=ToasterStatBus_Device.NT.AddReg
  
  [ToasterStatBus_Device.NT.AddReg]
  HKR,,NumberOfToasters,0x10001,2
  ```

- **Dynamic**

  The dynamic version of the bus driver shows how to enumerate child devices using child list objects.

  *Dynamic enumeration* enables a driver to detect and report changes to the number and type of devices that are connected to the system while the system is running.

  Bus drivers must use dynamic enumeration if the number or types of devices that are connected to the parent device depend on a system's configuration. Some of these devices might be always connected to the system, and some might be plugged in and unplugged while the system is running.

  For example, the number and type of devices that are plugged into a system's PCI bus are system-dependent, but they are permanent unless a user turns off power, opens the case, and adds or removes a device by using a screwdriver. On the other hand, a user can add or remove USB devices by plugging in or unplugging a cable while the system is running.

  Each time a bus driver identifies a child device, it must add the child device's description to a child list. Driver can either use framework provided device's default child list by calling [**WdfFdoGetDefaultChildList**](/windows-hardware/drivers/ddi/wdffdo/nf-wdffdo-wdffdogetdefaultchildlist), or can create additional child lists, for grouping children, by calling [**WdfChildListCreate**](/windows-hardware/drivers/ddi/wdfchildlist/nf-wdfchildlist-wdfchildlistcreate). This sample uses the default child list. A *child description* consists of a required *identification description* and an optional *address description*.

  <table>
  <colgroup>
  <col width="50%" />
  <col width="50%" />
  </colgroup>
  <thead>
  <tr class="header">
  <th align="left">Term</th>
  <th align="left">Description</th>
  </tr>
  </thead>
  <tbody>
  <tr class="odd">
  <td align="left"><p><a href="" id="---------------------identification-description"></a> Identification Description</p></td>
  <td align="left"><p>An identification description is a structure that contains information that uniquely identifies each device that the driver enumerates. The driver defines this structure, but its first member must be a <a href="/windows-hardware/drivers/ddi/wdfchildlist/ns-wdfchildlist-_wdf_child_identification_description_header" data-raw-source="[&lt;strong&gt;WDF_CHILD_IDENTIFICATION_DESCRIPTION_HEADER&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdfchildlist/ns-wdfchildlist-_wdf_child_identification_description_header)"><strong>WDF_CHILD_IDENTIFICATION_DESCRIPTION_HEADER</strong></a> structure.</p></td>
  </tr>
  <tr class="even">
  <td align="left"><p><a href="" id="---------------------address-description"></a> Address Description</p></td>
  <td align="left"><p>An address description is a structure that contains information that the driver requires so that it can access the device on its bus, if the information can change while the device is plugged in. The driver defines this structure, but its first member must be a <a href="/windows-hardware/drivers/ddi/wdfchildlist/ns-wdfchildlist-_wdf_child_identification_description_header" data-raw-source="[&lt;strong&gt;WDF_CHILD_IDENTIFICATION_DESCRIPTION_HEADER&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdfchildlist/ns-wdfchildlist-_wdf_child_identification_description_header)"><strong>WDF_CHILD_IDENTIFICATION_DESCRIPTION_HEADER</strong></a> structure. Address descriptions are optional. This sample does not use address descriptions.</p></td>
  </tr>
  </tbody>
  </table>




To add children to a child list, the driver calls [**WdfChildListAddOrUpdateChildDescriptionAsPresent**](/windows-hardware/drivers/ddi/wdfchildlist/nf-wdfchildlist-wdfchildlistaddorupdatechilddescriptionaspresent) for each child device that it finds. This call informs the framework that a driver has discovered a child device that is connected to a parent device. When your driver calls **WdfChildListAddOrUpdateChildDescriptionAsPresent**, it supplies an identification description and, optionally, an address description.

After the driver calls [**WdfChildListAddOrUpdateChildDescriptionAsPresent**](/windows-hardware/drivers/ddi/wdfchildlist/nf-wdfchildlist-wdfchildlistaddorupdatechilddescriptionaspresent) to report a new device, the framework informs the PnP manager that the new device exists. The PnP manager then builds a device stack and driver stack for the new device. As part of this process, the framework calls the bus driver's [*EvtChildListCreateDevice*](/windows-hardware/drivers/ddi/wdfchildlist/nc-wdfchildlist-evt_wdf_child_list_create_device) callback function. This callback function must call [**WdfDeviceCreate**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicecreate) to create a PDO for the new device.

To report a child device missing, this driver calls WdfChildListUpdateChildDescriptionAsMissing. For further details on dynamic enumeration, please refer to the framework documentation.


## KMDF Function Driver


The function driver has two different versions: wdfsimple and wdffeatured. The two versions of the function driver share a common header file in the *shared* directory.

-   **WdfSimple**

    In this version, the driver doesn't handle any PnP and Power events, and relies instead on the framework's default support for these events. An application, such as notify.exe, can use this driver to open the device interface registered by the driver and send read, write or IOCTL requests.

-   **WdfFeatured**

    This version shows how to register for PNP and Power events, handle create and close file requests, handle WMI set and query events, and trigger WMI notification events. By being a power policy owner, it also registers for idle notification so it can put the device to low power state when there is no I/O activity.

## KMDF Filter Driver


This directory contains source code for two filter drivers. The Generic sample is a simple passthru filter driver. The SideBand shows how to provide a sideband ioctl interface to an application by using control-device object. This private interface enables application to talk to the filter driver directly; bypassing the functional device stack that filter is attached to. The SideBand sample also demonstrates how to implement a collection of device objects if the driver will handle requests for more than one device. You can install these filters on an existing toaster device by using the filter.inf.

## KMDF Toastmon


This sample demonstrates how to open a device and perform I/O in kernel mode using remote I/O target interfaces. This sample registers a PnP notification callback routine for the toaster interface class by calling [**IoRegisterPlugPlayNotification**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioregisterplugplaynotification). When a toaster device is plugged in, the PnP manager invokes the callback. In the callback, this sample creates a remote target and opens the device by using the symbolic link provided in the callback data.

Also, this sample uses a passive timer to demonstrate asynchronous read and write to the target device. It also shows how to respond to a device change notification by registering [*EvtIoTargetQueryRemove*](/windows-hardware/drivers/ddi/wdfiotarget/nc-wdfiotarget-evt_wdf_io_target_query_remove)/[*EvtIoTargetRemoveCanceled*](/windows-hardware/drivers/ddi/wdfiotarget/nc-wdfiotarget-evt_wdf_io_target_remove_canceled)/[*EvtIoTargetRemoveComplete*](/windows-hardware/drivers/ddi/wdfiotarget/nc-wdfiotarget-evt_wdf_io_target_remove_complete) on the I/O target object. You can use this technique if your driver talks to another device that your driver is not controlling. You install this driver as a root-enumerated device using Wdftoastmon.inf. Use the same steps for installation as the toaster bus driver.

## UMDF Function Driver


The WUDFToaster driver enables a user application (toast/notify.exe) to open the device interface that is registered by the driver and send read, write or IOCTL requests. This driver sample also shows how to register for PnP and Power events, set power policy ownership, and handle I/O requests. This is a minimal driver sample that is not intended for use in a production environment.

You can use the WUDF Toaster in conjunction with the KMDF Toastmon sample to demonstrates kernel-mode client access to a user-mode driver using remote I/O targets.

To do so, add the following line to the .WDF section of the INF for this UMDF driver: **UmdfKernelModeClientPolicy = AllowKernelModeClients**

### Testing UMDF Toaster

1.  Use Toast.exe, Notify.exe or Enum.exe applications.
2.  Install KMDF Toastmon driver. Allow kernel mode clients to user mode drivers as described previously. Install WUDFToaster.dll. Use Traceview.exe to see the requests sent from Toastmon to the UMDF Toaster.

### <a href="" id="umdf-toastmon"></a>UMDF Toastmon Overview

This sample is a UMDF version of the KMDF ToastMon sample.

UMDF Toastmon demonstrates how to use UMDF to write a minimal driver with the User-Mode Driver Framework and shows best practices. The driver will successfully load on a device (either root enumerated or a real hardware device) but has the minimum PnP functionality and does not support receiving any I/O operations.

Toastmon is intended to serve as a learning tool for other UMDF drivers that you may write.
