---
title: Language and Port Monitor Interaction
description: Language and Port Monitor Interaction
ms.assetid: 6c3c55fc-40f3-43d7-b8a2-20fed8d28813
keywords: ["print monitors WDK , language monitors", "print monitors WDK , port monitors", "language monitors WDK print , port monitor interaction", "port monitors WDK print , language monitor interaction"]
---

# Language and Port Monitor Interaction


## <a href="" id="ddk-language-and-port-monitor-interaction-gg"></a>


The following illustration demonstrates the path taken by printer data from the print processor to a printer that a) has a language monitor associated with it; and b) does not have a language monitor associated with it.

![figures comparing a printer data path with a language monitor and without a language monitor](images/mon1.png)

If a language monitor is associated with a printer during the printer's installation, the language monitor receives the printer's data stream from the spooler's print processor. The language monitor modifies the data stream and passes it to the printer's port monitor.

Most of the [functions defined by print monitors](functions-defined-by-print-monitors.md) are the same for [language monitors](language-monitors.md) and [port monitors](port-monitors.md). Typically, if a language monitor is in the data stream path, the spooler calls the language monitor's implementation of a function and the language monitor calls the port monitor's implementation of the same function. For example, the [**WritePort**](https://msdn.microsoft.com/library/windows/hardware/ff563792) function in the PJL language monitor (Pjlmon.dll) adds [*PJL*](https://msdn.microsoft.com/library/windows/hardware/ff556325#wdkgloss-pjl) commands to the data stream and then calls the port monitor's **WritePort** to send the stream to the port driver.

If a language monitor is not installed, the spooler calls the port monitor's implementation of the function.

Because language monitors and port monitors are discrete components of the printing architecture, customized and Microsoft-supplied monitors can be used together. Thus, you can provide a customized language monitor that works in conjunction with a Microsoft-supplied port monitor, and vice versa.

You can also provide a single print monitor consisting of a [combined language and port monitor](combined-language-and-port-monitor.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Language%20and%20Port%20Monitor%20Interaction%20%20RELEASE:%20%283/29/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




