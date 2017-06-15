---
title: Handling IRP\_MN\_REGINFO and IRP\_MN\_REGINFO\_EX to Register Blocks
author: windows-driver-content
description: Handling IRP\_MN\_REGINFO and IRP\_MN\_REGINFO\_EX to Register Blocks
MS-HAID:
- 'WMI\_de2ad851-3cd3-453c-be04-6ac236a6e077.xml'
- 'kernel.handling\_irp\_mn\_reginfo\_and\_irp\_mn\_reginfo\_ex\_to\_register\_blocks'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 2c17fc63-3c33-4d03-8c46-8d56242556d1
keywords: ["WMI WDK kernel , registering with WMI", "registering WMI data providers", "data providers WDK WMI", "driver registrations WDK WMI", "event blocks WDK WMI", "blocks WDK WMI", "IRP_MN_REGINFO", "IRP_MN_REGINFO_EX", "registering blocks"]
---

# Handling IRP\_MN\_REGINFO and IRP\_MN\_REGINFO\_EX to Register Blocks


## <a href="" id="ddk-handling-irp-mn-reginfo-and-irp-mn-reginfo-ex-to-register-blocks-k"></a>


On Windows 98 and Windows 2000, the system sends the [**IRP\_MN\_REGINFO**](https://msdn.microsoft.com/library/windows/hardware/ff551731) request to a driver to allow a driver to register its WMI classes. On Windows XP and later, the system sends the [**IRP\_MN\_REGINFO\_EX**](https://msdn.microsoft.com/library/windows/hardware/ff551734) request instead. Most drivers can handle these requests by using [**WmiSystemControl**](https://msdn.microsoft.com/library/windows/hardware/ff565834) to provide a callback routine. See [Using the WMI Library to Register Blocks](using-the-wmi-library-to-register-blocks.md) for details.

A driver must handle **IRP\_MN\_REGINFO** or **IRP\_MN\_REGINFO\_EX** requests to register blocks that use dynamic instance names or that use a list of driver-defined static instance names; it cannot call **WmiSystemControl** to register such blocks. A driver can optionally handle this request to register blocks that use static instance names based on the PDO or a driver-defined base name string.

In this case, the driver:

1.  Fills in a [**WMIREGINFO**](https://msdn.microsoft.com/library/windows/hardware/ff565832) structure at **Parameters.WMI.Buffer** that specifies:

    -   The number of bytes of all registration data supplied by the driver, including data supplied on behalf of another driver.

    -   The driver's registry path.

    -   The name of the driver's MOF resource.

    -   The number of blocks to register.

    -   An array of [**WMIREGGUID**](https://msdn.microsoft.com/library/windows/hardware/ff565827) structures, one for each block.

2.  For each block, the driver fills in a **WMIREGGUID** structure that specifies:

    -   The GUID that represents the block.

    -   Flags that provide information about instance names and other characteristics of the block, such as whether the block is expensive to collect. For more information, see [WMI Registration Flags](wmi-registration-flags.md).

    If the block is being registered with static instance names, the driver sets one of the following members to specify static instance name data for the block:

    -   If the driver sets **Flags** with WMIREG\_FLAG\_INSTANCE\_LIST, it sets **InstanceNameList** to an offset to a list of static instance name strings. WMI specifies instances in subsequent requests by index into this list.

    -   If the driver sets **Flags** with WMIREG\_FLAG\_INSTANCE\_BASENAME, it sets **BaseNameOffset** to an offset to a base name string. WMI uses this string to generate static instance names for the block.

    -   If the driver sets **Flags** with WMIREG\_FLAG\_INSTANCE\_PDO, it sets **Pdo** to the PDO passed to the driver's [*AddDevice*](https://msdn.microsoft.com/library/windows/hardware/ff540521) routine. WMI uses the device instance path of the PDO to generate static instance names for the block. When handling an **IRP\_MN\_REGINFO\_EX** request, drivers must call the [**ObReferenceObject**](https://msdn.microsoft.com/library/windows/hardware/ff558678) routine on the physical device object passed in **Pdo**. (The system will automatically call [**ObDereferenceObject**](https://msdn.microsoft.com/library/windows/hardware/ff557724) to dereference the object; the driver must not do so.)

    The driver writes instance name strings or a base name string at the offset indicated by **InstanceNameList** or **BaseName**, respectively.

3.  If the driver is registering blocks on behalf of another driver (as a class driver might on behalf of a miniclass driver), the driver fills in another [**WMIREGINFO**](https://msdn.microsoft.com/library/windows/hardware/ff565832) structure and list of [**WMIREGGUID**](https://msdn.microsoft.com/library/windows/hardware/ff565827) structures with registration information for the other driver's blocks, and sets **NextWmiRegInfo** in the first **WMIREGINFO** to the offset in bytes from the beginning of the first **WMIREGINFO** to the beginning of the second **WMIREGINFO** structure.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Handling%20IRP_MN_REGINFO%20and%20IRP_MN_REGINFO_EX%20to%20Register%20Blocks%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


