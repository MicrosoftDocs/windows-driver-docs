---
title: Original Interface
description: Original interface
keywords:
- joysticks WDK HID , interfaces
- virtual joystick drivers WDK HID , interfaces
- VJoyD WDK HID , interfaces
- interfaces WDK joysticks
- joysticks WDK HID , callbacks
- virtual joystick drivers WDK HID , callbacks
- VJoyD WDK HID , callbacks
- callbacks WDK joysticks
- polling WDK joysticks
ms.date: 01/11/2024
---

# Original interface

The following joystick minidriver callbacks are specific to the original interface. The four joystick-specific callbacks must be registered with the VJoyD VJOYD_Register_Device_Driver service before returning from processing the SYS_DYNAMIC_DEVICE_INIT message. EAX must point to the polling routine, EBX (the configuration handler), ECX (the capabilities callback), and EDX (the identification routine). An example of a joystick minidriver registration sequence is as follows:

| &nbsp; | &nbsp; |
|--|--|
| Mov | eax, offset32 _PollRoutine@8 |
| Mov | ebx, offset32 _CfgRoutine |
| Mov | ecx, offset32 _HWCapsRoutine@8 |
| Mov | edx, offset32 _JoyIdRoutine@8 |
| VxDcall | VJOYD_Register_Device_Driver |

In addition to the registration, a minidriver can perform any other initialization at this time. The joystick minidriver model doesn't require any specific actions in response to SYS_DYNAMIC_DEVICE_EXIT, though the VxD may still use it for final internal cleanup.

## Configuration manager callback

```cpp
CONFIGRET CM_HANDLER CfgRoutine( CONFIGFUNC cfFuncName,
    SUBCONFIGFUNC scfSubFuncName, DEVNODE dnToDevNode,
    ULONG dwRefData, ULONG ulFlags );
```

General information about how to interface the configuration manager is available in the Plug and Play Environment portion of the Windows Me section of the Windows Driver Development Kit (DDK). The DDK preceded the Windows Driver Kit (WDK).

Configuration manager callback is passed to the minidrivers only if minidrivers are loaded when VJoyD receives the callback. Because of this a significant problem exists with current implementations of this callback. VJoyD receives callbacks for those device nodes with which it's associated when the device nodes are enumerated during system boot, when the configuration manager sends a message during run time for a special event like device reconfiguration, and when the system is closing down. Therefore, only the devices that are selected on the previous boot are loaded in time to receive these messages. This limits the potential number of functions that are performed when this callback is invoked because a user can boot the system, configure a joystick, play games, de-configure the joystick, and shut down without calling this callback.

For devices that don't need any hardware resources, this isn't an issue. Devices that use such resources have several options: they can work only when configured at boot time, they can dynamically allocate the resources from the configuration manager, or they can search for their allocations in the registry for their device node and request the information.

Given the preceding information, driver is initialized properly either when the driver is first loaded and it receives the SYS_DYNAMIC_DEVICE_INIT, or on the first time through the polling routine. Similarly, resources should be made free when a SYS_DYNAMIC_DEVICE_EXIT message is received.

Another issue is that all configuration manager callbacks for currently serviced joystick devices are sent to all loaded minidrivers. However, you can use the *dnToDevNode* parameter to look up the device identifier, and you can check this against the devices that this driver can handle.

## Polling callback

```cpp
int stdcall PollRoutine( int type, LPJOYOEMPOLLDATA pojd );
```

The polling routine is called either in direct response to an application that calls joyGetPos or joyGetPosEx, or when Windows 95/98/Me periodically calls joyGetPos for an application that has called joySetCapture. Only when a minidriver first receives a call on its poll callback, it can be certain that an application requires data from it. All the other callbacks are called for all devices that are currently in the list of 16 available joysticks, whether any application has requested data.

The possible return values are JOY_OEMPOLLRC_YOUPOLL, JOY_OEMPOLLRC_FAIL, and JOY_OEMPOLLRC_OK. Except for a button-only poll, the return value is interpreted into either JOYERR_NOERROR or JOYERR_UNPLUGGED before being returned to an application. A button poll is always assumed to succeed.

JOY_OEMPOLLRC_FAIL is returned if the device that is polled doesn't respond, or if VJoyD requests a poll that the minidriver can't process. In the former case, you should ensure not to fail a device unless it really has failed, because the application is likely to stop everything and request that the user check the connections to the device. For example, a call to joySetCapture fails if the first poll fails. Minor device failures shouldn't result in failure report until user intervention is required or it detects an unrecoverable device error. For instance, a device that communicates using a packet-based protocol should attempt a retry before it fails the poll if one packet isn't valid.

It's important to recognize genuine device failure and return an error eventually; otherwise, an application can't determine whether the user intervention is required at all. If old or false data is returned while error recovery is performed, the meaning of data returned, the number of polls allowed, or the time allowed from the initial error should be restricted so the driver doesn't delay for an inordinate amount of time. When a minidriver is requested to perform a poll on a device that it doesn't control, or to perform a poll type or subtype that it can't service, a failure is always the correct response.

You can use JOY_OEMPOLLRC_YOUPOLL if the standard analog poll yields the correct results.

You should return JOY_OEMPOLLRC_OK in a regular case when JOYINFOEX structure is filled with the requested data.

You must take care if you use poll to perform initialization on the device. Applications can perform an initial poll to check for the availability of the device by checking the return code. They can then make subsequent polls with no error checks. This is essentially what joySetCapture does. Ideally, all initialization and the first poll should be performed. For those cases in which the time required to set up the device lasts up to a second, it's sufficient to verify that the device is present and working and to return inert data for the first poll.

The API and system drivers perform validation on the request made by the application and copy the required data into the application structure upon completion. The minidriver shouldn't replicate this functionality. However, nothing prevents one process from polling a device while another is still in the middle of a poll. The consequences of this event are no worse than different samples reporting the two axes. If necessary, a minidriver can perform its own process synchronization.

Return values depend upon the "type" parameter and the device it supports. You should always return the buttons and button number. Because there's no way to specify to the minidriver that a POV poll is required, you should return this value if any axes are requested. Set the POV_UNDEFINED if the device doesn't support one. For a single axis poll, the value is returned in the **dwX** member of the JOYPOLLDATA structure (the **[VJPOLLDATA](/previous-versions/windows/hardware/drivers/ff543573(v=vs.85))** structure in DirectX 5.0 and later). For a multiple axes request in which the number of axes requested is odd, the **do_other** member of the **[JOYOEMPOLLDATA](/previous-versions/windows/hardware/drivers/ff542251(v=vs.85))** structure specifies whether the last axis is returned in place or for the following axis. In a three-axis poll, for example, the member specifies whether the axes returned are X, Y, Z or X, Y, R.

The following is a list of other possible return values, categorized by type (you can fill in extra data, but note that all polls of an odd number of axes must decode the **do_other** member to decide what it returns):

- JOY_OEMPOLL_GETBUTTONS: Nothing extra.

- JOY_OEMPOLL_POLL1: The axis specified in the **do_other** member is returned in the **dwX** member.

- JOY_OEMPOLL_POLL2: The X and Y axes are returned in the **dwX** and **dwY** members.

- JOY_OEMPOLL_POLL3: The X and Y axes are returned in the **dwX** and **dwY** members.

  If the **do_other** member is nonzero, the R axis is returned in the **dwR** member. Otherwise, the Z axis is returned in the **dwZ** member.

- JOY_OEMPOLL_POLL4: The X, Y, Z and R axes are returned in the **dwX**, **dwY**, **dwZ**, and **dwR** members respectively.

- JOY_OEMPOLL_POLL5: The X, Y, Z and R axes are returned in the **dwX**, **dwY**, **dwZ**, and **dwR** members respectively.

  If the **do_other** member is nonzero, the V-axis is returned in the **dwR** member. Otherwise, the U-axis is returned in the **dwZ** member.

- JOY_OEMPOLL_POLL6: The X, Y, Z, R, U and V axes are returned in the **dwX**, **dwY**, **dwZ**, **dwR**, **dwU**, and **dwV** members respectively.

DirectX 3.0 added the non-poll type of JOY_OEMPASSDRIVERDATA, in which the **do_other** member contains a DWORD that an application passes. You can use this DWORD for any minidriver-defined function, but it's intended in particular to enable custom setup applications that have fully identified the minidriver to send device-specific commands and configuration information.

A minidriver should return JOY_OEMPOLLRC_FAIL for all types it doesn't support.

Although the axis data is returned in double words, the range of axis values should be restricted to approximately 10-bit values if the standard joystick control panel configuration is used as the sole configuration mechanism. Because the user can't easily see what is happening, this helps to avoid confusion. To aid compatibility with existing applications, the axes returned by a minidriver should be the same as those returned by an analog joystick (where applicable). For example, X would be a left-to-right movement minimized at the left, and so on.

For an activated POV hat, the direction should be represented as the angle, in degrees, multiplied by 100, with 0 being forward, 9000 right, 18000 backwards, and 27000 left.

Because the poll routine call is the only positive indication that the device is still in use, minidrivers that use shared resources such as communications ports should keep track of the last time they were used. If usage time becomes significant, the minidrivers should stop to sample the device, and free the resources in case the user has completed the device usage and is now trying to use the resource for another purpose. This is important if there are occurrences of communications errors, because this could be an indication that the device is unplugged.

## Hardware capabilities callback

```cpp
int __stdcall HWCapsRoutine( int joyid, LPJOYOEMHWCAPS pjhwc );
```

Whenever one requests the hardware capabilities of the device, HWCapsRoutine is called. In particular, VJoyD calls HWCapsRoutine before it returns from VJOYD_Register_Device_Driver. So, it's important that the driver completes any initialization upon which this call relies before the device is registered. These values are generally constants. For a device that has four buttons and three axes, of which the third may return either a throttle or a rudder value, the following is appropriate:

```cpp
pjhwc->dwMaxButtons = 4;    // This should always be the number of buttons 
pjhwc->dwMaxAxes = 4;       // The largest axis number which may be requested 
pjhwc->dwNumAxes = 3;       // The number of axes the device has 
```

## Joystick identification callback

```cpp
int __stdcall JoyIdRoutine( int joyid, BOOL used );
```

VJoyD calls JoyIDRoutine when a user configures or de-configures a joystick as one of the 16 joysticks. If the minidriver can support the ID requested in *joyid*, JoyIdRoutine returns a nonzero value. If the minidriver can't support the ID, the routine returns zero value.

Whenever any change is made and joyConfigChanged is called to update the driver, VJoyD cycles through all 16 devices, starting with JOYSTICKID1. It resets all devices to unused and then loops through them again to set all those that the system needs to use. During control panel operations, this process can entail a large number of calls, which creates problem in this callback usage for initialization. This is true if the call is made before the system boot is complete, that is when other services aren't available.

Minidrivers that service callbacks for more than one device should attempt to keep joystick identifiers tied to a single physical device, where possible, to avoid user confusion. You can implement this relatively easily during a single session, but is probably not necessary over reboots.

The four joystick-specific callbacks must be registered with the VJoyD VJOYD_Register_Device_Driver service before returning from processing the SYS_DYNAMIC_DEVICE_INIT message. EAX must point to the polling routine, EBX (the configuration handler), ECX (the capabilities callback), and EDX (the identification routine). An example of a joystick minidriver registration sequence is as follows:

| &nbsp; | &nbsp; |
|--|--|
| Mov | eax, offset32 _PollRoutine@8 |
| Mov | ebx, offset32 _CfgRoutine |
| Mov | ecx, offset32 _HWCapsRoutine@8 |
| Mov | edx, offset32 _JoyIdRoutine@8 |
| VxDcall | VJOYD_Register_Device_Driver |

In addition to the registration, a minidriver can perform any other initialization at this time. The joystick minidriver model doesn't require any specific actions in response to SYS_DYNAMIC_DEVICE_EXIT, though the VxD may still use it for final internal cleanup.
