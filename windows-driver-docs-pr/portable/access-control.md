---
Description: Access Control
title: Access Control
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Access Control


The Windows Driver Model (WDM) supports the restriction of device access via Access Control Lists (ACLs) on the Plug and Play (PnP) Device Nodes. This means that vendors and network administrators can restrict access to any device type. When an application opens a handle to a driver by calling the **IPortableDevice::Open** method, the driver's I/O Manager verifies whether the given user has the required access, and similarly does access checks when IOCTLs are sent to the driver from that handle.

For example, a network administrator could restrict Guest users to read-only access for portable devices, while they could grant Authenticated users read/write access. In this case, if a Guest issued a WPD command that required read/write Access (such as Delete Object); it would fail with Access Denied, whereas if an Authenticated user issued the same command, it would succeed.

The Group Policy entries for controlling access to removable storage and portable devices is actually nothing more than an easy way for Administrators to apply PnP device node ACLs to a whole class of devices at a time (for example, applying the "Deny Write Access to Portable Devices" Group Policy would adjust the ACLs of all WPD devices to deny write access).

## <span id="I_O_Control_Codes_in_WPD"></span><span id="i_o_control_codes_in_wpd"></span><span id="I_O_CONTROL_CODES_IN_WPD"></span>I/O Control Codes in WPD


WPD applications communicate with drivers by opening device handles and sending I/O Control Codes (IOCTLs). These IOCTLs consist of four sections:

1.  Device Type
2.  Function Code
3.  Buffer Method
4.  Access Type

The fourth section, the Access Type, specifies the specific access requirement for the given command. The driver's I/O manager uses this data to perform the Access Control List (ACL) check.

So if an IOCTL were defined as:

```ManagedCPlusPlus
    #define MY_READ_IOCTL CTL_CODE(FILE_DEVICE_X, CONTROL_FUNCTION_Y, METHOD_BUFFERED, FILE_READ_ACCESS)
```

The driver's I/O manager would check that the owner of the device handle has READ access to the device when this message is sent.

And, if an IOCTL were defined as:

```ManagedCPlusPlus
    #define MY_READWRITE_IOCTL CTL_CODE(FILE_DEVICE_X, CONTROL_FUNCTION_Z, METHOD_BUFFERED, (FILE_READ_ACCESS | FILE_WRITE_ACCESS))
```

The driver's I/O manager would check that the owner of the device handle has READ and WRITE access to the device when this message is sent.

## <span id="Payload_Verification"></span><span id="payload_verification"></span><span id="PAYLOAD_VERIFICATION"></span>Payload Verification


WPD is slightly different from many other driver stacks in that it is the payload of the WPD message that contains the WPD command, not the IOCTL (in most driver stacks, the IOCTL is the command). This is not unique, but it means that WPD has 2 IOCTLs:

-   A read-only IOCTL (IOCTL\_WPD\_MESSAGE\_READ\_ACCESS) for all WPD commands that require read-only access
-   A read-write IOCTL (IOCTL\_WPD\_MESSAGE\_READWRITE\_ACCESS) for all WPD commands that require read-write access

In WPD, it is possible for an application to by-pass the WPD API, and to open a handle to the driver directly. This, combined with the fact that the IOCTL payload contains the actual command, means that it is possible a malicious application could attempt to trick a driver by sending a WPD command that requires read-write access with the read-only IOCTL (for example, the IOCTL used would be IOCTL\_WPD\_MESSAGE\_READ\_ACCESS, but the payload may contain WPD\_COMMAND\_OBJECT\_MANAGEMENT\_DELETE\_OBJECTS).

Therefore, WPD drivers must verify that the WPD command payload was sent with the proper IOCTL to ensure that the I/O manager performed the appropriate ACL check (for example, in the previous example, the I/O manager would have checked that the caller had read-only access since the IOCTL was IOCTL\_WPD\_MESSAGE\_READ\_ACCESS. Even if the caller had read-only access, the driver should reject such a call because IOCTL\_WPD\_MESSAGE\_READWRITE\_ACCESS should have been used with a command like WPD\_COMMAND\_OBJECT\_MANAGEMENT\_DELETE\_OBJECTS).

Because every driver has to perform payload verification, WPD supplies easy to use MACROs to make this checking automatic for the driver. See the [Handling Access Control](handling-access-control.md) section of the WPD Drivers Programming Guide for details and sample code.

## <span id="related_topics"></span>Related topics


[**WPD Drivers Overview**](wpd-drivers-overview.md)

 

 





