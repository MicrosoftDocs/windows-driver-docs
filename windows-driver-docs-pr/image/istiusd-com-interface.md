---
title: IStiUSD COM Interface
description: IStiUSD COM Interface
ms.date: 04/20/2017
---

# IStiUSD COM Interface





The **IStiUSD** COM interface is the means by which the [IStiDevice COM Interface](istidevice-com-interface.md) communicates with still image devices. The **IStiUSD** interface's methods are implemented by each vendor-supplied [User-Mode Still Image Minidrivers](overview-of-sti-components.md#ddk-user-mode-still-image-minidrivers-si).

Typically, **IStiUSD** interface methods are called by similarly-named methods defined by the **IStiDevice** interface. Still image minidrivers typically implement **IStiUSD** interface methods by calling the appropriate kernel-mode driver. Each minidriver must define all interface methods, but if a method is not needed it can return STIERR\_UNSUPPORTED.

The methods defined by the **IStiUSD** interface include the following:

<a href="" id="istiusd--devicereset"></a>[**IStiUSD::DeviceReset**](/windows-hardware/drivers/ddi/stiusd/nf-stiusd-istiusd-devicereset)  
Resets a still image device to a known, initialized state.

<a href="" id="istiusd--diagnostic"></a>[**IStiUSD::Diagnostic**](/windows-hardware/drivers/ddi/stiusd/nf-stiusd-istiusd-diagnostic)  
Runs diagnostic tests on a still image device.

<a href="" id="istiusd--escape"></a>[**IStiUSD::Escape**](/windows-hardware/drivers/ddi/stiusd/nf-stiusd-istiusd-escape)  
Performs a vendor-specific I/O operation on a still image device.

<a href="" id="istiusd--getcapabilities"></a>[**IStiUSD::GetCapabilities**](/windows-hardware/drivers/ddi/stiusd/nf-stiusd-istiusd-getcapabilities)  
Returns a still image device's capabilities.

<a href="" id="istiusd--getlasterrorinfo"></a>[**IStiUSD::GetLastErrorInfo**](/windows-hardware/drivers/ddi/stiusd/nf-stiusd-istiusd-getlasterrorinfo)  
Returns information about the last known error associated with a still image device.

<a href="" id="istiusd--getnotificationdata"></a>[**IStiUSD::GetNotificationData**](/windows-hardware/drivers/ddi/stiusd/nf-stiusd-istiusd-getnotificationdata)  
Returns a description of the most recent event that occurred on a still image device.

<a href="" id="istiusd--getstatus"></a>[**IStiUSD::GetStatus**](/windows-hardware/drivers/ddi/stiusd/nf-stiusd-istiusd-getstatus)  
Returns the status of a still image device.

<a href="" id="istiusd--initialize"></a>[**IStiUSD::Initialize**](/windows-hardware/drivers/ddi/stiusd/nf-stiusd-istiusd-initialize)  
Initializes an instance of the COM object that defines the **IStiUSD** interface.

<a href="" id="istiusd--lockdevice"></a>[**IStiUSD::LockDevice**](/windows-hardware/drivers/ddi/stiusd/nf-stiusd-istiusd-lockdevice)  
Locks a device for exclusive use by the caller.

<a href="" id="istiusd--rawreadcommand"></a>**IStiUSD::RawReadCommand**  
Reads command information from a still image device.

<a href="" id="istiusd--rawreaddata"></a>[**IStiUSD::RawReadData**](/windows-hardware/drivers/ddi/stiusd/nf-stiusd-istiusd-rawreaddata)  
Reads data from a still image device.

<a href="" id="istiusd--rawwritecommand"></a>[**IStiUSD::RawWriteCommand**](/windows-hardware/drivers/ddi/stiusd/nf-stiusd-istiusd-rawwritecommand)  
Writes command information to a still image device.

<a href="" id="istiusd--rawwritedata"></a>[**IStiUSD::RawWriteData**](/windows-hardware/drivers/ddi/stiusd/nf-stiusd-istiusd-rawwritedata)  
Writes data to a still image device.

<a href="" id="istiusd--setnotificationhandle"></a>[**IStiUSD::SetNotificationHandle**](/windows-hardware/drivers/ddi/stiusd/nf-stiusd-istiusd-setnotificationhandle)  
Specifies an event handle that the minidriver should use to inform the caller of device events. Typically called by the still image event monitor.

<a href="" id="istiusd--unlockdevice"></a>[**IStiUSD::UnLockDevice**](/windows-hardware/drivers/ddi/stiusd/nf-stiusd-istiusd-unlockdevice)  
Unlocks a device.

 

