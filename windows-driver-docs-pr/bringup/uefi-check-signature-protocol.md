---
title: UEFI check signature protocol
description: UEFI check signature protocol
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 71df491f-c507-4ca4-831b-50ca95167fb3
---

# UEFI check signature protocol


**Note**  Some information in this section may apply only to Windows 10 Mobile and certain processor architectures.

 

The check signature protocol enables flashing tools to validate the signature on the catalog file in an FFU and verify that the hash of the table of hashes matches the hash specified in the catalog file.

**Note**  Information about the structure of FFU files and flashing tools will be provided in a future release of this documentation.

 

## <a href="" id="efi-checksig-protocol"></a>EFI\_CHECKSIG\_PROTOCOL


This section provides a detailed description of the **EFI\_CHECKSIG\_PROTOCOL**.

**GUID**

``` syntax
// {E52500C3-4BF4-41A5-9692-6DF73DBFB9FE}
#define EFI_CHECKSIG_PROTOCOL_GUID \
  { 0xe52500c3, 0x4bf4, 0x41a5, { 0x96, 0x92, 0x6d, 0xf7, 0x3d, 0xbf, 0xb9, 0xfe } }
```

**Revision number**

``` syntax
#define EFI_SIMPLE_WINPHONE_IO_PROTOCOL_REVISION   0x00000000
```

**Protocol interface structure**

``` syntax
struct _EFI_CHECKSIG_PROTOCOL {
  UINT32 Revision;
  EFI_CHECK_SIG_AND_HASH EfiCheckSignatureAndHash;
};
```

**Members**

<a href="" id="revision"></a>**Revision**  
The revision to which the **EFI\_CHECKSIG\_PROTOCOL** adheres. All future revisions must be backward compatible. If a future version is not backward compatible, a different GUID must be used.

<a href="" id="efichecksignatureandhash"></a>**EfiCheckSignatureAndHash**  
Verifies the signature and hash of the FFU catalog file. See [EFI\_CHECKSIG\_PROTOCOL.EfiCheckSignatureAndHash](efi-checksig-protocolefichecksignatureandhash.md)

## Requirements


**Header:** User generated

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_OEMBringUp\p_oembringup%5D:%20UEFI%20check%20signature%20protocol%20%20RELEASE:%20%284/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


