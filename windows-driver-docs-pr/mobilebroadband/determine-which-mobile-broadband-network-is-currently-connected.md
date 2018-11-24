---
title: Determine which mobile broadband network is currently connected
description: Determine which mobile broadband network is currently connected
ms.assetid: 65a47e79-3976-4f72-b810-982e7222fee3
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Determine which mobile broadband network is currently connected


You can determine which mobile broadband network you’re connected to by retrieving the APN through the [**AccessPointName**](https://msdn.microsoft.com/library/windows/apps/hh770617) property of the current network object for the account.

For example:

``` syntax
account.currentNetwork.accessPointName
```

## <span id="related_topics"></span>Related topics


[Common tasks for mobile broadband Windows Runtime APIs](common-tasks-for-mobile-broadband-windows-runtime-apis.md)

 

 






