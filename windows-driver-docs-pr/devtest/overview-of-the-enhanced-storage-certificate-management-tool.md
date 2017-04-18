---
title: Overview of the Enhanced Storage Certificate Management Tool
description: Overview of the Enhanced Storage Certificate Management Tool
ms.assetid: 963e6510-d62f-421f-9c3d-781092f98969
---

# Overview of the Enhanced Storage Certificate Management Tool


Starting with Windows 7, the operating system provides the *Enhanced Storage* infrastructure for USB storage devices that are connected to a computer. This infrastructure is based on version 1.1 of the IEEE 1667 standard for device authentication and communication. For an overview of the IEEE 1667 standard, see IEEE 1667 Standard Terms and Definitions.

The Enhanced Storage Certificate Management tool manages certificates within the ASC store in USB storage devices that are compliant with the IEEE 1667 standard This tool provides the following functionality:

-   Imports certificates from the host to the ASC store.

    Certificates can be added or replaced (except for the ASCm certificate) in the ASC store of any USB storage devices that are compliant with the IEEE 1667 standard.

    For more information, see [Importing Certificates through the Enhanced Storage Certificate Management Tool](importing-certificates-by-using-the-enhanced-storage-certificate-manag.md).

-   Exports certificates from the ASC store to a file.

    As soon as they are exported, these certificates can be imported to the ASC store on other USB storage devices that are compliant with the IEEE 1667 standard.

-   Removes certificates from the ASC store.

    Individual certificates can be removed from the ASC store, except for the ASCm and PCp certificates.

-   Clears all certificates from the ASC store, except for the ASCm and PCp certificates.

-   Initializes the ASC store back to its initial state.

    This clears all certificates from the ASC store, except for the ASCm certificate.

-   Lists the certificates within the ASC store.

**Note**  You cannot add, delete, or remove the ASCm certificate by using this tool.

 

The Enhanced Storage Certificate Management tool performs these functions by issuing IEEE 1667 commands to an ACT on a USB storage device. Each USB storage device is specified through a unique volume name in the following format:

```
\\?\USB_Hardware_ID{GUID}
```

Where:

-   *USB\_Hardware\_ID* that is the hardware or compatible identifier (ID) of the USB storage device. For more information about these IDs, see [Identifiers for USB Devices](https://msdn.microsoft.com/library/windows/hardware/ff546284).

-   A GUID that represents the device instance.

For example, the following is an example of the volume name for a USB storage device:

```
\\?\usbstor#ieee1667control&ven_&prod_&rev_#123456789&0&control#{4f40006f-b933-4550-b532-2b58cee614d3}
```

**Note**  To produce a list of the volume names of the IEEE 1667-compliant USB storage devices that are currently connected to a computer, type **EhStorCertMgrCmd /List** at the command-line.

 

In order to issue IEEE 1667 commands to an ACT on a USB storage device, the user might need to be authenticated to use the device. Authentication is based on the PCp certificate and private key that is available to the user. If the user does not have the correct PCp certificate and private key, the user will not have access to the device for provisioning through the Enhanced Storage Certificate Management tool.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Overview%20of%20the%20Enhanced%20Storage%20Certificate%20Management%20Tool%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




