---
title: Opening and Closing a Port
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
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Opening and Closing a Port





After a port has been added, as described in [Adding a Port](adding-a-port.md), the spooler can open it by calling the appropriate language monitor's [**OpenPortEx**](https://msdn.microsoft.com/library/windows/hardware/ff559596) function.

The language monitor uses the **OpenPortEx** function to create and return a port handle. Typically, a language monitor calls its associated port monitor's [**OpenPort**](https://msdn.microsoft.com/library/windows/hardware/ff559593) function, and the language monitor just returns the handle obtained from the port monitor's **OpenPort**.

If a language monitor is not associated with a port, the spooler calls the port monitor's **OpenPort** function directly.

The spooler does not allow more than one path to a port to be enabled at one time. Thus, after it has called **OpenPortEx** (or **OpenPort**) in a particular monitor, it does not attempt to open the same port again before closing it.

After a port has been opened, the spooler can call additional functions to print a job, as described in [Printing a Print Job](printing-a-print-job.md), using the port handle as an input argument. A monitor should be written so that, after a port has been opened, the spooler can send multiple print jobs before closing the port.

The spooler closes a port if a job must be sent through a different language monitor, if no print queues are associated with a port, or when the system shuts down. To close a port, the spooler calls a language monitor's [**ClosePort**](https://msdn.microsoft.com/library/windows/hardware/ff545975) function. The function invalidates the handle that was created when the port was opened. A language monitor typically calls the **ClosePort** function defined by its associated port monitor.

If a language monitor is not associated with a port, the spooler calls the port monitor's **ClosePort** function directly.

 

 




