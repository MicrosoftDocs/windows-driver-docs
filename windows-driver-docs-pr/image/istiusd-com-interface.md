---
title: IStiUSD COM Interface
author: windows-driver-content
description: IStiUSD COM Interface
MS-HAID:
- 'stillimg\_57617ce0-9992-43e6-ac7f-73caa456c318.xml'
- 'image.istiusd\_com\_interface'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 2f805955-8c66-4c9e-839e-c8a98c6637a8
---

# IStiUSD COM Interface


## <a href="" id="ddk-istiusd-com-interface-si"></a>


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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20IStiUSD%20COM%20Interface%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


