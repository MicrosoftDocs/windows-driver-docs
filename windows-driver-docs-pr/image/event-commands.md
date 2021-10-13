---
title: Event Commands
description: The commands in this section are used by the microdriver for device event support.
ms.date: 09/27/2021
ms.localizationpriority: medium
---

# Event Commands

The commands in this section are used by the microdriver for device event support.

## CMD_GET_INTERRUPT_EVENT  

Called by the WIA Flatbed Driver in a separate thread to monitor the status of button events that use interrupts from the device (that is, for USB devices that report events via the interrupt pipe). If your device only supports polling, this command does not need to be implemented, and E_NOTIMPL should be returned.

Two event handles are passed to the microdriver. The **lVal** member of the [**VAL**](/windows-hardware/drivers/ddi/wiamicro/ns-wiamicro-val) structure holds an event handle that should be signaled by the microdriver using the **SetEvent** function when a button event occurs. The **handle** member of the VAL structure holds an event handle that will be signaled by the WIA Flatbed Driver when the driver is being unloaded or shut down.

The **pGuid** member of the VAL structure should be set to point to the GUID of the button that was pushed. If no button was pressed, it should be set to GUID_NULL.

## CMD_STI_GETSTATUS  

Called by the WIA Flatbed Driver to get the online status of the device and if the device has push buttons, to get the button status.

Set the **lVal** member of the passed [**VAL**](/windows-hardware/drivers/ddi/wiamicro/ns-wiamicro-val) structure to 1 if your device is online, and functioning properly. If **lVal** is set to any value other than 1, the device is considered offline, and it will fail the device test in Control Panel.

If the device supports buttons that do not use interrupts from the device and a button was pressed, the **pGuid** member of the passed VAL structure should be set to the GUID of the button event. If no buttons were pressed, point **pGuid** to the value GUID_NULL. This signals that there are no events pending.

This command is required if the device supports polled events or you want the device to display on-line status.
