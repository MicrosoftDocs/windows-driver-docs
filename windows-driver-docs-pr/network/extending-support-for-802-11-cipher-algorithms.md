---
title: Extending Support for 802.11 Cipher Algorithms
description: Extending Support for 802.11 Cipher Algorithms
ms.assetid: 2c58e839-f33a-4151-b680-3528ae43922a
keywords:
- extending functionality WDK Native 802.11
- Extensible Station cipher algorithms WDK Native 802.11
- ExtSTA cipher algorithms WDK Native 802.11
- algorithms WDK Native 802.11 cipher
- cipher operations WDK Native 802.11 , extending support
- cipher operations WDK Native 802.11 , cipher algorithms
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Extending Support for 802.11 Cipher Algorithms


**Important**  The [Native 802.11 Wireless LAN](native-802-11-wireless-lan4.md) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](wifi-universal-driver-model.md).

 

The independent hardware vendor (IHV) can use the Extensible Station (ExtSTA) operation mode to extend the types of 802.11 cipher algorithms that are provided by the operating system to include proprietary or non-standard algorithms supported by the IHV.

Windows Vista and later operating systems support the following 802.11 cipher algorithms:

-   IEEE 802.11 Wired Equivalent Privacy (WEP) algorithm.

-   Temporal Key Integrity Protocol (TKIP) algorithm, along with the Michael Message Integrity Code (MIC) algorithm for payload forgery protection. TKIP and Michael are defined in the *Wi-Fi Protected Access (WPA)* specification and IEEE 802.11i-2004 standard.

-   AES-CCMP algorithm, as specified in the IEEE 802.11i-2004 standard and IETF RFC 3610. Advanced Encryption Standard (AES) is the encryption algorithm defined in FIPS PUB 197.

To extend this list for the support of proprietary or non-standard 802.11 cipher algorithms, the miniport driver must assign a unique value within the range of **DOT11\_CIPHER\_ALGO\_IHV\_START** through **DOT11\_CIPHER\_ALGO\_IHV\_END** for each proprietary cipher algorithm that is supported by the 802.11 station.

**Note**  The value assigned to a proprietary cipher algorithm is not a globally unique identifier (GUID). The same value can be used by different Native 802.11 miniport drivers that are developed by the IHV.

 

The miniport driver returns a list of supported cipher algorithms, including supported proprietary algorithms, whenever the following Native 802.11 object identifiers (OIDs) are queried:

<a href="" id="--------oid-dot11-supported-unicast-algorithm-pair"></a>[OID\_DOT11\_SUPPORTED\_UNICAST\_ALGORITHM\_PAIR](https://msdn.microsoft.com/library/windows/hardware/ff569430)  
When this OID is queried, the driver returns the list of 802.11 authentication and cipher algorithms that the 802.11 station supports for unicast packets.

<a href="" id="--------oid-dot11-supported-multicast-algorithm-pair"></a>[OID\_DOT11\_SUPPORTED\_MULTICAST\_ALGORITHM\_PAIR](https://msdn.microsoft.com/library/windows/hardware/ff569424)  
When this OID is queried, the driver returns the list of 802.11 authentication and cipher algorithms that the 802.11 station supports for multicast and broadcast packets.

<a href="" id="--------oid-dot11-enabled-unicast-cipher-algorithm"></a>[OID\_DOT11\_ENABLED\_UNICAST\_CIPHER\_ALGORITHM](https://msdn.microsoft.com/library/windows/hardware/ff569358)  
When this OID is queried, the driver returns the list of 802.11 cipher algorithms that are enabled on the 802.11 station for the encryption and decryption of unicast packets.

<a href="" id="--------oid-dot11-enabled-multicast-cipher-algorithm"></a>[OID\_DOT11\_ENABLED\_MULTICAST\_CIPHER\_ALGORITHM](https://msdn.microsoft.com/library/windows/hardware/ff569357)  
When this OID is queried, the driver returns the list of 802.11 cipher algorithms that are enabled on the 802.11 station for the encryption and decryption of multicast and broadcast packets.

For more information about 802.11 encryption and decryption by Native 802.11 miniport drivers, see [Native 802.11 Cipher Operations](native-802-11-cipher-operations.md).

 

 





