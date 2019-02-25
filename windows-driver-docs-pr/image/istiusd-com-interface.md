---
title: IStiUSD COM Interface
description: IStiUSD COM Interface
ms.assetid: 2f805955-8c66-4c9e-839e-c8a98c6637a8
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# IStiUSD COM Interface





The **IStiUSD** COM interface is the means by which the [IStiDevice COM Interface](istidevice-com-interface.md) communicates with still image devices. The **IStiUSD** interface's methods are implemented by each vendor-supplied [User-Mode Still Image Minidrivers](overview-of-sti-components.md#ddk-user-mode-still-image-minidrivers-si).

Typically, **IStiUSD** interface methods are called by similarly-named methods defined by the **IStiDevice** interface. Still image minidrivers typically implement **IStiUSD** interface methods by calling the appropriate kernel-mode driver. Each minidriver must define all interface methods, but if a method is not needed it can return STIERR\_UNSUPPORTED.

The methods defined by the **IStiUSD** interface include the following:

<a href="" id="istiusd--devicereset"></a>[**IStiUSD::DeviceReset**](https://msdn.microsoft.com/library/windows/hardware/ff543812)  
Resets a still image device to a known, initialized state.

<a href="" id="istiusd--diagnostic"></a>[**IStiUSD::Diagnostic**](https://msdn.microsoft.com/library/windows/hardware/ff543814)  
Runs diagnostic tests on a still image device.

<a href="" id="istiusd--escape"></a>[**IStiUSD::Escape**](https://msdn.microsoft.com/library/windows/hardware/ff543815)  
Performs a vendor-specific I/O operation on a still image device.

<a href="" id="istiusd--getcapabilities"></a>[**IStiUSD::GetCapabilities**](https://msdn.microsoft.com/library/windows/hardware/ff543817)  
Returns a still image device's capabilities.

<a href="" id="istiusd--getlasterrorinfo"></a>[**IStiUSD::GetLastErrorInfo**](https://msdn.microsoft.com/library/windows/hardware/ff543820)  
Returns information about the last known error associated with a still image device.

<a href="" id="istiusd--getnotificationdata"></a>[**IStiUSD::GetNotificationData**](https://msdn.microsoft.com/library/windows/hardware/ff543821)  
Returns a description of the most recent event that occurred on a still image device.

<a href="" id="istiusd--getstatus"></a>[**IStiUSD::GetStatus**](https://msdn.microsoft.com/library/windows/hardware/ff543823)  
Returns the status of a still image device.

<a href="" id="istiusd--initialize"></a>[**IStiUSD::Initialize**](https://msdn.microsoft.com/library/windows/hardware/ff543824)  
Initializes an instance of the COM object that defines the **IStiUSD** interface.

<a href="" id="istiusd--lockdevice"></a>[**IStiUSD::LockDevice**](https://msdn.microsoft.com/library/windows/hardware/ff543829)  
Locks a device for exclusive use by the caller.

<a href="" id="istiusd--rawreadcommand"></a>**IStiUSD::RawReadCommand**  
Reads command information from a still image device.

<a href="" id="istiusd--rawreaddata"></a>[**IStiUSD::RawReadData**](https://msdn.microsoft.com/library/windows/hardware/ff543834)  
Reads data from a still image device.

<a href="" id="istiusd--rawwritecommand"></a>[**IStiUSD::RawWriteCommand**](https://msdn.microsoft.com/library/windows/hardware/ff543836)  
Writes command information to a still image device.

<a href="" id="istiusd--rawwritedata"></a>[**IStiUSD::RawWriteData**](https://msdn.microsoft.com/library/windows/hardware/ff543839)  
Writes data to a still image device.

<a href="" id="istiusd--setnotificationhandle"></a>[**IStiUSD::SetNotificationHandle**](https://msdn.microsoft.com/library/windows/hardware/ff543840)  
Specifies an event handle that the minidriver should use to inform the caller of device events. Typically called by the still image event monitor.

<a href="" id="istiusd--unlockdevice"></a>[**IStiUSD::UnLockDevice**](https://msdn.microsoft.com/library/windows/hardware/ff543843)  
Unlocks a device.

 

 




