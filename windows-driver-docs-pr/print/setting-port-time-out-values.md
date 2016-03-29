---
title: Setting Port Time-Out Values
description: Setting Port Time-Out Values
ms.assetid: bf39670b-440d-46f9-9110-790d36eb3b49
keywords: ["port management WDK print , time-out values", "time-outs WDK print", "OpenPort", "SetPortTimeOuts"]
---

# Setting Port Time-Out Values


## <a href="" id="ddk-setting-port-time-out-values-gg"></a>


If you are writing a port monitor for a port that has modifiable time-out values, the time-out values should be initialized from within the monitor's [**OpenPort**](https://msdn.microsoft.com/library/windows/hardware/ff559593) function. For example the **OpenPort** function in Localmon.dll, the [sample port monitor](sample-port-monitor.md), calls the **SetCommTimeouts** function, described in the Microsoft Windows SDK documentation, for this purpose.

Additionally, a port monitor can optionally provide a [**SetPortTimeOuts**](https://msdn.microsoft.com/library/windows/hardware/ff562630) function, which can be called by language monitors. The function is called by Pjlmon.dll, the [sample language monitor](sample-language-monitor.md). The print spooler does not call **SetPortTimeOuts**.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Setting%20Port%20Time-Out%20Values%20%20RELEASE:%20%283/29/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




