---
title: Creating a persistent unique identifier for a sensor
author: windows-driver-content
description: Creating a persistent unique identifier for a sensor
ms.assetid: 09ff583e-6bb5-4812-ae3b-970dac671e39
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Creating a persistent unique identifier for a sensor


Your driver must create persistent unique identifier (PUID) for each sensor. A PUID is a GUID value that is stored across sessions and uniquely identifies the object on the device. Your driver must return the PUID value when queried for the property named SENSOR\_PROPERTY\_PERSISTENT\_UNIQUE\_ID. If a device contains multiple sensors, each sensor must be assigned its own PUID. Applications can retrieve this ID by calling the [ISensor::GetID](http://go.microsoft.com/fwlink/p/?linkid=157812) method in the Sensor API.

You should create a new PUID for each sensor, when the sensor first connects to the computer, and then store this value for later use.

Your driver should create or retrieve the PUID before the sensor class extension is initialized, for example, when it is called in [**IPnpCallbackHardware::OnPrepareHardware**](https://msdn.microsoft.com/library/windows/hardware/ff556766). This method supplies a pointer to the [IWDFDevice](https://msdn.microsoft.com/library/windows/hardware/ff556917) interface that represents the sensor. You can use this pointer to access a specific property store for each device.

The following code example creates a function that creates, stores, and retrieves a PUID, as needed.

```
// Sets the persistent unique ID property in the WDF property store
// and returns the GUID for use in PortableDeviceValues property bags.
HRESULT CMyDevice::GetUniqueID(__in IWDFDevice* pWdfDevice, 
                                            __in LPCWSTR wszSensorID, __out GUID* puid)
{
    HRESULT hr = S_OK;

    // Smart pointer to the WDF property store.
    // This pointer can store or retrieve the ID.
    CComPtr<IWDFNamedPropertyStore> spPropStore;
    if (SUCCEEDED(hr))
    {
        // Create the property store for this device or
        // retrieve the existing one.
        hr = pWdfDevice->RetrieveDevicePropertyStore(NULL, WdfPropertyStoreCreateIfMissing, &amp;spPropStore, NULL);
    }

    if(SUCCEEDED(hr))
    {
        GUID idGuid;
 
        PROPVARIANT vID;

        // Try to get the PUID value previously stored as a string.
        hr = spPropStore->GetNamedValue(wszSensorID, &amp;vID);
        if (SUCCEEDED(hr))
        {
            // Convert the PUID string to a GUID.
            hr = ::CLSIDFromString(vID.bstrVal, &amp;idGuid);
        }
        else
        {
            // There was no value in the store, so create a new value.
            hr = ::CoCreateGuid(&amp;idGuid);

            if (SUCCEEDED(hr))
            {
                // Convert the GUID to a string.
                LPOLESTR lpszGUID = NULL;
                hr = ::StringFromCLSID(idGuid, &amp;lpszGUID);
                if (SUCCEEDED(hr))
                {
                    // Put the new value into the property store.
                    PropVariantInit(&amp;vID);
                    vID.vt = VT_LPWSTR;
                    vID.pwszVal = lpszGUID;
                    hr = spPropStore->SetNamedValue(wszSensorID, &amp;vID);
                    PropVariantClear(&amp;vID);
                }
            }
        }

        // Return the PUID GUID.
        *puid = idGuid;
    }

    return hr;
}
```

## Related topics
[The Sensors Geolocation Driver Sample](https://msdn.microsoft.com/library/windows/hardware/hh768273)  

--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bsensors\sensors%5D:%20Creating%20a%20persistent%20unique%20identifier%20for%20a%20sensor%20%20RELEASE:%20%281/12/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


