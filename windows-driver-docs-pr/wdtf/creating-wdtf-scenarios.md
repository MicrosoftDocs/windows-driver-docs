---
title: Creating WDTF Scenarios
description: With WDTF scenarios, you build device-focused automated and customized test scenarios using the WDTF framework.
keywords:
- Windows Device Testing Framework WDK , scripts
- WDTF WDK , scripts
- scripts WDK WDTF
- test scripts WDK WDTF
- phantom devices WDK WDTF
- removed devices WDK WDTF
- hot-swapped devices WDK WDTF
ms.date: 04/20/2017
---

# Creating WDTF Scenarios


You can begin your WDTF-based scenarios by creating an instance of the [**IWDTF2**](/windows-hardware/drivers/ddi/index) aggregation interface, which contains [**DeviceDepot**](/windows-hardware/drivers/ddi/wdtf/nf-wdtf-iwdtf2-get_devicedepot) and [**SystemDepot**](/windows-hardware/drivers/ddi/wdtf/nf-wdtf-iwdtf2-get_systemdepot) properties.

To collect one or more target objects, use the [**IWDTFDeviceDepot2**](/windows-hardware/drivers/ddi/wdtf/nn-wdtf-iwdtfdevicedepot2) interface, and use the **Query** method with the [Simple Data Evaluation Language](simple-data-evaluation-language-overview.md) (SDEL).

A script might also examine specific targets by using the [**IWDTFTarget2::Eval**](/windows-hardware/drivers/ddi/wdtf/nf-wdtf-iwdtftarget2-eval) method. After you choose the targets, control them by using [one or more action interfaces](controlling-targets.md).

Before you start to develop WDTF scenarios, you must install WDTF. See [WDTF Quick Start](wdtf-quick-start-.md) for more information.

The following sections in this topic describe how to create basic WDTF scenarios.

### Simple WDTF Scenario

The following VBScript code sample (WDTF\_Sample1.vbs) shows a simplified scenario that uses WDTF to enable and disable every non-phantom device. A *non-phantom device* is any physically present device. For complete samples, see [Sample WDTF Scenarios](sample-wdtf-scenarios.md).

```cpp
Set WDTF = WScript.CreateObject("WDTF.WDTF")
For Each Device In WDTF.DeviceDepot.Query("IsPhantom=false AND IsDisableable")
    On Error Resume Next
    Set DevMan = Device.GetInterface("DeviceManagement")
    If err <> 0 Then
 DevMan.Disable()
 DevMan.Enable()
    End If
Next
```

You can run this scenario by running **CScript.exe WDTF\_Sample1.vbs**.

### Storing Target Information by Using Context

Some programming languages, such as VBScript, do not easily manage object references. To simplify this management in WDTF, each target provides a [**Context**](/windows-hardware/drivers/ddi/wdtf/nf-wdtf-iwdtftarget2-put_context) property that you can use to store arbitrary key/value pairs, including references to active objects. This property is especially useful for storing action interfaces so you can use them later. The following VBScript code example stores an [**IWDTFSimpleIOStressAction2**](/windows-hardware/drivers/ddi/wdtfinterfaces/nn-wdtfinterfaces-iwdtfsimpleiostressaction2) action within a named **Context** item.

```cpp
deviceObj.Context("IWDTFSimpleIOStressAction2") = SimpleIOObj
```

Later, your scenario can stop, pause, or restart the [**IWDTFSimpleIOStressAction2**](/windows-hardware/drivers/ddi/wdtfinterfaces/nn-wdtfinterfaces-iwdtfsimpleiostressaction2) interface by accessing it through [**Context**](/windows-hardware/drivers/ddi/wdtf/nf-wdtf-iwdtftarget2-put_context) again, as the following code example shows.

```cpp
Device.Context("IWDTFSimpleIOStressAction2").Stop
```

### Detecting Phantom Devices

Phantom devices are devices that were physically installed on the computer in the past but are not currently present. For example, a phantom device may be a USB mouse that has been unplugged. To speed up and simplify re-installation of a device that is plugged into a computer that is turned on, or removed devices, the Windows operating system keeps the device drivers installed but marks the device as a phantom.

Device-type targets include an **IsPhantom** attribute (and **IsAttached** attribute, which is equivalent to **IsPhantom**=false) that specifies the hardware's physical presence. The following VBScript code example lists a collection of all devices that are physically present in the computer.

```cpp
Set NonPhantomDevices = WDTF.DeviceDepot.Query ("IsAttached")
```

For more attribute keywords, see [SDEL Tokens](/windows-hardware/drivers/ddi/index).

 

