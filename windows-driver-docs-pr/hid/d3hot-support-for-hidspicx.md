---
title: D3Hot Support for HidSpiCx devices
description: Describes the D3Hot support feature of HidSpiCx.
ms.date: 07/19/2022
---

# D3Hot Support for HID over SPI devices

Starting Windows 11 22H2, HidSpiCx provides support for a D3Hot power policy, allowing hardware accelerated controllers to support wake from D3. This increases support for hardware accelerated applications on buses such as PCI to allow the HidSpiCx device to remain armed for wake (in the HIDSPI SLEEP state) in the D3Hot power state, without going through a host initiated reset on return to D0.

## Behavior
Enabling the D3Hot power policy has the following effects:
- If a HIDSPI device goes to the HIDSPI `OFF` power state (not armed for wake), it will be reset when transitioning back to `D0` (HIDSPI `ON` power state)
- If a HIDSPI device goes to the HIDSPI `SLEEP` power state (armed for wake) in `D1` or `D2`, it will **not** be reset on `Dx` to `D0` transition (HIDSPI `ON` power state).
- If a HIDSPI device goes to the HIDSPI `SLEEP` power state (armed for wake) in `D3`:
    - If a `D3COLD_SUPPORT_INTERFACE` is exposed by the parent bus, and a call to the interface indicates that a `D3Cold` transition has occurred, the device will be reset on `D3Cold` to `D0` transition (HIDSPI `ON` power state).
    - If a `D3COLD_SUPPORT_INTERFACE` is exposed by the parent bus, and a call to the interface indicates that a `D3Cold` transition has **not** occurred, the device will **not** be reset on `D3Hot` to `D0` transition (HIDSPI `ON` power state).
    - If a `D3COLD_SUPPORT_INTERFACE` is **not** exposed by the parent bus, it is assumed the device does not support `D3Cold`, and it will **not** be reset on `D3` to `D0` transition.

Without the D3Hot power policy, the default behavior is:
- If a HIDSPI device goes to the HIDSPI `OFF` power state (not armed for wake), it will be reset when transitioning back to `D0` (HIDSPI `ON` power state)
- If a HIDSPI device goes to the HIDSPI `SLEEP` power state (armed for wake) in `D1` or `D2`, it will **not** be reset on `Dx` to `D0` transition (HIDSPI `ON` power state).
- If a HIDSPI device goes to the HIDSPI `SLEEP` (armed for wake) or `OFF` power state (not armed for wake) in `D3`, it **will be reset** on `D3` to `D0` transition (HIDSPI `ON` power state).

## Configuration
To use the D3Hot power policy, HidSpiCx client drivers may opt-in by adding the `UseD3HotPowerPolicy` registry value under the device's hardware key.

In the INF file that installs the HidSpiCx client HWA driver, use the **[AddReg Directive](../install/inf-addreg-directive.md)**.

```
[EXAMPLE_DEVICE.NT.AddReg]
HKR,,"UseD3HotPowerPolicy",0x00010001,1
```

All drivers which support use of the HIDSPI `SLEEP` power state (meaning device will be armed for wake) in D3 should enable `UseD3HotPowerPolicy` in their driver install INF.