---
title: Event Commands
description: Event Commands
ms.assetid: e2b9f985-be57-49a9-b546-5cc74b0b061b
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Event Commands


## <span id="ddk_event_commands_si"></span><span id="DDK_EVENT_COMMANDS_SI"></span>


The commands in this section are used by the microdriver for device event support.

<span id="CMD_GET_INTERRUPT_EVENT"></span><span id="cmd_get_interrupt_event"></span>CMD\_GET\_INTERRUPT\_EVENT  
Called by the WIA Flatbed Driver in a separate thread to monitor the status of button events that use interrupts from the device (that is, for USB devices that report events via the interrupt pipe). If your device only supports polling, this command does not need to be implemented, and E\_NOTIMPL should be returned.

Two event handles are passed to the microdriver. The **lVal** member of the [**VAL**](https://msdn.microsoft.com/library/windows/hardware/ff548627) structure holds an event handle that should be signaled by the microdriver using the **SetEvent** function when a button event occurs. The **handle** member of the VAL structure holds an event handle that will be signaled by the WIA Flatbed Driver when the driver is being unloaded or shut down.

The **pGuid** member of the VAL structure should be set to point to the GUID of the button that was pushed. If no button was pressed, it should be set to GUID\_NULL.

<span id="CMD_STI_GETSTATUS"></span><span id="cmd_sti_getstatus"></span>CMD\_STI\_GETSTATUS  
Called by the WIA Flatbed Driver to get the online status of the device and if the device has push buttons, to get the button status.

Set the **lVal** member of the passed [**VAL**](https://msdn.microsoft.com/library/windows/hardware/ff548627) structure to 1 if your device is online, and functioning properly. If **lVal** is set to any value other than 1, the device is considered offline, and it will fail the device test in Control Panel.

If the device supports buttons that do not use interrupts from the device and a button was pressed, the **pGuid** member of the passed VAL structure should be set to the GUID of the button event. If no buttons were pressed, point **pGuid** to the value GUID\_NULL. This signals that there are no events pending.

This command is required if the device supports polled events or you want the device to display on-line status.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Event%20Commands%20%20RELEASE:%20%2811/13/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




