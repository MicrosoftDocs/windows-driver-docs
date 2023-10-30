---
title: Camera Profile V2 interfaces and interactions
description: This topic provides information about the Camera Profile V2 interfaces and interactions.
ms.date: 06/08/2023
---

# Interfaces and interactions (Camera Profile V2)

Depending on your feature, consider each of below and describe if relevant.

## Public API added or changed (Win32)

### SENSORPROFILEID

SENSORPROFILEID structure represents a unique ID for each profile. It is comprised of the Profile Type KSCAMERAPROFILE\_\* declared in OEMCameraProfileVersion (see [Detailed design for IHVs and OEMs](camera-profile-v2-detailed-design-for-ihvs-and-oems.md)) and a Profile Index.

```cpp
typedef struct
{
    GUID    Type;
    UINT32  Index;
    UINT32  Unused;
} SENSORPROFILEID;

```

### IMFSensorProfileCollection

IMFSensorProfileCollection represents a collection of profiles. IHV/OEMs must use the MFCreateSensorProfileCollection API to obtain a new profile collection interface.

```cs
[
    object,
    uuid(C95EA55B-0187-48BE-9353-8D2507662351),
    helpstring("IMFSensorProfileCollection Interface"),
    local
]
interface IMFSensorProfileCollection : IUnknown
{
    DWORD GetProfileCount(
        );

    HRESULT GetProfile(
        [in, annotation("_In_")] DWORD Index,
        [out, annotation("_COM_Outptr_")] IMFSensorProfile** ppProfile
        );

    HRESULT AddProfile(
        [in, annotation("_In_")] IMFSensorProfile* pProfile
        );

    HRESULT FindProfile(
        [in, annotation("_In_")] SENSORPROFILEID* ProfileId, 
        [out, annotation("_COM_Outptr_")] IMFSensorProfile** ppProfile
        );

    void RemoveProfileByIndex(
        [in, annotation("_In_")] DWORD Index
        );

    void RemoveProfile(
        [in, annotation("_In_")] SENSORPROFILEID* ProfileId
        );
 };

STDAPI
MFCreateSensorProfileCollection(
    _COM_Outptr_ IMFSensorProfileCollection** ppSensorProfile
    );
```

### IMFSensorProfile

The IMFSensorProfile object also implements the IMFAttributes interface. The attribute store is read-only for the application developers but read/write for the DMFT/Sensor Group Transform component.

```cs
[
    object,
    uuid(22F765D1-8DAB-4107-846D-56BAF72215E7),
    helpstring("IMFSensorProfile Interface"),
    local
]
interface IMFSensorProfile : IUnknown
{
    HRESULT GetProfileId(
        [out, annotation("_Out_")] SENSORPROFILEID* pId
        );

    HRESULT AddProfileFilter(
        [in, annotation("_In_")] UINT32 StreamId, 
        [in, annotation("_In_z_")] LPCWSTR wzFilterSetString
        );

    HRESULT IsMediaTypeSupported(
        [in, annotation("_In_")] UINT32 StreamId, 
        [in, annotation("_In_")] IMFMediaType* pMediaType, 
        [out, annotation("_Out_")] BOOL* pfSupported
        );

    HRESULT AddBlockedControl(
        [in, annotation("_In_z_")] LPCWSTR wzBlockedControl
        );
 };

STDAPI
MFCreateSensorProfile(
    _In_ REFGUID ProfileType,
    _In_ UINT32 ProfileIndex,
    _In_opt_z_ LPCWSTR Constraints,
    _COM_Outptr_ IMFSensorProfile** ppProfile
    );

```

## Public API added or changed (WinRT)

```cs
[contract(Windows.Foundation.UniversalApiContract, 1)]
typedef enum KnownVideoProfile
{
    VideoRecording = 0,
    HighQualityPhoto,
    BalancedVideoAndPhoto,
    VideoConferencing,
    PhotoSequence
    PhotoSequence,
    
    [contract(Windows.Foundation.UniversalApiContract, 6)]
    HighFrameRate,
    [contract(Windows.Foundation.UniversalApiContract, 6)]
    VariablePhotoSequence
    [contract(Windows.Foundation.UniversalApiContract, 6)]
    HDRWithWCGVideo,
    [contract(Windows.Foundation.UniversalApiContract, 6)]
    HDRWithWCGPhoto,
    [contract(Windows.Foundation.UniversalApiContract, 6)]
    VideoHDR8
    
} KnownVideoProfile;


[uuid(8012AFEF-B691-49FF-83F2-C1E76EAAEA1B)]
[exclusiveto(MediaCaptureVideoProfileMediaDescription)]
[contract(Windows.Foundation.UniversalApiContract, 1)]
interface IMediaCaptureVideoProfileMediaDescription : IInspectable
{
    [propget] HRESULT Width([out, retval] UINT32* value);
    [propget] HRESULT Height([out, retval] UINT32* value);
    [propget] HRESULT FrameRate([out, retval] double* value);
    
    [deprecated("IsVariablePhotoSequenceSupported might not be available in future versions of Windows. Starting with Windows RS4", deprecate, Windows.Foundation.UniversalApiContract, 6)]
    [propget] HRESULT IsVariablePhotoSequenceSupported([out, retval] boolean* value);

    [deprecated("IsHdrVideoSupported might not be available in future versions of Windows. Starting with Windows RS4", deprecate, Windows.Foundation.UniversalApiContract, 6)]
    [propget] HRESULT IsHdrVideoSupported([out, retval] boolean* value);
}

[uuid(C6A6EF13-322D-413A-B85A-68A88E02F4E9)]
[contract(Windows.Foundation.UniversalApiContract, 6)]
[exclusiveto(MediaCaptureVideoProfileMediaDescription)]
interface IMediaCaptureVideoProfileMediaDescription2 : IInspectable
{
    [propget] HRESULT Subtype([out, retval] HSTRING* value);
    [propget] HRESULT Properties([out, retval] Windows.Foundation.Collections.IMapView<GUID, IInspectable*>** value);
}


[uuid(97DDC95F-94CE-468F-9316-FC5BC2638F6B)]
[contract(Windows.Foundation.UniversalApiContract, 6)]
[exclusiveto(MediaCaptureVideoProfile)]
interface IMediaCaptureVideoProfile2 : IInspectable
{
    [propget] HRESULT FrameSourceInfos([out, retval] IVectorView<Windows.Media.Capture.Frames.MediaFrameSourceInfo*>** value);
    [propget] HRESULT Properties([out, retval] Windows.Foundation.Collections.IMapView<GUID, IInspectable*>** value);
}

[uuid(195A7855-6457-42C6-A769-19B65BD32E6E)]
[contract(Windows.Foundation.UniversalApiContract, 6)]
[exclusiveto(MediaFrameSourceInfo)]
interface IMediaFrameSourceInfo2 : IInspectable
{
    [propget] HRESULT ProfileId(
    [out, retval] HSTRING* value);
    
    [propget] HRESULT VideoProfileMediaDescription(
    [out, retval] Windows.Foundation.Collections.IVectorView<Windows.Media.Capture.MediaCaptureVideoProfileMediaDescription*>** value);
}

RUNTIMECLASS_CONTRACT_WIN10_RS1
runtimeclass MediaFrameSourceInfo
{
    [default] interface IMediaFrameSourceInfo;
    
    [contract(Windows.Foundation.UniversalApiContract, 6)]
    interface IMediaFrameSourceInfo2;
}

```

## Related articles

[Camera Profile V2 developer specification](camera-profile-v2-specification.md)
