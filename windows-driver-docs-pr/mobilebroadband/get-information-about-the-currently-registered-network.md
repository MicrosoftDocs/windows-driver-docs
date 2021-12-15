---
title: Get information about the currently registered network
description: Get information about the currently registered network
ms.date: 04/20/2017
---

# Get information about the currently registered network


You can get the data class, service provider ID and name of the network that the mobile broadband device is currently registered to. To do this, use the [**RegisteredDataClass**](/uwp/api/Windows.Networking.NetworkOperators.MobileBroadbandNetwork#Windows_Networking_NetworkOperators_MobileBroadbandNetwork_RegisteredDataClass), [**RegisteredProviderId**](/uwp/api/Windows.Networking.NetworkOperators.MobileBroadbandNetwork#Windows_Networking_NetworkOperators_MobileBroadbandNetwork_RegisteredProviderId), and [**RegisteredProviderName**](/uwp/api/Windows.Networking.NetworkOperators.MobileBroadbandNetwork#Windows_Networking_NetworkOperators_MobileBroadbandNetwork_RegisteredProviderName) properties of the current network object for the account.

For example:

``` syntax
var myNetwork = myNetworkAccountObject.currentNetwork
if (myNetwork != null && myNetwork.registeredDataClass == DataClasses.LteAdvanced)
{
  // user is connected to an LTE network
}
```

## <span id="related_topics"></span>Related topics


[Common tasks for mobile broadband Windows Runtime APIs](./create-a-mobilebroadbandaccount-object.md)

 

