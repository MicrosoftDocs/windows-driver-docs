---
title: UEFI simple I/O protocol
description: UEFI simple I/O protocol
ms.date: 08/20/2021
---

# UEFI simple I/O protocol

> [!NOTE]
> Some information in this section may apply only to Windows 10 Mobile and certain processor architectures.

The simple I/O protocol is used by flashing tools to enable communication between the device and a host computer in the pre-boot environment.

> [!NOTE]
> Information about flashing tools will be provided in a future release of this documentation.

## EFI_SIMPLE_WINPHONE_IO_PROTOCOL

This section provides a detailed description of **EFI_SIMPLE_WINPHONE_IO_PROTOCOL**. This protocol enables simple communication between host and device in a pre-boot environment.

### GUID

```cpp
// {BDE900DD-190A-4c7d-9663-16BA8ED88B55}
#define EFI_SIMPLE_WINPHONE_IO_PROTOCOL_GUID \
  { 0xbde900dd, 0x190a, 0x4c7d, 0x96, 0x63, 0x16, 0xba, 0x8e, \
   0xd8, 0x8b, 0x55 };
```

### Revision number

```cpp
#define EFI_SIMPLE_WINPHONE_IO_PROTOCOL_REVISION   0x00010001
```

### Protocol interface structure

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

**Revision**  
The revision to which the **EFI_SIMPLE_WINPHONE_IO_PROTOCOL** adheres. All future revisions must be backward compatible. If a future version is not backward compatible, a different GUID must be used.

**Initialize**  
This function waits for a connection from the host computer. See [EFI_SIMPLE_WINPHONE_IO_PROTOCOL.Initialize](efi-simple-winphone-io-protocolinitialize.md).

**Read**  
Receives a buffer of bytes from the host computer. See [EFI_SIMPLE_WINPHONE_IO_PROTOCOL.Read](efi-simple-winphone-io-protocolread.md).

**Reserved**
Reserved for future use.

**Write**  
Sends a buffer of bytes to the host computer. See [EFI_SIMPLE_WINPHONE_IO_PROTOCOL.Write](efi-simple-winphone-io-protocolwrite.md).

**GetMaxPacketSize**  
Returns the maximum packet size supported by this protocol. See [EFI_SIMPLE_WINPHONE_IO_PROTOCOL.GetMaxPacketSize](efi-simple-winphone-io-protocolgetmaxpacketsize.md).
