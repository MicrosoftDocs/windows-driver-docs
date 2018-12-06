---
title: Determine if a device is PIN-locked
description: Determine if a device is PIN-locked
ms.assetid: 7889c049-e8a2-4d69-9e5b-4b4756dcf1b4
ms.date: 04/20/2017
ms.localizationpriority: medium
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

 

 






