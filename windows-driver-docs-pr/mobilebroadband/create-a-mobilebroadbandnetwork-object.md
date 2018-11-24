---
title: Create a MobileBroadbandNetwork object
description: Create a MobileBroadbandNetwork object
ms.assetid: b69c72dc-56cd-4358-9eae-3859705488ea
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Create a MobileBroadbandNetwork object


[**MobileBroadbandNetwork**](https://msdn.microsoft.com/library/windows/apps/hh770616) objects contain a set of properties that you can use to obtain live data about the network that is associated with a mobile broadband account (for example, the network registration state or the APN). You can obtain these objects from a [**MobileBroadbandAccount**](https://msdn.microsoft.com/library/windows/apps/br207353) object only. Note that a single **MobileBroadbandAccount** object can be associated with multiple **MobileBroadbandNetwork** objects, but only one at a time. (This will happen if a single SIM card, which holds the information that the MNO uses to differentiate user accounts, is used in two different mobile broadband devices.)

You obtain [**MobileBroadbandAccount**](https://msdn.microsoft.com/library/windows/apps/br207353) objects by getting the [**CurrentNetwork**](https://msdn.microsoft.com/library/windows/apps/hh770610) property of a **MobileBroadbandAccount** object. If there is no active network at the time that the **CurrentNetwork** property was read (for example, because the network device was unplugged or turned off, or the radio had no signal), reading this property will return NULL. Because this can change at any time (for example, the user can walk into an elevator with the computer, causing the connection to drop), we recommend that you get a copy of the property, test that for NULL, and use the copy. The following code example illustrates this.

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

## <span id="related_topics"></span>Related topics


[Common tasks for mobile broadband Windows Runtime APIs](common-tasks-for-mobile-broadband-windows-runtime-apis.md)

 

 






