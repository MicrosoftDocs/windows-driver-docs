---
title: Create a MobileBroadbandDeviceInformation object
description: Create a MobileBroadbandDeviceInformation object
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: d7f89045-acb5-4b7c-9154-c05e4169490d
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_mb\p_mb%5D:%20Create%20a%20MobileBroadbandDeviceInformation%20object%20%20RELEASE:%20%281/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





