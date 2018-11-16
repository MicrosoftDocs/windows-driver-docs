---
title: Supporting radio management
description: When the user chooses the Wireless option in PC settings on their Windows 8 laptop, notebook, or tablet, they can turn any connected wireless devices on or off.
ms.assetid: AA7AB429-30C5-4C10-AA85-41ED9EAEE69A
keywords:
- radio management API
- radio management API, example
- radio management, example
- GPS radio management
- radio management, GPS
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Supporting radio management

> [!IMPORTANT] 
> This documentation and the geolocation driver sample for Windows 8.1 has been deprecated.

When the user chooses the Wireless option in PC settings on their Windows 8 laptop, notebook, or tablet, they can turn any connected wireless devices on or off. These wireless devices may include a Wi-Fi antennae or a GPS device. The internal linkage between PC settings and a given wireless device is the [Radio Management API](https://msdn.microsoft.com/library/windows/hardware/hh406615) and a corresponding Radio Management DLL for the given device.

The Radio Management API is a set of COM/Win32 interfaces that ship as part of the Windows Driver Kit. These interfaces include methods that:

-   Retrieve the current state of a radio device
-   Support notification events for a radio device
-   Retrieve device properties (such as a friendly name)

These interfaces are intended only for OEMs and IHVs rather than application developers.

## The radio-management dynamic-link library (DLL)


If you create a device-driver for a radio device, like a GPS, your driver will need to include an additional dynamic-link library (DLL) that supports the interfaces in the Radio Management API. To help you understand the requirements of this DLL, Microsoft ships a sample Microsoft Visual Studio project and source code as part of the geolocation driver sample. This sample project, SampleRM.vcxproj is found in the Sensors Geolocation Driver Sample\\C++\\RadioManagerGPS folder of the driver sample. It includes seven C++ source files, six C++ header files, a module definition file, a resource file, two IDL files, a registry file (for registering the DLL), and an install script.

The following table lists the methods in the Radio Management API and the corresponding methods found in the sample DLL.

|                                                     |                                                       |
|-----------------------------------------------------|-------------------------------------------------------|
| Radio Manager API                                   | Radio Manager DLL                                     |
| IMediaRadioManager::GetRadioInstances               | CSampleRadioManager::GetRadioInstances                |
| IMediaRadioManager::OnSystemRadioStateChange        | CSampleRadioManager::OnSystemRadioStateChange         |
| IRadioInstance::GetFriendlyName                     | CSampleRadioInstance::GetFriendlyName                 |
| IRadioInstance::GetInstanceSignature                | CSampleRadioInstance::GetInstanceSignature            |
| IRadioInstance::GetRadioManagerSignature            | CSampleRadioInstance::GetRadioManagerSignature        |
| IRadioInstance::GetRadioState                       | CSampleRadioInstance::GetRadioState                   |
| IRadioState::IsAssociatingDevice                    | CSampleRadioInstance::IsAssociatingDevice             |
| IRadioState::IsMultiComm                            | CSampleRadioInstance::IsMultiComm                     |
| IRadioState::SetRadioState                          | CSampleRadioInstance::SetRadioState                   |
| IRadioInstanceCollection::GetAt                     | CRadioInstanceCollection::GetAt                       |
| IRadioInstanceCollection::GetCount                  | CRadioInstanceCollection::GetCount                    |
| IMediaRadioManagerNotifySink::OnInstanceAdd         | CSampleRadioManager::\_FireEventOnInstanceAdd         |
| IMediaRadioManagerNotifySink::OnInstanceRadioChange | CSampleRadioManager::\_FireEventOnInstanceRadioChange |
| IMediaRadioManagerNotifySink::OnInstanceRemove      | CSampleRadioManager::\_FireEventOnInstanceRemove      |

 

## Communicating with the device driver


When the radio-management DLL receives a request to retrieve or set the radio state from the radio-management API, it forwards that request as an IOCTL to the corresponding device driver. The DLL sends IOCTLs by invoking the [DeviceIoControl]( http://go.microsoft.com/fwlink/p/?linkid=256462) function. The specific IOCTLs associated with radio management are:

-   IOCTL\_GPS\_RADIO\_MANAGEMENT\_GET\_RADIO\_STATE
-   IOCTL\_GPS\_RADIO\_MANAGEMENT\_GET\_PREVIOUS\_RADIO\_STATE
-   IOCTL\_GPS\_RADIO\_MANAGEMENT\_SET\_RADIO\_STATE
-   IOCTL\_GPS\_RADIO\_MANAGEMENT\_SET\_PREVIOUS\_RADIO\_STATE

In the case of the sample radio-management DLL, the **CSensorCommuncation::GetRadioStateHelper** and **CSensorCommunication::SetRadioStateHelper** methods forward the IOCTLs so the sample Geolocation driver.

## Driver support for radio management


In addition to the radio-management DLL, you will also need to modify your device driver to handle the four radio-management IOCTLs that are sent from the DLL to the driver. These IOCTLs inform the device driver that it should retrieve the current radio state, or, turn the device’s radio on or off.

The device driver initially receives and processes any IOCTL in the **CMyQueue::OnDeviceIoControl** method. If this method identifies one of the four radio-management IOCTLs, it forwards that IOCTL to the **CMyDevice::ProcessIoControlRadioManagement** method for further processing. This method, in turn, forwards the IOCTL to **CSensorManager::ProcessIoControlRadioManagement**. Within this last method, the radio state is set or retrieved by calls into the **CSensorDDI** class.

The **CSensorDDI** class contains one method that retrieves the radio state (**CSensorDDI::OnGetRadioState**) and one method that sets the radio state (**CSEnsorDDI::OnSetRadioState**). This is where the final IOCTL processing occurs in the sample device driver which emulates hardware. In the case of an actual device driver, the **CSensorDDI::OnGetRadioState** method would request the radio state from the device firmware and the **CSensorDDI::OnSetRadioState** method would issue a request to the firmware to set the state.

## Debugging the radio-management DLL


You can debug the radio-management DLL in Visual Studio by completing the following steps.

1.  1. Open Visual Studio and select **SampleRM.vcsproj** in the C++\\RadioManagerGPS folder.
2.  2. Select **Debug/Attach to Process**. In the list of available processes that appears in the **Attach to Process** dialog box, select dllhost.exe.

Note that if multiple instances of dllhost.exe are running, you may need to choose each one in a process of elimination in order to determine the process associated with the radio-management DLL. Once you’ve attached to the correct process, you can set breakpoints in Visual Studio and begin debugging.

 

 




