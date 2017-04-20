---
title: Opening and Closing a Port
author: windows-driver-content
description: Opening and Closing a Port
ms.assetid: 8bfdb3af-51d4-4252-ae1c-7910f973f5f6
keywords:
- print monitors WDK , port management
- port management WDK print , opening ports
- opening print ports
- port management WDK print , closing ports
- closing print ports
- OpenPort
- OpenPortEx
- ClosePort
- spooler opening and closing ports WDK print
- print spooler opening and closing ports WDK
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Opening and Closing a Port


## <a href="" id="ddk-opening-and-closing-a-port-gg"></a>


After a port has been added, as described in [Adding a Port](adding-a-port.md), the spooler can open it by calling the appropriate language monitor's [**OpenPortEx**](https://msdn.microsoft.com/library/windows/hardware/ff559596) function.

The language monitor uses the **OpenPortEx** function to create and return a port handle. Typically, a language monitor calls its associated port monitor's [**OpenPort**](https://msdn.microsoft.com/library/windows/hardware/ff559593) function, and the language monitor just returns the handle obtained from the port monitor's **OpenPort**.

If a language monitor is not associated with a port, the spooler calls the port monitor's **OpenPort** function directly.

The spooler does not allow more than one path to a port to be enabled at one time. Thus, after it has called **OpenPortEx** (or **OpenPort**) in a particular monitor, it does not attempt to open the same port again before closing it.

After a port has been opened, the spooler can call additional functions to print a job, as described in [Printing a Print Job](printing-a-print-job.md), using the port handle as an input argument. A monitor should be written so that, after a port has been opened, the spooler can send multiple print jobs before closing the port.

The spooler closes a port if a job must be sent through a different language monitor, if no print queues are associated with a port, or when the system shuts down. To close a port, the spooler calls a language monitor's [**ClosePort**](https://msdn.microsoft.com/library/windows/hardware/ff545975) function. The function invalidates the handle that was created when the port was opened. A language monitor typically calls the **ClosePort** function defined by its associated port monitor.

If a language monitor is not associated with a port, the spooler calls the port monitor's **ClosePort** function directly.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Opening%20and%20Closing%20a%20Port%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


