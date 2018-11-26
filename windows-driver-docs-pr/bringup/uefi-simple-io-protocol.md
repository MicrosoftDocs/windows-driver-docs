---
title: UEFI simple I/O protocol
description: UEFI simple I/O protocol
ms.assetid: 0cb55bf5-71e9-4b59-aef1-7d74eb331a18
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# UEFI simple I/O protocol


**Note**  Some information in this section may apply only to Windows 10 Mobile and certain processor architectures.

 

The simple I/O protocol is used by flashing tools to enable communication between the device and a host computer in the pre-boot environment.

**Note**  Information about flashing tools will be provided in a future release of this documentation.

 

## EFI\_SIMPLE\_WINPHONE\_IO\_PROTOCOL


This section provides a detailed description of **EFI\_SIMPLE\_WINPHONE\_IO\_PROTOCOL**. This protocol enables simple communication between host and device in a pre-boot environment.

**GUID**

```cpp
// {BDE900DD-190A-4c7d-9663-16BA8ED88B55}
#define EFI_SIMPLE_WINPHONE_IO_PROTOCOL_GUID \
  { 0xbde900dd, 0x190a, 0x4c7d, 0x96, 0x63, 0x16, 0xba, 0x8e, \
   0xd8, 0x8b, 0x55 };
```

**Revision number**

```cpp
#define EFI_SIMPLE_WINPHONE_IO_PROTOCOL_REVISION   0x00010001
```

**Protocol interface structure**

```cpp
typedef struct _EFI_SIMPLE_WINPHONE_IO_PROTOCOL {
  UINT32                                        Revision;
  EFI_SIMPLE_WINPHONE_IO_INITIALIZE             Initialize;
  EFI_SIMPLE_WINPHONE_IO_READ                   Read;
  VOID*                                         Reserved;
  EFI_SIMPLE_WINPHONE_IO_WRITE                  Write;
  EFI_SIMPLE_WINPHONE_IO_GET_MAXPACKET_SIZE     GetMaxPacketSize;
} EFI_SIMPLE_WINPHONE_IO_PROTOCOL;
```

### Members

<a href="" id="revision"></a>**Revision**  
The revision to which the **EFI\_SIMPLE\_WINPHONE\_IO\_PROTOCOL** adheres. All future revisions must be backward compatible. If a future version is not backward compatible, a different GUID must be used.

<a href="" id="initialize"></a>**Initialize**  
This function waits for a connection from the host computer. See [EFI\_SIMPLE\_WINPHONE\_IO\_PROTOCOL.Initialize](efi-simple-winphone-io-protocolinitialize.md).

<a href="" id="read"></a>**Read**  
Receives a buffer of bytes from the host computer. See [EFI\_SIMPLE\_WINPHONE\_IO\_PROTOCOL.Read](efi-simple-winphone-io-protocolread.md).

<a href="" id="reserved-"></a>**Reserved**   
Reserved for future use.

<a href="" id="write"></a>**Write**  
Sends a buffer of bytes to the host computer. See [EFI\_SIMPLE\_WINPHONE\_IO\_PROTOCOL.Write](efi-simple-winphone-io-protocolwrite.md).

<a href="" id="getmaxpacketsize"></a>**GetMaxPacketSize**  
Returns the maximum packet size supported by this protocol. See [EFI\_SIMPLE\_WINPHONE\_IO\_PROTOCOL.GetMaxPacketSize](efi-simple-winphone-io-protocolgetmaxpacketsize.md).

