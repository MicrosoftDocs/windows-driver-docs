---
title: Create a MobileBroadbandDeviceInformation object
description: Create a MobileBroadbandDeviceInformation object
ms.date: 04/20/2017
---

# Create a MobileBroadbandDeviceInformation object


A [**MobileBroadbandDeviceInformation**](/uwp/api/Windows.Networking.NetworkOperators.MobileBroadbandDeviceInformation) object contain a set of properties that you can use to obtain mobile broadband–specific data about the network device that is associated with a mobile broadband account (for example, the firmware version). You can obtain these objects from a [**MobileBroadbandAccount**](/uwp/api/Windows.Networking.NetworkOperators.MobileBroadbandAccount) object only. Note that a single **MobileBroadbandAccount** object can be associated with multiple **MobileBroadbandDeviceInformation** objects, but only one at a time. (This will happen if a single SIM card, which holds the information that the MNO uses to differentiate user accounts, is used in two different mobile broadband devices.)

You get [**MobileBroadbandDeviceInformation**](/uwp/api/Windows.Networking.NetworkOperators.MobileBroadbandDeviceInformation) objects by getting the [**CurrentDeviceInformation**](/uwp/api/Windows.Networking.NetworkOperators.MobileBroadbandAccount#Windows_Networking_NetworkOperators_MobileBroadbandAccount_CurrentDeviceInformation) property of a [**MobileBroadbandAccount**](/uwp/api/Windows.Networking.NetworkOperators.MobileBroadbandAccount) object. If there is no network device present at the time that the **CurrentDeviceInformation** property was read (for example, because it was unplugged or turned off), reading this property will return NULL. Because this can change at any time (for example, the user can unplug the device), we recommend that you get a copy of the property, test that for NULL, and use the copy. The following code example illustrates shows how to do this:

``` syntax
var myDeviceInfo = myNetworkAccountObject.currentDeviceInformation

if (myDeviceInfo == null)
{
  // no device present, inform user
}
else 
{
  // use myDeviceInfo to get the data you need
}
```

## Related topics


[Common tasks for mobile broadband Windows Runtime APIs](./create-a-mobilebroadbandaccount-object.md)

 

