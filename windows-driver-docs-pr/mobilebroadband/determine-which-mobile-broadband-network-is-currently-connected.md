---
title: Determine which mobile broadband network is currently connected
description: Determine which mobile broadband network is currently connected
ms.date: 04/20/2017
---

# Determine which mobile broadband network is currently connected


You can determine which mobile broadband network you’re connected to by retrieving the APN through the [**AccessPointName**](/uwp/api/Windows.Networking.NetworkOperators.MobileBroadbandNetwork#Windows_Networking_NetworkOperators_MobileBroadbandNetwork_AccessPointName) property of the current network object for the account.

For example:

``` syntax
account.currentNetwork.accessPointName
```

## <span id="related_topics"></span>Related topics


[Common tasks for mobile broadband Windows Runtime APIs](./create-a-mobilebroadbandaccount-object.md)

 

