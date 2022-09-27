---
title: USB Device-Specific Method (_DSM)
description: To support device-class-specific configuration of the USB subsystem, Windows defines a Device-Specific Method (_DSM) that has the functions that are described in this article.
ms.date: 07/14/2022
---

# USB Device-Specific Method (_DSM)

To support device-class-specific configuration of the USB subsystem, Windows defines a Device-Specific Method (_DSM) that has the functions that are described in this article.

## Function 1: Post-reset processing for dual-role controllers

The _DSM control method parameters for the post-reset processing function for dual-role USB controllers are as follows:

### Arguments (Function 1)

- **Arg0:** UUID = ce2ee385-00e6-48cb-9f05-2edb927c4899
- **Arg1:** Revision ID = 0
- **Arg2:** Function index = 1
- **Arg3:** Empty package (not used)

### Return (Function 1)

None

The Windows inbox drivers only support USB controllers in host mode. After each controller reset, the USB driver will invoke the _DSM function index 1 to perform any controller-specific initialization required to configure the USB controller to operate in host mode.

When this function is used, the _DSM method must appear under the USB controller device.

## Function 2: Port type identification

The _DSM control method parameters for identifying the USB port type are as follows:

### Arguments (Function 2)

- **Arg0:** UUID = ce2ee385-00e6-48cb-9f05-2edb927c4899
- **Arg1:** Revision ID = 0
- **Arg2:** Function index = 2
- **Arg3:** Empty package (not used)

### Return (Function 2)

An integer containing one of the following values:

<table>
  <thead>
    <th>Element</th>
    <th>Object type</th>
    <th>Description</th>
  </thead>
  <tbody>
    <tr>
      <td>Port type</td>
      <td>Integer (BYTE)</td>
      <td><p>Specifies the type of the USB port:</p>
        <ul>
          <li>0x00 – Regular USB</li>
          <li>0x01 – HSIC</li>
          <li>0x02 – SSIC</li>
          <li>0x03 – 0xff reserved</li>
        </ul>
      </td>
    </tr>
  </tbody>
</table>

When this function is used, the _DSM method must appear under the USB port device.

## Function 5: Disable U1 and U2 transitions for a port

When this _DSM method returns 0x01 the USB bus driver disables U1 and U2 transitions for the port. If it returns 0x00 the USB bus driver falls back to its default heuristics for U1 and U2 transitions described in [U1 and U2 transitions](../usbcon/u1-and-u2-transitions.md).

The _DSM method must appear under a USB3 port. It is available starting with Windows 10, version 2004 (Vibranium).

The _DSM control method parameters are as follows:

### Arguments (Function 5)

- **Arg0:** UUID = ce2ee385-00e6-48cb-9f05-2edb927c4899
- **Arg1:** Revision ID = 0
- **Arg2:** Function index = 5
- **Arg3:** Empty package (not used)

### Return (Function 5)

An integer containing one of the following values:

<table>
  <thead>
    <th>Element</th>
    <th>Object type</th>
    <th>Description</th>
  </thead>
  <tbody>
    <tr>
      <td>Disable U1 and U2?</td>
      <td>Integer (BYTE)</td>
      <td><p>Specifies the U1 and U2 behavior:</p>
        <ul>
          <li>0x00 – The USB bus driver will fall back to its default heuristics for U1 and U2.</li>
          <li>0x01 – U1 and U2 transitions will be disabled.</li>
          <li>0x02 – 0xff reserved</li>
        </ul>
      </td>
    </tr>
  </tbody>
</table>

## Function 6: Query controller register access type

This function is available starting in Windows Server 2022 and Windows 11.

The _DSM control method parameters for querying the register access type for communicating with USB controllers are as follows:

### Arguments (Function 6)

- **Arg0:** UUID = ce2ee385-00e6-48cb-9f05-2edb927c4899
- **Arg1:** Revision ID = 0
- **Arg2:** Function index = 6
- **Arg3:** Empty package (not used)

### Return (Function 6)

An Integer containing one of the following values:

<table>
  <thead>
    <th>Element</th>
    <th>Object type</th>
    <th>Description</th>
  </thead>
  <tbody>
    <tr>
      <td>RegisterAccessType</td>
      <td>4-byte (32-bit) unsigned long</td>
      <td><p>Specifies the type of the USB controller register access:</p>
        <ul>
          <li>0x00 – Undefined register access</li>
          <li>0x01 – Must use 32bit register access</li>
          <li>0x02 – 0xffffffff reserved</li>
        </ul>
      </td>
    </tr>
  </tbody>
</table>

When this function is used, the _DSM method must appear under the USB controller device.

> [!NOTE]
> Function index 0 of every _DSM is a query function that returns the set of supported function indexes, and is always required. For more information, see section 9.14.1, "_DSM (Device Specific Method)", in the [ACPI 5.0 specification](https://uefi.org/specifications).