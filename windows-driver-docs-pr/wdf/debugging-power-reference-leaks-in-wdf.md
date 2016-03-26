---
title: Debugging Power Reference Leaks in WDF
description: When a Windows Driver Frameworks (WDF) driver calls WdfDeviceStopIdle, the framework increments the device's power reference count.
ms.assetid: 25F4EEBB-4733-498C-8704-8E015F81FE06
---

# Debugging Power Reference Leaks in WDF


When a Windows Driver Frameworks (WDF) driver calls [**WdfDeviceStopIdle**](https://msdn.microsoft.com/library/windows/hardware/ff546921), the framework increments the device's power reference count. Every successful call to **WdfDeviceStopIdle** must be matched by a call to [**WdfDeviceResumeIdle**](https://msdn.microsoft.com/library/windows/hardware/ff546838) to decrement the power reference count.

Starting in Kernel-Mode Driver Framework (KMDF) 1.15 and User-Mode Driver Framework (UMDF) 2.15, you can monitor power reference usage by using the [**!wdfkd.wdfdevice**](https://msdn.microsoft.com/library/windows/hardware/ff565703) and [**!wdfkd.wdftagtracker**](https://msdn.microsoft.com/library/windows/hardware/ff566126) debugger extensions. This functionality is disabled by default for performance reasons, so you need to turn it on with the WdfVerifier application or by manually editing the driver’s service key.

## WdfVerifier


Open the settings list for your driver and right-click the **TrackPower** setting. Choose the option appropriate for your scenario.

**Tip**  Avoid capturing stack traces in performance-critical code paths.

 

![setting track power references in wdfverifier](images/wdfverifier--track-power-references-on.png)

## Editing the Registry


You can also turn on Verifier support and power reference tracking by editing your driver’s service key.

For a KMDF driver:

**HKLM\\SYSTEM\\ControlSet001\\Services\\&lt;Driver Service Name&gt;\\Parameters\\Wdf**

For a UMDF driver:

**HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\WUDF\\Services\\&lt;Driver Service Name&gt;\\Parameters\\Wdf**

``` syntax
(REG_DWORD) VerifierOn = 0x1
(REG_DWORD) TrackPower = 0x0 (disabled)
                       = 0x1 (capture tick count, file name, line number)
                       = 0x2 (capture tick count, file name, line number, and stack traces)
```

## Driver Code


Drivers call [**WdfDeviceStopIdle**](https://msdn.microsoft.com/library/windows/hardware/ff546921) and [**WdfDeviceResumeIdle**](https://msdn.microsoft.com/library/windows/hardware/ff546838) to manage the device’s working power state as follows:

```
//
// Take power reference
//
status = WdfDeviceStopIdle(device, FALSE);
if (NT_SUCCESS(status)) {
    //
    // Release power reference
    //
    WdfDeviceResumeIdle(device);
}
```

## Debugging with WdfKd


To display the power references taken on the device, as well as a tag tracker that shows the reference history, use [**!wdfkd.wdfdevice**](https://msdn.microsoft.com/library/windows/hardware/ff565703) with verbose flags:

``` syntax
kd> !wdfkd.wdfdevice 0x6d939790 ff
Power references: 0 !wdftagtracker 0x9ea030a8
```

Calling the [**!wdfkd.wdftagtracker**](https://msdn.microsoft.com/library/windows/hardware/ff566126) shows the device’s power reference history:

``` syntax
kd> !wdftagtracker 0x9ea030a8
Reference and Release History:
# (showing most recent first; refcount is approximate in multi-threaded scenarios)

## 3 entries, history depth is 25

(--) 0 ref: Tag '....' at Time 0x1331e ticks
##      path\to\your\driver\code.c @ 374

(++) 1 refs: Tag '....' at Time 0x1331e ticks
##      path\to\your\driver\code.c @ 372

(++) Initial Tag '....' at Time 0x12c9a ticks
```

## Specifying a Tag


Optionally, specify a tag name to facilitate identification of specific power references. To do so, use [**WdfDeviceStopIdleWithTag**](https://msdn.microsoft.com/library/windows/hardware/dn932460) and [**WdfDeviceResumeIdleWithTag**](https://msdn.microsoft.com/library/windows/hardware/dn932459):

``` syntax
status = WdfDeviceStopIdleWithTag(device, FALSE, (PVOID)'oyeH');
if (NT_SUCCESS(status)) {
    WdfDeviceResumeIdleWithTag(device, (PVOID)'oyeH');
}
```

Corresponding [**!wdftagtracker**](https://msdn.microsoft.com/library/windows/hardware/ff566126) sample output:

``` syntax
(--) 0 ref: Tag 'Heyo' at Time 0x24e40 ticks
##      path\to\your\driver\code.c @ 374

(++) 1 refs: Tag 'Heyo' at Time 0x24e40 ticks
##      path\to\your\driver\code.c @ 372

(++) Initial Tag '....' at Time 0x12c9a ticks
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20Debugging%20Power%20Reference%20Leaks%20in%20WDF%20%20RELEASE:%20%283/24/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




