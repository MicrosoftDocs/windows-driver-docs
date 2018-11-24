---
title: Create a MobileBroadbandDeviceInformation object
description: Create a MobileBroadbandDeviceInformation object
ms.assetid: d7f89045-acb5-4b7c-9154-c05e4169490d
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Create a MobileBroadbandDeviceInformation object


A [**MobileBroadbandDeviceInformation**](https://msdn.microsoft.com/library/windows/apps/br207361) object contain a set of properties that you can use to obtain mobile broadband–specific data about the network device that is associated with a mobile broadband account (for example, the firmware version). You can obtain these objects from a [**MobileBroadbandAccount**](https://msdn.microsoft.com/library/windows/apps/br207353) object only. Note that a single **MobileBroadbandAccount** object can be associated with multiple **MobileBroadbandDeviceInformation** objects, but only one at a time. (This will happen if a single SIM card, which holds the information that the MNO uses to differentiate user accounts, is used in two different mobile broadband devices.)

You get [**MobileBroadbandDeviceInformation**](https://msdn.microsoft.com/library/windows/apps/br207361) objects by getting the [**CurrentDeviceInformation**](https://msdn.microsoft.com/library/windows/apps/hh770609) property of a [**MobileBroadbandAccount**](https://msdn.microsoft.com/library/windows/apps/br207353) object. If there is no network device present at the time that the **CurrentDeviceInformation** property was read (for example, because it was unplugged or turned off), reading this property will return NULL. Because this can change at any time (for example, the user can unplug the device), we recommend that you get a copy of the property, test that for NULL, and use the copy. The following code example illustrates shows how to do this:

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

## <span id="related_topics"></span>Related topics


[Common tasks for mobile broadband Windows Runtime APIs](common-tasks-for-mobile-broadband-windows-runtime-apis.md)

 

 






