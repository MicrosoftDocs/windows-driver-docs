---
title: Troubleshooting Common Errors
description: This article covers common issues that hardware vendors and driver developers might encounter when debugging their I2C firmware or driver software.
ms.date: 01/11/2024
---

# Troubleshooting common errors

This article covers common issues that hardware vendors and driver developers might encounter when debugging their I2C firmware or driver software.

## HIDI2C driver doesn't load

A scenario where the I2C Controller driver loaded but the device doesn't appear in the Windows Device Manager typically occurs if there's an invalid [ACPI Source Language (ASL)](https://uefi.org/htmlspecs/ACPI_Spec_6_4_html/19_ASL_Reference/ACPI_Source_Language_Reference.html?highlight=acpi%20source%20language) code for the host or the device. To determine whether the problem was due to a failure to match the INF, refer to the setupapi.dev.log file. Another indicator that the problem is due to a mismatch is *Error Code 10* in Windows Device Manager.

To resolve the issue, ensure:

- The \_CID value must be **PNP0C50**.
- The I2C **controller** and **device characteristics** in the BIOS must be accurate.
- The **HID descriptor address** (for the device) in the BIOS must be accurate.
- The GPIO Interrupt must be correctly identified and marked as **Exclusive, Level, ActiveLow**.

Refer to Section 13 of the [HID I2C Protocol Spec](/previous-versions/windows/hardware/design/dn642101(v=vs.85)) for more detail.

## Invalid report descriptor

If the host failed to retrieve the correct report descriptor from the device, make sure that:

- The enumeration sequence must finish running before the report descriptor is retrieved.
- The byte offsets 4 and 6 in the HID descriptor must be valid. (Pay particular attention to the length.)

If the correct report descriptor was retrieved from the device is verified but there's still a related issue, make sure that:

- The wReportDescLength field is accurate.
- The HID Report is correctly formatted. (To verify the results, test an alternative bus such as USB.)

### FAQ

This section highlights questions frequently asked by hardware vendors and driver developers.

- Will the Windows 8 inbox HIDI2C driver work for HID devices connected over I2C?
  - Yes, it works provided the firmware is compliant with this HID I2C Protocol Specification

- What is the data structure communicated between devices (such as Keyboards) and OS drivers?
  - The data structure would be in the form of an input report defined by a report descriptor, according to HID standard. The device itself rather than HIDI2C defines the input report structure. You report the keyboard usages as you would with a USB keyboard, and then provide the descriptor and corresponding INPUT reports as per the HID I2C Specification

- If multiple reports are being buffered at the same time, what should the device do?
  - If multiple reports are being buffered, the device should keep the interrupt asserted until the last report is read (acknowledged). As long as there's more data to report after a given read operation, the device should keep the line asserted using a level-trigger GPIO setting.

- Is it accurate to say that we should get the same DevicePath for USB and I2C connectivity?
  - No, the device path *isn't* identical between USB and I2C. The differences are minor, but noteworthy. For more information, see the Hardware ID section in the Windows Driver Kit (WDK).

- What is the required I2C transfer limit in order for HIDI2C devices to use the Windows inbox HIDI2C driver?
  - All I2C controllers are required to support transfers up to 4 KB. The maximum HID report descriptor length is 4 KB.
