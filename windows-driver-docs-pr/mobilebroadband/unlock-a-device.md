---
title: Unlock a device
description: Unlock a device
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Unlock a device


A subset of the mobile broadband API includes the PIN Management API. To unlock a device, do the following:

1.  Get the network adapter ID for the account device:

    ``` syntax
    account.currentNetwork.networkAdapter. networkAdapterId
    ```

2.  Create an [**IMbnInterfaceManager**](/windows/win32/api/mbnapi/nn-mbnapi-imbninterfacemanager) instance.

3.  Advise to the [**IMbnPinManagerEvents**](/windows/win32/api/mbnapi/nn-mbnapi-imbnpinmanagerevents) and [**IMbnPinEvents**](/windows/win32/api/mbnapi/nn-mbnapi-imbnpinevents) connection points (these are used for getting PIN state and unblock/unlock results). For more info, see the Remarks section of [**IMbnInterfaceManager**](/windows/win32/api/mbnapi/nn-mbnapi-imbninterfacemanager).

4.  Pass the network adapter ID into [**IMbnInterfaceManager::GetInterface**](/windows/win32/api/mbnapi/nf-mbnapi-imbninterfacemanager-getinterface) to get an [**IMbnInterface**](/windows/win32/api/mbnapi/nn-mbnapi-imbninterface) interface for the device.

5.  Get an [**IMbnPinManager**](/windows/win32/api/mbnapi/nn-mbnapi-imbnpinmanager) interface for the device by calling [**IMbnInterface::QueryInterface**](/windows/win32/api/mbnapi/nn-mbnapi-imbninterface).

6.  Call [**IMbnPinManager::GetPinState**](/windows/win32/api/mbnapi/nf-mbnapi-imbnpinmanager-getpinstate) to get the PIN state of the device (the state returned by using the connection point that was registered in step 3).

7.  Determine how the device is locked or blocked by using the [**MBN\_PIN\_INFO::pinState**](/windows/win32/api/mbnapi/ns-mbnapi-mbn_pin_info) parameter that is passed into the event.

8.  Get an IMbnPin interface for the appropriate PIN by calling [**IMbnPinManager::GetPin**](/windows/win32/api/mbnapi/nf-mbnapi-imbnpinmanager-getpin).

9.  Call either [**IMbnPin::Enter**](/windows/win32/api/mbnapi/nf-mbnapi-imbnpin-enter) or [**IMbnPin::Unblock**](/windows/win32/api/mbnapi/nf-mbnapi-imbnpin-unblock), based on how the device is locked (see step 7).

10. Listen for **Unlock** or **Unblock** results by using [**IMbnPinEvents**](/windows/win32/api/mbnapi/nn-mbnapi-imbnpinevents) registration to know whether the operation was successful.

## <span id="related_topics"></span>Related topics


[Common tasks for mobile broadband Windows Runtime APIs](./create-a-mobilebroadbandaccount-object.md)

 

