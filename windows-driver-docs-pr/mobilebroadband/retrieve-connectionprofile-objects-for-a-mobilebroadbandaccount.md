---
title: Retrieve ConnectionProfile objects for a MobileBroadbandAccount
description: Retrieve ConnectionProfile objects for a MobileBroadbandAccount
ms.assetid: 7e612aa5-1627-4ada-971a-a1d04eafeb81
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_mb\p_mb%5D:%20Retrieve%20ConnectionProfile%20objects%20for%20a%20MobileBroadbandAccount%20%20RELEASE:%20%281/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





