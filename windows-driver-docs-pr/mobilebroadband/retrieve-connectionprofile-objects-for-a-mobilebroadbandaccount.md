---
title: Retrieve ConnectionProfile objects for a MobileBroadbandAccount
description: Retrieve ConnectionProfile objects for a MobileBroadbandAccount
ms.assetid: 7e612aa5-1627-4ada-971a-a1d04eafeb81
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Retrieve ConnectionProfile objects for a MobileBroadbandAccount


A [**ConnectionProfile**](https://msdn.microsoft.com/library/windows/apps/br207249) object contains a set of properties and methods that you can use to obtain connectivity, usage, and data plan information for established network connections. The connection profiles associated with a mobile account can be retrieved by using the [**MobileBroadbandAccount**](https://msdn.microsoft.com/library/windows/apps/br207353) object. The following code example illustrates shows how to do this:

**Note**  
A list of all [**ConnectionProfile**](https://msdn.microsoft.com/library/windows/apps/br207249) objects can be retrieved from [**Windows.Networking.Connectivity.NetworkInformation.GetConnectionProfiles**](https://msdn.microsoft.com/library/windows/apps/br207294).

 

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

## <span id="related_topics"></span>Related topics


[Common tasks for mobile broadband Windows Runtime APIs](common-tasks-for-mobile-broadband-windows-runtime-apis.md)

 

 






