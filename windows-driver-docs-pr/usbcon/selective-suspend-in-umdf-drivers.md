---
Description: This topic describes how UMDF function drivers support USB selective suspend.
title: Selective suspend in USB UMDF drivers
ms.date: 05/09/2018
ms.localizationpriority: medium
---

# Selective suspend in USB UMDF drivers


**Important APIs**

-   [**IWDFUsbTargetDevice::SetPowerPolicy**](https://msdn.microsoft.com/library/windows/hardware/ff560385)
-   [**IWDFDevice2::AssignSxWakeSettings**](https://msdn.microsoft.com/library/windows/hardware/ff556923)
-   [**IWDFDevice2::AssignS0IdleSettings**](https://msdn.microsoft.com/library/windows/hardware/ff556920)

This topic describes how UMDF function drivers support USB selective suspend.

UMDF function drivers can support USB selective suspend in either of two ways:

-   By claiming power policy ownership and handling device idle power-down and resume.
-   By relying on the WinUSB.sys driver, which Microsoft supplies, to handle selective suspend. WinUSB.sys is installed as part of the kernel-mode device stack during the installation of the UMDF USB driver. WinUSB.sys implements the underlying mechanisms for suspending and resuming USB device operation.

Both approaches require only small amounts of code. The IdleWake sample that is provided in the WDK shows how to support selective suspend in a UMDF USB driver. You can find this sample in %WinDDK%\\BuildNumber\\Src\\Usb\\OsrUsbFx2\\ UMDF\\Fx2\_Driver\\IdleWake. The folder contains both PPO and non-PPO versions of the sample.

UMDF drivers that support selective suspend must follow these guidelines:

-   The UMDF driver can claim power policy ownership for its device stack, but is not required to do so. By default, the underlying WinUSB.sys driver owns power policy.
-   A UMDF driver that supports selective suspend and is the PPO can use power-managed queues or queues that are not power-managed. A UMDF driver that supports selective suspend but is not the PPO must not use power-managed queues.

## Power policy ownership in UMDF USB drivers


By default, WinUSB.sys is the PPO for a device stack that contains a UMDF USB driver. Starting with WDF 1.9, UMDF-based USB drivers can claim power policy ownership. Because only one driver in each device stack can be the PPO, a UMDF USB driver that is the PPO must explicitly disable power policy ownership in WinUSB.sys.

**To claim power policy ownership in a UMDF USB driver**

1.  Call **IWDFDeviceInitialize::SetPowerPolicyOwnership** and pass **TRUE**, typically from the **IDriverEntry::OnDeviceAdd** method on the driver callback object. For example:

    ``` syntax
    FxDeviceInit->SetPowerPolicyOwnership(TRUE);
    ```

2.  Disable power policy ownership in WinUSB. In the driver’s INF file, include an **AddReg** directive that sets the **WinUsbPowerPolicyOwnershipDisabled** value in the registry to a nonzero value. The **AddReg** directive must appear in a DDInstall.HW section. For example:

    ``` syntax
    [MyDriver_Install.NT.hw]
    AddReg=MyDriver_AddReg

    [MyDriver_AddReg]
    HKR,,"WinUsbPowerPolicyOwnershipDisabled",0x00010001,1
    ```

UMDF USB drivers that support selective suspend and are built with WDF versions earlier than 1.9 must not claim power policy ownership. With these earlier versions of WDF, USB selective suspend works properly only if WinUSB.sys is the PPO.

## I/O queues in UMDF USB drivers


For a UMDF driver that supports selective suspend, whether the UMDF driver owns power policy for its device determines the type of I/O queues that it can use. UMDF drivers that support selective suspend and are PPOs can use queues that are either power managed or not power managed. UMDF USB drivers that support selective suspend but are not the PPO should not use any power-managed I/O queues.

If an I/O request arrives for a power-managed queue while the device is suspended, the framework does not present the request unless the driver is PPO, as shown in image in the [Selective suspend in USB drivers](https://msdn.microsoft.com/library/windows/hardware/dn449739). If the UMDF driver is not the PPO for the device, the framework cannot power up the device on its behalf. As a result, the request remains stuck in the power-managed queue. The request never reaches WinUSB, so WinUSB cannot power up the device. Consequently, the device stack can stall.

If the queue is not power managed, the framework presents I/O requests to the UMDF driver even when the device is powered down. The UMDF driver formats the request and forwards it down the device stack to the default I/O target in the usual way. Special code is not required. When the request reaches the PPO (WinUSB.sys), WinUSB.sys powers up the device and performs the required I/O operation.

The sample driver in **%WinDDK%\\BuildNumber\\Src\\Usb\\OsrUsbFx2\\umdf\\Fx2\_Driver\\IdleWake** defines the constant \_NOT\_POWER\_POLICY\_OWNER\_ when you build the non-PPO version of the driver. When the driver creates a queue for read and write requests, it determines whether to create a power-managed queue by checking for the constant.

To create the queue, the driver calls the driver-defined **CMyQueue::Initialize** method, which takes the following three parameters:

-   *DispatchType*, a WDF\_IO\_QUEUE\_DISPATCH\_TYPE enumeration value that indicates how the queue dispatches requests.
-   *Default*, a Boolean that indicates whether the queue is a default queue.
-   *PowerManaged*, a Boolean that indicates whether the queue is power managed.

The following code snippet shows the driver’s call to the **CMyQueue::Initialize** method as part of read-write queue creation:

```cpp
#if defined(_NOT_POWER_POLICY_OWNER_)
    powerManaged = false;
#else
    powerManaged = true;
#endif  
hr = __super::Initialize(WdfIoQueueDispatchParallel,
                         true,
                         powerManaged,
                         );
```

**CMyQueue::Initialize** then calls [**IWDFDevice::CreateIoQueue**](https://msdn.microsoft.com/library/windows/hardware/ff557020) to create the queue as follows:

```cpp
hr = m_FxDevice->CreateIoQueue(
                               callback,
                               Default,
                               DispatchType,
                               PowerManaged,
                               FALSE,
                               &fxQueue
                               );
```

This code sequence results in a default queue that dispatches requests in parallel. If the driver is the PPO the queue is power managed, and if the driver is not the PPO, the queue is not power managed.

## Supporting USB selective suspend in a UMDF PPO


To support selective suspend, a UMDF USB driver that is the PPO for its device stack must do the following:

1.  Claim power policy ownership for the device stack, typically in the [**IDriverEntry::OnDeviceAdd**](https://msdn.microsoft.com/library/windows/hardware/ff554896) method on its driver callback object, as described earlier.
2.  Enable selective suspend by calling the [**IWDFDevice2::AssignS0IdleSettings**](https://msdn.microsoft.com/library/windows/hardware/ff556920) method on the framework device object.

**To enable USB selective suspend from a PPO**

-   Call [**IWDFDevice2::AssignS0IdleSettings**](https://msdn.microsoft.com/library/windows/hardware/ff556920), typically from the **OnPrepareHardware** method on the device callback object. Set the parameters to AssignS0IdleSettings as follows:
    -   *IdleCaps* to **IdleUsbSelectiveSuspend**.
    -   *DxState* to the device sleep state to which the framework transitions the idle device. For USB selective suspend, specify **PowerDeviceMaximum**, which indicates that the framework should use the value that the bus driver specified.
    -   *IdleTimeout* to the number of milliseconds that the device must be idle before the framework transitions it to *DxState*.
    -   *UserControlOfIdleSettings* to **IdleAllowUserControl** if your driver allows users to manage the idle settings, or otherwise to **IdleDoNotAllowUserControl**.
    -   *Enabled* to **WdfUseDefault** to enable selective suspend by default, but to allow the user’s setting to override the default.

The following example shows how the IdleWake\_PPO driver calls this method in its internal CMyDevice::SetPowerManagement method:

```cpp
hr = m_FxDevice->AssignS0IdleSettings( IdleUsbSelectiveSuspend,
                                PowerDeviceMaximum,
                                IDLE_TIMEOUT_IN_MSEC,
                                IdleAllowUserControl,
                                WdfUseDefault);                                                                                                   
```

If the device hardware can generate a wake signal, the UMDF driver can also support system wake from S1, S2, or S3. For details, see [System Wake in a UMDF Driver](#systemwake).

## Supporting USB selective suspend in a non-PPO UMDF driver


A UMDF function driver that is not the PPO can support selective suspend by using the features of the underlying WinUSB.sys driver. The UMDF driver must notify WinUSB that the device and driver support selective suspend and must enable selective suspend either in the INF file or by setting power policy on the USB target device object.

If a UMDF function driver enables selective suspend, the underlying WinUSB.sys driver determines when the device is idle. WinUSB starts an idle time-out counter when no transfers are pending or when the only pending transfers are IN transfers on an interrupt or bulk endpoint. By default, the idle time-out is 5 seconds, but the UMDF driver can change this default.

When WinUSB.sys determines that the device is idle, it sends a request to suspend the device down the kernel-mode device stack. The bus driver changes the state of the hardware as appropriate. If all device functions on the port have been suspended, the port enters the USB selective suspend state.

If an I/O request arrives at WinUSB.sys while the device is suspended, WinUSB.sys resumes device operation if the device must be powered up to service the request. The UMDF driver does not require any code to resume the device while the system remains in S0. If the device hardware can generate a wake signal, the UMDF driver can also support system wake from S1, S2, or S3. For details, see [System Wake in a UMDF Driver](#systemwake).

A UMDF driver that is not the PPO can support selective suspend by taking the following two steps:

1.  Notifying WinUSB.sys that the device and driver support selective suspend.
2.  Enabling USB selective suspend.

In addition, the driver can optionally:

-   Set a time-out value for the device.
-   Allow the user to enable or disable selective suspend.

For an example of how to implement USB selective suspend in a UMDF USB function driver that is not the PPO, see the Fx2\_Driver sample in the WDK. This sample is located at **%WinDDK%\\BuildNumber\\Src\\Usb\\OsrUsbFx2\\Umdf\\Fx2\_Driver\\ IdleWake\_Non-PPO**.

**To notify WinUSB about selective suspend support**

To notify WinUSB.sys that the device can support USB selective suspend, the device INF must add the DeviceIdleEnabled value to the device’s hardware key and set the value to 1. The following example shows how the Fx2\_Driver sample adds and sets this value in the WUDFOsrUsbFx2\_IdleWakeNon-PPO.Inx file:

```cpp
[OsrUsb_Device_AddReg]
...
HKR,,"DeviceIdleEnabled",0x00010001,1
```

**To enable USB selective suspend**

A UMDF USB driver can enable USB selective suspend either at runtime or during installation in the INF.

-   To enable support at runtime, the function driver calls [**IWDFUsbTargetDevice::SetPowerPolicy**](https://msdn.microsoft.com/library/windows/hardware/ff560385) and sets the PolicyType parameter to AUTO\_SUSPEND and the Value parameter to TRUE or 1. The following example shows how the Fx2\_Driver sample enables selective suspend in the DeviceNonPpo.cpp file:
    ```cpp
    BOOL AutoSuspend = TRUE;
    hr = m_pIUsbTargetDevice->SetPowerPolicy( AUTO_SUSPEND,
                                              sizeof(BOOL),
                                             (PVOID) &AutoSuspend );
    ```

-   To enable support during installation, the INF includes an AddReg directive that adds the DefaultIdleState value to the device’s hardware key and sets the value to 1. For example:
    ```cpp
    HKR,,"DefaultIdleState",0x00010001,1
    ```

**To set an idle time-out value**

By default, WinUSB suspends the device after 5 seconds if no transfers are pending or if the only pending transfers are IN transfers on an interrupt or bulk endpoint. A UMDF driver can change this idle time-out value either at installation in the INF or at runtime.

-   To set an idle time-out at installation, the INF includes an AddReg directive that adds the DefaultIdleTimeout value to the device’s hardware key and sets the value to the time-out interval in milliseconds. The following example sets the time-out to 7 seconds:
    ```cpp
    HKR,,"DefaultIdleTimeout",0x00010001,7000
    ```

-   To set an idle time-out at runtime, the driver calls **IWDFUsbTargetDevice::SetPowerPolicy** with PolicyType set to SUSPEND\_DELAY and Value to the idle time-out value, in milliseconds. In the following example from the Device.cpp file, the Fx2\_Driver sample sets the time-out to 10 seconds:
    ```cpp
    HRESULT hr;
    ULONG value;
    value = 10 * 1000;
    hr = m_pIUsbTargetDevice->SetPowerPolicy( SUSPEND_DELAY,
                                              sizeof(ULONG),
                                             (PVOID) &value );
    ```

**To provide user control of USB selective suspend**

UMDF USB drivers that use WinUSB selective suspend support can optionally allow the user to enable or disable selective suspend. To do so, include an AddReg directive in the INF that adds the UserSetDeviceIdleEnabled value to the device’s hardware key and sets the value to 1. The following shows the string to use for the AddReg directive:

```cpp
HKR,,"UserSetDeviceIdleEnabled",0x00010001,1
```

If UserSetDeviceIdleEnabled is set, the device’s Properties dialog box includes a Power Management tab that allows the user to enable or disable USB selective suspend.

## System wake in a UMDF driver


In a UMDF driver, support for system wake is independent of support for selective suspend. A UMDF USB driver can support both system wake and selective suspend, neither system wake nor selective suspend, or either system wake or selective suspend. A device that supports system wake can wake the system from a sleep state (S1, S2, or S3).

A UMDF USB PPO driver can support system wake by providing wake-up information for the framework’s driver object. When an external event triggers system wake, the framework returns the device to the working state.

A USB non-PPO driver can use the system wake support that the WinUSB.sys driver implements.

**To support system wake in a UMDF USB driver that is the PPO**

Call the [**IWDFDevice2::AssignSxWakeSettings**](https://msdn.microsoft.com/library/windows/hardware/ff556923) method on the framework’s device object with the following parameters:

-   *DxState* to the power state to which the device transitions when the system enters a wakeable Sx state. For USB devices, specify **PowerDeviceMaximum** to use the value that the bus driver specified.
-   *UserControlOfWakeSettings* to **WakeAllowUserControl** if your driver allows users to manage the wake settings or otherwise to **WakeDoNotAllowUserControl.**
-   *Enabled* to **WdfUseDefault** to enable wake by default, but to allow the user’s setting to override the default.

The following example shows how the IdleWake\_PPO driver calls this method in its internal **CMyDevice::SetPowerManagement** method:

```cpp
hr = m_FxDevice->AssignSxWakeSettings( PowerDeviceMaximum,
                                       WakeAllowUserControl,
                                       WdfUseDefault);
```

**To enable system wake through WinUSB in a non-PPO Driver**

To enable system wake through WinUSB, the driver’s INF adds the registry value SystemWakeEnabled to the device’s hardware key and sets it to 1. The IdleWake\_Non-PPO sample enables system wake as follows:

```cpp
[OsrUsb_Device_AddReg]
...
HKR,,"SystemWakeEnabled",0x00010001,1
```

By setting this value, the driver both enables system wake and allows the user to control the ability of the device to wake the system. In Device Manager, the power management settings property page for the device includes a check box with which the user can enable or disable system wake.

## Related topics
[Selective suspend in USB drivers (WDF)](selective-suspend-in-usb-drivers-wdf.md)  



