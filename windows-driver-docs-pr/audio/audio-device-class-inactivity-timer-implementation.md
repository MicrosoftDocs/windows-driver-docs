---
title: Audio Device Class Inactivity Timer Implementation
description: Audio Device Class Inactivity Timer Implementation
ms.assetid: e7e431ec-626d-4fdb-8705-fc5420c43f17
keywords:
- inactivity timers WDK audio
- timers WDK audio
- power-idle detection WDK audio
- idle power states WDK audio
- idle time-outs WDK audio
- time-out intervals WDK audio
- power-conservation mode WDK audio
- conservation power mode WDK audio
- performance power mode WDK audio
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Audio Device Class Inactivity Timer Implementation


## <span id="audio_device_class_inactivity_timer_implementation"></span><span id="AUDIO_DEVICE_CLASS_INACTIVITY_TIMER_IMPLEMENTATION"></span>


In Windows Server 2003 SP1, Windows XP SP2, and later, the PortCls system driver utilizes the system's power-idle detection capabilities to implement an inactivity timer for its audio clients. PortCls programs two time-out values and a desired idle power state into the timer when it initializes it. PortCls monitors any accesses (such as I/O and property accesses) of the device and effectively resets the timer count on each access. If the timer times out, the system requests a power IRP to place the device in the desired idle state. After the device has been placed in the idle state, PortCls will power the device back up in the event of new access activity.

PortCls contains hard-coded default values for the idle time-outs and the idle power state. Hardware vendors can optionally override the default values by writing their own values to driver-specific keys in the system registry. In this way, vendors can select the power-idle parameter values that are best-suited to their devices.

Vendors can override the default values of the following power-idle parameters:

-   *ConservationIdleTime*

    This parameter specifies the idle time-out interval when the system is running in power-conservation mode. This is the mode that is typically used when the system is running on battery power. The default value for this parameter is 0, which disables the power-idle timer in conservation mode. The hardware vendor can override the default by writing a DWORD value to the following driver-specific registry key:

    ```inf
    \HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Class\xxxx\yyyy\PowerSettings\ConservationIdleTime
    ```

    Note that *xxxx* represents the Media class GUID (see [System-Supplied Device Setup Classes](https://msdn.microsoft.com/library/windows/hardware/ff553419)) and *yyyy* represents the name of the driver's subkey under the Media class GUID. The value of the key specifies the time-out interval in seconds.

-   *PerformanceIdleTime*

    This parameter specifies the idle time-out interval when the system is running in performance mode. This is the mode that is typically used when the system is running on AC power. The default value for this parameter is 0, which disables the power-idle timer in performance mode. The hardware vendor can override the default by writing a DWORD value to the following driver-specific registry key:

    ```inf
    \HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Class\xxxx\yyyy\PowerSettings\PerformanceIdleTime
    ```

    Again, *xxxx* represents the Media class GUID and *yyyy* represents the name of the driver's subkey. The value of the key specifies the time-out interval in seconds.

-   *IdlePowerState*

    This parameter specifies the power state that the device will be placed in if the idle time-out period expires. The default value for this parameter is 0, corresponding to device power state D0 (full power). The hardware vendor can override the default by writing a DWORD value to the following driver-specific registry key:

    ```inf
    \HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Class\xxxx\yyyy\PowerSettings\IdlePowerState
    ```

    Again, *xxxx* represents the Media class GUID and *yyyy* represents the name of the driver's subkey. The value placed in the key should be 0, 1, 2, or 3, corresponding to device power state D0, D1, D2, or D3, respectively.

The three power-idle registry keys exist only if the device-installation INF file creates them. Before configuring the power-idle timer, PortCls attempts to retrieve the driver-specific power-idle parameters from the registry. PortCls uses the default values in place of any power-idle parameters it does not find in the registry. As explained previously, the default power-idle parameter values disable the idle timer.

For more information about specifying the *ConservationIdleTime*, *PerformanceIdleTime*, and *IdlePowerState* parameters, see the definitions of the last three call parameters in [**PoRegisterDeviceForIdleDetection**](https://msdn.microsoft.com/library/windows/hardware/ff559721).

### <span id="example"></span><span id="EXAMPLE"></span> Example

For example, a hardware vendor might want to specify the following power-idle parameters for an audio device: *ConservationIdleTime* = 0x0000001e (30 seconds), *PerformanceIdleTime* = 0x0000012c (300 seconds), and *IdlePowerState* = 0x00000003 (device power state D3). To enable these settings, the device-installation file can include an [**INF AddReg section**](https://msdn.microsoft.com/library/windows/hardware/ff546320) containing the following directives:

```inf
[MyAudioDevice.AddReg]
HKR,PowerSettings,ConservationIdleTime,1,1e,00,00,00
HKR,PowerSettings,PerformanceIdleTime,1,2c,01,00,00
HKR,PowerSettings,IdlePowerState,1,03,00,00,00
```

HKR represents the driver's root key in the registry:

```inf
\HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Class\xxxx\yyyy
```

Again, *xxxx* represents the Media class GUID and *yyyy* represents the name of the driver's subkey. The **PowerSettings** subkey is specified relative to the path name for the root key.

 

 




