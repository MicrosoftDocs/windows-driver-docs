---
title: Using Custom Hardware IDs and Compatible IDs
description: Using Custom Hardware IDs and Compatible IDs
ms.date: 04/20/2017
---

# Using Custom Hardware IDs and Compatible IDs


As described in [Device Identification Strings](device-identification-strings.md), the following is the generic format that a new bus driver should use for Plug and Play (PnP) hardware IDs and compatible IDs.

```cpp
enumerator\enumerator-specific-device-ID 
```

Where:

-   *Enumerator* identifies the *enumerator* (bus driver) that detects and reports child devices on a bus to the PnP manager.

-   *enumerator-specific-device-ID* is a device identifier specific to the bus driver.

If the configuration or operation of a bus differs significantly from other buses, the bus driver for the bus should use a unique enumerator name to ensure that the child devices of the bus are not unintentionally and inappropriately grouped with child devices that are enumerated by the bus drivers for these other buses. The bus driver should use the following format to report device identification strings to the PnP manager:

```cpp
bus-type-guid\vendor-specific-id
```

Where:

-   *bus-type-guid* is a unique GUID that identifies the bus and should be the same GUID that is used to identify the bus. As described in [Installing a Bus Driver](installing-a-new-bus-driver.md), the bus driver identifies the bus type for a device in response to an [**IRP_MN_QUERY_BUS_INFORMATION**](../kernel/irp-mn-query-bus-information.md) request for the device.

-   *vendor-specific-id* is vendor-defined format that typically identifies the vendor, the device, a subsystem, a revision number, and possibly other device information. For example, the format might take the form of *Vendor*&*Device*&*Subsystem*&*Revision,* where the ampersand character ("&") delimits the subfields and the format of each subfield is vendor-specific. For examples of actual device identification strings, see [Device Identification Strings](device-identification-strings.md).

The PnP manager sends [**IRP_MN_QUERY_ID**](../kernel/irp-mn-query-id.md) requests to a bus driver to obtain device identification strings for a device. The device identification strings include a device ID, a device instance ID, a list of hardware IDs, and a list of compatible IDs. The following fictitious examples include a device ID, a list of hardware IDs and a list of compatible IDs. In these examples, the enumerator is specified by the *bus-type-guid* subfield, which is the GUID "{xxxxxxxx-yyyy-zzzz-xxxx-yyyyyyyyyyyy}". The format of the *vendor-specific-id* field is *Vendor*&*Device*&*Subsystem*&*Revision*, where the *Vendor* subfield is "ven_1", the *Device* subfield is "dev_2", the *Subsystem* subfield is "subsys_3", and the *Revision* subfield is "rev_4".

A device ID is the hardware ID that is the most specific description of a device. In the following example, the device ID specifies the vendor, the device, the subsystem, and the revision.

```cpp
{xxxxxxxx-yyyy-zzzz-xxxx-yyyyyyyyyyyy}\ven_1&dev_2&subsys_3&rev_4 
```

A hardware ID list specifies IDs in order, from the most specific to the least specific. In the following list, a device identification string is reported as hardware ID if it specifies at least the vendor, the device, and the subsystem. The hardware ID that includes the most information is listed first.

```cpp
{xxxxxxxx-yyyy-zzzz-xxxx-yyyyyyyyyyyy}\ven_1&dev_2&subsys_3&rev_4 
{xxxxxxxx-yyyy-zzzz-xxxx-yyyyyyyyyyyy}\ven_1&dev_2&subsys_3 
```

In the following list, a device identification string is reported as compatible ID if it specifies at least the vendor and device (positions 1 and 2), but does not specify the subsystem (position 3). The compatible ID that includes the most information is listed first.

```cpp
{xxxxxxxx-yyyy-zzzz-xxxx-yyyyyyyyyyyy}\ven_1&dev_2&rev_4 
{xxxxxxxx-yyyy-zzzz-xxxx-yyyyyyyyyyyy}\ven_1&dev_2
```

If a driver installs using a hardware ID, it implies full functionality for matching devices. If a driver installs using a compatible ID, it implies at least basic functionality for matching devices.A driver might use a compatible ID so that a generic driver can work on a large number of devices. For example, many of the Windows system-supplied drivers match compatible IDs. A driver that matches a hardware ID typically targets a small set of devices but provides full functionality.
