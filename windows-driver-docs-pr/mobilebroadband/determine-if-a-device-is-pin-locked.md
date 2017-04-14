---
title: Determine if a device is PIN-locked
description: Determine if a device is PIN-locked
ms.assetid: 7889c049-e8a2-4d69-9e5b-4b4756dcf1b4
---

# Determine if a device is PIN-locked


Because the subscription information on a locked device (for example, ICCID or IMEI) might not be available, all locked devices enumerate an available network account. To know whether an account represents a locked device, query the [**NetworkDeviceStatus**](https://msdn.microsoft.com/library/windows/apps/br207369) property of the [**CurrentDeviceInformation**](https://msdn.microsoft.com/library/windows/apps/hh770609) property for the account. [**NetworkDeviceStatus**](https://msdn.microsoft.com/library/windows/apps/br207375).**DeviceLocked** indicates a PIN lock, whereas **NetworkDeviceStatus**.**DeviceBlocked** indicates a PUK block.

For example:

``` syntax
var account = Windows.Networking.NetworkOperators.MobileBroadbandAccount.createFromNetworkAccountId(accountId);
if (account.currentDeviceInformation.networkDeviceStatus == Windows.Networking.NetworkOperators.NetworkDeviceStatus.DeviceLocked)
{
  // the pin is locked
}
```

## <span id="related_topics"></span>Related topics


[Common tasks for mobile broadband Windows Runtime APIs](common-tasks-for-mobile-broadband-windows-runtime-apis.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_mb\p_mb%5D:%20Determine%20if%20a%20device%20is%20PIN-locked%20%20RELEASE:%20%281/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





