---
title: Supporting ambient light sensors
author: windows-driver-content
description: Supporting ambient light sensors
ms.assetid: a0875084-c093-4659-91b9-375450f65234
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

```ManagedCPlusPlus
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

--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bsensors\sensors%5D:%20Supporting%20ambient%20light%20sensors%20%20RELEASE:%20%281/12/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


