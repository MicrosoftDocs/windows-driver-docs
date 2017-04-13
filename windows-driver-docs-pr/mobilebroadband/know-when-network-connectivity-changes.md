---
title: Know when network connectivity changes
description: Know when network connectivity changes
ms.assetid: 2937ba62-16ad-4a81-92e8-62a8bb40d608
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_mb\p_mb%5D:%20Know%20when%20network%20connectivity%20changes%20%20RELEASE:%20%281/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





