---
title: Create a MobileBroadbandAccount object
description: Create a MobileBroadbandAccount object
ms.assetid: 631e885f-67bb-4c30-a82f-352c23cc973a
---

# Create a MobileBroadbandAccount object


Because the [**MobileBroadbandAccount**](https://msdn.microsoft.com/library/windows/apps/br207353) objects represent network accounts, a network account ID is needed to create such an object. When a mobile broadband app is started from the network list, it receives the network account ID to use as a parameter to the tile launch contract.

If the app is activated directly from its tile, there are no parameters associated with the tile launch contract, and you must get the value of the [**AvailableNetworkAccountIds**](https://msdn.microsoft.com/library/windows/apps/hh770608) static property of the [**MobileBroadbandAccount**](https://msdn.microsoft.com/library/windows/apps/br207353) class. This returns a read-only collection of strings, in which each string is a single account ID. If this method returns a collection that has a single string, you don’t need to take any further action. The following JavaScript code example shows how to do this:

``` syntax
var myNetworkAccountId;
var allNetworkAccountIds = Windows.Networking.NetworkOperators.MobileBroadbandAccount.availableNetworkAccountIds;

if (allNetworkAccountIds.size == 1)
{
  myNetworkAccountId = allNetworkAccountIds[0]; 
}
```

If the returned collection contains more than one string, you will need input from end user who is running the application. One way is to iterate through the collection, creating a [**MobileBroadbandAccount**](https://msdn.microsoft.com/library/windows/apps/br207353) object for each account ID in the collection, and then use a property of the object (for example, the telephone number) to populate a list box control. This control is presented to the end user, and after the user makes a selection, all other **MobileBroadbandAccount** objects can be released.

After you have the account ID, call the [**CreateFromNetworkAccountId**](https://msdn.microsoft.com/library/windows/apps/br207354) static method of class [**MobileBroadbandAccount**](https://msdn.microsoft.com/library/windows/apps/br207353) . The following code example shows how to do this by using JavaScript:

``` syntax
var myNetworkAccountId = "{95499FEF-1579-4547-A0BE-FF271ADBBE76}";
var myNetworkAccountObject = Windows.Networking.NetworkOperators.MobileBroadbandAccount.createFromNetworkAccountId(myNetworkAccountId);
```

## <span id="emptylist"></span><span id="EMPTYLIST"></span>MobileBroadbandAccount.AvailableNetworkAccountIds returns an empty list


If your app is not trusted, the property returns an empty collection instead of throwing an exception because users can have accounts from more than one network operator on their computer. The [**AvailableNetworkAccountIds**](https://msdn.microsoft.com/library/windows/apps/hh770608) property returns only those account IDs that the app’s metadata package is allowed to see. Because the **AvailableNetworkAccountIds** property checks that each account ID has a device associated with it at the time it is retrieved, this property can return an empty collection even if [**CreateFromNetworkAccountId**](https://msdn.microsoft.com/library/windows/apps/br207354) does not throw an Access Denied exception.

This can happen if no network hardware is detected, or if the network hardware does not have an accessible SIM. A simple way to determine the exact reason why the returned collection is empty is to look at the WWAN logs. After you have collected the logs, search the text log file for entries that contain the text **AvailableNetworkAccountIds**.

## <span id="related_topics"></span>Related topics


[Common tasks for mobile broadband Windows Runtime APIs](common-tasks-for-mobile-broadband-windows-runtime-apis.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_mb\p_mb%5D:%20Create%20a%20MobileBroadbandAccount%20object%20%20RELEASE:%20%281/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





