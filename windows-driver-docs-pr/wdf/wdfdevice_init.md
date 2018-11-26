---
title: WDFDEVICE_INIT structure
description: The WDFDEVICE_INIT structure is an opaque structure that is defined and allocated by the framework.
ms.assetid: 38a8d316-6d66-4c1a-bb1c-93e2893542e8
keywords:
 - WDFDEVICE_INIT structure
ms.date: 02/23/2018
ms.localizationpriority: medium
---

# WDFDEVICE_INIT structure


\[Applies to KMDF and UMDF\]

The **WDFDEVICE_INIT** structure is an opaque structure that is defined and allocated by the framework.

Syntax
------

```ManagedCPlusPlus
struct WDFDEVICE_INIT {
  ;      // Reserved.
};
```

Members
----------

Function and filter drivers receive a pointer to this structure as input to a [*EvtDriverDeviceAdd*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfdriver/nc-wdfdriver-evt_wdf_driver_device_add) callback function or as a return value from [**WdfControlDeviceInitAllocate**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfcontrol/nf-wdfcontrol-wdfcontroldeviceinitallocate).

Bus drivers receive a structure pointer as input to a [*EvtChildListCreateDevice*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfchildlist/nc-wdfchildlist-evt_wdf_child_list_create_device) callback function or as the return value from [**WdfPdoInitAllocate**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfpdo/nf-wdfpdo-wdfpdoinitallocate).

After a driver receives a **WDFDEVICE_INIT** structure, it passes the structure pointer to initialization functions.
These functions use the **WDFDEVICE_INIT** structure to store information that the framework uses to create a framework device object.

To find documentation for device initialization methods, see [wdfdevice.h header](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfdevice/).

After calling initialization functions, the driver must call [**WdfDeviceCreate**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfdevice/nf-wdfdevice-wdfdevicecreate) to create the framework device object.

If your driver received the **WDFDEVICE_INIT** structure from a call to [**WdfPdoInitAllocate**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfpdo/nf-wdfpdo-wdfpdoinitallocate)
 or [**WdfControlDeviceInitAllocate**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfcontrol/nf-wdfcontrol-wdfcontroldeviceinitallocate),
 and if the driver receives an error from calling an initialization function, the driver must call [**WdfDeviceInitFree**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfdevice/nf-wdfdevice-wdfdeviceinitfree) instead of [**WdfDeviceCreate**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfdevice/nf-wdfdevice-wdfdevicecreate).

Your driver must not call [**WdfDeviceInitFree**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfdevice/nf-wdfdevice-wdfdeviceinitfree) after a successful call to [**WdfDeviceCreate**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfdevice/nf-wdfdevice-wdfdevicecreate).

The **WDFDEVICE_INIT** structure is available in version 1.0 and later versions of KMDF.


Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Header</p></td>
<td>Wdftypes.h (include Wdftypes.h)</td>
</tr>
</tbody>
</table>


