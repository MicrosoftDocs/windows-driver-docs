---
title: Example sequence
ms.assetid: 2B15570A-A220-4BF7-B595-D9CF66E02673
description: 
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnfpdrivers\nfpdrivers%5D:%20Example%20sequence%20%20RELEASE:%20%284/5/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




