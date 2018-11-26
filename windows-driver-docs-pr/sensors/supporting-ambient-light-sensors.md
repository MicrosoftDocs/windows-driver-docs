---
title: Supporting ambient light sensors
description: Supporting ambient light sensors
ms.assetid: a0875084-c093-4659-91b9-375450f65234
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Supporting ambient light sensors


Ambient light sensors can measure current lighting conditions. You can use data from light sensors to automatically adjust screen brightness and keyboard illumination. You can also create light-aware applications that adjust user interface elements for current lighting conditions. In Windows 8, automatic brightness control with ambient light sensors (adaptive brightness) is fully supported.

Windows 8 includes class driver support for both ACPI 3.0b-compliant and HID-compliant ambient light sensor implementations. This means that you do not have to write custom drivers to support ambient light sensors. These sensors can also be used by Sensor API-based client applications, because these drivers integrate with the Windows Sensor and Location platform.

For more information about ambient light sensors and the adaptive brightness feature in Windows 8, see the white paper "Integrating Ambient Light Sensors with " Windows 7 on the [Windows Hardware Developer Central](http://go.microsoft.com/fwlink/p/?linkid=133337) website.

For ambient light sensors that are not ACPI 3.0b-compliant or HID-compliant, you must create a sensor driver to integrate with the Sensor and Location platform.

## Handling light sensor properties


For Windows 8, the correct type for SENSOR\_DATA\_TYPE\_LIGHT\_LEVEL\_LUX is VT\_R4. However, for Windows 7, the correct type was VT\_UI4. As a result, device drivers need to correctly handle both types.

Another point of difference between Windows 8 and Windows 7 is that the earlier ALS device drivers expected SENSOR\_PROPERTY\_CHANGE\_SENSITIVITY to be passed as a single value rather than as a set of values in an **IPortableDeviceValues** object.

The following pseudo code demonstrates the correct handling of possible types for SENSOR\_DATA\_TYPE\_LIGHT\_LEVEL\_LUX.

```cpp
SetLuxChangeSensitivity(PROPVARIANT var)
{
    if (var.vt == VT_UNKNOWN)
    {
        CComPtr<IPortableDeviceValues> spValues;
        PROPVARIANT entry;

        //
        // Var is a pointer to an IPortableDeviceValues
        // container. Cast and iterate through its entries.
        //

        spValues = static_cast<IPortableDeviceValues*>(pVar->punkVal);

        foreach entry in spValues
        {
            //
            // Note: omitting check for SENSOR_DATA_TYPE_LIGHT_LEVEL_LUX key
            //

            if (entry.vt == VT_R4)
            {
                //
                // VT_R4 is the expected type for
                // SENSOR_DATA_TYPE_LIGHT_LEVEL_LUX.
                // Reference entry.fltVal.
                //
            }
            else if (entry.vt == VT_UI4)
            {
                //
                // VT_UI4 is deprecated, but use it anyway.
                // Reference entry.ulVal.
                //
            }
            else
            {
                //
                // All other types are invalid.
                // Return an error accordingly.
                //
            }
        }
    }
    else if (var.vt == VT_UI4)
    {
        //
        // Top level type of VT_UI4 is deprecated for
        // SENSOR_PROPERTY_CHANGE_SENSITIVITY, but use it anyway.
        // Reference entry.ulVal.
        //
    }
    else
    {
        //
        // All other types are invalid.
        // Return an error accordingly.
        //
    }
}
```

## Related topics

[Sensor Driver Development Basics](sensor-driver-development-basics.md)



