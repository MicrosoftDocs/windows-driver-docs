---
title: Adding Polling Event Support
author: windows-driver-content
description: Adding Polling Event Support
MS-HAID:
- 'WIA\_db\_event\_645eacba-1ef0-47a0-a2af-8d699fc599d2.xml'
- 'image.adding\_polling\_event\_support'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 7c7617d4-22d6-48a8-b69c-dd0347f078dd
---

# Adding Polling Event Support


## <a href="" id="ddk-adding-polling-event-support-si"></a>


To properly set up your WIA driver to report polling events, do the following:

1.  Set **Capabilities=0x33** in your device's INF file. (See [INF Files for WIA Devices](inf-files-for-wia-devices.md) for details.)

2.  Report STI\_GENCAP\_NOTIFICATIONS and STI\_USD\_GENCAP\_NATIVE\_PUSHSUPPORT in the [**IStiUSD::GetCapabilities**](https://msdn.microsoft.com/library/windows/hardware/ff543817) method.

3.  Report all supported events in the [**IWiaMiniDrv::drvGetCapabilities**](https://msdn.microsoft.com/library/windows/hardware/ff543977) method.

4.  Respond to calls to the [**IStiUSD::GetStatus**](https://msdn.microsoft.com/library/windows/hardware/ff543823) method. The WIA service calls this method at a preset interval that is configurable in the INF file. The default setting is a 1-second interval.

5.  Report the proper event information response in the [**IStiUSD::GetNotificationData**](https://msdn.microsoft.com/library/windows/hardware/ff543821) method.

The WIA service calls the **IStiUSD::GetStatus** method for two major operations:

1.  Checking the device's online status.

2.  Polling for device events, such as a push button event.

Determining the operation request can be done by checking the **StatusMask** member of the [**STI\_DEVICE\_STATUS**](https://msdn.microsoft.com/library/windows/hardware/ff548369) structure. The **StatusMask** member can be either of the following requests:

<a href="" id="sti-devstatus-online-state"></a>STI\_DEVSTATUS\_ONLINE\_STATE  
This operation request checks whether the device is online and should be filled by setting the **dwOnlinesState** member of the STI\_DEVICE\_STATUS structure.

<a href="" id="sti-devstatus-events-state"></a>STI\_DEVSTATUS\_EVENTS\_STATE  
This operation request checks for device events. It should be filled by setting the **dwEventHandlingState** member of the STI\_DEVICE\_STATUS structure. The value that should be used is STI\_EVENTHANDLING\_PENDING. (The device has an event pending and is waiting to report it to the WIA service.)

When STI\_EVENTHANDLING\_PENDING is set, the WIA service is signaled that an event has occurred in the WIA driver. The WIA service calls the **IStiUSD::GetNotificationData** method to get more information about the event.

The **IStiUSD::GetNotificationData** method is called for polled events and interrupt events. It is in this method that you should fill out the proper event information to return to the WIA service.

**Note**  **** Always clear the STI\_EVENTHANDLING\_PENDING flag in the **dwEventHandlingState** member to ensure that it is properly set when a device event occurs.
This WIA driver should set the *m\_guidLastEvent* class member variable to the proper event GUID when an event is detected. The *m\_guidLastEvent* is checked at a later time when the WIA service calls the **IStiUSD::GetNotificationData** method. The *m\_guidLastEvent* member variable is defined in the **CWIADevice** class (in the following code snippet), used to cache the last event signaled. After this member variable has been requested by the WIA service, it is always set to GUID\_NULL.

 

The following example shows an implementation of the [**IStiUSD::GetStatus**](https://msdn.microsoft.com/library/windows/hardware/ff543823) method.

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
  // If we are asked, verify state of an event handler 
  //(front panel buttons, user controlled attachments, etc.).
  //
  // If your device requires polling, then this is where you would
  // specify the event result.
  // However, It is not recommended to have polled events.
  // Interrupt events are better for performance, and reliability.
  // See the SetNotificationsHandle method for how to
  // implement interrupt events.
  //

  //
  // clear the dwEventHandlingState field first to make sure we are really setting
  // a pending event.
  //

  pDevStatus->dwEventHandlingState &= ~STI_EVENTHANDLING_PENDING;
  if (pDevStatus->StatusMask & STI_DEVSTATUS_EVENTS_STATE) {

    //
    // set the polled event result here, for the GetNotificationData()
    // method to read and report.
    // (m_guidLastEvent will be read in GetNotificationData)
    //

    LONG lEventResult = 0;
    PollMyDeviceForEvents(&lEventResult)

    if(lEventResult == DEVICE_SCAN_BUTTON_PRESSED) {

        //
        // polled event result was one we know about
        //

        m_guidLastEvent = WIA_EVENT_SCAN_IMAGE;
    } else {

        //
        // nothing happened, so continue
        //

        m_guidLastEvent = GUID_NULL;
    }

    if (m_guidLastEvent != GUID_NULL) {

        //
        // if the event GUID is NOT GUID_NULL, set the
        // STI_EVENTHANDLING_PENDING flag letting the WIA service
        // know that we have an event ready. This will tell the WIA
        // service to call GetNotificationData() for the event
        // specific information.
        //

        pDevStatus->dwEventHandlingState |= STI_EVENTHANDLING_PENDING;
    }
  }
  return S_OK;
}
```

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Adding%20Polling%20Event%20Support%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


