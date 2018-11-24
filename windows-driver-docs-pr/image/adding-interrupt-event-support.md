---
title: Adding Interrupt Event Support
description: Adding Interrupt Event Support
ms.assetid: 74fbaa7c-f058-4b17-b278-3dea0faf4431
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Adding Interrupt Event Support





To properly set up your WIA driver to report interrupt events, do the following:

1.  Set **Capabilities=0x31** in the device's INF file. (See [INF Files for WIA Devices](inf-files-for-wia-devices.md) for details.)

2.  Report STI\_GENCAP\_NOTIFICATIONS and STI\_USD\_GENCAP\_NATIVE\_PUSHSUPPORT in the [**IStiUSD::GetCapabilities**](https://msdn.microsoft.com/library/windows/hardware/ff543817) method.

3.  Report all supported events in the [**IWiaMiniDrv::drvGetCapabilities**](https://msdn.microsoft.com/library/windows/hardware/ff543977) method.

4.  Cache and use the event handle passed in the [**IStiUSD::SetNotificationHandle**](https://msdn.microsoft.com/library/windows/hardware/ff543840) method. This is the event handle that the device signals, or the WIA minidriver signals directly using **SetEvent** (described in the Microsoft Windows SDK documentation). It is in this method that you initiate the waiting state of the WIA device.

5.  Report the proper event information response in the [**IStiUSD::GetNotificationData**](https://msdn.microsoft.com/library/windows/hardware/ff543821) method.

The following two examples show configuring your device for interrupts with implementations of the **IWiaMiniDrv::drvGetCapabilities** and **IStiUSD::SetNotificationHandle** methods.

**Note**   It is important to use overlapped I/O calls with all activities involving the kernel mode drivers. This allows for proper time-outs and cancellation of device requests.

 

### <a href="" id="explanation-of-the-iwiaminidrv-drvgetcapabilities-implementation"></a>Explanation of the IWiaMiniDrv::drvGetCapabilities Implementation

The WIA service calls the **IWiaMiniDrv::drvGetCapabilities** method to obtain the WIA device-supported events and commands. The WIA driver should first look at the incoming *lFlags* parameter to determine which request it should answer.

The WIA driver should allocate memory (to be used by the WIA driver and freed by it) to contain an array of [**WIA\_DEV\_CAP\_DRV**](https://msdn.microsoft.com/library/windows/hardware/ff550233) structures. In the call to the **IWiaMiniDrv::drvGetCapabilities**, pass a pointer to the memory location that holds the address of the WIA driver-allocated memory in the *ppCapabilities* parameter.

**Note**   The WIA service will not free this memory. It is important that the WIA driver manages the allocated memory.

 

The following example shows an implementation of the [**IWiaMiniDrv::drvGetCapabilities**](https://msdn.microsoft.com/library/windows/hardware/ff543977) method.

```cpp
HRESULT _stdcall CWIADevice::drvGetCapabilities(
  BYTE            *pWiasContext,
  LONG            lFlags,
  LONG            *pcelt,
  WIA_DEV_CAP_DRV **ppCapabilities,
  LONG            *plDevErrVal)
{
  //
  // If the caller did not pass in the correct parameters,
  //  then fail the call and return E_INVALIDARG.
  //

  if (!pWiasContext) {

    //
    // The WIA service may pass in a NULL for the pWiasContext. 
    // This is expected because there is a case where no item 
    // was created at the time the event was fired.
    //
  }

  if (!plDevErrVal) {
      return E_INVALIDARG;
  }

  if (!pcelt) {
      return E_INVALIDARG;
  }

  if (!ppCapabilities) {
      return E_INVALIDARG;
  }

  *plDevErrVal = 0;

  HRESULT hr = S_OK;

  LONG lNumberOfCommands = 1;
  LONG lNumberOfEvents   = 2;

  //
  // initialize WIA driver capabilities ARRAY
  // a member WIA_DEV_CAP_DRV m_Capabilities[3] variable
  // This memory should live with the WIA minidriver.
  // A pointer to this structure is given to the WIA service using
  // ppCapabilities.  Do not delete this memory until
  // the WIA minidriver has been unloaded.
  //

  // This ARRAY should only be initialized once.
  // The Descriptions and Names should be read from the proper
  // string resource.  These string values should be localized in
  // multiple languages because an application will be use them to
  // be displayed to the user.
  //

  // Command #1
  m_Capabilities[0].wszDescription =   L"Synchronize Command";
  m_Capabilities[0].wszName = L"Synchronize";
  m_Capabilities[0].guid    = (GUID*)&WIA_CMD_SYNCHRONIZE;
  m_Capabilities[0].lFlags = 0;
  m_Capabilities[0].wszIcon = WIA_ICON_SYNCHRONIZE;

  // Event #1
  m_Capabilities[1].wszDescription = L"Scan Button";
  m_Capabilities[1].wszName = L"Scan";
  m_Capabilities[1].guid    = (GUID*)&WIA_EVENT_SCAN_IMAGE;
  m_Capabilities[1].lFlags = WIA_NOTIFICATION_EVENT | WIA_ACTION_EVENT;
  m_Capabilities[1].wszIcon = WIA_ICON_SCAN_BUTTON_PRESS;

  // Event #2
  m_Capabilities[2].wszDescription = L"Copy Button";
  m_Capabilities[2].wszName = L"Copy";
  m_Capabilities[2].guid    = (GUID*)&WIA_EVENT_SCAN_PRINT_IMAGE;
  m_Capabilities[2].lFlags = WIA_NOTIFICATION_EVENT | WIA_ACTION_EVENT;
  m_Capabilities[2].wszIcon = WIA_ICON_SCAN_BUTTON_PRESS;


  //
  //  Return depends on flags.  Flags specify whether we should return
  //  commands, events, or both.
  //
  //

  switch (lFlags) {
  case WIA_DEVICE_COMMANDS:

    //
    //  report commands only
    //

    *pcelt          = lNumberOfCommands;
    *ppCapabilities = &m_Capabilities[0];
    break;
  case WIA_DEVICE_EVENTS:

    //
    //  report events only
    //

    *pcelt          = lNumberOfEvents;
    *ppCapabilities = &m_Capabilities[1]; // start at the first event in the ARRAY
    break;
  case (WIA_DEVICE_COMMANDS | WIA_DEVICE_EVENTS):

    //
    //  report both events and commands
    //

     *pcelt          = (lNumberOfCommands + lNumberOfEvents);
     *ppCapabilities = &m_Capabilities[0];
     break;
  default:

    //
    //  invalid request
    //
    hr = E_INVALIDARG;
    break;
  }

  return hr;
}
```

The [**IStiUSD::SetNotificationHandle**](https://msdn.microsoft.com/library/windows/hardware/ff543840) method is called by the WIA service or internally by this driver to start or stop event notifications. The WIA service will pass in a valid handle, created using **CreateEvent** (described in the Microsoft Windows SDK documentation), indicating that the WIA driver is to signal this handle when an event occurs in the hardware.

**NULL** can be passed to the **IStiUSD::SetNotificationHandle** method. **NULL** indicates that the WIA minidriver is to stop all device activity, and exit any event wait operations.

The following example shows an implementation of the **IStiUSD::SetNotificationHandle** method.

```cpp
STDMETHODIMP CWIADevice::SetNotificationHandle(HANDLE hEvent)
{
  HRESULT hr = S_OK;

  if (hEvent && (hEvent != INVALID_HANDLE_VALUE)) {

    //
    // A valid handle indicates that we are asked to start our "wait"
    // for device interrupt events
    //

    //
    // reset last event GUID to GUID_NULL
    //

    m_guidLastEvent = GUID_NULL;

    //
    // clear EventOverlapped structure
    //

    memset(&m_EventOverlapped,0,sizeof(m_EventOverlapped));

    //
    // fill overlapped hEvent member with the event passed in by 
    // the WIA service. This handle will be automatically signaled
    //  when an event is triggered at the hardware level.
    //

    m_EventOverlapped.hEvent = hEvent;

    //
    // clear event data buffer.  This is the buffer that will be used
    //  to determine what event was signaled from the device.
    //

    memset(m_EventData,0,sizeof(m_EventData));

    //
    // use the following call for interrupt events on your device
    //

    DWORD dwError = 0;
    BOOL bResult = DeviceIoControl( m_hDeviceDataHandle,
                                    IOCTL_WAIT_ON_DEVICE_EVENT,
                                    NULL,
                                    0,
                                    &m_EventData,
                                    sizeof(m_EventData),
                                    &dwError,
                                    &m_EventOverlapped );

    if (bResult) {
        hr = S_OK;
    } else {
        hr = HRESULT_FROM_WIN32(::GetLastError());
    }

  } else {

    //
    // stop any hardware waiting events here, the WIA service has
    // notified us to stop all hardware event waiting
    //

    //
    // Stop hardware interrupt events. This will stop all activity on
    // the device. Since DeviceIOControl was used with OVERLAPPED i/o 
    // functionality the CancelIo() can be used to stop all kernel
    // mode activity.
    //


    if(m_hDeviceDataHandle){
        if(!CancelIo(m_hDeviceDataHandle)){

            //
            // canceling of the IO failed, call GetLastError() here to determine the cause.
            //

            LONG lError = ::GetLastError();

        }
    }
  }
  return hr;
}
```

When the WIA minidriver or a WIA device has detected and signaled an event, the WIA service calls the [**IStiUSD::GetNotificationData**](https://msdn.microsoft.com/library/windows/hardware/ff543821) method. It is in this method that the WIA minidriver should report the details of the event that occurred.

The WIA service calls the **IStiUSD::GetNotificationData** method to get information about an event that has just been signaled. The **IStiUSD::GetNotificationData** method can be called as a result of one of two event operations.

1.  **IStiUSD::GetStatus** reported that there was an event pending by setting the STI\_EVENTHANDLING\_PENDING flag in the [**STI\_DEVICE\_STATUS**](https://msdn.microsoft.com/library/windows/hardware/ff548369) structure.

2.  The *hEvent* handle passed in by **IStiUSD::SetNotificationHandle** was signaled by the hardware, or by calling **SetEvent** (described in the Microsoft Windows SDK documentation).

The WIA driver is responsible for filling out the [**STINOTIFY**](https://msdn.microsoft.com/library/windows/hardware/ff548350) structure

The following example shows an implementation of the **IStiUSD::GetNotificationData** method.

```cpp
STDMETHODIMP CWIADevice::GetNotificationData( LPSTINOTIFY pBuffer )
{
  //
  // If the caller did not pass in the correct parameters,
  // then fail the call with E_INVALIDARG.
  //

  if(!pBuffer){
      return E_INVALIDARG;
  }
 
  GUID guidEvent = GUID_NULL;
  DWORD dwBytesRet = 0;
  BOOL bResult = GetOverlappedResult(m_hDeviceDataHandle, &m_EventOverlapped, &dwBytesRet, FALSE );
  if (bResult) {
    //
    // read the m_EventData buffer to determine the proper event.
    // set guidEvent to the proper event GUID
    // set guidEvent to GUID_NULL when an event has
    // not happened that you are concerned with
    //

    if(m_EventData[0] == DEVICE_SCAN_BUTTON_PRESSED) {
       guidEvent = WIA_EVENT_SCAN_IMAGE;
    } else {
       guidEvent = GUID_NULL;
    }
  }

  //
  // If the event was triggered, then fill in the STINOTIFY structure
  // with the proper event information
  //

  if (guidEvent != GUID_NULL) {
    memset(pBuffer,0,sizeof(STINOTIFY));
    pBuffer->dwSize               = sizeof(STINOTIFY);
    pBuffer->guidNotificationCode = guidEvent;        
  } else {
    return STIERR_NOEVENTS;
  }

  return S_OK;
}
```

Interrupt events can be stopped at any time by passing **NULL** as the event handle. The minidriver should interpret this as a signal to stop any wait states on the hardware device.

**Note**   The [**IWiaMiniDrv::drvNotifyPnpEvent**](https://msdn.microsoft.com/library/windows/hardware/ff544998) method can receive power management events that affect the event waiting state.

 

The WIA service calls the **IWiaMiniDrv::drvNotifyPnpEvent** method and sends a WIA\_EVENT\_POWER\_SUSPEND event when the system is about to be placed in a sleep state. If this call occurs, the device might already be out of its wait state. Sleep states automatically trigger kernel-mode drivers to exit any waiting state to allow the system to enter this powered-down state. When the system resumes from its sleep state, the WIA service sends the WIA\_EVENT\_POWER\_RESUME event. At this time the WIA minidriver must reestablish the interrupt event wait state. For more information about sleep states, see [System Power States](https://msdn.microsoft.com/library/windows/hardware/ff564571) and [Device Power States](https://msdn.microsoft.com/library/windows/hardware/ff543162).

It is recommended that the WIA minidriver cache the event handle initially passed into the [**IStiUSD::SetNotificationHandle**](https://msdn.microsoft.com/library/windows/hardware/ff543840) method so that it can be reused when the system wakes up from a sleep or hibernation.

The WIA service *does not* call the **IStiUSD::SetNotificationHandle** method after the system has resumed. It is recommended that the minidriver call its **IStiUSD::SetNotificationHandle** method, passing the cached event handle.

The WIA service calls the **IWiaMiniDrv::drvNotifyPnpEvent** method when system events occur. The WIA driver should check the *pEventGUID* parameter to determine which event is being processed.

Some common events that must be processed are:

<a href="" id="wia-event-power-suspend"></a>WIA\_EVENT\_POWER\_SUSPEND  
The system is going into suspend/sleep mode.

<a href="" id="wia-event-power-resume"></a>WIA\_EVENT\_POWER\_RESUME  
The system is waking up from suspend/sleep mode.

The WIA driver should restore any event interrupt wait states after returning from a suspend. This ensures that the events will still function when the system wakes up.

The following example shows an implementation of the [**IWiaMiniDrv::drvNotifyPnpEvent**](https://msdn.microsoft.com/library/windows/hardware/ff544998) method.

```cpp
HRESULT _stdcall CWIADevice::drvNotifyPnpEvent(
  const GUID *pEventGUID,
  BSTR       bstrDeviceID,
  ULONG      ulReserved)
{
  //
  // If the caller did not pass in the correct parameters,
  // then fail the call with E_INVALIDARG.
  //

  if ((!pEventGUID)||(!bstrDeviceID)) {
      return E_INVALIDARG;
  }

  HRESULT hr = S_OK;

  if(*pEventGUID == WIA_EVENT_POWER_SUSPEND) {

    //
    // disable any driver activity to make sure we properly
    // shut down (the driver is not being unloaded, just disabled)
    //

  } else if(*pEventGUID == WIA_EVENT_POWER_RESUME) {

    //
    // reestablish any event notifications to make sure we properly
    // set up any event waiting status using the WIA service supplied
    // event handle
    //

    if(m_EventOverlapped.hEvent) {

      //
      // call ourselves with the cached EVENT handle given to
      // the WIA driver by the WIA service.
      //

        SetNotificationHandle(m_EventOverlapped.hEvent);
    }
  }
  return hr;
}
```

 

 




