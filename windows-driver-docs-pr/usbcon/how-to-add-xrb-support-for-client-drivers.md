---
title: Allocating and Building URBs
description: This article describes how a USB client driver can use Windows Driver Model (WDM) driver routines to allocate and format an URB before sending the request to the Microsoft-provided USB driver stack.
ms.date: 01/24/2023
---

# Allocating and Building URBs

A USB client driver can use Windows Driver Model (WDM) driver routines to allocate and format an URB before sending the request to the Microsoft-provided USB driver stack.

The client driver uses an URB to package all information required by the lower drivers in the USB driver stack to process the request. In the Windows operating system, an URB is described in a **[URB](/windows-hardware/drivers/ddi/usb/ns-usb-_urb)** structure.

Microsoft provides a library of [Routines for USB Client Drivers](/windows-hardware/drivers/ddi/_usbref/#client). By using those routines, USB client drivers can build URB requests for certain specified operations and forward them down the USB stack. If you prefer, you can design your client driver to call the library routines for the supported operations rather than building your own URB requests.

## URB Allocation in Windows 7 and Earlier

To send a USB request by using routines included in Windows Driver Kit (WDK) for Windows 7 and earlier versions of Windows, a client driver typically allocates and fills a **[URB](/windows-hardware/drivers/ddi/usb/ns-usb-_urb)** structure, associates the **URB** structure with a new IRP, and sends the IRP to the USB driver stack.

For certain types of requests, Microsoft provides helper routines (exported by Usbd.sys) that allocate and format the **[URB](/windows-hardware/drivers/ddi/usb/ns-usb-_urb)** structure. For example, the **[USBD\_CreateConfigurationRequestEx](/windows-hardware/drivers/ddi/usbdlib/nf-usbdlib-usbd_createconfigurationrequestex)** routine allocates memory for an **URB** structure, formats the URB for a select-configuration request, and returns the address of the **URB** structure to the client driver. However, the helper routines cannot be used for all types of requests.

Microsoft also provides macros that format URBs for some types of requests. For those macros, the client driver must allocate the **[URB](/windows-hardware/drivers/ddi/usb/ns-usb-_urb)** structure by calling **[ExAllocatePoolWithTag](/windows-hardware/drivers/ddi/wdm/nf-wdm-exallocatepoolwithtag)** or allocate the structure on the stack. For example, after the client driver allocates an **URB**, the driver can call **[UsbBuildSelectConfigurationRequest](/previous-versions/ff538968(v=vs.85))** to format the URB for a select-configuration request or to clear the configuration.

For other requests the client driver must allocate and format the URB manually by setting various members of the **[URB](/windows-hardware/drivers/ddi/usb/ns-usb-_urb)** structure, depending on the request type.

When a USB request is complete, the client driver must release the **[URB](/windows-hardware/drivers/ddi/usb/ns-usb-_urb)** structure. If the URB is allocated on the stack, the URB is released when it goes out of scope. If the URB is allocated in non-paged pool, the client driver must call **[ExFreePool](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-exfreepool)** to release the URB.

## URB Allocation in Windows 8

WDK for Windows 8 provides a new static library, Usbdex.lib, that exports routines for allocating, formatting, and releasing URBs. In addition, there is a new way of associating an URB with an IRP. The new routines can be called by a client driver targeting Windows Vista and later versions of Windows.

A client driver running on Windows Vista and later must use the new routines so that the underlying USB driver stack can utilize certain performance and reliability improvements. Those improvements apply to the new USB driver stack introduced in Windows 8 to support USB 3.0 devices and host controllers. For USB 2.0 host controllers, Windows loads an earlier version of the driver stack that does not support the improvements. Regardless of the version of the underlying driver stack or the protocol version supported by the host controller, you must always call the new URB routines.

Before you call any of the new routines, make sure that you have a USBD handle for your client driver registration with the USB driver stack. To obtain a USBD handle, call **[USBD\_CreateHandle](/windows-hardware/drivers/ddi/usbdlib/nf-usbdlib-usbd_createhandle)**.

The following routines are available with the WDK for Windows 8. These routines are defined in Usbdlib.h.

- **[USBD\_UrbAllocate](/windows-hardware/drivers/ddi/usbdlib/nf-usbdlib-usbd_urballocate)**
- **[USBD\_IsochUrbAllocate](/windows-hardware/drivers/ddi/usbdlib/nf-usbdlib-usbd_isochurballocate)**
- **[USBD\_SelectConfigUrbAllocateAndBuild](/windows-hardware/drivers/ddi/usbdlib/nf-usbdlib-usbd_selectconfigurballocateandbuild)**
- **[USBD\_SelectInterfaceUrbAllocateAndBuild](/windows-hardware/drivers/ddi/usbdlib/nf-usbdlib-usbd_selectinterfaceurballocateandbuild)**
- **[USBD\_UrbFree](/windows-hardware/drivers/ddi/usbdlib/nf-usbdlib-usbd_urbfree)**
- **[USBD\_AssignUrbToIoStackLocation](/windows-hardware/drivers/ddi/usbdlib/nf-usbdlib-usbd_assignurbtoiostacklocation)**

The allocation routines in the preceding list return a pointer to a new **[URB](/windows-hardware/drivers/ddi/usb/ns-usb-_urb)** structure, which is allocated by the USB driver stack. Depending on the version of the USB driver stack loaded by Windows, the **URB** structure can be paired with an opaque *URB context*. An URB context is a block of information about the URB. You cannot view the contents of the URB header; the information is intended to be used internally by the USB driver stack to improve URB tracking and processing. The URB context is *only* used by the USB driver stack for Windows 8.
If URB context is available, the USB driver stack uses it to make URB processing safer and more efficient. For example, the USB driver stack must make sure that the client driver does not submit an URB and then attempt to reuse that same URB before the first request has completed. To detect that kind of error, the USB driver stack stores state information in the URB context. Without the state information, the USB driver stack would have to compare the incoming URB with all URBs currently in progress. The state information is also used by the USB driver stack when the client driver attempts to release the URB. Before releasing the URB, the USB driver stack verifies the state to make sure that the URB is not pending.

URB context provides an official mechanism for storing extra URB information. Using URB context is preferable to allocating extra memory as needed or storing extra information in reserved members of the **[URB](/windows-hardware/drivers/ddi/usb/ns-usb-_urb)** structure. The USB driver stack allocates URBs and their associated URB context in non-paged pool, so that in the future if larger URB context are needed, the only required adjustment will be the size of a pool allocation.

## URB Routine Migration

The following table summarizes the changes in URB routines.

| Use case | Available in WDK for Windows 7 and earlier | Available in WDK for Windows 8 and later |
|---|---|---|
| &nbsp; | Targets Windows 7 and earlier versions of the operating system | Targets Windows 8 and later versions of the operating system |
| To create an URB... | The client driver allocates a **[URB](/windows-hardware/drivers/ddi/usb/ns-usb-_urb)** structure and formats the structure depending on the request.<br/><br/>The client driver allocates the URB structure on the stack, or the driver allocates the structure in non-paged pool by calling **[ExAllocatePoolWithTag](/windows-hardware/drivers/ddi/wdm/nf-wdm-exallocatepoolwithtag)**. | The client driver calls **[USBD_UrbAllocate](/windows-hardware/drivers/ddi/usbdlib/nf-usbdlib-usbd_urballocate)** and receives a pointer to the new **[URB](/windows-hardware/drivers/ddi/usb/ns-usb-_urb)** structure, which is allocated by the USB driver stack. The URB might be associated with an URB context, depending on the USBD interface version of the underlying USB driver stack. |
| To create an URB for a select-configuration request... | The client driver calls the **[USBD_CreateConfigurationRequestEx](/windows-hardware/drivers/ddi/usbdlib/nf-usbdlib-usbd_createconfigurationrequestex)** routine that returns a pointer to the new URB that is created and formatted by the USB driver stack. | The client driver calls **[USBD_SelectConfigUrbAllocateAndBuild](/windows-hardware/drivers/ddi/usbdlib/nf-usbdlib-usbd_selectconfigurballocateandbuild)** and receives a pointer to the new **[URB](/windows-hardware/drivers/ddi/usb/ns-usb-_urb)** structure, which is allocated and formatted (for the select-configuration request) by the USB driver stack. The URB might be associated with an URB context, depending on the USBD interface version of the underlying USB driver stack. |
| To create a URB for an select-interface request... | The client driver allocates a **[URB](/windows-hardware/drivers/ddi/usb/ns-usb-_urb)** structure and uses the **[_URB_SELECT_INTERFACE](/windows-hardware/drivers/ddi/usb/ns-usb-_urb_select_interface)** structure to define the format of a select interface command for a USB device. | The client driver calls **[USBD_SelectInterfaceUrbAllocateAndBuild](/windows-hardware/drivers/ddi/usbdlib/nf-usbdlib-usbd_selectinterfaceurballocateandbuild)** and receives a pointer to the new **[URB](/windows-hardware/drivers/ddi/usb/ns-usb-_urb)** structure, which is allocated and formatted (for the select-interface request) by the USB driver stack. The URB might be associated with an URB context, depending on the USBD interface version of the underlying USB driver stack. |
| To associate an URB with an IRP... | The client driver gets a pointer to the next IRP stack location by calling **[IoGetNextIrpStackLocation](/windows-hardware/drivers/ddi/wdm/nf-wdm-iogetnextirpstacklocation)**. Then the client driver manually sets the Parameters.Others.Argument1 member of the stack location to the address of the **[URB](/windows-hardware/drivers/ddi/usb/ns-usb-_urb)** structure. | The client driver gets a pointer to the next IRP stack location by calling **[IoGetNextIrpStackLocation](/windows-hardware/drivers/ddi/wdm/nf-wdm-iogetnextirpstacklocation)**. Then the client driver calls **[USBD_AssignUrbToIoStackLocation](/windows-hardware/drivers/ddi/usbdlib/nf-usbdlib-usbd_assignurbtoiostacklocation)** to associate a the URB with the stack location. |
| To release an URB... | If the client driver allocates a URB on the stack, the variable goes out of scope after the request is complete.<br/><br/>To free a URB structure that the client driver or the USB driver stack allocated in non-paged pool, the client driver calls **[ExFreePool](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-exfreepool)**. | The client driver calls **[USBD_UrbFree](/windows-hardware/drivers/ddi/usbdlib/nf-usbdlib-usbd_urbfree)**. |

## Related topics

- [Sending Requests to a USB Device](communicating-with-a-usb-device.md)
