---
title: Audio Device Class Inactivity Timer Implementation
description: Audio Device Class Inactivity Timer Implementation
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
ms.date: 09/29/2022
---

# Audio Device Class Inactivity Timer Implementation


## <span id="audio_device_class_inactivity_timer_implementation"></span><span id="AUDIO_DEVICE_CLASS_INACTIVITY_TIMER_IMPLEMENTATION"></span>


The PortCls system driver utilizes the system's power-idle detection capabilities to implement an inactivity timer for its audio clients. PortCls programs two time-out values and a desired idle power state into the timer when it initializes it. PortCls monitors any accesses (such as I/O and property accesses) of the device and effectively resets the timer count on each access. If the timer times out, the system requests a power IRP to place the device in the desired idle state. After the device has been placed in the idle state, PortCls will power the device back up in the event of new access activity.

PortCls contains hard-coded default values for the idle time-outs and the idle power state. Hardware vendors can optionally override the default values by writing their own values to driver-specific keys in the system registry. In this way, vendors can select the power-idle parameter values that are best-suited to their devices.

Vendors can override the default values of the following power-idle parameters:

-   *ConservationIdleTime*

    This parameter specifies the idle time-out interval when the system is running in power-conservation mode. This is the mode that is typically used when the system is running on battery power. The default value for this parameter is 0, which disables the power-idle timer in conservation mode. The hardware vendor can set the value using an inf file like this.

    ```inf
    [MyAudioDevice.AddReg]
    HKR,PowerSettings,ConservationIdleTime,%REG_BINARY%,1e,00,00,00
    ```

The preceding INF file fragment shows a hexadecimal (hex) value of "1e" for the *ConservationIdleTime*, and this equates to a 30-second idle timeout.
 
FLG_ADDREG_BINVALUETYPE

The other parameters are used to control how the registry key is added. For example %REG_BINARY% indicates that the data is stored as  "raw" data. For more information, see [INF AddReg directive](../install/inf-addreg-directive.md). 

-   *PerformanceIdleTime*

    This parameter specifies the idle time-out interval when the system is running in performance mode. This is the mode that is typically used when the system is running on AC power. The default value for this parameter is 0, which disables the power-idle timer in performance mode. 

    The hardware vendor can set the value using an inf file like this.

    ```inf
    [MyAudioDevice.AddReg]
    HKR,PowerSettings,PerformanceIdleTime,%REG_BINARY%,2c,01,00,00
    ```
    The value of the key specifies the time-out interval in seconds. In this example, the value of 2c,01 will be 300 seconds, or five minutes.

-   *IdlePowerState*

    This parameter specifies the power state that the device will be placed in if the idle time-out period expires. The default value for this parameter is 3, corresponding to device power state D3, which is the lowest-powered device low-power state. The hardware vendor can set the value using an inf file like this.

    ```inf
    [MyAudioDevice.AddReg]
    HKR,PowerSettings,IdlePowerState,%REG_BINARY%,03,00,00,00
    ```
    The value placed in the key should be 0, 1, 2, or 3, corresponding to device power state D0, D1, D2, or D3, respectively.

The three power-idle registry keys exist only if the device-installation INF file creates them. Before configuring the power-idle timer, PortCls attempts to retrieve the driver-specific power-idle parameters from the registry. PortCls uses the default values in place of any power-idle parameters it does not find in the registry. As explained previously, the default power-idle parameter values disable the idle timer.

For more information about specifying the *ConservationIdleTime*, *PerformanceIdleTime*, and *IdlePowerState* parameters, see the definitions of the last three call parameters in [**PoRegisterDeviceForIdleDetection**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-poregisterdeviceforidledetection).

### <span id="example"></span><span id="EXAMPLE"></span> Example

For example, a hardware vendor might want to specify the following power-idle parameters for an audio device: *ConservationIdleTime* = 0x0000001e (30 seconds), *PerformanceIdleTime* = 0x0000012c (300 seconds), and *IdlePowerState* = 0x00000003 (device power state D3). To enable these settings, the device-installation file can include an [**INF AddReg section**](../install/inf-addreg-directive.md) containing the following directives:

```inf
[MyAudioDevice.AddReg]
HKR,PowerSettings,ConservationIdleTime,%REG_BINARY%,1e,00,00,00
HKR,PowerSettings,PerformanceIdleTime,%REG_BINARY%,2c,01,00,00
HKR,PowerSettings,IdlePowerState,%REG_BINARY%,03,00,00,00
```
## See also

[**PoRegisterDeviceForIdleDetection**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-poregisterdeviceforidledetection)
