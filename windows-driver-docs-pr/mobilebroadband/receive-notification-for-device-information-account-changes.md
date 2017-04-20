---
title: Receive notification for device information account changes
description: Receive notification for device information account changes
ms.assetid: 67d96f61-57dc-4e4b-a6c1-5c3da28e8aaf
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Receive notification for device information account changes


To receive a notification for device information account changes, use the [**AccountUpdated**](https://msdn.microsoft.com/library/windows/apps/hh770601) event of [**MobileBroadbandAccountWatcher**](https://msdn.microsoft.com/library/windows/apps/hh770597) as described here:

1.  Instantiate a [**MobileBroadbandAccountWatcher**](https://msdn.microsoft.com/library/windows/apps/hh770597) object.

2.  Add an [**AccountUpdated**](https://msdn.microsoft.com/library/windows/apps/hh770601) event handler.

3.  Invoke [**Start**](https://msdn.microsoft.com/library/windows/apps/hh770604) on the watcher.

4.  Query the [**HasDeviceInformationChanged**](https://msdn.microsoft.com/library/windows/apps/hh770594) property of the [**MobileBroadbandAccountUpdatedEventArgs**](https://msdn.microsoft.com/library/windows/apps/hh770593) object in the [**AccountUpdated**](https://msdn.microsoft.com/library/windows/apps/hh770601) event handler.

5.  If the device information has changed, query the account [**CurrentDeviceInformation.TelephoneNumbers**](https://msdn.microsoft.com/library/windows/apps/br207373) property for the telephone number.

    For example:

    ``` syntax
    if (account.currentDeviceInformation.TelephoneNumbers.length > 0)
    {
      // there is now at least one telephone number
    }
    ```

## <span id="related_topics"></span>Related topics


[Common tasks for mobile broadband Windows Runtime APIs](common-tasks-for-mobile-broadband-windows-runtime-apis.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_mb\p_mb%5D:%20Receive%20notification%20for%20device%20information%20account%20changes%20%20RELEASE:%20%281/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





