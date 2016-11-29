---
title: Reporting Device Online Status
author: windows-driver-content
description: Reporting Device Online Status
MS-HAID:
- 'WIA\_drv\_basic\_fd76f962-9761-4086-ab10-e8a16cf3f9cf.xml'
- 'image.reporting\_device\_online\_status'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 59ce747a-bb5e-4e8c-ab4a-d3f4432f17e6
---

# Reporting Device Online Status


## <a href="" id="ddk-reporting-device-online-status-si"></a>


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

```
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Reporting%20Device%20Online%20Status%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


