---
title: Handling IRP_MN_REGINFO and IRP_MN_REGINFO_EX to Register Blocks
description: Handling IRP_MN_REGINFO and IRP_MN_REGINFO_EX to Register Blocks
keywords: ["WMI WDK kernel , registering with WMI", "registering WMI data providers", "data providers WDK WMI", "driver registrations WDK WMI", "event blocks WDK WMI", "blocks WDK WMI", "IRP_MN_REGINFO", "IRP_MN_REGINFO_EX", "registering blocks"]
ms.date: 06/16/2017
---

# Handling IRP\_MN\_REGINFO and IRP\_MN\_REGINFO\_EX to Register Blocks





On Windows 98 and Windows 2000, the system sends the [**IRP\_MN\_REGINFO**](./irp-mn-reginfo.md) request to a driver to allow a driver to register its WMI classes. On Windows XP and later, the system sends the [**IRP\_MN\_REGINFO\_EX**](./irp-mn-reginfo-ex.md) request instead. Most drivers can handle these requests by using [**WmiSystemControl**](/windows-hardware/drivers/ddi/wmilib/nf-wmilib-wmisystemcontrol) to provide a callback routine. See [Using the WMI Library to Register Blocks](using-the-wmi-library-to-register-blocks.md) for details.

A driver must handle **IRP\_MN\_REGINFO** or **IRP\_MN\_REGINFO\_EX** requests to register blocks that use dynamic instance names or that use a list of driver-defined static instance names; it cannot call **WmiSystemControl** to register such blocks. A driver can optionally handle this request to register blocks that use static instance names based on the PDO or a driver-defined base name string.

In this case, the driver:

1.  Fills in a [**WMIREGINFO**](/windows-hardware/drivers/ddi/wmistr/ns-wmistr-wmireginfow) structure at **Parameters.WMI.Buffer** that specifies:

    -   The number of bytes of all registration data supplied by the driver, including data supplied on behalf of another driver.

    -   The driver's registry path.

    -   The name of the driver's MOF resource.

    -   The number of blocks to register.

    -   An array of [**WMIREGGUID**](/windows-hardware/drivers/ddi/wmistr/ns-wmistr-wmiregguidw) structures, one for each block.

2.  For each block, the driver fills in a **WMIREGGUID** structure that specifies:

    -   The GUID that represents the block.

    -   Flags that provide information about instance names and other characteristics of the block, such as whether the block is expensive to collect. For more information, see [WMI Registration Flags](wmi-registration-flags.md).

    If the block is being registered with static instance names, the driver sets one of the following members to specify static instance name data for the block:

    -   If the driver sets **Flags** with WMIREG\_FLAG\_INSTANCE\_LIST, it sets **InstanceNameList** to an offset to a list of static instance name strings. WMI specifies instances in subsequent requests by index into this list.

    -   If the driver sets **Flags** with WMIREG\_FLAG\_INSTANCE\_BASENAME, it sets **BaseNameOffset** to an offset to a base name string. WMI uses this string to generate static instance names for the block.

    -   If the driver sets **Flags** with WMIREG\_FLAG\_INSTANCE\_PDO, it sets **Pdo** to the PDO passed to the driver's [*AddDevice*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_add_device) routine. WMI uses the device instance path of the PDO to generate static instance names for the block. When handling an **IRP\_MN\_REGINFO\_EX** request, drivers must call the [**ObReferenceObject**](/windows-hardware/drivers/ddi/wdm/nf-wdm-obfreferenceobject) routine on the physical device object passed in **Pdo**. (The system will automatically call [**ObDereferenceObject**](/windows-hardware/drivers/ddi/wdm/nf-wdm-obdereferenceobject) to dereference the object; the driver must not do so.)

    The driver writes instance name strings or a base name string at the offset indicated by **InstanceNameList** or **BaseName**, respectively.

3.  If the driver is registering blocks on behalf of another driver (as a class driver might on behalf of a miniclass driver), the driver fills in another [**WMIREGINFO**](/windows-hardware/drivers/ddi/wmistr/ns-wmistr-wmireginfow) structure and list of [**WMIREGGUID**](/windows-hardware/drivers/ddi/wmistr/ns-wmistr-wmiregguidw) structures with registration information for the other driver's blocks, and sets **NextWmiRegInfo** in the first **WMIREGINFO** to the offset in bytes from the beginning of the first **WMIREGINFO** to the beginning of the second **WMIREGINFO** structure.

 

