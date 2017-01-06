---
Description: Supporting the Property Range Attributes
MS-HAID: 'wpddk.the\_wpdbasichardwaredriver\_supporting\_property\_range\_attributes'
MSHAttr: 'PreferredLib:/library/windows/hardware'
title: Supporting the Property Range Attributes
---

# Supporting the Property Range Attributes


The sample driver supports two properties: the update interval (SENSOR\_UPDATE\_INTERVAL) and the current sensor reading (SENSOR\_READING). Each of these properties supports a set of general attributes (deleteable, readable, writeable, and so on). In addition, these properties support specific range attributes (minimum, maximum, and step value).

In the case of the sensor reading, the property is expressed as a range (WPD\_PROPERTY\_ATTRIBUTE\_FORM\_RANGE).

The property attributes correspond to entries in the *Rs232connection.h* file. These entries specify the minimum and maximum values that the device supports as well as the step value that an application can use when it sets the property within the given range:

```
#define SENSOR_READING_MIN 1  
#define SENSOR_READING_MAX 378  
#define SENSOR_READING_STEP 1   
```

The code that sets these range attributes is found in WpdObjectProperties::GetPropertyAttributesForObject (in the *Wpdobjectproperties.cpp* module). This code uses the values that are defined in *Rs232connection.h* to set these attributes:

```
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[wpd_dk\wpddk]:%20Supporting%20the%20Property%20Range%20Attributes%20%20RELEASE:%20%281/5/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




