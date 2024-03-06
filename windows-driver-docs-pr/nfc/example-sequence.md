---
title: Example Sequence
keywords: ["Examples of sequences of IOCTLs in the Smart Card resource manager including start-up connection and disconnection", "NFC","near field communications","proximity","near field proximity","NFP"]
description: Provides examples of sequences of IOCTLs in the Smart Card resource manager, including start-up, connection, and disconnection.
ms.date: 01/11/2024
---

# Example sequence

The following is an example sequence of IOCTLs in the Smart Card resource manager:

## Start-up sequence

1. Use the DevObj or CfgMgr API with the Smart Card access device interface GUID to discover the NFC device driver's name, and use it with CreateFile to open a device handle.

2. Initialize thread pool.

3. Determine reader name.

    - IOCTL_SMARTCARD_GET_ATTRIBUTE on SCARD_ATTR_VENDOR_NAME, SCARD_ATTR_VENDOR_IFD_TYPE, and SCARD_ATTR_DEVICE_UNIT

4. Determine reader characteristics.
    - IOCTL_SMARTCARD_GET_ATTRIBUTE on SCARD_ATTR_CHARACTERISTICS

5. Start the card state monitor.
    - IOCTL_SMARTCARD_IS_PRESENT – To wait for a smart card arrival.

    - IOCTL_SMARTCARD_IS_ABSENT – To wait for the smart card departure.

The Power reset is irrelevant since we do not support SCARD_SWALLOWED, SCARD_POWERED state.

## Connect sequence

1. Start of loop.

2. IOCTL_SMARTCARD_GET_STATE

    - Case SCARD_UNKNOWN and SCARD_ABSENT, do nothing

    - Case SCARD_PRESENT, swallow card

    - Case SCARD_SWALLOWED, cold reset

    - Case SCARD_POWERED, warm reset

    - Case SCARD_NEGOTIABLE, determine the card ATR

    - Case SCARD_SPECIFIC, determine the card ATR and protocol

3. IOCTL_SMARTCARD_SET_PROTOCOL

## Disconnect sequence

1. Power-down timeout starts.

2. Start of loop.

3. IOCTL_SMARTCARD_GET_STATE

    - Case SCARD_SPECIFIC, SCARD_NEGOTIABLE, SCARD_POWERED, set power down

    - Case SCARD_SWALLOWED, SCARD_PRESENT, do nothing

    - Case SCARD_ABSENT, SCARD_UNKNOWN, do nothing

## Related topics

- [NFC device driver interface (DDI) overview](/windows-hardware/drivers/ddi/index)
- [Smart card DDI and command reference](/previous-versions/dn905601(v=vs.85))
