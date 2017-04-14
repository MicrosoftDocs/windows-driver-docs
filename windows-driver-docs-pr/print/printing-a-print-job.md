---
title: Printing a Print Job
author: windows-driver-content
description: Printing a Print Job
ms.assetid: 2e881f99-9dbe-4e89-8628-feb05137c9b0
keywords: ["print monitors WDK , printing print jobs", "print jobs WDK , printing", "jobs WDK print , printing", "WritePort", "ReadPort", "GetPrinterDataFromPort", "bidirectional communication WDK print", "bidi communication WDK print", "printing print jobs WDK"]
---

# Printing a Print Job


## <a href="" id="ddk-printing-a-print-job-gg"></a>


After a port has been opened, as described in [Opening and Closing a Port](opening-and-closing-a-port.md), the spooler can send print jobs to the port.

Each print job is delimited by spooler calls to a language or port monitor's [**StartDocPort**](https://msdn.microsoft.com/library/windows/hardware/ff562710) and [**EndDocPort**](https://msdn.microsoft.com/library/windows/hardware/ff548742) functions. The spooler calls these functions when a print processor calls the spooler's **StartDocPrinter** and **EndDocPrinter** functions, which are described in the Microsoft Windows SDK documentation. Within the scope of a set of **StartDocPort** and **EndDocPort** functions, unlimited spooler calls to a monitor's [**WritePort**](https://msdn.microsoft.com/library/windows/hardware/ff563792), [**ReadPort**](https://msdn.microsoft.com/library/windows/hardware/ff561909), and [**GetPrinterDataFromPort**](https://msdn.microsoft.com/library/windows/hardware/ff550506) functions can occur.

Each of these functions requires the port handle returned by [**OpenPortEx**](https://msdn.microsoft.com/library/windows/hardware/ff559596) (or [**OpenPort**](https://msdn.microsoft.com/library/windows/hardware/ff559593)) to be specified as in input argument. Typically, a language monitor implements each of the functions by calling the like-named function in its associated port monitor.

When the spooler calls a language monitor's **WritePort** function to send a data stream to the port, the function generally adds language-specific information, such as [*PJL*](https://msdn.microsoft.com/library/windows/hardware/ff556325#wdkgloss-pjl) commands, to the received data stream before passing it to the associated port monitor's **WritePort** function.

The **ReadPort** function is used for obtaining status information from bidirectional printer hardware, which a language monitor might send to the spooler by calling **SetPort**, described in the Windows SDK documentation. The spooler does not call the **ReadPort** function.

If printing hardware is bidirectional, both its language monitor and its port monitor should support a **GetPrinterDataFromPort** function. A language monitor's **GetPrinterDataFromPort** function should accept a registry value name as input, obtain a value for that name (generally by calling associated port monitor's **WritePort** and **ReadPort** functions), and return the value to the caller. A port monitor's **GetPrinterDataFromPort** function should accept an I/O control code as input, call [**DeviceIoControl**](https://msdn.microsoft.com/library/windows/desktop/aa363216) (described in the Windows SDK documentation) to pass the control code to the port driver, and return the result.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Printing%20a%20Print%20Job%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


