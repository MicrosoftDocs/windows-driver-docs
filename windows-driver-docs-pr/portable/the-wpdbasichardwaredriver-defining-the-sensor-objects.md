---
Description: Defining the Sensor Objects
title: Defining the Sensor Objects
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Defining the Sensor Objects


In Windows Portable Devices (WPD), the logical entities on devices are referred to as objects. Objects can represent informational or functional parts of a device. Any object has one or more properties. You can think of the properties as object-description metadata. For example, the TempHumidity Object on the sample temperature and humidity sensor supports a SENSOR\_READING property. This property specifies the current temperature and relative humidity that the device obtained.

The WpdHelloWorldDriver supports the objects that are shown in the following table.

| Object  | Description                                                                                                                |
|---------|----------------------------------------------------------------------------------------------------------------------------|
| Device  | The root object that contains descriptive properties, for example, the firmware version, the model, and the friendly name. |
| Storage | An object that exposes properties, for example, a storage capacity, a file-system type, and a count of free bytes.         |
| Folder  | An object that exposes properties, for example, a folder name.                                                             |
| File    | An object that exposes properties, for example, a file name and actual file contents.                                      |

 

Because the sample sensors do not support a storage, folder, or file object, the WpdBasicHardwareDriver does not implement these objects. Instead, each sensor type is represented by a single object. The following table lists the objects that the WpdBasicHardwareDriver supports.

| Object       | Description                                                                                                                                |
|--------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| Device       | The root object that contains descriptive properties, for example, the firmware version, the model, and the friendly name.                 |
| TempHumidity | A functional object that displays the temperature reading and humidity reading, as well as an update interval property that can be edited. |
| Compass      | A functional object that displays the compass reading, as well as an update interval property that can be edited.                          |
| PIR          | A functional object that displays the passive infrared reading, as well as an update interval property that can be edited.                 |
| QTI          | A functional object that displays the ambient light reading, as well as an update interval property that can be edited.                    |
| Flex         | A functional object that displays the pressure reading, as well as an update interval property that can be edited.                         |
| Ping         | A functional object that displays the distance reading, as well as an update interval property that can be edited.                         |
| Piezo        | A functional object that displays the vibration reading, as well as an update interval property that can be edited.                        |
| Memsic       | A functional object that displays the 2-axis accelerometer reading, as well as an update interval property that can be edited.             |
| Hitachi      | A functional object that displays the 3-axis accelerometer reading, as well as an update interval property that can be edited.             |

 

In WPD, objects are identified by strings. The string identifier for the device object is defined in the *Portabledevice.h* file:

```cpp
#define WPD_DEVICE_OBJECT_ID  L"DEVICE"
```

The string identifiers for the sensor objects are defined in the *WpdObjectProperties.h* file for the WpdBasicHardwareDriver:

```cpp
#define SENSOR_OBJECT_ID             L"Sensor"
#define SENSOR_OBJECT_NAME_VALUE          L"Parallax Sensor"
#define COMPASS_SENSOR_OBJECT_ID              L"Compass"
#define COMPASS_SENSOR_OBJECT_NAME_VALUE      L"HM55B Compass Sensor"
#define PIR_SENSOR_OBJECT_ID                  L"PIR"
#define PIR_SENSOR_OBJECT_NAME_VALUE          L"Passive Infra-Red Sensor"
#define QTI_SENSOR_OBJECT_ID                  L"QTI"
#define QTI_SENSOR_OBJECT_NAME_VALUE          L"QTI Light Sensor"
#define FLEX_SENSOR_OBJECT_ID                 L"Flex"
#define FLEX_SENSOR_OBJECT_NAME_VALUE         L"Flex Force Sensor"
#define PING_SENSOR_OBJECT_ID                 L"Ping"
#define PING_SENSOR_OBJECT_NAME_VALUE         L"Ultrasonic Distance Sensor"
#define PIEZO_SENSOR_OBJECT_ID                L"Piezo"
#define PIEZO_SENSOR_OBJECT_NAME_VALUE        L"Piezo Vibration Sensor"
#define TEMP_SENSOR_OBJECT_ID                 L"TempHumidity"
#define TEMP_SENSOR_OBJECT_NAME_VALUE         L"Sensiron Temperature and Humidity Sensor"
#define MEMSIC_SENSOR_OBJECT_ID               L"Memsic"
#define MEMSIC_SENSOR_OBJECT_NAME_VALUE       L"Memsic Dual-Axis G-Force Sensor"
#define HITACHI_SENSOR_OBJECT_ID              L"Hitachi"
#define HITACHI_SENSOR_OBJECT_NAME_VALUE      L"Hitachi Tri-Axis G-Force Sensor"
```

These object identifier constants are passed to the methods in source modules that handle object enumeration (*WpdObjectEnum.cpp*), property handling (*WpdObjectProperties.cpp*), and device-capability retrieval (*WpdCapabilities.cpp*). The following excerpt from the **WpdObjectEnumerator::OnFindNext** method shows how these identifiers are used in object enumeration for the sample driver:

```cpp
// If the enumeration context reports that there are more objects to return, then continue, if not,
    // return an empty results set.
    if ((hr == S_OK) && (pEnumeratorContext != NULL) && (pEnumeratorContext->HasMoreChildrenToEnumerate() == TRUE))
    {
        if (pEnumeratorContext->m_strParentObjectID.CompareNoCase(L"") == 0)
        {
            // We are being asked for the WPD_DEVICE_OBJECT_ID
            hr = AddStringValueToPropVariantCollection(pObjectIDCollection, WPD_DEVICE_OBJECT_ID);
            CHECK_HR(hr, "Failed to add &#39;DEVICE&#39; object ID to enumeration collection");

            // Update the number of children we are returning for this enumeration call
            NumObjectsEnumerated++;
        }
        else if (pEnumeratorContext->m_strParentObjectID.CompareNoCase(WPD_DEVICE_OBJECT_ID) == 0)
        {
    
            // We are being asked for direct children of the WPD_DEVICE_OBJECT_ID
            switch (m_pBaseDriver->m_SensorType)
            {
            case WpdBaseDriver::UNKNOWN:
                    hr = AddStringValueToPropVariantCollection(pObjectIDCollection, SENSOR_OBJECT_ID);
                    break;
            case WpdBaseDriver::COMPASS:
                    hr = AddStringValueToPropVariantCollection(pObjectIDCollection, COMPASS_SENSOR_OBJECT_ID);
                    break;
            case WpdBaseDriver::SENSIRON:
                    hr = AddStringValueToPropVariantCollection(pObjectIDCollection, TEMP_SENSOR_OBJECT_ID);
                    break;
            case WpdBaseDriver::FLEX:
                    hr = AddStringValueToPropVariantCollection(pObjectIDCollection, FLEX_SENSOR_OBJECT_ID);
                    break;
            case WpdBaseDriver::PING:
                    hr = AddStringValueToPropVariantCollection(pObjectIDCollection, PING_SENSOR_OBJECT_ID);
                    break;
            case WpdBaseDriver::PIR:
                    hr = AddStringValueToPropVariantCollection(pObjectIDCollection, PIR_SENSOR_OBJECT_ID);
                    break;
            case WpdBaseDriver::MEMSIC:
                    hr = AddStringValueToPropVariantCollection(pObjectIDCollection, MEMSIC_SENSOR_OBJECT_ID);
                    break;
            case WpdBaseDriver::QTI:
                    hr = AddStringValueToPropVariantCollection(pObjectIDCollection, QTI_SENSOR_OBJECT_ID);
                    break;
            case WpdBaseDriver::PIEZO:
                    hr = AddStringValueToPropVariantCollection(pObjectIDCollection, PIEZO_SENSOR_OBJECT_ID);
                    break;
            case WpdBaseDriver::HITACHI:
                    hr = AddStringValueToPropVariantCollection(pObjectIDCollection, HITACHI_SENSOR_OBJECT_ID);
                    break;
                default:
                    break;
```

In the WpdBasicHardwareDriver sample, the driver defines a single functional category that encompasses all sensors. A driver developer can extend this sample and define separate functional categories for each sensor type so that applications can identify which sensors the driver supports. This requires that the developer modify the WpdCapabilities::OnGetFunctionalCategories method so that it correctly returns these new categories.

 

 




