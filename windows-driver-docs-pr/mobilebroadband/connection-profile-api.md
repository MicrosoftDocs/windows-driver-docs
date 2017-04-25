---
title: Connection Profile API
description: Connection Profile API
ms.assetid: 671b0df6-4f4b-4867-86dd-5eb832d86b4b
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Connection Profile API


The connection profile API, which is part of [**Windows.Networking.Connectivity.NetworkInformation**](https://msdn.microsoft.com/library/windows/apps/br207293), provides connectivity, usage, and data plan information for established network connections. The connection profiles associated with a given mobile account can be retrieved by using the [**MobileBroadbandAccount**](https://msdn.microsoft.com/library/windows/apps/br207353) API. The connection profile API allows your mobile broadband app to query several properties of the network connection on the mobile broadband interface, including the following:

-   [**GetNetworkConnectivityLevel**](https://msdn.microsoft.com/library/windows/apps/hh701021) Indicates whether the network is connected and if the network provides internet connectivity.

-   [**GetSignalBars**](https://msdn.microsoft.com/library/windows/apps/dn266074) Indicates the current number of signal bars displayed by the Windows UI for the connection.

-   [**GetNetworkUsageAsync**](https://msdn.microsoft.com/library/windows/apps/dn266073) Provides bytes sent, bytes received, and connectivity times for a connection profile.

This API also includes a status change event that notifies the application whenever connectivity on the operator’s interface has changed. For more info about the [**NetworkStatusChanged**](https://msdn.microsoft.com/library/windows/apps/br207299) event, see [**NetworkStatusChangedEventHandler delegate**](https://msdn.microsoft.com/library/windows/apps/br207303).

## <span id="related_topics"></span>Related topics


[List of mobile broadband Windows Runtime APIs](list-of-mobile-broadband-windows-runtime-apis.md)

[Network Information sample](http://go.microsoft.com/fwlink/p/?linkid=227013)

[**NetworkStatusChangedEventHandler delegate**](https://msdn.microsoft.com/library/windows/apps/br207303)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_mb\p_mb%5D:%20Connection%20Profile%20API%20%20RELEASE:%20%281/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





