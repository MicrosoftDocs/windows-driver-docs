---
title: Know when network connectivity changes
description: Know when network connectivity changes
ms.assetid: 2937ba62-16ad-4a81-92e8-62a8bb40d608
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Know when network connectivity changes


To know when network connectivity changes, use the [**AccountUpdated**](https://msdn.microsoft.com/library/windows/apps/hh770601) event of [**MobileBroadbandAccountWatcher**](https://msdn.microsoft.com/library/windows/apps/hh770597):

1.  Instantiate a [**MobileBroadbandAccountWatcher**](https://msdn.microsoft.com/library/windows/apps/hh770597) object.

2.  Add an [**AccountUpdated**](https://msdn.microsoft.com/library/windows/apps/hh770601) event handler.

3.  Invoke [**Start**](https://msdn.microsoft.com/library/windows/apps/hh770604) on the watcher.

4.  Query the [**HasNetworkChanged**](https://msdn.microsoft.com/library/windows/apps/hh770595) property of the [**MobileBroadbandAccountUpdatedEventArgs**](https://msdn.microsoft.com/library/windows/apps/hh770593) object in the [**AccountUpdated**](https://msdn.microsoft.com/library/windows/apps/hh770601) event handler.

5.  If the network has changed, query the [**CurrentNetwork**](https://msdn.microsoft.com/library/windows/apps/hh770610) property for the current network object.

## <span id="related_topics"></span>Related topics


[Common tasks for mobile broadband Windows Runtime APIs](common-tasks-for-mobile-broadband-windows-runtime-apis.md)

 

 






