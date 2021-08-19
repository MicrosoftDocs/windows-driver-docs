---
title: UEFI check signature protocol
description: Provides information about the UEFI check signature protocol.
ms.date: 08/19/2021
ms.localizationpriority: medium
---

# UEFI check signature protocol

> [!NOTE]
> Some information in this section may apply only to Windows 10 Mobile and certain processor architectures.

The check signature protocol enables flashing tools to validate the signature on the catalog file in an FFU and verify that the hash of the table of hashes matches the hash specified in the catalog file.

> [!NOTE]
> Information about the structure of FFU files and flashing tools will be provided in a future release of this documentation.

## EFI_CHECKSIG_PROTOCOL

This section provides a detailed description of the **EFI_CHECKSIG_PROTOCOL**.

### GUID

```cpp
// {E52500C3-4BF4-41A5-9692-6DF73DBFB9FE}
#define EFI_CHECKSIG_PROTOCOL_GUID \
  { 0xe52500c3, 0x4bf4, 0x41a5, { 0x96, 0x92, 0x6d, 0xf7, 0x3d, 0xbf, 0xb9, 0xfe } }
```

### Revision number

```cpp
#define EFI_SIMPLE_WINPHONE_IO_PROTOCOL_REVISION   0x00000000
```

### Protocol interface structure

```cpp
struct _EFI_CHECKSIG_PROTOCOL {
  UINT32 Revision;
  EFI_CHECK_SIG_AND_HASH EfiCheckSignatureAndHash;
};
```

### Members

**Revision**  
The revision to which the **EFI_CHECKSIG_PROTOCOL** adheres. All future revisions must be backward compatible. If a future version is not backward compatible, a different GUID must be used.

**EfiCheckSignatureAndHash**  
Verifies the signature and hash of the FFU catalog file. See [EFI_CHECKSIG_PROTOCOL.EfiCheckSignatureAndHash](efi-checksig-protocolefichecksignatureandhash.md)

## Requirements

**Header:** User generated
