---
Description: Supporting Device Events
MS-HAID: 'wpddk.the\_wpdbasichardwaredriver\_supporting\_device\_events'
MSHAttr: 'PreferredLib:/library/windows/hardware'
title: Supporting Device Events
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

```
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[wpd_dk\wpddk]:%20Supporting%20Device%20Events%20%20RELEASE:%20%281/5/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




