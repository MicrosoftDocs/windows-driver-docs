---
title: Background segmentation shallow focus mode and eye gaze stare mode driver sample
description: Provides an example implementation of background segmentation shallow focus mode and eye gaze stare mode controls in a camera driver.
ms.date: 05/16/2022
---

# Background segmentation shallow focus mode and eye gaze stare mode driver sample

This is an example implementation of background segmentation shallow focus mode and eye gaze stare mode, two new bit fields being introduced in Windows 11, version 22H2.

These controls are typically implemented in C++, as part of the user mode extension of an Avstream camera driver in Device MFT.

> [!NOTE]
> The [EyeGazeAndBackgroundSegmentation](https://github.com/microsoft/Windows-Camera/tree/master/Samples/ExtendedControlAndMetadata/EyeGazeAndBackgroundSegmentation) C# UWP application sample on GitHub previews a camera and interacts with its extended controls.

## SampleMFT.h

```cpp
Class CSampleMFT //Snipped from SampleDeviceMFT Implementation
{
...
Private:
...
    VOID SetBackgroundSegmentationShallowFocus(BOOLEAN enabled)
    {
        m_backgroundSegmentationShallowFocusEnabled = enabled;
    }
    BOOLEAN GetBackgroundSegmentationShallowFocus()
    {
        return m_backgroundSegmentationShallowFocusEnabled;
    }
    constexpr ULONGLONG SupportedBackgroundSegmentation()
    {
        return  KSCAMERA_EXTENDEDPROP_BACKGROUNDSEGMENTATION_BLUR |
                KSCAMERA_EXTENDEDPROP_BACKGROUNDSEGMENTATION_MASK |
                KSCAMERA_EXTENDEDPROP_BACKGROUNDSEGMENTATION_SHALLOWFOCUS;
    }

    VOID SetEyeGazeCorrectionMode(DWORD flags)
    {
        m_eyeGazeCorrectionMode = flags;
    }
    DWORD GetEyeGazeCorrectionMode()
    {
        return m_eyeGazeCorrectionMode;
    }
    BOOLEAN m_backgroundSegmentationShallowFocusEnabled;
    DWORD m_eyeGazeCorrectionMode;
};
```

## SampleMFT.cpp

```cpp
// KSCAMERA_EXTENDEDPROP_BACKGROUNDSEGMENTATION_SHALLOWFOCUS
HRESULT CSampleMft::BackgroundSegmentationHandler(
    _In_ PKSPROPERTY property,
    _In_ LPVOID data,
    _In_ ULONG outputBufferLength,
    _Inout_ PULONG bytesReturned)
{
    *bytesReturned = 0;
    if (property->Flags & KSPROPERTY_TYPE_SET)
    {
        if (outputBufferLength == 0)
        {
            *bytesReturned = sizeof(KSCAMERA_EXTENDEDPROP_HEADER) + sizeof(KSCAMERA_EXTENDEDPROP_VALUE);
            RETURN_IF_FAILED(HRESULT_FROM_WIN32(ERROR_MORE_DATA));
        }
        else if (outputBufferLength < sizeof(KSCAMERA_EXTENDEDPROP_HEADER) + sizeof(KSCAMERA_EXTENDEDPROP_VALUE))
        {
            RETURN_IF_FAILED(HRESULT_FROM_WIN32(ERROR_MORE_DATA));
        }
        else if (data && outputBufferLength >= sizeof(KSCAMERA_EXTENDEDPROP_HEADER) + sizeof(KSCAMERA_EXTENDEDPROP_VALUE))
        {
            PBYTE payload = (PBYTE)data;
            PKSCAMERA_EXTENDEDPROP_HEADER extendedHeader = (PKSCAMERA_EXTENDEDPROP_HEADER)payload;
            // The extended value is unused for SET with this control, only flags are expected
            PKSCAMERA_EXTENDEDPROP_VALUE extendedValue = (PKSCAMERA_EXTENDEDPROP_VALUE)(payload + sizeof(KSCAMERA_EXTENDEDPROP_HEADER));
            if (extendedHeader->Flags & ~SupportedBackgroundSegmentation())
            {
                RETURN_HR(E_INVALIDARG);
            }

            bool shallowFocus = WI_IsFlagSet((extendedHeader->Flags, KSCAMERA_EXTENDEDPROP_BACKGROUNDSEGMENTATION_SHALLOWFOCUS);
            bool blur = WI_IsFlagSet((extendedHeader->Flags, KSCAMERA_EXTENDEDPROP_BACKGROUNDSEGMENTATION_BLUR);
            bool mask = WI_IsFlagSet((extendedHeader->Flags, KSCAMERA_EXTENDEDPROP_BACKGROUNDSEGMENTATION_MASK);

            // If you ask for shallow focus, you must also ask for blur.
            if (shallowFocus && !blur)
            {
                RETURN_HR(E_INVALIDARG);
            }
            SetBackgroundSegmentationShallowFocus(shallowFocus);
            SetBackgroundSegmentationBlur(blur);
            SetBackgroundSegmentationMask(mask);
        }
        else
        {
            RETURN_IF_FAILED(E_INVALIDARG);
        }
    }
    else if (property->Flags & KSPROPERTY_TYPE_GET)
    {
        if (outputBufferLength == 0)
        {
            *bytesReturned = sizeof(KSCAMERA_EXTENDEDPROP_HEADER) + sizeof(m_configCaps);
            RETURN_IF_FAILED(HRESULT_FROM_WIN32(ERROR_MORE_DATA));
        }
        else if (outputBufferLength < sizeof(KSCAMERA_EXTENDEDPROP_HEADER) + sizeof(m_configCaps))
        {
            RETURN_IF_FAILED(HRESULT_FROM_WIN32(ERROR_MORE_DATA));
        }
        else if (data && outputBufferLength >= sizeof(KSCAMERA_EXTENDEDPROP_HEADER) + sizeof(m_configCaps))
        {
            PBYTE payload = (PBYTE)data;
            PKSCAMERA_EXTENDEDPROP_HEADER extendedHeader = (PKSCAMERA_EXTENDEDPROP_HEADER)(payload);
            extendedHeader->Capability = KSCAMERA_EXTENDEDPROP_BACKGROUNDSEGMENTATION_MASK |
                                         KSCAMERA_EXTENDEDPROP_BACKGROUNDSEGMENTATION_BLUR |
                                         KSCAMERA_EXTENDEDPROP_BACKGROUNDSEGMENTATION_SHALLOWFOCUS |
                                         KSCAMERA_EXTENDEDPROP_BACKGROUNDSEGMENTATION_OFF;

            if (GetBackgroundSegmentationMask())
            {
                extendedHeader->Flags |= KSCAMERA_EXTENDEDPROP_BACKGROUNDSEGMENTATION_MASK;
            }

            if (GetBackgroundSegmentationBlur())
            {
                extendedHeader->Flags |= KSCAMERA_EXTENDEDPROP_BACKGROUNDSEGMENTATION_BLUR;
            }
            else if (GetBackgroundSegmentationShallowFocus())
            {
                extendedHeader->Flags |= KSCAMERA_EXTENDEDPROP_BACKGROUNDSEGMENTATION_BLUR | KSCAMERA_EXTENDEDPROP_BACKGROUNDSEGMENTATION_SHALLOWFOCUS;
            }
            else
            {
                extendedHeader->Flags = KSCAMERA_EXTENDEDPROP_BACKGROUNDSEGMENTATION_OFF;
            }
            extendedHeader->Result = 0;
            extendedHeader->Size = sizeof(KSCAMERA_EXTENDEDPROP_HEADER) + sizeof(m_configCaps);
            extendedHeader->Version = 1;
            
            PKSCAMERA_EXTENDEDPROP_BACKGROUNDSEGMENTATION_CONFIGCAPS configCap = (PKSCAMERA_EXTENDEDPROP_BACKGROUNDSEGMENTATION_CONFIGCAPS)( payload + sizeof(KSCAMERA_EXTENDEDPROP_HEADER)));
            memcpy(configCap, m_configCaps, sizeof(m_configCaps));
            *bytesReturned = sizeof(KSCAMERA_EXTENDEDPROP_HEADER) + sizeof(m_configCaps);
        }
    }

    return S_OK;
}

// KSCAMERA_EXTENDEDPROP_EYEGAZECORRECTION_STARE 
HRESULT CSampleMft::EyeGazeCorrectionHandler(   
    _In_       PKSPROPERTY property,   
    _In_       LPVOID      data,   
    _In_       ULONG       outputBufferLength,   
    _Inout_    PULONG      bytesReturned   
)   
{   
    HRESULT hr = S_OK;   
    *bytesReturned = 0;   

    if (property->Flags & KSPROPERTY_TYPE_SET)   
    {   
        if (outputBufferLength == 0) 
        {   
            *bytesReturned = sizeof(KSCAMERA_EXTENDEDPROP_HEADER) + sizeof(KSCAMERA_EXTENDEDPROP_VALUE);   
            RETURN_IF_FAILED(HRESULT_FROM_WIN32(ERROR_MORE_DATA));   
        }   
        else if (outputBufferLength < sizeof(KSCAMERA_EXTENDEDPROP_HEADER) + sizeof(KSCAMERA_EXTENDEDPROP_VALUE))   
        {   
            RETURN_IF_FAILED(HRESULT_FROM_WIN32(ERROR_MORE_DATA));   
        }   
        else if (data && outputBufferLength >= sizeof(KSCAMERA_EXTENDEDPROP_HEADER) + sizeof(KSCAMERA_EXTENDEDPROP_VALUE))   
        {   
            PBYTE payload = (PBYTE)data;   
            PKSCAMERA_EXTENDEDPROP_HEADER extendedHeader = (PKSCAMERA_EXTENDEDPROP_HEADER)payload;   
            //   
            // Use the extended value to make changes to the property.. refer documentation   
            // PKSCAMERA_EXTENDEDPROP_VALUE extendedValue = (PKSCAMERA_EXTENDEDPROP_VALUE)(payload + sizeof(KSCAMERA_EXTENDEDPROP_HEADER));   
            //
            if ( (extendedHeader->Flags == KSCAMERA_EXTENDEDPROP_EYEGAZECORRECTION_ON) ||
                 (extendedHeader->Flags == (KSCAMERA_EXTENDEDPROP_EYEGAZECORRECTION_ON | KSCAMERA_EXTENDEDPROP_EYEGAZECORRECTION_STAREMODE)) ||
                 (extendedHeader->Flags == KSCAMERA_EXTENDEDPROP_EYEGAZECORRECTION_OFF) )
            {
                SetEyeGazeCorrectionMode (extendedHeader->Flags);   
            }
            else
            {
                RETURN_HR(E_INVALIDARG);
            } 
            *bytesReturned = sizeof(PKSCAMERA_EXTENDEDPROP_HEADER) + sizeof(KSCAMERA_EXTENDEDPROP_VALUE);   
        }   
        else  
        {  
            RETURN_IF_FAILED(E_INVALIDARG);  
        }  
    }   
    else if (property->Flags & KSPROPERTY_TYPE_GET)   
    {   
        if (outputBufferLength == 0)   
        {   
            *bytesReturned = sizeof(KSCAMERA_EXTENDEDPROP_HEADER) + sizeof(KSCAMERA_EXTENDEDPROP_VALUE);   
            RETURN_IF_FAILED(HRESULT_FROM_WIN32(ERROR_MORE_DATA));  
        }   
        else if (outputBufferLength < sizeof(KSCAMERA_EXTENDEDPROP_HEADER) + sizeof(KSCAMERA_EXTENDEDPROP_VALUE)) 
        {   
            RETURN_IF_FAILED(HRESULT_FROM_WIN32(ERROR_MORE_DATA));  
        }   
        else if (data && outputBufferLength >= sizeof(KSCAMERA_EXTENDEDPROP_HEADER) + sizeof(KSCAMERA_EXTENDEDPROP_VALUE))   
        {         
            PBYTE payload = (PBYTE)data;   
            PKSCAMERA_EXTENDEDPROP_HEADER extendedHeader = (PKSCAMERA_EXTENDEDPROP_HEADER)(payload);   
            //   
            // Use the extended value to make changes to the property.. refer documentation   
            // PKSCAMERA_EXTENDEDPROP_VALUE extendedValue = (PKSCAMERA_EXTENDEDPROP_VALUE)(payload +sizeof(KSCAMERA_EXTENDEDPROP_HEADER));   
            //   
            extendedHeader->Capability = KSCAMERA_EXTENDEDPROP_EYEGAZECORRECTION_OFF |  
                                         KSCAMERA_EXTENDEDPROP_EYEGAZECORRECTION_ON |   
                                         KSCAMERA_EXTENDEDPROP_EYEGAZECORRECTION_STAREMODE;   

            extendedHeader->Flags = GetEyeGazeCorrectionMode();
            extendedHeader->Result = 0;   
            extendedHeader->Size = sizeof(KSCAMERA_EXTENDEDPROP_HEADER) + sizeof(KSCAMERA_EXTENDEDPROP_VALUE);   
            extendedHeader->Version = 1;   

            *bytesReturned = sizeof(KSCAMERA_EXTENDEDPROP_HEADER) + sizeof(KSCAMERA_EXTENDEDPROP_VALUE);   
        }   
    }   
    return S_OK;   
}
```

## See also

[KSPROPERTY_CAMERACONTROL_EXTENDED_BACKGROUNDSEGMENTATION](ksproperty-cameracontrol-extended-backgroundsegmentation.md)

[KSPROPERTY_CAMERACONTROL_EXTENDED_EYEGAZECORRECTION](ksproperty-cameracontrol-extended-eyegazecorrection.md)
