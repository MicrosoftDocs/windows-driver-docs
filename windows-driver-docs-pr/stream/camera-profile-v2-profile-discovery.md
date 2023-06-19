---
title: Camera Profile V2 profile discovery
description: This topic provides information about Camera Profile V2 profile discovery.
ms.date: 06/08/2023
---

# Profile discovery (Camera Profile V2)

In Camera Profile 1507 schema, Profile Discovery is device centric. Meaning the application must determine first which device the application wishes to query against and enumerate the available profiles for that device.

The existing Camera Profile APIs are supported for Camera Profile V2 and the API is extended to provide additional information that the new schema supports:

```cs
[version(NTDDI_WINTHRESHOLD), uuid(ACEF81FF-99ED-4645-965E-1925CFC63834)]
[version(NTDDI_WINTHRESHOLD, Platform.WindowsPhone)]
[exclusiveto(MediaCapture)]
[contract(Windows.Foundation.UniversalApiContract, 1)]
interface IMediaCaptureStatics : IInspectable
{
    HRESULT IsVideoProfileSupported([in] HSTRING videoDeviceId, 
                                    [out, retval] boolean* value);
    HRESULT FindAllVideoProfiles([in] HSTRING videoDeviceId, 
                                 [out, retval] IVectorView<MediaCaptureVideoProfile*>** value);
    HRESULT FindConcurrentProfiles([in] HSTRING videoDeviceId, 
                                   [out, retval] IVectorView<MediaCaptureVideoProfile*>** value);
    HRESULT FindKnownVideoProfiles([in] HSTRING videoDeviceId, 
                                   [in] KnownVideoProfile name, 
                                   [out, retval] IVectorView<MediaCaptureVideoProfile*>** value);
}

```

To provide added information regarding the new Camera Profile V2, the MediaCaptureVideoProfile object is extended:

```cs
        [version(NTDDI_WINTHRESHOLD), uuid(21A073BF-A3EE-4ECF-9EF6-50B0BC4E1305)]
        [version(NTDDI_WINTHRESHOLD, Platform.WindowsPhone)]
        [exclusiveto(MediaCaptureVideoProfile)]
        [contract(Windows.Foundation.UniversalApiContract, 1)]
        interface IMediaCaptureVideoProfile : IInspectable
        {
            [propget] HRESULT Id([out, retval] HSTRING* value);
            [propget] HRESULT VideoDeviceId([out, retval]HSTRING* value);
            [propget] HRESULT SupportedPreviewMediaDescription([out, retval] IVectorView<MediaCaptureVideoProfileMediaDescription*>** value);
            [propget] HRESULT SupportedRecordMediaDescription([out, retval] IVectorView<MediaCaptureVideoProfileMediaDescription*>** value);
            [propget] HRESULT SupportedPhotoMediaDescription([out, retval] IVectorView<MediaCaptureVideoProfileMediaDescription*>** value);
            HRESULT GetConcurrency([out, retval] IVectorView<MediaCaptureVideoProfile*>** value);
        }

        API_CONTRACT_WIN10_RS4 // TDB
        [uuid(5AE36D1E-211D-474E-A763-3EDE406C2663), exclusiveto(MediaCaptureVideoProfileMediaDescription)]
        interface IMediaCaptureVideoProfileMediaDescription2 : IInspectable
        {
            [propget] HRESULT EncodingProperties([out, retval] IMediaEncodingProperties** value);
        };
        
        API_CONTRACT_WIN10_RS4 // TDB
        [uuid(085344F6-09AE-49D3-8D9A-442DE692B0E5), exclusiveto(MediaCaptureProfileStream)]
        interface IMediaCaptureProfileStream : IInspectable
        {
            [propget] HRESULT SourceInfo([out, retval] MediaFrameSourceInfo** value);
            [propget] HRESULT SupportedMediaDescription([out, retval] IVectorView<MediaCaptureVideoProfileMediaDescription*>** value);
        };

        API_CONTRACT_WIN10_RS4 // TDB
        [uuid(4CDC8BB7-4789-418E-AF12-C0CEC7442F5D), exclusiveto(MediaCaptureVideoProfile)]
        interface IMediaCaptureVideoProfile2 : IInspectable
        {
            [propget] HRESULT ProfileStreams([out, retval] IVectorView<MediaCaptureProfileStream*>** value);
        };

        [version(NTDDI_WINTHRESHOLD)]
        [version(NTDDI_WINTHRESHOLD, Platform.WindowsPhone)]
        [dualapipartition(NTDDI_WINTHRESHOLD)]
        [threading(both), marshaling_behavior(agile)]
        [contract(Windows.Foundation.UniversalApiContract, 1)]
        runtimeclass MediaCaptureVideoProfile
        {
            [default] interface IMediaCaptureVideoProfile;

            API_CONTRACT_WIN10_RS4 // TDB
            interface IMediaCaptureVideoProfile2;
        };
```

## Related articles

[Camera Profile V2 developer specification](camera-profile-v2-specification.md)
