---
title: DirectInput Kernel-Mode Service Macros (Windows Drivers)
description: Learn more about DirectInput Kernel-Mode Service Macros.
ms.date: 10/27/2022
---

# DirectInput Kernel-Mode Service Macros

DirectInput provides a set of macros that contain entry points to kernel-mode services. These entry points are:

**Microsoft services**

VJOYD\_Register\_Device\_Driver. For information about this service macro, see [The DirectX 5.0 Interface](directx-5-0-interface.md).

VJOYD\_GetPosEx\_Service

The VJOYD\_GetPosEx\_Service macro allows kernel-mode components to get joystick data, thereby bypassing WinMM.

```cpp
VJOYDAPI_GetPosEx_Service, SERVICE
```

ENTRY:

eax = pointer to JOYINFOEX

ebx = joystick ID

EXIT:

eax = joystick return code

**DirectInput Services**

VJOYD\_GetInitParams\_Service. SIn DirectX 5.0 and later, the **Initialize** callback signals the driver about the identity of the device. This callback replaces the joystick identification callback (see [Joystick Identification Callback](original-interface.md#joystick-identification-callback) used in previous versions of DirectX.

```cpp
/*
Parameters
dwDeviceID 
Indicates the joystick ID number being used. The Windows joystick subsystem allocates external IDs.

lpInitParams 
Points to a DID_INITPARAMS structure that contains the initialization parameters. 

Return value
When access is being started, returns S_OK on success; otherwise returns an error value if the driver cannot service this ID. The result is ignored if access is being stopped.
*/

HRESULT Initialize(
   DWORD            dwDeviceID,
   LPDID_INITPARAMS lpInitParams
);
```

VJOYD\_Poll\_Service. See [Polling Callback](original-interface.md#polling-callback).

```cpp
/*
Parameters
dwDeviceID 
Indicates the joystick ID number being used. 

lpdwMask 
Points to a DWORD mask that describes the data requested on entry, and the data returned on exit. The mask is a combination of the following: 

JOYPD_X 
Bitmask for the dwX member of the VJPOLLDATA structure. 

JOYPD_Y 
Bitmask for the dwY member of the VJPOLLDATA structure. 

JOYPD_Z 
Bitmask for the dwZ member of the VJPOLLDATA structure. 

JOYPD_R 
Bitmask for the dwR member of the VJPOLLDATA structure. 

JOYPD_U 
Bitmask for the dwU member of the VJPOLLDATA structure. 

JOYPD_V 
Bitmask for the dwV member of the VJPOLLDATA structure. 

JOYPD_POV0 
Bitmask for the dwPOV0 member of the VJPOLLDATA structure. 

JOYPD_POV1 
Bitmask for the dwPOV1 member of the VJPOLLDATA structure. 

JOYPD_POV2 
Bitmask for the dwPOV2 member of the VJPOLLDATA structure. 

JOYPD_POV3 
Bitmask for the dwPOV3 member of the VJPOLLDATA structure. 

JOYPD_BTN0 
Bitmask for the dwBTN0 member of the VJPOLLDATA structure. 

JOYPD_BTN1 
Bitmask for the dwBTN1 member of the VJPOLLDATA structure. 

JOYPD_BTN2 
Bitmask for the dwBTN2 member of the VJPOLLDATA structure. 

JOYPD_BTN3 
Bitmask for the dwBTN3 member of the VJPOLLDATA structure. 

JOYPD_RESERVED0 
Bitmask for the dwReserved0 member of the VJPOLLDATA structure. 

JOYPD_RESERVED1 
Bitmask for the dwReserved1 member of the VJPOLLDATA structure. 

JOYPD_ELEMENT_MASK 
Bitmask for all members of the VJPOLLDATA structure. 

JOYPD_POSITION 
Bitmask for the position attribute of the device. 

JOYPD_VELOCITY 
Bitmask for the velocity attribute of the device. 

JOYPD_ACCELERATION 
Bitmask for the acceleration attribute of the device. 

JOYPD_FORCE 
Bitmask for the force attribute of the device. 

JOYPD_ATTRIB_MASK 
Bitmask for all possible attributes of the device. 

lpPollData 
Points to the polling data. 

Return value
Returns S_OK if the poll was completed successfully; returns S_FALSE if returned data is (partially or wholly) out of date; otherwise, returns an error code. 
*/

HRESULT Poll(
   DWORD        dwDeviceID,
   LPDWORD      lpdwMask,
   LPVJPOLLDATA lpPollData
);
```

The upper and lower words of the lpdwMask parameter are treated separately. The lower word is a simple bitmask of the elements in the VJPOLLDATA structure. The upper word describes the attributes for which these elements are requested. The lpPollData parameter to the poll contains an array of at least as many VJPOLLDATA structures as there are bits set in the upper word of the mask.

The first VJPOLLDATA structure should contain the position information. The next three VJPOLLDATA structures should contain information about the acceleration, velocity, and force, in that order. For example, if the device only supports position and force, the first structure contains position data, the second and third structures are empty and, therefore, are skipped, and the fourth structure contains force information.

The minidriver should always set the mask to what it can return, even if the poll fails because the device is unplugged. So if the device has less than 33 buttons, X, Y, and R, for position only, it should perform an operation such as the following before searching for the available data:

`*pdwMask &= ( JOYPD_POSITION | JOYPD_BTN0 | JOYPD_X | JOYPD_Y | JOYPD_R );`

If the device can return data for more than one attribute, the upper word has a bit set for each attribute and the lower word should have the bit set for any element that can be returned for any of the supported attributes. So even though force is an unlikely value for the button masks (which are single-bit), if the device reports buttons in the position data and force for X and Y, then position, force, X, Y, and buttons should all have their bits set.

**Device Services**

VJOYD\_Escape\_Service. See [**IDirectInputEffectDriver::Escape**](/windows/win32/api/dinputd/nf-dinputd-idirectinputeffectdriver-escape).

VJOYD\_CtrlMsg\_Service. The CtrlMsg callback sends specific messages to a minidriver.

```cpp
/*
Parameters
dwDeviceID 
Indicates the joystick ID number being used. 

dwMsgId 
Indicates the message being sent to the minidriver. A value of VJCM_PASSDRIVERDATA indicates that the dwParam parameter contains a DWORD to pass to the driver. A value of VJCM_CONFIGCHANGED indicates that the dwParam parameter informs the minidriver of a change in configuration. 

dwParam 
Specifies one of the following:

If the dwMsgId parameter is set to VJCM_PASSDRIVERDATA, this parameter contains a DWORD to pass to the driver. This allows the JOY_OEMPOLL_PASSDRIVERDATA poll type that was used to pass driver data to a DirectX 3.0 driver to still be used for a driver designed for DirectX 5.0 and later versions. 

If the dwMsgId parameter is set to VJCM_CONFIGCHANGED, this parameter contains a pointer to a VJCFGCHG structure that informs the minidriver of a change in configuration. 

Return value
Returns S_OK if successful, otherwise returns S_FALSE.

*/

HRESULT CtrlMsg(
   DWORD dwDeviceID,
   DWORD dwMsgId,
   DWORD dwParam
);
```

**Force Feedback Device Services**

VJOYD\_DestroyEffect\_Service. See [**IDirectInputEffectDriver::DestroyEffect**](/windows/win32/api/dinputd/nf-dinputd-idirectinputeffectdriver-destroyeffect).

VJOYD\_DownloadEffect\_Service. See [**IDirectInputEffectDriver::DownloadEffect**](/windows/win32/api/dinputd/nf-dinputd-idirectinputeffectdriver-downloadeffect).

VJOYD\_GetEffectStatus\_Service. See [**IDirectInputEffectDriver::GetEffectStatus**](/windows/win32/api/dinputd/nf-dinputd-idirectinputeffectdriver-geteffectstatus).

VJOYD\_GetFFState\_Service. See [**IDirectInputEffectDriver::GetForceFeedbackState**](/windows/win32/api/dinputd/nf-dinputd-idirectinputeffectdriver-getforcefeedbackstate).

VJOYD\_SendFFCommand\_Service. See [**IDirectInputEffectDriver::SendForceFeedbackCommand**](/windows/win32/api/dinputd/nf-dinputd-idirectinputeffectdriver-sendforcefeedbackcommand).

VJOYD\_SetGain\_Service. See [**IDirectInputEffectDriver::SetGain**](/windows/win32/api/dinputd/nf-dinputd-idirectinputeffectdriver-setgain).

VJOYD\_StartEffect\_Service. See [**IDirectInputEffectDriver::StartEffect**](/windows/win32/api/dinputd/nf-dinputd-idirectinputeffectdriver-starteffect).

VJOYD\_StopEffect\_Service. See [**IDirectInputEffectDriver::StopEffect**](/windows/win32/api/dinputd/nf-dinputd-idirectinputeffectdriver-stopeffect).

**Interrupt Polling Service**

VJOYD\_DeviceUpdateNotify\_Service

A minidriver that receives asynchronous updates from its device should call VJOYD\_DeviceUpdateNotify\_Service to notify DirectInput that new data is available. If an application has requested data from this device, DirectInput responds by issuing a poll to retrieve the data. If no applications request data from this device, or if the applications are not using DirectInput (if they are using **WinMM** functions instead) this service does nothing.

**Screen Saver Service**

VJOYD\_JoystickActivity\_Service

The **VJOYD\_JoystickActivity\_Service** macro is called internally to allow DirectInput to receive information about the joystick activity that is being reported through the **WinMM** functions. This information should prevent a screen saver from being activated. This macro should not be called by minidrivers and may not be supported in future versions.

**Registry Access Services**

The VJOYD\_OpenConfigKey\_Service macro is used by joystick drivers to open a configuration key. This should mirror the [**IDirectInputJoyConfig8::OpenConfigKey**](/previous-versions/windows/hardware/device-stage/drivers/ff540995(v=vs.85)) method.

`VJOYD_OpenConfigKey_Service, SERVICE`

- ENTRY:  
  eax = ID of key to open

  ecx = address of a **DWORD** in which to store the key

- EXIT:  
  eax = same as \_RegOpenKey except that ERROR\_CANTOPEN is returned if VJoyD has not yet established the current configuration key.

VJOYD\_OpenConfigKey\_Service

The VJOYD\_OpenTypeKey\_Service macro is used by joystick drivers to open a type key. It should mirror the [**IDirectInputJoyConfig8::OpenTypeKey**](/windows/win32/api/dinputd/nf-dinputd-idirectinputjoyconfig8-opentypekey) method.

`VJOYD_OpenTypeKey_Service, SERVICE`

- ENTRY:  
  eax = pointer to name of type

  ecx = pointer to **DWORD** in which to store the key

- EXIT:  
  eax = same as \_RegOpenKey

> [!NOTE]
> If you need to open registry keys, you should use the VJOYD\_OpenConfigKey\_Service and VJOYD\_OpenTypeKey\_Service service macros instead of opening the registry keys directly. Using these services ensures that the correct registry branch is opened. In addition, the service macros will be supported in future versions of DirectInput when the underlying registry data may be structured differently.
