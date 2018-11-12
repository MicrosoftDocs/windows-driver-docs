---
Description: Support for property commands (WpdBasicHardwareDriverSample)
title: Support for property commands (WpdBasicHardwareDriverSample)
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Supporting WPD property commands (WpdBasicHardwareDriverSample)


The sample driver supports six property commands. These commands are processed initially by the **WpdObjectProperties::DispatchMessage** method that, in turn, invokes a corresponding command handler. The **DispatchMessage** method and the individual handlers are all found in the *WpdObjectProperties.cpp* file.

The information in the following table describes each of the supported property commands, together with the names of the handlers that **WpdObjectProperties::DispatchMessage** calls when it processes a given command.

| Command                                           | Handler                  | Description                                                                                          |
|---------------------------------------------------|--------------------------|------------------------------------------------------------------------------------------------------|
| WPD\_COMMAND\_OBJECT\_PROPERTIES\_GET\_SUPPORTED  | OnGetSupportedProperties | Returns an array of property keys for the given object.                                              |
| WPD\_COMMAND\_OBJECT\_PROPERTIES\_GET             | OnGetPropertyValues      | Returns a collection of property values that correspond to the property keys supplied to the driver. |
| WPD\_COMMAND\_OBJECT\_PROPERTIES\_GET\_ALL        | OnGetAllProperties       | Returns all the property values for a given object.                                                  |
| WPD\_COMMAND\_OBJECT\_PROPERTIES\_SET             | OnSetPropertyValues      | Sets the specified property value on the device.                                                     |
| WPD\_COMMAND\_OBJECT\_PROPERTIES\_GET\_ATTRIBUTES | OnGetPropertyAttributes  | Returns a collection of attributes for one or more properties on a given object.                     |
| WPD\_COMMAND\_OBJECT\_PROPERTIES\_DELETE          | OnDeleteProperties       | Deletes the properties that are identified by the given property keys.                               |



## <span id="WPD_COMMAND_OBJECT_PROPERTIES_GET_SUPPORTED"></span><span id="wpd_command_object_properties_get_supported"></span>WPD\_COMMAND\_OBJECT\_PROPERTIES\_GET\_SUPPORTED


The driver calls the **WpdObjectProperties::OnGetSupportedProperties** handler in response to the WPD\_COMMAND\_OBJECT\_PROPERTIES\_GET\_ SUPPORTED command. The handler in turn calls an **AddSupportedPropertyKeys** method to retrieve the supported keys for the requested object.

Because the sample device does not support the Storage, Folder, or File objects in the WpdHelloWorldSample driver and because the new driver supported an object that is not found in the original driver, updating the **AddSupportedPropertyKeys** method was necessary.

The following code is taken from the revised **AddSupportedPropertyKeys** method. This method calls two supporting methods (**AddDevicePropertyKeys** and **AddSensorPropertyKeys**) to retrieve the keys for the requested object:

```cpp
HRESULT AddSupportedPropertyKeys(
    LPCWSTR                        wszObjectID,
    IPortableDeviceKeyCollection*  pKeys)
{
    HRESULT     hr          = S_OK;
    CAtlStringW strObjectID = wszObjectID;

    // Add Common PROPERTYKEYs for ALL WPD objects
    AddCommonPropertyKeys(pKeys);

    if (strObjectID.CompareNoCase(WPD_DEVICE_OBJECT_ID) == 0)
    {
        // Add the PROPERTYKEYs for the &#39;DEVICE&#39; object
        AddDevicePropertyKeys(pKeys);
    }

    // Add other PROPERTYKEYs for other supported objects...
    if (
           (strObjectID.CompareNoCase(SENSOR_OBJECT_ID) == 0) ||
           (strObjectID.CompareNoCase(TEMP_SENSOR_OBJECT_ID) == 0) ||
           (strObjectID.CompareNoCase(FLEX_SENSOR_OBJECT_ID) == 0) ||
           (strObjectID.CompareNoCase(PIR_SENSOR_OBJECT_ID) == 0) ||
           (strObjectID.CompareNoCase(PING_SENSOR_OBJECT_ID) == 0) ||
           (strObjectID.CompareNoCase(QTI_SENSOR_OBJECT_ID) == 0) ||
           (strObjectID.CompareNoCase(MEMSIC_SENSOR_OBJECT_ID) == 0) ||
           (strObjectID.CompareNoCase(HITACHI_SENSOR_OBJECT_ID) == 0) ||
           (strObjectID.CompareNoCase(PIEZO_SENSOR_OBJECT_ID) == 0) ||
           (strObjectID.CompareNoCase(COMPASS_SENSOR_OBJECT_ID) == 0)
       )
    {
        // Add the PROPERTYKEYs for the Sensor object
        AddSensorPropertyKeys(pKeys);
    }

    return hr;
}
```

## <span id="WPD_COMMAND_OBJECT_PROPERTIES_GET"></span><span id="wpd_command_object_properties_get"></span>WPD\_COMMAND\_OBJECT\_PROPERTIES\_GET


The driver calls the **WpdObjectProperties::OnGetPropertyValues** handler in response to the WPD\_COMMAND\_OBJECT\_PROPERTIES\_GET command. The handler, in turn, calls a **GetPropertyValuesForObject** method to retrieve the current values for the requested properties. Because the sensor devices do not support the Storage, Folder, or File objects that were found in the WpdHelloWorldSample driver, and, because the new driver supported an object that was not found in the original driver, updating this method was necessary.

The code that returned properties for the Device object remained intact. This is the code that returned the firmware version, power level, power source, device protocol, device model, and so on.

Although this code was unchanged, the device model (and other similar properties) that was returned by the sample driver differ from the property values that were returned by the WpdHelloWorldSample driver. This is because we updated the definitions in *WpdObjectProperties.h*:

```cpp
#define DEVICE_PROTOCOL_VALUE                L"Sensor Protocol ver 1.00"
#define DEVICE_FIRMWARE_VERSION_VALUE        L"1.0.0.0"
#define DEVICE_POWER_LEVEL_VALUE             100
#define DEVICE_MODEL_VALUE                   L"RS232 Sensor"
#define DEVICE_FRIENDLY_NAME_VALUE           L"Parallax BS2 Sensor"
#define DEVICE_MANUFACTURER_VALUE            L"Windows Portable Devices Group"
#define DEVICE_SERIAL_NUMBER_VALUE           L"01234567890123-45676890123456"
#define DEVICE_SUPPORTS_NONCONSUMABLE_VALUE  FALSE
```

The following table lists the definitions in *WpdObjectProperties.h*, the original value from the WpdHelloWorldSample, and the new value that is specified in the sample driver.

| Definition                             | Original value              | New value                   |
|----------------------------------------|-----------------------------|-----------------------------|
| DEVICE\_PROTOCOL\_VALUE                | Hello World Protocol v1.00  | Sensor Protocol v1.00       |
| DEVICE\_FIRMWARE\_VERSION              | 1.0.0.0                     | 1.0.0.0                     |
| DEVICE\_POWER\_LEVEL                   | 100                         | 100                         |
| DEVICE\_MODEL\_VALUE                   | Hello World!                | RS-232 Sensor               |
| DEVICE\_FRIENDLY\_NAME                 | Hello World!                | Parallax BS2 Sensor         |
| DEVICE\_MANUFACTURER\_VALUE            | WPD Group                   | WPD Group                   |
| DEVICE\_SERIAL\_NUMBER\_VALUE          | 012345678901234567890123456 | 012345678901234567890123456 |
| DEVICE\_SUPPORTS\_NONCONSUMABLE\_VALUE | **FALSE**                   | **FALSE**                   |



The most significant changes to the **GetPropertyValuesForObject** method occurred in the section that retrieves the sensor properties. This code retrieves several values that are defined in *WpdObjectProperties.h* such as the object name, its format, its content type, and whether it can be deleted.

In addition, this code also retrieves the current sensor reading and the sensor-update interval. These last two properties are retrieved by calling two helper functions: **GetSensorReading** and **GetUpdateInterval**.

The following excerpt from the **GetPropertyValuesForObject** method contains the code that retrieves the properties for the sensor object:

```cpp
// Retrieve the sensor properties

        else if (
                    (strObjectID.CompareNoCase(SENSOR_OBJECT_ID) == 0) ||
                    (strObjectID.CompareNoCase(TEMP_SENSOR_OBJECT_ID) == 0) ||
                    (strObjectID.CompareNoCase(FLEX_SENSOR_OBJECT_ID) == 0) ||
                    (strObjectID.CompareNoCase(PIR_SENSOR_OBJECT_ID) == 0) ||
                    (strObjectID.CompareNoCase(PING_SENSOR_OBJECT_ID) == 0) ||
                    (strObjectID.CompareNoCase(QTI_SENSOR_OBJECT_ID) == 0) ||
                    (strObjectID.CompareNoCase(MEMSIC_SENSOR_OBJECT_ID) == 0) ||
                    (strObjectID.CompareNoCase(HITACHI_SENSOR_OBJECT_ID) == 0) ||
                    (strObjectID.CompareNoCase(PIEZO_SENSOR_OBJECT_ID) == 0) ||
                    (strObjectID.CompareNoCase(COMPASS_SENSOR_OBJECT_ID) == 0)
                 )
        {
            for (DWORD dwIndex = 0; dwIndex < cKeys; dwIndex++)
            {
                PROPERTYKEY Key = WPD_PROPERTY_NULL;
                hr = pKeys->GetAt(dwIndex, &Key);
                CHECK_HR(hr, "Failed to get PROPERTYKEY at index %d in collection", dwIndex);

                if (hr == S_OK)
                {
                    // Preset the property value to &#39;error not supported&#39;.  The actual value
                    // will replace this value, if read from the device.
                    pValues->SetErrorValue(Key, HRESULT_FROM_WIN32(ERROR_NOT_SUPPORTED));
                    if (IsEqualPropertyKey(Key, WPD_OBJECT_ID))
                    {
                        hr = pValues->SetStringValue(WPD_OBJECT_ID, strObjectID);
                        CHECK_HR(hr, "Failed to set WPD_OBJECT_ID");
                    }

                    else if (IsEqualPropertyKey(Key, WPD_OBJECT_PERSISTENT_UNIQUE_ID))
                    {

                        // Retrieve the ID of the sensor using the m_SensorType member of the
                        // basedriver that is set during the data-read operation.
                        hr = pValues->SetStringValue(WPD_OBJECT_PERSISTENT_UNIQUE_ID, strObjectID);
                        CHECK_HR(hr, "Failed to set WPD_OBJECT_PERSISTENT_UNIQUE_ID");
                    }

                    else if (IsEqualPropertyKey(Key, WPD_OBJECT_PARENT_ID))
                    {
                        hr = pValues->SetStringValue(WPD_OBJECT_PARENT_ID, WPD_DEVICE_OBJECT_ID);
                        CHECK_HR(hr, "Failed to set WPD_OBJECT_PARENT_ID");
                    }

                    else if (IsEqualPropertyKey(Key, WPD_OBJECT_NAME))
                    {
                        // Retrieve the name of the sensor using the m_SensorType member of the
                        // basedriver that is set during the data-read operation.
                        if (m_pBaseDriver->m_SensorType == 0)
                            hr = pValues->SetStringValue(WPD_OBJECT_NAME, SENSOR_OBJECT_NAME_VALUE);
                        else if (m_pBaseDriver->m_SensorType == 2)
                            hr = pValues->SetStringValue(WPD_OBJECT_NAME, TEMP_SENSOR_OBJECT_NAME_VALUE);
                        else if (m_pBaseDriver->m_SensorType == 3)
                            hr = pValues->SetStringValue(WPD_OBJECT_NAME, FLEX_SENSOR_OBJECT_NAME_VALUE);
                        else if (m_pBaseDriver->m_SensorType == 4)
                            hr = pValues->SetStringValue(WPD_OBJECT_NAME, PING_SENSOR_OBJECT_NAME_VALUE);
                        else if (m_pBaseDriver->m_SensorType == 5)
                            hr = pValues->SetStringValue(WPD_OBJECT_NAME, PIR_SENSOR_OBJECT_NAME_VALUE);
                        else if (m_pBaseDriver->m_SensorType == 6)
                            hr = pValues->SetStringValue(WPD_OBJECT_NAME, MEMSIC_SENSOR_OBJECT_NAME_VALUE);
                        else if (m_pBaseDriver->m_SensorType == 7)
                            hr = pValues->SetStringValue(WPD_OBJECT_NAME, QTI_SENSOR_OBJECT_NAME_VALUE);
                        else if (m_pBaseDriver->m_SensorType == 8)
                            hr = pValues->SetStringValue(WPD_OBJECT_NAME, PIEZO_SENSOR_OBJECT_NAME_VALUE);
                        else if (m_pBaseDriver->m_SensorType == 9)
                            hr = pValues->SetStringValue(WPD_OBJECT_NAME, HITACHI_SENSOR_OBJECT_NAME_VALUE);
                        CHECK_HR(hr, "Failed to set WPD_OBJECT_NAME");
                    }

                    else if (IsEqualPropertyKey(Key, WPD_OBJECT_FORMAT))
                    {
                        hr = pValues->SetGuidValue(WPD_OBJECT_FORMAT, WPD_OBJECT_FORMAT_UNSPECIFIED);
                        CHECK_HR(hr, "Failed to set WPD_OBJECT_FORMAT");
                    }

                    else if (IsEqualPropertyKey(Key, WPD_OBJECT_CONTENT_TYPE))
                    {
                        hr = pValues->SetGuidValue(WPD_OBJECT_CONTENT_TYPE, WPD_CONTENT_TYPE_FUNCTIONAL_OBJECT);
CHECK_HR(hr, "Failed to set WPD_OBJECT_CONTENT_TYPE");
                    }

                    else if (IsEqualPropertyKey(Key, WPD_OBJECT_CAN_DELETE))
                    {
                        hr = pValues->SetBoolValue(WPD_OBJECT_CAN_DELETE, FALSE);
                        CHECK_HR(hr, "Failed to set WPD_OBJECT_CAN_DELETE");
                    }

                    else if (IsEqualPropertyKey(Key, SENSOR_READING))
                    {
                        hr = pValues->SetUnsignedLargeIntegerValue(SENSOR_READING, GetSensorReading());
                        CHECK_HR(hr, "Failed to set SENSOR_READING");
                    }

                    else if (IsEqualPropertyKey(Key, SENSOR_UPDATE_INTERVAL))
                    {
                        hr = pValues->SetUnsignedLargeIntegerValue(SENSOR_UPDATE_INTERVAL, GetUpdateInterval());
                        CHECK_HR(hr, "Failed to set SENSOR_UPDATE_INTERVAL");
                    }
                    else if (IsEqualPropertyKey(Key, WPD_FUNCTIONAL_OBJECT_CATEGORY))
                    {
                        hr = pValues->SetGuidValue(WPD_FUNCTIONAL_OBJECT_CATEGORY, FUNCTIONAL_CATEGORY_SENSOR_SAMPLE);
                        CHECK_HR(hr, "Failed to set WPD_FUNCTIONAL_OBJECT_CATEGORY");
                    }
                }
             } // end for
        } // end else if
```

The **GetSensorReading** helper function retrieves the most recent sensor reading in numeric (DWORD) format:

```cpp
LONGLONG WpdObjectProperties::GetSensorReading()
{    
    // Ensure that this value isn&#39;t currently being accessed by another thread
    CComCritSecLock<CComAutoCriticalSection> Lock(m_SensorReadingCriticalSection);

    return m_llSensorReading;
}
```

**Note**  A critical section is necessary to prevent concurrent accesses of the *m\_llSensorReading* member variable. This value is overwritten when each RS232 read completes asynchronously, and is read whenever the SENSOR\_READING property is retrieved by a WPD application.



The **GetUpdateInterval** helper function performs an identical operation: it accesses the *m\_dwUpdateInterval* member variable and returns the value in numeric (DWORD) format if it is available:

```ManagedCPlusPlus
DWORD WpdObjectProperties::GetUpdateInterval()
{    
    return m_dwUpdateInterval;
}
```

Be aware that the *m\_dwUpdateInterval* member variable must be protected by a critical section if multiple threads will access this value (if ,for example, a WDF parallel dispatch queue is used instead of the sequential dispatch queue, or if **WpdBaseDriver::ProcessReadData** is modified to set the update interval multiple times instead of one time during initialization). For simplicity, the critical section is omitted.

## <span id="WPD_COMMAND_OBJECT_PROPERTIES_GET_ALL"></span><span id="wpd_command_object_properties_get_all"></span>WPD\_COMMAND\_OBJECT\_PROPERTIES\_GET\_ALL


The driver calls the **WpdObjectProperties::OnGetAllPropertyValues** handler in response to the WPD\_COMMAND\_OBJECT\_PROPERTIES\_GET\_ALL command. The handler, in turn, retrieves all the property keys for the given object and then calls the **GetPropertyValuesForObject** helper function to retrieve the current values for the requested properties.

## <span id="WPD_COMMAND_OBJECT_PROPERTIES_SET"></span><span id="wpd_command_object_properties_set"></span>WPD\_COMMAND\_OBJECT\_PROPERTIES\_SET


The driver calls the **WpdObjectProperties::OnSetPropertyValues** handler in response to the WPD\_COMMAND\_OBJECT\_PROPERTIES\_SET command. The only property that can be written (or set) in the sample driver is SENSOR\_UPDATE\_INTERVAL.

The handler first examines the object identifier for the given property and then examines the property key itself. If the object identifier is set to SENSOR\_OBJECT\_ID and the property key is SENSOR\_UPDATE\_INTERVAL, the handler calls the **SendUpdateIntervalToDevice** helper function to update the value.

The **SendUpdateIntervalToDevice** helper function performs the write operation by checking for a valid input value, formatting a write request with that value, and then sending the write request to the device.

```cpp
HRESULT WpdObjectProperties::SendUpdateIntervalToDevice(DWORD dwNewInterval)
{
    HRESULT      hr                           = S_OK;
    RS232Target* pDeviceTarget                = NULL;

    CHAR  szInterval[INTERVAL_DATA_LENGTH+1]  = {0};

    // Check the input value
    if (IsValidUpdateInterval(dwNewInterval) == FALSE)
    {
        hr = HRESULT_FROM_WIN32(ERROR_INVALID_DATA);
        CHECK_HR(hr, "Invalid update interval: %d", dwNewInterval);
    }

    // Format a write request with the input value
    if (hr == S_OK)
    {
        hr = StringCchPrintfA(szInterval, 
                              ARRAYSIZE(szInterval), "%d", dwNewInterval);
        CHECK_HR(hr, "Failed to convert the new interval to a CHAR string");
    }

    // Send the write request to the device
    if (hr == S_OK)
    {
        pDeviceTarget = m_pBaseDriver->GetRS232Target();

        if (pDeviceTarget->IsReady())
        {
            hr = pDeviceTarget->
                 SendWriteRequest((BYTE *)szInterval, sizeof(szInterval));
            CHECK_HR(hr, 
                     "Failed to send the write request to 
                      set the new temperature update interval");

            if (hr == S_OK)
            {
                TraceEvents(TRACE_LEVEL_VERBOSE, TRACE_FLAG_DRIVER, 
                            "%!FUNC! Sent new interval: %s", szInterval);
            }
        }
        else
        {
            hr = HRESULT_FROM_WIN32(ERROR_NOT_READY);
            CHECK_HR(hr, "Device is not ready to receive write requests");
        }
    }

    if (hr == S_OK)
    {
        // Update the cached value on the driver
        SetUpdateInterval(dwNewInterval);
    }

    return hr;
}
```

## <span id="WPD_COMMAND_OBJECT_PROPERTIES_GET_ATTRIBUTES"></span><span id="wpd_command_object_properties_get_attributes"></span>WPD\_COMMAND\_OBJECT\_PROPERTIES\_GET\_ATTRIBUTES


The driver calls the **WpdObjectProperties::OnGetPropertyAttributes** handler in response to the WPD\_COMMAND\_OBJECT\_PROPERTIES\_GET\_ATTRIBUTES command. The handler, in turn, calls the **GetPropertyAttributesForObject** helper function to retrieve the attributes for the given object.

In the original WpdHelloWorldSample driver, the attributes for every property were identical and all the properties were read-only. However, in the updated driver, the SENSOR\_UPDATE\_INTERVAL is read/write, and both SENSOR\_UPDATE\_INTERVAL and SENSOR\_READING have the form WPD\_PROPERTY\_ATTRIBUTE\_FORM\_RANGE. As a result, minor changes were required in this helper function.

## <span id="related_topics"></span>Related topics


****
[The WpdBasicHardwareDriverSample](the-wpdbasichardwaredriver-sample.md)

[The WPD Driver Samples](the-wpd-driver-samples.md)









