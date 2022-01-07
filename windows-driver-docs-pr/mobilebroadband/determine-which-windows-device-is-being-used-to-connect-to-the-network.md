---
title: Determine which Windows device is connecting to the network
description: Determine which Windows device is being used to connect to the network
ms.date: 04/20/2017
---

# Determine which Windows device is being used to connect to the network

To determine which Windows device is being used to connect to the network, check the Windows device ID for the network adapter, which is exposed by the [**DeviceId**](/uwp/api/Windows.Networking.NetworkOperators.MobileBroadbandDeviceInformation#Windows_Networking_NetworkOperators_MobileBroadbandDeviceInformation_DeviceId) property of the current network device object for the account.

For example:

``` syntax
account.currentDeviceInformation.deviceId
```

## <span id="related_topics"></span>Related topics


[Common tasks for mobile broadband Windows Runtime APIs](./create-a-mobilebroadbandaccount-object.md)

 

