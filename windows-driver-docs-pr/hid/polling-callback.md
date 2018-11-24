---
title: Polling Callback
description: Polling Callback
ms.assetid: d86ed391-19c6-47e4-83df-cc2f2298846a
keywords: ["polling WDK joysticks", "callbacks WDK joysticks", "joysticks WDK HID , polling", "virtual joystick drivers WDK HID , polling", "VJoyD WDK HID , polling", "joysticks WDK HID , positions", "locations WDK joysticks", "positions WDK joysticks"]
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# Polling Callback





```cpp
int stdcall PollRoutine( int type, LPJOYOEMPOLLDATA pojd );
```

The polling routine is called either in direct response to an application that calls joyGetPos or joyGetPosEx, or when Windows 95/98/Me periodically calls joyGetPos for an application that has called joySetCapture. Only when a minidriver first receives a call on its poll callback, it can be certain that an application requires data from it. All the other callbacks are called for all devices that are currently in the list of 16 available joysticks, whether any application has requested data.

The possible return values are JOY\_OEMPOLLRC\_YOUPOLL, JOY\_OEMPOLLRC\_FAIL, and JOY\_OEMPOLLRC\_OK. With the exception of a button-only poll, the return value is interpreted into either JOYERR\_NOERROR or JOYERR\_UNPLUGGED before being returned to an application. A button poll is always assumed to succeed.

JOY\_OEMPOLLRC\_FAIL is returned if the device that is polled does not respond, or if VJoyD requests a poll that the minidriver cannot process. In the former case, you should ensure not to fail a device unless it really has failed, because the application is likely to stop everything and request that the user check the connections to the device. For example, a call to joySetCapture fails if the first poll fails. Minor device failures should not result in failure report until user intervention is required or it detects an unrecoverable device error. For instance, a device that communicates using a packet-based protocol should attempt a retry before it fails the poll if one packet is not valid.

It is important to recognize genuine device failure and return an error eventually; otherwise, an application cannot determine whether the user intervention is required at all. If old or false data is returned while error recovery is performed, the meaning of data returned, the number of polls allowed, or the time allowed from the initial error should be restricted so the driver does not delay for an inordinate amount of time. When a minidriver is requested to perform a poll on a device that it does not control, or to perform a poll type or subtype that it cannot service, a failure is always the correct response.

You can use JOY\_OEMPOLLRC\_YOUPOLL if the standard analog poll yields the correct results.

You should return JOY\_OEMPOLLRC\_OK in a regular case when JOYINFOEX structure is filled with the requested data.

You must take care if you use poll to perform initialization on the device. Applications can perform an initial poll to check for the availability of the device by checking the return code. They can then make subsequent polls with no error checks. This is essentially what joySetCapture does. Ideally, all initialization and the first poll should be performed. For those cases in which the time required to set up the device lasts up to a second, it is sufficient to verify that the device is present and working and to return inert data for the first poll.

The API and system drivers perform validation on the request made by the application and copy the required data into the application structure upon completion. The minidriver should not replicate this functionality. However, nothing prevents one process from polling a device while another is still in the middle of a poll. The consequences of this event are no worse than different samples reporting the two axes. If necessary, a minidriver can perform its own process synchronization.

Return values depend upon the "type" parameter and the device it supports. You should always return the buttons and button number. Because there is no way to specify to the minidriver that a POV poll is required, you should return this value if any axes are requested. Set the POV\_UNDEFINED if the device does not support one. For a single axis poll, the value is returned in the **dwX** member of the JOYPOLLDATA structure (the [**VJPOLLDATA**](https://msdn.microsoft.com/library/windows/hardware/ff543573) structure in DirectX 5.0 and later). For a multiple axes request in which the number of axes requested is odd, the **do\_other** member of the [**JOYOEMPOLLDATA**](https://msdn.microsoft.com/library/windows/hardware/ff542251) structure specifies whether the last axis is returned in place or for the following axis. In a three-axis poll, for example, the member specifies whether the axes returned are X, Y, Z or X, Y, R.

The following is a list of other possible return values, categorized by type (you can fill in extra data, but note that all polls of an odd number of axes must decode the **do\_other** member to decide what it returns):

-   JOY\_OEMPOLL\_GETBUTTONS: Nothing extra.

-   JOY\_OEMPOLL\_POLL1: The axis specified in the **do\_other** member is returned in the **dwX** member.

-   JOY\_OEMPOLL\_POLL2: The X and Y axes are returned in the **dwX** and **dwY** members.

-   JOY\_OEMPOLL\_POLL3: The X and Y axes are returned in the **dwX** and **dwY** members.

    If the **do\_other** member is nonzero, the R axis is returned in the **dwR** member. Otherwise, the Z axis is returned in the **dwZ** member.

-   JOY\_OEMPOLL\_POLL4: The X, Y, Z and R axes are returned in the **dwX**, **dwY**, **dwZ**, and **dwR** members respectively.

-   JOY\_OEMPOLL\_POLL5: The X, Y, Z and R axes are returned in the **dwX**, **dwY**, **dwZ**, and **dwR** members respectively.

    If the **do\_other** member is nonzero, the V-axis is returned in the **dwR** member. Otherwise, the U-axis is returned in the **dwZ** member.

-   JOY\_OEMPOLL\_POLL6: The X, Y, Z, R, U and V axes are returned in the **dwX**, **dwY**, **dwZ**, **dwR**, **dwU**, and **dwV** members respectively.

DirectX 3.0 added the non-poll type of JOY\_OEMPASSDRIVERDATA, in which the **do\_other** member contains a DWORD that an application passes. You can use this DWORD for any minidriver-defined function, but it is intended in particular to enable custom setup applications that have fully identified the minidriver to send device-specific commands and configuration information.

A minidriver should return JOY\_OEMPOLLRC\_FAIL for all types it does not support.

Although the axis data is returned in double words, the range of axis values should be restricted to approximately 10-bit values if the standard joystick control panel configuration is used as the sole configuration mechanism. Because the user cannot easily see what is happening, this helps to avoid confusion. To aid compatibility with existing applications, the axes returned by a minidriver should be the same as those returned by an analog joystick (where applicable). For example, X would be a left-to-right movement minimized at the left, and so on.

For an activated POV hat, the direction should be represented as the angle, in degrees, multiplied by 100, with 0 being forward, 9000 right, 18000 backwards, and 27000 left.

Because the poll routine call is the only positive indication that the device is still in use, minidrivers that use shared resources such as communications ports should keep track of the last time they were used. If usage time becomes significant , the minidrivers should stop to sample the device and free the resources in case the user has completed the device usage and is now trying to use the resource for another purpose. This is particularly important if there are occurrences of communications errors, because this could be an indication that the device is unplugged.

 

 




