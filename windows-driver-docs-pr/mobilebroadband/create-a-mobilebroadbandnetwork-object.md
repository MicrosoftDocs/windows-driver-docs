---
title: Create a MobileBroadbandNetwork object
description: Create a MobileBroadbandNetwork object
ms.assetid: b69c72dc-56cd-4358-9eae-3859705488ea
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_mb\p_mb%5D:%20Create%20a%20MobileBroadbandNetwork%20object%20%20RELEASE:%20%281/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





