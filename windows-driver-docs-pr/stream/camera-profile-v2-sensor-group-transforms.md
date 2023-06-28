---
title: Camera Profile V2 sensor group transforms
description: This article provides information about the Camera Profile V2 sensor group transforms (SGT).
ms.date: 06/08/2023
---

# Sensor group transforms (Camera Profile V2)

Sensor group transforms may publish Camera Profiles using a similar mechanism as DMFT. The MF_DEVICEMFT_SENSORPROFILE_COLLECTION attribute may be published through the IMFAttributes parameter from the IMFSensorTransformFactory::GetTransformInformation for each of the supported sensor group transforms (SGT).

During the IMFSensorTransformFactory::InitializeFactory call, a collection of IMSensorDevice interfaces will be provided, SGT Factory may alter the available Camera Profiles from the available devices by QI-ing the IMFSensorDevice interface for the IMFGetService interface. From this interface, the SGT Factory may request the IMFSensorProfileCollection interface.

SGT Factory may then add/remove/update the available Camera Profiles for each IMFSensorDevice if the SGT Factory chooses to do so. The modified Camera Profiles will only be persisted for the sensor group that contains the SGT. The Camera Profiles for the individual devices won't be modified with the new information.

## Sample sensor group transform

```cpp
IFACEMETHODIMP
SampleSensorTransformFactory::InitializeFactory(
    _In_ DWORD dwMaxTransformCount, 
    _In_ IMFCollection* sensorDevices, 
    _In_opt_ IMFAttributes* pAttributes 
    )
{
    DWORD sensorDeviceCount = 0;
    ComPtr<IUnknown> unknown;

    if (nullptr == sensorDevices)
    {
        return E_INVALIDARG;
    }

    // For this example, the IHV/OEM added a SGT to a multi-camera
    // setup.  And the SGT is responsible for updating the profile
    // information available from each of the physical cameras, and
    // leave it's own profile as "blank".  This has the net effect
    // of having the SGT support any profile the physical devices
    // expose.
    RETURN_IF_FAILED (sensorDevices->GetElementCount(&sensorDeviceCount));
    for (DWORD idx = 0; idx < sensorDeviceCount; idx++)
    {
        ComPtr<IMFGetService> service;
        ComPtr<IMFSensorProfileCollection> profileCollection;
        SENSORPROFILEID sensorProfileId;

        RETURN_IF_FAILED (sensorDevices->GetElement(idx, 
                              unknown.ReleaseAndGetAddressOf()));
        RETURN_IF_FAILED (unknown.As(service.ReleaseAndGetAddressOf()));
        RETURN_IF_FAILED (service->GetService(GUID_NULL, 
                              ID_PPV_ARGS(profileCollection.ReleaseAndGetAddressOf())));

        // Let's assume that for this ISP/sensor, we cannot support
        // photo sequence but our reference driver published a single
        // photo sequence profile whose ID is hardcoded to a static
        // variable s_PhotoSequenceProfileId.
        RETURN_IF_FAILED (profileCollection->RemoveProfile(&s_PhotoSequenceProfileId));

        // Let's also assume this is a low cost ISP/sensor so our driver
        // cannot support Video HDR (VHDR) control for high frame rate
        // recording and our reference implementation published multiple
        // high frame rate recording profile.
        // 
        // Also for this combination of ISP/sensor, we cannot support
        // Face Auth (IR doesn't support alternate illumination option).
        // So we need to remove all Face Auth from our collection.
        for (DWORD profileIdx = 0; 
                   profileIdx < profileCollection->GetProfileCount();)
        {
            ComPtr<IMFSensorProfile> profile;

            RETURN_IF_FAILED (profileCollection->GetProfile(profileIdx, 
                                  profile.ReleaseAndGetAddressOf()));

            RETURN_IF_FAILED (profile->GetProfileId(&profileId));
            if (profileId.Type == KSCAMERAPROFILE_HighFrameRate)
            {
                RETURN_IF_FAILED (profile->AddBlockedControl(L"VHDR"));
            }
            if (profileId.Type == KSCAMERAPROFILE_FaceAuth_Mode)
            {
                RETURN_IF_FAILED (profileCollection->RemoveProfileByIndex(profileIdx));
            }
            else
            {
                profileIdx++;
            }
        }
    }

    // Set the profile collection to the attribute store that will be returned when
    // IMFSensorTransformFactory::GetTransformInformation is called.
    RETURN_IF_FAILED (m_spAttributes->SetUnknown(MF_DEVICEMFT_SENSORPROFILE_COLLECTION, 
                                                 spProfileCollection));

    // ... Rest of the InitializeFactory logic...
}
```

## Related articles

[Camera Profile V2 developer specification](camera-profile-v2-specification.md)
