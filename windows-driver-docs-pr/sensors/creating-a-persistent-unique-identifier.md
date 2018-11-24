---
title: Creating a persistent unique identifier for a sensor
description: Creating a persistent unique identifier for a sensor
ms.assetid: 09ff583e-6bb5-4812-ae3b-970dac671e39
ms.date: 07/20/2018
ms.localizationpriority: medium
---

# Creating a persistent unique identifier for a sensor


Your driver must create persistent unique identifier (PUID) for each sensor. A PUID is a GUID value that is stored across sessions and uniquely identifies the object on the device. Your driver must return the PUID value when queried for the property named SENSOR\_PROPERTY\_PERSISTENT\_UNIQUE\_ID. If a device contains multiple sensors, each sensor must be assigned its own PUID. Applications can retrieve this ID by calling the [ISensor::GetID](http://go.microsoft.com/fwlink/p/?linkid=157812) method in the Sensor API.

You should create a new PUID for each sensor, when the sensor first connects to the computer, and then store this value for later use.

Your driver should create or retrieve the PUID before the sensor class extension is initialized, for example, when it is called in [**IPnpCallbackHardware::OnPrepareHardware**](https://msdn.microsoft.com/library/windows/hardware/ff556766). This method supplies a pointer to the [IWDFDevice](https://msdn.microsoft.com/library/windows/hardware/ff556917) interface that represents the sensor. You can use this pointer to access a specific property store for each device.

The following code example creates a function that creates, stores, and retrieves a PUID, as needed.

```cpp
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
        hr = pWdfDevice->RetrieveDevicePropertyStore(NULL, WdfPropertyStoreCreateIfMissing, &spPropStore, NULL);
    }

    if(SUCCEEDED(hr))
    {
        GUID idGuid;

        PROPVARIANT vID;

        // Try to get the PUID value previously stored as a string.
        hr = spPropStore->GetNamedValue(wszSensorID, &vID);
        if (SUCCEEDED(hr))
        {
            // Convert the PUID string to a GUID.
            hr = ::CLSIDFromString(vID.bstrVal, &idGuid);
        }
        else
        {
            // There was no value in the store, so create a new value.
            hr = ::CoCreateGuid(&idGuid);

            if (SUCCEEDED(hr))
            {
                // Convert the GUID to a string.
                LPOLESTR lpszGUID = NULL;
                hr = ::StringFromCLSID(idGuid, &lpszGUID);
                if (SUCCEEDED(hr))
                {
                    // Put the new value into the property store.
                    PropVariantInit(&vID);
                    vID.vt = VT_LPWSTR;
                    vID.pwszVal = lpszGUID;
                    hr = spPropStore->SetNamedValue(wszSensorID, &vID);
                    PropVariantClear(&vID);
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



