---
title: Supporting Standard WMI Blocks
author: windows-driver-content
description: Supporting Standard WMI Blocks
MS-HAID:
- 'WMI\_ac4b1202-b5bd-4b7c-8808-67dcb7b6beee.xml'
- 'kernel.supporting\_standard\_wmi\_blocks'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: ddec3afb-8274-4eff-93ef-b0a07fd7c13a
keywords: ["WMI WDK kernel , event blocks", "event blocks WDK WMI", "data blocks WDK WMI", "WMI WDK kernel , data blocks", "blocks WDK WMI", "standard blocks WDK WMI"]
---

# Supporting Standard WMI Blocks


## <a href="" id="ddk-supporting-standard-wmi-blocks-kg"></a>


Each driver should support any *standard blocks* defined for drivers of its type. Standard blocks provide WMI clients with consistent data for all devices of a given type, regardless of vendor.

To support a standard block, a driver:

-   Registers the block with WMI, along with the other standard and custom blocks supported by the driver, as described in [Registering as a WMI Data Provider](registering-as-a-wmi-data-provider.md).

-   Handles all WMI requests that specify the driver's device object pointer at **Parameters.WMI.ProviderId** and the GUID of the standard block at **Parameters.WMI.DataPath**, as described in [Handling WMI Requests](handling-wmi-requests.md).

MOF classes for standard blocks are published in system-supplied MOF files. A driver must not redefine a standard block in its own MOF file, because doing so would duplicate the block in the WMI database.

Currently, class definitions of standard blocks are published in the file wmicore.mof, which is included in the Windows Driver Kit (WDK).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Supporting%20Standard%20WMI%20Blocks%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


