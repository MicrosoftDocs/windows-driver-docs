---
title: Receive notification for device information account changes
description: Receive notification for device information account changes
ms.assetid: 67d96f61-57dc-4e4b-a6c1-5c3da28e8aaf
ms.date: 04/20/2017
ms.localizationpriority: medium
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

 

 






