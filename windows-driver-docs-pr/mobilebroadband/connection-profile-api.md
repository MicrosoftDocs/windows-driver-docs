---
title: Connection Profile API
description: Connection Profile API
ms.assetid: 671b0df6-4f4b-4867-86dd-5eb832d86b4b
ms.date: 04/20/2017
ms.localizationpriority: medium
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

 

 






