---
title: Create a MobileBroadbandNetwork object
description: Create a MobileBroadbandNetwork object
ms.date: 04/20/2017
---

# Create a MobileBroadbandNetwork object


[**MobileBroadbandNetwork**](/uwp/api/Windows.Networking.NetworkOperators.MobileBroadbandNetwork) objects contain a set of properties that you can use to obtain live data about the network that is associated with a mobile broadband account (for example, the network registration state or the APN). You can obtain these objects from a [**MobileBroadbandAccount**](/uwp/api/Windows.Networking.NetworkOperators.MobileBroadbandAccount) object only. Note that a single **MobileBroadbandAccount** object can be associated with multiple **MobileBroadbandNetwork** objects, but only one at a time. (This will happen if a single SIM card, which holds the information that the MNO uses to differentiate user accounts, is used in two different mobile broadband devices.)

You obtain [**MobileBroadbandAccount**](/uwp/api/Windows.Networking.NetworkOperators.MobileBroadbandAccount) objects by getting the [**CurrentNetwork**](/uwp/api/Windows.Networking.NetworkOperators.MobileBroadbandAccount#Windows_Networking_NetworkOperators_MobileBroadbandAccount_CurrentNetwork) property of a **MobileBroadbandAccount** object. If there is no active network at the time that the **CurrentNetwork** property was read (for example, because the network device was unplugged or turned off, or the radio had no signal), reading this property will return NULL. Because this can change at any time (for example, the user can walk into an elevator with the computer, causing the connection to drop), we recommend that you get a copy of the property, test that for NULL, and use the copy. The following code example illustrates this.

``` syntax
var myNetwork = myNetworkAccountObject.currentNetwork

if (myNetwork == null)
{
  // no network, inform user
}
else
{
  // use myNetwork to get the data you need
}
```

## Related topics


[Common tasks for mobile broadband Windows Runtime APIs](./create-a-mobilebroadbandaccount-object.md)

 

