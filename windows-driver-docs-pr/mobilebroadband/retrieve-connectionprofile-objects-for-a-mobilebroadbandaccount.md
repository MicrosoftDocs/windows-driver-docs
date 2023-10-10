---
title: Retrieve ConnectionProfile objects for a MobileBroadbandAccount
description: Retrieve ConnectionProfile objects for a MobileBroadbandAccount
ms.date: 04/20/2017
---

# Retrieve ConnectionProfile objects for a MobileBroadbandAccount


A [**ConnectionProfile**](/uwp/api/Windows.Networking.Connectivity.ConnectionProfile) object contains a set of properties and methods that you can use to obtain connectivity, usage, and data plan information for established network connections. The connection profiles associated with a mobile account can be retrieved by using the [**MobileBroadbandAccount**](/uwp/api/Windows.Networking.NetworkOperators.MobileBroadbandAccount) object. The following code example illustrates shows how to do this:

**Note**  
A list of all [**ConnectionProfile**](/uwp/api/Windows.Networking.Connectivity.ConnectionProfile) objects can be retrieved from [**Windows.Networking.Connectivity.NetworkInformation.GetConnectionProfiles**](/uwp/api/Windows.Networking.Connectivity.NetworkInformation#Windows_Networking_Connectivity_NetworkInformation_GetConnectionProfiles).

 

``` syntax
var myConnectionProfileList = myNetworkAccountObject.getConnectionProfiles();

if (myConnectionProfileList.length !== 0)
{
  for (var i = 0; i < myConnectionProfileList.length; i++)
  {
    //Display connection profile properties
    var connectivityLevel = myConnectionProfileList[i].getNetworkConnectivityLevel();
    }
  }
else 
{
  // No connection profiles are associated with this mobile broadband account.
}
```

## Related topics


[Common tasks for mobile broadband Windows Runtime APIs](./create-a-mobilebroadbandaccount-object.md)

 

