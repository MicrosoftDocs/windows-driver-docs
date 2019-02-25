---
Description: Supporting the Property Range Attributes
title: Supporting the Property Range Attributes
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Supporting the Property Range Attributes


The sample driver supports two properties: the update interval (SENSOR\_UPDATE\_INTERVAL) and the current sensor reading (SENSOR\_READING). Each of these properties supports a set of general attributes (deleteable, readable, writeable, and so on). In addition, these properties support specific range attributes (minimum, maximum, and step value).

In the case of the sensor reading, the property is expressed as a range (WPD\_PROPERTY\_ATTRIBUTE\_FORM\_RANGE).

The property attributes correspond to entries in the *Rs232connection.h* file. These entries specify the minimum and maximum values that the device supports as well as the step value that an application can use when it sets the property within the given range:

```cpp
#define SENSOR_READING_MIN 1  
#define SENSOR_READING_MAX 378  
#define SENSOR_READING_STEP 1   
```

The code that sets these range attributes is found in WpdObjectProperties::GetPropertyAttributesForObject (in the *Wpdobjectproperties.cpp* module). This code uses the values that are defined in *Rs232connection.h* to set these attributes:

```cpp
else if (IsEqualPropertyKey(Key, SENSOR_READING))
{
    // Form range attributes for the temperature reading property
    hr = pAttributes->SetUnsignedIntegerValue(WPD_PROPERTY_ATTRIBUTE_FORM, 
                                              WPD_PROPERTY_ATTRIBUTE_FORM_RANGE);
    CHECK_HR(hr, 
             "Failed to set WPD_PROPERTY_ATTRIBUTE_RANGE_MIN 
              for SENSOR_READING");

    hr = pAttributes->SetUnsignedIntegerValue(WPD_PROPERTY_ATTRIBUTE_RANGE_MIN, 
                                              SENSOR_READING_MIN);
    CHECK_HR(hr, 
             "Failed to set WPD_PROPERTY_ATTRIBUTE_RANGE_MIN 
              for SENSOR_READING");

    hr = pAttributes->SetUnsignedIntegerValue(WPD_PROPERTY_ATTRIBUTE_RANGE_MAX, 
                                              SENSOR_READING_MAX);
    CHECK_HR(hr, 
             "Failed to set WPD_PROPERTY_ATTRIBUTE_RANGE_MAX 
              for SENSOR_READING");

    hr = pAttributes->SetUnsignedIntegerValue(WPD_PROPERTY_ATTRIBUTE_RANGE_STEP, 
                                              SENSOR_READING_STEP);
    CHECK_HR(hr, 
             "Failed to set WPD_PROPERTY_ATTRIBUTE_RANGE_STEP 
              for TEMPERATURE_SENSOR_READING");
}
```

## <span id="related_topics"></span>Related topics


****
[The WpdBasicHardwareDriverSample](the-wpdbasichardwaredriver-sample.md)

[The WPD Driver Samples](the-wpd-driver-samples.md)

 

 





