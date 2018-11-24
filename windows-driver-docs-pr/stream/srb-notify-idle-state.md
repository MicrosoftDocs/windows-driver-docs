---
title: SRB\_NOTIFY\_IDLE\_STATE
description: The class driver sends this request to the minidriver immediately before sending the first open request or last close request. The minidriver can use SRB\_NOTIFY\_IDLE\_STATE as a notification to wake from USB Selective Suspend.
ms.assetid: 7a2950a4-bd9f-4765-bb60-9e3aeeff49fb
keywords: ["SRB_NOTIFY_IDLE_STATE Streaming Media Devices"]
topic_type:
- apiref
api_name:
- SRB_NOTIFY_IDLE_STATE
api_type:
- NA
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# SRB\_NOTIFY\_IDLE\_STATE


The class driver sends this request to the minidriver immediately before sending the first open request or last close request. The minidriver can use SRB\_NOTIFY\_IDLE\_STATE as a notification to wake from [USB selective suspend](../usbcon/usb-selective-suspend.md).

### <span id="Return_Value"></span><span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

This request is a notification packet only; any minidriver-supplied return value is ignored.

Remarks
-------

SRB\_NOTIFY\_IDLE\_STATE is sent in Microsoft Windows XP with Service Pack 2 (SP2) and later, but not in Microsoft Windows Server 2003.

SRB\_NOTIFY\_IDLE\_STATE fixes the USB selective suspend problem that exists in the stream class driver (*Stream.sys*) in Windows XP with SP1, described in [Knowledge Base article 813348](http://go.microsoft.com/fwlink/p/?linkid=210855). You can use SRB\_NOTIFY\_IDLE\_STATE to support selective suspend within single instance minidrivers based on [stream class](https://msdn.microsoft.com/library/windows/hardware/ff568277) and [USBCAMD2](https://msdn.microsoft.com/library/windows/hardware/ff568573).

In Windows XP and earlier, SRB\_NOTIFY\_IDLE\_STATE does not exist. For Windows XP and earlier, the minidriver receives [**SRB\_GET\_DEVICE\_PROPERTY**](srb-get-device-property.md) to wake from an idle state. The minidriver then calls [**PoRequestPowerIrp**](https://msdn.microsoft.com/library/windows/hardware/ff559734) to change the device state to D0.

In Windows XP with SP1 and Windows Server 2003, SRB\_GET\_DEVICE\_PROPERTY is not sent in this situation. If you are using *Stream.sys* with these operating systems, follow the instructions in the Knowledge Base article mentioned earlier.

When opening the first instance of the device, the class driver sends SRB\_NOTIFY\_IDLE\_STATE immediately before sending [**SRB\_OPEN\_DEVICE\_INSTANCE**](srb-open-device-instance.md).

When closing the last instance of the device, the class driver sends SRB\_NOTIFY\_IDLE\_STATE immediately before sending the request for the device to transition to state D3.

When the stream class driver sends an SRB\_NOTIFY\_IDLE\_STATE request, the minidriver receives a call to [*StrMiniReceiveDevicePacket*](https://msdn.microsoft.com/library/windows/hardware/ff568463).

## See also


[**SRB\_GET\_DEVICE\_PROPERTY**](srb-get-device-property.md)

[**SRB\_OPEN\_DEVICE\_INSTANCE**](srb-open-device-instance.md)

[*StrMiniReceiveDevicePacket*](https://msdn.microsoft.com/library/windows/hardware/ff568463)

 

 






