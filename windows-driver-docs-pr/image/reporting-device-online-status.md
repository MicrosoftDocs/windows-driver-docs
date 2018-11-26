---
title: Reporting Device Online Status
description: Reporting Device Online Status
ms.assetid: 59ce747a-bb5e-4e8c-ab4a-d3f4432f17e6
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Reporting Device Online Status





The WIA service checks a WIA device's online status by calling the [**IStiUSD::GetStatus**](https://msdn.microsoft.com/library/windows/hardware/ff543823) method. The WIA minidriver should check the hardware's current online state and report the results.

The WIA service calls the **IStiUSD::GetStatus** method for two major operations:

-   Checking the device's online status.

-   Polling for device events, such as a push button event.

Determining the operation request can be done by checking the **StatusMask** member of the [**STI\_DEVICE\_STATUS**](https://msdn.microsoft.com/library/windows/hardware/ff548369) structure. The **StatusMask** member can be either of the following requests.

<a href="" id="sti-devstatus-online-state"></a>STI\_DEVSTATUS\_ONLINE\_STATE  
Check whether the device is online.

<a href="" id="sti-devstatus-events-state"></a>STI\_DEVSTATUS\_EVENTS\_STATE  
Check for device events.

### <a href="" id="sti-devstatus-online-state"></a>STI\_DEVSTATUS\_ONLINE\_STATE

This operation request should be carried out by setting the **dwOnlineState** member of the STI\_DEVICE\_STATUS structure.

### <a href="" id="sti-devstatus-events-state"></a>STI\_DEVSTATUS\_EVENTS\_STATE

This operation request should be carried out by setting the **dwEventHandlingState** member of the STI\_DEVICE\_STATUS structure. The value that should be used is STI\_EVENTHANDLING\_PENDING. (The device has an event pending and is waiting to report it to the WIA service.)

When STI\_EVENTHANDLING\_PENDING is set, the WIA service is signaled that an event has occurred in the WIA driver. The WIA service calls the [**IStiUSD::GetNotificationData**](https://msdn.microsoft.com/library/windows/hardware/ff543821) method to get more information about the event.

The **IStiUSD::GetNotificationData** method is called for polled events and interrupt events. It is in this method that you should fill out the proper event information to return to the WIA service.

**Note**   Always clear the STI\_EVENTHANDLING\_PENDING flag in the **dwEventHandlingState** member to ensure that it is properly set when a device event occurs.

 

The following example shows an implementation of the **IStiUSD::GetStatus** method.

```cpp
STDMETHODIMP CWIADevice::GetStatus(PSTI_DEVICE_STATUS pDevStatus)
{
  //
  // If the caller did not pass in the correct parameters,
  // then fail the call with E_INVALIDARG.
  //

  if(!pDevStatus)
  {
      return E_INVALIDARG;
  }

  HRESULT hr = S_OK;

  //
  // If we are asked, verify the device is online.
  //

  if (pDevStatus->StatusMask & STI_DEVSTATUS_ONLINE_STATE) {

    //
    // assume the device is OFF-LINE before continuing. This will
    // validate that the online check was successful.
    //

    pDevStatus->dwOnlineState = STI_ONLINESTATE_OFFLINE;

    if(MyDeviceIsOnlineStatus()) {
 
      //
      // device is ON-LINE and operational
      //

      pDevStatus->dwOnlineState |= STI_ONLINESTATE_OPERATIONAL;
    } else {

      //
      // device is OFF-LINE and NOT operational
      //

 }
  }
  return S_OK;
}
```

 

 




