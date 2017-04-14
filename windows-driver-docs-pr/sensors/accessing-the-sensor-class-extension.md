---
title: Access the sensor class extension
author: windows-driver-content
description: Access the sensor class extension
ms.assetid: 206A00AE-45D7-49D8-97E2-45A6DACFCB08
---

# Access the sensor class extension


| Module     | Class/Interface |
|------------|-----------------|
| Device.cpp | CMyDevice       |

 

Microsoft supports two Sensor APIs. Both simplify accessing devices, retrieving data, and setting properties:

-   **Desktop API** (for traditional desktop apps) - uses COM/Win32; you write apps in C++.
-   **WinRT API** (for windows store apps) - you write apps in HtML and JavaScript, or, XAML and Visual Basic, C# or C++.

The sensor class extension (**ISensorClassExtension**) links your sensor driver and the Sensor APIs. Your driver uses it to accomplish the following:

-   Initialize and unitialize the sensor class extension
-   Raise events
-   Process WPD input/output control codes (IOCTLs)
-   Close UMDF file handles

### Initializing the class extension

The SpbAccelerometer sample initializes the class extension when WUDFx.dll (a component of the Windows user-mode driver framework) invokes **CMyDevice::OnPrepareHardware**:

```ManagedCPlusPlus
if (SUCCEEDED(hr))
{
    // Initialize the sensor class extension
    hr = m_spClassExtension->Initialize(pWdfDevice, spUnknown);
}  
```

### Releasing the class extension

The sample driver un-initializes and releases the class extension when CMyDevice::OnReleaseHardware is invoked:

```ManagedCPlusPlus
if (m_spClassExtension != nullptr)
{
   hr = m_spClassExtension->Uninitialize();
}
```

### Supporting data events with the class extension

When a sensor app registers an event handler for data events, the sample driver posts event notifications using **ISensorClassExtension::PostEvent**. This occurs within **CSensorDdi::PostDataEvent**:

```ManagedCPlusPlus
if (SUCCEEDED(hr))
{
   hr = m_spClassExtension->PostEvent(SensorId, spCollection);
}
```

### Supporting state-change events with the class extension

When a sensor app registers an event handler for state-change events, the sample driver posts event notifications using **ISensorClassExtension::PostStateChange**. This occurs within **CSensorDdi::PostStateChange**:

```ManagedCPlusPlus
HRESULT hr = m_spClassExtension->PostStateChange(SensorId, state);
```

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bsensors\sensors%5D:%20Access%20the%20sensor%20class%20extension%20%20RELEASE:%20%281/12/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


