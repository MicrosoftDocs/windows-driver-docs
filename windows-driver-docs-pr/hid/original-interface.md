---
title: Original Interface
author: windows-driver-content
description: Original Interface
ms.assetid: 78f1e722-c2bd-4232-96f1-71df7e6ece23
keywords: ["joysticks WDK HID , interfaces", "virtual joystick drivers WDK HID , interfaces", "VJoyD WDK HID , interfaces", "interfaces WDK joysticks", "joysticks WDK HID , callbacks", "virtual joystick drivers WDK HID , callbacks", "VJoyD WDK HID , callbacks", "callbacks WDK joysticks", "polling WDK joysticks"]
---

#  Original Interface


## <a href="" id="ddk-the-original-interface-di"></a>


The following joystick minidriver callbacks are specific to the original interface:

-   A [Polling Callback](polling-callback.md) to return the joystick position and button information.

-   A [Configuration Manager Callback](configuration-manager-callback.md) to handle the configuration manager messages in Windows 95.

-   A [Hardware Capabilities Callback](hardware-capabilities-callback.md) to handle requests for joystick capabilities.

-   A [Joystick Identification Callback](joystick-identification-callback.md) used by VJoyD to inform a minidriver of the joysticks, which it should respond to.

The four joystick-specific callbacks must be registered with the VJoyD VJOYD\_Register\_Device\_Driver service before returning from processing the SYS\_DYNAMIC\_DEVICE\_INIT message. EAX must point to the polling routine, EBX (the configuration handler), ECX (the capabilities callback), and EDX (the identification routine). An example of a joystick minidriver registration sequence is as follows:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Mov</p></td>
<td><p>eax, offset32 _PollRoutine@8</p></td>
</tr>
<tr class="even">
<td><p>Mov</p></td>
<td><p>ebx, offset32 _CfgRoutine</p></td>
</tr>
<tr class="odd">
<td><p>Mov</p></td>
<td><p>ecx, offset32 _HWCapsRoutine@8</p></td>
</tr>
<tr class="even">
<td><p>Mov</p></td>
<td><p>edx, offset32 _JoyIdRoutine@8</p></td>
</tr>
<tr class="odd">
<td><p>VxDcall</p></td>
<td><p>VJOYD_Register_Device_Driver</p></td>
</tr>
</tbody>
</table>

 

In addition to the registration, a minidriver can perform any other initialization at this time. The joystick minidriver model does not require any specific actions in response to SYS\_DYNAMIC\_DEVICE\_EXIT, though the VxD may still use it for final internal clean up.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bhid\hid%5D:%20%20Original%20Interface%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


