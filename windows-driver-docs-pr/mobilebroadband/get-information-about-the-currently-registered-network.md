---
title: Get information about the currently registered network
description: Get information about the currently registered network
ms.assetid: 94321933-fc93-4203-8de1-e715d66fd1e3
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_mb\p_mb%5D:%20Get%20information%20about%20the%20currently%20registered%20network%20%20RELEASE:%20%281/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





