---
Description: Supporting Device Events
title: Supporting Device Events
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Supporting Device Events


The sample driver defines and supports a custom WPD event that is associated with the sensor functional object, WPD\_EVENT\_SENSOR\_READING\_UPDATED.

This custom event is sent to notify any connected client that a new sensor reading is available. The information in the following table describes the parameters.

| Parameter name                   | Description                                                         |
|----------------------------------|---------------------------------------------------------------------|
| WPD\_EVENT\_PARAMETER\_EVENT\_ID | A GUID value set to WPD\_EVENT\_ SENSOR\_READING\_UPDATED.          |
| SENSOR\_READING                  | An unsigned large integer value that contains the sensor reading.   |
| SENSOR\_UPDATE\_INTERVAL         | An unsigned integer value that contains the sensor update interval. |



The event GUID for this custom event is defined in *Stdafx.h*. In **WpdBaseDriver::ProcessReadData**, the driver calls **WpdBaseDriver::PostSensorReadingEvent** after it extracts the sensor reading, updates interval from a read request, and then converts them to DWORD values.

**WpdBaseDriver::PostSensorReadingEvent** completes the following steps:

1.  Initializes an **IPortableDeviceValues** to hold the event parameters.
2.  Serializes the **IPortableDeviceValues** into a BYTE buffer.
3.  Calls **IWDFDevice::PostEvent** that has the EventGuid set to WPD\_EVENT\_NOTIFICATION, the event type set to WdfEventBroadcast, and the serialized BYTE buffer of the event parameters:

```cpp
if (hr == S_OK)
{
    // Initialize the event parameters
    m_pEventParams->Clear();

    // Populate the event parameters
    hr = m_pEventParams-> 
         SetGuidValue(WPD_EVENT_PARAMETER_EVENT_ID, 
                      WPD_EVENT_SENSOR_READING_UPDATED);
    CHECK_HR(hr, "Failed to set the WPD_EVENT_PARAMETER_EVENT_ID");
}

if (hr == S_OK)
{
    hr = m_pEventParams->SetUnsignedLargeIntegerValue(SENSOR_READING, 
                                                 llSensorData);
    CHECK_HR(hr, "Failed to set the sensor reading");
}

if (hr == S_OK)
{
    hr = m_pEventParams->SetUnsignedIntegerValue(SENSOR_UPDATE_INTERVAL, dwUpdateInterval);
    CHECK_HR(hr, "Failed to set the sensor update interval");
}

if (hr == S_OK)
{
    // Create a buffer with the serialized parameters
    hr = m_pWpdSerializer->GetBufferFromIPortableDeviceValues(m_pEventParams,  
                                                              &pBuffer,
                                                              &cbBuffer);
    CHECK_HR(hr, "Failed to get buffer from IPortableDeviceValues");
}
// Send the event
if (hr == S_OK)
{
    hr = m_pWDFDevice->PostEvent(WPD_EVENT_NOTIFICATION, 
                                 WdfEventBroadcast, 
                                 pBuffer, 
                                 cbBuffer);
    CHECK_HR(hr, "Failed to post the WPD broadcast event");
}
```

To receive any WPD event, an application would implement the **IPortableDeviceEventCallback::OnEvent** callback method and call **IPortableDevice::Advise** to register to receive an event notification callback.

In the event callback, the application checks if the event GUID matches WPD\_EVENT\_ SENSOR\_READING\_UPDATED and gets the sensor reading and interval data from the event parameters.

## <span id="related_topics"></span>Related topics


****
[The WpdBasicHardwareDriverSample](the-wpdbasichardwaredriver-sample.md)

[The WPD Driver Samples](the-wpd-driver-samples.md)









