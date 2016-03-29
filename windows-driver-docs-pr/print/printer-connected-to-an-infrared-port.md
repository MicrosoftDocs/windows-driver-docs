---
title: Printer Connected to an Infrared Port
description: Printer Connected to an Infrared Port
ms.assetid: 8545cf66-9b5c-41e8-82e0-e0edd75ad41b
keywords: ["infrared ports WDK printer", "IR ports WDK printer"]
---

# Printer Connected to an Infrared Port


## <a href="" id="ddk-printer-connected-to-an-infrared-port-gg"></a>


Printers connected over an infrared (IR) port do not support Plug and Play using the 1284 device string. For a computer with an IR port, a service constantly polls for devices. When an IR Plug and Play printer is brought within range, a PDO is created under Enum\\Root\\ with a [*device ID*](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-device-id) of the form HWP*nnnn*. The [*hardware ID*](https://msdn.microsoft.com/library/windows/hardware/ff556288#wdkgloss-hardware-id) of the [*devnode*](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-devnode) has a single entry of the form HWP*nnnn*.

The [**INF Manufacturer section**](https://msdn.microsoft.com/library/windows/hardware/ff547454) entries for a printer that supports Plug and Play over LPT and IR ports should appear similar to the following:

```
 
"Model Name XYZ" = Install_Section_XYZ, LPTENUM\Company_NameModelNam1234, Company_NameModelNam1234, Model_Name_XYZ
"Model Name XYZ" = Install_Section_XYZ, HWP9876, Model_Name_XYZ
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Printer%20Connected%20to%20an%20Infrared%20Port%20%20RELEASE:%20%283/29/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




