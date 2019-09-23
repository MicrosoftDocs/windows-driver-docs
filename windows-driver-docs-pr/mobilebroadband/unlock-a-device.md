---
title: Unlock a device
description: Unlock a device
ms.assetid: 4e6ed725-2384-429b-be1e-027b7784e95b
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Unlock a device


A subset of the mobile broadband API includes the PIN Management API. To unlock a device, do the following:

1.  Get the network adapter ID for the account device:

    ``` syntax
    account.currentNetwork.networkAdapter. networkAdapterId
    ```

2.  Create an [**IMbnInterfaceManager**](https://docs.microsoft.com/windows/desktop/api/mbnapi/nn-mbnapi-imbninterfacemanager) instance.

3.  Advise to the [**IMbnPinManagerEvents**](https://docs.microsoft.com/windows/desktop/api/mbnapi/nn-mbnapi-imbnpinmanagerevents) and [**IMbnPinEvents**](https://docs.microsoft.com/windows/desktop/api/mbnapi/nn-mbnapi-imbnpinevents) connection points (these are used for getting PIN state and unblock/unlock results). For more info, see the Remarks section of [**IMbnInterfaceManager**](https://docs.microsoft.com/windows/desktop/api/mbnapi/nn-mbnapi-imbninterfacemanager).

4.  Pass the network adapter ID into [**IMbnInterfaceManager::GetInterface**](https://docs.microsoft.com/windows/desktop/api/mbnapi/nf-mbnapi-imbninterfacemanager-getinterface) to get an [**IMbnInterface**](https://docs.microsoft.com/windows/desktop/api/mbnapi/nn-mbnapi-imbninterface) interface for the device.

5.  Get an [**IMbnPinManager**](https://docs.microsoft.com/windows/desktop/api/mbnapi/nn-mbnapi-imbnpinmanager) interface for the device by calling [**IMbnInterface::QueryInterface**](https://docs.microsoft.com/windows/desktop/api/mbnapi/nn-mbnapi-imbninterface).

6.  Call [**IMbnPinManager::GetPinState**](https://docs.microsoft.com/windows/desktop/api/mbnapi/nf-mbnapi-imbnpinmanager-getpinstate) to get the PIN state of the device (the state returned by using the connection point that was registered in step 3).

7.  Determine how the device is locked or blocked by using the [**MBN\_PIN\_INFO::pinState**](https://docs.microsoft.com/windows/desktop/api/mbnapi/ns-mbnapi-mbn_pin_info) parameter that is passed into the event.

8.  Get an IMbnPin interface for the appropriate PIN by calling [**IMbnPinManager::GetPin**](https://docs.microsoft.com/windows/desktop/api/mbnapi/nf-mbnapi-imbnpinmanager-getpin).

9.  Call either [**IMbnPin::Enter**](https://docs.microsoft.com/windows/desktop/api/mbnapi/nf-mbnapi-imbnpin-enter) or [**IMbnPin::Unblock**](https://docs.microsoft.com/windows/desktop/api/mbnapi/nf-mbnapi-imbnpin-unblock), based on how the device is locked (see step 7).

10. Listen for **Unlock** or **Unblock** results by using [**IMbnPinEvents**](https://docs.microsoft.com/windows/desktop/api/mbnapi/nn-mbnapi-imbnpinevents) registration to know whether the operation was successful.

## <span id="related_topics"></span>Related topics


[Common tasks for mobile broadband Windows Runtime APIs](common-tasks-for-mobile-broadband-windows-runtime-apis.md)

 

 






