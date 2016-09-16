---
title: Storing Port Configuration Information
author: windows-driver-content
description: Storing Port Configuration Information
MS-HAID:
- 'provider\_fbdcbe5c-e458-414f-8741-8ed5bc6f2815.xml'
- 'print.storing\_port\_configuration\_information'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: b1c83729-d7d2-4920-9402-4e00baa12633
keywords: ["port management WDK print , storing configuration information", "registry WDK print", "print spooler registry information WDK print monitor", "storing print port configuration information", "spooler registry information WDK print monitor"]
---

# Storing Port Configuration Information


## <a href="" id="ddk-storing-port-configuration-information-gg"></a>


The Windows 2000 and later print spooler can operate in either a clustered or nonclustered server environment. When the spooler is operating in a server cluster, print monitor configuration information must be stored in the cluster registry. On the other hand, if the spooler is operating on a single, nonclustered server system, print monitor configuration information must be stored in the server's local registry.

The print spooler defines a set of registry functions for use by print monitors. These functions direct configuration data to the appropriate registry, so the print monitor does not have to determine if the server is clustered. Print monitors must not use the Win32 registry API or the cluster registry API directly; all configuration data must be stored and accessed using the spooler's registry functions. Addresses of these functions are supplied to the print monitor in a [**MONITORREG**](https://msdn.microsoft.com/library/windows/hardware/ff557537) structure when the spooler calls the monitor's [**InitializePrintMonitor2**](https://msdn.microsoft.com/library/windows/hardware/ff551605) function.

In a server cluster, multiple instances of the spooler can coexist. Specifically, each cluster node possesses its own instance, and an additional instance exists for the cluster itself. One of the input parameters of the spooler registry functions is a spooler handle. This handle is received by the monitor's **InitializePrintMonitor2** function and identifies the spooler instance (node or cluster) that has opened the monitor. Using the spooler handle, the spooler registry functions maintain subkeys for each spooler instance.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Storing%20Port%20Configuration%20Information%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


