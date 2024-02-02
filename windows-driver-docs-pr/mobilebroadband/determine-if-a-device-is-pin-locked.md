---
title: Determine if a Device is PIN-locked
description: Determine if a device is PIN-locked
ms.date: 04/20/2017
---

# Determine if a device is PIN-locked


Because the subscription information on a locked device (for example, ICCID or IMEI) might not be available, all locked devices enumerate an available network account. To know whether an account represents a locked device, query the [**NetworkDeviceStatus**](/uwp/api/Windows.Networking.NetworkOperators.MobileBroadbandDeviceInformation#Windows_Networking_NetworkOperators_MobileBroadbandDeviceInformation_NetworkDeviceStatus) property of the [**CurrentDeviceInformation**](/uwp/api/Windows.Networking.NetworkOperators.MobileBroadbandAccount#Windows_Networking_NetworkOperators_MobileBroadbandAccount_CurrentDeviceInformation) property for the account. [**NetworkDeviceStatus**](/uwp/api/Windows.Networking.NetworkOperators.NetworkDeviceStatus).**DeviceLocked** indicates a PIN lock, whereas **NetworkDeviceStatus**.**DeviceBlocked** indicates a PUK block.

For example:

``` syntax
var account = Windows.Networking.NetworkOperators.MobileBroadbandAccount.createFromNetworkAccountId(accountId);
if (account.currentDeviceInformation.networkDeviceStatus == Windows.Networking.NetworkOperators.NetworkDeviceStatus.DeviceLocked)
{
  // the pin is locked
}
```

## <span id="related_topics"></span>Related topics


[Common tasks for mobile broadband Windows Runtime APIs](./create-a-mobilebroadbandaccount-object.md)

 

