---
title: IRP_MN_QUERY_ID
description: Bus drivers must handle requests for BusQueryDeviceID for their child devices (child PDOs). Bus drivers can handle requests for BusQueryHardwareIDs, BusQueryCompatibleIDs, and BusQueryInstanceID for their child devices.
ms.date: 08/12/2017
ms.assetid: 3135cb30-a696-4201-8dfc-cdc1a29fe52b
keywords:
 - IRP_MN_QUERY_ID Kernel-Mode Driver Architecture
ms.localizationpriority: medium
---

# IRP\_MN\_QUERY\_ID


Bus drivers must handle requests for **BusQueryDeviceID** for their child devices (child PDOs). Bus drivers can handle requests for **BusQueryHardwareIDs**, **BusQueryCompatibleIDs**, and **BusQueryInstanceID** for their child devices.

Beginning with Windows 7, bus drivers must also handle requests for BusQueryContainerID for their child PDOs.

For more information about these identifiers (IDs), see [Device Identification Strings](https://msdn.microsoft.com/library/windows/hardware/ff541224).

**Note**  Function drivers and filter drivers do not handle this IRP.

 

Major Code
----------

[**IRP\_MJ\_PNP**](irp-mj-pnp.md)
When Sent
---------

The PnP manager sends this IRP when a device is enumerated. A driver might send this IRP to retrieve the instance ID for one of its devices.

The PnP manager and drivers send this IRP at IRQL PASSIVE\_LEVEL in an arbitrary thread context.

## Input Parameters


The **Parameters.QueryId.IdType** member of the [**IO\_STACK\_LOCATION**](https://msdn.microsoft.com/library/windows/hardware/ff550659) structure specifies the kind of ID(s) requested. Possible values include BusQueryDeviceID, BusQueryHardwareIDs, BusQueryCompatibleIDs, BusQueryInstanceID, and BusQueryContainerID. The following ID type is reserved: BusQueryDeviceSerialNumber.

## Output Parameters


Returned in the I/O status block.

## I/O Status Block


A driver sets **Irp-&gt;IoStatus.Status** to STATUS\_SUCCESS or to an appropriate error status.

On success, a driver sets **Irp-&gt;IoStatus.Information** to a WCHAR pointer that points to the requested information. On error, a driver sets **Irp-&gt;IoStatus.Information** to zero.

Operation
---------

If a driver returns ID(s) in response to this IRP, it allocates a WCHAR structure from paged pool to contain the ID(s). The PnP manager frees the structure when it is no longer needed.

A driver returns one of the following:

-   A REG\_SZ string in response to a BusQueryDeviceID, BusQueryInstanceID, or, BusQueryContainerID request.

-   A REG\_MULTI\_SZ string in response to a BusQueryHardwareIDs or BusQueryCompatibleIDs request.

If a driver returns an ID with an illegal character, the system will bug check. Characters with the following values are illegal in an ID for this IRP:

-   Less than or equal to 0x20 (' ')

-   Greater than 0x7F

-   Equal to 0x2C (',')

A driver must conform to the following length restrictions for IDs:

-   Each hardware ID or compatible ID that a driver returns in this IRP must be less than MAX\_DEVICE\_ID\_LEN characters long. This constant currently has a value of 200 as defined in sdk\\inc\\cfgmgr32.h.

-   The container ID that a driver returns in this IRP must be formatted as a globally unique identifier (GUID), and must be MAX\_GUID\_STRING\_LEN characters, which includes the null terminator.

-   If a bus driver supplies globally unique instance IDs for its child devices (that is, the driver sets [**DEVICE\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff543095)**.UniqueID** for the devices), then the combination of device ID plus instance ID must be less than (MAX\_DEVICE\_ID\_LEN - 1) characters. The operating system requires the additional character for a path separator.

-   If a bus driver does not supply globally unique instance IDs for its child devices, then the combination of device ID plus instance ID must be less than (MAX\_DEVICE\_ID\_LEN - 28). The value of this equation is currently 172.

Bus drivers should be prepared to handle this IRP for a child device immediately after the device is enumerated.

**Specifying BusQueryDeviceID and BusQueryInstanceID**

The values a bus driver supplies for BusQueryDeviceID and BusQueryInstanceID allow the operating system to differentiate a device from other devices on the computer. The operating system uses the device ID and instance ID that are returned in the **IRP\_MN\_QUERY\_ID** IRP and the unique ID field that are returned in the [**IRP\_MN\_QUERY\_CAPABILITIES**](irp-mn-query-capabilities.md) IRP to locate registry information for the device.

For **BusQueryDeviceID**, a bus driver supplies the device's [*device ID*](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-device-id). A device ID should contain the most-specific description of the device possible, incorporating the name of the enumerator and strings identifying the manufacturer, device, revision, packager, and packaged product, where possible. For example, the PCI bus driver responds with device IDs of the form PCI\\VEN\_xxxx&DEV\_xxxx&SUBSYS\_xxxxxxxx&REV\_xx, encoding all five of the items mentioned above. However, a device ID should not contain enough information to differentiate between two identical devices. This information should be encoded in the instance ID.

For BusQueryInstanceID, a bus driver should supply a string that contains the [*instance ID*](https://msdn.microsoft.com/library/windows/hardware/ff556290#wdkgloss-instance-id) for the device. Setup and bus drivers use the instance ID, with other information, to differentiate between two identical devices on the computer. The instance ID is either unique across the whole computer or just unique on the device's parent bus.

If an instance ID is only unique on the bus, the bus driver specifies that string for BusQueryInstanceID but also specifies a **UniqueID** value of **FALSE** in response to an [**IRP\_MN\_QUERY\_CAPABILITIES**](irp-mn-query-capabilities.md) request for the device. If **UniqueID** is **FALSE**, the PnP manager enhances the instance ID by adding information about the device's parent and thus makes the ID unique on the computer. In this case the bus driver should not take extra steps to make its devices' instance IDs globally unique; just return the appropriate capabilities information and the operating system takes care of it.

If a bus driver can supply a globally unique ID for each child device, such as a serial number, the bus driver specifies those strings for BusQueryInstanceID and specifies a **UniqueID** value of **TRUE** in response to an [**IRP\_MN\_QUERY\_CAPABILITIES**](irp-mn-query-capabilities.md) request for each device.

**Specifying BusQueryHardwareIDs and BusQueryCompatibleIDs**

The values a bus driver supplies for BusQueryHardwareIDs and BusQueryCompatibleIDs allow Setup to locate the appropriate drivers for the bus's child device.

A bus driver responds to each of these requests with a REG\_MULTI\_SZ list of IDs that describe the device. The maximum length, in characters, of a list of IDs, including the two NULL characters that terminate the list, is REGSTR\_VAL\_MAX\_HCID\_LEN.

When returning more than one [*hardware ID*](https://msdn.microsoft.com/library/windows/hardware/ff556288#wdkgloss-hardware-id) and/or more than one [*compatible ID*](https://msdn.microsoft.com/library/windows/hardware/ff556274#wdkgloss-compatible-id), a bus driver should list the IDs in the order of most-specific to most-general to facilitate choosing the best driver match for the device. The first entry in the hardware IDs list is the most-specific description of the device and, as such, it is usually identical to the device ID.

Setup checks the IDs against the IDs listed in INF files for possible matches. Setup first scans the hardware IDs list, then the compatible IDs list. Earlier entries are treated as more specific descriptions of the device, and later entries as more general (and thus less optimal) matches for the device. If no match is found in the list of hardware IDs, Setup might prompt the user for installation media before moving on to the list of compatible IDs.

See [Plug and Play](https://msdn.microsoft.com/library/windows/hardware/ff547125) for the general rules for handling [Plug and Play minor IRPs](plug-and-play-minor-irps.md).

**Specifying BusQueryContainerIDs**

Beginning with Windows 7, a bus driver should supply a string for BusQueryContainerID that contains the [container ID](https://msdn.microsoft.com/library/windows/hardware/ff540024) for the device. The container ID allows the operating system to group all functional devices from a single removable physical device. For example, all functional devices from a removable multifunction device have the same container ID. For more information about reporting container IDs in special cases, such as a volume device that may span multiple disks in multiple containers but does not belong to any container, see [Overview of Container IDs](https://msdn.microsoft.com/library/windows/hardware/ff549447).

A removable physical device is defined as a child device that the bus driver specifies a **Removable** capability of **TRUE** in response to an [**IRP\_MN\_QUERY\_CAPABILITIES**](irp-mn-query-capabilities.md) request. For more information about the **Removable** value, see [**DEVICE\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff543095).

The bus driver creates a container ID based on a bus-specific unique ID that the device provides. For more information, see [How Container IDs are Generated](https://msdn.microsoft.com/library/windows/hardware/ff546193).

The driver must fail the IRP request and set **IoStatus.Status** to STATUS\_NOT\_SUPPORTED if any of the following are true:

-   The device does not support a bus-specific unique ID that the bus driver can use to generate a container ID.

-   The bus driver had previously specified a **Removable** capability of **FALSE** in response to an [**IRP\_MN\_QUERY\_CAPABILITIES**](irp-mn-query-capabilities.md) request for the device.

**Sending This IRP**

Typically, only the PnP manager sends this IRP.

To get the hardware IDs or compatible IDs for a device, call [**IoGetDeviceProperty**](https://msdn.microsoft.com/library/windows/hardware/ff549203) instead of sending this IRP.

A driver might send this IRP to retrieve the instance ID for one of its devices. For example, consider a multifunction PnP ISA device whose functions do not operate independently. The PnP manager enumerates the functions as separate devices, but the driver for such a device might be required to associate one or more of the functions. Because PnP ISA guarantees a unique instance ID, the driver for such a multifunction device can use the instance IDs to locate functions that reside on the same device. The driver for such a device must also get the device's enumerator name by calling [**IoGetDeviceProperty**](https://msdn.microsoft.com/library/windows/hardware/ff549203), to confirm that the device is a PnP ISA device.

See [Handling IRPs](https://msdn.microsoft.com/library/windows/hardware/ff546847) for information about sending IRPs. The following steps apply specifically to this IRP:

-   Set the values in the next I/O stack location of the IRP: set **MajorFunction** to [**IRP\_MJ\_PNP**](irp-mj-pnp.md), set **MinorFunction** to IRP\_MN\_QUERY\_ID, and set **Parameters.QueryId.IdType** to **BusQueryInstanceID**.

-   Set **IoStatus.Status** to STATUS\_NOT\_SUPPORTED.

In addition to sending the query ID IRP, the driver must call [**IoGetDeviceProperty**](https://msdn.microsoft.com/library/windows/hardware/ff549203) to get the **DevicePropertyEnumeratorName** for the device.

After the IRP completes and the driver is finished with the ID, the driver must free the ID structure returned by the driver(s) that handled the query IRP.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Header</p></td>
<td>Wdm.h (include Wdm.h, Ntddk.h, or Ntifs.h)</td>
</tr>
</tbody>
</table>

## See also


[Device Identification Strings](https://msdn.microsoft.com/library/windows/hardware/ff541224)

[**IoGetDeviceProperty**](https://msdn.microsoft.com/library/windows/hardware/ff549203)

 

 




