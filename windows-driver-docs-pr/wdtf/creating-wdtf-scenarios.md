---
title: Creating WDTF Scenarios
author: windows-driver-content
description: .
MS-HAID:
- 'wdtfdevguide\_2fa9104a-0c69-4ac5-8f31-347ea3976d8d.xml'
- 'dtf.creating\_wdtf\_scenarios'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: f9e3de20-28be-40c6-802c-f4637b3f6c20
keywords: ["Windows Device Testing Framework WDK , scripts", "WDTF WDK , scripts", "scripts WDK WDTF", "test scripts WDK WDTF", "phantom devices WDK WDTF", "removed devices WDK WDTF", "hot-swapped devices WDK WDTF"]
---

# Creating WDTF Scenarios


You can begin your WDTF-based scenarios by creating an instance of the [**IWDTF2**](https://msdn.microsoft.com/library/windows/hardware/ff539628) aggregation interface, which contains [**DeviceDepot**](https://msdn.microsoft.com/library/windows/hardware/hh406304) and [**SystemDepot**](https://msdn.microsoft.com/library/windows/hardware/hh406309) properties.

To collect one or more target objects, use the [**IWDTFDeviceDepot2**](https://msdn.microsoft.com/library/windows/hardware/hh406391) interface, and use the **Query** method with the [Simple Data Evaluation Language](simple-data-evaluation-language-overview.md) (SDEL).

A script might also examine specific targets by using the [**IWDTFTarget2::Eval**](https://msdn.microsoft.com/library/windows/hardware/hh439396) method. After you choose the targets, control them by using [one or more action interfaces](controlling-targets.md).

Before you start to develop WDTF scenarios, you must install WDTF. See [WDTF Quick Start](wdtf-quick-start-.md) for more information.

The following sections in this topic describe how to create basic WDTF scenarios.

### Simple WDTF Scenario

The following VBScript code sample (WDTF\_Sample1.vbs) shows a simplified scenario that uses WDTF to enable and disable every non-phantom device. A *non-phantom device* is any physically present device. For complete samples, see [Sample WDTF Scenarios](sample-wdtf-scenarios.md).

```
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

Some programming languages, such as VBScript, do not easily manage object references. To simplify this management in WDTF, each target provides a [**Context**](https://msdn.microsoft.com/library/windows/hardware/hh439393) property that you can use to store arbitrary key/value pairs, including references to active objects. This property is especially useful for storing action interfaces so you can use them later. The following VBScript code example stores an [**IWDTFSimpleIOStressAction2**](https://msdn.microsoft.com/library/windows/hardware/hh451157) action within a named **Context** item.

```
deviceObj.Context("IWDTFSimpleIOStressAction2") = SimpleIOObj
```

Later, your scenario can stop, pause, or restart the [**IWDTFSimpleIOStressAction2**](https://msdn.microsoft.com/library/windows/hardware/hh451157) interface by accessing it through [**Context**](https://msdn.microsoft.com/library/windows/hardware/hh439393) again, as the following code example shows.

```
Device.Context("IWDTFSimpleIOStressAction2").Stop
```

### Detecting Phantom Devices

Phantom devices are devices that were physically installed on the computer in the past but are not currently present. For example, a phantom device may be a USB mouse that has been unplugged. To speed up and simplify re-installation of a device that is plugged into a computer that is turned on, or removed devices, the Windows operating system keeps the device drivers installed but marks the device as a phantom.

Device-type targets include an **IsPhantom** attribute (and **IsAttached** attribute, which is equivalent to **IsPhantom**=false) that specifies the hardware's physical presence. The following VBScript code example lists a collection of all devices that are physically present in the computer.

```
Set NonPhantomDevices = WDTF.DeviceDepot.Query ("IsAttached")
```

For more attribute keywords, see [SDEL Tokens](https://msdn.microsoft.com/library/windows/hardware/ff539571).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdtf\dtf%5D:%20Creating%20WDTF%20Scenarios%20%20RELEASE:%20%289/13/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


