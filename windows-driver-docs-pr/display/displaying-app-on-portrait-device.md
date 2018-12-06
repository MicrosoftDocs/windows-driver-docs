---
title: Example code for displaying an app on a portrait device
description: Here is code that you can use to make your app display correctly on a portrait device.
ms.assetid: 5653E920-A068-4EBA-869E-0E2D65118B33
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Example code for displaying an app on a portrait device


Here is code that you can use to make your app display correctly on a portrait device.

```cpp
//
// This file contains utility functions for use in desktop applications for getting the current
// orientation as Landscape/Portrait/LandscapeFlipped/PortraitFlipped (abbr: L/P/LF/PF). These
// functions are most helpful for use with APIs which expect one of these values, while the APIs
// for retrieving all return the rotation in degrees (0/90/180/270). There is not a direct mapping
// between these two forms since 0 degrees means portrait on portrait-native devices and landscape
// on landscape-native devices.
//

#include <windows.h>
#include <iostream>

enum ORIENTATION
{
    INVALID,
    LANDSCAPE,
    PORTRAIT,
    LANDSCAPE_FLIPPED,
    PORTRAIT_FLIPPED
};

// Maps the current rotation from 0/90/180/270 to L/P/LF/PF using the unrotated
// resolution to guess at what the native orientation is.
ORIENTATION GetOrientationFromCurrentMode(_In_ PCWSTR pszDeviceName)
{
    DEVMODEW CurrentMode = {};
    CurrentMode.dmSize = sizeof(CurrentMode);
    if (!EnumDisplaySettingsW(pszDeviceName,
                              ENUM_CURRENT_SETTINGS,
                              &CurrentMode))
    {
        // Error condition, likely invalid device name, could log error
        // HRESULT hr = HRESULT_FROM_WIN32(GetLastError());
        return INVALID;
    }

    if ((CurrentMode.dmDisplayOrientation == DMDO_90) ||
        (CurrentMode.dmDisplayOrientation == DMDO_270))
    {
        DWORD temp = CurrentMode.dmPelsHeight;
        CurrentMode.dmPelsHeight = CurrentMode.dmPelsWidth;
        CurrentMode.dmPelsWidth = temp;
    }

    if (CurrentMode.dmPelsWidth < CurrentMode.dmPelsHeight)
    {
        switch (CurrentMode.dmDisplayOrientation)
        {
            case DMDO_DEFAULT: return PORTRAIT;
            case DMDO_90: return LANDSCAPE_FLIPPED;
            case DMDO_180: return PORTRAIT_FLIPPED;
            case DMDO_270: return LANDSCAPE;
            default: return INVALID;
        }
    }
    else
    {
        switch (CurrentMode.dmDisplayOrientation)
        {
            case DMDO_DEFAULT: return LANDSCAPE;
            case DMDO_90: return PORTRAIT;
            case DMDO_180: return LANDSCAPE_FLIPPED;
            case DMDO_270: return PORTRAIT_FLIPPED;
            default: return INVALID;
        }
    }
}

// Overloaded function accepts an HMONITOR and converts to DeviceName
ORIENTATION GetOrientationFromCurrentMode(HMONITOR hMonitor)
{
    // Get the name of the &#39;monitor&#39; being requested
    MONITORINFOEXW ViewInfo;
    RtlZeroMemory(&ViewInfo, sizeof(ViewInfo));
    ViewInfo.cbSize = sizeof(ViewInfo);
    if (!GetMonitorInfoW(hMonitor, &ViewInfo))
    {
        // Error condition, likely invalid monitor handle, could log error
        // HRESULT hr = HRESULT_FROM_WIN32(GetLastError());
        return INVALID;
    }
    else
    {
        return GetOrientationFromCurrentMode(ViewInfo.szDevice);
    }
}

// Returns true if this is an integrated display panel e.g. the screen attached to tablets or laptops.
bool IsInternalVideoOutput(const DISPLAYCONFIG_VIDEO_OUTPUT_TECHNOLOGY VideoOutputTechnologyType)
{
    switch (VideoOutputTechnologyType)
    {
        case DISPLAYCONFIG_OUTPUT_TECHNOLOGY_INTERNAL:
        case DISPLAYCONFIG_OUTPUT_TECHNOLOGY_DISPLAYPORT_EMBEDDED:
        case DISPLAYCONFIG_OUTPUT_TECHNOLOGY_UDI_EMBEDDED:
            return TRUE;

        default:
            return FALSE;
    }
}

// Given a target on an adapter, returns whether it is a natively portrait display
bool IsNativeOrientationPortrait(const LUID AdapterLuid, const UINT32 TargetId)
{
    DISPLAYCONFIG_TARGET_PREFERRED_MODE PreferredMode;
    PreferredMode.header.type = DISPLAYCONFIG_DEVICE_INFO_GET_TARGET_PREFERRED_MODE;
    PreferredMode.header.size = sizeof(PreferredMode);
    PreferredMode.header.adapterId = AdapterLuid;
    PreferredMode.header.id = TargetId;

    HRESULT hr = HRESULT_FROM_WIN32(DisplayConfigGetDeviceInfo(&PreferredMode.header));
    if (FAILED(hr))
    {
        // Error condition, assume natively landscape
        return false;
    }

    return (PreferredMode.height > PreferredMode.width);
}

// Note: Since an hmon can represent multiple monitors while in clone, this function as written will return
//  the value for the internal monitor if one exists, and otherwise the highest clone-path priority. 
HRESULT GetPathInfo(_In_ PCWSTR pszDeviceName, _Out_ DISPLAYCONFIG_PATH_INFO* pPathInfo)
{
    HRESULT hr = S_OK;
    UINT32 NumPathArrayElements = 0;
    UINT32 NumModeInfoArrayElements = 0;
    DISPLAYCONFIG_PATH_INFO* PathInfoArray = nullptr;
    DISPLAYCONFIG_MODE_INFO* ModeInfoArray = nullptr;

    do
    {
        // In case this isn&#39;t the first time through the loop, delete the buffers allocated
        delete[] PathInfoArray;
        PathInfoArray = nullptr;

        delete[] ModeInfoArray;
        ModeInfoArray = nullptr;

        hr = HRESULT_FROM_WIN32(GetDisplayConfigBufferSizes(QDC_ONLY_ACTIVE_PATHS, &NumPathArrayElements, &NumModeInfoArrayElements));
        if (FAILED(hr))
        {
            break;
        }

        PathInfoArray = new(std::nothrow) DISPLAYCONFIG_PATH_INFO[NumPathArrayElements];
        if (PathInfoArray == nullptr)
        {
            hr = E_OUTOFMEMORY;
            break;
        }

        ModeInfoArray = new(std::nothrow) DISPLAYCONFIG_MODE_INFO[NumModeInfoArrayElements];
        if (ModeInfoArray == nullptr)
        {
            hr = E_OUTOFMEMORY;
            break;
        }

        hr = HRESULT_FROM_WIN32(QueryDisplayConfig(QDC_ONLY_ACTIVE_PATHS, &NumPathArrayElements, PathInfoArray, &NumModeInfoArrayElements, ModeInfoArray, nullptr));
    }while (hr == HRESULT_FROM_WIN32(ERROR_INSUFFICIENT_BUFFER));

    INT DesiredPathIdx = -1;

    if (SUCCEEDED(hr))
    {
        // Loop through all sources until the one which matches the &#39;monitor&#39; is found.
        for (UINT PathIdx = 0; PathIdx < NumPathArrayElements; ++PathIdx)
        {
            DISPLAYCONFIG_SOURCE_DEVICE_NAME SourceName = {};
            SourceName.header.type = DISPLAYCONFIG_DEVICE_INFO_GET_SOURCE_NAME;
            SourceName.header.size = sizeof(SourceName);
            SourceName.header.adapterId = PathInfoArray[PathIdx].sourceInfo.adapterId;
            SourceName.header.id = PathInfoArray[PathIdx].sourceInfo.id;

            hr = HRESULT_FROM_WIN32(DisplayConfigGetDeviceInfo(&SourceName.header));
            if (SUCCEEDED(hr))
            {
                if (wcscmp(pszDeviceName, SourceName.viewGdiDeviceName) == 0)
                {
                    // Found the source which matches this hmonitor. The paths are given in path-priority order
                    // so the first found is the most desired, unless we later find an internal.
                    if (DesiredPathIdx == -1 || IsInternalVideoOutput(PathInfoArray[PathIdx].targetInfo.outputTechnology))
                    {
                        DesiredPathIdx = PathIdx;
                    }
                }
            }
        }
    }

    if (DesiredPathIdx != -1)
    {
        *pPathInfo = PathInfoArray[DesiredPathIdx];
    }
    else
    {
        hr = E_INVALIDARG;
    }

    delete[] PathInfoArray;
    PathInfoArray = nullptr;
    
    delete[] ModeInfoArray;
    ModeInfoArray = nullptr;

    return hr;
}

// Overloaded function accepts an HMONITOR and converts to DeviceName
HRESULT GetPathInfo(HMONITOR hMonitor, _Out_ DISPLAYCONFIG_PATH_INFO* pPathInfo)
{
    HRESULT hr = S_OK;

    // Get the name of the &#39;monitor&#39; being requested
    MONITORINFOEXW ViewInfo;
    RtlZeroMemory(&ViewInfo, sizeof(ViewInfo));
    ViewInfo.cbSize = sizeof(ViewInfo);
    if (!GetMonitorInfoW(hMonitor, &ViewInfo))
    {
        // Error condition, likely invalid monitor handle, could log error
        hr = HRESULT_FROM_WIN32(GetLastError());
    }

    if (SUCCEEDED(hr))
    {
        hr = GetPathInfo(ViewInfo.szDevice, pPathInfo);
    }

    return hr;
}

// Note: Function return S_FALSE if there is no internal target
// Gets the path info for the integrated display panel e.g. the screen attached to tablets or laptops.
HRESULT GetPathInfoForInternal(_Out_ DISPLAYCONFIG_PATH_INFO* pPathInfo)
{
    HRESULT hr = S_OK;
    UINT32 NumPathArrayElements = 0;
    UINT32 NumModeInfoArrayElements = 0;
    DISPLAYCONFIG_PATH_INFO* PathInfoArray = nullptr;
    DISPLAYCONFIG_MODE_INFO* ModeInfoArray = nullptr;

    do
    {
        // In case this isn&#39;t the first time through the loop, delete the buffers allocated
        delete[] PathInfoArray;
        PathInfoArray = nullptr;

        delete[] ModeInfoArray;
        ModeInfoArray = nullptr;

        hr = HRESULT_FROM_WIN32(GetDisplayConfigBufferSizes(QDC_ONLY_ACTIVE_PATHS, &NumPathArrayElements, &NumModeInfoArrayElements));
        if (FAILED(hr))
        {
            break;
        }

        PathInfoArray = new(std::nothrow) DISPLAYCONFIG_PATH_INFO[NumPathArrayElements];
        if (PathInfoArray == nullptr)
        {
            hr = E_OUTOFMEMORY;
            break;
        }

        ModeInfoArray = new(std::nothrow) DISPLAYCONFIG_MODE_INFO[NumModeInfoArrayElements];
        if (ModeInfoArray == nullptr)
        {
            hr = E_OUTOFMEMORY;
            break;
        }

        hr = HRESULT_FROM_WIN32(QueryDisplayConfig(QDC_ONLY_ACTIVE_PATHS, &NumPathArrayElements, PathInfoArray, &NumModeInfoArrayElements, ModeInfoArray, nullptr));
    }while (hr == HRESULT_FROM_WIN32(ERROR_INSUFFICIENT_BUFFER));

    if (SUCCEEDED(hr))
    {
        hr = S_FALSE;
        RtlZeroMemory(pPathInfo, sizeof(*pPathInfo));

        for (UINT PathIdx = 0; PathIdx < NumPathArrayElements; ++PathIdx)
        {
            if (IsInternalVideoOutput(PathInfoArray[PathIdx].targetInfo.outputTechnology))
            {
                // There&#39;s only one internal target on the system and we found it.
                *pPathInfo = PathInfoArray[PathIdx];

                hr = S_OK;
                break;
            }
        }
    }

    delete[] PathInfoArray;
    PathInfoArray = nullptr;
    
    delete[] ModeInfoArray;
    ModeInfoArray = nullptr;

    return hr;
}

// Given a path info, this function will find the native orientation of the path and map 0/90/180/270 to L/P/LF/PF
ORIENTATION GetOrientationFromPathInfo(_In_ const DISPLAYCONFIG_PATH_INFO* const pPathInfo)
{
    bool IsNativelyPortrait = IsNativeOrientationPortrait(pPathInfo->targetInfo.adapterId, pPathInfo->targetInfo.id);
    DISPLAYCONFIG_ROTATION CurrentRotation = pPathInfo->targetInfo.rotation;

    if (IsNativelyPortrait)
    {
        switch (CurrentRotation)
        {
            case DISPLAYCONFIG_ROTATION_IDENTITY: return PORTRAIT;
            case DISPLAYCONFIG_ROTATION_ROTATE90: return LANDSCAPE_FLIPPED;
            case DISPLAYCONFIG_ROTATION_ROTATE180: return PORTRAIT_FLIPPED;
            case DISPLAYCONFIG_ROTATION_ROTATE270: return LANDSCAPE;
            default: return INVALID;
        }
    }
    else
    {
        switch (CurrentRotation)
        {
            case DISPLAYCONFIG_ROTATION_IDENTITY: return LANDSCAPE;
            case DISPLAYCONFIG_ROTATION_ROTATE90: return PORTRAIT;
            case DISPLAYCONFIG_ROTATION_ROTATE180: return LANDSCAPE_FLIPPED;
            case DISPLAYCONFIG_ROTATION_ROTATE270: return PORTRAIT_FLIPPED;
            default: return INVALID;
        }
    }
}

// This function shows the use of each of the utility functions found above in a reasonable order of calling.
ORIENTATION GetOrientation(bool UseInternal)
{
    DISPLAYCONFIG_PATH_INFO PathInfo = {};
    HMONITOR hPrimaryMon = MonitorFromWindow(NULL, MONITOR_DEFAULTTOPRIMARY);

    HRESULT hr = S_FALSE;
    if (UseInternal)
    {
        hr = GetPathInfoForInternal(&PathInfo);
    }

    if ((hr == S_FALSE) || FAILED(hr))
    {
        // Could log an error on FAILED(hr), but whether legitimate failure or desktop system, try the primary monitor
        hr = GetPathInfo(hPrimaryMon, &PathInfo);
    }

    if (SUCCEEDED(hr))
    {
        return GetOrientationFromPathInfo(&PathInfo);
    }
    else
    {
        // In Windows 8.1 and previous operating systems, the GetPathInfo (and ForInternal) call will fail in a remote session,
        // falling back to checking the current mode is the most appropriate thing to do in this situation.
        return GetOrientationFromCurrentMode(hPrimaryMon);
    }
}

void PrintOrientation(ORIENTATION Orientation)
{
    switch (Orientation)
    {
        case INVALID: std::cout << "Error" << std::endl; break;
        case LANDSCAPE: std::cout << "Landscape" << std::endl; break;
        case PORTRAIT: std::cout << "Portrait" << std::endl; break;
        case LANDSCAPE_FLIPPED: std::cout << "Landscape Flipped" << std::endl; break;
        case PORTRAIT_FLIPPED: std::cout << "Portrait Flipped" << std::endl; break;
    }
}

int __cdecl main(int argc, const char* argv[])
{
    UNREFERENCED_PARAMETER(argc);
    UNREFERENCED_PARAMETER(argv);
    HRESULT hr = E_FAIL;

    // Note: This MonitorFromWindow call should be modified if the orientation is needed for 
    // the monitor the application&#39;s window is currently on. It is also unnecessary if only
    // the internal monitor is desired.
    HMONITOR hPrimaryMon = MonitorFromWindow(NULL, MONITOR_DEFAULTTOPRIMARY);

    // Print the orientation of the integrated panel.
    {
        DISPLAYCONFIG_PATH_INFO PathInfo = {};

        hr = GetPathInfoForInternal(&PathInfo);
        if (hr == S_FALSE)
        {
            std::cout << "No integrated panel found." << std::endl;
        }
        else if (SUCCEEDED(hr))
        {
            std::cout << "Integrated panel: ";
            PrintOrientation(GetOrientationFromPathInfo(&PathInfo));
        }
        else
        {
            std::cout << "Error looking for internal monitor: " << hr << std::endl;
        }
    }

    // Print the orientation of the primary monitor.
    {
        DISPLAYCONFIG_PATH_INFO PathInfo = {};

        hr = GetPathInfo(hPrimaryMon, &PathInfo);
        if (SUCCEEDED(hr))
        {
            std::cout << "Primary monitor: ";
            PrintOrientation(GetOrientationFromPathInfo(&PathInfo));
        }
        else
        {
            std::cout << "Error getting path info for primary monitor: " << hr << std::endl;
        }
    }

    // In Windows 8.1 and previous operating systems, GetPathInfo (and GetPathInfoForInternal) will fail in a remote
    // session, falling back to checking the current mode is the most appropriate thing to do in this situation.
    if (FAILED(hr))
    {
        std::cout << "Fallback based on current mode: ";
        PrintOrientation(GetOrientationFromCurrentMode(hPrimaryMon));
    }
}
```

 

 





