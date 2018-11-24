---
title: Get information about the currently registered network
description: Get information about the currently registered network
ms.assetid: 94321933-fc93-4203-8de1-e715d66fd1e3
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Get information about the currently registered network


You can get the data class, service provider ID and name of the network that the mobile broadband device is currently registered to. To do this, use the [**RegisteredDataClass**](https://msdn.microsoft.com/library/windows/apps/hh967833), [**RegisteredProviderId**](https://msdn.microsoft.com/library/windows/apps/hh967834), and [**RegisteredProviderName**](https://msdn.microsoft.com/library/windows/apps/hh967835) properties of the current network object for the account.

For example:

``` syntax
var myNetwork = myNetworkAccountObject.currentNetwork
if (myNetwork != null && myNetwork.registeredDataClass == DataClasses.LteAdvanced)
{
  // user is connected to an LTE network
}
```

## <span id="related_topics"></span>Related topics


[Common tasks for mobile broadband Windows Runtime APIs](common-tasks-for-mobile-broadband-windows-runtime-apis.md)

 

 






