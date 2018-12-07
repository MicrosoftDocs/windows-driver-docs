---
title: Example sequence
ms.assetid: 2B15570A-A220-4BF7-B595-D9CF66E02673
keywords: ["Examples of sequences of IOCTLs in the Smart Card resource manager including start-up connection and disconnection", "NFC","near field communications","proximity","near field proximity","NFP"]
description: Provides examples of sequences of IOCTLs in the Smart Card resource manager, including start-up, connection, and disconnection.
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Example sequence


The following is an example sequence of IOCTLs in the Smart Card resource manager:

## Start-up sequence


1.  Use the DevObj or CfgMgr API with the Smart Card access device interface GUID to discover the NFC device driver’s name, and use it with CreateFile to open a device handle.

2.  Initialize thread pool.

3.  Determine reader name.

    -   IOCTL\_SMARTCARD\_GET\_ATTRIBUTE on SCARD\_ATTR\_VENDOR\_NAME, SCARD\_ATTR\_VENDOR\_IFD\_TYPE, and SCARD\_ATTR\_DEVICE\_UNIT

4.  Determine reader characteristics.
    -   IOCTL\_SMARTCARD\_GET\_ATTRIBUTE on SCARD\_ATTR\_CHARACTERISTICS

5.  Start the card state monitor.
    -   IOCTL\_SMARTCARD\_IS\_PRESENT – To wait for a smart card arrival.

    -   IOCTL\_SMARTCARD\_IS\_ABSENT – To wait for the smart card departure.

The Power reset is irrelevant since we do not support SCARD\_SWALLOWED, SCARD\_POWERED state.

## Connect sequence


1.  Start of loop.

2.  IOCTL\_SMARTCARD\_GET\_STATE

    -   Case SCARD\_UNKNOWN and SCARD\_ABSENT, do nothing

    -   Case SCARD\_PRESENT, swallow card

    -   Case SCARD\_SWALLOWED, cold reset

    -   Case SCARD\_POWERED, warm reset

    -   Case SCARD\_NEGOTIABLE, determine the card ATR

    -   Case SCARD\_SPECIFIC, determine the card ATR and protocol

3.  IOCTL\_SMARTCARD\_SET\_PROTOCOL

## Disconnect sequence


1.  Power-down timeout starts.

2.  Start of loop.

3.  IOCTL\_SMARTCARD\_GET\_STATE

    -   Case SCARD\_SPECIFIC, SCARD\_NEGOTIABLE, SCARD\_POWERED, set power down

    -   Case SCARD\_SWALLOWED, SCARD\_PRESENT, do nothing

    -   Case SCARD\_ABSENT, SCARD\_UNKNOWN, do nothing

 

 
## Related topics
[NFC device driver interface (DDI) overview](https://msdn.microsoft.com/library/windows/hardware/mt715815)  
[Smart card DDI and command reference](https://msdn.microsoft.com/library/windows/hardware/dn905601)  
