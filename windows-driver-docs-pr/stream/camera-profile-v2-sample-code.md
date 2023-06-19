---
title: Camera Profile V2 sample code
description: This topic provides sample code for the Camera Profile V2 developer specification.
ms.date: 06/08/2023
---

# Sample code (Camera Profile V2)

The following sections contain sample code showing how the new API surfaces can be consumed. Each section describes the scenario for the sample code.

## Sample 1

A IHV/OEM provided Device MFT will need to provide a set of camera profiles supported by the underlying sensor and ISP. This is published during the Device MFT's IMFDeviceTransform::InitializeTransform() method.

The provided camera profiles must be set on the connected transform's IMFAttributes store (this is the store the pipeline queries once the pipeline is fully constructed).

This sample is typical of a case where an IHV ships a single reference driver package that enabled profiles, however, OEMs may choose to pair the camera module with different sensor modules. In such cases, because the sensors may not have the same capabilities, a runtime update of the profiles are necessary. This is done by the DMFT.

```cpp
IFACEMETHODIMP
SampleDMFT::InitializeTransform(
    _In_ IMFAttributes *pAttributes 
    )
{
    ComPtr<IMFTransform>                spTransform;
    ComPtr<IMFAttributes>               spAttributes;
    ComPtr<IMFSensorProfileCollection>  spProfileCollection;
    ComPtr<IMFSensorProfile>            spProfile;


    if (nullptr == pAttributes)
    {
        return E_INVALIDARG;
    }

    // Get the connected KSCONTROL interface, this is the 
    // IMFTransform of the up stream transform--which will
    // be the devproxy if only one DMFT is present, or
    // will be forwarded by the platform DMFT if that is
    // in between the IHV/OEM DMFT and devproxy.
    // In either case, the IHV/OEM DMFT won't need to know
    // the topology.
    RETURN_IF_FAILED (pAttributes->GetUnknown(MF_DEVICEMFT_CONNECTED_FILTER_KSCONTROL, 
                                              IID_PPV_ARGS(&spTransform)));
    RETURN_IF_FAILED (spTransform->GetAttributes(&spAttributes));

    // Create an empty profile collection...
    RETURN_IF_FAILED (MFCreateSensorProfileCollection(&spProfileCollection));

    // In this example:
    // Pin0 - Preview pin.
    // Pin1 - Capture/Record pin.
    // Pin2 - Photo pin.
    // Pin3 - IR pin.
    // 
    // Legacy profile is mandatory.  This is to ensure non-profile
    // aware applications can still function, but with degraded
    // feature sets.
    RETURN_IF_FAILED (MFCreateSensorProfile(KSCAMERAPROFILE_Legacy, 0, nullptr, 
                                            spProfile.ReleaseAndGetAddressOf()));
    RETURN_IF_FAILED (spProfile->AddProfileFilter(0, L"((RES==;FRT<=30,1;SUT==))"));
    RETURN_IF_FAILED (spProfile->AddProfileFilter(1, L"((RES==;FRT<=30,1;SUT==))"));
    RETURN_IF_FAILED (spProfile->AddProfileFilter(2, L"((RES==;FRT<=30,1;SUT==))"));
    RETURN_IF_FAILED (spProfile->AddProfileFilter(3, L"((RES==;FRT<=30,1;SUT==))"));
    RETURN_IF_FAILED (spProfileCollection->AddProfile(spProfile));

    // High Frame Rate profile will only allow preview & record/capture pin.
    RETURN_IF_FAILED (MFCreateSensorProfile(KSCAMERAPROFILE_HighFrameRate, 0, nullptr, 
                                            spProfile.ReleaseAndGetAddressOf()));
    RETURN_IF_FAILED (spProfile->AddProfileFilter(0, L"((RES==;FRT==;SUT==))"));
    RETURN_IF_FAILED (spProfile->AddProfileFilter(1, L"((RES==;FRT>=60,1;SUT==))"));
    RETURN_IF_FAILED (spProfile->AddProfileFilter(2, L"(!)"));
    RETURN_IF_FAILED (spProfile->AddProfileFilter(3, L"(!)"));
    RETURN_IF_FAILED (spProfileCollection->AddProfile(spProfile));

    // HighQualityPhoto profile will only allow preview and photo pin.
    RETURN_IF_FAILED (MFCreateSensorProfile(KSCAMERAPROFILE_HighQualityPhoto, 0, nullptr, 
                                            spProfile.ReleaseAndGetAddressOf()));
    RETURN_IF_FAILED (spProfile->AddProfileFilter(0, L"((RES==;FRT==;SUT==))"));
    RETURN_IF_FAILED (spProfile->AddProfileFilter(1, L"(!)"));
    RETURN_IF_FAILED (spProfile->AddProfileFilter(2, L"((RES==;FRT==;SUT==))"));
    RETURN_IF_FAILED (spProfile->AddProfileFilter(3, L"(!)"));
    RETURN_IF_FAILED (spProfileCollection->AddProfile(spProfile));

    // Face auth only allows 720p@30fps from preview and any from IR pin.
    RETURN_IF_FAILED (MFCreateSensorProfile(KSCAMERAPROFILE_FaceAuth_Mode, 0, nullptr, 
                                            spProfile.ReleaseAndGetAddressOf()));
    RETURN_IF_FAILED (spProfile->AddProfileFilter(0, L"((RES==1280,720;FRT==30,1;SUT==))"));
    RETURN_IF_FAILED (spProfile->AddProfileFilter(1, L"(!)"));
    RETURN_IF_FAILED (spProfile->AddProfileFilter(2, L"(!)"));
    RETURN_IF_FAILED (spProfile->AddProfileFilter(3, L"((RES==;FRT==;SUT==))"));
    RETURN_IF_FAILED (spProfileCollection->AddProfile(spProfile));


    // Se the profile collection to the attribute store of the IMFTransform.
    RETURN_IF_FAILED (spAttributes->SetUnknown(MF_DEVICEMFT_SENSORPROFILE_COLLECTION, 
                                               spProfileCollection));

    // ... Rest of the InitializeTransform logic...
}

```

## Sample 2

In this scenario, we assume the IHV/OEM provided a Sensor Group Transform (SGT), which synthesizes media flow from multiple physical devices. We'll also assume that the IHV provided a single reference implementation for their camera drivers for each of the physical devices (possibly sourced from different vendors), but the OEM (or a different IHV) has chosen to pair the camera driver with different sensors and/or ISP.

This results in some of the capabilities declared by the reference implementation to be no longer valid. The SGT will update/remove profiles provided to more accurately describe the underlying hardware's capabilities.

The sample below is the implementation of IMFSensorTransformFactory::InitializeFactory method. This is implemented by an IHV/OEM who produces the driver package for the camera subsystem.

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

    // ... Rest of the InitializeFactory logic...
}

```

## Sample 3

Based on the selected profile for a particular device, determine which media type from that device is supported/not supported for the profile using the IMFSensorStream information.

This sample is supplied to illustrate how the profile can be consumed at the client space when using Win32 API directly. The WinRT API already implements this logic when consumed through the CameraProfile APIs.

```cpp
HRESULT
CheckMediaTypesOnPin(
    _In_z_ LPCWSTR deviceSymbolicName,
    _In_ UINT32 pinId,
    _In_ SENSORPROFILEID* profileId,
    _COM_Outptr_ IMFCollection** mediaTypeCollection
    )
{
    HRESULT hr = S_OK;
    ComPtr<IMFCollection> collection;
    ComPtr<IMFSensorGroup> sensorGroup;
    ComPtr<IMFGetService> service;
    ComPtr<IMFSensorProfileCollection> profileCollection;
    ComPtr<IMFSensorProfile> profile;
    ComPtr<IMFSensorStream> sensorStream;
    DWORD deviceCount = 0;
    DWORD streamCount = 0;
    DWORD mediaTypeCount = 0;

    // Validate in params.
    if (nullptr == deviceSymbolicName || nullptr == profileId)
    {
        return E_INVALIDARG;
    }
    if (pinId == (UINT32)-1)
    {
        return MF_E_INVALIDSTREAMNUMBER;
    }
    if (nullptr == mediaTypeCollection)
    {
        return E_POINTER;
    }
    *mediaTypeCollection = nullptr;

    RETURN_IF_FAILED (MFCreateCollection(collection.ReleaseAndGetAddressOf()));

    // Create the SensorGroup for our device name.  This device name
    // can be a single physical device name or it can be a multi-device
    // group of devices.  In either case, MFCreateSensorGroup will create
    // a non-activated snapshot of the device(s).
    RETURN_IF_FAILED (MFCreateSensorGroup(deviceSymbolicName, &sensorGroup));
    RETURN_IF_FAILED (sensorGroup.As(service.ReleaseAndGetAddressOf()));

    // Now check if they have a profile collection.
    RETURN_IF_FAILED (service->GetService(GUID_NULL, 
                          IID_PPV_ARGS(profileCollection.ReleaseAndGetAddressOf())));

    if (profileCollection->GetProfileCount() != 0)
    {
        // If they published profiles, but we can't find the specific
        // profile, it means this camera doesn't support that scenario
        // so we should return an empty collection of media types to
        // indicate no support.
        if (FAILED(profileCollection->FindProfile(profileId, 
                       profile.ReleaseAndGetAddressOf())))
        {
            *mediaTypeCollection = collection.Detach();
            return S_OK;
        }
    }

    // If profiles are not supported, then ALL media types are
    // supported.  And we can indicate that by keeping the
    // profile null.  So we have to walk the sensor stream
    // but that means we have to find the sensor stream for
    // the pinId.
    RETURN_IF_FAILED (sensorGroup->GetSensorDeviceCount(&deviceCount));
    for (DWORD deviceIdx = 0; deviceIdx < deviceCount && 
                              sensorStream.Get() == nullptr; deviceIdx++)
    {
        RETURN_IF_FAILED (sensorGroup->GetSensorDevice(deviceIdx, 
                              sensorDevice.ReleaseAndGetAddressOf()));

        RETURN_IF_FAILED (sensorDevice->GetStreamAttributesCount(MFSensorStreamType_Output, 
                              &streamCount));
        
        for (DWORD streamIdx = 0; streamIdx < streamCount; streamIdx++)
        {
            RETURN_IF_FAILED (sensorDevice->GetStreamAttributes(
                                  MFSensorStreamType_Output, 
                                  streamIdx, 
                                  &streamAttributes));

            if (MFGetAttributesUINT32(streamAttributes, 
                                      MF_DEVICESTREAM_STREAM_ID, 
                                      (UINT32) -1) == pinId)
            {
                RETURN_IF_FAILED (streamAttributes.As(sensorStream.ReleaseAndGetAddressOf()));
                break;
            }
        }
    }

    // If we didn't find a sensorStream for the PinId, then we
    // were given bad data....
    if (sensorStream.Get() == nullptr)
    {
        return MF_E_INVALIDSTREAMNUMBER;
    }
    RETURN_IF_FAILED (sensorStream->GetMediaTypeCount(&mediaTypeCount));
    for (DWORD mediaTypeIdx = 0; mediaTypeIdx < mediaTypeCount; mediaTypeIdx++)
    {
        ComPtr<IMFMediaType> mediaType;

        RETURN_IF_FAILED (sensorStream->GetMediaType(mediaTypeIdx, 
                                                     mediaType.ReleaseAndGetAddressOf()));
        if (profile.Get() != nullptr)
        {
            BOOL supported = FALSE;

            RETURN_IF_FAILED (profile->IsMediaTypeSupported(pinId, 
                                                            mediaType.Get(),
                                                             &supported));
            if (supported)
            {
                RETURN_IF_FAILED (collection->AddElement(mediaType.Get()));
            }
        }
        else
        {
            RETURN_IF_FAILED (collection->AddElement(mediaType.Get()));
        }
    }

    *mediaTypeCollection = collection.Detach();

    return S_OK;
}

```

## Related articles

[Camera Profile V2 developer specification](camera-profile-v2-specification.md)
