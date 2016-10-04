---
title: Print Provider Capabilities
author: windows-driver-content
description: Print Provider Capabilities
MS-HAID:
- 'splarch\_b0f015b5-65f7-4109-9e5e-1a0e0d235a9f.xml'
- 'print.print\_provider\_capabilities'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 1b01aac5-673a-4593-a52e-6017d9683c42
keywords: ["print providers WDK , capabilities"]
---

# Print Provider Capabilities


## <a href="" id="ddk-print-provider-capabilities-gg"></a>


**Warning**  
Starting with Windows 10, the APIs which support third-party print providers are deprecated. Microsoft does not recommend any investment into third-party print providers. Additionally, on Windows 8 and newer products where the v4 print driver model is available, third-party print providers may not create or manage queues which use v4 print drivers.

 

By supporting predefined sets of API functions, Microsoft Windows 2000 and later print providers can supply the following capabilities:

-   Print Queue Management

    Adding, deleting, opening, closing, enumerating, and setting parameters for print queues. Also, providing notification of changes to a print queue's state.

-   Printer Driver Management

    Adding, deleting, enumerating, and specifying a directory for printer drivers.

-   Print Job Creation

    Starting and ending a document, starting and ending a document page, writing the job's data stream to a port, reading printer status information.

-   Print Job Scheduling

    Scheduling, enumerating, and setting parameters for a print job.

-   Forms Management

    Adding, deleting, enumerating, and setting parameters for print forms.

-   Print Processor Management

    Adding, deleting, enumerating, specifying a directory for and the data types supported by print processors.

-   Print Monitor Management

    Adding, deleting, and enumerating print monitors.

-   Port Management

    Adding, deleting, configuring, enumerating, and setting parameters for printer ports.

-   Registry Management

    Creating, deleting, and enumerating registry keys and values associated with a print provider.

-   Other Capabilities

    Displaying a message box, shutting down the print provider, reading a memory mapped spool file, providing a communication path between port monitor UI DLLs and port monitor server DLLs.

These capabilities are implemented as a set of [functions defined by print providers](functions-defined-by-print-providers.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Print%20Provider%20Capabilities%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


