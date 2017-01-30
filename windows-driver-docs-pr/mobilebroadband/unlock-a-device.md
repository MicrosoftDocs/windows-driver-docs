---
title: Unlock a device
description: Unlock a device
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 4e6ed725-2384-429b-be1e-027b7784e95b
---

# Unlock a device


A subset of the mobile broadband API includes the PIN Management API. To unlock a device, do the following:

1.  Get the network adapter ID for the account device:

    ``` syntax
    account.currentNetwork.networkAdapter. networkAdapterId
    ```

2.  Create an [**IMbnInterfaceManager**](https://msdn.microsoft.com/library/windows/desktop/dd430416) instance.

3.  Advise to the [**IMbnPinManagerEvents**](https://msdn.microsoft.com/library/windows/desktop/dd323118) and [**IMbnPinEvents**](https://msdn.microsoft.com/library/windows/desktop/dd323110) connection points (these are used for getting PIN state and unblock/unlock results).

4.  Pass the network adapter ID into [**IMbnInterfaceManager::GetInterface**](https://msdn.microsoft.com/library/windows/desktop/dd430420) to get an [**IMbnInterface**](https://msdn.microsoft.com/library/windows/desktop/dd430406) interface for the device.

5.  Get an [**IMbnPinManager**](https://msdn.microsoft.com/library/windows/desktop/dd323117) interface for the device by calling [**IMbnInterface::QueryInterface**](https://msdn.microsoft.com/library/windows/desktop/dd430406).

6.  Call [**IMbnPinManager::GetPinState**](https://msdn.microsoft.com/library/windows/desktop/dd323123) to get the PIN state of the device (the state returned by using the connection point that was registered in step 3).

7.  Determine how the device is locked or blocked by using the [**MBN\_PIN\_INFO::pinState**](https://msdn.microsoft.com/library/windows/desktop/dd323226) parameter that is passed into the event.

8.  Get an IMbnPin interface for the appropriate PIN by calling [**IMbnPinManager::GetPin**](https://msdn.microsoft.com/library/windows/desktop/dd323121).

9.  Call either [**IMbnPin::Enter**](https://msdn.microsoft.com/library/windows/desktop/dd323127) or [**IMbnPin::Unblock**](https://msdn.microsoft.com/library/windows/desktop/dd323134), based on how the device is locked (see step 7).

10. Listen for **Unlock** or **Unblock** results by using [**IMbnPinEvents**](https://msdn.microsoft.com/library/windows/desktop/dd323110) registration to know whether the operation was successful.

## <span id="related_topics"></span>Related topics


[Common tasks for mobile broadband Windows Runtime APIs](common-tasks-for-mobile-broadband-windows-runtime-apis.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_mb\p_mb%5D:%20Unlock%20a%20device%20%20RELEASE:%20%281/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





