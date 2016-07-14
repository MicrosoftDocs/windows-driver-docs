---
Description: Audio Device Class Inactivity Timer Implementation
MS-HAID: 'audio.audio\_device\_class\_inactivity\_timer\_implementation'
MSHAttr: 'PreferredLib:/library/windows/hardware'
title: Audio Device Class Inactivity Timer Implementation
---

# Audio Device Class Inactivity Timer Implementation


## <span id="audio_device_class_inactivity_timer_implementation"></span><span id="AUDIO_DEVICE_CLASS_INACTIVITY_TIMER_IMPLEMENTATION"></span>


In Windows Server 2003 SP1, Windows XP SP2, and later, the PortCls system driver utilizes the system's power-idle detection capabilities to implement an inactivity timer for its audio clients. PortCls programs two time-out values and a desired idle power state into the timer when it initializes it. PortCls monitors any accesses (such as I/O and property accesses) of the device and effectively resets the timer count on each access. If the timer times out, the system requests a power IRP to place the device in the desired idle state. After the device has been placed in the idle state, PortCls will power the device back up in the event of new access activity.

PortCls contains hard-coded default values for the idle time-outs and the idle power state. Hardware vendors can optionally override the default values by writing their own values to driver-specific keys in the system registry. In this way, vendors can select the power-idle parameter values that are best-suited to their devices.

Vendors can override the default values of the following power-idle parameters:

-   *ConservationIdleTime*

    This parameter specifies the idle time-out interval when the system is running in power-conservation mode. This is the mode that is typically used when the system is running on battery power. The default value for this parameter is 0, which disables the power-idle timer in conservation mode. The hardware vendor can override the default by writing a DWORD value to the following driver-specific registry key:

    ```
    \HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Class\xxxx\yyyy\PowerSettings\ConservationIdleTime
    ```

    Note that *xxxx* represents the Media class GUID (see [System-Supplied Device Setup Classes](devinst.system_defined_device_setup_classes)) and *yyyy* represents the name of the driver's subkey under the Media class GUID. The value of the key specifies the time-out interval in seconds.

-   *PerformanceIdleTime*

    This parameter specifies the idle time-out interval when the system is running in performance mode. This is the mode that is typically used when the system is running on AC power. The default value for this parameter is 0, which disables the power-idle timer in performance mode. The hardware vendor can override the default by writing a DWORD value to the following driver-specific registry key:

    ```
    \HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Class\xxxx\yyyy\PowerSettings\PerformanceIdleTime
    ```

    Again, *xxxx* represents the Media class GUID and *yyyy* represents the name of the driver's subkey. The value of the key specifies the time-out interval in seconds.

-   *IdlePowerState*

    This parameter specifies the power state that the device will be placed in if the idle time-out period expires. The default value for this parameter is 0, corresponding to device power state D0 (full power). The hardware vendor can override the default by writing a DWORD value to the following driver-specific registry key:

    ```
    \HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Class\xxxx\yyyy\PowerSettings\IdlePowerState
    ```

    Again, *xxxx* represents the Media class GUID and *yyyy* represents the name of the driver's subkey. The value placed in the key should be 0, 1, 2, or 3, corresponding to device power state D0, D1, D2, or D3, respectively.

The three power-idle registry keys exist only if the device-installation INF file creates them. Before configuring the power-idle timer, PortCls attempts to retrieve the driver-specific power-idle parameters from the registry. PortCls uses the default values in place of any power-idle parameters it does not find in the registry. As explained previously, the default power-idle parameter values disable the idle timer.

For more information about specifying the *ConservationIdleTime*, *PerformanceIdleTime*, and *IdlePowerState* parameters, see the definitions of the last three call parameters in [**PoRegisterDeviceForIdleDetection**](kernel.poregisterdeviceforidledetection).

### <span id="example"></span><span id="EXAMPLE"></span> Example

For example, a hardware vendor might want to specify the following power-idle parameters for an audio device: *ConservationIdleTime* = 0x0000001e (30 seconds), *PerformanceIdleTime* = 0x0000012c (300 seconds), and *IdlePowerState* = 0x00000003 (device power state D3). To enable these settings, the device-installation file can include an [**INF AddReg section**](devinst.inf_addreg_directive) containing the following directives:

```
[MyAudioDevice.AddReg]
HKR,PowerSettings,ConservationIdleTime,1,1e,00,00,00
HKR,PowerSettings,PerformanceIdleTime,1,2c,01,00,00
HKR,PowerSettings,IdlePowerState,1,03,00,00,00
```

HKR represents the driver's root key in the registry:

```
\HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Class\xxxx\yyyy
```

Again, *xxxx* represents the Media class GUID and *yyyy* represents the name of the driver's subkey. The **PowerSettings** subkey is specified relative to the path name for the root key.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20Audio%20Device%20Class%20Inactivity%20Timer%20Implementation%20%20RELEASE:%20%287/14/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")



