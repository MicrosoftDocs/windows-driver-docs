---
title: Access the Sensor Class Extension
description: Access the sensor class extension
ms.date: 01/11/2024
---

# Access the sensor class extension

| Module     | Class/Interface |
|------------|-----------------|
| Device.cpp | CMyDevice       |

Microsoft supports two Sensor APIs. Both simplify accessing devices, retrieving data, and setting properties:

- **Desktop API** (for traditional desktop apps) - uses COM/Win32; you write apps in C++.
- **WinRT API** (for Windows apps) - you write apps in HtML and JavaScript, or, XAML and Visual Basic, C# or C++.

The sensor class extension (**ISensorClassExtension**) links your sensor driver and the Sensor APIs. Your driver uses it to accomplish the following:

- Initialize and unitialize the sensor class extension
- Raise events
- Process WPD input/output control codes (IOCTLs)
- Close UMDF file handles

## Initializing the class extension

The SpbAccelerometer sample initializes the class extension when WUDFx.dll (a component of the Windows user-mode driver framework) invokes **CMyDevice::OnPrepareHardware**:

```cpp
if (SUCCEEDED(hr))
{
    // Initialize the sensor class extension
    hr = m_spClassExtension->Initialize(pWdfDevice, spUnknown);
}
```

### Releasing the class extension

The sample driver un-initializes and releases the class extension when CMyDevice::OnReleaseHardware is invoked:

```cpp
if (m_spClassExtension != nullptr)
{
   hr = m_spClassExtension->Uninitialize();
}
```

### Supporting data events with the class extension

When a sensor app registers an event handler for data events, the sample driver posts event notifications using **ISensorClassExtension::PostEvent**. This occurs within **CSensorDdi::PostDataEvent**:

```cpp
if (SUCCEEDED(hr))
{
   hr = m_spClassExtension->PostEvent(SensorId, spCollection);
}
```

### Supporting state-change events with the class extension

When a sensor app registers an event handler for state-change events, the sample driver posts event notifications using **ISensorClassExtension::PostStateChange**. This occurs within **CSensorDdi::PostStateChange**:

```cpp
HRESULT hr = m_spClassExtension->PostStateChange(SensorId, state);
```
