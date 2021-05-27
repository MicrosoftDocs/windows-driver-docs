---
title: UEFI requirements for USB flashing support
description: Microsoft provides several USB-based flashing solutions for use in engineering and manufacturing environments. In order for a device to be used with these tools, the UEFI environment on the device must meet the requirements listed in this topic.
ms.date: 01/28/2019
ms.localizationpriority: medium
---

# UEFI requirements for USB flashing support

Microsoft provides several USB-based flashing solutions for use in engineering and manufacturing environments. In order for a device to be used with these tools, the UEFI environment on the device must meet the requirements listed in this topic.

These requirements related to flashing expand on the UEFI requirements listed in [UEFI requirements that apply to all Windows editions](uefi-requirements-that-apply-to-all-windows-platforms.md) and [UEFI requirements for Windows 10 Mobile](uefi-requirements-specific-to-windows-mobile.md).

## Required UEFI protocols

| Procotol | Requirement details |
| --- | --- |
| USB function protocol | For USB flashing over USB 3.0, the firmware must implement UEFI USB function protocol revision 0x00010002 or higher, including support for the [EFI\_USBFN\_IO\_PROTOCOL.ConfigureEnableEndpointsEx](efi-usbfn-io-protocol-configureenableendpointsex.md) function. For more information, see [UEFI USB function protocol](uefi-usb-function-protocol.md). |
| BlockIO | The Microsoft-provided USB flashing solutions select the first returned pointer to a non-zero sized block I/O storage device for flashing. The device can be non-removable or removable storage.                                                                                                                                                             |
## UEFI desync event (optional)

UEFI components that attempt to read or write to disk during flashing must implement support for the UEFI desync event (EFI\_EVENT\_GROUP\_FIRMWARE\_DESYNC) as described in the following table.

| Requirement | Description |
| --- | --- |
| UEFI boot services support | The UEFI firmware must support the Event, Timer, and Task Priority Services as defined in section 6.1 of the UEFI 2.3.1 Specification. |
| Event group GUID | Microsoft defines the EFI_EVENT_GROUP_FIRMWARE_DESYNC with the following GUID: {24FA5E72-1A82-49A2-970B-3230372662A5} |
| UEFI firmware events | Identify all UEFI firmware components that require refreshing or syncing their state back to storage on a regular basis. In each of these components, create an event associated with the EFI_EVENT_GROUP_FIRMWARE_DESYNC and a NotifyFunction() that causes the component to stop refreshing/syncing back to storage. The event’s NotifyFunction() should perform any cleanup operations necessary for the component to transition to the desynchronized mode. After this cleanup, the component must not refresh or sync its storage back with flash until the next device reboot. If the event’s NotifyFunction fails(), the NotifyFunction() should not return EFI_SUCCESS. |

The following code example demonstrates how firmware could create the Event group GUID event:

```cpp
gBS->CreateEventEx (
    EVT_NOTIFY_SIGNAL,
    TPL_CALLBACK,
    FIRMWARE_NOTIFICATION_FUNCTION,          // To be defined by SoC Vendor
    &FIRMWARE_NOTIFICATION_FUNCTION_CONTEXT, // To be defined by SoC Vendor
    &EFI_EVENT_GROUP_FIRMWARE_DESYNC,
    &Event                                   // Event returned by CreateEventEx
);
```

## Related topics

[Minimum UEFI requirements for Windows on SoC platforms](minimum-uefi-requirements-for-windows-on-soc-platforms.md)  

[UEFI requirements that apply to all Windows editions](uefi-requirements-that-apply-to-all-windows-platforms.md)  

[UEFI requirements for Windows 10 Mobile](uefi-requirements-specific-to-windows-mobile.md)  
